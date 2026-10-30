# PHYS 3810 status

Current integration snapshot, October 30: this local documentation/PDF change
is based on published main `3894391`. The original development checkout and
index have a verified recovery checkpoint and remain intact. QFT code and its
64-test/five-notebook evidence are outside this revision and will follow in a
separate commit. Its runtime remains the published Grover 50-test/four-notebook
scope. Older planning and validation entries below retain their dated context.

As of October 30, 2026: **the Grover prerelease is published and its additional
independent audit is reconciled; QFT remains locally validated.** QPE is the next
implementation, after the planned Git integration. **Git preservation and local
integration are the next Codex work item.** The PDF receipt is resolved and the
first instructor review packet is ready. The latest policy update requires a
copyable next-step instruction at the end of every response; only docs/plans
changed, and integration has not started. See the [instructor review plan](INSTRUCTOR_REVIEW_PLAN.md),
[release audit reconciliation](GROVER_RELEASE_RECONCILIATION.md) and
[Git integration plan](GIT_INTEGRATION_PLAN.md).
The [Grover preview](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1)
was published through [PR #112](https://github.com/M-Gage-Plott42/qiskit-v2-guide/pull/112).
QFT development remains local on `feat/phys3810-m1-onboarding`. See [VALIDATION.md](VALIDATION.md) for the base, inventory, commands,
installed versions, outcomes, and reviewer handoff.

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
QFT is excluded from the release; its local evidence is in the preserved development checkout.

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
  review and remain unchanged, uncommitted, and unpublished. Final classroom PDFs
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

1. **Next Codex work item — reconcile Git locally:** preserve staged, unstaged, and untracked
   work, then use a durable clean worktree based on current main. Separate the
   documentation/PDF change from QFT carry-forward in coherent local commits.
   Follow the integration plan and run required Python 3.12 validation;
   report recovery evidence, the worktree, commit IDs, and clean status.
   Preserve the original checkout/index and published Grover rc1 assets.
2. **Then implement QPE:** use the validated QFT conventions and preserve
   existing algorithm/runner regressions. Prepare the substantive QFT/QPE
   review before HHL/Shor. None of this implementation began this turn.
3. **In parallel, instructor feedback:** the user can send the two verified
   v0.2 guides and existing Grover rc1 ZIP link using [the plan](INSTRUCTOR_REVIEW_PLAN.md).
   State that the attached setup guide supersedes the older one in the ZIP.
   Sending has not been confirmed in this thread; do not assume it happened.
   Dates, platforms, and teaching feedback need not delay local Git integration.
4. **Before teaching release:** confirm dates, platforms, preparation, and
   assessment; validate native platforms and interactive setup, obtain the
   matching ChatGPT-reviewed PDFs, and rehearse delivery. Publication and
   instructor messages still require authorization covering those actions.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims; they
do not require pausing unrelated local work. Dates and assessment expectations
are still unknown. No implementation of QFT, QPE, HHL, or Shor was included in the
Grover preview. Remote CI passed for Grover. A deliberately failed remote job's
artifact-upload behavior and remote QFT checks remain untested.

**GPT Pro sync: not needed now; the corrected receipt closes the PDF issue.**
The next substantive review remains after QFT/QPE. Application tests/notebooks
were not rerun for the documentation-only follow-up. Full-file/prefix hashes,
the public ZIP download/integrity, and documentation checks are separate from
the earlier 50-test and 64-test results. Git integration and QPE remain planned.
