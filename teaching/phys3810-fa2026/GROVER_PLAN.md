# Grover milestone: implementation contract

Implemented October 29, 2026 after the milestone-1 review correction. This is
the supported contract and acceptance criteria; actual checks and limitations
are recorded in [GROVER_VALIDATION.md](GROVER_VALIDATION.md). Independent review
confirmed the bounded algorithm; its editable-exercise correction is now
validated. A versioned standalone preview is being prepared separately from QFT.

## Initial supported scope

- Local, ideal small circuits on **2 through 5 qubits**. The core lab uses
  2 and 3 qubits; the larger cases exercise the reusable implementation.
- Marked targets are a finite, nonempty iterable of distinct binary strings, each
  exactly `num_qubits` characters long. Reject duplicate targets, invalid
  characters, wrong lengths, and the all-marked set with clear errors.
  Reject a bare string or bytes object. Consume an iterable once and sort its
  targets for deterministic circuit construction without mutating the caller.
- Displayed strings use Qiskit's ordering: the rightmost bit is qubit 0;
  `int(bitstring, 2)` is the corresponding computational-basis index.
- Iterations are explicit nonnegative integers. Reject booleans and fractional
  values. Zero iterations returns the uniformly prepared state.
  Both integer parameters accept `numbers.Integral`, including NumPy integers,
  while excluding booleans. Invalid types raise `TypeError`; out-of-scope
  values raise `ValueError`, including invalid targets when iterations are zero.
- Returned circuits contain no measurements. The lab adds measurements to a
  copy for V2 sampling, retaining the original for exact statevector checks.
- State the limits: enumerated marked states, ideal local simulation, and
  small circuit sizes. No claim of general search performance or quantum
  advantage; explain oracle construction cost separately from query count.

## Files and responsibilities

- `src/phys3810/grover.py`: validated phase-oracle construction and the search
  circuit, with commented diffusion and bit-order conventions.
  Public functions: `phase_oracle`, `diffusion_operator`, `grover_iteration`,
  and `grover_circuit`. The iteration is exact `D O` without preparation;
  `grover_circuit` prepares the uniform state before repeating it.
- `tests/test_grover.py`: input validation, independent operator/probability
  expectations, and separate SDK reference comparisons.
- `notebooks/01_grover.ipynb` in this course folder: narrative, predictions,
  a single-target example, multiple targets, and overshooting exercises.
- `scripts/validate_classroom.py`: register the new required notebook and
  update the remaining-unimplemented-lessons message.

## Mathematical acceptance criteria

For every basis state in the selected small fixtures, assert exact phase
oracle action: marked states acquire a minus sign, other states are unchanged,
and there are no off-diagonal transitions. Include asymmetric targets `001`
and `011`, plus a multiple-target case. Cover each supported qubit count.

For uniform preparation, calculate the total marked-state probability
independently as `sin((2*r + 1)*theta)**2`, where
`theta = asin(sqrt(M/N))`, `N = 2**n`, and `M` counts distinct targets.
Assert these exact fixtures with explicit numerical tolerances:

- Zero iterations: `M/N`.
- `N=4, M=1, r=1`: probability `1`.
- `N=8, M=1, r=2`: probability `121/128`.
- `N=8, M=2, r=1`: probability `1`.
- Overshooting, `N=4, M=1, r=2`: probability `1/4`.

Also compare the iteration operator with
[`grover_operator()`](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator).
Account for an irrelevant overall global phase in that comparison; the
oracle's marked/unmarked relative phase remains an exact contract. The analytic
tests must not calculate their expectations using the SDK reference circuit.

## Completion and review

Retain the onboarding tests. Run the new tests, all required notebooks in fresh
kernels, and relevant lint. Required cells may not use skip/error tags to evade
validation; intentional error demonstrations must handle their exceptions.
Keep source notebooks output-free and record actual results in status/evidence.

The completed lesson's independent review has been reconciled. A second GPT Pro
round is not required for the demonstrated small corrections. The next substantial
checkpoint is after QFT/QPE. Dates, student preparation, and assessment details remain open
and can refine exercises without blocking this small local implementation.
