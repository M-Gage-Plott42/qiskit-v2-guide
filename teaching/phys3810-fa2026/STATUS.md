# PHYS 3810 status

As of October 30, 2026: **QPE is implemented and locally validated; the combined
QFT/QPE independent review is due.** Work is on local branch
`feat/phys3810-qpe`, following integration commit
`f277e213ea44d0f119add543cabbeceda6e706d8`. The new milestone passes **92 tests
and six required notebooks**. See [QPE_VALIDATION.md](QPE_VALIDATION.md) for
commands, independent expectations, register conventions, and limits.

The source/notebooks/tests form a standalone technical review snapshot, with
version-matched Markdown setup. The exact commit, ZIP hash, extracted-run
results, and desktop-copy verification are recorded in the local handoff
receipt under `artifacts/qpe-2026-10-30/`. No GPT Pro response for this snapshot
has yet been received. HHL/Shor remain unimplemented.

The original dirty checkout/index remain intact. Continue in the established
integration worktree. Grover rc1 remains the published 50-test/four-notebook
preview; its source, ZIP, and release PDFs have not changed. The verified v0.2
PDFs also remain unchanged and are excluded from the QFT/QPE review ZIP because
they describe Grover-only setup. No new PDF was generated or substituted.

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
- **QPE implemented and tested locally:** numeric 1-2-qubit target unitaries,
  1-6 counting qubits, 23 source tests, five editable-cell regressions, and an
  eight-code-cell notebook. All 64 prior tests remain; the validator now runs
  92 tests and six notebooks. The SDK output reversal is explicitly reconciled.
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

1. **Send the standalone QFT/QPE ZIP and chat-provided review prompt to GPT Pro.**
   Review the exact transferred source, mathematics, editable exercises, and
   sign/register conventions. The assistant owns technical review and repairs.
2. **Return the actual review to Codex for reconciliation.** Reproduce actionable
   findings, update evidence, and resolve the shared phase conventions before
   starting HHL/Shor. Do not infer that another chat sees this local worktree.
3. **In parallel, instructor feedback:** the user can send the unchanged Grover
   review packet. Dates, platforms, classroom emphasis, and assessment remain
   open; sending has not been confirmed in this thread.
4. **Later teaching/publication work:** native-platform and interactive checks,
   pacing rehearsal, and version-matched PDFs still precede final classroom
   claims. Local implementation does not authorize publication or messages.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims; they
do not require pausing unrelated local work. Dates and assessment expectations
are still unknown. No implementation of QFT, QPE, HHL, or Shor was included in the
Grover preview. Remote CI passed for Grover. A deliberately failed remote job's
artifact-upload behavior and remote QFT checks remain untested.

**GPT Pro sync: due now.** The combined QFT/QPE phase-convention checkpoint is
ready for independent review; no such response has yet been received. User
input needed next: transfer the prepared ZIP/prompt and return the review.
No manual source or diff audit is assigned to the user.
