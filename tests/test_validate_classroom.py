"""Regression checks for required-notebook execution, including real kernels."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import nbformat

from scripts import validate_classroom as validator


class RequiredNotebookExecutionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="phys3810 required notebook ")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.relative = "notebooks/required.ipynb"
        self.path = self.root / self.relative
        self.path.parent.mkdir()

    def run_notebook(self, source, *, tags=(), required_pngs=None):
        notebook = nbformat.v4.new_notebook(cells=[
            nbformat.v4.new_code_cell('print("BEFORE")'),
            nbformat.v4.new_code_cell(source, metadata={"tags": list(tags)}),
            nbformat.v4.new_code_cell('print("AFTER")'),
            # Empty cells are not required code, even if they carry a skip tag.
            nbformat.v4.new_code_cell("  \n", metadata={"tags": ["skip-execution"]}),
        ])
        nbformat.write(notebook, self.path)
        original = self.path.read_bytes()
        # Run the actual execution gate from a directory with spaces and no Git.
        # Calling execute_notebooks avoids recursively running unittest discovery.
        command = """
from pathlib import Path
import sys
sys.path.insert(0, sys.argv[1])
from scripts import validate_classroom as runner
runner.ROOT = Path(sys.argv[2])
runner.NOTEBOOKS = (sys.argv[3],)
if sys.argv[4]:
    runner.REQUIRED_PNGS[sys.argv[3]] = int(sys.argv[4])
raise SystemExit(runner.execute_notebooks())
"""
        result = subprocess.run(
            [sys.executable, "-c", command, str(validator.ROOT), str(self.root), self.relative,
             "" if required_pngs is None else str(required_pngs)],
            cwd=self.root, capture_output=True, text=True, timeout=90, check=False,
        )
        self.assertEqual(self.path.read_bytes(), original, "Source notebook was modified.")
        output = self.root / "artifacts" / "executed-classroom" / self.path.name
        self.assertTrue(output.exists(), result.stdout + result.stderr)
        return result, nbformat.read(output, as_version=4)

    def assert_failed(self, result):
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"FAILED: {self.relative}:", result.stdout)
        self.assertNotIn(f"PASSED: {self.relative}", result.stdout)

    def test_successful_notebook_executes_all_nonempty_code(self):
        result, notebook = self.run_notebook('assert 6 * 7 == 42\nprint("EXECUTED")')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"PASSED: {self.relative}", result.stdout)
        self.assertEqual([cell.execution_count for cell in notebook.cells], [1, 2, 3, None])
        self.assertIn("EXECUTED", notebook.cells[1].outputs[0].text)
        self.assertFalse(any(item.output_type == "error" for cell in notebook.cells for item in cell.outputs))

    def check_failing_cell(self, tags):
        result, notebook = self.run_notebook(
            'raise AssertionError("M1_REVIEW_NEGATIVE_CONTROL")', tags=tags
        )
        self.assert_failed(result)
        self.assertIn("M1_REVIEW_NEGATIVE_CONTROL", result.stdout)
        self.assertEqual(notebook.cells[0].execution_count, 1)
        self.assertEqual(notebook.cells[1].outputs[-1].ename, "AssertionError")
        # force_raise_errors must stop even when raises-exception is present.
        self.assertIsNone(notebook.cells[2].execution_count)

    def test_ordinary_error_fails_and_preserves_partial_output(self):
        self.check_failing_cell(())

    def test_raises_exception_tag_cannot_hide_a_failure(self):
        self.check_failing_cell(("raises-exception",))

    def test_skip_execution_tag_is_rejected_for_nonempty_code(self):
        result, notebook = self.run_notebook(
            'raise AssertionError("MUST_NOT_BE_SILENTLY_SKIPPED")', tags=("skip-execution",)
        )
        self.assert_failed(result)
        self.assertIn("Required code cell 2", result.stdout)
        self.assertIn("skip-execution", result.stdout)
        self.assertIn("Remove that tag", result.stdout)
        self.assertTrue(all(cell.execution_count is None for cell in notebook.cells))

    @staticmethod
    def figure_source(count):
        return f"""%matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import display
for number in range({count}):
    figure, axes = plt.subplots()
    axes.plot([0, 1], [number, number + 1])
    display(figure)
    plt.close(figure)
"""

    def test_two_of_three_pngs_fail_and_preserve_executed_output(self):
        minimum = validator.REQUIRED_PNGS[validator.HHL_NOTEBOOK]
        self.assertEqual(minimum, 3)
        result, notebook = self.run_notebook(self.figure_source(2), required_pngs=minimum)
        self.assert_failed(result)
        self.assertIn("must render at least 3 PNG figures; found 2", result.stdout)
        self.assertEqual([cell.execution_count for cell in notebook.cells], [1, 2, 3, None])
        self.assertEqual(sum("image/png" in item.get("data", {})
                             for cell in notebook.cells for item in cell.outputs), 2)
        self.assertIn("AFTER", notebook.cells[2].outputs[0].text)

    def test_three_pngs_meet_required_figure_gate(self):
        minimum = validator.REQUIRED_PNGS[validator.SHOR_NOTEBOOK]
        self.assertEqual(minimum, 3)
        result, notebook = self.run_notebook(self.figure_source(3), required_pngs=minimum)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"PASSED: {self.relative}", result.stdout)
        self.assertEqual([cell.execution_count for cell in notebook.cells], [1, 2, 3, None])
        self.assertEqual(sum("image/png" in item.get("data", {})
                             for cell in notebook.cells for item in cell.outputs), 3)


class RequiredNotebookCompletionTests(unittest.TestCase):
    def test_missing_execution_count_is_rejected(self):
        notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell("assert True")])
        with self.assertRaisesRegex(RuntimeError, "cell 1 has no execution count"):
            validator.validate_required_cells(notebook, executed=True)

    def test_error_output_is_rejected_despite_execution_count(self):
        cell = nbformat.v4.new_code_cell("assert False", execution_count=1)
        cell.outputs = [nbformat.v4.new_output(
            "error", ename="AssertionError", evalue="failed", traceback=[]
        )]
        notebook = nbformat.v4.new_notebook(cells=[cell])
        with self.assertRaisesRegex(RuntimeError, "cell 1 retains an error output"):
            validator.validate_required_cells(notebook, executed=True)


if __name__ == "__main__":
    unittest.main()
