"""Execute the actual Shor teaching cells with independent finite fixtures."""

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


NOTEBOOK = Path(__file__).resolve().parents[1] / "teaching/phys3810-fa2026/notebooks/05_shor.ipynb"


class ShorNotebookExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.cells = {c.id: c.source for c in nbformat.read(NOTEBOOK, as_version=4).cells}

    def setUp(self):
        self.namespace = {"sys": sys, "version": version}
        self.execute_cell("shor-imports-helpers")
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
        self.assertEqual(changed, set(parameters), "An editable parameter disappeared.")
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compile(ast.fix_missing_locations(tree), cell_id, "exec"), self.namespace)
        return output.getvalue()

    def check_case(self, base, width, orbit):
        order, size = len(orbit), 2**width
        self.execute_cell("shor-parameters-circuit", base=base, num_counting_qubits=width)
        self.assertIn("PASSED", self.execute_cell("shor-joint-checks"))
        # Closed exact-orbit amplitudes: r distinct residue states, r phase bins.
        expected = np.zeros((16, size), dtype=complex)
        for position, residue in enumerate(orbit):
            for y in range(0, size, size//order):
                angle = -2*np.pi*position*y/size
                expected[residue, y] = (np.cos(angle)+1j*np.sin(angle))/order
        np.testing.assert_allclose(self.namespace["actual_joint"], expected, rtol=0, atol=2e-11)
        probabilities = np.zeros(size)
        probabilities[::size//order] = 1/order
        np.testing.assert_allclose(self.namespace["expected_probabilities"], probabilities, rtol=0, atol=2e-11)
        output = self.execute_cell("shor-sampling-recovery")
        self.assertIn("PASSED", output)
        trial = self.namespace["trial"]
        self.assertEqual(sum(trial["counts"].values()), 2048)
        expected_order_shots = expected_factor_shots = 0
        for bits, count, fraction, recovered, factors in trial["rows"]:
            y = int(bits, 2)
            self.assertEqual(fraction, self.namespace["Fraction"](y, size))
            # Known fixture orders, not calls back into production recovery.
            expected_order = order if y and fraction.denominator == order else None
            expected_factors = (3, 5) if expected_order and base not in (1, 14) else None
            self.assertEqual(recovered, expected_order)
            self.assertEqual(factors, expected_factors)
            expected_order_shots += count if expected_order else 0
            expected_factor_shots += count if expected_factors else 0
        self.assertEqual(trial["order_shots"], expected_order_shots)
        self.assertEqual(trial["factor_shots"], expected_factor_shots)
        expected_order_probability = 0.0 if order == 1 else 0.5
        expected_factor_probability = 0.0 if base in (1, 14) else 0.5
        self.assertEqual(self.namespace["theory_order"], expected_order_probability)
        self.assertEqual(self.namespace["theory_factors"], expected_factor_probability)
        self.assertIn(f"Order recovery: {expected_order_shots}/2048 "
                      f"(theory per shot {expected_order_probability:.3f})", output)
        self.assertIn(f"factors: {expected_factor_shots}/2048 "
                      f"(theory per shot {expected_factor_probability:.3f})", output)
        if not expected_factor_shots:
            self.assertIn("no factors", output)
        axes = self.namespace["axes"]
        self.assertIn(f"base={base}, m={width}", axes.get_title())
        np.testing.assert_allclose(axes.lines[0].get_ydata(), probabilities, rtol=0, atol=2e-11)
        expected_bars = [trial["counts"].get(format(y, f"0{width}b"), 0)/2048 for y in range(size)]
        np.testing.assert_allclose([p.get_height() for p in axes.patches], expected_bars, rtol=0, atol=2e-11)
        ticks = np.arange(0, size, max(1, size//16))
        self.assertEqual([t.get_text() for t in axes.get_xticklabels()],
                         [format(y, f"0{width}b") for y in ticks])
        self.assertEqual(len(self.figures), 2)

    def test_default_base_two(self):
        # Literal independent finite fixtures cover every supported teaching base.
        expected = {1: (0.0, 0.0), 2: (0.5, 0.5), 4: (0.5, 0.5),
                    7: (0.5, 0.5), 8: (0.5, 0.5), 11: (0.5, 0.5),
                    13: (0.5, 0.5), 14: (0.5, 0.0)}
        for base, probabilities in expected.items():
            with self.subTest(base=base):
                self.assertEqual(self.namespace["theoretical_trial_probabilities"](base), probabilities)
        self.check_case(2, 4, [1, 2, 4, 8])

    def test_different_orbit_and_width_five(self):
        self.check_case(7, 5, [1, 7, 4, 13])

    def test_upper_width_six(self):
        self.check_case(8, 6, [1, 8, 4, 2])

    def test_identity_is_an_honest_unproductive_trial(self):
        self.check_case(1, 4, [1])
        self.assertEqual(self.namespace["trial"]["order_shots"], 0)

    def test_order_two_yields_factors(self):
        self.check_case(11, 5, [1, 11])

    def test_order_two_with_trivial_root_yields_no_factors(self):
        self.check_case(14, 6, [1, 14])
        self.assertGreater(self.namespace["trial"]["order_shots"], 0)
        self.assertEqual(self.namespace["trial"]["factor_shots"], 0)

    def test_expansion_finite_budget_and_separate_success_metrics(self):
        self.check_case(2, 4, [1, 2, 4, 8])
        output = self.execute_cell("shor-expansion-batches")
        summaries = self.namespace["expansion_results"]
        self.assertEqual(set(summaries), {11, 14})
        self.assertEqual(self.namespace["trial"]["shots"]+sum(s["shots"] for s in summaries.values()), 6144)
        for base in (11, 14):
            self.assertEqual(summaries[base]["order_shots"], summaries[base]["counts"].get("1000", 0))
            self.assertGreater(summaries[base]["order_shots"], 0)
        self.assertEqual(summaries[11]["factor_shots"], summaries[11]["order_shots"])
        self.assertEqual(summaries[14]["factor_shots"], 0)
        self.assertEqual(self.namespace["expansion_theory"], {11: (0.5, 0.5), 14: (0.5, 0.0)})
        for base, factor_probability in ((11, 0.5), (14, 0.0)):
            self.assertIn(f"base={base}: order recovery {summaries[base]['order_shots']}/2048 "
                          "(theory per shot 0.500)", output)
            self.assertIn(f"factors {summaries[base]['factor_shots']}/2048 "
                          f"(theory per shot {factor_probability:.3f})", output)
        heights = [p.get_height() for p in self.namespace["axes"].patches]
        np.testing.assert_allclose(heights, [summaries[11]["order_shots"]/2048,
            summaries[14]["order_shots"]/2048, summaries[11]["order_shots"]/2048, 0], rtol=0, atol=2e-11)
        np.testing.assert_allclose(self.namespace["axes"].lines[0].get_ydata(), [0.5, 0.5], rtol=0, atol=0)
        np.testing.assert_allclose(self.namespace["axes"].lines[1].get_ydata(), [0.5, 0.0], rtol=0, atol=0)
        np.testing.assert_allclose(self.namespace["axes"].lines[0].get_xdata(), [-0.18, 0.82], rtol=0, atol=1e-15)
        np.testing.assert_allclose(self.namespace["axes"].lines[1].get_xdata(), [0.18, 1.18], rtol=0, atol=1e-15)
        self.assertEqual(len(self.figures), 3)

    def test_classical_failures_and_synthesis_diagnostic(self):
        self.check_case(2, 4, [1, 2, 4, 8])
        self.assertIn("PASSED", self.execute_cell("shor-classical-failures"))
        self.assertIn("PASSED", self.execute_cell("shor-resource-diagnostic"))
        self.assertEqual(self.namespace["resource_counts"]["qubits"], 8)
        self.assertTrue(set(self.namespace["resource_counts"]["operations"]) <= {"u", "cx"})

    def test_unexpected_or_missing_sample_bins_fail_actual_cell(self):
        self.execute_cell("shor-parameters-circuit")
        self.execute_cell("shor-joint-checks")
        for counts in ({"0001": 2048}, {}, {"0000": 2048}):
            bits = SimpleNamespace(get_counts=lambda: counts)
            result = SimpleNamespace(data=SimpleNamespace(phase=bits))
            sampler = SimpleNamespace(run=lambda circuits, shots: SimpleNamespace(result=lambda: [result]))
            self.namespace["StatevectorSampler"] = lambda seed: sampler
            with self.subTest(counts=counts), self.assertRaises(AssertionError):
                self.execute_cell("shor-sampling-recovery")

    def test_invalid_editable_inputs_fail(self):
        for base, width in [(6, 4), (2, 3), (2, 7), (15, 4)]:
            with self.subTest(base=base, width=width), self.assertRaises(ValueError):
                self.execute_cell("shor-parameters-circuit", base=base, num_counting_qubits=width)


if __name__ == "__main__":
    unittest.main()
