"""Exercise the actual QPE notebook cells with different student parameters."""

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


NOTEBOOK = Path(__file__).resolve().parents[1] / "teaching/phys3810-fa2026/notebooks/03_qpe.ipynb"


class QPENotebookExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.cells = {cell.id: cell.source for cell in nbformat.read(NOTEBOOK, as_version=4).cells}

    def setUp(self):
        self.namespace = {"sys": sys, "version": version}
        with redirect_stdout(io.StringIO()):
            exec(compile(self.cells["qpe-imports-helpers"], "qpe-imports-helpers", "exec"), self.namespace)
        self.figures = []
        self.namespace["display"] = self.figures.append
        self.addCleanup(self.namespace["plt"].close, "all")

    def execute_cell(self, cell_id, **parameters):
        tree = ast.parse(self.cells[cell_id])
        changed = set()
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in parameters:
                        node.value = ast.parse(repr(parameters[target.id]), mode="eval").body
                        changed.add(target.id)
        self.assertEqual(changed, set(parameters), "An editable notebook parameter disappeared.")
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compile(ast.fix_missing_locations(tree), cell_id, "exec"), self.namespace)
        return output.getvalue()

    def test_exact_phase_and_width_variations(self):
        for width, phi, label in [(3, 1 / 8, "001"), (3, 6 / 8, "110"), (4, 3 / 16, "0011")]:
            with self.subTest(width=width, phi=phi):
                self.execute_cell("qpe-exact-example", num_counting_qubits=width, exact_phase=phi)
                output = self.execute_cell("qpe-exact-sampling")
                self.assertEqual(self.namespace["exact_counts"], {label: 2048})
                self.assertIn(label, output)
                self.assertIn(label, self.namespace["axes"].get_title())

    def test_exact_section_rejects_non_grid_phase(self):
        with self.assertRaisesRegex(AssertionError, "exact grid phase"):
            self.execute_cell("qpe-exact-example", num_counting_qubits=3, exact_phase=1 / 3)

    def test_nonexact_phase_and_precision_variation(self):
        output = self.execute_cell("qpe-nonexact-distributions", nonexact_phase=0.31, precision_bits=(2, 4))
        self.assertIn("m=2", output)
        self.assertIn("m=4", output)
        for width, panel in zip((2, 4), self.namespace["panels"]):
            size = 2**width
            delta = 0.31 - np.arange(size) / size
            expected = (np.sin(np.pi * size * delta) / (size * np.sin(np.pi * delta)))**2
            np.testing.assert_allclose(self.namespace["nonexact_probabilities"][width], expected,
                                       rtol=0, atol=2e-11)
            np.testing.assert_allclose(panel.lines[0].get_ydata(), expected, rtol=0, atol=2e-11)
            self.assertIn(f"m={width}", panel.get_title())
        self.assertIn("PASSED", self.execute_cell("qpe-precision-report"))

    def test_precision_exercise_requires_two_distinct_widths(self):
        for widths in [(3,), (3, 3), (2, 3, 4)]:
            with self.subTest(widths=widths), self.assertRaisesRegex(AssertionError, "two distinct"):
                self.execute_cell("qpe-nonexact-distributions", precision_bits=widths)

    def test_sdk_check_follows_changed_parameters(self):
        self.execute_cell("qpe-exact-example", num_counting_qubits=4, exact_phase=3 / 16)
        output = self.execute_cell("qpe-sdk-reference")
        self.assertIn("1100", output)
        self.assertIn("0011", output)
        np.testing.assert_allclose(Operator(self.namespace["reference"]).data,
                                   Operator(self.namespace["qpe_block"]).data, rtol=0, atol=2e-11)


if __name__ == "__main__":
    unittest.main()
