# PHYS 3810 status

As of October 30, 2026: **local Git integration is complete; QPE is next.**
The integration branch `integration/phys3810-docs-qft-2026-10-30` starts at
published main `3894391f2026d4fd9351b346b44b5eda453a17da`. Its first commit,
`b16d235ca01ebc9c7f610dcfeb64f081d5d6b453`, integrates the verified v0.2 PDFs and
Grover documentation. The subsequent QFT commit contains the existing source,
tests, notebook, validator registration, and this status/evidence update.
See [INTEGRATION_VALIDATION.md](INTEGRATION_VALIDATION.md) for checks and scope.

The original `feat/phys3810-m1-onboarding` checkout and index remain intact,
with a successfully rehearsed recovery checkpoint. The durable integration
worktree is under `artifacts/local-integration-2026-10-30/worktree` relative to
the original repository. Continue implementation there. Its local commits
have not been pushed or reviewed by remote CI. The published Grover rc1 tag,
ZIP, and release assets remain unchanged; QFT is not in that public preview.

The PDF receipt issue is resolved. The [instructor packet](INSTRUCTOR_REVIEW_PLAN.md)
is ready; sending has not been confirmed. The response policy ends each turn
with a copyable next instruction. No QPE implementation began during integration.

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
  validator passes **64 tests and five required notebooks**, including two QFT figures.
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
- **Not implemented / untested:** QPE, HHL, and Shor lessons.
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

1. **Implement QPE in the integration worktree.** State its supported unitary,
   eigenstate preparation, counting/target register roles, controlled powers,
   precision, and bit-order contract before implementation. Use the tested QFT
   conventions and independent asymmetric exact/nonexact phase distributions;
   retain all existing Grover/QFT/runner regressions.
2. **Then prepare the combined QFT/QPE review:** provide the standalone desktop
   bundle and a separate GPT Pro prompt before HHL/Shor implementation.
3. **In parallel, instructor feedback:** the user can send the two verified
   v0.2 guides and unchanged Grover rc1 ZIP link using the instructor plan.
   Dates, platforms, classroom emphasis, and assessment remain open.
4. **Publication and final teaching release:** local commits and verified PDF
   tracking are ready for a separately scoped publication decision. Native
   platform checks, interactive setup validation, and pacing rehearsal still
   precede final classroom claims. No external action was taken during integration.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims; they
do not require pausing unrelated local work. Dates and assessment expectations
are still unknown. No implementation of QFT, QPE, HHL, or Shor was included in the
Grover preview. Remote CI passed for Grover. A deliberately failed remote job's
artifact-upload behavior and remote QFT checks remain untested.

**GPT Pro sync: not needed for this unchanged-source integration.** The next
substantive review remains after QFT/QPE. The integrated checkout passed the
64-test/five-notebook baseline plus the documented local checks; see the
integration evidence for exact commands, versions, and limits.
