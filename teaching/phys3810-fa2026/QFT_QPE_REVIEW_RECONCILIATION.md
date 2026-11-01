# QFT/QPE independent review reconciliation

October 30, 2026. **The independent review accepts the QFT/QPE milestone with
no blocking defects.** Four optional P3 follow-ups have been adopted locally.
The algorithmic conventions are resolved; HHL/Shor implementation has not begun.

## Reviewed snapshot and available files

The received report identifies source commit
`e365d38c324444e3558bbd2d175c17c9c54ccf97` and review ZIP SHA-256
`a8ed3ed9ece505d941adb84f054f8a1e17a79374336216bb9e4ef9470fea2832`.
The reviewer verified all 32 manifest entries and reports that all 33 exported
files, including the manifest, remained unchanged after review. Codex rechecked
both retained ZIP copies, all manifest entries, and the 29 canonical files
against that local Git commit. The original review ZIP remains immutable.

The return consists of a review report and references to files in the
reviewer's private sandbox; it does not supply replacements. All eight named
source/test/notebook/validator files are present locally and in the reviewed
archive. The private sandbox paths are not mounted in this workspace. The
screenshot's file cards do not themselves transfer file contents or prove
cross-chat access. No returned ZIP is needed for this unchanged-snapshot review.
Codex has not claimed access to the reviewer's private executed copies or
additional probe scripts. The access and identity checks are retained locally
under ignored `artifacts/review-reconciliation-2026-10-30/`.

## Independent execution evidence received

The following results are **reviewer-reported execution**, separate from the
existing Codex CPython 3.12.15 reused-environment runs:

- A newly created isolated environment on Linux x86_64/glibc 2.39,
  CPython **3.12.14**, installed the unchanged supplied requirements/constraints.
  All **114 installed packages covered by active constraints** matched their pins.
  The report does not provide an installer-version claim, and none is inferred.
- Core versions: Qiskit **2.6.1**, Aer **0.17.2**, NumPy **2.5.4**, nbclient
  **0.11.0**, nbformat **5.10.4**, ipykernel **7.4.0**, Matplotlib **3.11.2**,
  and JupyterLab **4.6.4**.
- The unchanged validator exited 0: dependency consistency, **92 tests**, and
  **six fresh-kernel notebooks** passed. All **35 nonempty code cells** executed
  without retained errors; ten PNG figures were produced. Sources stayed
  output-free. The reported 11.667 seconds is the unit-test duration only.
- Additional probes passed: four actual QFT parameter edits; six nonexact
  complex two-target superposition cases at widths 2/4/6, with and without
  0.173 turns of unitary global phase; one extra full-operator SDK comparison;
  and three asymmetric SDK-label examples. These probes are not part of the
  reported 92-test count, and their scripts were not returned.

The review's substantive command sequence was an isolated Python 3.12 venv,
`python -m pip install --retries 1 -r requirements.txt`, followed by
`python scripts/validate_classroom.py` with `OMP_NUM_THREADS=2`,
`OPENBLAS_NUM_THREADS=2`, and `PYTHONDONTWRITEBYTECODE=1`.

It confirmed the positive Fourier sign, inverse/swap conventions, target/count
ordering, controlled powers, eigenstate-preparation responsibility, global-phase
retention, mixtures, finite-precision distributions, and pinned SDK reversal.
Native Windows/macOS, interactive UI, hardware/GPU/Runtime, remote CI for local
commits, and live classroom pacing remain unvalidated. The reviewer did not
rerun Codex's Ruff, pre-commit, Bash smoke, or broader link checks.

## Optional findings and local disposition

1. **Prediction ordering — confirmed and corrected.** In the reviewed notebook,
   `qpe-exact-example` printed the label before `qpe-exact-prediction` asked for
   a prediction. The prediction Markdown now precedes both exact-example and
   sampling cells and asks for predictions before parameter reruns. The planned
   20-30, 30-45, and 45-50 minute sequence is retained. All eight code cells,
   their order, IDs, metadata, and empty output state are unchanged. No test
   was added solely for this Markdown relocation.
2. **QFT editable-cell regressions — accepted as preventive coverage.** Four
   new tests execute the actual notebook cells for `(3, "001")`, `(3, "110")`,
   `(2, "01")`, and `(4, "0011")`. Independent trigonometric/NumPy-DFT
   expectations check amplitudes, normalization, inverse counts, plotted data,
   titles, bitstring ticks, and reversal reporting. The original behavior
   already passed; no QFT source or notebook repair was required.
3. **Nonexact two-target/global-phase regression — accepted as preventive
   coverage.** One test uses a seeded complex four-dimensional eigenbasis,
   complex coefficients, nonexact eigenphases, an actual circuit global phase
   of 0.173 turns, and counting widths 2/4/6. It compares coherent full states
   with Fourier-sum amplitudes and marginals with independently weighted
   sine-ratio probabilities, without output renormalization or phase fitting.
   This reproduces the reported behavior class, not an unavailable exact
   reviewer script. No algorithm repair was required.
4. **Preparation wording — clarified.** The QPE docstring now says no
   **target-state preparation**, acknowledging the counting Hadamards. The
   implementation AST is unchanged apart from the docstring; no extra test
   was added for this wording edit.

## Local validation after reconciliation

Linux x86_64/glibc 2.43, reused CPython **3.12.15** classroom environment,
Qiskit **2.6.1**, Aer **0.17.2**, NumPy **2.5.4**, nbclient **0.11.0**.
No dependency pin or environment migration was introduced.

- Targeted QFT actual-cell suite: **four passed**.
- Targeted QPE suite: **24 passed**, including the new three-width regression.
- `python -m pip check`: **passed**.
- `python -m unittest discover -s tests -v`: **97 passed**.
- `python scripts/validate_classroom.py`: **passed**, including 97 tests and
  all six fresh-kernel notebooks, 35 nonempty code cells, and ten PNGs.
  Source outputs/counts remain empty.
- Ruff **0.15.22** over source/scripts/tests/course and core notebooks: **passed**.
- `bash scripts/smoke_local.sh`: **passed**.
- `pre-commit run --all-files`: **passed**, including Ruff, YAML, and Markdown.
  All 151 relative documentation links and diff-whitespace checks passed.
  Preservation checks confirmed the original checkout/index, PDFs, Grover rc1
  assets, and reviewed ZIP unchanged; the local receipt records final commit
  identity and clean-worktree checks.

The five additional test methods explain the increase from the independently
reviewed 92 to the current 97. The new local revision is not falsely described
as the exact ZIP GPT Pro executed. These scoped follow-ups do not change the
accepted QFT/QPE algorithmic contract or require another review round.

## Next design gates and sync

HHL must declare evolution sign, time/scaling, spectral interval and aliasing,
negative-eigenvalue support or exclusion, phase-to-eigenvalue decoding,
reciprocal rotation, and QPE inversion/uncomputation before implementation.
Shor must choose a reversible-arithmetic or explicitly compiled/reduced model.
An ordinary residue register for N=15 needs four target qubits; the existing
QPE helper supports only one or two. Do not merely widen that bound and call
dense matrix powers a scalable modular-exponentiation implementation.

These are **future design decisions**, not defects in the accepted milestone.
No HHL/Shor source or notebook was implemented here. The original checkout,
verified PDF bytes, Grover rc1 assets, and reviewed ZIP remain preserved.

**GPT Pro sync: not needed for these evidenced P3 follow-ups.** The next action
is HHL/Shor design contracts only. Sync sooner if design requires a material
QPE/environment change or reveals unresolved mathematical disagreement; the
later combined HHL/Shor review remains recommended before publication.
