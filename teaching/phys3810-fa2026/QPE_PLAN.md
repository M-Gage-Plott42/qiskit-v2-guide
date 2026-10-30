# QPE milestone: phase and register contract

October 30, 2026. This contract precedes QPE implementation. It completes the
planned QFT/QPE session using the existing exact QFT. It does not implement HHL
or Shor. The combined phase-convention review is due after this milestone.
Implementation and local checks are now complete; see [QPE_VALIDATION.md](QPE_VALIDATION.md).

## Supported interface

`qpe_circuit(num_counting_qubits, unitary)` returns an unmeasured estimation
block. Counting width is an integer (`numbers.Integral`, excluding booleans)
from **1 through 6**. `unitary` is a numeric Qiskit `Gate` or `QuantumCircuit`
on **1 or 2 target qubits**. Raw matrices and generic `Instruction` objects
are not accepted; wrap an explicit small matrix in `UnitaryGate` if needed.

Circuit inputs must contain only gates and no classical bits. Unbound
parameters, measurements, reset/initialize, circuit-level barriers, control flow, nonfinite
matrices, and nonunitary operations are rejected. The complete small matrix
must satisfy `U.conj().T @ U = I` with `rtol=0, atol=1e-12`; no projection,
renormalization, or global-phase removal is performed. Unsupported types raise
`TypeError`; invalid ranges or operations raise `ValueError`. Inputs are not
mutated. The result has no classical bits or extra ancillary qubits.

## State preparation and bit order

The first register, `count`, occupies qubits `0..m-1`. The second, `target`,
occupies `m..m+k-1`. Counting qubit `j` controls `U**(2**j)`. Counting qubit 0
is the least-significant bit; its displayed result is the rightmost bit.

The caller supplies counting input `|0...0>` and prepares the target state
**before** composing the returned block. The function neither prepares nor
checks an eigenstate. For `U|u> = exp(+2*pi*i*phi)|u>`, phases are interpreted
modulo one. A superposition of eigenstates generally produces entanglement and
a weighted mixture of phase distributions when only `count` is measured.

The block applies H to counting qubits, controlled integer powers of U, then
`qft_circuit(m, inverse=True, do_swaps=True)` on `count`. The existing positive
Fourier convention is retained. Measure only `count[j]` into classical bit j
of a named `phase` register. A bitstring b means `int(b, 2)/2**m`; do not reverse
it. Full-state basis order is `|target>|count>` in increasing integer indexing.

## Independent mathematical expectations

For `N=2**m`, counting amplitude y on an eigenstate input is

`a_y = sum(exp(2*pi*i*x*(phi-y/N)) for x in range(N)) / N`.

Its probability is `|a_y|**2`. Independently use the squared sine-ratio formula
for nonexact phases, with the removable singularity handled at exact grid
points. If `phi = y/N`, all counting probability is at y. Use asymmetric
fixtures `1/8 -> 001`, `3/8 -> 011`, and `6/8 -> 110`, plus negative/wrapped
phases and nonexact `1/3`. Increasing m refines the grid; it does not guarantee
every sampled estimate is closer to the phase.

Verify full complex output states `kron(u, a)`, target preservation on eigenstate
input, normalization, two-qubit complex eigenstates, global phase on U, and a
non-eigenstate mixture. Verify complete estimation operators against an
independent spectral construction, not just histograms. Floating-point checks
use `rtol=0, atol=2e-11`; input unitarity uses the stricter tolerance above.

The [pinned Qiskit 2.6.1 implementation](https://github.com/Qiskit/qiskit/blob/2.6.1/qiskit/circuit/library/phase_estimation.py)
of `phase_estimation()` appends a final counting
bit reversal after its inverse `QFTGate`. Local inspection and asymmetric
examples reproduced that convention. Compare the complete reference after
explicitly undoing this output reversal; also test the unadjusted relationship
`reference = (I_target tensor R_count) @ canonical`. Do not copy the SDK's
construction into the independent mathematical expectations.

## Acceptance and teaching

- Test all counting widths and both target widths, numeric circuit/gate inputs,
  unsupported inputs, input immutability, and declared register roles.
- Test asymmetric exact phases, independent nonexact distributions, complex
  states, the full estimation operator, global-phase retention, and mixtures.
- Add V2 sampling with seed 2026, shot accounting, exact-state decoding, and
  explicit statistical tolerances for nonexact outcomes.
- Import canonical QPE/QFT source into `03_qpe.ipynb`; keep source outputs empty.
  Required fresh-kernel validation must execute every nonempty cell and render
  the circuit, exact sampling, and nonexact/precision figures.
- Exercise actual editable notebook cells with alternative phase/precision
  settings so labels and expectations cannot silently stay at their defaults.
- Preserve all 64 prior tests and five required notebooks. Add QPE as the sixth
  required notebook without weakening any runner/error/skip safeguards.

QFT occupies the first 20 minutes of session 2. QPE supplies the remaining
30-minute core: 10 minutes on kickback/controlled powers, 15 on asymmetric exact
phase prediction and local sampling, and 5 on register interpretation. The
75-minute expansion adds 15 minutes on nonexact distributions and 10 on
precision. All expansion code still executes during validation. These are
proposed timings; a live classroom rehearsal remains outstanding.

## Resource limits and references

This implementation classically validates and raises dense matrices of size
2 or 4, then wraps controlled powered matrices as gates. That is an explicit
small-example choice, not a scalable black-box implementation. There are m
controlled-power blocks; naive repeated access to U would require `2**m-1`
uses, before synthesis costs. State preparation, controlled-U availability,
gate synthesis, and readout are not free. Phase estimation is modulo one and
does not resolve an unknown Hamiltonian's energy scale/sign by itself.

Primary references checked against the pinned local SDK:
[phase_estimation API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.phase_estimation),
[phase-estimation procedure](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/phase-estimation-and-factoring/phase-estimation-procedure),
and [bit ordering](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering).
