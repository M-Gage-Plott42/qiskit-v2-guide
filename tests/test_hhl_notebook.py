"""Run editable HHL notebook cells against closed, independent fixtures."""

import ast
from contextlib import redirect_stdout
from importlib.metadata import version
import io
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

import nbformat
import numpy as np


NOTEBOOK = Path(__file__).resolve().parents[1] / "teaching/phys3810-fa2026/notebooks/04_hhl.ipynb"
A0 = [[1.5, 0.5], [0.5, 1.5]]


class HHLNotebookExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.cells = {cell.id: cell.source for cell in nbformat.read(NOTEBOOK, as_version=4).cells}

    def setUp(self):
        self.namespace = {"sys": sys, "version": version}
        self.execute_cell("hhl-imports-helpers")
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

    def check_case(self, matrix, rhs, raw_success, raw_failure, probability, observables):
        self.execute_cell("hhl-parameters-circuit", matrix_entries=matrix, rhs_amplitudes=rhs)
        output = self.execute_cell("hhl-raw-state-checks")
        self.assertIn("PASSED", output)
        expected = np.zeros((2, 2, 8), dtype=complex)
        expected[0, :, 0] = raw_failure
        expected[1, :, 0] = raw_success
        np.testing.assert_allclose(self.namespace["joint"], expected, rtol=0, atol=1e-10)
        np.testing.assert_allclose(self.namespace["raw_success"], raw_success, rtol=0, atol=1e-10)
        self.assertAlmostEqual(self.namespace["observed_success"], probability, delta=1e-10)
        conditioned = np.asarray(raw_success) / np.sqrt(probability)
        np.testing.assert_allclose(self.namespace["conditioned_system"], conditioned, rtol=0, atol=1e-9)
        np.testing.assert_allclose(self.namespace["count_leakage"], 0, rtol=0, atol=1e-9)
        for name, value in zip(("X", "Y", "Z"), observables, strict=True):
            self.assertAlmostEqual(self.namespace["expected_observables"][name], value, delta=1e-10)

        self.execute_cell("hhl-state-comparison")
        panels = self.namespace["panels"]
        self.assertEqual(len(self.figures), 2)
        for panel, component in zip(panels[:2], (np.real, np.imag), strict=True):
            self.assertEqual(panel.get_ylim(), (-1.05, 1.05))
            heights = [bar.get_height() for bar in panel.patches]
            np.testing.assert_allclose(heights[:2], component(conditioned), rtol=0, atol=1e-9)
            np.testing.assert_allclose(heights[2:], component(conditioned), rtol=0, atol=1e-9)
        np.testing.assert_allclose([bar.get_height() for bar in panels[2].patches],
                                   [1-probability, probability] * 2, rtol=0, atol=1e-10)
        self.assertIn(f"{probability:.4f}", panels[2].get_title())

        output = self.execute_cell("hhl-postselected-sampling")
        self.assertIn("PASSED", output)
        self.assertEqual(len(self.figures), 3)
        self.assertEqual(self.namespace["circuit"].num_clbits, 0)
        shots = 4096
        for basis, expected_mean, result in zip(("X", "Y", "Z"), observables,
                                               self.namespace["results"], strict=True):
            # Reconstruct the selection directly from paired shot records; a
            # product of marginal frequencies cannot satisfy this assertion.
            bits = result.data.system_readout.get_bitstrings()
            flags = result.data.success_readout.get_bitstrings()
            selected = [int(bits[index]) for index in range(shots) if flags[index] == "1"]
            summary = self.namespace["sampling_summary"][basis]
            self.assertEqual(summary["selected"], len(selected))
            self.assertGreater(len(selected), 0)
            self.assertEqual(summary["mean"], float(np.mean(1-2*np.asarray(selected))))
            success_bound = 6*np.sqrt(probability*max(0, 1-probability)/shots) + 1/shots
            self.assertLessEqual(abs(len(selected)/shots-probability), success_bound)
            conditional_bound = 6*np.sqrt(max(0, 1-expected_mean**2)/len(selected)) + 2/len(selected)
            self.assertLessEqual(abs(summary["mean"]-expected_mean), conditional_bound)
        np.testing.assert_allclose(self.namespace["axes"].lines[0].get_ydata(), observables,
                                   rtol=0, atol=1e-10)

    def test_default_sign_and_probability(self):
        self.check_case(A0, [1, 0], [0.75, -0.25], [np.sqrt(3)/4]*2,
                        5/8, [-3/5, 0, 4/5])

    def test_other_basis_input(self):
        self.check_case(A0, [0, 1], [-0.25, 0.75], [np.sqrt(3)/4]*2,
                        5/8, [-3/5, 0, -4/5])

    def test_plus_eigenstate(self):
        self.check_case(A0, [1/np.sqrt(2)]*2, [1/np.sqrt(8)]*2,
                        [np.sqrt(3/8)]*2, 1/4, [1, 0, 0])

    def test_minus_eigenstate_with_zero_failure(self):
        rhs = [1/np.sqrt(2), -1/np.sqrt(2)]
        self.check_case(A0, rhs, rhs, [0, 0], 1, [-1, 0, 0])

    def test_complex_relative_phase(self):
        self.check_case(A0, [1/np.sqrt(2), 1j/np.sqrt(2)],
                        [(3-1j)/(4*np.sqrt(2)), (-1+3j)/(4*np.sqrt(2))],
                        [np.sqrt(3)*(1+1j)/(4*np.sqrt(2))]*2,
                        5/8, [-3/5, 4/5, 0])

    def test_absolute_matrix_scale_changes_success(self):
        failure = [(np.sqrt(15)+2*np.sqrt(3))/8, (np.sqrt(15)-2*np.sqrt(3))/8]
        self.check_case([[3, 1], [1, 3]], [1, 0], [3/8, -1/8], failure,
                        5/32, [-3/5, 0, 4/5])

    def test_upper_spectrum_boundary(self):
        self.check_case([[7, 0], [0, 7]], [1, 0], [1/7, 0], [np.sqrt(48)/7, 0],
                        1/49, [0, 0, 1])

    def test_empty_selected_sample_reports_undefined_mean_and_fails_statistics(self):
        self.execute_cell("hhl-parameters-circuit")
        self.execute_cell("hhl-raw-state-checks")
        zero_bits = SimpleNamespace(get_bitstrings=lambda: ["0"]*4096)
        result = SimpleNamespace(data=SimpleNamespace(system_readout=zero_bits,
                                                      success_readout=zero_bits))
        job = SimpleNamespace(result=lambda: [result]*3)
        sampler = SimpleNamespace(run=lambda circuits, shots: job)
        self.namespace["StatevectorSampler"] = lambda seed: sampler
        with self.assertRaisesRegex(AssertionError, "conditioned mean is undefined"):
            self.execute_cell("hhl-postselected-sampling")
        self.assertEqual(self.namespace["sampling_summary"]["X"]["selected"], 0)
        self.assertIsNone(self.namespace["sampling_summary"]["X"]["mean"])

    def test_shot_alignment_and_empty_selection(self):
        select = self.namespace["selected_system_bits"]
        np.testing.assert_array_equal(select(["0", "1", "1", "0"], ["0", "1", "0", "1"]), [1, 0])
        self.assertEqual(select(["0", "1"], ["0", "0"]).size, 0)
        with self.assertRaisesRegex(ValueError, "matching shot counts"):
            select(["0"], ["0", "1"])
        self.assertIn("PASSED", self.execute_cell("hhl-invalid-input-demo"))


if __name__ == "__main__":
    unittest.main()
