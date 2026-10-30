# PHYS 3810 status

As of October 30, 2026: **the independent QFT/QPE review is accepted and
reconciled; HHL/Shor design contracts are next.** The review found no blocking
defects in snapshot `e365d38c324444e3558bbd2d175c17c9c54ccf97`. It reports a
fresh Linux CPython 3.12.14 install passing 92 tests and six notebooks. Four
optional P3 follow-ups were adopted locally; the current revision passes
**97 tests and six notebooks**. See [the review disposition](QFT_QPE_REVIEW_RECONCILIATION.md).

Work continues on `feat/phys3810-qpe` in the established integration worktree.
The QPE prediction now precedes the answer, its target-preparation wording is
precise, and new QFT editable-cell and QPE mixed-state regressions preserve the
reviewer's successful cases. Computational logic, the strict validator, pins,
and QFT source are unchanged. HHL/Shor implementation has not begun.

All eight files referenced by the review have accessible local copies. The
reviewer reported an unchanged 33-file ZIP; no replacement files were supplied
or needed. Its private sandbox paths are not directly accessible here. Future
handoffs explicitly distinguish review reports from transferred changed files.

The reviewed desktop ZIP remains immutable, with SHA-256
`a8ed3ed9ece505d941adb84f054f8a1e17a79374336216bb9e4ef9470fea2832`.
It contains the reviewed 92-test snapshot, not the subsequent 97-test changes.
The original checkout/index, verified PDF bytes, and Grover rc1 assets remain
preserved; no publication, external message, or hardware job occurred.

Technical review and validation are owned by the implementation assistant;
the user is not being asked to review code manually. The latest coordination
plan is [WORKFLOW.md](WORKFLOW.md). GPT Pro's review of source snapshot
`06e22d9b5d2a` was received, and its required validator correction was reproduced,
fixed, and tested. See [REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md) for
findings, execution evidence, and the basis for closing that checkpoint.
The new lesson's evidence is in [GROVER_VALIDATION.md](GROVER_VALIDATION.md).
The received Grover review and five new exercise regressions are recorded in
[GROVER_REVIEW_RECONCILIATION.md](GROVER_REVIEW_RECONCILIATION.md). The published
versioned preview is separate from QFT development; see [PREVIEW_PLAN.md](PREVIEW_PLAN.md).
The published Grover-only source is `3894391f2026d4fd9351b346b44b5eda453a17da`.
All nine required PR checks passed before merging, and subsequent main workflows
passed. The three release assets were downloaded anonymously and hash-verified.
QFT is excluded from the release; its local evidence is in [QFT_VALIDATION.md](QFT_VALIDATION.md).

## Deliverables

- **Implemented and reviewed:** [course plan](COURSE_PLAN.md), [student landing page](README.md),
  [setup draft](SETUP.md), [environment decision](ENVIRONMENT.md), preflight
  notebook, complete pinned dependency resolution, offline `.env` fix/tests,
  and cross-platform classroom validation command.
- **Grover implemented and tested locally:** canonical source, **20 new tests**,
  and [the teaching notebook](notebooks/01_grover.ipynb), with a 50-minute core
  and 25-minute expansion. Independent review confirmed the algorithm; editable
  exercise parameters and teaching presentation have since been corrected.
- **Passed locally for the corrected Grover preview:** **50 offline tests**, four required fresh-kernel notebooks,
  the original smoke entry point, and visualization checks. The tests retain
  all 25 onboarding/runner regressions, 20 Grover tests, and five exercise tests.
  See the Grover evidence report for archive/path checks and precise limits.
- **QFT implemented and tested locally:** canonical exact transform on 1–6
  qubits, 14 new tests, and a seven-code-cell teaching notebook. The development
  validator passed **64 tests and five required notebooks** at the QFT-only
  checkpoint, including two QFT figures. The combined suite is now 97 tests/six notebooks.
- **Independent review evidence:** GPT Pro reported another Linux install on
  CPython 3.12.14 with the same 114 application-package pins, all original 19
  tests and three notebooks passing, and reproduced M1-01. The correction was
  subsequently verified here on CPython 3.12.15. The later Grover review also
  reproduced all 45 then-current tests/four notebooks and closed M1-01. The
  latest audit now independently reports **50 tests/four notebooks passed**
  on Linux CPython 3.12.14 in a reused pinned environment, closing G1. It also
  observed the successful PR and merged-commit Linux classroom executions.
- **Untested on native hosts:** Windows x64 and macOS. Compatible package wheels
  were checked; this is not installation or notebook-execution evidence.
- **Skipped by classroom validation:** optional Runtime/cloud and GPU paths.
  No IBM service calls or hardware jobs are part of milestone 1 validation.
  A separate optional environment passed the Runtime fake-backend smoke locally;
  this does not validate hardware access.
- **QPE implemented and tested locally:** numeric 1-2-qubit target unitaries,
  1-6 counting qubits, 24 source tests, five editable-cell regressions, and an
  eight-code-cell notebook. The reviewed baseline contained 92 tests and six
  notebooks; the P3 follow-up coverage now raises that to 97 tests. The SDK
  output reversal is explicitly reconciled.
- **Independent QFT/QPE review accepted:** fresh Linux x86_64/glibc 2.39,
  CPython 3.12.14, 114 installed packages covered by active constraints matching
  pins, 92 tests, six notebooks, 35 code cells, and ten figures. These are
  reviewer-reported executions, distinct from local reused-environment evidence.
- **Review follow-ups validated locally:** four QFT editable-cell regressions
  and one nonexact two-target/global-phase QPE regression raise the suite to 97.
  Prediction ordering and docstring wording changed without computational changes.
- **Not implemented / untested:** HHL and Shor lessons.
  The original smoke notebooks do not count as those algorithm implementations.
- **Drafts now, final later:** the original v0.1 guides remain published with
  rc1. ChatGPT supplied new v0.2 student/instructor drafts, now copied unchanged
  into the repository and locally inspected. The corrected delivered-file
  [receipt](handouts/README.md) matches both copies; the earlier hashes referred
  to their pre-delivery prefixes. Both existing PDFs are ready for instructor
  review and are tracked in the documentation commit with unchanged bytes. The
  v0.2 editions are not yet public release assets. Final classroom PDFs
  still require platform validation and instructor feedback.

## Open teaching decisions

Actual session dates, student preparation, session length, complete-materials
deadline, format/platforms, and assessment expectations remain unknown. Confirm
whether all five algorithms need in-class treatment or some support the wider
course, and the intended depth/examples for HHL/Shor. Providing five tested
implementations remains the requested deliverable. Proposed sequence:
Grover; QFT/QPE; HHL/Shor.
Each session has a 50-minute core and a 75-minute expansion in the course plan.
UTC has no classes November 25–29, and November 30 is the last class day;
these facts do not establish the invited-session dates.

## Recommended next actions

1. **Prepare HHL/Shor design contracts only.** Specify HHL evolution sign,
   time/scaling, spectral interval, phase/eigenvalue decoding, reciprocal
   rotation, and uncomputation. Specify Shor's arithmetic or explicitly compiled
   model and target-register scope; do not silently widen the current QPE bound.
2. **Implement only after those contracts are explicit.** Preserve independent
   mathematical expectations and the accepted QFT/QPE conventions. No HHL/Shor
   implementation is part of this reconciliation.
3. **In parallel, instructor feedback:** the unchanged Grover review packet is
   ready. Dates, platforms, classroom emphasis, and assessment remain open;
   sending has not been confirmed in this thread.
4. **Later validation and publication:** native-platform and interactive checks,
   pacing rehearsal, and matching PDFs still precede final classroom claims.
   Further external actions require authorization covering them.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims; they
do not require pausing unrelated local work. Dates and assessment expectations
are still unknown. No implementation of QFT, QPE, HHL, or Shor was included in the
Grover preview. Remote CI passed for Grover. A deliberately failed remote job's
artifact-upload behavior and remote QFT checks remain untested.

**GPT Pro sync: not needed for these evidenced P3 follow-ups.** The independent
phase-convention checkpoint is closed. Sync sooner for a material QPE/environment
scope change or unresolved mathematical disagreement; retain the later combined
HHL/Shor review before publication. User input needed for this reconciliation:
none. No manual code or diff audit is assigned to the user.
