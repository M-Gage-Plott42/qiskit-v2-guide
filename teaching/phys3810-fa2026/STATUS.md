# PHYS 3810 status

November 2, 2026: **the beginner guided route is implemented and source validation
passed: 197 tests, eleven fresh-kernel notebooks, 74 nonempty code cells, 27 PNGs.**
The [contract](GUIDED_TEACHING_PLAN.md), [review entrance](guided/START_HERE.md),
and [validation record](GUIDED_VALIDATION.md) identify the scope and evidence.
The current task is completing rendering/OCR, exact exported-package checks,
desktop delivery, and commit/push with CI. This is an instructor review kit,
not a replacement release or final classroom approval.

The received planning return reports two or three classes, no Python experience,
no grading/evaluation/assignments/submissions, and demonstrations repeated on
laptops. Material receipt is acknowledged; the instructor offers to deliver
following a walkthrough, with detailed review and delivery arrangements still
open. The proposed route is Python/Qiskit, Grover, QFT/QPE; the two-day fallback
uses Python/Qiskit plus one algorithm day, default Grover. HHL and full compiled
Shor remain references. All five implementations and their contracts are preserved.

The current author name is **Gage Plott**. New audience-facing material excludes
internal model/workflow notes. Historical PDF/companion bytes remain unchanged
and excluded from this new packet. The original release at `f717aea`, reviewed
documentation at `7600e85`, and recovery stash remain preserved. The optional GPU
repair and dependency-update PRs are outside this scope.

## Historical November 1 position

November 1 post-publication review: **the independent audit is accepted, and
the supplied full-course document-v0.2 review editions are reconciled locally.**
See [the receipt and finding dispositions](NOVEMBER_REVIEW_RECONCILIATION.md).
The reviewed baseline is `f4990b4`; published source remains `f717aea`.
Repository navigation/status issues are repaired in documentation only. The
optional GPU error-reporting finding is recorded for a separately scoped code
fix. The new instructor edition resolves P3-01; the unchanged v0.1 edition still
needs its reading note. Neither edition claims final classroom approval.

The class period is now known: **12:40–2:05 PM, 85 minutes**. November 16, 19,
and 23 remain provisional. November 19 is Thursday, inconsistent with the
listed Monday/Wednesday schedule; confirm the date rather than substituting
one. Session count beyond three and allocation of QPE/HHL remain unresolved.
See [the course plan](COURSE_PLAN.md). No reply, outreach, human rehearsal,
native-platform/editor check, commit, push, or new release occurred during the
reconciliation. The subsequent CP-and-park instruction authorizes committing
and pushing the documentation on `docs/phys3810-november-review`, then stopping.

## Published preview and earlier milestones

November 1, 2026 update: **the full-course provisional preview is published.**
[Release v0.2.0-rc1](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-v0.2.0-rc1)
uses source `f717aea`; PR #113 passed all nine required checks before normal
merge. The merged-source ZIP passed 160/eight/50/16 plus smoke/lint, and both
published assets were anonymously downloaded and hash-verified. The
[publication receipt](PUBLIC_PREVIEW_RELEASE.md) records exact assets and limits.
The original dirty checkout was preserved in verified stash `2705385` and recovery
files, then fast-forwarded to clean main. Completion documentation is delivered
through the normal workflow. The requested preview is delivered; **wait for
Rick's reply or a specific new change** rather than starting another preparation
cycle. Final classroom and teaching/native/editor/pacing gates remain open.

As of October 31, 2026: **R7 local preview packaging passed.** The
[builder contract](R7_PREVIEW_PACKAGE.md) and [execution evidence](R7_PREVIEW_VALIDATION.md)
identify source `135d5d0` and the unpublished 47-file preview. It includes the
verified student PDF unchanged and excludes instructor answer documents/PDFs.
All 160 tests/eight notebooks/50 cells/16 PNGs passed from a separate extraction
in the reused R6 environment; all payload hashes/modes stayed unchanged. Twenty
builder acceptance cases and an identical repeat build passed. No publication,
new PDF, environment installation, UI/native check, or hardware job occurred.

The provisional document review remains received and reconciled locally. The [reconciliation](R6_DOCUMENT_REVIEW_RECONCILIATION.md)
records the accessible return ZIP, four-page student PDF, six-page instructor
PDF, synchronized companions, receipt checks, and scoped editorial integration.
PDF bytes are unchanged. Student commands remain unchanged; local companion
edits add only hidden lint annotations. A nonblocking [phase-decoding reading
clarification](instructor/README.md) is recorded for the next instructor edition.
Rick's reply, native/editor coverage, human pacing, and final classroom approval
remain open. No publication or external message occurred.

The earlier provisional GPT Pro document-review handoff remains preserved. The [handoff receipt](R6_DOCUMENT_REVIEW_HANDOFF.md)
identifies the ZIP frozen at `c63381a`, source/adaptation manifest, desktop hash,
extracted validation, and separate prompt. The 50-file archive passed 160 tests,
eight notebooks, 50 cells, and 16 PNGs using the reused R6 environment. The
subsequently supplied review identifies that exact archive/source. Its separate
fresh Ubuntu CPython 3.12.14 execution reports the same 160/eight/50/16 result;
raw execution logs are referenced by receipt hashes, not included in the return.
Local document-only integration does not claim a new runtime or UI execution.

The R6 Ubuntu student-guide walkthrough remains passed.
A fresh in-project `.venv` installed unchanged pins, registered the named kernel
with `--sys-prefix`, and passed 160 tests/eight notebooks/50 cells/16 PNGs.
Actual JupyterLab UI execution covered all eight notebooks and all 16 figures;
shutdown/reopen with cleared-output preflight/Shor reruns also passed. See
[R6_GUIDE_WALKTHROUGH_VALIDATION.md](R6_GUIDE_WALKTHROUGH_VALIDATION.md) for exact
source/guide hashes, commands, UI coverage, and configuration limits.

R6 provisional Markdown companions remain prepared.
The [student setup draft](handouts/FULL_COURSE_SETUP_DRAFT.md) and
[instructor guide draft](instructor/FULL_COURSE_INSTRUCTOR_DRAFT.md) are separate
document-v0.1 inputs for proposed code-v0.2.0-rc1. They keep the unpublished
full-course download, untested platform/editor paths, and pending teaching
choices explicit. [R6_DOCUMENT_INPUTS.md](R6_DOCUMENT_INPUTS.md) now records the
received review and remaining inputs before a final classroom edition. The
initial Markdown-only preparation created no PDFs; the later supplied PDF
editions are now integrated as recorded above.

R5 protected local integration remains passed. The fresh
upstream check found no changes after `3894391`; all 13 accepted local commits
through `0570863` remain intact. The new candidate worktree is
`artifacts/local-candidate-2026-10-31/worktree` beneath the original repository,
on `candidate/phys3810-fa2026-v0.2.0-rc1`. Required Python 3.12 checks passed:
160 tests, eight fresh-kernel notebooks, 50 code cells, and 16 PNGs. The existing
R1 environment was reused, not reinstalled. See
[R5_CANDIDATE_VALIDATION.md](R5_CANDIDATE_VALIDATION.md) and the
[provisional publication draft](CLASSROOM_PUBLICATION_DRAFT.md).

R4 provisional presenter run sheets are prepared, and local demonstration
timing checks passed. The [presenter index](R4_PRESENTER_RUN_SHEETS.md)
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

Confirm final dates/count, algorithm priorities or substitutions, laptop/setup
arrangements, prior quantum coverage, and delivery responsibility after the
walkthrough. The listed period is 85 minutes, with 75 planned plus ten margin.
November 16/19/23 remain provisional; November 19 is Thursday, conflicting with
the listed Monday/Wednesday pattern. No substitute date or mandatory guest
attendance has been inferred. Zero Python, laptop follow-along, and absence of
assessment are now settled requirements, not open questions.

## Recommended next action

Complete and provide the focused beginner-kit review, then use its concise
agenda for the walkthrough. No broad algorithm reaudit is needed. **GPT Pro sync:
recommended after the verified kit is ready**, focused on novice explanations,
editable-cell behavior, strict profile integration, and short documents.
No user technical audit or further input is needed to finish this authorized
scope. Teaching decisions above remain provisional until discussed.

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

## R5 protected candidate evidence, October 31

The accepted integration worktree remains at `0570863` and its original raw
index/status/files are preserved. The new candidate adds only Markdown R5
context/evidence/publication planning. There were no upstream commits to replay,
conflicts to repair, or algorithm changes. A complete pre-fetch Git bundle was
verified, restored into an isolated bare repository, and checked against all
118 accepted file hashes; the older recovery materials remain unchanged.

R5 reran dependency, standalone unit, classroom-validator, Ruff, and Bash-smoke
checks. Both unit invocations ran the same 160 tests; saved classroom outputs
independently verify eight notebooks/50 cells/16 PNGs. The selected interpreter
was R1's retained CPython 3.12.15. Source notebooks, dependency pins, workflows,
verified PDF bytes, original Grover assets, and reviewed archives are unchanged.
Final lint, all 311 local file links, Git-scope, and preservation checks passed;
the completion receipt records the committed candidate's clean status.
Evidence is under the original repository's
`artifacts/local-candidate-2026-10-31/evidence/`.

The provisional full-course identity is `v0.2.0-rc1`, separate from Grover rc1
and document-v0.2. No matching remote tag was advertised by the exact read-only
query; no tag or package was created, and availability must be rechecked before
publication. Earlier R1/R2/R4 evidence retains its recorded source/method limits;
no UI, native-platform, or human-pacing pass was added here. Rick's reply remains
pending. No external write, publication, new PDF, or hardware job occurred.

## R6 provisional Markdown evidence, October 31

The drafts use candidate `d491b3b` as their source baseline. Student setup
contains the current notebook list, unchanged package pins, validation output,
kernel selection, return workflow, and troubleshooting without maintainer
coordination or instructor answer cues. The instructor companion adds bounded
contracts, answer cues, provisional session routes, and evidence limits. It
explicitly notes that the existing notebooks already reveal worked results;
excluding an instructor file does not make them an answer-free assessment.

R2's actual JupyterLab run used a preservation-specific external kernelspec and
sibling environment. The ordinary in-project `.venv`/`--sys-prefix` sequence
retained in the new student draft is therefore still pending a literal complete
walkthrough. This does not invalidate the observed R1/R2/R5 results, and those
results do not newly certify that draft's command sequence.

Documentation, command-syntax, consistency, and preservation checks are recorded
under `artifacts/r6-markdown-2026-10-31/` in the candidate worktree. No runtime
suite, installation, kernel registration, UI session, new PDF, package, external
message, or hardware job was performed. The 160-test/eight-notebook/50-cell/
16-PNG result remains R5 evidence. Existing Grover guides/links/PDFs, source,
contracts, tests, pins, archives, both earlier checkouts/indexes, environments,
and R5 receipts remain preserved. Final PDF rendering/visual review/OCR and
actual delivered-byte verification await a later document handoff.

Documentation checks passed: 365 local file links, five Bash syntax blocks,
two inline Python parses, source/contract/count consistency, and pre-commit.
Preservation checks confirmed 114 unchanged candidate files and all 51 R5
evidence files, plus the earlier checkout/index/assets/environment receipts.
The completion receipt records the new local commit and clean candidate status.

## R6 literal Ubuntu walkthrough evidence, October 31

Source `7b8a8e2` and the recorded student-guide bytes were exported to isolated
staging outside both prior checkouts. Python 3.12.15 already existed; a new
in-project `.venv` began with only bootstrap pip. Unchanged requirements installed
114 application distributions matching active pins plus pip 26.2.2. The full
validator and supplemental required checks passed. No command, dependency,
algorithm, or contract repair was needed. The student guide's executable blocks
remain identical; its introductory validation status is updated.

All eight notebooks were explicitly assigned the named kernel and restarted,
run, inspected, and saved through Chrome/JupyterLab 4.6.4. All 16 figures were
visually inspected. The server was shut down, its tab closed, and JupyterLab
reopened without reinstalling packages or re-registering the kernel. Preflight
and Shor outputs were cleared and their kernels restarted/run again. Both server
children exited zero; the first outer launcher session reported 143 during
cleanup, with the application's shutdown independently confirmed. Final task
server records are absent and task tabs are closed.

Saved notebook counts/cell content corroborate the UI. First/final bytes are
identical under the fixed seeds and configuration; reruns are evidenced by actual
UI transitions and server logs, not inferred from timestamps or file changes.
Working-copy notebook outputs/metadata changed, while source cells and the other
115 exported files stayed intact. R1/R2 staging and existing environments,
prior checkout/index states, PDFs, recovery material, and archives are preserved.
No new PDF, student package, external transfer, publication, or hardware job was
performed. Evidence is under `artifacts/r6-walkthrough-2026-10-31/`.

Final documentation checks passed: 379 local file links, eight Bash syntax
blocks, unchanged student-guide executable blocks, and pre-commit. All 114
unchanged tracked files, ten prior Markdown evidence files, and 51 R5 evidence
files retain their bytes. The completion receipt identifies the new local commit
and clean candidate worktree; earlier checkout/index preservation is separate.

## R6 document-review packet evidence, October 31

The archive `PHYS3810-Document-Review-2026-10-31-c63381a8e6fb.zip` is 164550 bytes;
its SHA-256 is `f0af2bfd8507a5c1c6aedc04d67bfacee86faf34d678a4e77e70fd42e853980c`.
The desktop copy matches the sealed retained copy. All 36 canonical source/
test/notebook/dependency/student-guide files retain exact committed bytes;
13 guidance exports/generated entry points disclose their adaptations, and
one manifest covers the other 49 files. No prompts, policy/chat files, old PDFs,
archives, caches, environments, credentials, or generated outputs are included.

Independent payload inspection passed, including 100 local file/fragment links
and safe ZIP paths. The extracted archive passed dependency checks, the full
160-test/eight-notebook validator with 50 cells/16 PNGs, and Bash smoke. Imports
resolve inside the extracted copy; all 50 payload files and the sealed ZIP stayed
unchanged. This reused the earlier walkthrough environment; it is not another
fresh install or new UI execution. No source/contract repair was needed.

Evidence is under `artifacts/r6-doc-review-2026-10-31/`. The included validation
summary predates sealing and explicitly defers the final extracted-run receipt
to the handoff record; no post-verification payload edits were made. The new
handoff/status commit is distinct from the frozen source inside the ZIP.
User upload, new review disposition, and returned PDF/Markdown bytes remain
pending. Existing assets, environments, source staging, and prior indexes remain
preserved. No publication, external message, or hardware job occurred.

## R6 returned document reconciliation, October 31

The Downloads ZIP is accessible and matches the reported 176121 bytes and
SHA-256 `45520beb2780f713d903f225970541b35d9d71041b6bb4d1af5f77eb8916b927`.
All six members are retained; the receipt verifies the five other members.
The input archive/source and both exported Markdown base hashes match the
outgoing packet. The export-based patch applies in an isolated copy and exactly
reproduces the returned companions. All four reported editorial findings were
reproduced and their corrections accepted.

The unchanged PDFs pass local whole-file hash/size, four/six-page Letter
geometry, title/empty-author metadata, five HTTPS annotation/rectangle checks,
embedded-visible-font checks, and exact normalized body-text correspondence.
All ten pages were rendered at 150 dpi and visually inspected locally. Five
primary documentation URLs opened successfully. Reviewer-reported 300 dpi OCR
was not rerun locally. Full PDF bytes and provenance were preserved; no PDF
was regenerated, optimized, or stripped.

The revised Markdown keeps all six student fenced blocks unchanged. Two hidden
single-line MD036 directives preserve the authored edition labels while passing
repository lint; their distinct repository hashes are recorded separately from
received Markdown hashes. The P3-01 reading note qualifies phase-fraction
conversion for phase-estimation count registers; it is nonblocking for these
provisional review drafts and pending the next authored instructor edition.

Runtime source, tests, notebooks, constraints, supported inputs, old Grover
editions/assets, original and accepted checkouts/indexes, recovery materials,
review archives, Downloads ZIP, and existing environments/staging remain
preserved. No unit suite was rerun solely for document changes. The independent
reviewer's fresh 160/eight/50/16 result remains a separately attributed report.
Evidence is under `artifacts/r6-doc-reconciliation-2026-10-31/`.

Final checks passed: 378 local file links, seven Bash syntax blocks, unchanged
student commands, pre-commit, and preservation. The completion receipt records
the local integration commit and clean candidate status. No original checkout
or accepted integration index was changed.

## R7 local preview evidence, October 31

The scoped full-course builder and its four deployment-relative Markdown
sources were committed in `135d5d00e3197708a26b547013a0fd8105194385` before building.
It reads only that commit's inputs, requires the exact reviewed student document
pair, rejects inventory/output/link drift and overwrites, and records provenance.
Two guard defects were repaired before the source commit: Git-tree inventory
prevents export-ignore from hiding tests, and protocol-relative/hostless links
are rejected. All 20 CLI acceptance cases passed in a disposable Git fixture;
no protected checkout was changed to test failures.

The sealed preview is `PHYS3810-Fall2026-v0.2.0-rc1-local-135d5d00e319.zip`,
200130 bytes, SHA-256
`7cd1cb0a75b268141a8962d512fe38deb3fe1a38911e90577d736fe445a2f79f`.
The independent payload audit confirmed 47 safe files, 46 manifest entries,
37 exact committed files, five retained technical bodies, four template renders,
and 50 internal file/fragment links. The entire instructor folder and excluded
history/policy/prompt/cache/output/credential content are absent. The tested
student PDF/Markdown hashes are unchanged. Known expectations remain in tests,
notebooks, and contracts; no assessment-safe claim is made.

The extraction outside all checkouts passed dependency consistency, the full
160-test/eight-notebook validator, Bash smoke, Ruff, and exported Markdown lint
under the existing repository profile. Saved outputs verified 50 complete cells,
zero errors, and 16 actual PNGs. The initial Markdown lint check used standalone
defaults; selecting the unchanged repository profile resolved its long-line
findings without changing payload bytes. Every delivered file and the sealed
ZIP remained unchanged. An actual repeat build is byte-identical.

This reused the R6 CPython 3.12.15 environment; no new fresh-install, UI/native,
PDF, remote-CI, or classroom-readiness pass is inferred. P3-01, Rick's decisions,
platform/editor coverage, human pacing, final document wording, and publication
remain open. Source, old builders, reviews, PDFs, environments/staging, original
and accepted indexes, and Grover assets remain preserved. Local evidence is
under `artifacts/r7-preview-2026-10-31/`; the final context commit is separate
from the build-source identity inside the archive.

One preservation exception was observed at the final check: the incoming review
ZIP's original Downloads path is now absent, although it existed at the start.
Its verified 176121-byte retained copy inside reconciliation evidence still
matches SHA-256 `45520beb2780f713d903f225970541b35d9d71041b6bb4d1af5f77eb8916b927`;
the PDF/Markdown editions and outgoing review archives remain intact. The cause
is unverified. No Downloads file was restored or deleted by R7 work. This is
recorded explicitly and does not invalidate the committed-source preview.
