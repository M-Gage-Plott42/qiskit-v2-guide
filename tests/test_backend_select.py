"""Credential configuration tests: temporary dummy values and mocked Runtime only."""

from __future__ import annotations

import os
import tempfile
import unittest
from contextlib import chdir
from pathlib import Path
from unittest.mock import Mock, patch

from src import backend_select
from src.backend_select import MissingCredentialsError, RuntimeConfig, initialize_service


class RuntimeConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.env_path = self.root / ".env"
        environment = patch.dict(os.environ, {}, clear=True)
        environment.start()
        self.addCleanup(environment.stop)

    def write_env(self, contents: str) -> None:
        self.env_path.write_text(contents, encoding="utf-8")

    def test_missing_file_and_variables_return_defaults(self) -> None:
        self.assertEqual(RuntimeConfig.from_env(self.env_path), RuntimeConfig())
        self.assertEqual(dict(os.environ), {})

    def test_reads_dotenv_quotes_comments_without_environment_mutation(self) -> None:
        self.write_env(
            '# These are dummy test values.\n'
            'QISKIT_IBM_TOKEN="dummy-file-token"\n'
            "QISKIT_IBM_INSTANCE='dummy-file-instance' # comment\n"
            'QISKIT_IBM_CHANNEL=ibm_quantum_platform\n'
        )
        self.assertEqual(
            RuntimeConfig.from_env(self.env_path),
            RuntimeConfig(token="dummy-file-token", instance="dummy-file-instance"),
        )
        self.assertEqual(dict(os.environ), {})

    def test_default_path_is_repository_root_even_from_unrelated_directory(self) -> None:
        self.write_env("API_KEY=dummy-token\nINSTANCE=dummy-instance\n")
        unrelated = self.root / "unrelated"
        unrelated.mkdir()
        (unrelated / ".env").write_text("API_KEY=wrong-directory-token\n", encoding="utf-8")
        with patch.object(backend_select, "__file__", str(self.root / "src" / "backend_select.py")):
            with chdir(unrelated):
                config = RuntimeConfig.from_env()
        self.assertEqual(config.token, "dummy-token")
        self.assertEqual(config.instance, "dummy-instance")

    def test_process_legacy_aliases_override_preferred_file_names(self) -> None:
        self.write_env(
            "QISKIT_IBM_TOKEN=dummy-file-token\n"
            "QISKIT_IBM_INSTANCE=dummy-file-instance\n"
            "QISKIT_IBM_CHANNEL=dummy-file-channel\n"
        )
        os.environ.update(API_KEY="dummy-process-token", INSTANCE="dummy-process-instance", CHANNEL="dummy-channel")
        before = dict(os.environ)
        self.assertEqual(
            RuntimeConfig.from_env(self.env_path),
            RuntimeConfig(channel="dummy-channel", token="dummy-process-token", instance="dummy-process-instance"),
        )
        self.assertEqual(dict(os.environ), before)

    def test_preferred_names_win_within_each_source(self) -> None:
        values = {
            "QISKIT_IBM_TOKEN": "dummy-preferred-token",
            "API_KEY": "dummy-legacy-token",
            "IBM_QUANTUM_API_KEY": "dummy-alternate-token",
            "QISKIT_IBM_INSTANCE": "dummy-preferred-instance",
            "INSTANCE": "dummy-legacy-instance",
            "IBM_QUANTUM_INSTANCE": "dummy-alternate-instance",
            "QISKIT_IBM_CHANNEL": "dummy-preferred-channel",
            "CHANNEL": "dummy-legacy-channel",
        }
        expected = RuntimeConfig(
            channel="dummy-preferred-channel", token="dummy-preferred-token", instance="dummy-preferred-instance"
        )
        self.write_env("\n".join(f"{key}={value}" for key, value in values.items()))
        self.assertEqual(RuntimeConfig.from_env(self.env_path), expected)
        self.env_path.unlink()
        os.environ.update(values)
        self.assertEqual(RuntimeConfig.from_env(self.env_path), expected)

    def test_alternate_aliases_are_supported(self) -> None:
        self.write_env("IBM_QUANTUM_API_KEY=dummy-token\nIBM_QUANTUM_INSTANCE=dummy-instance\n")
        expected = RuntimeConfig(token="dummy-token", instance="dummy-instance")
        self.assertEqual(RuntimeConfig.from_env(self.env_path), expected)
        self.env_path.unlink()
        os.environ.update(IBM_QUANTUM_API_KEY="dummy-token", IBM_QUANTUM_INSTANCE="dummy-instance")
        self.assertEqual(RuntimeConfig.from_env(self.env_path), expected)

    def test_blank_values_fall_through_and_nonempty_values_are_trimmed(self) -> None:
        self.write_env('QISKIT_IBM_TOKEN=" dummy-file-token "\nINSTANCE=dummy-instance\n')
        os.environ.update(QISKIT_IBM_TOKEN="  ", API_KEY="", INSTANCE=" dummy-process-instance ")
        self.assertEqual(
            RuntimeConfig.from_env(self.env_path),
            RuntimeConfig(token="dummy-file-token", instance="dummy-process-instance"),
        )

    def test_dotenv_values_are_literal_not_interpolated(self) -> None:
        self.write_env("QISKIT_IBM_TOKEN=dummy-${UNRELATED}\n")
        os.environ["UNRELATED"] = "expanded"
        self.assertEqual(RuntimeConfig.from_env(self.env_path).token, "dummy-${UNRELATED}")

    def test_default_initialization_uses_dotenv_with_mocked_service(self) -> None:
        self.write_env("QISKIT_IBM_TOKEN=dummy-token\nQISKIT_IBM_INSTANCE=dummy-instance\n")
        service_class = Mock()
        with patch.object(backend_select, "__file__", str(self.root / "src" / "backend_select.py")):
            with patch.object(backend_select, "_runtime_service_class", return_value=service_class):
                service = initialize_service()
        self.assertIs(service, service_class.return_value)
        service_class.assert_called_once_with(
            channel="ibm_quantum_platform", token="dummy-token", instance="dummy-instance"
        )


class RuntimeInitializationTests(unittest.TestCase):
    def test_explicit_config_bypasses_dotenv(self) -> None:
        service_class = Mock()
        with patch.object(RuntimeConfig, "from_env", side_effect=AssertionError("must not load .env")):
            with patch.object(backend_select, "_runtime_service_class", return_value=service_class):
                initialize_service(RuntimeConfig(token=" dummy-token ", instance=" dummy-instance "))
        service_class.assert_called_once_with(
            channel="ibm_quantum_platform", token="dummy-token", instance="dummy-instance"
        )

    def test_missing_partial_or_placeholder_credentials_try_saved_account(self) -> None:
        configs = [
            RuntimeConfig(),
            RuntimeConfig(token="dummy-token"),
            RuntimeConfig(token="YOUR_API_KEY", instance="dummy-instance"),
            RuntimeConfig(token="dummy-token", instance="INSTANCE_HERE"),
            RuntimeConfig(token=" ", instance="dummy-instance"),
        ]
        for config in configs:
            with self.subTest(config=config):
                service_class = Mock()
                with patch.object(backend_select, "_runtime_service_class", return_value=service_class):
                    initialize_service(config)
                service_class.assert_called_once_with()

    def test_saved_account_failure_has_actionable_error(self) -> None:
        service_class = Mock(side_effect=RuntimeError("mock saved-account failure"))
        with patch.object(backend_select, "_runtime_service_class", return_value=service_class):
            with self.assertRaisesRegex(MissingCredentialsError, "No usable IBM Runtime credentials"):
                initialize_service(RuntimeConfig())
        service_class.assert_called_once_with()

    def test_invalid_explicit_credentials_do_not_silently_try_saved_account(self) -> None:
        token = "dummy-sensitive-token"
        instance = "dummy-sensitive-instance"
        service_class = Mock(side_effect=RuntimeError(f"mock credential failure: {token} {instance}"))
        with patch.object(backend_select, "_runtime_service_class", return_value=service_class):
            with self.assertRaisesRegex(MissingCredentialsError, "Could not initialize IBM Runtime") as raised:
                initialize_service(RuntimeConfig(token=token, instance=instance))
        message = str(raised.exception)
        for guidance in ("RuntimeConfig", "process environment", "repository-root .env", "take precedence"):
            self.assertIn(guidance, message)
        self.assertNotIn(token, message)
        self.assertNotIn(instance, message)
        service_class.assert_called_once_with(channel="ibm_quantum_platform", token=token, instance=instance)


if __name__ == "__main__":
    unittest.main()
