# PHYS 3810 status

As of October 30, 2026: **HHL is implemented and locally validated: 129 tests
and seven required fresh-kernel notebooks passed.** This retains all 97 existing
tests and adds 23 HHL mathematical tests plus nine actual-notebook regressions.
See [HHL_VALIDATION.md](HHL_VALIDATION.md) for commands, tolerances, artifacts,
and limits. The next scoped implementation is Shor under [SHOR_PLAN.md](SHOR_PLAN.md).

HHL follows [HHL_PLAN.md](HHL_PLAN.md): 2x2 positive Hermitian matrices with
integer eigenvalues 1-7, positive evolution, three count bits, one system qubit,
and one success flag. Raw success/failure amplitudes, probability, both-branch
count cleanup, normalization, and complex relative phase are checked independently.
Shor remains design only: compiled full-domain N=15 modular permutations with
four residue qubits and a separate builder. The QPE contract is unchanged.

The user sent the initial setup/Grover email on October 30 and is awaiting the
instructor's reply. The supplied screenshot confirms a student setup attachment;
delivery of the rest of the recommended packet is not assumed. Session coverage,
student preparation, format, assessment, teaching responsibility, and preferred
examples remain open. See [INSTRUCTOR_REVIEW_PLAN.md](INSTRUCTOR_REVIEW_PLAN.md).

The independent QFT/QPE review is accepted. HHL has local implementation review
and execution evidence, not an independent GPT Pro review yet. The original
checkout/index, reviewed phase ZIP, verified PDFs, and Grover rc1 assets remain
intact. Work remains local; no Shor implementation or external action was performed.

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
  checkpoint, including two QFT figures. The HHL milestone now extends the suite to 129 tests/seven notebooks.
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
- **HHL implemented and tested locally:** canonical circuit and reciprocal helper,
  23 mathematical tests (including all 28 spectral pairs), nine editable-cell
  regressions, and a seven-code-cell notebook with three figures. All 42 required
  code cells across seven notebooks executed; 13 PNGs were produced.
- **Not implemented / untested:** Shor lesson.
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

1. **Implement the bounded Shor milestone.** Keep four residue qubits, the
   full-domain permutation contract, conservative exact-rational recovery, and
   honest failure outcomes. Add independent tests, a teaching notebook, and
   strict validator integration; preserve all 129 regressions. Do not widen QPE.
2. **Then prepare the combined HHL/Shor GPT Pro review.** Produce one runnable
   ZIP on the desktop with a separate review prompt, enforce bundle exclusions,
   and verify an extraction outside the checkouts. Record the exact reviewed
   snapshot and actually received response before claiming independent acceptance.
3. **In parallel, await instructor feedback.** The setup email is already sent;
   no follow-up has been sent or scheduled by the assistant. Continue bounded
   local development while teaching decisions remain provisional.
4. **Before a combined teaching publication:** validate claimed platforms/UI,
   rehearse pacing, and obtain matching reviewed PDFs. Publication and messages
   require applicable authorization.

Native Windows/macOS checks and instructor decisions can progress alongside
Linux algorithm development. They limit portability and release claims, not
unrelated local work. The Grover preview still contains no later algorithms.
Remote CI passed for Grover; remote checks for subsequent local commits and
intentional failure-artifact upload remain untested.

**GPT Pro sync: not needed for this bounded HHL implementation alone.** The
pre-HHL/Shor phase review is accepted and the contract/environment is unchanged.
The next planned sync follows completed Shor and the combined evidence packet;
sync sooner for unresolved mathematics or a scope change. User input needed
for the defined next local milestone: none. Instructor decisions are pending.

The required Python 3.12 checks, Ruff, original smoke workflow, pre-commit,
source-notebook cleanliness, documentation links, and preservation checks passed.
Detailed local evidence is under `artifacts/hhl-2026-10-30/`; the public summary
is [HHL_VALIDATION.md](HHL_VALIDATION.md). The earlier scalar-only design record
remains under `artifacts/hhl-shor-design-2026-10-30/` and is not relabeled as
algorithm execution.
