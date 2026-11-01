"""Bounded, unmeasured phase estimation with explicit counting-bit order.

The caller prepares count=0 and a target eigenstate before this block. For
U|u> = exp(2*pi*i*phi)|u>, counting label y estimates phi by y / 2**m,
modulo one. Target superpositions need not have a single phase outcome.

This teaching implementation validates dense 2x2 or 4x4 matrices and computes
their integer powers classically. Those conveniences, target preparation, and
controlled-gate synthesis are not a scalable or cost-free black-box oracle.
"""

from __future__ import annotations

from numbers import Integral

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Gate
from qiskit.circuit.library import UnitaryGate
from qiskit.exceptions import QiskitError
from qiskit.quantum_info import Operator

from .qft import qft_circuit


def qpe_circuit(num_counting_qubits: int, unitary: QuantumCircuit | Gate) -> QuantumCircuit:
    """Build QPE on 1--6 counting qubits and a 1--2-qubit numeric unitary.

    Counting width accepts Integral values except booleans. The unitary must
    be a Gate or a circuit containing only gates, with no classical bits or
    unbound parameters. Its finite matrix must satisfy U†U=I at absolute
    tolerance 1e-12 (zero relative tolerance). Invalid types raise TypeError;
    unsupported ranges/operations raise ValueError. Inputs are not mutated.

    Registers are count[0:m] followed by target[0:k]. count[j] controls U**2**j;
    count[0] is the least-significant output bit. The final inverse QFT includes
    swaps, so measuring count[j] into classical bit j needs no bit reversal.
    The returned circuit has no target-state preparation, measurements,
    classical bits, or extra ancillas. With an eigenstate input, full-state
    ordering is |target>|count>, and the target is unchanged apart from its
    shared phase.
    """
    if isinstance(num_counting_qubits, bool) or not isinstance(num_counting_qubits, Integral):
        raise TypeError("num_counting_qubits must be an integer, not a boolean.")
    if not 1 <= num_counting_qubits <= 6:
        raise ValueError("num_counting_qubits must be between 1 and 6.")
    if not isinstance(unitary, (QuantumCircuit, Gate)):
        raise TypeError("unitary must be a QuantumCircuit or Gate, not a raw matrix.")
    if unitary.num_qubits not in (1, 2):
        raise ValueError("The teaching unitary must act on 1 or 2 target qubits.")
    if isinstance(unitary, QuantumCircuit):
        if unitary.num_clbits or any(not isinstance(item.operation, Gate) for item in unitary.data):
            raise ValueError("The unitary circuit must contain only gates and no classical bits.")
        parameterized = bool(unitary.parameters)
    else:
        parameterized = unitary.is_parameterized()
    if parameterized:
        raise ValueError("Bind all unitary parameters before building QPE.")
    try:
        # Copy the complete matrix, including global phase. A global phase of U
        # becomes a relative phase under control and changes the QPE outcome.
        matrix = np.array(Operator(unitary).data, dtype=complex, copy=True)
    except (QiskitError, TypeError, ValueError) as error:
        raise ValueError("The operation must have a numeric unitary matrix.") from error
    if not np.all(np.isfinite(matrix)) or not np.allclose(
        matrix.conj().T @ matrix, np.eye(matrix.shape[0]), rtol=0, atol=1e-12
    ):
        raise ValueError("The operation matrix must be finite and unitary.")

    m = int(num_counting_qubits)
    count = QuantumRegister(m, "count")
    target = QuantumRegister(unitary.num_qubits, "target")
    circuit = QuantumCircuit(count, target, name="QPE")
    circuit.h(count)
    for bit in range(m):
        exponent = 2**bit
        # Dense integer powers are deliberately limited to the small target
        # matrices above. m such blocks represent 2**m-1 repeated U queries.
        powered = UnitaryGate(np.linalg.matrix_power(matrix, exponent), label=f"U^{exponent}")
        circuit.append(powered.control(annotated=False), [count[bit], *target])
    circuit.append(qft_circuit(m, inverse=True, do_swaps=True).to_gate(label="IQFT"), count)
    return circuit
