"""Independent spectral, phase-distribution, register, and V2 checks for QPE."""

import unittest

import numpy as np
from qiskit import ClassicalRegister, QuantumCircuit
from qiskit.circuit import Gate, Instruction, Parameter
from qiskit.circuit.library import PhaseGate, StatePreparation, UnitaryGate, phase_estimation
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Operator, Statevector

from src.phys3810.qpe import qpe_circuit


ATOL = 2e-11


def amplitudes(phi, width):
    size = 2**width
    delta = phi - np.arange(size) / size
    return np.exp(2j * np.pi * np.outer(delta, np.arange(size))).mean(axis=1)


def sine_probabilities(phi, width):
    """Closed sine-ratio expression, independent of the Fourier sum/circuit."""
    size = 2**width
    delta = (phi - np.arange(size) / size + 0.5) % 1 - 0.5
    result = np.empty(size)
    exact = np.abs(delta) < 1e-14
    result[exact] = 1
    result[~exact] = (np.sin(np.pi * size * delta[~exact])
                      / (size * np.sin(np.pi * delta[~exact]))) ** 2
    return result


def spectral_fixture(target_width):
    if target_width == 1:
        basis = np.array([[1, 1], [1j, -1j]]) / np.sqrt(2)
        phases = np.array([1 / 8, 3 / 8])
    else:
        basis = np.array([[1, 0, 0, 1], [0, 1, 1j, 0],
                          [0, 1j, 1, 0], [1j, 0, 0, -1j]]) / np.sqrt(2)
        phases = np.array([1 / 8, 3 / 8, 5 / 8, 7 / 8])
    matrix = (basis * np.exp(2j * np.pi * phases)) @ basis.conj().T
    return basis, phases, matrix


def prepared(width, unitary, target_state):
    block = qpe_circuit(width, unitary)
    circuit = QuantumCircuit(*block.qregs)
    circuit.append(StatePreparation(target_state), range(width, circuit.num_qubits))
    circuit.compose(block, inplace=True)
    return circuit


def measured_count(circuit, width):
    sampled = circuit.copy()
    phase = ClassicalRegister(width, "phase")
    sampled.add_register(phase)
    sampled.measure(range(width), phase)
    return sampled


class QPEInputTests(unittest.TestCase):
    def test_counting_width_type(self):
        for value in [True, False, np.bool_(True), 3.0, "3", None]:
            with self.subTest(value=value), self.assertRaises(TypeError):
                qpe_circuit(value, PhaseGate(0.2))

    def test_counting_width_range(self):
        for value in [-1, 0, 7, 20]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                qpe_circuit(value, PhaseGate(0.2))

    def test_unitary_type(self):
        for value in [np.eye(2), [[1, 0], [0, 1]], Operator(np.eye(2)),
                      Instruction("opaque", 1, 0, []), None, "phase"]:
            with self.subTest(value=type(value)), self.assertRaises(TypeError):
                qpe_circuit(3, value)

    def test_target_width(self):
        for value in [QuantumCircuit(0), QuantumCircuit(3), UnitaryGate(np.eye(8))]:
            with self.subTest(width=value.num_qubits), self.assertRaises(ValueError):
                qpe_circuit(3, value)

    def test_non_gate_or_classical_circuit(self):
        circuits = [QuantumCircuit(1, 1)]
        measured = QuantumCircuit(1, 1)
        measured.measure(0, 0)
        circuits.append(measured)
        for operation in ["reset", "barrier", "initialize"]:
            circuit = QuantumCircuit(1)
            if operation == "initialize":
                circuit.initialize([1, 0], 0)
            else:
                getattr(circuit, operation)(0)
            circuits.append(circuit)
        for circuit in circuits:
            with self.subTest(circuit=circuit), self.assertRaises(ValueError):
                qpe_circuit(3, circuit)

    def test_unbound_parameters(self):
        angle = Parameter("angle")
        circuit = QuantumCircuit(1)
        circuit.p(angle, 0)
        for value in [circuit, PhaseGate(angle)]:
            with self.subTest(value=type(value)), self.assertRaises(ValueError):
                qpe_circuit(3, value)

    def test_nonfinite_or_nonunitary_matrix(self):
        for matrix in [np.diag([1, 2]), np.diag([1, np.nan]), np.diag([1, np.inf]),
                       np.diag([1, 1 + 1e-9])]:
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                qpe_circuit(3, UnitaryGate(matrix, check_input=False))

    def test_opaque_gate_is_rejected(self):
        with self.assertRaises(ValueError):
            qpe_circuit(3, Gate("opaque", 1, []))

    def test_integer_scalar_and_bound_parameter(self):
        angle = Parameter("angle")
        circuit = QuantumCircuit(1)
        circuit.p(angle, 0)
        bound = circuit.assign_parameters({angle: 0.75})
        np.testing.assert_allclose(
            Operator(qpe_circuit(np.int64(3), bound)).data,
            Operator(qpe_circuit(3, PhaseGate(0.75))).data, rtol=0, atol=ATOL,
        )

    def test_input_is_not_mutated_or_retained_by_reference(self):
        unitary = QuantumCircuit(1)
        unitary.p(0.3, 0)
        before = unitary.copy()
        block = qpe_circuit(3, unitary)
        self.assertEqual(unitary, before)
        expected = Operator(block).data.copy()
        unitary.x(0)
        np.testing.assert_allclose(Operator(block).data, expected, rtol=0, atol=ATOL)

    def test_register_roles_and_no_measurement_or_ancillas(self):
        for width in range(1, 7):
            for targets in (1, 2):
                circuit = qpe_circuit(width, QuantumCircuit(targets))
                with self.subTest(width=width, targets=targets):
                    self.assertEqual([(r.name, len(r)) for r in circuit.qregs],
                                     [("count", width), ("target", targets)])
                    self.assertEqual(circuit.num_clbits, 0)
                    self.assertEqual(circuit.num_ancillas, 0)
                    self.assertNotIn("measure", circuit.count_ops())


class QPEMathematicsTests(unittest.TestCase):
    def test_full_operator_from_independent_spectral_construction(self):
        for targets in (1, 2):
            basis, phases, unitary = spectral_fixture(targets)
            for width in (1, 2, 3):
                size = 2**width
                x = np.arange(size)
                fourier = np.exp(2j * np.pi * np.outer(x, x) / size) / np.sqrt(size)
                hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
                initial_h = np.ones((1, 1))
                for _ in range(width):
                    initial_h = np.kron(initial_h, hadamard)
                expected = np.zeros((size * 2**targets,) * 2, dtype=complex)
                for index, phi in enumerate(phases):
                    projector = np.outer(basis[:, index], basis[:, index].conj())
                    phase_block = fourier.conj().T @ np.diag(np.exp(2j * np.pi * phi * x)) @ initial_h
                    expected += np.kron(projector, phase_block)
                with self.subTest(targets=targets, width=width):
                    np.testing.assert_allclose(
                        Operator(qpe_circuit(width, UnitaryGate(unitary))).data,
                        expected, rtol=0, atol=ATOL,
                    )

    def test_asymmetric_exact_phases(self):
        for phi, label in [(1 / 8, "001"), (3 / 8, "011"), (6 / 8, "110")]:
            state = Statevector.from_instruction(prepared(3, PhaseGate(2 * np.pi * phi), [0, 1]))
            expected = np.zeros(8)
            expected[int(label, 2)] = 1
            with self.subTest(phi=phi):
                np.testing.assert_allclose(state.probabilities([0, 1, 2]), expected, rtol=0, atol=ATOL)
                np.testing.assert_allclose(state.data, np.kron([0, 1], expected), rtol=0, atol=ATOL)

    def test_all_supported_precisions_and_target_widths(self):
        for width in range(1, 7):
            size = 2**width
            phi = 1 / size
            for targets in (1, 2):
                vector = np.zeros(2**targets, dtype=complex)
                vector[0], vector[-1] = 1 / np.sqrt(2), 1j / np.sqrt(2)
                unitary = UnitaryGate(np.exp(2j * np.pi * phi) * np.eye(2**targets))
                state = Statevector.from_instruction(prepared(width, unitary, vector))
                expected = np.zeros(size)
                expected[1] = 1
                with self.subTest(width=width, targets=targets):
                    np.testing.assert_allclose(state.data, np.kron(vector, expected), rtol=0, atol=ATOL)

    def test_nonexact_distribution_and_target_preservation(self):
        target = np.array([1, 1j]) / np.sqrt(2)
        other = np.array([1, -1j]) / np.sqrt(2)
        for phi in [1 / 3, 0.31, -1 / 7, 0.97]:
            matrix = (np.exp(2j * np.pi * phi) * np.outer(target, target.conj())
                      + np.outer(other, other.conj()))
            for width in (2, 3, 5):
                state = Statevector.from_instruction(prepared(width, UnitaryGate(matrix), target))
                with self.subTest(phi=phi, width=width):
                    np.testing.assert_allclose(state.probabilities(list(range(width))),
                                               sine_probabilities(phi, width), rtol=0, atol=ATOL)
                    np.testing.assert_allclose(state.data, np.kron(target, amplitudes(phi, width)),
                                               rtol=0, atol=ATOL)
                    np.testing.assert_allclose(np.vdot(state.data, state.data), 1, rtol=0, atol=ATOL)

    def test_complex_entangled_two_qubit_eigenstates(self):
        basis, phases, matrix = spectral_fixture(2)
        for index, phi in enumerate(phases):
            state = Statevector.from_instruction(prepared(3, UnitaryGate(matrix), basis[:, index]))
            with self.subTest(index=index):
                np.testing.assert_allclose(state.data, np.kron(basis[:, index], amplitudes(phi, 3)),
                                           rtol=0, atol=ATOL)

    def test_negative_exact_phase_wraps_modulo_one(self):
        state = Statevector.from_instruction(prepared(3, PhaseGate(-2 * np.pi / 8), [0, 1]))
        expected = np.zeros(8)
        expected[7] = 1
        np.testing.assert_allclose(state.probabilities([0, 1, 2]), expected, rtol=0, atol=ATOL)

    def test_zero_and_full_turn_have_zero_phase(self):
        for unitary in [QuantumCircuit(1), PhaseGate(0), PhaseGate(2 * np.pi)]:
            state = Statevector.from_instruction(prepared(3, unitary, [0, 1]))
            expected = np.zeros(8)
            expected[0] = 1
            np.testing.assert_allclose(state.probabilities([0, 1, 2]), expected, rtol=0, atol=ATOL)

    def test_circuit_global_phase_changes_counting_result(self):
        unitary = QuantumCircuit(1, global_phase=2 * np.pi * 3 / 8)
        target = np.array([1, 1j]) / np.sqrt(2)
        state = Statevector.from_instruction(prepared(3, unitary, target))
        expected = np.zeros(8)
        expected[3] = 1
        np.testing.assert_allclose(state.data, np.kron(target, expected), rtol=0, atol=ATOL)

    def test_non_eigenstate_has_weighted_phase_distribution(self):
        basis, phases, matrix = spectral_fixture(1)
        coefficients = np.array([0.5, 1j * np.sqrt(0.75)])
        state = Statevector.from_instruction(prepared(3, UnitaryGate(matrix), basis @ coefficients))
        expected_state = sum(coefficients[j] * np.kron(basis[:, j], amplitudes(phi, 3))
                             for j, phi in enumerate(phases))
        expected_probabilities = sum(abs(coefficients[j])**2 * sine_probabilities(phi, 3)
                                     for j, phi in enumerate(phases))
        np.testing.assert_allclose(state.data, expected_state, rtol=0, atol=ATOL)
        np.testing.assert_allclose(state.probabilities([0, 1, 2]), expected_probabilities,
                                   rtol=0, atol=ATOL)

    def test_sdk_reference_with_explicit_output_reversal(self):
        for targets in (1, 2):
            _, _, matrix = spectral_fixture(targets)
            for width in (2, 3, 4):
                unitary = UnitaryGate(matrix)
                circuit_input = QuantumCircuit(targets)
                circuit_input.append(unitary, range(targets))
                for input_unitary in [unitary, circuit_input]:
                    reference = phase_estimation(width, input_unitary)
                    canonical = Operator(qpe_circuit(width, input_unitary)).data
                    reversed_rows = [int(format(j, f"0{width}b")[::-1], 2) for j in range(2**width)]
                    reversal = np.kron(np.eye(2**targets), np.eye(2**width)[reversed_rows])
                    with self.subTest(width=width, targets=targets, kind=type(input_unitary)):
                        np.testing.assert_allclose(Operator(reference).data, reversal @ canonical,
                                                   rtol=0, atol=ATOL)
                        for low in range(width // 2):
                            reference.swap(low, width - low - 1)
                        np.testing.assert_allclose(Operator(reference).data, canonical, rtol=0, atol=ATOL)

    def test_exact_v2_counts_measure_only_counting_register(self):
        for phi, label in [(1 / 8, "001"), (3 / 8, "011"), (6 / 8, "110")]:
            circuit = prepared(3, PhaseGate(2 * np.pi * phi), [0, 1])
            counts = StatevectorSampler(seed=2026).run(
                [measured_count(circuit, 3)], shots=256
            ).result()[0].data.phase.get_counts()
            with self.subTest(phi=phi):
                self.assertEqual(counts, {label: 256})
                self.assertEqual(circuit.num_clbits, 0)

    def test_nonexact_v2_frequencies(self):
        width, shots, phi = 3, 4096, 1 / 3
        circuit = prepared(width, PhaseGate(2 * np.pi * phi), [0, 1])
        counts = StatevectorSampler(seed=2026).run(
            [measured_count(circuit, width)], shots=shots
        ).result()[0].data.phase.get_counts()
        expected = sine_probabilities(phi, width)
        observed = np.array([counts.get(format(y, "03b"), 0) / shots for y in range(8)])
        self.assertEqual(sum(counts.values()), shots)
        self.assertTrue(all(len(label) == width for label in counts))
        self.assertTrue(np.all(np.abs(observed - expected)
                               <= 6 * np.sqrt(expected * (1 - expected) / shots) + 1 / shots))


if __name__ == "__main__":
    unittest.main()
