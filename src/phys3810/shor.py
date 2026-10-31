"""Compiled full-domain N=15 order finding and conservative classical recovery.

This fixed example stores dense 16x16 modular-permutation matrices. It is not
scalable reversible arithmetic or general integer factoring. Its four residue
qubits require a separate builder; the one/two-target QPE API stays unchanged.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from numbers import Integral

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import UnitaryGate

from .qft import qft_circuit


def _integer(value: int, name: str, low: int, high: int) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be an integer, not a boolean.")
    if not low <= value <= high:
        raise ValueError(f"{name} must be between {low} and {high}.")
    return int(value)


def _unit(value: int, name: str = "base") -> int:
    value = _integer(value, name, 1, 14)
    if gcd(value, 15) != 1:
        raise ValueError(f"{name} must be coprime to 15.")
    return value


def modular_multiplier_15(multiplier: int) -> UnitaryGate:
    """Map x<15 to multiplier*x mod 15, and fix 15, on four residue qubits.

    The supported multipliers are {1,2,4,7,8,11,13,14}. Each matrix entry at
    destination row/source column is exactly +1: both 0 and 15 stay fixed,
    with no extra global or basis-dependent phase. Invalid types raise
    TypeError; out-of-range/noncoprime integers raise ValueError. Integers are
    accepted through numbers.Integral except booleans; no modulo coercion.
    """
    multiplier = _unit(multiplier, "multiplier")
    matrix = np.zeros((16, 16), dtype=complex)
    for source in range(15):
        matrix[(multiplier * source) % 15, source] = 1
    matrix[15, 15] = 1
    return UnitaryGate(matrix, label=f"M{multiplier}")


def order_finding_15(base: int, *, num_counting_qubits: int = 4) -> QuantumCircuit:
    """Prepare order-finding output from all-zero input on m+4 qubits.

    base is a unit modulo 15; counting width m is an Integral in 4..6 excluding
    booleans. Count occupies qubits 0..m-1, residue the next four, so full-state
    order is |residue>|count>. This circuit prepares residue |1> itself.
    Count[j] controls multiplication by pow(base, 2**j, 15); constants equal
    to 1 are omitted. No order search or order-dependent initialization is used.

    The canonical inverse QFT includes swaps. Measure count[j] into bit j of
    a named phase register, decode int(bits, 2)/2**m, without bit reversal.
    The returned circuit has no measurements, classical bits, or work ancillas.
    Dense gate synthesis and this small exact-grid family do not establish
    general Shor resource scaling. The existing QPE helper is not broadened.
    """
    base = _unit(base)
    width = _integer(num_counting_qubits, "num_counting_qubits", 4, 6)
    count = QuantumRegister(width, "count")
    residue = QuantumRegister(4, "residue")
    circuit = QuantumCircuit(count, residue, name=f"Order15({base})")
    circuit.x(residue[0])
    circuit.h(count)
    for bit in range(width):
        multiplier = pow(base, 2**bit, 15)
        if multiplier != 1:
            gate = modular_multiplier_15(multiplier).control(annotated=False)
            circuit.append(gate, [count[bit], *residue])
    circuit.append(qft_circuit(width, inverse=True, do_swaps=True).to_gate(), count)
    return circuit


def _is_order_15(base: int, candidate: int) -> bool:
    """Verify a candidate period and its minimality, without searching orders."""
    if pow(base, candidate, 15) != 1:
        return False
    # A proper divisor order would divide candidate/p for some prime p|candidate.
    # Factor the candidate alone; do not test multiples or manufacture an order.
    remainder = candidate
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            if pow(base, candidate // divisor, 15) == 1:
                return False
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    return remainder <= 1 or pow(base, candidate // remainder, 15) != 1


def recover_order_15(base: int, outcome: str) -> int | None:
    """Verify an exact reduced phase denominator, or return None if inconclusive.

    outcome must be a binary string of length 4..6 with no spaces/separators.
    Non-string types raise TypeError; malformed strings raise ValueError. Base
    validation is the same as order_finding_15. Zero data, denominators >=15,
    failed period tests, and nonminimal periods return None. This intentionally
    does not approximate fractions, try multiples, or combine samples by LCM.
    """
    base = _unit(base)
    if not isinstance(outcome, str):
        raise TypeError("outcome must be a binary string.")
    if not 4 <= len(outcome) <= 6 or any(bit not in "01" for bit in outcome):
        raise ValueError("outcome must contain 4 to 6 binary digits without separators.")
    numerator = int(outcome, 2)
    if numerator == 0:
        return None
    denominator = Fraction(numerator, 2**len(outcome)).denominator
    if denominator >= 15 or not _is_order_15(base, denominator):
        return None
    return denominator


def factors_from_order_15(base: int, order: int) -> tuple[int, int] | None:
    """Return sorted nontrivial GCD factors only for a verified even true order.

    Base must be a unit modulo 15; order must be an Integral in 1..14, excluding
    booleans. Wrong but well-formed periods, odd orders, trivial square roots,
    and failed factor products return None rather than a fabricated success.
    """
    base = _unit(base)
    order = _integer(order, "order", 1, 14)
    if not _is_order_15(base, order) or order % 2:
        return None
    midpoint = pow(base, order // 2, 15)
    if midpoint in (1, 14):
        return None
    factors = tuple(sorted((gcd(midpoint - 1, 15), gcd(midpoint + 1, 15))))
    if all(1 < factor < 15 for factor in factors) and factors[0] * factors[1] == 15:
        return factors
    return None


def classical_factor_15(base: int) -> tuple[int, int] | None:
    """Run the classical GCD precheck for bases 1..14; never build a circuit.

    Noncoprime bases can factor 15 immediately. This is a separate classical
    success, not evidence of quantum order finding. Units return None.
    """
    base = _integer(base, "base", 1, 14)
    factor = gcd(base, 15)
    return tuple(sorted((factor, 15 // factor))) if factor > 1 else None
