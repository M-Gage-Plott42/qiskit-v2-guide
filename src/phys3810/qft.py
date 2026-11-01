"""Exact small-register quantum Fourier transform circuits for PHYS 3810.

For N = 2**n, the forward convention is F[j, k] = exp(2*pi*i*j*k/N)/sqrt(N).
Basis index k is interpreted with qubit 0 as the least-significant bit (the
rightmost displayed bit). This module uses explicit H, controlled-phase, and
SWAP gates. Tests compare these circuits with the SDK's QFTGate as a separate
reference.

The instructional scope is 1--6 qubits with all rotation angles retained.
No measurements, classical bits, or ancillas are added. Constructing this
small circuit and classically simulating it do not demonstrate quantum
advantage or solve the state-preparation/readout problem for arbitrary data.
"""

from __future__ import annotations

from math import pi
from numbers import Integral

from qiskit import QuantumCircuit


def qft_circuit(
    num_qubits: int, *, inverse: bool = False, do_swaps: bool = True
) -> QuantumCircuit:
    """Return the exact QFT or the inverse of the selected forward circuit.

    ``num_qubits`` accepts ``numbers.Integral`` values from 1 through 6,
    excluding booleans. ``inverse`` and ``do_swaps`` must be Python booleans;
    truthy integers or strings are not accepted. Invalid types raise
    ``TypeError``; an out-of-range qubit count raises ``ValueError``.

    With swaps, the forward operator is F with positive Fourier exponent,
    and its inverse is F.conj().T. Let R reverse the bits of each basis index.
    Without swaps, the forward operator is R @ F and the inverse is
    F.conj().T @ R. In particular, inverse-without-swaps is not R @ F.conj().T:
    it reverses the entire selected forward circuit, including gate order.

    The forward circuit contains n Hadamards, n*(n-1)/2 controlled phases,
    and floor(n/2) swaps when requested. The returned circuit is unmeasured
    and uses no additional qubits. No approximate-QFT option is provided.
    """
    if isinstance(num_qubits, bool) or not isinstance(num_qubits, Integral):
        raise TypeError("num_qubits must be an integer, not a boolean.")
    if not 1 <= num_qubits <= 6:
        raise ValueError("num_qubits must be between 1 and 6 for this teaching implementation.")
    if not isinstance(inverse, bool):
        raise TypeError("inverse must be a Python boolean.")
    if not isinstance(do_swaps, bool):
        raise TypeError("do_swaps must be a Python boolean.")
    num_qubits = int(num_qubits)

    circuit = QuantumCircuit(num_qubits)
    # Work from the most-significant wire toward qubit 0. After each H, add
    # the phase contributions of the lower-significance input bits. A wire
    # separation d contributes a controlled phase of pi / 2**d.
    for target in reversed(range(num_qubits)):
        circuit.h(target)
        for control in reversed(range(target)):
            angle = pi / (2 ** (target - control))
            circuit.cp(angle, control, target)

    # The H/CP network leaves Fourier-output bits reversed. These final swaps
    # restore the standard integer ordering; omitting them implements R @ F.
    if do_swaps:
        for low in range(num_qubits // 2):
            circuit.swap(low, num_qubits - low - 1)

    # Taking the complete adjoint moves the swaps to the beginning and reverses
    # all gates/phase signs. It also gives the correct F† @ R when swaps were
    # omitted, rather than incorrectly reversing the inverse's output bits.
    if inverse:
        circuit = circuit.inverse()
    circuit.name = ("IQFT" if inverse else "QFT") + (" without swaps" if not do_swaps else "")
    return circuit
