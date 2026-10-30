"""Run the actual editable QFT notebook cells against independent expectations."""

import ast
from contextlib import redirect_stdout
from importlib.metadata import version
import io
from pathlib import Path
import sys
import unittest

import nbformat
import numpy as np


NOTEBOOK = Path(__file__).resolve().parents[1] / "teaching/phys3810-fa2026/notebooks/02_qft.ipynb"
ATOL = 1e-12


class QFTNotebookExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.cells = {cell.id: cell.source for cell in nbformat.read(NOTEBOOK, as_version=4).cells}

    def setUp(self):
        self.namespace = {"sys": sys, "version": version}
        self.figures = []

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

    def check_case(self, width, label):
        self.execute_cell("qft-imports-parameters", num_qubits=width, basis_label=label)
        self.namespace["display"] = self.figures.append
        self.addCleanup(self.namespace["plt"].close, "all")
        self.execute_cell("qft-matrix-and-circuit")
        phase_output = self.execute_cell("qft-phase-pattern-figure")

        size = 2**width
        index = int(label, 2)
        grid = np.arange(size)
        # Analytic Fourier-column expectation, independent of notebook helpers.
        angles = 2 * np.pi * index * grid / size
        expected = (np.cos(angles) + 1j * np.sin(angles)) / np.sqrt(size)
        transformed = self.namespace["transformed"]
        np.testing.assert_allclose(transformed.data, expected, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.vdot(transformed.data, transformed.data), 1,
                                   rtol=0, atol=ATOL)
        np.testing.assert_allclose(transformed.probabilities(), np.full(size, 1 / size),
                                   rtol=0, atol=ATOL)
        self.assertIn(f"phase ramp for {label}", phase_output)

        axes = self.namespace["axes"]
        self.assertEqual(len(self.figures), 2)
        for line, values in zip(axes[0].lines[:2], (expected.real, expected.imag)):
            np.testing.assert_array_equal(line.get_xdata(), grid)
            np.testing.assert_allclose(line.get_ydata(), values, rtol=0, atol=ATOL)
        np.testing.assert_allclose([bar.get_height() for bar in axes[1].patches],
                                   np.full(size, 1 / size), rtol=0, atol=ATOL)
        np.testing.assert_array_equal(axes[1].get_xticks(), grid)
        self.assertEqual([tick.get_text() for tick in axes[1].get_xticklabels()],
                         [format(j, f"0{width}b") for j in range(size)])
        title = axes[0].get_title()
        for selected in (f"|{label}>", f"k={index}", f"N={size}"):
            self.assertIn(selected, title)
        self.assertNotIn("|011>", title, "The title retained the original three-bit label.")

        inverse_output = self.execute_cell("qft-inverse-and-known-gradient")
        self.assertEqual(self.namespace["counts"], {label: 256})
        expected_basis = np.zeros(size)
        expected_basis[index] = 1
        np.testing.assert_allclose(self.namespace["recovered_basis"].data, expected_basis,
                                   rtol=0, atol=ATOL)
        self.assertIn(f"decodes to {label}", inverse_output)
        self.assertEqual(self.namespace["decoded"].num_clbits, 0)

        self.execute_cell("qft-complex-state-check")
        input_data = self.namespace["input_data"]
        output_state = self.namespace["output_state"]
        # NumPy's inverse DFT has the positive exponent and a 1/N factor.
        expected_complex = np.fft.ifft(input_data) * np.sqrt(size)
        np.testing.assert_allclose(output_state.data, expected_complex, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.vdot(input_data, input_data), 1, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.vdot(output_state.data, output_state.data), 1,
                                   rtol=0, atol=ATOL)
        reversal_output = self.execute_cell("qft-swap-convention-check")
        self.assertIn(f"Bit reversal maps {label} to {label[::-1]}", reversal_output)
        self.assertIn("PASSED", reversal_output)

    def test_three_qubit_low_index(self):
        self.check_case(3, "001")

    def test_three_qubit_reversed_high_index(self):
        self.check_case(3, "110")

    def test_two_qubit_width_change(self):
        self.check_case(2, "01")

    def test_four_qubit_width_change(self):
        self.check_case(4, "0011")


if __name__ == "__main__":
    unittest.main()
