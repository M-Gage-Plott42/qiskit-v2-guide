# HHL milestone: exact-spectrum teaching contract

October 30, 2026. **Implemented and locally validated under this contract.**
See [HHL_VALIDATION.md](HHL_VALIDATION.md) for execution evidence and remaining
review limits. This contract follows the accepted QFT/QPE conventions and
does not modify [QPE_PLAN.md](QPE_PLAN.md). Canonical HHL source is
`src/phys3810/hhl.py`, with mathematical tests in `tests/` and the teaching
notebook `notebooks/04_hhl.ipynb`.

## Scope, interface, and inputs

The first HHL example is a **one-system-qubit, exact-spectrum linear-system
state-preparation demonstration**. It is not a general linear-system solver.
Public interfaces:

- `hhl_circuit(matrix, rhs)` returns an unmeasured five-qubit circuit.
- `hhl_reciprocal_rotation()` returns the fixed four-qubit count/flag rotation
  circuit described below, enabling independent operator checks and teaching.

`matrix` is a finite numeric 2x2 Hermitian matrix A whose eigenvalues belong to
`{1, 2, 3, 4, 5, 6, 7}` in the stated teaching units. Arbitrary real or complex
eigenbases and repeated eigenvalues are supported. Thus A is positive definite
and its condition number is at most 7. `rhs` is a finite length-two complex
vector b with squared norm one. Real inputs are included; inputs are copied,
never mutated. Numeric lists/tuples/NumPy arrays are accepted; strings, booleans,
symbolic parameters, and nonnumeric objects are not numerical inputs.

Use `TypeError` for unsupported input types and `ValueError` for invalid shapes,
nonfinite data, failed Hermiticity/normalization, or unsupported spectra.
Validation uses absolute tolerance `1e-12`, relative tolerance zero, solely
for floating representation of the exact family. Reject materially off-grid,
zero, negative, or out-of-range eigenvalues; reject nonnormalized/zero b.
Do not silently symmetrize, shift, rescale, round a different spectrum onto
the grid, or normalize an invalid b. There is no configurable precision,
rotation constant, or evolution time in this first interface.

## Evolution, scaling, and phase decoding

Fix three counting qubits, `t = pi/4`, and

`U = exp(+i*A*t) = exp(+2*pi*i*A/8)`.

For an eigenvalue lambda, `phi = lambda/8`, so the canonical three-bit QPE label
has integer value `y = lambda`. Decode **lambda = y**, not y/8, when evaluating
the reciprocal. The phase itself is y/8. Labels 1 through 7 are positive; the
high bit is not a sign bit. The known interval `1 <= lambda <= 7` excludes zero
and the alias at lambda=8. Negative eigenvalues and wrapped signed decoding are
unsupported. An arbitrary user scaling is not inferred.

Numerically construct the small dense U from the validated A, preserving its
complete global phase. This disclosed classical work is acceptable for the
teaching scope; constructing or preparing `solve(A,b)` as the algorithm is not.
Wrap that dense matrix in `UnitaryGate` before passing it to QPE; the existing
helper rejects a raw matrix. Use dimensionless teaching units with no hidden
spectral scaling.
The sign is deliberate: IBM's [PauliEvolutionGate](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.PauliEvolutionGate)
uses `exp(-i*t*A)`. A future implementation choosing that reference would need
negative time for this contract and must account for synthesis approximation.
The default design uses the dense exponential, not an approximate product formula.

## Registers and circuit sequence

- `count`: qubits 0, 1, 2, initially `000`; bit 0 is least significant.
- `system`: qubit 3, prepared in b using a unitary state-preparation gate.
- `success`: qubit 4, initially 0, retained as the postselection flag.
- Full-state tensor order: **success tensor system tensor count**.

The composite circuit is intended for **all-zero input on all five qubits**;
it prepares b itself. The declared sequence is target preparation,
`qpe_circuit(3, U_gate)`, reciprocal
rotation, then the **inverse of that same QPE block** on count/system only.
Do not invert b's preparation or the reciprocal rotation. Do not measure
between these operations. QPE of the adjoint unitary is not a substitute for
the inverse of the entire QPE block. The returned circuit contains no classical bits,
measurements, or extra work qubits.

Reuse the existing QPE helper unchanged: its one-target input and counting
width three are already supported. Use its canonical bit order directly, with
no SDK-reference reversal inserted. The success flag is not part of QPE.

## Reciprocal rotation and exact cleanup

Fix `C = 1`. On count label y, rotate the flag by

- `theta_0 = 0` (identity; never divide by zero);
- `theta_y = 2*asin(1/y)` for y=1 through 7.

In the standalone rotation circuit, count occupies local qubits 0-2 and the
flag occupies local qubit 3. In HHL, connect those to `[0,1,2,4]`, leaving the
system untouched. Control each rotation on the **complete counting pattern**.
The factor of two follows [RYGate's matrix](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.RYGate):
the flag-1 amplitude from flag 0 is `sin(theta/2)`. No clipping is needed because
`0 <= C/y <= 1`. This seven-entry lookup is a compiled small-spectrum choice,
not scalable coherent reciprocal arithmetic.

Exact representability is essential. After inverse QPE, count must be `000`
on **both flag branches**. The success flag itself must not be reset: it is the
output to postselect. For nonexact phases, a y-dependent rotation generally
changes the phase-register superposition, so inverse QPE does not exactly erase
it. Such spectra are outside this contract; do not claim generic exact cleanup.
The [HHL paper's perfect-phase-estimation argument](https://arxiv.org/html/0811.3171v3)
and its separate finite-precision analysis motivate this distinction.

## Postselection and independent expectations

Let `x_raw = solve(A,b)` and `F = sqrt(I - A^(-2))`, taking the positive
Hermitian matrix square root. The ideal complete output is

`|0>success tensor (F b) tensor |000>count`
`+ |1>success tensor x_raw tensor |000>count`.

Therefore `P(success=1) = ||x_raw||**2`, between `1/49` and 1. Conditioned on
success, the system state is `x_raw/||x_raw||`. This is a normalized quantum
encoding, not a returned classical solution vector; the system marginal before
postselection is not generally the solution state. Preserve relative signs and
complex phases. Zero-norm failure branches must not be normalized.

These formulas refer to the exact integer-spectrum family. Failure-branch
expectations should use the known integer eigenvalues of the fixtures/generators,
so a floating eigensolver returning a value just below 1 cannot introduce a
spurious negative square-root radicand. A test reference may set a scalar
radicand in `[-1e-12,0]` to zero only after confirming exact-family membership;
a larger negative value fails. This is reference-roundoff handling, not
eigenvalue/angle clipping or admission of a genuinely off-grid problem. F is
an independent expected-state formula, not a circuit-construction shortcut.

For sampling, measure the flag and system into explicitly named classical
registers, retain shot alignment, and condition system data on the same shot's
flag=1. Never combine independent marginal histograms to invent conditional
counts. Handle an empty selected sample explicitly. Use 4096 shots per sampled
measurement basis and seed local V2 sampling at 2026; no Runtime service or
hardware path is part of this milestone.

## Fixed fixtures and acceptance gates

Default matrix `A0 = [[3/2, 1/2], [1/2, 3/2]]` has eigenvalues 1 and 2.

- With `b=(1,0)`, `x_raw=(3/4,-1/4)`, success probability `5/8`, and normalized
  system `(3,-1)/sqrt(10)`. The failure system vector is
  `(sqrt(3)/4,sqrt(3)/4)`, with probability `3/8`.
- With `b=(0,1)`, the normalized answer is `(-1,3)/sqrt(10)`, again `5/8` success.
- For b equal to `|+>`, success is `1/4`; for `|->`, success is 1. The output
  system retains the selected eigenstate. These nontrivial preparations detect
  an accidental inversion of the preparation gate during uncomputation.
- With `b=(1,i)/sqrt(2)`, the normalized answer is
  `(3-i,-1+3i)/sqrt(20)` and success remains `5/8`.
- Explicitly passing `2*A0` gives the same normalized answer for b=(1,0), but
  success `5/32`. With fixed C, success depends on absolute scaling as well as
  conditioning; this is not automatic matrix rescaling by the API.
- `A=[[2,1],[1,2]]`, b=(1,0), gives `(2,-1)/sqrt(5)` and success `5/9`.
- `A=3I` and `A=7I` retain any normalized b with success `1/9` and `1/49`.
  These scalar matrices detect dropped global phase and test the upper boundary.

Independent tests must:

1. Check all eight counting labels and both input flag states against the full
   reciprocal-rotation matrix, including exact identity at label 0.
2. Test all 28 unordered eigenvalue pairs including repeated values, using
   seeded complex eigenbases and normalized complex right-hand sides. Verify
   success vectors with a classical linear solve, not a copy of the circuit.
3. Verify the full joint state, norm, success probability **before** conditioning,
   count-register cleanup on both branches, and normalized successful system.
   Use known spectral generators or closed fixtures for the independent failure
   branch; do not derive expectations by invoking the HHL implementation.
4. Detect relative sign/phase errors. For the default b, conditional X and Z
   expectations are `-3/5` and `4/5`; for the complex b, X/Y/Z are `-3/5,4/5,0`.
   Computational-basis probabilities alone are insufficient.
5. Cover invalid data, wrong dimensions, singular/negative/off-grid spectra,
   lambda=8 aliasing, unnormalized b, input immutability, and resource/register
   invariants. Do not add an approximate fallback for rejected matrices.
6. Check finite-shot success and conditional observables using explicit
   six-standard-error bounds plus one-shot allowance; use the actual selected
   shot count for conditional bounds. Statevector expectations remain primary.

Numerical tolerances: `rtol=0`; full-state/operator/probability/norm
`atol=1e-10`; conditioned-state `atol=1e-9`, allowing amplification by at most
seven during normalization. Require the norm of the nonzero-count projection
to be at most `1e-9` (leakage probability at most `1e-18`). Normalize the success
branch only after independently checking its raw amplitudes and probability.
No additional rescaling or global-phase fitting may force agreement or hide
an algorithm error.

## Resources, lesson scope, and completion

The ideal interface uses **five qubits**: three count, one system, one flag.
It contains two QPE directions, six controlled-power blocks total, two Fourier
transforms, seven three-control rotations, and one b-preparation. Naive repeated
U accounting is `2*(1+2+4)=14`, before synthesis; this dense implementation does
not literally perform fourteen black-box calls. Dense exponentiation, classical
validation, known spectral bounds, state loading, postselection, synthesis,
and readout are explicit costs. No sparse-oracle scaling or speedup is claimed.

Session 3 reserves 20 core minutes for tracing A0/b=(1,0): prediction, the
QPE/rotation/uncompute stages, success versus failure, and the relative sign.
The 15-minute expansion changes b/scaling and checks the complex solution and
count cleanup. Deriving every decomposition or coding HHL from scratch is not
inside that slot. The shared session retains its five-minute QPE refresher,
20-minute Shor core, and five-minute limitations discussion.

The implementation must import canonical source into `04_hhl.ipynb`, place
predictions before answers, exercise editable parameters, and register fresh
execution with at least two meaningful figures (circuit and conditioned-state/
success comparison). Preserve the existing 97-test/six-notebook baseline and
all strict runner safeguards. Commit notebooks without outputs.

Classical design checks confirmed the nine fixtures above and seven rotation
amplitudes on Python 3.12.15/NumPy 2.5.4. These are scalar/linear-algebra checks,
not HHL execution. That earlier design evidence is ignored under
`artifacts/hhl-shor-design-2026-10-30/`. Subsequent circuit, notebook, and full
regression executions are recorded in [HHL_VALIDATION.md](HHL_VALIDATION.md).
The independent phase review is already closed; no additional GPT Pro round
is required solely for this bounded design. Expand the contract or revisit
review if nonexact/negative spectra or a different algorithmic scope is needed.
