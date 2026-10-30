"""Grover search circuits for the PHYS 3810 small-instance teaching lab.

Supported circuits use 2--5 qubits, explicit marked basis states, uniform input
preparation, and a caller-selected number of iterations. Displayed bitstrings
have qubit 0 on the right, so ``int(bitstring, 2)`` is the basis-state index.
Every returned circuit is unmeasured, with no classical bits or ancillas.

These enumerated oracles are instructional, not a scalable search interface:
each marked string adds one multi-controlled phase flip plus X conjugations.
Circuit construction and decomposed gate costs are distinct from oracle-query
counts. No quantum advantage is asserted for these local simulation examples.
"""

from __future__ import annotations

from collections.abc import Iterable
from math import pi
from numbers import Integral

from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate


def _validate_num_qubits(num_qubits: int) -> int:
    if isinstance(num_qubits, bool) or not isinstance(num_qubits, Integral):
        raise TypeError("num_qubits must be an integer, not a boolean.")
    if not 2 <= num_qubits <= 5:
        raise ValueError("num_qubits must be between 2 and 5 for this teaching implementation.")
    return int(num_qubits)


def _validate_marked_states(num_qubits: int, marked_states: Iterable[str]) -> tuple[str, ...]:
    if isinstance(marked_states, (str, bytes)):
        raise TypeError("marked_states must be an iterable of bitstrings, not one string or bytes.")
    try:
        iterator = iter(marked_states)
    except TypeError as error:
        raise TypeError("marked_states must be an iterable of bitstrings.") from error

    targets: set[str] = set()
    for target in iterator:
        if not isinstance(target, str):
            raise TypeError("Every marked state must be a binary string.")
        if len(target) != num_qubits or any(bit not in "01" for bit in target):
            raise ValueError(f"Every marked state must contain exactly {num_qubits} binary digits.")
        if target in targets:
            raise ValueError("Duplicate marked states are not allowed.")
        targets.add(target)
        if len(targets) == 2**num_qubits:
            raise ValueError("At least one basis state must remain unmarked.")
    if not targets:
        raise ValueError("At least one marked state is required.")
    # Stable circuit ordering for sets; caller collections are never modified.
    return tuple(sorted(targets))


def _validate_iterations(iterations: int) -> int:
    if isinstance(iterations, bool) or not isinstance(iterations, Integral):
        raise TypeError("iterations must be a nonnegative integer, not a boolean.")
    if iterations < 0:
        raise ValueError("iterations must be nonnegative.")
    return int(iterations)


def _flip_all_ones(circuit: QuantumCircuit) -> None:
    """Apply a minus sign only to |11...1>, using H--MCX--H on the last qubit."""
    last = circuit.num_qubits - 1
    circuit.h(last)
    circuit.append(MCXGate(last), range(circuit.num_qubits))
    circuit.h(last)


def phase_oracle(num_qubits: int, marked_states: Iterable[str]) -> QuantumCircuit:
    """Return O with O|x> = -|x> for marked x and +|x> otherwise.

    ``num_qubits`` is an integer from 2 through 5. ``marked_states`` is a
    finite iterable of distinct, fixed-width binary strings; raw strings,
    duplicates, empty/all-marked sets, and malformed targets are rejected.
    The iterable is consumed once and sorted; its order has no semantic effect.
    Integer parameters accept ``numbers.Integral`` values, excluding booleans.

    Raises ``TypeError`` for invalid input types and ``ValueError`` for values
    outside that contract. The returned circuit has no measurements/ancillas.
    """
    num_qubits = _validate_num_qubits(num_qubits)
    targets = _validate_marked_states(num_qubits, marked_states)
    oracle = QuantumCircuit(num_qubits, name="Oracle")
    for target in targets:
        # Strings are displayed q_(n-1)...q_0, while gate indices start at q_0.
        zero_qubits = [qubit for qubit, bit in enumerate(reversed(target)) if bit == "0"]
        # Map this target to all ones, flip its phase, and undo the mapping.
        if zero_qubits:
            oracle.x(zero_qubits)
        _flip_all_ones(oracle)
        if zero_qubits:
            oracle.x(zero_qubits)
    return oracle


def diffusion_operator(num_qubits: int) -> QuantumCircuit:
    """Return exactly D = 2|s><s| - I, for uniform |s> on 2--5 qubits.

    The qubit-count validation and exception types match ``phase_oracle``.
    No measurements, classical bits, or additional qubits are introduced.
    """
    num_qubits = _validate_num_qubits(num_qubits)
    diffusion = QuantumCircuit(num_qubits, name="Diffusion")
    diffusion.h(range(num_qubits))
    diffusion.x(range(num_qubits))
    _flip_all_ones(diffusion)
    diffusion.x(range(num_qubits))
    diffusion.h(range(num_qubits))
    # The gates above give I - 2|s><s|. Multiplication by -1 gives our exact D.
    # This phase is physically irrelevant alone, but explicit for matrix tests.
    diffusion.global_phase = pi
    return diffusion


def grover_iteration(num_qubits: int, marked_states: Iterable[str]) -> QuantumCircuit:
    """Return one Grover iteration Q = D O, without initial state preparation.

    Apply the phase oracle first, then diffusion. Inputs and exceptions follow
    ``phase_oracle``. Other implementations may choose the global phase -Q;
    the marked/unmarked relative oracle phase is not an arbitrary convention.
    """
    iteration = phase_oracle(num_qubits, marked_states)
    iteration.name = "Grover iteration"
    iteration.compose(diffusion_operator(iteration.num_qubits), inplace=True)
    return iteration


def grover_circuit(
    num_qubits: int, marked_states: Iterable[str], iterations: int
) -> QuantumCircuit:
    """Prepare uniform |s>, then apply ``iterations`` copies of Q = D O.

    ``iterations`` must be a nonnegative integer (``numbers.Integral``), not a
    boolean. The other inputs follow ``phase_oracle``. All inputs are validated
    even for zero iterations, which returns only the uniform preparation.
    ``TypeError`` reports wrong types; ``ValueError`` reports out-of-scope values.

    The circuit is intentionally unmeasured. Use ``measure_all(inplace=False)``
    to create a sampling copy while retaining this circuit for exact checks.
    """
    num_qubits = _validate_num_qubits(num_qubits)
    targets = _validate_marked_states(num_qubits, marked_states)
    iterations = _validate_iterations(iterations)
    circuit = QuantumCircuit(num_qubits, name="Grover search")
    circuit.h(range(num_qubits))
    if iterations:
        iteration = grover_iteration(num_qubits, targets)
        for _ in range(iterations):
            circuit.compose(iteration, inplace=True)
    return circuit
