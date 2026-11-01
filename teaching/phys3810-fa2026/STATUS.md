# PHYS 3810 status

As of October 31, 2026: **R4 provisional presenter run sheets are prepared, and
local demonstration timing checks passed.** The [presenter index](R4_PRESENTER_RUN_SHEETS.md)
links all three proposed sessions, each with a 50-minute core and 75-minute
expanded route, predictions, notebook transitions, demonstrations, exercises,
and debriefs. [Machine timing evidence](R4_DEMONSTRATION_TIMINGS.md) records
42 fresh-kernel executions using the retained R1 environment. Human pacing
rehearsal remains **untested**; Rick's teaching decisions remain pending.

R3 host inventory and procedures remain prepared; Windows x64, macOS ARM64,
and macOS Intel execution remain **untested**. Only Ubuntu 26.04.1 LTS x86_64
is accessible, and the user confirmed no additional host. Exact procedures and
evidence requirements are in [R3_NATIVE_PLATFORM_VALIDATION.md](R3_NATIVE_PLATFORM_VALIDATION.md).
No target was provisioned, simulated, or reported passed without execution.

Linux retains R1's fresh-install evidence and R2's actual Chrome/JupyterLab UI
result: eight notebooks, 50 cells, 16 inspected figures, saving, shutdown/relaunch,
and preflight/Shor reruns. Native VS Code/Cursor UI is still untested, and exact
Chrome version remains unverified under the recorded R2 browser-policy limit.

R1's fresh installation of source `9e73b82` remains preserved, including all
110 frozen files/modes and the validated environment. Its **160-test** result
was not rerun or relabeled as a new UI test count. R2 used a separate copy;
only its outputs/kernel metadata changed, with notebook code/Markdown intact.
[R1 evidence](R1_FRESH_LINUX_VALIDATION.md) and the current UI evidence are distinct.
All 57 relevant runtime/test/notebook/runner/pin/workflow files match R1 source
`9e73b82`. R4 reused that environment to time notebook execution; no installation
or 160-test unit-suite rerun is claimed. Its three canonical trials each passed
eight notebooks, 50 code cells, and 16 PNGs. Six additional demonstration cases
were each checked three times in separate execution copies.

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

1. **Proceed to R5 under a separate local integration instruction.** Preserve
   the accepted history, refresh upstream read-only, inspect changes since the
   cached Grover base, and reconcile in a new durable worktree if needed. Record
   candidate identity and commit mapping, rerun affected/full required checks,
   and reassess earlier platform/UI evidence. No push, PR, merge, publication,
   or external message is implied by this recommendation.
2. **Resume R3 when actual native hosts become available.** Follow the prepared
   procedures with exact source identity, fresh environments, native architecture
   checks, full validator, and actual UI evidence. Windows x64 and each macOS
   architecture keep separate untested entries until then.
3. **Keep R4 agreement and human rehearsal open.** Use the prepared run sheets
   when the presenter and teaching decisions are available; record observed
   segment times and revisions. Validate native VS Code/Cursor only through
   authorized UI. Matching PDFs, final packaging, and publication remain later
   scoped work. Machine execution does not close those gates.

**GPT Pro sync: not needed now.** The HHL/Shor technical checkpoint is closed;
D1 and the optional O1/O2 changes have direct local evidence. Sync again for
unresolved mathematics, an expanded scope, or the matching final PDF/teaching
checkpoint when its inputs are ready. User input needed for the completed R4
preparation: none. Actual native host access and instructor target decisions
remain prerequisites for closing R3; agreed teaching scope and an observed
presenter run-through are still needed to close R4. Share Rick's reply when
received; no manual code audit is requested.

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

## R3 inventory/procedure evidence, October 31

Native host discovery was limited to this session's execution/tool inventory;
no SSH credential/config inspection, network scan, remote login, or infrastructure
provisioning occurred. Linux identity and unchanged runtime files were checked.
The user confirmed no additional host and requested procedures only. Windows
x64, macOS ARM64, and macOS Intel remain untested, not failed. No new 160-test
or UI execution is claimed.

Documentation checks, Python/Bash snippet syntax checks, source/asset/environment
preservation, and local links passed. PowerShell/native execution remains untested.
Evidence is under `artifacts/r3-native-platform-2026-10-31/`. The platform
procedures use actual-host constraint markers and do not impose Linux's package
count on another OS. No source/pin/algorithm contract or reviewed archive changed.

## R4 preparation and demonstration evidence, October 31

The three provisional run sheets use the proposed 50/75-minute routes without
assigning dates, assessed work, delivery roles, or confirmed in-class coverage.
Their minute allocations are planning estimates, not observed teaching times.
They include answer cues, prerequisite checks, explicit notebook dependencies,
parameter restoration, bounded algorithm claims, and overrun/failure handling.

The committed snapshot `07831f4c806d2c4203ea03aa589c31983cbb08de` was exported to
`/tmp/phys3810-r4-2026-10-31-03cwfyr5/source`; its 113 files/modes remained
unchanged during timing. Separate fresh kernels used R1's CPython 3.12.15
environment. Three trials covered each of the eight required notebooks. Derived
copies also exercised a changed Grover marked pair, QPE phases 1/8 and 6/8,
scaled-matrix and complex-state HHL examples, and Shor's presenter cell order.
All 42 executions passed their cell/error/count/figure checks: 291 repeated
code-cell executions and 102 generated PNGs in total. These repeated totals do
not replace the classroom baseline of eight notebooks/50 cells/16 PNGs.

Evidence is under `artifacts/r4-presenter-2026-10-31/`, with execution copies in
the separate `/tmp` staging directory. Timings cover local headless kernel/code
execution, including figure generation; they exclude browser interaction,
installation, explanation, learner exercises, discussion, and human rehearsal.
The 160-test result carries forward from unchanged source. No new PDF, package,
algorithm contract, environment installation, or external handoff was made.

Run-sheet cell references and 50/75-minute intervals, all 133 local documentation
links, source cleanliness, and pre-commit checks passed. Preservation checks
confirmed original checkout/index, frozen R1 source, environment identity/
distribution metadata, verified PDFs, reviewed archives, and Grover assets.
The interruption left no failed/partial timing record; all 33 initial runs were
retained before executing the nine additional Grover/QPE checks.
