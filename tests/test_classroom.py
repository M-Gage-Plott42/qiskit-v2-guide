"""Independent small mathematical checks for the credential-free classroom stack."""

import unittest

import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import SparsePauliOp, Statevector
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import EstimatorV2, SamplerV2


def bell_circuit():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit


class ClassroomMathematicsTests(unittest.TestCase):
    def test_bell_amplitudes_and_normalization(self):
        state = Statevector.from_instruction(bell_circuit())
        # Basis order is |00>, |01>, |10>, |11>. Check the relative sign too.
        expected = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
        np.testing.assert_allclose(state.data, expected, rtol=0, atol=1e-12)
        self.assertAlmostEqual(float(np.vdot(state.data, state.data).real), 1.0)

    def test_bell_probabilities_and_correlations(self):
        state = Statevector.from_instruction(bell_circuit())
        np.testing.assert_allclose(state.probabilities(), [0.5, 0, 0, 0.5], rtol=0, atol=1e-12)
        for pauli, expected in (("ZZ", 1), ("XX", 1), ("ZI", 0)):
            with self.subTest(pauli=pauli):
                actual = state.expectation_value(SparsePauliOp(pauli))
                self.assertAlmostEqual(actual.real, expected)
                self.assertAlmostEqual(actual.imag, 0)

    def test_little_endian_qubit_and_count_order(self):
        # Bell alone is symmetric and cannot reveal a reversed bit convention.
        circuit = QuantumCircuit(2)
        circuit.x(0)
        np.testing.assert_allclose(
            Statevector.from_instruction(circuit).probabilities(), [0, 1, 0, 0], rtol=0, atol=1e-12
        )
        circuit.measure_all()
        counts = StatevectorSampler(seed=17).run([circuit], shots=32).result()[0].data.meas.get_counts()
        self.assertEqual(counts, {"01": 32})

    def assert_bell_counts(self, counts, shots):
        self.assertEqual(sum(counts.values()), shots)
        self.assertEqual(set(counts), {"00", "11"})
        self.assertTrue(all(isinstance(count, int) and count > 0 for count in counts.values()))
        # Six binomial standard deviations; do not require identical random counts.
        self.assertLessEqual(abs(counts["00"] - shots / 2), 6 * np.sqrt(shots * 0.25))

    def test_reference_sampler_bell_counts(self):
        circuit = bell_circuit()
        circuit.measure_all()
        result = StatevectorSampler(seed=1234).run([circuit], shots=1024).result()[0]
        self.assert_bell_counts(result.data.meas.get_counts(), 1024)
        self.assertEqual(len(result.data.meas.get_bitstrings()), 1024)

    def test_aer_sampler_bell_counts(self):
        backend = AerSimulator()
        circuit = bell_circuit()
        circuit.measure_all()
        manager = generate_preset_pass_manager(backend=backend, optimization_level=1, seed_transpiler=17)
        isa = manager.run(circuit)
        sampler = SamplerV2.from_backend(backend, seed=1234)
        result = sampler.run([isa], shots=1024).result()[0]
        self.assert_bell_counts(result.data.meas.get_counts(), 1024)

    def test_aer_estimator_bell_zz(self):
        backend = AerSimulator()
        manager = generate_preset_pass_manager(backend=backend, optimization_level=1, seed_transpiler=17)
        circuit = manager.run(bell_circuit())
        observable = SparsePauliOp("ZZ").apply_layout(circuit.layout)
        result = EstimatorV2.from_backend(backend).run([(circuit, observable)]).result()[0]
        np.testing.assert_allclose(result.data.evs, 1.0, rtol=0, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
