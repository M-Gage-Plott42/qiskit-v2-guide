"""Independent mathematical and input-contract tests for the small Grover module.

Expected matrices, amplitude updates, and probabilities are calculated without
the implementation or Qiskit's Grover reference. The SDK comparison is separate.
"""

from fractions import Fraction
from math import asin, sin, sqrt
import unittest

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import grover_operator
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Operator, Statevector

from src.phys3810.grover import (
    diffusion_operator,
    grover_circuit,
    grover_iteration,
    phase_oracle,
)


ATOL = 1e-12
SUPPORTED_QUBITS = range(2, 6)


def expected_oracle(num_qubits, marked_states):
    """The mathematical contract: columns are the action on every basis state."""
    phases = np.ones(2**num_qubits, dtype=complex)
    phases[[int(bits, 2) for bits in marked_states]] = -1
    return np.diag(phases)


def selected_targets(num_qubits, count):
    # Multiplication by 3 permutes indices modulo a power of 2. The first target
    # is asymmetric (00...01); larger cases include low and high bit positions.
    size = 2**num_qubits
    return [format((3 * index + 1) % size, f"0{num_qubits}b") for index in range(count)]


class GroverInputContractTests(unittest.TestCase):
    def assert_bad_targets(self, targets, exception):
        for builder in (phase_oracle, grover_iteration, grover_circuit):
            with self.subTest(builder=builder.__name__, targets=targets):
                with self.assertRaises(exception):
                    if builder is grover_circuit:
                        # Even zero iterations must validate the declared search.
                        builder(3, targets, iterations=0)
                    else:
                        builder(3, targets)

    def test_qubit_count_requires_integer_not_boolean(self):
        for value in (True, False, np.bool_(True), 3.0, "3", None, 3 + 0j):
            for builder in (phase_oracle, diffusion_operator, grover_iteration, grover_circuit):
                with self.subTest(value=value, builder=builder.__name__):
                    with self.assertRaises(TypeError):
                        if builder is diffusion_operator:
                            builder(value)
                        elif builder is grover_circuit:
                            builder(value, ["001"], iterations=0)
                        else:
                            builder(value, ["001"])

    def test_qubit_count_is_restricted_to_two_through_five(self):
        for value in (-2, 0, 1, 6, 20):
            for builder in (phase_oracle, diffusion_operator, grover_iteration, grover_circuit):
                with self.subTest(value=value, builder=builder.__name__):
                    with self.assertRaises(ValueError):
                        if builder is diffusion_operator:
                            builder(value)
                        elif builder is grover_circuit:
                            builder(value, ["001"], iterations=0)
                        else:
                            builder(value, ["001"])

    def test_targets_require_a_collection_not_a_bare_string(self):
        for targets in ("001", b"001", None, 1):
            self.assert_bad_targets(targets, TypeError)

    def test_each_target_must_be_a_string(self):
        for targets in ([1], [None], [b"001"], ["001", 3]):
            self.assert_bad_targets(targets, TypeError)

    def test_target_width_and_binary_alphabet_are_enforced(self):
        for target in ("", "1", "01", "0001", "012", "0 1", "01\n", "００１"):
            self.assert_bad_targets([target], ValueError)

    def test_empty_and_duplicate_targets_are_rejected(self):
        for targets in ([], (), set(), ["001", "001"], ["001", "011", "001"]):
            self.assert_bad_targets(targets, ValueError)

    def test_all_marked_sets_are_rejected_for_each_supported_size(self):
        for num_qubits in SUPPORTED_QUBITS:
            targets = [format(index, f"0{num_qubits}b") for index in range(2**num_qubits)]
            for builder in (phase_oracle, grover_iteration, grover_circuit):
                with self.subTest(num_qubits=num_qubits, builder=builder.__name__):
                    with self.assertRaises(ValueError):
                        if builder is grover_circuit:
                            builder(num_qubits, targets, iterations=0)
                        else:
                            builder(num_qubits, targets)

    def test_iterations_require_nonnegative_integers_not_booleans(self):
        for value in (True, False, np.bool_(True), 1.0, 0.5, "2", None, 1 + 0j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    grover_circuit(3, ["001"], iterations=value)
        for value in (-1, -10):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    grover_circuit(3, ["001"], iterations=value)

    def test_numpy_integer_arguments_are_supported(self):
        circuit = grover_circuit(np.int64(3), ["001"], iterations=np.int64(2))
        self.assertEqual(circuit.num_qubits, 3)
        probability = Statevector.from_instruction(circuit).probabilities()[1]
        np.testing.assert_allclose(probability, 121 / 128, rtol=0, atol=ATOL)

    def test_valid_iterables_are_equivalent_and_input_order_is_unchanged(self):
        targets = ["011", "001"]
        expected = expected_oracle(3, targets)
        factories = (
            lambda: targets,
            lambda: tuple(targets),
            lambda: set(targets),
            lambda: (target for target in targets),
        )
        for factory in factories:
            np.testing.assert_allclose(Operator(phase_oracle(3, factory())).data, expected, rtol=0, atol=ATOL)
            np.testing.assert_allclose(
                Statevector.from_instruction(grover_circuit(3, factory(), iterations=1)).probabilities(),
                [0, 0.5, 0, 0.5, 0, 0, 0, 0], rtol=0, atol=ATOL,
            )
        self.assertEqual(targets, ["011", "001"], "The builder mutated caller-owned targets.")

    def test_returned_circuits_are_unmeasured_and_use_no_ancillas(self):
        for num_qubits in SUPPORTED_QUBITS:
            targets = selected_targets(num_qubits, 1)
            circuits = (
                phase_oracle(num_qubits, targets), diffusion_operator(num_qubits),
                grover_iteration(num_qubits, targets), grover_circuit(num_qubits, targets, iterations=2),
            )
            for circuit in circuits:
                with self.subTest(num_qubits=num_qubits, name=circuit.name):
                    self.assertEqual(circuit.num_qubits, num_qubits)
                    self.assertEqual(circuit.num_clbits, 0)
                    self.assertEqual(circuit.num_ancillas, 0)
                    self.assertNotIn("measure", circuit.count_ops())


class GroverMathematicsTests(unittest.TestCase):
    def test_single_target_oracle_action_on_every_basis_state(self):
        # Every possible marked target for each supported n: 60 whole operators.
        # A full-matrix assertion checks all basis inputs, not just the marked one.
        for num_qubits in SUPPORTED_QUBITS:
            for target in range(2**num_qubits):
                marked = [format(target, f"0{num_qubits}b")]
                with self.subTest(num_qubits=num_qubits, marked=marked):
                    actual = Operator(phase_oracle(num_qubits, marked)).data
                    np.testing.assert_allclose(actual, expected_oracle(num_qubits, marked), rtol=0, atol=ATOL)

    def test_multiple_target_oracle_action_on_every_basis_state(self):
        for num_qubits in SUPPORTED_QUBITS:
            for count in (2, 2**num_qubits - 1):
                targets = selected_targets(num_qubits, count)
                with self.subTest(num_qubits=num_qubits, count=count):
                    actual = Operator(phase_oracle(num_qubits, targets)).data
                    np.testing.assert_allclose(actual, expected_oracle(num_qubits, targets), rtol=0, atol=ATOL)
        # Explicit asymmetric fixture also used by the teaching notebook.
        np.testing.assert_allclose(
            Operator(phase_oracle(3, ["001", "011"])).data,
            np.diag([1, -1, 1, -1, 1, 1, 1, 1]), rtol=0, atol=ATOL,
        )

    def test_diffusion_is_exact_reflection_about_uniform_state(self):
        for num_qubits in SUPPORTED_QUBITS:
            size = 2**num_qubits
            diffusion = Operator(diffusion_operator(num_qubits)).data
            with self.subTest(num_qubits=num_qubits):
                expected = np.full((size, size), 2 / size) - np.eye(size)
                np.testing.assert_allclose(diffusion, expected, rtol=0, atol=ATOL)
                # Independent amplitude interpretation, including complex phases.
                state = np.arange(1, size + 1) + 1j * np.arange(size, 0, -1)
                state = state / np.linalg.norm(state)
                np.testing.assert_allclose(diffusion @ state, 2 * state.mean() - state, rtol=0, atol=ATOL)

    def test_iteration_is_diffusion_after_oracle(self):
        for num_qubits in SUPPORTED_QUBITS:
            size = 2**num_qubits
            for count in (1, 2):
                targets = selected_targets(num_qubits, count)
                expected_diffusion = np.full((size, size), 2 / size) - np.eye(size)
                expected = expected_diffusion @ expected_oracle(num_qubits, targets)
                with self.subTest(num_qubits=num_qubits, count=count):
                    np.testing.assert_allclose(
                        Operator(grover_iteration(num_qubits, targets)).data, expected, rtol=0, atol=ATOL
                    )

    def test_full_state_matches_classical_amplitude_recurrence(self):
        for num_qubits in SUPPORTED_QUBITS:
            size = 2**num_qubits
            for count in (1, 2):
                targets = selected_targets(num_qubits, count)
                indices = [int(bits, 2) for bits in targets]
                for iterations in (0, 1, 2, 4):
                    expected = np.full(size, 1 / sqrt(size), dtype=complex)
                    for _ in range(iterations):
                        expected[indices] *= -1
                        expected = 2 * expected.mean() - expected
                    actual = Statevector.from_instruction(grover_circuit(num_qubits, targets, iterations))
                    with self.subTest(num_qubits=num_qubits, count=count, iterations=iterations):
                        np.testing.assert_allclose(actual.data, expected, rtol=0, atol=ATOL)
                        np.testing.assert_allclose(np.vdot(actual.data, actual.data), 1, rtol=0, atol=ATOL)

    def test_analytic_amplification_across_sizes_and_marked_fractions(self):
        for num_qubits in SUPPORTED_QUBITS:
            size = 2**num_qubits
            for count in sorted({1, 2, size // 2, size - 1}):
                targets = selected_targets(num_qubits, count)
                indices = [int(bits, 2) for bits in targets]
                theta = asin(sqrt(count / size))
                for iterations in range(6):
                    expected = sin((2 * iterations + 1) * theta) ** 2
                    state = Statevector.from_instruction(grover_circuit(num_qubits, targets, iterations))
                    actual = state.probabilities()[indices].sum()
                    with self.subTest(num_qubits=num_qubits, count=count, iterations=iterations):
                        np.testing.assert_allclose(actual, expected, rtol=0, atol=ATOL)

    def test_required_rational_probability_fixtures(self):
        fixtures = (
            (3, ["001", "011"], 0, Fraction(1, 4)),
            (2, ["01"], 1, Fraction(1)),
            (3, ["001"], 2, Fraction(121, 128)),
            (3, ["001", "011"], 1, Fraction(1)),
            (2, ["01"], 2, Fraction(1, 4)),
        )
        for num_qubits, targets, iterations, expected in fixtures:
            state = Statevector.from_instruction(grover_circuit(num_qubits, targets, iterations))
            actual = sum(state.probabilities()[int(bits, 2)] for bits in targets)
            with self.subTest(num_qubits=num_qubits, targets=targets, iterations=iterations):
                np.testing.assert_allclose(actual, float(expected), rtol=0, atol=ATOL)

    def test_sdk_reference_agrees_up_to_global_phase(self):
        # The reference oracle is built from the independent diagonal matrix,
        # rather than from the implementation under test.
        for num_qubits in SUPPORTED_QUBITS:
            for count in (1, 2):
                targets = selected_targets(num_qubits, count)
                reference_oracle = QuantumCircuit(num_qubits)
                reference_oracle.unitary(expected_oracle(num_qubits, targets), range(num_qubits))
                reference = Operator(grover_operator(reference_oracle))
                actual = Operator(grover_iteration(num_qubits, targets))
                with self.subTest(num_qubits=num_qubits, count=count):
                    self.assertTrue(actual.equiv(reference, rtol=0, atol=ATOL))

    def test_seeded_v2_sampling_of_asymmetric_targets(self):
        shots = 4096
        fixtures = ((["001"], 2, 121 / 128), (["001", "011"], 1, 1.0))
        for targets, iterations, expected_probability in fixtures:
            circuit = grover_circuit(3, targets, iterations)
            measured = circuit.measure_all(inplace=False)
            result = StatevectorSampler(seed=1234).run([measured], shots=shots).result()[0]
            counts = result.data.meas.get_counts()
            with self.subTest(targets=targets, iterations=iterations):
                self.assertEqual(circuit.num_clbits, 0)
                self.assertEqual(sum(counts.values()), shots)
                self.assertEqual(len(result.data.meas.get_bitstrings()), shots)
                self.assertTrue(set(counts) <= {format(i, "03b") for i in range(8)})
                successes = sum(counts.get(target, 0) for target in targets)
                tolerance = 6 * sqrt(shots * expected_probability * (1 - expected_probability))
                self.assertLessEqual(abs(successes - shots * expected_probability), tolerance)
                if expected_probability == 1:
                    self.assertEqual(set(counts), set(targets))
                    self.assertLessEqual(abs(counts[targets[0]] - shots / 2), 6 * sqrt(shots / 4))


if __name__ == "__main__":
    unittest.main()
