# PHYS 3810 status

As of October 29, 2026: **Grover's review is reconciled; its prerelease workflow is authorized and QFT is next**.
The [versioned release page](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1)
records publication availability. This source snapshot does not infer remote
check results from local tests. See [VALIDATION.md](VALIDATION.md) for the base, inventory, commands,
installed versions, outcomes, and reviewer handoff.

Technical review and validation are owned by the implementation assistant;
the user is not being asked to review code manually. The latest coordination
plan is [WORKFLOW.md](WORKFLOW.md). GPT Pro's review of source snapshot
`06e22d9b5d2a` was received, and its required validator correction was reproduced,
fixed, and tested. See [REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md) for
findings, execution evidence, and the basis for closing that checkpoint.
The new lesson's evidence is in [GROVER_VALIDATION.md](GROVER_VALIDATION.md).
The received Grover review and five new exercise regressions are recorded in
[GROVER_REVIEW_RECONCILIATION.md](GROVER_REVIEW_RECONCILIATION.md). The proposed
versioned preview is separate from QFT development; see [PREVIEW_PLAN.md](PREVIEW_PLAN.md).

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
- **Independent review evidence:** GPT Pro reported another Linux install on
  CPython 3.12.14 with the same 114 application-package pins, all original 19
  tests and three notebooks passing, and reproduced M1-01. The correction was
  subsequently verified here on CPython 3.12.15. The later Grover review also
  reproduced all 45 then-current tests/four notebooks and closed M1-01. The
  latest G1 correction was demonstrated locally, without another GPT Pro run.
- **Untested on native hosts:** Windows x64 and macOS. Compatible package wheels
  were checked; this is not installation or notebook-execution evidence.
- **Skipped by classroom validation:** optional Runtime/cloud and GPU paths.
  No IBM service calls or hardware jobs are part of milestone 1 validation.
  A separate optional environment passed the Runtime fake-backend smoke locally;
  this does not validate hardware access.
- **Not implemented / untested:** QFT, QPE, HHL, and Shor lessons.
  The original smoke notebooks do not count as those algorithm implementations.
- **Drafts now, final later:** setup and instructor review PDFs are prepared
  from editable sources. Final classroom PDFs still require feedback and
  platform validation; use the release page for the versioned review assets.

## Open teaching decisions

Actual session dates, student preparation, session length, and assessment
expectations remain unknown. Proposed sequence: Grover; QFT/QPE; HHL/Shor.
Each session has a 50-minute core and a 75-minute expansion in the course plan.
UTC has no classes November 25–29, and November 30 is the last class day;
these facts do not establish the invited-session dates.

## Recommended next actions

1. **Complete the authorized Grover prerelease:** preserve upstream fixes and
   the normal PR/check workflow; build/test assets from the merged revision.
   Authorization covers this preview's push, PR, green-check merge, and prerelease.
2. **Implement QFT:** follow [QFT_PLAN.md](QFT_PLAN.md), retaining the existing
   algorithm and notebook regressions. No manual code audit is assigned to the user.
3. **Then QFT/QPE, then HHL/Shor:** follow the staged acceptance criteria in the
   course plan and the explicit sync points in the workflow.
4. **Before teaching release:** resolve target-platform validation, produce and
   inspect the linked setup PDF, rehearse the sessions, and prepare publication
   for a separately authorized action.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims; they
do not require pausing unrelated local work. Dates and assessment expectations
are still unknown. No implementation of QFT, QPE, HHL, or Shor was started in the
Grover preview. Remote CI behavior, including failure artifact upload, remains
untested; local lint does not establish a remote execution result.
