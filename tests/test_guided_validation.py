"""Keep the expanded inventory on the same strict fresh-kernel execution path."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import nbformat

from scripts import validate_classroom as validator


class GuidedValidationProfileTests(unittest.TestCase):
    def test_default_inventory_is_the_original_eight(self):
        expected = (
            "teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb",
            "notebooks/00_local_statevector_smoke.ipynb",
            "notebooks/01_local_aer_smoke.ipynb",
            "teaching/phys3810-fa2026/notebooks/01_grover.ipynb",
            "teaching/phys3810-fa2026/notebooks/02_qft.ipynb",
            "teaching/phys3810-fa2026/notebooks/03_qpe.ipynb",
            "teaching/phys3810-fa2026/notebooks/04_hhl.ipynb",
            "teaching/phys3810-fa2026/notebooks/05_shor.ipynb",
        )
        self.assertEqual(validator.NOTEBOOKS, expected)
        self.assertEqual(validator.notebooks_for_profile(), expected)

    def test_all_profile_adds_three_without_omitting_references(self):
        expected_guided = (
            "teaching/phys3810-fa2026/notebooks/guided/01_python_and_qiskit.ipynb",
            "teaching/phys3810-fa2026/notebooks/guided/02_grover_follow_along.ipynb",
            "teaching/phys3810-fa2026/notebooks/guided/03_qft_qpe_follow_along.ipynb",
        )
        self.assertEqual(validator.GUIDED_NOTEBOOKS, expected_guided)
        actual = validator.notebooks_for_profile("all")
        self.assertEqual(actual, (*validator.NOTEBOOKS, *expected_guided))
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(len(actual), 11)
        self.assertTrue(all(validator.REQUIRED_PNGS[path] > 0 for path in expected_guided))

    def test_profile_selection_reads_overridden_globals_at_call_time(self):
        with patch.object(validator, "NOTEBOOKS", ("temporary/reference.ipynb",)), \
                patch.object(validator, "GUIDED_NOTEBOOKS", ("temporary/guided.ipynb",)):
            self.assertEqual(validator.notebooks_for_profile(), ("temporary/reference.ipynb",))
            self.assertEqual(validator.notebooks_for_profile("all"),
                             ("temporary/reference.ipynb", "temporary/guided.ipynb"))

    def test_unknown_profile_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown classroom profile"):
            validator.notebooks_for_profile("guided-only")

    def test_main_passes_selected_profile_to_shared_runner(self):
        for arguments, expected in (([], "default"), (["--profile", "all"], "all")):
            with self.subTest(profile=expected), \
                    patch.object(validator, "check_environment") as environment, \
                    patch.object(validator.subprocess, "run", return_value=SimpleNamespace(returncode=0)), \
                    patch.object(validator, "execute_notebooks", return_value=0) as execute, \
                    redirect_stdout(io.StringIO()):
                self.assertEqual(validator.main(arguments), 0)
                environment.assert_called_once_with()
                execute.assert_called_once_with(expected)

    def test_all_profile_real_kernels_keep_strict_failure_and_figure_gates(self):
        # One isolated runner invocation covers the new profile's selection and
        # all strict gates; full notebook/unit acceptance runs separately once.
        with tempfile.TemporaryDirectory(prefix="phys3810 all profile ") as directory:
            root = Path(directory)
            folder = root / "notebooks"
            folder.mkdir()
            inputs = {
                "reference.ipynb": ("assert 6 * 7 == 42", []),
                "guided-success.ipynb": (
                    f"import sys\nassert sys.executable == {sys.executable!r}\nprint('GUIDED_EXECUTED')", []
                ),
                "guided-error.ipynb": (
                    "raise AssertionError('GUIDED_NEGATIVE_CONTROL')", ["raises-exception"]
                ),
                "guided-skip.ipynb": ("raise AssertionError('MUST_EXECUTE')", ["skip-execution"]),
                "guided-no-figure.ipynb": ("print('NO_FIGURE')", []),
            }
            originals = {}
            for name, (source, tags) in inputs.items():
                notebook = nbformat.v4.new_notebook(cells=[
                    nbformat.v4.new_code_cell("print('BEFORE')"),
                    nbformat.v4.new_code_cell(source, metadata={"tags": tags}),
                    nbformat.v4.new_code_cell("print('AFTER')"),
                ])
                path = folder / name
                nbformat.write(notebook, path)
                originals[name] = path.read_bytes()
            command = """
from pathlib import Path
import sys
sys.path.insert(0, sys.argv[1])
from scripts import validate_classroom as runner
runner.ROOT = Path(sys.argv[2])
runner.NOTEBOOKS = ('notebooks/reference.ipynb',)
runner.GUIDED_NOTEBOOKS = (
    'notebooks/guided-success.ipynb', 'notebooks/guided-error.ipynb',
    'notebooks/guided-skip.ipynb', 'notebooks/guided-no-figure.ipynb',
)
runner.REQUIRED_PNGS = {'notebooks/guided-no-figure.ipynb': 1}
raise SystemExit(runner.execute_notebooks('all'))
"""
            result = subprocess.run(
                [sys.executable, "-c", command, str(validator.ROOT), str(root)],
                cwd=root, capture_output=True, text=True, timeout=120, check=False,
            )
            self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
            for name in ("reference.ipynb", "guided-success.ipynb"):
                self.assertIn(f"PASSED: notebooks/{name}", result.stdout)
            for name in ("guided-error.ipynb", "guided-skip.ipynb", "guided-no-figure.ipynb"):
                self.assertIn(f"FAILED: notebooks/{name}", result.stdout)
                self.assertNotIn(f"PASSED: notebooks/{name}", result.stdout)
            self.assertIn("GUIDED_NEGATIVE_CONTROL", result.stdout)
            self.assertIn("skip-execution", result.stdout)
            self.assertIn("must render at least 1 PNG figures; found 0", result.stdout)
            outputs = {}
            for name, original in originals.items():
                self.assertEqual((folder / name).read_bytes(), original)
                output = root / "artifacts" / "executed-classroom" / name
                self.assertTrue(output.exists(), name)
                outputs[name] = nbformat.read(output, as_version=4)
            self.assertEqual([c.execution_count for c in outputs["guided-success.ipynb"].cells], [1, 2, 3])
            self.assertEqual(outputs["guided-error.ipynb"].cells[1].outputs[-1].ename, "AssertionError")
            self.assertIsNone(outputs["guided-error.ipynb"].cells[2].execution_count)
            self.assertTrue(all(c.execution_count is None for c in outputs["guided-skip.ipynb"].cells))
            self.assertEqual([c.execution_count for c in outputs["guided-no-figure.ipynb"].cells], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
