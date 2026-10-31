"""Five-qubit HHL for normalized two-entry states and exact spectra in 1..7.

This is a compiled teaching example, not a general linear-system solver.
Three-bit QPE, a seven-entry reciprocal lookup, and exact inverse QPE prepare
the normalized solution state only after postselection. Dense classical
validation/evolution, state loading, and postselection are explicit costs.
"""

from __future__ import annotations

from numbers import Number

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import RYGate, StatePreparation, UnitaryGate

from .qpe import qpe_circuit

_INPUT_ATOL = 1e-12


def _numeric_array(value: object, name: str, shape: tuple[int, ...]) -> np.ndarray:
    """Copy numerical containers without coercing strings or booleans to numbers."""
    if not isinstance(value, (list, tuple, np.ndarray)):
        raise TypeError(f"{name} must be a numeric list, tuple, or NumPy array.")
    try:
        # Object conversion retains booleans in mixed Python sequences, unlike
        # converting directly to complex (which would silently accept them).
        elements = np.asarray(value, dtype=object)
    except ValueError as error:
        raise ValueError(f"{name} must have shape {shape}.") from error
    if elements.shape != shape:
        raise ValueError(f"{name} must have shape {shape}.")
    # A ragged vector can become a length-two object array whose entries are
    # themselves sequences. Its apparent outer shape is not a numeric vector.
    if any(isinstance(element, (list, tuple, np.ndarray)) for element in elements.flat):
        raise ValueError(f"{name} must have shape {shape} with scalar entries.")
    if any(
        isinstance(element, (bool, np.bool_)) or not isinstance(element, Number)
        for element in elements.flat
    ):
        raise TypeError(f"{name} must contain numbers, not booleans or symbolic values.")
    try:
        result = np.array(elements, dtype=complex, copy=True)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"{name} must contain finite representable numbers.") from error
    if not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must contain finite numbers.")
    return result


def hhl_reciprocal_rotation() -> QuantumCircuit:
    """Return the fixed count-controlled reciprocal rotation on four qubits.

    Local count qubits 0..2 encode y in little-endian order; local qubit 3 is
    the success flag. Label 0 acts as identity. For each y=1..7, the flag sees
    RY(2*asin(1/y)), so its flag-1 amplitude from flag 0 is 1/y. All three count
    bits control each rotation, including open controls where the label has 0.
    No measurement, classical bits, or additional work qubits are introduced.
    """
    count = QuantumRegister(3, "count")
    success = QuantumRegister(1, "success")
    circuit = QuantumCircuit(count, success, name="Reciprocal")
    for label in range(1, 8):
        angle = 2 * np.arcsin(1 / label)
        rotation = RYGate(angle).control(3, ctrl_state=label, annotated=False)
        circuit.append(rotation, [*count, success[0]])
    return circuit


def hhl_circuit(matrix: object, rhs: object) -> QuantumCircuit:
    """Prepare the bounded HHL state from all-zero input on five qubits.

    matrix is a finite numeric 2x2 Hermitian matrix A with eigenvalues in
    {1,2,3,4,5,6,7}; rhs is a finite numeric length-two vector b of squared norm
    one. Real/complex lists, tuples, and NumPy arrays are accepted and copied.
    Invalid types (including booleans/strings/symbolic data) raise TypeError;
    invalid shapes, nonfinite values, or unsupported mathematical inputs raise
    ValueError. Admission uses atol=1e-12, rtol=0 solely for floating-point
    representation of the exact family. There is no rescaling, spectral
    rounding, approximate-spectrum fallback, or normalization of invalid b.

    Registers are count[0:3], system[3], success[4], with tensor order
    |success>|system>|count>. With t=pi/4 and U=exp(+i*A*t), exact QPE label y
    equals the positive eigenvalue, not the phase y/8. C=1 reciprocal rotation
    is followed by the inverse of the same QPE block, leaving count=000 on
    both flag branches. State preparation is not inverted; the success flag
    is retained. The returned circuit is unmeasured, with no classical bits
    or extra work qubits.

    The raw success vector is A^-1 b, with probability ||A^-1 b||^2. Only
    after selecting flag=1 is the system state its normalized version. The
    failure vector is sqrt(I-A^-2)b, so the unconditional system marginal is
    generally not the solution. Exact cleanup does not extend to off-grid
    eigenvalues; negative/singular/wrapped spectra are deliberately excluded.
    """
    operator = _numeric_array(matrix, "matrix", (2, 2))
    state = _numeric_array(rhs, "rhs", (2,))
    if not np.allclose(operator, operator.conj().T, rtol=0, atol=_INPUT_ATOL):
        raise ValueError("matrix must be Hermitian.")
    if not np.isclose(np.vdot(state, state).real, 1, rtol=0, atol=_INPUT_ATOL):
        raise ValueError("rhs must have squared norm one.")
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    allowed = np.arange(1, 8)
    if not np.all(np.min(np.abs(eigenvalues[:, None] - allowed), axis=1) <= _INPUT_ATOL):
        raise ValueError("matrix eigenvalues must belong to the exact spectrum {1,...,7}.")

    # Use the actual validated eigenvalues, not rounded labels. Keep the full
    # global phase: for scalar A it is the phase that QPE must estimate.
    phases = np.exp(1j * (np.pi / 4) * eigenvalues)
    evolution = (eigenvectors * phases) @ eigenvectors.conj().T
    estimation = qpe_circuit(3, UnitaryGate(evolution, label="exp(+i A pi/4)"))

    count = QuantumRegister(3, "count")
    system = QuantumRegister(1, "system")
    success = QuantumRegister(1, "success")
    circuit = QuantumCircuit(count, system, success, name="HHL")
    circuit.append(StatePreparation(state), system)
    estimation_gate = estimation.to_gate(label="QPE")
    circuit.append(estimation_gate, [*count, system[0]])
    circuit.append(hhl_reciprocal_rotation().to_gate(), [*count, success[0]])
    # Invert only estimation. Neither b preparation nor the flag rotation is
    # part of this inverse; QPE(U†) would not undo the complete QPE block.
    circuit.append(estimation_gate.inverse(), [*count, system[0]])
    return circuit
