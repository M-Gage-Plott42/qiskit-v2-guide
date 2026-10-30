# Combined QFT/QPE validation

October 30, 2026. **QFT/QPE is independently accepted and its optional follow-ups
are reconciled.** The original 92-test record below identifies the reviewed
snapshot; current evidence is in [the reconciliation](QFT_QPE_REVIEW_RECONCILIATION.md). This milestone follows local
integration commit `f277e213ea44d0f119add543cabbeceda6e706d8`. No Grover release
asset, dependency pin, or existing QFT implementation was changed.

## Original reviewed scope (92 tests)

- `src/phys3810/qpe.py`: `qpe_circuit(m, unitary)` on 1-6 counting qubits and
  a numeric 1-2-qubit gate/circuit, with caller-supplied target preparation.
  The exact contract is [QPE_PLAN.md](QPE_PLAN.md).
- `tests/test_qpe.py`: **23 tests** for input validation, complete independent
  spectral operators, asymmetric exact phases, sine-ratio nonexact probabilities,
  complex/entangled target states, normalization, global phase, mixtures,
  supported widths, SDK convention comparison, and V2 sampling.
- `tests/test_qpe_notebook.py`: **five tests** execute the actual notebook cells
  with alternative exact phases/widths, nonexact phase 0.31 with widths 2/4,
  parameter-dependent labels, invalid exercise choices, and a changed SDK check.
- `notebooks/03_qpe.ipynb`: **16 cells, eight executable**, importing canonical
  QPE source. Three figures show the controlled-power circuit, exact counting
  samples, and nonexact distributions at two precisions.
- The strict validator adds QPE as the sixth required notebook, requires three
  QPE PNGs, and now reports only HHL/Shor as unimplemented. Its fresh-kernel,
  forced-error, skip-rejection, execution-count, and partial-output rules remain.

QFT retains its positive Fourier sign and inverse/swap contract in
[QFT_PLAN.md](QFT_PLAN.md). QPE measures count[j] into classical bit j and decodes
`int(bitstring, 2)/2**m`, without reversing the result. Independent exact fixtures
include `1/8 -> 001`, `3/8 -> 011`, and `6/8 -> 110`; width checks use asymmetric
labels where possible. Nonexact fixtures include `1/3`, `0.31`, `-1/7`, and
`0.97`. Full-state checks use `kron(target, counting_amplitudes)`, not only
marginal probabilities. Matrix/state tolerances are `rtol=0, atol=2e-11`;
unitarity admission uses `atol=1e-12` with zero relative tolerance.

## SDK convention evidence

Installed Qiskit 2.6.1 and its [pinned source](https://github.com/Qiskit/qiskit/blob/2.6.1/qiskit/circuit/library/phase_estimation.py)
append a counting-bit reversal after `QFTGate(...).inverse()` inside
`phase_estimation()`. Raw SDK outcomes for the three fixtures above were
`100`, `110`, and `011`. Tests verify the full-operator relationship
`SDK = (I_target tensor R_count) @ canonical`, then undo R explicitly for
comparison. The notebook exposes that difference; no hidden bitstring reversal
is built into canonical decoding. The SDK is an additional reference, not the
source of the independent mathematical expectations.

## Original local checks before independent review

Platform: Linux x86_64, glibc 2.43. The reused classroom environment contains
CPython **3.12.15**, Qiskit **2.6.1**, Aer **0.17.2**, nbclient **0.11.0**, and
NumPy **2.5.4**. No new classroom dependency installation or version change was
performed. Separate Python 3.12 maintainer tools supply Ruff **0.15.22**,
yamllint **1.38.0**, and pre-commit **4.7.0**. BLAS/OpenMP threads were limited
to two during the complete checks, with writable temporary/cache directories.

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

- Dependency consistency: **passed**.
- Unit tests: **92 passed** (64 existing, 23 QPE, five QPE exercise regressions).
- Classroom validation: **passed**, including all 92 tests and **six required
  notebooks** in fresh interpreter-bound kernels. All **35 nonempty code cells**
  executed without retained errors. Preflight/Grover/QFT/QPE produced 2/3/2/3
  PNGs; the three new QPE figures were visually inspected.
- Source notebooks: output lists remain empty and execution counts unset.
- Ruff and the original Bash smoke workflow: **passed**.
- `pre-commit run --all-files`: **passed**, including Ruff, YAML, and Markdown.
  All 146 relative documentation links and diff-whitespace checks passed.
  Exported-bundle verification and its exact identity are recorded separately
  after final packaging in the local handoff receipt and final chat response.

Detailed logs and artifact checks are retained in ignored
`artifacts/qpe-2026-10-30/` in the integration worktree. Standalone verification
must run outside both checkouts, without Git metadata; it reuses the pinned
interpreter unless explicitly stated otherwise. Source/test/notebook/dependency
bytes must match the identified snapshot, and executed outputs stay outside the ZIP.

## Teaching and limits

The notebook completes session 2's proposed 50-minute core: 20 minutes of QFT,
then 30 minutes of QPE. The 25-minute expansion covers nonexact probabilities
and precision; all its code executes during validation. Rehearsal, native
platform checks, and instructor feedback remain outstanding.

Dense validation and classical matrix powers are deliberate small-case choices.
The routine does not prepare/check an eigenstate or implement scalable oracle
access. There are m controlled-power blocks, corresponding to `2**m-1` repeated
U uses before synthesis costs. Phase is modulo one; increased precision does
not guarantee that every sample is closer. No quantum-advantage claim is made.

**Skipped:** optional IBM Runtime/cloud and GPU paths. **Untested:** native
Windows/macOS, interactive notebook/editor setup, remote CI for these local
commits, and timed classroom delivery. **Unimplemented:** HHL and Shor.
The published Grover-only rc1 remains a distinct 50-test/four-notebook snapshot.
The original checkout/index, verified PDFs, and rc1 assets remain preserved.

## Independent review and subsequent reconciliation

The received review accepted source `e365d38c324444e3558bbd2d175c17c9c54ccf97`,
ZIP `a8ed3ed9ece505d941adb84f054f8a1e17a79374336216bb9e4ef9470fea2832`,
with no blocking defects. It reports a **fresh** Linux x86_64/glibc 2.39,
CPython 3.12.14 installation of the supplied pins, 114 active-constraint package
matches, 92 tests/six notebooks, and additional successful numerical probes.
This evidence is separate from Codex's reused CPython 3.12.15 environment.

Local follow-ups move prediction text ahead of answer output, clarify target
preparation wording, add four actual-cell QFT regression cases, and add one
nonexact two-target/global-phase QPE test with three precision subtests.
The current suite passes **97 tests and six notebooks**; all 35 code cells and
ten figures remain required. The QPE computational AST and notebook code cells
are unchanged; no QFT algorithm or validator logic changed. The original
92-test archive remains preserved, not relabeled as the new revision.

See [QFT_QPE_REVIEW_RECONCILIATION.md](QFT_QPE_REVIEW_RECONCILIATION.md) for each
finding, access/transfer clarification, commands, and limits. **GPT Pro sync:
not needed for these evidenced P3 follow-ups.** HHL/Shor design is next;
implementation remains outside this reconciliation.
