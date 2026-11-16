"""Exercise the actual introductory lesson cells and their advertised rerun paths."""

import ast
from collections import Counter
from contextlib import redirect_stdout
import io
from pathlib import Path
import unittest

import nbformat
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector


ROOT = Path(__file__).resolve().parents[1]
INTRO = ROOT / "teaching/phys3810-fa2026/notebooks/intro"
NAMES = {"rng": "01_quantum_rng.ipynb", "bell": "02_bell_state.ipynb"}
ATOL = 1e-12


class IntroNotebookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.notebooks = {
            kind: nbformat.read(INTRO / name, as_version=4) for kind, name in NAMES.items()
        }
        cls.cells = {
            cell.id: cell.source
            for notebook in cls.notebooks.values() for cell in notebook.cells
            if cell.cell_type == "code"
        }

    def setUp(self):
        import matplotlib.pyplot as plt

        self.namespace = {}
        self.figures = []
        self.addCleanup(plt.close, "all")

    def cell_program(self, cell_id, **parameters):
        # Only omit the inline-display magic in these direct-cell tests. The
        # classroom validator executes the original notebook in a fresh kernel.
        source = self.cells[cell_id].replace("%matplotlib inline\n", "")
        tree = ast.parse(source)
        changed = set()
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in parameters:
                        node.value = ast.parse(repr(parameters[target.id]), mode="eval").body
                        changed.add(target.id)
        self.assertEqual(changed, set(parameters), "Advertised parameter assignment disappeared.")
        return compile(ast.fix_missing_locations(tree), cell_id, "exec")

    def execute_program(self, program):
        output = io.StringIO()
        with redirect_stdout(output):
            exec(program, self.namespace)
        if "display" in self.namespace:
            self.namespace["display"] = self.figures.append
        return output.getvalue()

    def run_cell(self, kind, suffix, **parameters):
        return self.execute_program(self.cell_program(f"intro-{kind}-{suffix}", **parameters))

    def prepare(self, kind, shots=128):
        self.run_cell(kind, "environment")
        self.run_cell(kind, "parameters", shots=shots)
        self.run_cell(kind, "prepare")

    def sample_and_plot(self, kind):
        return self.run_cell(kind, "sample") + self.run_cell(kind, "plot")

    def assert_counts(self, kind, shots):
        counts = self.namespace[f"{kind}_counts"]
        support = {"0", "1"} if kind == "rng" else {"00", "11"}
        self.assertEqual(sum(counts.values()), shots)
        self.assertTrue(set(counts) <= support)
        self.assertTrue(all(len(label) == (1 if kind == "rng" else 2) for label in counts))
        self.assertTrue(all(isinstance(count, int) and count > 0 for count in counts.values()))
        if kind == "rng":
            bits = self.namespace["rng_bits"]
            self.assertEqual(len(bits), shots)
            self.assertEqual(Counter(bits), counts)
            self.assertEqual(bits, self.namespace["rng_result"].data.meas.get_bitstrings())

    def assert_plot_and_caption(self, kind, shots, output):
        self.assertIn(f"{shots} simulated shots", self.namespace[f"{kind}_caption"])
        self.assertIn(self.namespace[f"{kind}_caption"], output)
        self.assertIn(f"{shots} simulated shots", self.namespace[f"{kind}_title"])
        axis = self.namespace[f"{kind}_histogram"].axes[0]
        self.assertEqual(axis.get_title(), self.namespace[f"{kind}_title"])
        bars = {label.get_text(): bar.get_height()
                for label, bar in zip(axis.get_xticklabels(), axis.patches)}
        self.assertEqual(bars, self.namespace[f"{kind}_counts"])
        self.assertEqual(sum(bars.values()), shots)

    def test_sources_have_stable_unique_ids_and_no_saved_execution_state(self):
        identifiers = []
        for kind, notebook in self.notebooks.items():
            with self.subTest(notebook=kind):
                nbformat.validate(notebook)
                code = [cell for cell in notebook.cells if cell.cell_type == "code"]
                expected = [f"intro-{kind}-{suffix}" for suffix in
                            ("environment", "parameters", "prepare", "sample", "plot")]
                if kind == "bell":
                    expected.append("intro-bell-x-basis")
                self.assertEqual([cell.id for cell in code], expected)
                for cell in notebook.cells:
                    identifiers.append(cell.id)
                    if cell.cell_type == "code":
                        self.assertIsNone(cell.execution_count)
                        self.assertEqual(cell.outputs, [])
                        self.assertFalse({"skip-execution", "raises-exception"}
                                         & set(cell.metadata.get("tags", [])))
        self.assertEqual(len(identifiers), len(set(identifiers)))

    def test_both_notebooks_execute_independently_in_empty_namespaces(self):
        for kind, notebook in self.notebooks.items():
            with self.subTest(notebook=kind):
                self.namespace = {}
                self.figures = []
                for cell in notebook.cells:
                    if cell.cell_type == "code":
                        self.execute_program(self.cell_program(cell.id))
                self.assertEqual(self.namespace["shots"], 128)
                self.assertEqual(self.namespace["seed"], 2026)
                self.assert_counts(kind, 128)
                self.assertEqual(len(self.figures), 2 if kind == "rng" else 3)

    def test_rng_amplitudes_normalization_and_probabilities(self):
        self.prepare("rng")
        state = self.namespace["rng_state"].data
        expected = np.array([1, 1], dtype=complex) / np.sqrt(2)
        np.testing.assert_allclose(state, expected, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.vdot(state, state), 1, rtol=0, atol=ATOL)
        np.testing.assert_allclose(self.namespace["rng_probabilities"], [0.5, 0.5],
                                   rtol=0, atol=ATOL)

    def test_bell_amplitudes_normalization_relative_phase_and_marginals(self):
        self.prepare("bell")
        state = self.namespace["bell_state"].data
        expected = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
        np.testing.assert_allclose(state, expected, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.vdot(state, state), 1, rtol=0, atol=ATOL)
        np.testing.assert_allclose(state[3] / state[0], 1, rtol=0, atol=ATOL)
        probabilities = self.namespace["bell_probabilities"]
        np.testing.assert_allclose(probabilities, [0.5, 0, 0, 0.5], rtol=0, atol=ATOL)
        # Derive each marginal from the stated q1 q0 outcome ordering.
        np.testing.assert_allclose(
            [probabilities[1] + probabilities[3], probabilities[2] + probabilities[3]],
            [0.5, 0.5], rtol=0, atol=ATOL,
        )

    def test_rng_samples_are_ordered_and_counts_match_for_one_and_many_shots(self):
        for shots in (1, 128, 1024):
            with self.subTest(shots=shots):
                self.prepare("rng", shots)
                output = self.sample_and_plot("rng")
                self.assert_counts("rng", shots)
                self.assert_plot_and_caption("rng", shots, output)
                self.assertIn(f"First {min(24, shots)} bits in shot order:", output)
                self.assertIn(" ".join(self.namespace["rng_bits"][:24]), output)

    def test_bell_sampling_handles_one_shot_without_requiring_both_outcomes(self):
        for shots in (1, 128, 1024):
            with self.subTest(shots=shots):
                self.prepare("bell", shots)
                output = self.sample_and_plot("bell")
                self.assert_counts("bell", shots)
                self.assert_plot_and_caption("bell", shots, output)

    def test_asymmetric_calibration_uses_the_actual_bell_sampling_cell(self):
        self.prepare("bell", 17)
        for qubit, label in ((0, "01"), (1, "10")):
            with self.subTest(qubit=qubit):
                calibration = QuantumCircuit(2)
                calibration.x(qubit)
                self.namespace["bell"] = calibration
                self.run_cell("bell", "sample")
                self.assertEqual(self.namespace["bell_counts"], {label: 17})
                measured = self.namespace["bell_measured"]
                pairs = [(measured.find_bit(inst.qubits[0]).index,
                          measured.find_bit(inst.clbits[0]).index)
                         for inst in measured.data if inst.operation.name == "measure"]
                self.assertEqual(pairs, [(0, 0), (1, 1)])
                self.assertEqual(calibration.num_clbits, 0)

    def test_repeated_preparation_and_sampling_never_accumulate_gates_or_measurements(self):
        for kind, gates in (("rng", {"h": 1}), ("bell", {"h": 1, "cx": 1})):
            with self.subTest(notebook=kind):
                self.prepare(kind)
                original = Operator(self.namespace[kind]).data.copy()
                for _ in range(3):
                    self.run_cell(kind, "prepare")
                    self.run_cell(kind, "sample")
                    self.run_cell(kind, "sample")
                    prepared = self.namespace[kind]
                    measured = self.namespace[f"{kind}_measured"]
                    self.assertIsNot(prepared, measured)
                    self.assertEqual(dict(prepared.count_ops()), gates)
                    self.assertEqual(prepared.num_clbits, 0)
                    self.assertEqual(measured.num_clbits, prepared.num_qubits)
                    self.assertEqual(dict(measured.count_ops()),
                                     {**gates, "measure": prepared.num_qubits})
                    np.testing.assert_allclose(Operator(prepared).data, original, rtol=0, atol=ATOL)

    def test_advertised_edits_and_reversal_update_counts_captions_and_plots(self):
        for kind in NAMES:
            with self.subTest(notebook=kind):
                self.prepare(kind)
                for shots in (128, 1024, 128):
                    self.run_cell(kind, "parameters", shots=shots)
                    output = self.sample_and_plot(kind)
                    self.assert_counts(kind, shots)
                    self.assert_plot_and_caption(kind, shots, output)
                    if kind == "bell":
                        output = self.run_cell("bell", "x-basis")
                        self.assertEqual(sum(self.namespace["bell_x_counts"].values()), shots)
                        self.assert_plot_and_caption("bell_x", shots, output)

    def test_source_edit_without_parameter_execution_retains_old_runtime_value(self):
        for kind in NAMES:
            with self.subTest(notebook=kind):
                self.prepare(kind)
                self.sample_and_plot(kind)
                pending_edit = self.cell_program(f"intro-{kind}-parameters", shots=1024)
                # Deliberately do not execute the edited parameter cell. Even
                # successful downstream assertions still describe 128 shots.
                stale = self.sample_and_plot(kind)
                self.assertEqual(self.namespace["shots"], 128)
                self.assert_counts(kind, 128)
                self.assert_plot_and_caption(kind, 128, stale)
                self.assertNotIn("1024 simulated shots", stale)
                self.execute_program(pending_edit)
                current = self.sample_and_plot(kind)
                self.assertEqual(self.namespace["shots"], 1024)
                self.assert_counts(kind, 1024)
                self.assert_plot_and_caption(kind, 1024, current)
                pending_reverse = self.cell_program(f"intro-{kind}-parameters", shots=128)
                still_current = self.sample_and_plot(kind)
                self.assert_plot_and_caption(kind, 1024, still_current)
                self.execute_program(pending_reverse)
                restored = self.sample_and_plot(kind)
                self.assert_counts(kind, 128)
                self.assert_plot_and_caption(kind, 128, restored)

    def test_plot_rejects_results_from_before_an_executed_shot_count_change(self):
        for kind in NAMES:
            with self.subTest(notebook=kind):
                self.prepare(kind)
                self.run_cell(kind, "sample")
                self.run_cell(kind, "parameters", shots=1024)
                with self.assertRaisesRegex(AssertionError, "Run section 4"):
                    self.run_cell(kind, "plot")

    def test_parameter_cell_rejects_invalid_shot_counts(self):
        for kind in NAMES:
            for shots in (0, -1, 1.5, True):
                with self.subTest(notebook=kind, shots=shots):
                    with self.assertRaises(AssertionError):
                        self.run_cell(kind, "parameters", shots=shots)

    def test_optional_x_basis_matches_independent_rotation_and_classical_mixture(self):
        self.prepare("bell")
        self.run_cell("bell", "x-basis")
        h = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        rotation = np.kron(h, h)
        plus_bell = np.array([1, 0, 0, 1]) / np.sqrt(2)
        expected_state = rotation @ plus_bell
        expected_mixture = (np.abs(rotation[:, 0]) ** 2 + np.abs(rotation[:, 3]) ** 2) / 2
        np.testing.assert_allclose(Statevector.from_instruction(self.namespace["bell_x"]).data,
                                   expected_state, rtol=0, atol=ATOL)
        np.testing.assert_allclose(self.namespace["bell_x_probabilities"], [0.5, 0, 0, 0.5],
                                   rtol=0, atol=ATOL)
        np.testing.assert_allclose(expected_mixture, [0.25] * 4, rtol=0, atol=ATOL)
        np.testing.assert_allclose(self.namespace["classical_mixture_x_probabilities"],
                                   expected_mixture, rtol=0, atol=ATOL)
        self.assertTrue(set(self.namespace["bell_x_counts"]) <= {"00", "11"})

    def test_optional_x_basis_repeated_runs_preserve_preparation_and_shots_one(self):
        self.prepare("bell", 1)
        original = Operator(self.namespace["bell"]).data.copy()
        for _ in range(3):
            output = self.run_cell("bell", "x-basis")
            self.assertEqual(sum(self.namespace["bell_x_counts"].values()), 1)
            self.assert_plot_and_caption("bell_x", 1, output)
            self.assertEqual(dict(self.namespace["bell"].count_ops()), {"h": 1, "cx": 1})
            self.assertEqual(dict(self.namespace["bell_x"].count_ops()), {"h": 3, "cx": 1})
            self.assertEqual(dict(self.namespace["bell_x_measured"].count_ops()),
                             {"h": 3, "cx": 1, "measure": 2})
            self.assertEqual(self.namespace["bell"].num_clbits, 0)
            self.assertEqual(self.namespace["bell_x"].num_clbits, 0)
            np.testing.assert_allclose(Operator(self.namespace["bell"]).data, original,
                                       rtol=0, atol=ATOL)

    def test_relative_phase_negative_control_keeps_z_histogram_but_fails_x_expectation(self):
        self.prepare("bell")
        self.namespace["bell"].z(0)
        minus_state = Statevector.from_instruction(self.namespace["bell"])
        np.testing.assert_allclose(minus_state.probabilities(), [0.5, 0, 0, 0.5],
                                   rtol=0, atol=ATOL)
        expected_plus = np.array([1, 0, 0, 1]) / np.sqrt(2)
        self.assertFalse(np.allclose(minus_state.data, expected_plus, rtol=0, atol=ATOL))
        h = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        expected_minus_x = np.kron(h, h) @ (np.array([1, 0, 0, -1]) / np.sqrt(2))
        np.testing.assert_allclose(np.abs(expected_minus_x) ** 2, [0, 0.5, 0.5, 0],
                                   rtol=0, atol=ATOL)
        with self.assertRaises(AssertionError):
            self.run_cell("bell", "x-basis")
        np.testing.assert_allclose(Statevector.from_instruction(self.namespace["bell_x"]).data,
                                   expected_minus_x, rtol=0, atol=ATOL)


if __name__ == "__main__":
    unittest.main()
