"""Execute the actual guided cells and independently check every advertised edit."""

import ast
from contextlib import redirect_stdout
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import nbformat
import numpy as np
from qiskit.quantum_info import Operator, Statevector


ROOT = Path(__file__).resolve().parents[1]
GUIDED = ROOT / "teaching/phys3810-fa2026/notebooks/guided"
NAMES = (
    "01_python_and_qiskit.ipynb",
    "02_grover_follow_along.ipynb",
    "03_qft_qpe_follow_along.ipynb",
)


class GuidedNotebookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import matplotlib

        matplotlib.use("Agg", force=True)
        cls.notebooks = {name: nbformat.read(GUIDED / name, as_version=4) for name in NAMES}
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

    def run_cell(self, cell_id, **parameters):
        # A direct-cell regression uses Agg; only the display-backend magic is
        # omitted here. The strict validator executes the original whole cells.
        source = self.cells[cell_id].replace("%matplotlib inline\n", "")
        tree = ast.parse(source)
        changed = set()
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in parameters:
                        node.value = ast.parse(repr(parameters[target.id]), mode="eval").body
                        changed.add(target.id)
        self.assertEqual(changed, set(parameters), "An advertised editable parameter disappeared.")
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compile(ast.fix_missing_locations(tree), cell_id, "exec"), self.namespace)
        if "display" in self.namespace:
            self.namespace["display"] = self.figures.append
        return output.getvalue()

    def test_all_sources_are_output_free_and_cell_ids_are_unique(self):
        all_ids = []
        for name, notebook in self.notebooks.items():
            with self.subTest(notebook=name):
                nbformat.validate(notebook)
                for cell in notebook.cells:
                    all_ids.append(cell.id)
                    if cell.cell_type == "code":
                        self.assertIsNone(cell.execution_count)
                        self.assertEqual(cell.outputs, [])
                        self.assertNotIn("skip-execution", cell.metadata.get("tags", []))
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def prepare_python(self):
        for cell in ("guided-python-support", "guided-python-values", "guided-python-lists",
                     "guided-python-calls", "guided-python-imports"):
            self.run_cell(cell)

    def test_python_worked_basics_and_advertised_greeting_edit(self):
        self.prepare_python()
        output = self.run_cell("guided-python-values", greeting="Hello from a beginner")
        self.assertEqual(self.namespace["greeting"], "Hello from a beginner")
        self.assertIn("Hello from a beginner", output)
        self.assertEqual(self.namespace["repetitions"], 512)
        self.assertEqual(self.namespace["half"], 0.5)
        self.assertEqual(self.namespace["outcomes"], ["0", "1"])
        self.run_cell("guided-python-calls")

    def test_python_x_and_h_observations_and_repeated_runs(self):
        self.prepare_python()
        for label, circuit_cell, sampling_cell, expected in (
            ("x", "guided-python-x-circuit", "guided-python-x-sampling", [0, 1]),
            ("h", "guided-python-h-circuit", "guided-python-h-sampling", [0.5, 0.5]),
        ):
            with self.subTest(circuit=label):
                self.run_cell(circuit_cell)
                first = Operator(self.namespace[f"{label}_circuit"]).data.copy()
                self.run_cell(sampling_cell)
                np.testing.assert_allclose(self.namespace[f"{label}_probabilities"], expected,
                                           rtol=0, atol=1e-12)
                counts = self.namespace[f"{label}_counts"]
                self.assertEqual(sum(counts.values()), 512)
                if label == "x":
                    self.assertEqual(counts, {"1": 512})
                else:
                    self.assertEqual(set(counts), {"0", "1"})
                    self.assertLessEqual(abs(counts["0"] - 256), 6 * np.sqrt(512 * 0.25))
                self.assertEqual(self.namespace[f"{label}_circuit"].num_clbits, 0)
                self.run_cell(circuit_cell)
                self.run_cell(sampling_cell)
                np.testing.assert_allclose(Operator(self.namespace[f"{label}_circuit"]).data,
                                           first, rtol=0, atol=1e-12)
                self.assertEqual(self.namespace[f"{label}_counts"], counts)

    def prepare_grover(self, target="01", iterations=1):
        if "grover_circuit" not in self.namespace:
            self.run_cell("guided-grover-support")
        self.run_cell("guided-grover-parameters", target=target, iterations=iterations)
        self.run_cell("guided-grover-build")

    def test_all_twelve_grover_edits_recompute_probabilities_counts_and_captions(self):
        for target in ("00", "01", "10", "11"):
            for iterations, expected_probability in ((0, 0.25), (1, 1.0), (2, 0.25)):
                with self.subTest(target=target, iterations=iterations):
                    self.prepare_grover(target, iterations)
                    expected = np.full(4, 0.25)
                    if iterations == 1:
                        expected[:] = 0
                        expected[int(target, 2)] = 1
                    np.testing.assert_allclose(self.namespace["probabilities"], expected,
                                               rtol=0, atol=1e-12)
                    self.assertAlmostEqual(self.namespace["target_probability"], expected_probability)
                    self.assertEqual(self.namespace["expected_probability"], expected_probability)
                    self.run_cell("guided-grover-circuit")
                    output = self.run_cell("guided-grover-sampling")
                    counts = self.namespace["counts"]
                    self.assertEqual(sum(counts.values()), 512)
                    self.assertTrue(set(counts).issubset({"00", "01", "10", "11"}))
                    for index, probability in enumerate(expected):
                        label = f"{index:02b}"
                        tolerance = 6 * np.sqrt(512 * probability * (1 - probability)) + 1
                        self.assertLessEqual(abs(counts.get(label, 0) - 512 * probability), tolerance)
                    self.assertAlmostEqual(self.namespace["observed_probability"], counts.get(target, 0) / 512)
                    self.assertIn(target, self.namespace["circuit_title"])
                    self.assertIn(str(iterations), self.namespace["circuit_title"])
                    self.assertIn(target, self.namespace["histogram_title"])
                    self.assertIn(str(iterations), self.namespace["histogram_title"])
                    self.assertIn(f"exact P={expected_probability:g}", self.namespace["histogram_title"])
                    self.assertIn(target, output)
                    self.assertEqual(self.namespace["search"].num_clbits, 0)
        self.assertEqual(len(self.figures), 24)

    def test_grover_comparison_updates_target_and_analytic_curve(self):
        for target in ("01", "10"):
            with self.subTest(target=target):
                self.prepare_grover(target)
                self.run_cell("guided-grover-comparison")
                np.testing.assert_allclose(self.namespace["comparison_probabilities"],
                                           [0.25, 1.0, 0.25], rtol=0, atol=1e-12)
                self.assertIn(target, self.namespace["comparison_title"])
                np.testing.assert_allclose([bar.get_height() for bar in self.namespace["axes"].patches],
                                           [0.25, 1.0, 0.25], rtol=0, atol=1e-12)
                np.testing.assert_allclose(self.namespace["axes"].lines[0].get_ydata(),
                                           [0.25, 1.0, 0.25], rtol=0, atol=1e-12)

    def test_grover_rerunning_build_and_sampling_does_not_accumulate_operations(self):
        self.prepare_grover("10", 2)
        first = Operator(self.namespace["search"]).data.copy()
        self.run_cell("guided-grover-sampling")
        counts = self.namespace["counts"].copy()
        self.run_cell("guided-grover-build")
        self.run_cell("guided-grover-sampling")
        np.testing.assert_allclose(Operator(self.namespace["search"]).data, first, rtol=0, atol=1e-12)
        self.assertEqual(self.namespace["counts"], counts)
        self.assertEqual(self.namespace["search"].num_clbits, 0)

    def prepare_phase(self):
        if "qpe_circuit" not in self.namespace:
            self.run_cell("guided-phase-support")

    def test_qft_advertised_basis_edits_show_complex_phase_and_inverse_recovery(self):
        self.prepare_phase()
        for label in ("01", "10"):
            with self.subTest(basis=label):
                self.run_cell("guided-qft-parameters", basis_label=label)
                self.run_cell("guided-qft-forward")
                expected = np.exp(2j * np.pi * int(label, 2) * np.arange(4) / 4) / 2
                np.testing.assert_allclose(self.namespace["fourier_state"].data, expected,
                                           rtol=0, atol=1e-12)
                np.testing.assert_allclose(self.namespace["fourier_state"].probabilities(),
                                           np.full(4, 0.25), rtol=0, atol=1e-12)
                self.run_cell("guided-qft-pattern")
                self.assertIn(label, self.namespace["phase_title"])
                self.assertEqual(self.namespace["phase_axes"].get_title(), self.namespace["phase_title"])
                heights = [bar.get_height() for bar in self.namespace["phase_axes"].patches]
                np.testing.assert_allclose(heights, np.r_[expected.real, expected.imag], rtol=0, atol=1e-12)
                self.run_cell("guided-qft-inverse")
                recovered = np.zeros(4)
                recovered[int(label, 2)] = 1
                np.testing.assert_allclose(self.namespace["recovery_probabilities"], recovered,
                                           rtol=0, atol=1e-12)
                self.assertIn(label, self.namespace["recovery_title"])
                np.testing.assert_allclose(
                    [bar.get_height() for bar in self.namespace["recovery_axes"].patches],
                    recovered, rtol=0, atol=1e-12,
                )
        self.assertEqual(len(self.figures), 4)

    def test_qft_repeating_forward_and_inverse_has_no_stale_state(self):
        self.prepare_phase()
        self.run_cell("guided-qft-parameters", basis_label="01")
        self.run_cell("guided-qft-forward")
        self.run_cell("guided-qft-inverse")
        first = self.namespace["fourier_state"].data.copy()
        for _ in range(2):
            self.run_cell("guided-qft-forward")
            self.run_cell("guided-qft-inverse")
            np.testing.assert_allclose(self.namespace["fourier_state"].data, first, rtol=0, atol=1e-12)
            np.testing.assert_allclose(self.namespace["recovery_probabilities"], [0, 1, 0, 0],
                                       rtol=0, atol=1e-12)

    def test_qpe_both_exact_phase_edits_prepare_eigenstate_and_preserve_bit_order(self):
        self.prepare_phase()
        for phase, label in ((3 / 8, "011"), (1 / 8, "001")):
            with self.subTest(phase=phase):
                self.run_cell("guided-qpe-parameters", exact_phase=phase)
                self.run_cell("guided-qpe-build")
                expected = np.zeros(8)
                expected[int(label, 2)] = 1
                np.testing.assert_allclose(self.namespace["counting_probabilities"], expected,
                                           rtol=0, atol=1e-12)
                full_expected = np.zeros(16, dtype=complex)
                full_expected[8 + int(label, 2)] = 1
                np.testing.assert_allclose(Statevector.from_instruction(self.namespace["qpe_prepared"]).data,
                                           full_expected, rtol=0, atol=1e-12)
                self.assertEqual(self.namespace["expected_label"], label)
                self.run_cell("guided-qpe-circuit")
                output = self.run_cell("guided-qpe-sampling")
                self.assertEqual(self.namespace["phase_counts"], {label: 512})
                self.assertEqual(self.namespace["decoded_phase"], phase)
                self.assertIn(label, self.namespace["phase_histogram_title"])
                self.assertIn(label, output)
                self.assertEqual(self.namespace["qpe_prepared"].num_clbits, 0)

    def test_qpe_repeated_build_and_sampling_preserve_circuit_and_counts(self):
        self.prepare_phase()
        self.run_cell("guided-qpe-parameters", exact_phase=1 / 8)
        self.run_cell("guided-qpe-build")
        first = Operator(self.namespace["qpe_prepared"]).data.copy()
        self.run_cell("guided-qpe-sampling")
        self.run_cell("guided-qpe-build")
        self.run_cell("guided-qpe-sampling")
        np.testing.assert_allclose(Operator(self.namespace["qpe_prepared"]).data, first,
                                   rtol=0, atol=1e-12)
        self.assertEqual(self.namespace["phase_counts"], {"001": 512})
        self.assertEqual(self.namespace["qpe_prepared"].num_clbits, 0)

    def test_import_bootstrap_resolves_only_inside_a_git_free_copy_with_spaces(self):
        with tempfile.TemporaryDirectory(prefix="phys3810 guided import ") as directory:
            root = Path(directory) / "runtime"
            shutil.copytree(ROOT / "src", root / "src", ignore=shutil.ignore_patterns("__pycache__"))
            folder = root / "teaching/phys3810-fa2026/notebooks/guided"
            folder.mkdir(parents=True)
            for name in NAMES:
                shutil.copy2(GUIDED / name, folder / name)
            command = """
import json
from pathlib import Path
import sys
expected = Path(sys.argv[1]).resolve()
name = sys.argv[2]
cell_id = sys.argv[3]
notebook = json.loads(Path(name).read_text())
source = next(''.join(cell['source']) for cell in notebook['cells'] if cell['id'] == cell_id)
namespace = {}
exec(compile(source.replace('%matplotlib inline\\n', ''), cell_id, 'exec'), namespace)
from src.phys3810 import grover, qft, qpe
for module in (grover, qft, qpe):
    path = Path(module.__file__).resolve()
    assert path.is_relative_to(expected), (path, expected)
    print(path)
assert not (expected / '.git').exists()
"""
            environment = os.environ.copy()
            environment.pop("PYTHONPATH", None)
            environment["PYTHONNOUSERSITE"] = "1"
            environment["MPLBACKEND"] = "Agg"
            for name, support in ((NAMES[1], "guided-grover-support"), (NAMES[2], "guided-phase-support")):
                with self.subTest(notebook=name):
                    result = subprocess.run(
                        [sys.executable, "-c", command, str(root), name, support],
                        cwd=folder, env=environment, capture_output=True, text=True,
                        timeout=45, check=False,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertNotIn(str(ROOT), result.stdout)
                    for module in ("grover.py", "qft.py", "qpe.py"):
                        self.assertIn(str(root / "src" / "phys3810" / module), result.stdout)


if __name__ == "__main__":
    unittest.main()
