"""Independent full-state, reciprocal, input, and same-shot V2 checks for HHL."""

from itertools import combinations_with_replacement
import unittest

import numpy as np
from qiskit import ClassicalRegister
from qiskit.circuit import Parameter
from qiskit.circuit.library import UnitaryGate
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Operator, Statevector

from src.phys3810.hhl import hhl_circuit, hhl_reciprocal_rotation
from src.phys3810.qpe import qpe_circuit


ATOL = 1e-10
CONDITIONED_ATOL = 1e-9
A0 = np.array([[1.5, 0.5], [0.5, 1.5]])
ZERO = np.array([1, 0], dtype=complex)
PLUS = np.array([1, 1]) / np.sqrt(2)
MINUS = np.array([1, -1]) / np.sqrt(2)
COMPLEX_RHS = np.array([1, 1j]) / np.sqrt(2)
PAULIS = {
    "X": np.array([[0, 1], [1, 0]]),
    "Y": np.array([[0, -1j], [1j, 0]]),
    "Z": np.diag([1, -1]),
}


def sampled_basis(circuit, basis):
    """Return a local measurement circuit; flag/system results retain shot order."""
    circuit = circuit.copy()
    flag = ClassicalRegister(1, "flag_readout")
    system = ClassicalRegister(1, "system_readout")
    circuit.add_register(flag, system)
    if basis == "X":
        circuit.h(3)
    elif basis == "Y":
        circuit.sdg(3)
        circuit.h(3)
    elif basis != "Z":
        raise ValueError("Unknown measurement basis")
    circuit.measure(4, flag)
    circuit.measure(3, system)
    return circuit


class HHLInputTests(unittest.TestCase):
    def test_matrix_types(self):
        for value in [None, "matrix", True, 2, {"matrix": A0},
                      [[True, 0], [0, 2]], [["1", "0"], ["0", "2"]],
                      [[Parameter("a"), 0], [0, 2]], [[object(), 0], [0, 2]],
                      np.array([[True, False], [False, True]])]:
            with self.subTest(value=repr(value)), self.assertRaises(TypeError):
                hhl_circuit(value, ZERO)

    def test_rhs_types(self):
        for value in [None, "state", True, 1, {"rhs": ZERO}, [True, False],
                      ["1", "0"], [Parameter("b"), 0], [object(), 0]]:
            with self.subTest(value=repr(value)), self.assertRaises(TypeError):
                hhl_circuit(A0, value)

    def test_wrong_matrix_shapes(self):
        for value in [[], [1, 2], [[1]], np.eye(3), np.ones((1, 2, 2)),
                      [[1, 0], [0]]]:
            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
                hhl_circuit(value, ZERO)

    def test_wrong_rhs_shapes(self):
        for value in [[], [1], [1, 0, 0], [[1, 0]], [[1], [0]], [[1], []]]:
            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
                hhl_circuit(A0, value)

    def test_nonfinite_matrix_and_rhs(self):
        for value in [np.nan, np.inf, -np.inf, complex(0, np.inf)]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                hhl_circuit([[1, 0], [0, value]], ZERO)
            with self.subTest(rhs=value), self.assertRaises(ValueError):
                hhl_circuit(A0, [value, 0])

    def test_nonhermitian_matrix(self):
        for matrix in [[[1, 1], [0, 2]], [[1 + 1e-5j, 0], [0, 2]],
                       [[1.5, 0.5 + 2e-11j], [0.5, 1.5]]]:
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                hhl_circuit(matrix, ZERO)

    def test_singular_negative_off_grid_and_wrapped_spectra(self):
        for spectrum in [(0, 1), (-1, 2), (1, 1.5), (1, 8), (8, 8),
                         (1, 9), (1, 2 + 1e-10), (1 - 1e-10, 2)]:
            with self.subTest(spectrum=spectrum), self.assertRaises(ValueError):
                hhl_circuit(np.diag(spectrum), ZERO)

    def test_rhs_must_already_be_normalized(self):
        for rhs in [[0, 0], [1, 1], [2, 0], [0.5, 0], [1 + 1e-10, 0]]:
            with self.subTest(rhs=rhs), self.assertRaises(ValueError):
                hhl_circuit(A0, rhs)

    def test_absolute_admission_tolerance_for_floating_representation(self):
        almost_hermitian = A0.astype(complex)
        almost_hermitian[0, 1] += 5e-13j
        accepted = [
            (np.diag([1 + 5e-13, 7 - 5e-13]), COMPLEX_RHS),
            (almost_hermitian, COMPLEX_RHS),
            (A0, COMPLEX_RHS * np.sqrt(1 + 5e-13)),
            (A0, COMPLEX_RHS * np.sqrt(1 - 5e-13)),
        ]
        for matrix, rhs in accepted:
            with self.subTest(matrix=matrix, rhs=rhs):
                state = Statevector.from_instruction(hhl_circuit(matrix, rhs)).data
                np.testing.assert_allclose(np.linalg.norm(state), 1, rtol=0, atol=ATOL)
                self.assertLessEqual(np.linalg.norm(state.reshape(2, 2, 8)[:, :, 1:]), 1e-9)
        # Boundaries use absolute tolerance, not NumPy's default relative tolerance.
        nonhermitian = A0.astype(complex)
        nonhermitian[0, 1] += 2e-12j
        rejected = [
            (np.diag([1 + 2e-12, 7]), COMPLEX_RHS),
            (np.diag([1, 7 + 2e-12]), COMPLEX_RHS),
            (nonhermitian, COMPLEX_RHS),
            (A0, COMPLEX_RHS * np.sqrt(1 + 2e-12)),
            (A0, COMPLEX_RHS * np.sqrt(1 - 2e-12)),
        ]
        for matrix, rhs in rejected:
            with self.subTest(matrix=matrix, rhs=rhs), self.assertRaises(ValueError):
                hhl_circuit(matrix, rhs)

    def test_numeric_lists_tuples_and_arrays(self):
        expected = Statevector.from_instruction(hhl_circuit(A0, ZERO)).data
        for matrix, rhs in [(A0.tolist(), [1, 0]),
                            (tuple(map(tuple, A0)), (1, 0)),
                            (A0.astype(complex), ZERO.copy())]:
            with self.subTest(type=type(matrix)):
                np.testing.assert_allclose(
                    Statevector.from_instruction(hhl_circuit(matrix, rhs)).data,
                    expected, rtol=0, atol=ATOL,
                )

    def test_inputs_not_mutated_or_retained_by_reference(self):
        matrix, rhs = A0.copy(), COMPLEX_RHS.copy()
        before_matrix, before_rhs = matrix.copy(), rhs.copy()
        circuit = hhl_circuit(matrix, rhs)
        np.testing.assert_array_equal(matrix, before_matrix)
        np.testing.assert_array_equal(rhs, before_rhs)
        expected = Statevector.from_instruction(circuit).data.copy()
        matrix[:] = np.eye(2)
        rhs[:] = ZERO
        np.testing.assert_allclose(Statevector.from_instruction(circuit).data,
                                   expected, rtol=0, atol=ATOL)

    def test_register_roles_and_no_classical_or_work_bits(self):
        circuit = hhl_circuit(A0, ZERO)
        self.assertEqual(circuit.num_qubits, 5)
        self.assertEqual([(reg.name, len(reg)) for reg in circuit.qregs],
                         [("count", 3), ("system", 1), ("success", 1)])
        self.assertEqual(circuit.num_clbits, 0)
        self.assertEqual(circuit.num_ancillas, 0)
        self.assertFalse(circuit.parameters)
        for instruction in circuit.data:
            self.assertNotIn(instruction.operation.name, ["measure", "reset", "initialize"])
        # HHL fits the existing helper; this milestone must not widen QPE for Shor.
        with self.assertRaises(ValueError):
            qpe_circuit(3, UnitaryGate(np.eye(16)))


class HHLReciprocalTests(unittest.TestCase):
    def test_full_operator_all_count_labels_and_both_flag_inputs(self):
        expected = np.zeros((16, 16), dtype=complex)
        for label in range(8):
            sine = 0 if label == 0 else 1 / label
            cosine = np.sqrt(1 - sine**2)
            # Flag is the high bit; the count pattern stays unchanged.
            expected[label, label] = expected[8 + label, 8 + label] = cosine
            expected[8 + label, label] = sine
            expected[label, 8 + label] = -sine
        actual = Operator(hhl_reciprocal_rotation()).data
        np.testing.assert_allclose(actual, expected, rtol=0, atol=ATOL)
        np.testing.assert_allclose(actual.conj().T @ actual, np.eye(16), rtol=0, atol=ATOL)
        np.testing.assert_allclose(actual[:, [0, 8]], np.eye(16)[:, [0, 8]], rtol=0, atol=ATOL)

    def test_rotation_resources_and_register_roles(self):
        circuit = hhl_reciprocal_rotation()
        self.assertEqual(circuit.num_qubits, 4)
        self.assertEqual([(reg.name, len(reg)) for reg in circuit.qregs],
                         [("count", 3), ("success", 1)])
        self.assertEqual(circuit.num_clbits, 0)
        self.assertEqual(circuit.num_ancillas, 0)
        self.assertEqual(len(circuit.data), 7)
        self.assertTrue(all(item.operation.num_ctrl_qubits == 3 for item in circuit.data))


class HHLMathematicsTests(unittest.TestCase):
    def assert_full_output(self, matrix, rhs, failure):
        """Check raw branches before normalization; never fit a phase or scale."""
        state = Statevector.from_instruction(hhl_circuit(matrix, rhs))
        branches = state.data.reshape(2, 2, 8)  # success, system, count
        raw_solution = np.linalg.solve(matrix, rhs)
        probability = float(np.vdot(raw_solution, raw_solution).real)
        expected = np.zeros((2, 2, 8), dtype=complex)
        expected[0, :, 0], expected[1, :, 0] = failure, raw_solution
        np.testing.assert_allclose(branches, expected, rtol=0, atol=ATOL)
        np.testing.assert_allclose(branches[1, :, 0], raw_solution, rtol=0, atol=ATOL)
        np.testing.assert_allclose(branches[0, :, 0], failure, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.linalg.norm(state.data)**2, 1, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.linalg.norm(branches[1])**2,
                                   probability, rtol=0, atol=ATOL)
        np.testing.assert_allclose(np.linalg.norm(branches[0])**2,
                                   1 - probability, rtol=0, atol=ATOL)
        self.assertGreaterEqual(probability, 1 / 49 - ATOL)
        self.assertLessEqual(probability, 1 + ATOL)
        for flag in (0, 1):
            self.assertLessEqual(np.linalg.norm(branches[flag, :, 1:]), 1e-9)
        self.assertLessEqual(np.linalg.norm(branches[:, :, 1:]), 1e-9)
        # Only now form the conditioned vector, with independently checked raw p.
        conditioned = branches[1, :, 0] / np.sqrt(probability)
        np.testing.assert_allclose(conditioned, raw_solution / np.sqrt(probability),
                                   rtol=0, atol=CONDITIONED_ATOL)
        np.testing.assert_allclose(np.linalg.norm(conditioned), 1, rtol=0, atol=CONDITIONED_ATOL)
        return probability, conditioned

    def test_default_signed_solution_and_closed_failure_branch(self):
        probability, conditioned = self.assert_full_output(A0, ZERO, np.sqrt(3) / 4 * np.ones(2))
        np.testing.assert_allclose(probability, 5 / 8, rtol=0, atol=ATOL)
        np.testing.assert_allclose(conditioned, np.array([3, -1]) / np.sqrt(10),
                                   rtol=0, atol=CONDITIONED_ATOL)
        for basis, expected in [("X", -3 / 5), ("Z", 4 / 5)]:
            np.testing.assert_allclose(np.vdot(conditioned, PAULIS[basis] @ conditioned),
                                       expected, rtol=0, atol=ATOL)

    def test_second_basis_rhs(self):
        probability, conditioned = self.assert_full_output(A0, [0, 1], np.sqrt(3) / 4 * np.ones(2))
        np.testing.assert_allclose(probability, 5 / 8, rtol=0, atol=ATOL)
        np.testing.assert_allclose(conditioned, np.array([-1, 3]) / np.sqrt(10),
                                   rtol=0, atol=CONDITIONED_ATOL)

    def test_eigenstates_and_zero_failure_branch(self):
        for rhs, failure, expected_probability in [(PLUS, np.sqrt(3) / 2 * PLUS, 1 / 4),
                                                   (MINUS, np.zeros(2), 1)]:
            with self.subTest(rhs=rhs):
                probability, conditioned = self.assert_full_output(A0, rhs, failure)
                np.testing.assert_allclose(probability, expected_probability, rtol=0, atol=ATOL)
                np.testing.assert_allclose(conditioned, rhs, rtol=0, atol=CONDITIONED_ATOL)

    def test_complex_relative_phase_and_observables(self):
        failure = np.sqrt(3) * (1 + 1j) / (4 * np.sqrt(2)) * np.ones(2)
        probability, conditioned = self.assert_full_output(A0, COMPLEX_RHS, failure)
        np.testing.assert_allclose(probability, 5 / 8, rtol=0, atol=ATOL)
        np.testing.assert_allclose(conditioned, np.array([3 - 1j, -1 + 3j]) / np.sqrt(20),
                                   rtol=0, atol=CONDITIONED_ATOL)
        for basis, expected in [("X", -3 / 5), ("Y", 4 / 5), ("Z", 0)]:
            np.testing.assert_allclose(np.vdot(conditioned, PAULIS[basis] @ conditioned),
                                       expected, rtol=0, atol=ATOL)

    def test_explicit_scaling_changes_probability(self):
        # Eigenvectors are |->, |+>; eigenvalues of 2*A0 are 2 and 4.
        failure = (np.sqrt(3) / 2 * MINUS + np.sqrt(15) / 4 * PLUS) / np.sqrt(2)
        probability, conditioned = self.assert_full_output(2 * A0, ZERO, failure)
        np.testing.assert_allclose(probability, 5 / 32, rtol=0, atol=ATOL)
        np.testing.assert_allclose(conditioned, np.array([3, -1]) / np.sqrt(10),
                                   rtol=0, atol=CONDITIONED_ATOL)

    def test_alternate_matrix(self):
        matrix = np.array([[2, 1], [1, 2]])
        probability, conditioned = self.assert_full_output(matrix, ZERO, np.sqrt(2) / 3 * np.ones(2))
        np.testing.assert_allclose(probability, 5 / 9, rtol=0, atol=ATOL)
        np.testing.assert_allclose(conditioned, np.array([2, -1]) / np.sqrt(5),
                                   rtol=0, atol=CONDITIONED_ATOL)

    def test_scalar_matrices_preserve_global_evolution_phase(self):
        rhs = np.exp(0.37j) * COMPLEX_RHS
        for eigenvalue in (1, 3, 7):
            with self.subTest(eigenvalue=eigenvalue):
                failure = np.sqrt(1 - 1 / eigenvalue**2) * rhs
                probability, conditioned = self.assert_full_output(eigenvalue * np.eye(2), rhs, failure)
                np.testing.assert_allclose(probability, 1 / eigenvalue**2, rtol=0, atol=ATOL)
                np.testing.assert_allclose(conditioned, rhs, rtol=0, atol=CONDITIONED_ATOL)

    def test_all_28_spectral_pairs_complex_eigenbases_and_states(self):
        rng = np.random.default_rng(2026)
        pairs = list(combinations_with_replacement(range(1, 8), 2))
        self.assertEqual(len(pairs), 28)
        for pair in pairs:
            eigenvalues = np.array(pair, dtype=float)
            basis, _ = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))
            rhs = rng.normal(size=2) + 1j * rng.normal(size=2)
            rhs /= np.linalg.norm(rhs)  # Normalize the generated input, never the raw output.
            matrix = (basis * eigenvalues) @ basis.conj().T
            # Known exact generator eigenvalues avoid cancellation at lambda=1.
            failure = (basis * np.sqrt(1 - eigenvalues**-2)) @ basis.conj().T @ rhs
            with self.subTest(eigenvalues=pair):
                self.assert_full_output(matrix, rhs, failure)

    def test_seeded_v2_success_and_conditional_xyz_same_shot(self):
        shots = 4096
        for rhs in (ZERO, COMPLEX_RHS):
            solution = np.linalg.solve(A0, rhs)
            probability = float(np.vdot(solution, solution).real)
            solution /= np.sqrt(probability)  # Independent classical expectation only.
            circuit = hhl_circuit(A0, rhs)
            results = StatevectorSampler(seed=2026).run(
                [sampled_basis(circuit, basis) for basis in PAULIS], shots=shots
            ).result()
            for basis, result in zip(PAULIS, results, strict=True):
                flags = result.data.flag_readout.get_bitstrings()
                system = result.data.system_readout.get_bitstrings()
                self.assertEqual(len(flags), shots)
                self.assertEqual(len(system), shots)
                selected = [int(bit) for flag, bit in zip(flags, system, strict=True) if flag == "1"]
                with self.subTest(rhs=rhs, basis=basis):
                    self.assertGreater(len(selected), 0, "No successful shots: estimate is undefined")
                    self.assertLessEqual(abs(len(selected) / shots - probability),
                                         6 * np.sqrt(probability * (1 - probability) / shots) + 1 / shots)
                    expectation = float(np.vdot(solution, PAULIS[basis] @ solution).real)
                    p_one = (1 - expectation) / 2
                    estimate = 1 - 2 * np.mean(selected)
                    selected_count = len(selected)
                    bound = 2 * (6 * np.sqrt(p_one * (1 - p_one) / selected_count) + 1 / selected_count)
                    self.assertLessEqual(abs(estimate - expectation), bound)


if __name__ == "__main__":
    unittest.main()
