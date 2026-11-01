# Classroom-release readiness plan

Updated October 31, 2026. **R1 passed:** fresh installation of unchanged pins
on Linux/CPython 3.12.15 validated the corrected 160-test revision. See
[R1_FRESH_LINUX_VALIDATION.md](R1_FRESH_LINUX_VALIDATION.md). All five bounded
lessons and their technical reviews remain complete. **R2's Linux/Chrome
JupyterLab path passed**; see [R2_INTERACTIVE_VALIDATION.md](R2_INTERACTIVE_VALIDATION.md).
Native editor UI remains untested and exact Chrome version unverified. R3
inventory/procedure preparation is complete; additional native execution remains
untested because the user confirmed no extra host. See
[R3_NATIVE_PLATFORM_VALIDATION.md](R3_NATIVE_PLATFORM_VALIDATION.md). R4's
[provisional presenter preparation](R4_PRESENTER_RUN_SHEETS.md) and separate
[machine timing checks](R4_DEMONSTRATION_TIMINGS.md) are complete. Agreed teaching
scope/human pacing, matching PDF/package, and publication remain open.
**R5 protected local integration passed** with unchanged upstream and all 13
accepted commits preserved; see [R5_CANDIDATE_VALIDATION.md](R5_CANDIDATE_VALIDATION.md).
Continue in the new candidate worktree named there. R6's provisional
[Markdown document inputs](R6_DOCUMENT_INPUTS.md) are prepared, and the
[literal Ubuntu walkthrough](R6_GUIDE_WALKTHROUGH_VALIDATION.md) has passed.
The [document-review handoff](R6_DOCUMENT_REVIEW_HANDOFF.md) has returned;
[provisional PDFs and companions are verified and integrated](R6_DOCUMENT_REVIEW_RECONCILIATION.md).
R7's [local preview package and builder](R7_PREVIEW_VALIDATION.md) now pass
acceptance and isolated extraction checks. Final classroom editions/approval
remain open, including P3-01 and teaching/platform/pacing decisions; publication
has not been performed or authorized by these local steps.

The original October 30 planning turn executed no readiness gate. The later R1
task performed internal source export, fresh dependency installation, and
validation. R2 later used a separate copy for actual JupyterLab UI execution and
return-workflow checks. R5 subsequently performed the authorized read-only
upstream fetch and protected local candidate preparation. No new student archive,
PDF, push, PR, merge, release, message, or hardware job was performed. The assistant owns technical review,
repairs, packaging, and evidence; no manual user code audit is assigned.
Rick's reply remains pending.

## Source identity and unpublished local inventory

The implementation baseline is `ec073599bb7c87019f957c129e8c6e4d66e9a61c` on
`feat/phys3810-qpe` in the durable integration worktree
`artifacts/local-integration-2026-10-30/worktree` relative to the original repo.
Its recorded baseline is **160 tests, eight notebooks, 50 nonempty code cells,
16 PNGs**. HHL and Shor each require three figures. Runtime/cloud/GPU remain
excluded; supported algorithm inputs and QPE's one/two-target limit are fixed.

At the October 30 planning baseline, local refs showed eight commits ahead
and zero behind cached `origin/main`,
`3894391f2026d4fd9351b346b44b5eda453a17da`, the Grover rc1 source. No remote query
or fetch was performed here. These commits are treated as unpublished from the
local-only session history and cached refs, not a new certification of GitHub's
live state. The old local `main` is stale; do not use it as an integration base.

1. `b16d235ca01ebc9c7f610dcfeb64f081d5d6b453`: documentation and verified Grover
   document-v0.2 PDFs, with receipts; preserves the 50-test Grover code snapshot.
2. `f277e213ea44d0f119add543cabbeceda6e706d8`: protected QFT integration,
   mathematical tests, teaching notebook, and 64-test/five-notebook checkpoint.
3. `e365d38c324444e3558bbd2d175c17c9c54ccf97`: QPE implementation and tests;
   the independently reviewed 92-test/six-notebook snapshot.
4. `695c425374444b3cdf860291b38eedc44682112a`: accepted phase-review follow-ups,
   transfer policy clarification, and 97-test regression baseline.
5. `6ed4d19d219db2eac3f2abccd7f53624c0c9c483`: bounded HHL/Shor design contracts.
6. `234c6084c414664a33b6c5856f22b0aa322325ca`: exact-spectrum HHL, tests,
   notebook, strict validation; 129 tests/seven notebooks.
7. `a85a88aa1fa148b8e64c739444899d5882202973`: compiled full-domain N=15 Shor;
   the independently reviewed 158-test/eight-notebook snapshot.
8. `ec073599bb7c87019f957c129e8c6e4d66e9a61c`: accepted HHL/Shor reconciliation,
   corrected lesson availability, three-figure gates, theoretical Shor recovery
   probabilities, and the current 160-test baseline.

The planning update was committed separately as
`9e73b82aa578f0264afcbf7125631774afa3eb1c` after those eight commits. R1 exported
and validated that exact snapshot; its runtime matches `ec07359`. Later R1
evidence/context updates are separate from the source actually installed/tested.

Subsequent local documentation commits are `6b70fbd` (R1 evidence), `4c589fd`
(R2 UI evidence), and `07831f4` (R3 procedures). R4 timings exported the exact
`07831f4c806d2c4203ea03aa589c31983cbb08de` snapshot; its runtime remains unchanged.
R4 run sheets/evidence form a later documentation-only change, not a new
algorithm or student-package revision. R4 was committed as `0570863`. R5 then
refreshed upstream on October 31 and found `3894391` unchanged. Its separate
candidate preserves all 13 local commit IDs; the complete mapping is in the
[R5 evidence](R5_CANDIDATE_VALIDATION.md). The original integration checkout
remains at `0570863`; R5 documentation is committed only on the candidate branch.

## Completed evidence and its limits

- **Passed locally:** corrected `ec07359`, reused Linux x86_64/glibc 2.43,
  CPython 3.12.15, full required checks, 160 tests/eight fresh-kernel notebooks,
  50 code cells/16 figures. Source outputs remain empty. See
  [the reconciliation](HHL_SHOR_REVIEW_RECONCILIATION.md).
- **Fresh installation passed, October 31:** source `9e73b82`, new isolated
  CPython 3.12.15 environment on Linux x86_64/glibc 2.43; all 114 installed
  application distributions match active pins, plus pip 26.2.2. All 160 tests,
  eight notebooks, 50 cells, and 16 figures passed; 110 exported files/modes
  remain unchanged. This reuses an existing interpreter/OS, not installed
  application packages.
- **Independent review accepted:** QFT/QPE's 92-test snapshot was installed
  freshly on Linux/CPython 3.12.14; the later 158-test HHL/Shor snapshot reused
  that environment. The latter passed all eight notebooks and mathematical
  review. Neither is a fresh install of the corrected 160-test revision.
- **Preserved and verified:** original checkout/index and recovery checkpoint,
  Grover rc1 assets, delivered v0.2 PDFs, and immutable 92-/158-test review ZIPs.
  The previous desktop review copies are absent; retained archives are intact.
- **Interactive JupyterLab passed, October 31:** Chrome with JupyterLab 4.6.4,
  explicit external named-kernel registration pointing at R1, all eight
  notebooks/50 cells/16 figures through UI restart/run-all, save, shutdown,
  relaunch, and preflight/Shor reruns. R1's frozen source/environment remained
  unchanged. Native editor UI is untested; exact browser version is unverified.
- **Not yet executed for the corrected classroom candidate:** native
  Windows/macOS, native editor setup, timed
  classroom rehearsal, new student-package extraction, or remote CI.
- **Not yet supplied:** full-course, version-matched student/instructor PDFs.
  The existing v0.2 documents describe Grover-only rc1 (50 tests/four notebooks).
  They remain valid for that edition, not the new eight-notebook course.

Fresh kernels and a fresh virtual environment are different evidence. Wheel
availability, lock resolution, WSL, or another OS's successful run cannot be
reported as native Windows/macOS execution. No new algorithm review is needed
solely for the already demonstrated P3 corrections.

## Ordered readiness steps and completion criteria

### R1. Fresh Linux installation of the corrected source — passed October 31

Completed for `9e73b82`; [the evidence](R1_FRESH_LINUX_VALIDATION.md) records
actual source/environment paths, installation, checks, and preservation. The
procedure and criteria below remain applicable if later changes require a rerun.

This step can proceed without Rick's reply. Export an identified committed snapshot to a
new local staging directory outside both checkouts and create a new isolated
CPython 3.12 virtual environment, without system site packages. Preserve the
existing classroom/tool environments. This is internal validation staging, not
a replacement student ZIP or new GPT Pro packet; it requires no new PDF yet.

Install with the documented pip version and unchanged requirements/constraints.
Record the exact source commit, OS/architecture/libc, interpreter, installed
versions, and correspondence with active constraints. A fresh virtual environment
on the existing host is not a fresh operating-system installation.

**Done when:** dependency installation and `pip check` pass; all 160 tests and
eight notebooks pass from that isolated source with 50 code cells/16 PNGs;
HHL/Shor each produce three required figures; the original smoke workflow passes;
source/manifest bytes stay unchanged and notebooks stay output-free. Use the
selected new interpreter for tests and kernels, and existing separate maintainer
tools for applicable lint. Retain logs/failure artifacts outside tracked files.
If a dependency repair is needed, scope it explicitly, regenerate evidence,
and reassess review/platform implications; do not quietly upgrade the pins.

### R2. Interactive setup and return workflow — JupyterLab path passed

Completed for the Linux/Chrome path with documented preservation adaptations;
see [the R2 evidence](R2_INTERACTIVE_VALIDATION.md). Native VS Code/Cursor remains
untested, and exact Chrome version could not be inspected under browser policy.
The original criteria below apply to any additional claimed UI/platform path.

Actually launch JupyterLab from the validated environment, select the intended
kernel, open preflight and the course lessons, restart/run all, and inspect
plots/errors. Close and reopen the application and repeat the documented
return-to-work steps. Exercise the intended editor's interpreter/kernel selection
if its workflow will be claimed as supported. An automated nbclient run alone
does not close this step.

**Done when:** the observed UI, interpreter paths, kernel selection, lesson/figure
rendering, restart/run behavior, and reopening steps are recorded against the
snapshot and setup instructions. Record editor/browser versions where used.
Correct instructions that fail. If UI access is unavailable, record **untested**
and the specific unavailable surface; do not substitute headless execution or
assign the user a code audit. Linux setup can progress independently of the
remaining native-platform decisions.

### R3. Native-platform coverage — prepared; additional hosts unavailable

The October 31 inventory found only the existing Ubuntu x86_64 execution host.
The user confirmed no additional native host; exact Windows/macOS procedures
and evidence requirements are prepared in
[R3_NATIVE_PLATFORM_VALIDATION.md](R3_NATIVE_PLATFORM_VALIDATION.md). Their
commands have not been executed on those targets. Existing Linux R1/R2 evidence
remains applicable because runtime/test/notebook/pin bytes are unchanged.

Linux x86_64 is the demonstrated development platform. Windows x64 and macOS
ARM64/Intel are candidate targets in [ENVIRONMENT.md](ENVIRONMENT.md), not passed
platforms. Rick's student/platform feedback determines which are required.
Windows ARM64 and 32-bit Python remain outside the stated target.

**Done for each claimed OS/architecture when:** record OS version/architecture,
use a fresh native Python 3.12 environment, follow the actual setup path, install
unchanged pins, run `pip check` and the full strict validator, and complete R2's
UI workflow. Bash smoke is additional where Bash is supported; the Python
validator remains the cross-platform entry point. Record failures and repairs
per platform. If a host is unavailable, preserve **untested** status; either
obtain execution evidence later or explicitly agree a supported classroom
alternative before final support claims. Do not assume one macOS architecture
covers another or ask students to solve an unvalidated setup during class.

### R4. Teaching decisions and pacing — preparation complete; rehearsal open

The October 31 [presenter index](R4_PRESENTER_RUN_SHEETS.md) links complete
provisional run sheets for all three sessions. Each covers predictions,
transitions, demonstrations, exercises, and debriefs with exact notebook cell
references and 50/75-minute stopping points. A separate local sheet audit
checked mathematical cues, dependencies, and timing arithmetic.

[Machine timing evidence](R4_DEMONSTRATION_TIMINGS.md) records three trials of
each required notebook plus six derived demonstrations: 42 fresh-kernel runs,
all passed. Canonical trials each executed eight notebooks/50 cells/16 PNGs.
The R1 environment was reused, with no source/notebook/test/pin changes.
These seconds do not establish a human rehearsal or confirm the proposed minutes.
No new UI run or 160-test unit-suite run is claimed for this documentation turn.

Pending: session count/dates/duration/deadline, five topics' in-class versus
outside-class coverage, Python/Jupyter/quantum preparation, hands-on versus
demonstration format, delivery responsibility, required platforms, assessment,
and preferred notes/HHL/Shor examples. No answer or new outreach is assumed.
All five tested implementations are available locally; eventual classroom
emphasis does not remove that deliverable.

The current proposal is three 50-minute cores with 75-minute expansions:
Grover; QFT/QPE; HHL/Shor. Session 3 allocates 5 minutes QPE refresher, 20 HHL,
20 Shor, and 5 limitations; expansion adds 15 HHL and 10 Shor minutes.

**Done when:** record the agreed scope, prepare a presenter run sheet, and
rehearse with prediction pauses, notebook transitions, demonstration execution,
and exercise/debrief time. Record segment timings and revisions. The assistant
can prepare materials and time executable demonstrations; that alone is not
human classroom-pacing evidence. Arrange a presenter run-through when available,
without assigning manual code review. Keep all required cells in validation even
if only core discussion fits the session. Resolve solution distribution before
shipping assessed variants; do not invent grading or duplicate notebooks now.

### R5. Protected upstream integration and candidate identity — passed locally

Completed October 31 in a separate durable candidate worktree. The
[evidence](R5_CANDIDATE_VALIDATION.md) records the pre-fetch recovery bundle and
restoration check, unchanged upstream, identity commit mapping, required Python
3.12 checks, preserved bytes, and earlier-evidence assessment. The
[publication draft](CLASSROOM_PUBLICATION_DRAFT.md) supplies a provisional
full-course identity and concrete PR/release description without publishing.
Both prior checkouts/indexes remain intact. Teaching/platform/PDF/package and
publication gates remain open; this is not a classroom-ready declaration.

The procedure below applies again if later upstream changes require integration.
Before freezing publication inputs, preserve this accepted history and recovery
material, then refresh upstream during a separately authorized integration task.
Inspect changes since cached `3894391`; do not assume it is still current.
If reconciliation is needed, use a new durable worktree/branch, retaining the
original checkout/index and reviewed commits. Record old-to-new commit mapping
and rerun affected/full required checks after integration. Reassess any earlier
platform/UI evidence against upstream changes; repeat affected native or
interactive checks rather than carrying an invalidated result forward.

Proposed ordered review groups are documentation/PDFs (`b16d235`), QFT/QPE with
its reconciliation (`f277e21`, `e365d38`, `695c425`), then HHL/Shor contracts,
implementations, and reconciliation (`6ed4d19`, `234c608`, `a85a88a`, `ec07359`).
Keep each proposed change coherent and link-complete. The final reconciliation
links earlier notebooks to later lessons, so do not detach it from those lessons.
Readiness documentation belongs after the full chain, not in the initial
Grover-only documentation group. Grouping is a plan, not PR creation authority.

**Done when:** the resulting local candidate has a clean worktree, exact source
identity, unchanged verified assets, updated acceptance evidence, and a concrete
publication description. Choose a distinct full-course candidate version/name;
check availability before publication. Do not reuse the Grover rc1 tag or
pretend a 92-/158-test review ZIP contains the 160-test corrections.

### R6. Matching student and instructor PDFs — review drafts integrated; final gate open

Provisional [student setup](handouts/FULL_COURSE_SETUP_DRAFT.md) and
[instructor](instructor/FULL_COURSE_INSTRUCTOR_DRAFT.md) companions are prepared
as document-v0.1 drafts for proposed code-v0.2.0-rc1. The returned four-page
student and six-page instructor PDFs and synchronized companions are now
[verified and integrated](R6_DOCUMENT_REVIEW_RECONCILIATION.md) without changing
PDF bytes. The reviewer reports fresh 160/eight/50/16 execution and rendered/
visual/OCR QA; local receipt, metadata, page, link, font, rendered-page, and
normalized text checks passed. The
[input/readiness record](R6_DOCUMENT_INPUTS.md) distinguishes available evidence,
open decisions, file-transfer requirements, and later PDF review. Student text
contains no maintainer coordination or instructor key; worked notebook outputs
and assertions still need an explicit assessment/solution-distribution decision.

The later [literal student-guide walkthrough](R6_GUIDE_WALKTHROUGH_VALIDATION.md)
passed on the accessible Ubuntu host using an isolated source copy and new
in-project `.venv`, unchanged pins, and ordinary `--sys-prefix` kernel registration.
It passed 160 tests/eight notebooks/50 cells/16 PNGs and actual UI execution of
all eight notebooks, plus shutdown/reopen reruns. This new evidence closes the
ordinary Linux route gap left by R2's preservation-adapted external kernelspec;
it does not retroactively change R2's method. Task-local settings and manual
browser opening are disclosed. No future download, other platform/editor,
automatic browser launch, or classroom pacing is certified by this result.

Keep open decisions visible and use demonstrated setup claims; do not turn
proposed dates, scope, assessment, or delivery into agreements. Final classroom
PDFs and R6 completion require stabilized inputs and the existing ChatGPT
review/delivery workflow. A separately requested review-draft handoff may retain
explicit provisional assumptions without closing missing gates. Supplied review
drafts are now integrated; no PDF was generated locally and no new student
package was created in this reconciliation. Apply the P3-01 phase-register
clarification in the next authored instructor edition before final distribution.

Prepare synchronized Markdown companions using the agreed teaching scope,
validated setup/platform claims, candidate version, notebook list, and current
validation counts. Student instructions should omit maintainer coordination and
internal review jargon; keep instructor answers separate when assessment needs it.

**Done when:** ChatGPT supplies the matching PDFs after rendering, visual review,
and OCR checks, and the delivered bytes are accessible locally. Verify exact
full-file hashes/sizes including provenance, page counts, metadata, links, and
placement under `handouts/` versus `instructor/`. Resolve receipt discrepancies
before distribution. Do not rewrite or strip supplied bytes, and do not regenerate
the existing v0.2 Grover PDFs. New document editions and code versions remain
separate identities. A planned download URL must be labeled as such until live;
verify it after publication. Avoid a PDF containing its enclosing ZIP's checksum,
which would create a circular artifact identity.

This provisional document/teaching sync is received and reconciled. No immediate
repeat review is needed for the verified unchanged bytes. A later authored-PDF
update should incorporate P3-01 and the relevant instructor/platform/pacing
feedback before a final classroom edition. Substantive scope/environment changes
still require appropriate evidence and review; do not infer new authorization.

### R7. New full-course package and extraction verification — local preview passed

The [scoped builder](R7_PREVIEW_PACKAGE.md) and
[unpublished preview](R7_PREVIEW_VALIDATION.md) are complete. Source `135d5d0`
produced 47 files with 46 manifest entries and 37 exact committed payload files,
including the verified student PDF unchanged. Instructor answer guides/PDFs are
excluded. Twenty builder acceptance cases, actual reproducibility, independent
payload audit, and isolated 160/eight/50/16 validation passed in the reused R6
environment. All delivered file hashes/modes and ZIP bytes remained unchanged.

This closes the authorized local-preview packaging task, not final classroom
or public-release gates. P3-01, teacher decisions, native/editor coverage, human
pacing, and final document wording remain open. Final release inputs must be
reassessed when source, guide, or approved teaching/support claims change.
The procedure below applies to each later candidate or final package.

Build a new exact-revision package only after its source/version/setup inputs
are fixed. A student-release candidate requires the matching supplied guide;
an internal source export or technical review bundle is a distinct artifact.
Refresh the export inventory and expected counts from **160**, not the old
92-/158-test builder constants. Include every required test/helper and all eight
notebooks; manifest every delivered payload file and record adaptations.

Exclude prompts, policies/chat records, unrelated history, duplicate exports,
Git metadata, generated outputs, caches, environments, credentials, and student
information. Keep instructor answer documents outside a student-only package.
For a future GPT Pro handoff, use one standalone desktop ZIP and a separate
copyable chat prompt, following [WORKFLOW.md](WORKFLOW.md).

**Done when:** unpack the sealed final archive outside both checkouts, verify its
manifest, paths, exclusions, local links, output-free sources, imports, and exact
version/count claims; run the full validator using the intended environment.
Record fresh versus reused installation accurately. Require all 160 tests,
eight notebooks, 50 cells, and 16 PNGs unless a separately documented change
legitimately changes the baseline. Compare payload hashes after execution.
Any edit to payload/setup/PDFs requires a new sealed archive and affected
verification. Preserve the original reviewed ZIPs and Grover release unchanged.

### R8. Readiness proposal next; publication remains unauthorized

Next prepare only a read-only/local readiness audit and concrete publication
proposal: verify then-current upstream, tag availability, repository rules and
required checks, source/package correspondence, and unresolved guide/teaching/
support gates. No such remote audit was performed during R7. Do not push, create
a PR, merge, tag, release, send messages, or submit hardware jobs as part of this
proposed next step.

Prepare the complete candidate/evidence before requesting external publication
authority. Verify the then-current repository rules and required checks without
changing rulesets or the solo-maintainer policy. Local workflow contexts currently
include `local-smoke`, `ruff`, `markdownlint`, `yamllint`, `actionlint`,
`shellcheck`, `dependency-review`, `Analyze (python)`, and `Analyze (actions)`.
This local inventory is not a live ruleset check; a conditional/skipped job is
not a pass. Existing Ubuntu CI is not Windows/macOS evidence.

**Done only after separate authorization:** push/open the scoped PRs, satisfy
actual required checks and resolve findings, merge through the normal workflow,
and identify the resulting source revision. If merging changes the revision,
rebuild/revalidate the final package from it and confirm guide/version consistency
before tagging/releasing. Publish under the new candidate identity, retaining
Grover rc1 and its original assets. Anonymously download the final assets, verify
hashes/manifests/links and release/tag targets, and retain publication receipts.
No earlier Grover authorization covers this new release or instructor outreach.

## Preservation and status reporting

Keep the original recovery bundle, staged/unstaged patches, untracked archive,
raw index, and restored-file/mode evidence at
`artifacts/local-integration-2026-10-30/recovery` in the original repository.
Never reset, clean, stash, or switch that dirty checkout as a cleanup shortcut.
The verified student/instructor v0.2 full-file hashes remain recorded in
[handouts/README.md](handouts/README.md); the Grover release receipt is in
[PREVIEW_PLAN.md](PREVIEW_PLAN.md). Retain both earlier review archives unchanged.

For every step record source identity, environment/platform, exact command or UI
action, artifact location, outcome, and limitations. Use **passed**, **failed**,
**skipped with reason**, or **untested** literally. The original planning turn closed no gate. R1 is now closed by the separately
recorded fresh-install execution, not by prose changes. Later documentation
checks cover Markdown, relative links, Git scope, and preserved bytes; they
do not substitute for executing another gate.

**Recommended next task:** prepare the R8 read-only/local readiness audit and
publication proposal described above. Preserve the verified local preview,
recheck current external state only when that next task is authorized, and
identify exact remaining decisions or material changes before any publication.
Keep preview status distinct from final classroom readiness. **GPT Pro sync:
not needed solely for unchanged-byte packaging.** The next authored PDF edition
must address P3-01 and any agreed teaching/publication wording changes; prepare
that concrete request when its inputs are ready.
