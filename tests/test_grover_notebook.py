"""Execute the actual editable Grover exercise cells with student variations."""

import ast
from contextlib import redirect_stdout
from importlib.metadata import version
import io
from pathlib import Path
import sys
import unittest

import nbformat
import numpy as np
from qiskit.quantum_info import Operator


NOTEBOOK = Path(__file__).resolve().parents[1] / "teaching/phys3810-fa2026/notebooks/01_grover.ipynb"


class GroverNotebookExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.cells = {cell.id: cell.source for cell in nbformat.read(NOTEBOOK, as_version=4).cells}

    def setUp(self):
        # Use the notebook's own imports and analysis helpers, without running
        # its IPython path-setup magic. The actual exercise body is not copied.
        self.namespace = {"sys": sys, "version": version}
        with redirect_stdout(io.StringIO()):
            exec(compile(self.cells["grover-imports"], "grover-imports", "exec"), self.namespace)
        self.figures = []
        self.namespace["display"] = self.figures.append
        self.addCleanup(self.namespace["plt"].close, "all")

    def execute_cell(self, cell_id, **parameters):
        tree = ast.parse(self.cells[cell_id])
        replaced = set()
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in parameters:
                        node.value = ast.parse(repr(parameters[target.id]), mode="eval").body
                        replaced.add(target.id)
        self.assertEqual(replaced, set(parameters), "The notebook's editable parameter disappeared.")
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compile(ast.fix_missing_locations(tree), cell_id, "exec"), self.namespace)
        return output.getvalue()

    def check_pair(self, targets):
        output = self.execute_cell("grover-multiple-target-check", multiple_targets=targets)
        expected_signs = np.ones(8)
        expected_probabilities = np.zeros(8)
        for target in targets:
            expected_signs[int(target, 2)] = -1
            expected_probabilities[int(target, 2)] = 0.5
            self.assertIn(target, output)
        for unselected in {"001", "011"} - set(targets):
            self.assertNotIn(unselected, output, "A success message retained an old target label.")
        self.assertIn("PASSED", output)
        np.testing.assert_allclose(
            Operator(self.namespace["multiple_oracle"]).data,
            np.diag(expected_signs), rtol=0, atol=1e-12,
        )
        np.testing.assert_allclose(
            self.namespace["multiple_probabilities"], expected_probabilities, rtol=0, atol=1e-12
        )

    def test_original_multiple_target_pair(self):
        self.check_pair(("001", "011"))

    def test_pair_with_changed_second_index(self):
        self.check_pair(("001", "101"))

    def test_pair_with_both_indices_changed(self):
        self.check_pair(("010", "111"))

    def test_multiple_target_exercise_requires_exactly_two_targets(self):
        for targets in (("001",), ("001", "011", "101")):
            with self.subTest(targets=targets):
                with self.assertRaisesRegex(AssertionError, "exactly two targets"):
                    self.execute_cell("grover-multiple-target-check", multiple_targets=targets)

    def test_iteration_curve_labels_the_actual_marked_count(self):
        examples = [(3, ("001", "101"), "tab:blue"), (3, ("010",), "tab:orange")]
        output = self.execute_cell("grover-iteration-curve", plot_examples=examples)
        self.assertIn("PASSED", output)
        self.assertEqual(len(self.figures), 1)
        axes = self.namespace["axes"]
        labels = axes.get_legend_handles_labels()[1]
        self.assertIn("N=8, M=2: formula", labels)
        self.assertIn("N=8, M=2: circuit", labels)
        self.assertIn("N=8, M=1: formula", labels)
        self.assertIn("N=8, M=1: circuit", labels)
        # Check the varying-M data independently, not only the legend text.
        iterations = np.arange(8)
        theta = np.arcsin(np.sqrt(2 / 8))
        expected = np.sin((2 * iterations + 1) * theta) ** 2
        np.testing.assert_allclose(axes.lines[0].get_ydata(), expected, rtol=0, atol=1e-12)
        circuit_offsets = axes.collections[0].get_offsets()
        np.testing.assert_allclose(circuit_offsets[:, 1], expected, rtol=0, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
