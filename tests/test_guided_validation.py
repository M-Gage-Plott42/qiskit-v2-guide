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

    def test_all_profile_adds_three_guided_and_two_intro_without_omitting_references(self):
        expected_guided = (
            "teaching/phys3810-fa2026/notebooks/guided/01_python_and_qiskit.ipynb",
            "teaching/phys3810-fa2026/notebooks/guided/02_grover_follow_along.ipynb",
            "teaching/phys3810-fa2026/notebooks/guided/03_qft_qpe_follow_along.ipynb",
        )
        expected_intro = (
            "teaching/phys3810-fa2026/notebooks/intro/01_quantum_rng.ipynb",
            "teaching/phys3810-fa2026/notebooks/intro/02_bell_state.ipynb",
        )
        self.assertEqual(validator.GUIDED_NOTEBOOKS, expected_guided)
        self.assertEqual(validator.INTRO_NOTEBOOKS, expected_intro)
        actual = validator.notebooks_for_profile("all")
        self.assertEqual(actual, (*validator.NOTEBOOKS, *expected_guided, *expected_intro))
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(len(actual), 13)
        self.assertTrue(all(validator.REQUIRED_PNGS[path] > 0 for path in (*expected_guided, *expected_intro)))
        self.assertEqual(tuple(validator.REQUIRED_PNGS[path] for path in expected_intro), (2, 3))

    def test_profile_selection_reads_overridden_globals_at_call_time(self):
        with patch.object(validator, "NOTEBOOKS", ("temporary/reference.ipynb",)), \
                patch.object(validator, "GUIDED_NOTEBOOKS", ("temporary/guided.ipynb",)), \
                patch.object(validator, "INTRO_NOTEBOOKS", ("temporary/intro.ipynb",)):
            self.assertEqual(validator.notebooks_for_profile(), ("temporary/reference.ipynb",))
            self.assertEqual(validator.notebooks_for_profile("all"),
                             ("temporary/reference.ipynb", "temporary/guided.ipynb", "temporary/intro.ipynb"))

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
            inputs = {"reference.ipynb": ("assert 6 * 7 == 42", [])}
            for route in ("guided", "intro"):
                inputs.update({
                    f"{route}-success.ipynb": (
                        f"import sys\nassert sys.executable == {sys.executable!r}\n"
                        "assert 'previous_route' not in globals()\nprevious_route = True", []
                    ),
                    f"{route}-error.ipynb": (
                        f"raise AssertionError('{route.upper()}_NEGATIVE_CONTROL')", ["raises-exception"]
                    ),
                    f"{route}-skip.ipynb": ("raise AssertionError('MUST_EXECUTE')", ["skip-execution"]),
                    f"{route}-no-figure.ipynb": ("print('NO_FIGURE')", []),
                })
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
runner.INTRO_NOTEBOOKS = (
    'notebooks/intro-success.ipynb', 'notebooks/intro-error.ipynb',
    'notebooks/intro-skip.ipynb', 'notebooks/intro-no-figure.ipynb',
)
runner.REQUIRED_PNGS = {
    'notebooks/guided-no-figure.ipynb': 1, 'notebooks/intro-no-figure.ipynb': 1,
}
raise SystemExit(runner.execute_notebooks('all'))
"""
            result = subprocess.run(
                [sys.executable, "-c", command, str(validator.ROOT), str(root)],
                cwd=root, capture_output=True, text=True, timeout=180, check=False,
            )
            self.assertEqual(result.returncode, 6, result.stdout + result.stderr)
            for name in ("reference.ipynb", "guided-success.ipynb", "intro-success.ipynb"):
                self.assertIn(f"PASSED: notebooks/{name}", result.stdout)
            for route in ("guided", "intro"):
                for suffix in ("error", "skip", "no-figure"):
                    name = f"{route}-{suffix}.ipynb"
                    self.assertIn(f"FAILED: notebooks/{name}", result.stdout)
                    self.assertNotIn(f"PASSED: notebooks/{name}", result.stdout)
                self.assertIn(f"{route.upper()}_NEGATIVE_CONTROL", result.stdout)
            self.assertIn("skip-execution", result.stdout)
            self.assertIn("must render at least 1 PNG figures; found 0", result.stdout)
            outputs = {}
            for name, original in originals.items():
                self.assertEqual((folder / name).read_bytes(), original)
                output = root / "artifacts" / "executed-classroom" / name
                self.assertTrue(output.exists(), name)
                outputs[name] = nbformat.read(output, as_version=4)
            for route in ("guided", "intro"):
                success = outputs[f"{route}-success.ipynb"].cells
                error = outputs[f"{route}-error.ipynb"].cells
                skipped = outputs[f"{route}-skip.ipynb"].cells
                no_figure = outputs[f"{route}-no-figure.ipynb"].cells
                self.assertEqual([c.execution_count for c in success], [1, 2, 3])
                self.assertEqual(error[1].outputs[-1].ename, "AssertionError")
                self.assertIsNone(error[2].execution_count)
                self.assertTrue(all(c.execution_count is None for c in skipped))
                self.assertEqual([c.execution_count for c in no_figure], [1, 2, 3])

    def test_intro_cells_cannot_pass_without_execution_counts_or_with_errors(self):
        for cell_id in ("intro-rng-sample", "intro-bell-x-basis"):
            with self.subTest(cell_id=cell_id):
                cell = nbformat.v4.new_code_cell("assert True", id=cell_id)
                notebook = nbformat.v4.new_notebook(cells=[cell])
                with self.assertRaisesRegex(RuntimeError, "no execution count"):
                    validator.validate_required_cells(notebook, executed=True)
                cell.execution_count = 1
                cell.outputs = [nbformat.v4.new_output(
                    "error", ename="AssertionError", evalue="", traceback=[]
                )]
                with self.assertRaisesRegex(RuntimeError, "retains an error output"):
                    validator.validate_required_cells(notebook, executed=True)


if __name__ == "__main__":
    unittest.main()
