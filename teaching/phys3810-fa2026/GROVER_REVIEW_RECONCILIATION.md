# Grover review reconciliation

October 29, 2026. The independent Grover review was received for the 23-file
standalone archive with SHA-256
`9cd567e2afd7c603b0d589bf7f7cd96f7880113da6ac3d98ec170e949eb297d1`.
The reviewer reported that all files were readable and independently ran all
45 tests and four notebooks on Linux, CPython 3.12.14 with the unchanged pins.
It confirmed the algorithm and M1-01 fix, but found an editable-exercise defect.
These are reviewer-reported runs, separate from the local correction evidence.

## G1: selected targets and plot legends

**Confirmed and fixed.** Before correction, the original target pair passed,
while `001`/`101` and `010`/`111` failed because expected matrix/probability
indices were fixed at 1 and 3. The circuit itself remained correct. A varying-M
plot also retained an `M=1` legend.

The notebook now derives expected indices and messages from the selected pair,
requires exactly two targets for this exercise, and labels both formula and
circuit series with the actual marked count. Expectations remain independent
of the tested circuit.

`tests/test_grover_notebook.py` executes the actual notebook cells by stable ID,
substituting only editable parameters. Its **five tests passed**: original pair,
two alternative pairs, exactly-two guard, and an M=2 plot with independent data
and legend checks. Full Grover-only validation subsequently passed **50 tests
and all four required notebooks** on the local CPython 3.12.15 environment.

## Teaching corrections

- **O1:** preflight no longer hard-codes an obsolete notebook count. It names
  available lessons and directs students to the current required validator.
- **O2:** before-class Run All verifies installation; in class, students clear
  outputs, discuss the prediction, and then execute the relevant cell.
- **O3:** the input-contract exercise is included within the 15-minute marked-set
  expansion. The stated core/expanded schedules remain 50 and 75 minutes.
- **O4:** the circuit figure labels Prepare, Oracle O, and Diffusion D using the
  canonical functions. An exact matrix assertion verifies that the grouped
  teaching circuit equals the implemented search circuit; the figure was inspected.

A live timed rehearsal and native Windows/macOS remain untested. These fixes
do not establish an unperformed rehearsal or platform execution.

## Preview preparation and next module

The original PDFs linked by the reviewer were not included as accessible files
in this workspace. New local setup and instructor drafts are being prepared
from editable sources; they must not be described as copies of those PDFs.
Review drafts may be shared before final platform validation, clearly marked
as drafts. Final classroom materials still require the stated release checks.

An isolated Grover-only checkout starts from current remote main
`bf6f362ded70767d3891db996a0a3e0cd152b34d`. It preserves upstream action pins
and the newer security/dependency updates while retaining the tested universal
classroom resolution. A course prerelease is proposed in [PREVIEW_PLAN.md](PREVIEW_PLAN.md).
Publication is separate from local preparation under the current authorization.

The review permits proceeding after these demonstrated fixes without a further
GPT Pro approval round. QFT can now proceed under [QFT_PLAN.md](QFT_PLAN.md).
The next substantial checkpoint remains after QFT/QPE and before HHL/Shor.
The QFT implementation is not part of the Grover-only preview source snapshot.

Detailed local logs are in ignored `artifacts/grover-review/`, including
`g1-before.log`, `exercise-regressions.log`, and `preview-validation.log`.
No private review correspondence is copied into public artifacts.
