# PHYS 3810 status

As of October 30, 2026: **HHL and Shor design contracts are complete;
implementation remains unstarted.** The next scoped work is HHL under
[HHL_PLAN.md](HHL_PLAN.md), followed separately by the compiled N=15 model in
[SHOR_PLAN.md](SHOR_PLAN.md). These are design decisions, not new algorithm
execution evidence. The accepted QFT/QPE baseline remains **97 tests and six
notebooks**, last executed during the review reconciliation.

HHL admits 2x2 Hermitian positive matrices with integer eigenvalues 1-7,
uses `exp(+i*pi*A/4)`, three count bits, one system qubit, and one success flag.
Shor retains a full four-qubit residue register for N=15, uses explicit compiled
modular-permutation gates, and verifies exact-rational order candidates.
Its separate builder uses the existing QFT; the QPE helper is not widened.

The independent QFT/QPE review is accepted, and its P3 follow-ups are reconciled.
The original checkout/index, reviewed ZIP, verified PDFs, and Grover rc1 assets
remain intact. Only Markdown plans/context changed in this design turn; no
circuit implementation, new notebook, dependency change, or external action
was performed. Scalar design fixtures and documentation checks are recorded
separately from the existing execution baseline.

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
- **Design contracts complete:** exact-spectrum HHL with five logical qubits;
  compiled full-domain N=15 order finding with 8-10 logical qubits and verified
  classical postprocessing. Independent acceptance gates and error cases are
  specified in the linked plans.
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

1. **Implement HHL only as the next milestone.** Follow its exact-spectrum
   contract, including target preparation, reciprocal lookup, both-branch count
   cleanup, success probability, normalized solution, and relative sign/phase.
   Add independent mathematical tests, a teaching notebook, and strict validator
   integration; preserve all existing regression coverage.
2. **Then implement the separate bounded Shor milestone.** Keep four residue
   qubits, the full-domain permutation contract, conservative exact-rational
   recovery, and honest failure outcomes. Do not widen QPE or claim general
   reversible-arithmetic performance.
3. **In parallel, instructor feedback:** the unchanged Grover packet is ready;
   dates, target platforms, preparation, depth, and assessment remain open.
4. **Before a combined teaching publication:** review completed HHL/Shor evidence,
   validate claimed platforms/UI, rehearse pacing, and obtain matching reviewed
   PDFs. Publication and messages require applicable authorization.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims; they
do not require pausing unrelated local work. Dates and assessment expectations
are still unknown. No implementation of QFT, QPE, HHL, or Shor was included in the
Grover preview. Remote CI passed for Grover. A deliberately failed remote job's
artifact-upload behavior and remote QFT checks remain untested.

**GPT Pro sync: not needed solely for these bounded design contracts.** The
pre-HHL/Shor phase review is already accepted, and QPE/environment scope is
unchanged. Sync sooner if the contracts expand or unresolved mathematics arises;
retain the later combined HHL/Shor review before publication. User input needed
for the defined next local milestone: none. Instructor decisions remain open
without being invented or assigned as manual code review.

Design validation: nine classical HHL fixtures, seven scalar rotation amplitudes,
128 modular-permutation images, 1,024 composition images, and selected rational
recovery/factor cases were checked. These calculations do not execute HHL/Shor.
Application tests were deliberately not rerun for Markdown-only changes.
`pre-commit run --all-files`, whitespace checks, and 56 relative documentation
links passed. Content hashes confirmed source, tests, notebooks, QPE contract,
dependencies, and PDFs unchanged, with the original checkout/index and release
assets preserved. Local evidence is under `artifacts/hhl-shor-design-2026-10-30/`.
