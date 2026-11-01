# PHYS 3810 status

As of October 31, 2026: **R2's Linux/Chrome JupyterLab workflow passed.**
All eight required notebooks ran through actual UI kernel selection and
restart/run-all, with **50 code cells and 16 inspected PNG figures**. Saving,
server shutdown/relaunch, and preflight/Shor reruns passed. See
[R2_INTERACTIVE_VALIDATION.md](R2_INTERACTIVE_VALIDATION.md).
Native VS Code/Cursor UI remains untested; exact Chrome version is unverified
because the browser policy blocked its internal version page.

R1's fresh installation of source `9e73b82` remains preserved, including all
110 frozen files/modes and the validated environment. Its **160-test** result
was not rerun or relabeled as a new UI test count. R2 used a separate copy;
only its outputs/kernel metadata changed, with notebook code/Markdown intact.
[R1 evidence](R1_FRESH_LINUX_VALIDATION.md) and the current UI evidence are distinct.
Next is R3 native-platform preparation/execution where authorized hosts exist.

The HHL/Shor independent review remains accepted and its follow-ups reconciled.
That review executed the earlier 158-test snapshot in a reused Python 3.12.14
environment; the current 160-test source includes two figure-gate regressions.
See [the review disposition](HHL_SHOR_REVIEW_RECONCILIATION.md) and
[the readiness plan](RELEASE_READINESS_PLAN.md) for the separate evidence stages.

HHL remains the exact-spectrum 2x2 demonstration under [HHL_PLAN.md](HHL_PLAN.md).
Shor now implements [SHOR_PLAN.md](SHOR_PLAN.md): compiled full-domain N=15
permutations, four residue qubits, a separate order finder, conservative exact
order recovery, and explicit factor failures. The QPE contract is unchanged.
Independent source/teaching tests verify complete complex states and failures;
all 50 required code cells execute and 16 PNGs are produced.

The user sent the initial setup/Grover email on October 30 and is awaiting the
instructor's reply. The supplied screenshot confirms a student setup attachment;
delivery of the rest of the recommended packet is not assumed. Session coverage,
student preparation, format, assessment, teaching responsibility, and preferred
examples remain open. See [INSTRUCTOR_REVIEW_PLAN.md](INSTRUCTOR_REVIEW_PLAN.md).

The independent QFT/QPE and HHL/Shor reviews are accepted. The two stale
notebook availability statements are corrected, all three HHL/Shor figures are
required, and Shor displays theoretical recovery probabilities. Algorithm source
and QPE supported inputs remain unchanged. The original
checkout/index, reviewed phase ZIP, verified PDFs, and Grover rc1 assets remain
intact. Work remains local; R2 served the copied source on authenticated loopback
and left no test server running. No publication, external message, package
upgrade, or hardware job was performed.

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
  checkpoint, including two QFT figures. The complete suite is now 160 tests/eight notebooks.
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
- **Shor implemented and tested locally:** compiled full-domain N=15 source,
  19 mathematical tests, ten actual-cell regressions, and an eight-code-cell
  notebook with three figures. The full 158-test/eight-notebook suite passes.
  The independent review accepted that snapshot. Subsequent D1/O1/O2 updates
  preserve the algorithms and raise the local test count to 160.
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

1. **Prepare/perform R3 of the [readiness plan](RELEASE_READINESS_PLAN.md).**
   Inventory actual authorized native-host access, execute setup/validator/UI
   checks only where that host is available, and retain explicit untested labels
   elsewhere. Keep platform requirements provisional while Rick's reply is pending.
2. **Retain the editor gap separately.** VS Code/Cursor was not accessible through
   the available native controls. Do not substitute CLI or headless evidence for
   editor interpreter/kernel selection; validate it when an authorized UI surface
   exists or narrow the eventual supported workflow explicitly.
3. **Continue the later gates without assuming completion.** Teaching decisions/
   pacing, protected upstream integration, matching PDFs, final package, and
   publication retain their completion criteria and authorization boundaries.

**GPT Pro sync: not needed now.** The HHL/Shor technical checkpoint is closed;
D1 and the optional O1/O2 changes have direct local evidence. Sync again for
unresolved mathematics, an expanded scope, or the matching final PDF/teaching
checkpoint when its inputs are ready. User input needed for native-host inventory/preparation: none. Actual host
access or classroom platform decisions may be needed before native runs can pass. Share Rick's reply when received; no manual code audit is requested.

At the previous reconciliation, required Python 3.12, lint, smoke, pre-commit,
notebook cleanliness, link, and preservation checks passed. That evidence is under
`artifacts/hhl-shor-review-2026-10-30/`. The unchanged reviewed ZIP and original
158-test extraction evidence remain under `artifacts/shor-2026-10-30/`; the prior
desktop copy is no longer present. No replacement archive was needed or created.
Do not distribute that historical ZIP as the corrected current student packet.

The independent review reused an environment; R1 now separately establishes
a fresh local dependency installation of the corrected source. R2 adds actual
Linux JupyterLab execution; native Windows/macOS, native editor UI, timed
teaching, and remote CI remain untested. Runtime/cloud/GPU remain
excluded. Original checkout/index, verified PDFs, and Grover rc1 assets are
preserved. No push, PR, merge, publication, message, or hardware job occurred.

## Readiness planning evidence, October 30

The planning baseline is `ec073599bb7c87019f957c129e8c6e4d66e9a61c`: eight
local integration commits after cached `origin/main`/Grover rc1 `3894391`. No
remote refresh or live ruleset check was performed; this does not establish
current upstream state. The new planning commit is separate from that inventory.
Existing workflows/dependency files match the cached published base.

In that planning turn, only Markdown plans/context changed. Documentation and
preservation checks passed; application tests were deliberately not rerun. The 160-test/eight-notebook result above remains the previous reconciliation's
execution evidence. At that point fresh installation, UI/native-host checks,
rehearsal, new PDFs/package, and publication were unperformed. R1 was subsequently
completed on October 31 as recorded above; the other gates remain open. Details are retained in ignored
`artifacts/release-readiness-plan-2026-10-30/`.

## Fresh-install evidence, October 31

The new environment started with bootstrap pip only, excludes system/user site
packages, and resolves application imports/kernels inside the new staging area.
All 114 installed application distributions match active constraints; pip 26.2.2
is the sole separately pinned bootstrap tool. Optional Runtime was not installed.
Required runtime checks ran against the isolated export; Ruff used separate
maintainer tools there, and pre-commit ran in the integration worktree because
it requires Git metadata. Source bytes, old environment configuration/package
metadata, original checkout/index, and immutable assets remain preserved.
Detailed receipts/logs are under `artifacts/r1-fresh-linux-2026-10-31/`. The retained
`/tmp` staging can support R2 but is not a durable backup or student package.

## Interactive evidence, October 31

The R2 copy contains the same 110 source files initially; only the eight executed
notebooks' outputs/metadata changed, with all source cells intact. All 16 figures
were inspected in Chrome. JupyterLab's About dialog displayed 4.6.4; the named
Python (PHYS 3810) kernel points to R1's 3.12.15 interpreter. Kernel registration
and user/runtime settings were placed outside the frozen environment. This is a
documented validation adaptation, not a certification of every literal setup
command or editor path. The old environments, original checkout/index, verified
PDFs, and archived releases/reviews remain preserved.

An auxiliary per-cell timestamp comparison failed because the UI configuration
stores no such timing metadata. Actual UI transitions, server lifecycle records,
and completed saved outputs support the rerun result. The browser approval gate
rejected `chrome://version` under its HTTP(S)-only policy; the version is marked
unverified without a workaround. Evidence remains under ignored
`artifacts/r2-interactive-2026-10-31/`. No student package or external handoff
was created, and no additional algorithm review is due solely for these checks.
