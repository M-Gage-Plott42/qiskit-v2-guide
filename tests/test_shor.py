"""Independent domain, coherent-state, recovery, and failure checks for N=15."""

import cmath
from fractions import Fraction
from math import gcd, pi
import unittest
from unittest.mock import patch

import numpy as np
from qiskit import ClassicalRegister
from qiskit.circuit.library import UnitaryGate
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Operator, Statevector

from src.phys3810.qpe import qpe_circuit
from src.phys3810.shor import (
    classical_factor_15, factors_from_order_15, modular_multiplier_15,
    order_finding_15, recover_order_15,
)


ATOL = 2e-11
# Independently enumerated finite fixtures; no such order table belongs in source.
ORDERS = {1: 1, 2: 4, 4: 2, 7: 4, 8: 4, 11: 2, 13: 4, 14: 2}
ORBITS = {1: [1], 2: [1, 2, 4, 8], 4: [1, 4], 7: [1, 7, 4, 13],
          8: [1, 8, 4, 2], 11: [1, 11], 13: [1, 13, 4, 7], 14: [1, 14]}


def independent_joint(base, width):
    """Literal modular-exponent/Fourier sum, independent of circuit construction."""
    size = 2**width
    expected = np.zeros((16, size), dtype=complex)
    for exponent in range(size):
        residue = pow(base, exponent, 15)
        for outcome in range(size):
            expected[residue, outcome] += cmath.exp(-2j*pi*exponent*outcome/size) / size
    return expected


def permutation_reference(multiplier):
    # Repeated integer addition defines each image independently of gate storage.
    expected = np.zeros((16, 16), dtype=complex)
    for source in range(15):
        destination = sum([source] * multiplier) % 15
        expected[destination, source] = 1
    expected[15, 15] = 1
    return expected


class ShorInputTests(unittest.TestCase):
    def test_integer_types_across_public_interfaces(self):
        calls = [modular_multiplier_15, order_finding_15, classical_factor_15,
                 lambda x: recover_order_15(x, "0100"),
                 lambda x: factors_from_order_15(x, 4),
                 lambda x: factors_from_order_15(2, x),
                 lambda x: order_finding_15(2, num_counting_qubits=x)]
        for value in [True, np.bool_(True), 2.0, "2", None, [], np.array([2])]:
            for call in calls:
                with self.subTest(value=repr(value), call=call), self.assertRaises(TypeError):
                    call(value)

    def test_out_of_range_bases_and_multipliers(self):
        for base in [-15, -1, 0, 15, 16, 29]:
            for call in [modular_multiplier_15, order_finding_15, classical_factor_15,
                         lambda x: recover_order_15(x, "0100"),
                         lambda x: factors_from_order_15(x, 4)]:
                with self.subTest(base=base), self.assertRaises(ValueError):
                    call(base)

    def test_noncoprime_bases_rejected_by_quantum_and_recovery(self):
        for base in [3, 5, 6, 9, 10, 12]:
            for call in [modular_multiplier_15, order_finding_15,
                         lambda x: recover_order_15(x, "0100"),
                         lambda x: factors_from_order_15(x, 4)]:
                with self.subTest(base=base), self.assertRaises(ValueError):
                    call(base)

    def test_counting_width_ranges(self):
        for width in [-1, 0, 1, 2, 3, 7, 20]:
            with self.subTest(width=width), self.assertRaises(ValueError):
                order_finding_15(2, num_counting_qubits=width)

    def test_recovery_bitstring_validation(self):
        for outcome in [0, True, None, [0, 1, 0, 0], b"0100"]:
            with self.subTest(outcome=outcome), self.assertRaises(TypeError):
                recover_order_15(2, outcome)
        for outcome in ["", "010", "0000100", "01 00", "0x10", "0102", "0100\n", "-100"]:
            with self.subTest(outcome=outcome), self.assertRaises(ValueError):
                recover_order_15(2, outcome)

    def test_order_range_validation(self):
        for order in [-1, 0, 15, 16, 100]:
            with self.subTest(order=order), self.assertRaises(ValueError):
                factors_from_order_15(2, order)

    def test_numpy_integer_acceptance_and_scalar_immutability(self):
        base, width = np.int64(2), np.int32(4)
        self.assertEqual(order_finding_15(base, num_counting_qubits=width).num_qubits, 8)
        self.assertEqual(recover_order_15(base, "0100"), 4)
        self.assertIs(type(recover_order_15(base, "0100")), int)
        self.assertEqual(factors_from_order_15(base, np.int64(4)), (3, 5))
        self.assertEqual(classical_factor_15(np.int64(6)), (3, 5))
        self.assertEqual(modular_multiplier_15(base).num_qubits, 4)
        self.assertEqual((base, width), (2, 4))


class ModularPermutationTests(unittest.TestCase):
    def test_all_128_basis_images_with_positive_phase(self):
        for multiplier in ORDERS:
            with self.subTest(multiplier=multiplier):
                actual = Operator(modular_multiplier_15(multiplier)).data
                np.testing.assert_allclose(actual, permutation_reference(multiplier), rtol=0, atol=ATOL)
                np.testing.assert_allclose(actual.conj().T @ actual, np.eye(16), rtol=0, atol=ATOL)
                self.assertEqual(set(np.argmax(abs(actual), axis=0)), set(range(16)))
                # Complementing all four bits would fail these two fixed states.
                np.testing.assert_allclose(actual[:, [0, 15]], np.eye(16)[:, [0, 15]], rtol=0, atol=ATOL)

    def test_group_composition_and_inverse_on_full_domain(self):
        matrices = {b: Operator(modular_multiplier_15(b)).data for b in ORDERS}
        for a in ORDERS:
            np.testing.assert_allclose(matrices[a].conj().T,
                                       permutation_reference(pow(a, -1, 15)), rtol=0, atol=ATOL)
            for b in ORDERS:
                with self.subTest(a=a, b=b):
                    np.testing.assert_allclose(matrices[a] @ matrices[b],
                                               permutation_reference(a*b % 15), rtol=0, atol=ATOL)

    def test_all_256_controlled_basis_images_and_control_coherence(self):
        for multiplier in ORDERS:
            actual = Operator(modular_multiplier_15(multiplier).control(annotated=False)).data
            expected = np.kron(np.eye(16), np.diag([1, 0])) + np.kron(
                permutation_reference(multiplier), np.diag([0, 1])
            )
            with self.subTest(multiplier=multiplier):
                np.testing.assert_allclose(actual, expected, rtol=0, atol=ATOL)
                for residue in range(16):
                    initial = np.zeros(32, dtype=complex)
                    initial[2*residue], initial[2*residue+1] = 1/np.sqrt(2), 1j/np.sqrt(2)
                    # This checks relative control phase, not only each output probability.
                    np.testing.assert_allclose(actual @ initial, expected @ initial, rtol=0, atol=ATOL)

    def test_independent_gate_instances(self):
        first, second = modular_multiplier_15(2), modular_multiplier_15(2)
        first.params[0][:] = np.eye(16)
        np.testing.assert_allclose(Operator(second).data, permutation_reference(2), rtol=0, atol=ATOL)


class OrderFindingTests(unittest.TestCase):
    def test_all_bases_and_widths_complete_complex_state(self):
        for base in ORDERS:
            for width in (4, 5, 6):
                with self.subTest(base=base, width=width):
                    size = 2**width
                    actual = Statevector.from_instruction(
                        order_finding_15(base, num_counting_qubits=width)
                    ).data.reshape(16, size)
                    expected = independent_joint(base, width)
                    np.testing.assert_allclose(actual, expected, rtol=0, atol=ATOL)
                    np.testing.assert_allclose(np.vdot(actual, actual), 1, rtol=0, atol=ATOL)
                    marginal = np.sum(abs(actual)**2, axis=0)
                    ideal = np.zeros(size)
                    ideal[::size//ORDERS[base]] = 1/ORDERS[base]
                    np.testing.assert_allclose(marginal, ideal, rtol=0, atol=ATOL)
                    outside = [z for z in range(16) if z not in ORBITS[base]]
                    np.testing.assert_allclose(actual[outside], 0, rtol=0, atol=ATOL)

    def test_register_roles_and_power_constants(self):
        for base, order in ORDERS.items():
            for width in (4, 5, 6):
                circuit = order_finding_15(base, num_counting_qubits=width)
                self.assertEqual([(r.name, len(r)) for r in circuit.qregs],
                                 [("count", width), ("residue", 4)])
                self.assertEqual(circuit.num_qubits, width+4)
                self.assertEqual(circuit.num_clbits, 0)
                self.assertEqual(circuit.num_ancillas, 0)
                self.assertFalse(circuit.parameters)
                self.assertFalse(any(i.operation.name in ("measure", "reset", "initialize") for i in circuit.data))
                controlled = [i for i in circuit.data if i.operation.num_qubits == 5 and
                              getattr(i.operation, "num_ctrl_qubits", None) == 1]
                self.assertEqual(len(controlled), {1: 0, 2: 1, 4: 2}[order])
                for bit, item in enumerate(controlled):
                    self.assertEqual(circuit.find_bit(item.qubits[0]).index, bit)
                    self.assertEqual([circuit.find_bit(q).index for q in item.qubits[1:]],
                                     list(range(width, width+4)))
                    expected = permutation_reference(pow(base, 2**bit, 15))
                    np.testing.assert_allclose(Operator(item.operation.base_gate).data,
                                               expected, rtol=0, atol=ATOL)

    def test_qpe_contract_still_rejects_four_targets(self):
        with self.assertRaisesRegex(ValueError, "1 or 2"):
            qpe_circuit(4, UnitaryGate(np.eye(16)))

    def test_seeded_v2_counts_and_distinct_recovery_factor_success(self):
        shots = 2048
        for base in (1, 2, 11, 14):
            circuit = order_finding_15(base)
            phase = ClassicalRegister(4, "phase")
            circuit.add_register(phase)
            circuit.measure(range(4), phase)
            counts = StatevectorSampler(seed=2026).run([circuit], shots=shots).result()[0].data.phase.get_counts()
            order = ORDERS[base]
            support = {format(y, "04b") for y in range(0, 16, 16//order)}
            self.assertEqual(sum(counts.values()), shots)
            self.assertFalse(set(counts)-support)
            for bits in support:
                probability = 1/order
                self.assertLessEqual(abs(counts.get(bits, 0)/shots-probability),
                                     6*np.sqrt(probability*(1-probability)/shots)+1/shots)
            recovered = {r for bits in counts if (r := recover_order_15(base, bits)) is not None}
            factors = {factors_from_order_15(base, r) for r in recovered}
            self.assertEqual(recovered, set() if base == 1 else {order})
            self.assertEqual(factors, set() if base == 1 else ({None} if base == 14 else {(3, 5)}))


class ClassicalRecoveryTests(unittest.TestCase):
    def test_every_supported_outcome_against_known_orders(self):
        for base, true_order in ORDERS.items():
            for width in (4, 5, 6):
                for numerator in range(2**width):
                    expected = true_order if (numerator and
                        Fraction(numerator, 2**width).denominator == true_order) else None
                    with self.subTest(base=base, width=width, numerator=numerator):
                        self.assertEqual(recover_order_15(base, format(numerator, f"0{width}b")), expected)

    def test_zero_hidden_factors_and_nonminimal_candidates(self):
        for base in ORDERS:
            self.assertIsNone(recover_order_15(base, "0000"))
        self.assertEqual(recover_order_15(2, "0100"), 4)
        self.assertEqual(recover_order_15(2, "1100"), 4)
        self.assertIsNone(recover_order_15(2, "1000"))
        self.assertIsNone(recover_order_15(2, "0010"))
        self.assertIsNone(recover_order_15(11, "0100"))
        self.assertIsNone(recover_order_15(2, "0001"))
        self.assertEqual(recover_order_15(11, "1000"), 2)
        self.assertEqual(recover_order_15(14, "1000"), 2)

    def test_factor_extraction_all_candidates_and_failures(self):
        for base, actual_order in ORDERS.items():
            for candidate in range(1, 15):
                expected = (3, 5) if base not in (1, 14) and candidate == actual_order else None
                with self.subTest(base=base, candidate=candidate):
                    self.assertEqual(factors_from_order_15(base, candidate), expected)
        # 11**(2/2) gives 11: take gcds 5 and 3, not raw values 10 and 12.
        self.assertEqual(factors_from_order_15(11, 2), (3, 5))
        self.assertIsNone(factors_from_order_15(14, 2))
        self.assertIsNone(factors_from_order_15(1, 1))

    def test_classical_precheck_all_bases_without_quantum_builder(self):
        with patch("src.phys3810.shor.order_finding_15", side_effect=AssertionError("No quantum shortcut")):
            for base in range(1, 15):
                expected = (3, 5) if gcd(base, 15) > 1 else None
                self.assertEqual(classical_factor_15(base), expected)


if __name__ == "__main__":
    unittest.main()
