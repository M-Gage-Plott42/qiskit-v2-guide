"""Independent exact Fourier, inverse, bit-order, and sampling checks."""

import unittest

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Operator, Statevector

from src.phys3810.qft import qft_circuit


ATOL = 1e-12


def fourier_matrix(num_qubits):
    size = 2**num_qubits
    indices = np.arange(size)
    return np.exp(2j * np.pi * np.outer(indices, indices) / size) / np.sqrt(size)


def reversed_indices(num_qubits):
    return [int(format(index, f"0{num_qubits}b")[::-1], 2) for index in range(2**num_qubits)]


class QFTInputTests(unittest.TestCase):
    def test_integer_qubit_count_required(self):
        for value in [True, False, np.bool_(True), 2.0, "3", None, 2j]:
            with self.subTest(value=value), self.assertRaises(TypeError):
                qft_circuit(value)

    def test_supported_range(self):
        for value in [-1, 0, 7, 32]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                qft_circuit(value)

    def test_flags_are_boolean(self):
        for flag in ["inverse", "do_swaps"]:
            for value in [0, 1, 0.0, "False", None, np.bool_(True)]:
                with self.subTest(flag=flag, value=value), self.assertRaises(TypeError):
                    qft_circuit(3, **{flag: value})

    def test_numpy_integer_is_supported(self):
        np.testing.assert_allclose(
            Operator(qft_circuit(np.int64(3))).data, fourier_matrix(3), rtol=0, atol=ATOL
        )

    def test_circuits_are_unmeasured_and_ancilla_free(self):
        for n in range(1, 7):
            for inverse in [False, True]:
                for swaps in [False, True]:
                    circuit = qft_circuit(n, inverse=inverse, do_swaps=swaps)
                    with self.subTest(n=n, inverse=inverse, swaps=swaps):
                        self.assertEqual(circuit.num_qubits, n)
                        self.assertEqual(circuit.num_clbits, 0)
                        self.assertEqual(circuit.num_ancillas, 0)
                        self.assertNotIn("measure", circuit.count_ops())


class QFTMathematicsTests(unittest.TestCase):
    def test_full_positive_fourier_matrix(self):
        for n in range(1, 7):
            with self.subTest(n=n):
                np.testing.assert_allclose(Operator(qft_circuit(n)).data, fourier_matrix(n), rtol=0, atol=ATOL)

    def test_full_inverse_fourier_matrix(self):
        for n in range(1, 7):
            with self.subTest(n=n):
                np.testing.assert_allclose(
                    Operator(qft_circuit(n, inverse=True)).data,
                    fourier_matrix(n).conj().T, rtol=0, atol=ATOL,
                )

    def test_no_swaps_is_row_reversal_of_forward_transform(self):
        for n in range(1, 7):
            expected = fourier_matrix(n)[reversed_indices(n), :]
            with self.subTest(n=n):
                np.testing.assert_allclose(
                    Operator(qft_circuit(n, do_swaps=False)).data, expected, rtol=0, atol=ATOL
                )

    def test_no_swaps_inverse_reverses_input_not_output(self):
        for n in range(1, 7):
            expected = fourier_matrix(n).conj().T[:, reversed_indices(n)]
            with self.subTest(n=n):
                np.testing.assert_allclose(
                    Operator(qft_circuit(n, inverse=True, do_swaps=False)).data,
                    expected, rtol=0, atol=ATOL,
                )

    def test_inverse_composition_both_orders(self):
        for n in range(1, 7):
            for swaps in [False, True]:
                forward = qft_circuit(n, do_swaps=swaps)
                inverse = qft_circuit(n, inverse=True, do_swaps=swaps)
                for circuit in [forward.compose(inverse), inverse.compose(forward)]:
                    with self.subTest(n=n, swaps=swaps, first=circuit.name):
                        np.testing.assert_allclose(Operator(circuit).data, np.eye(2**n), rtol=0, atol=ATOL)

    def test_complex_state_evolution_and_normalization(self):
        rng = np.random.default_rng(2026)
        for n in range(1, 7):
            data = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
            data /= np.linalg.norm(data)
            for swaps in [False, True]:
                expected = fourier_matrix(n)
                if not swaps:
                    expected = expected[reversed_indices(n), :]
                state = Statevector(data).evolve(qft_circuit(n, do_swaps=swaps))
                recovered = state.evolve(qft_circuit(n, inverse=True, do_swaps=swaps))
                with self.subTest(n=n, swaps=swaps):
                    np.testing.assert_allclose(state.data, expected @ data, rtol=0, atol=ATOL)
                    np.testing.assert_allclose(np.vdot(state.data, state.data), 1, rtol=0, atol=ATOL)
                    np.testing.assert_allclose(recovered.data, data, rtol=0, atol=ATOL)

    def test_asymmetric_basis_phase_ramps(self):
        for n in range(3, 7):
            for basis_index in [1, 3, 6]:
                circuit = QuantumCircuit(n)
                for qubit in range(n):
                    if (basis_index >> qubit) & 1:
                        circuit.x(qubit)
                circuit.compose(qft_circuit(n), inplace=True)
                expected = np.exp(2j * np.pi * basis_index * np.arange(2**n) / 2**n) / np.sqrt(2**n)
                state = Statevector.from_instruction(circuit)
                with self.subTest(n=n, basis_index=basis_index):
                    np.testing.assert_allclose(state.data, expected, rtol=0, atol=ATOL)
                    np.testing.assert_allclose(state.probabilities(), np.full(2**n, 1 / 2**n), rtol=0, atol=ATOL)

    def test_current_sdk_reference_agrees_exactly(self):
        for n in range(1, 7):
            for inverse in [False, True]:
                reference = QFTGate(n)
                if inverse:
                    reference = reference.inverse()
                with self.subTest(n=n, inverse=inverse):
                    np.testing.assert_allclose(
                        Operator(qft_circuit(n, inverse=inverse)).data,
                        Operator(reference).data, rtol=0, atol=ATOL,
                    )

    def test_inverse_decodes_known_phase_gradient_with_v2_sampling(self):
        # Preparation is independently factored into single-qubit phases.
        # This is a known input state, not a QPE implementation or free data loading.
        for integer in [1, 3, 6]:
            circuit = QuantumCircuit(3)
            for qubit in range(3):
                circuit.h(qubit)
                circuit.p(2 * np.pi * integer * 2**qubit / 8, qubit)
            circuit.compose(qft_circuit(3, inverse=True), inplace=True)
            expected = np.zeros(8)
            expected[integer] = 1
            with self.subTest(integer=integer):
                np.testing.assert_allclose(Statevector.from_instruction(circuit).probabilities(), expected, rtol=0, atol=ATOL)
                sampled = circuit.measure_all(inplace=False)
                counts = StatevectorSampler(seed=2026).run([sampled], shots=128).result()[0].data.meas.get_counts()
                self.assertEqual(counts, {format(integer, "03b"): 128})
                self.assertEqual(circuit.num_clbits, 0)


if __name__ == "__main__":
    unittest.main()
