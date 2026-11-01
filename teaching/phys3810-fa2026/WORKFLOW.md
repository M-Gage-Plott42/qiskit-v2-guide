# PHYS 3810 implementation workflow

Updated October 31, 2026. This is maintainer guidance; the student entry point
remains [README.md](README.md). The assistant owns technical review and tests.
The user supplies teaching decisions and any external reviewer response that
is not accessible in the current workspace.

## Source of truth and current position

The available planning baseline is the supplied GPT Pro milestone brief,
[COURSE_PLAN.md](COURSE_PLAN.md), and the milestone-1 implementation/validation
report. GPT Pro's review of source manifest `06e22d9b5d2a` was received on
October 29, 2026. It found no planning conflict, required one validator fix, and
recommended proceeding to Grover after an evidenced correction without another
approval round. [REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md) records the
subsequent local reproduction, fix, tests, and remaining limitations.

Current position: the independent QFT/QPE review has been received and accepted
with no blocking defects. It executed the immutable 92-test/six-notebook snapshot
in a fresh Linux CPython 3.12.14 environment. Four optional follow-ups are now
locally reconciled with 97 tests/six notebooks. See
[QFT_QPE_REVIEW_RECONCILIATION.md](QFT_QPE_REVIEW_RECONCILIATION.md).
The new local revision is distinguished from the exact ZIP GPT Pro executed.
No additional phase-algorithm implementation or dependency change was needed.

The HHL implementation now follows [HHL_PLAN.md](HHL_PLAN.md), including raw
success/failure amplitudes, exact-spectrum cleanup, and a strictly executed
teaching notebook. See [HHL_VALIDATION.md](HHL_VALIDATION.md) for the executed
checks and limitations. [SHOR_PLAN.md](SHOR_PLAN.md) is now implemented with a
compiled full-domain N=15 example and a separate four-residue-qubit order finder.
QPE stays bounded to one/two targets. The HHL/Shor independent review is
accepted and its D1/O1/O2 follow-ups are reconciled; see
[HHL_SHOR_REVIEW_RECONCILIATION.md](HHL_SHOR_REVIEW_RECONCILIATION.md).
The current suite passes 160 tests and eight notebooks. The original reviewed
158-test ZIP remains unchanged; a later distribution must identify its own revision.
The original checkout/index, PDFs, Grover release, and reviewed phase ZIP remain
intact. The user sent the initial setup/Grover email on October 30 and is awaiting
the instructor's reply; only the setup PDF attachment is confirmed by the
supplied screenshot. See [the instructor review record](INSTRUCTOR_REVIEW_PLAN.md).

Keep responsibilities distinct: the course plan defines deliverables;
`STATUS.md` records current evidence; `VALIDATION.md` records executed checks;
this file defines the collaboration process. A new user instruction can change
the plan. Record the resulting technical decision without publishing private
correspondence. Reviewer suggestions require evaluation against code and tests.

## Every implementation turn

1. Read the current status, relevant plan, Git changes, and any new feedback.
   Name the smallest useful next unit of work and its acceptance criteria.
2. Implement, inspect the diff, run relevant checks, and fix concrete failures.
   Research current primary documentation when an API or assumption needs
   verification. Preserve exact environment pins unless a tested change is
   necessary; do not upgrade dependencies as a routine side effect.
3. Update status and evidence for material changes. Distinguish passed, failed,
   skipped, and untested; keep source notebooks free of outputs. Do not rerun
   the Python suite solely because prose changed.
4. End with a short result, one recommended next action, GPT Pro sync status
   (`due`, `recommended`, or `not needed`) and its reason, plus any input needed
   from the user. Do not replace technical work with a request for manual review.
5. Make the final content of every response a fenced `text` block containing
   the recommended next instruction for the user to paste into this Codex
   conversation. Include the relevant plan, scope, completion checks, and
   authorization boundary. Keep it concise and actionable. Put explanation,
   validation, GPT Pro status, and any needed user input before the block.

This continuation format also applies to planning-only turns. Finish the
current authorized scope before proposing subsequent work; do not stop routine
work merely to obtain the next pasted prompt. A suggested prompt is not an
action already performed or approval already received. When a GPT Pro review
prompt is also needed, identify its recipient separately and keep the final
block reserved for the next instruction to Codex.

Routine implementation choices, review, and reversible local fixes stay with
the assistant. The existing local-only boundary remains: publishing, pushing,
opening a PR, merging, messaging other people, and hardware jobs are separate
actions requiring authorization that covers them. Do not repeatedly request
authorization already given for an action.

The user authorized and the assistant completed the Grover preview's normal
push/PR, required-check merge, and prerelease workflow. Do not request that
authorization again. Other releases, instructor messages, and hardware jobs
still need authorization covering those actions.

## Immediate next technical action

R1 of the [readiness plan](RELEASE_READINESS_PLAN.md) passed on October 31:
source `9e73b82` installed unchanged pins into a fresh isolated Python 3.12.15
environment and passed 160 tests/eight notebooks/50 cells/16 PNGs. See
[R1_FRESH_LINUX_VALIDATION.md](R1_FRESH_LINUX_VALIDATION.md) for paths and receipts.

R2's Linux/Chrome JupyterLab path has now passed through actual UI selection,
restart/run-all, figure inspection, save, shutdown/relaunch, and preflight/Shor
reruns. See [R2_INTERACTIVE_VALIDATION.md](R2_INTERACTIVE_VALIDATION.md).
The frozen R1 export/environment are preserved. Native VS Code/Cursor UI is
untested because native control is unavailable, and exact Chrome version is
unverified after the internal version URL was blocked by browser policy.
Neither limitation is a reason to relabel headless checks as UI evidence.

R3 inventory/procedure preparation is complete. Only the existing Ubuntu host
is accessible, and the user confirmed no additional host. The
[native-platform protocol](R3_NATIVE_PLATFORM_VALIDATION.md) supplies exact
Windows/macOS commands and receipt criteria; those targets remain untested.
Carry forward unchanged Linux evidence rather than rerunning it solely for
procedure preparation. No infrastructure, remote session, or native pass is inferred.

R4 provisional preparation is complete: the [presenter index](R4_PRESENTER_RUN_SHEETS.md)
links three 50-minute core/75-minute expansion run sheets with predictions,
transitions, demonstrations, exercises, and debriefs. The
[timing record](R4_DEMONSTRATION_TIMINGS.md) reports 42 successful fresh-kernel
executions from unchanged source `07831f4`, reusing R1's environment. The 160-test
result remains prior unit-test evidence; it was not rerun for these prose changes.
Human pacing remains untested and Rick's target platforms, dates, scope,
assessment, and delivery role remain open.

R5 protected local integration is complete; see
[R5_CANDIDATE_VALIDATION.md](R5_CANDIDATE_VALIDATION.md). Refreshed upstream is
still `3894391`, so all 13 accepted commits keep their IDs. The accepted
integration checkout stays at `0570863`. Continue in the new durable candidate
`artifacts/local-candidate-2026-10-31/worktree` relative to the original repo,
on `candidate/phys3810-fa2026-v0.2.0-rc1`. Runtime checks reran with 160 tests,
eight notebooks/50 cells/16 PNGs in the reused R1 environment; no source repair,
new installation, or UI check was needed or claimed.

R6 provisional Markdown inputs are now prepared: separate
[student setup](handouts/FULL_COURSE_SETUP_DRAFT.md) and
[instructor companion](instructor/FULL_COURSE_INSTRUCTOR_DRAFT.md), with actual
platform claims, bounded algorithm scope, and explicit pending teaching choices.
[R6_DOCUMENT_INPUTS.md](R6_DOCUMENT_INPUTS.md) records the remaining input and
file-transfer requirements. The [publication draft](CLASSROOM_PUBLICATION_DRAFT.md)
keeps the proposed identity distinct from published Grover.

Next validate the new student guide literally on Ubuntu, using a separate source
copy and fresh environment. Record its exact hash, commands, selected interpreter,
ordinary `.venv`/`--sys-prefix` registration, actual Jupyter UI actions, full
validator results, and instruction repairs. R2's external-kernelspec preservation
adaptation does not establish the literal route. No walkthrough occurred in the
Markdown-only turn. An internal source copy does not validate a future download
or student ZIP. Keep existing environments/staging/checkouts and receipts intact.

Keep audience-specific content separate: the student guide contains setup/help,
not model-review coordination or an instructor key. The current notebooks still
contain worked results; assessment and solution distribution require an actual
decision. Prepare the GPT Pro document/teaching sync when its inputs are ready,
with accessible bytes and the prompt separate from the bundle. A later requested
review draft may retain declared provisional assumptions; final classroom claims
require the relevant teaching/platform/pacing gates. Resume R3 when an actual
authorized host exists, retaining the native-editor gap separately.

For presenter work, always label proposed teaching minutes, measured machine
seconds, actual UI execution, and human rehearsal as distinct evidence. A
scripted walkthrough cannot close the human pacing gate. Record timings against
the exact source, environment, input variants, and execution method; preserve
source notebooks and measure edits only in execution copies. Complete all
required cells during validation even if a live core discusses a subset.

Do not broaden QPE, support nonexact HHL spectra, or claim general Shor arithmetic.
Changes to supported families require a revised contract and appropriate evidence.
Instructor feedback remains pending. Publication, new PDFs, native-platform
claims, and outreach are separate work; the local review packet does not perform
them or replace the published Grover preview.

## Ordered work and completion checks

1. **Milestone-1 review — completed.** The received review's required M1-01
   correction and optional O1/O2 improvements are recorded with evidence.
   Required cells cannot pass through skipped code or allowed errors. Remote
   success-path artifact upload is now observed in published Grover CI; deliberate
   remote failure-path upload remains untested.
2. **Grover module and lab — published and independently retested.** Files are `src/phys3810/grover.py`,
   `tests/test_grover.py`, and `notebooks/01_grover.ipynb` under this course
   directory. State supported small inputs and bit order; test phase-oracle
   action on all basis states and analytic amplification probabilities,
   including zero iterations and overshooting. Compare with `grover_operator()`.
   Add notebook explanation/exercises and register fresh-kernel execution in
   the classroom validator; update its unfinished-lesson reporting.
   [GROVER_PLAN.md](GROVER_PLAN.md) fixes the initial input contract and analytic
   fixtures before implementation.
3. **QFT module and lab — locally validated.** Test the full complex operator against the Fourier
   matrix with declared sign and swap/bit conventions. Compare with `QFTGate`,
   exercise inversion, and execute the teaching notebook from a fresh kernel.
4. **QFT/QPE checkpoint — independently accepted and reconciled.** Build on tested QFT conventions; compare with
   `phase_estimation()`. Independently verify asymmetric exact phases and a
   nonexact phase distribution. Test counting-register interpretation, not
   merely a visually plausible histogram.
5. **HHL independently accepted; follow-ups reconciled.** Follow [HHL_PLAN.md](HHL_PLAN.md),
   which fixes supported matrices, input preparation, phase precision, reciprocal rotation, and
   postselection procedure. Use a small, nontrivial example and independently
   check postselection probability, uncomputation, normalization, and relative
   sign against a classical solve. Restrictions belong in student explanations.
   [HHL_VALIDATION.md](HHL_VALIDATION.md) retains the original local evidence;
   [the combined reconciliation](HHL_SHOR_REVIEW_RECONCILIATION.md) records
   independent acceptance and the current 160-test follow-up.
6. **Shor independently accepted; review follow-ups reconciled.** Follow [SHOR_PLAN.md](SHOR_PLAN.md)
   for the fixed modulus, bases, compiled full-domain model, and failure policy;
   implement and test the declared modular permutations, order recovery, and
   classical factor extraction separately, including unsuccessful cases.
   Identify any compiled small-instance shortcuts explicitly. Do not use removed
   HHL/Shor imports or imply a general scalable implementation.
7. **Preview published; documentation integrated locally; final release later.**
   Follow [RELEASE_READINESS_PLAN.md](RELEASE_READINESS_PLAN.md) for the explicit
   remaining gates. The supplied PDF editions are tracked using corrected
   delivered-file receipts.
   Preserve their bytes and the original rc1 source/assets. Follow
   [PREVIEW_PLAN.md](PREVIEW_PLAN.md), preserving the normal PR/check workflow
   and the local-only authorization boundary. Then validate the claimed native platforms and
   interactive kernel instructions, obtain the matching reviewed PDF from
   ChatGPT, test the final archive, and rehearse 50/75-minute delivery. Reconcile
   newer upstream changes in a protected local integration step, rerun affected
   checks, and prepare the publishable result before seeking publication action.

Each numbered item is an outcome, not a promised one-turn time estimate. Keep
one logical module/milestone per change set. Preserve previous work before
branch/base changes. Do not block Linux implementation while waiting for native
Windows/macOS evidence or unknown scheduling details; keep the corresponding
platform and teaching claims provisional.

## GPT Pro checkpoints

- **Completed:** milestone-1 review was received and its required correction
  was demonstrated locally. The original [request](GPT_PRO_HANDOFF.md) is kept
  as history, with the current outcome in the reconciliation record.
- **Completed after Grover:** review was received; its notebook exercise defect
  was reproduced and corrected with five new regressions. The October 30 audit
  independently reports the final 50-test/four-notebook result. No further
  algorithm review is required solely for those repairs.
- **Completed, PDF delivery receipt:** the corrected v0.2 hashes match both
  existing PDFs. Local prefix hashes reproduce the superseded pre-delivery
  values; appended provenance explains the different full-file hashes.
  [The receipt](handouts/README.md) preserves both records and their disposition.
  No replacement files or further PDF sync are needed.
- **Completed after QFT/QPE:** the unchanged reviewed snapshot passed a fresh
  Linux installation and 92 tests/six notebooks. No blocking defects were found;
  four optional P3 updates were adopted and locally validated with 97 tests.
  Shared phase/bit conventions are resolved. HHL eigenvalue encoding and Shor
  register/oracle scope now have written contracts; HHL is implemented locally
  and Shor is now locally implemented as a separate bounded milestone.
- **Completed after HHL/Shor:** the unchanged 158-test/eight-notebook snapshot
  passed in a reused Linux CPython 3.12.14 environment with no algorithm blocker.
  D1 notebook availability prose and O1/O2 improvements are reconciled locally
  with 160 tests. This closes the technical checkpoint, not native-platform,
  pacing, new-PDF, or publication readiness. No new sync is needed solely for
  these demonstrated small follow-ups.
- **Sync sooner when needed:** conflicting mathematical conclusions, unsupported
  generality/advantage claims, a substantial scope/environment change, or a
  reviewer disagreement that experiments do not resolve.
- **Not needed:** routine lint repairs, small documentation corrections, and
  already-scoped fixes with clear test evidence.

These are project coordination recommendations, not claims that GPT Pro is a
formal verifier. The assistant must never invent an approval or treat silence
as a review. If a due review is unavailable, continue independent preparation
and tell the user precisely which dependent decision remains open.

## Packet and feedback protocol

For each new sync, supply **one standalone runnable ZIP on the Ubuntu desktop**.
Include only the source, notebooks, requirements/constraints, tests and runner,
setup/run instructions, license, and concise technical validation evidence needed
for that milestone. Give the review prompt separately in a copyable fenced code
block in the final chat response. No prompt text or prompt file goes in the ZIP.
An intentional instructional setup PDF may be a preview asset. It is distinct
from generated notebook output; label review drafts and preserve editable source.

**PDF ownership:** ChatGPT authors, renders, visually reviews, OCR-checks, and
supplies PDFs. Codex integrates the supplied bytes, verifies hashes/metadata/
links, maintains Markdown companions, and performs authorized packaging and
publication. Student PDFs belong under `handouts/`; instructor guides belong
separately under `instructor/`. Do not silently regenerate a supplied edition
using the existing maintainer renderer. Record discrepancies before publication;
obtain corrected evidence or files rather than declaring a mismatch a pass.
Hash the entire delivered file, including appended provenance; do not optimize
or strip a supplied PDF. A pre-delivery checksum is not interchangeable with
the delivered-file receipt. Preserve historical failed comparisons and record
the corrected evidence that closes them.

For the QFT/QPE technical review, include version-matched Markdown setup and
concise phase-validation evidence. Exclude the Grover-only PDF editions and
unrelated history/policy documents; do not regenerate PDFs for this handoff.
Retain canonical source, tests, notebooks, dependencies, and technical contracts
byte for byte from the identified commit. Validate the extracted final archive
outside both checkouts and verify the single desktop ZIP's hash. Record any
reused environment. This does not replace the published Grover student ZIP.

Document v0.2 accompanies unchanged Grover code rc1. A later authorized update
may add distinct v0.2 assets and link the documentation commit in release notes.
Do not overwrite the original rc1 tag, ZIP, or PDFs. A refreshed standalone ZIP
requires a new candidate version and a matching ChatGPT-supplied guide.

Exclude agent/policy/chat documents, unrelated historical reports, Git metadata,
duplicate text exports, nested archives, logs, notebook outputs, caches, venvs,
credentials, and student/account data. Bundle-specific setup/orientation prose
may replace repository-wide documents to keep local links usable; label that
adaptation and preserve canonical code/tests/notebooks/dependency files exactly.
Extract the curated ZIP, validate it independently of the Git checkout, and
verify the desktop copy's checksum. Report any reused environment or untested
platform rather than implying a fresh installation. Use a date/digest to
distinguish revisions; do not overwrite earlier packets.

The user transfers the ZIP and chat-provided prompt to the existing GPT Pro planning conversation
and brings the response back if no connected source exposes it. No manual
audit or command execution is expected from the user. The assistant then:

1. Identifies the snapshot the feedback actually reviewed.
2. Records each finding as confirmed, not reproduced, or needing a decision.
3. Implements confirmed fixes and runs affected checks; explains any rejected
   recommendation with evidence rather than silently discarding it.
4. Updates status and technical decisions, and prepares a new packet if changes
   materially invalidate the previous review.

Use explicit source transfer between chats. Official
[OpenAI project-context documentation](https://learn.chatgpt.com/docs/projects)
describes sharing uploaded/connected project sources and keeping durable local
guidance in repository docs. A chat's access to this working tree must be
established, not inferred from use of the same account.

## Access and return-file protocol

At every sync, state the source revision, exact archive/hash, what is actually
available in the current workspace, and what the receiving chat must be given.
Do not equate conversation history, filenames, screenshots, file cards, or a
private `sandbox:` URL with accessible bytes. Inspect local attachments,
explicit downloads, or connected sources before claiming a file was read.
OpenAI's [project documentation](https://learn.chatgpt.com/docs/projects)
distinguishes conversation synchronization from project-file access; this
workflow verifies the actual sources/tools available in each session.

There are two different kinds of return:

1. **Review only, files unchanged:** request a disposition identifying the
   exact input ZIP/manifest and explicitly stating whether files changed.
   That report is sufficient when the reviewed source already exists locally;
   no return ZIP is required. Verify its identity against retained bytes and
   distinguish reviewer-reported execution from new local reproduction.
2. **Changed/new files, patches, or generated artifacts:** request a real
   downloadable ZIP or applicable patch, with base revision, relative paths,
   actual delivered-file sizes/SHA-256 values, and a concise change summary.
   State that the files must be attached in this conversation or downloaded to
   an accessible local path. Private sandbox references or screenshots alone
   are not delivery. Do not claim those changes are integrated before reading
   and verifying the actual returned bytes. PDF receipts must cover delivered
   bytes including provenance, not only pre-delivery originals.

Every future outgoing GPT Pro prompt should explicitly ask it to say whether
it changed files and which of these return formats applies. If it only supplies
private links, explain exactly what is missing; continue independent local work
that does not depend on those files. Do not make the user assemble evidence or
perform a manual code audit. If reviewer probe scripts were not returned,
label any local reproduction as an equivalent case unless exact inputs are known.

For each new outgoing snapshot, refresh the canonical-file inventory, tests,
and expected counts. Do not reuse an older export whitelist unchecked. In
particular, the reconciled phase suite now includes `tests/test_qft_notebook.py`
and 97 tests; the preserved 33-file review ZIP remains the earlier 92-test snapshot.

For the received QFT/QPE review, all eight referenced files already exist
locally and in the retained archive. GPT Pro reported all 33 exported files
unchanged. Its private sandbox paths are not mounted here, but no changed-file
transfer is needed for this review. The report and verified snapshot suffice.

## Instructor feedback

The user sent the initial setup/Grover email on October 30 and is awaiting a
reply. Use [INSTRUCTOR_REVIEW_PLAN.md](INSTRUCTOR_REVIEW_PLAN.md) to distinguish
the confirmed setup attachment from the full recommended packet. The two
verified v0.2 guides and unchanged rc1 ZIP remain available; do not assume
additional delivery or repeat the initial send recommendation as unfinished work.

Requested decisions include session coverage, prior preparation, format,
assessment, teaching responsibility, and preferred notes/examples. Dates,
durations, deadlines, and required native platforms also remain open. The five
requested implementations remain deliverables; in-class coverage is a separate
teaching decision. Record a later reply's technical/teaching conclusions without
publishing private correspondence, email screenshots, or addresses. No reply,
follow-up message, or outreach schedule is assumed, and sending tools remain
outside the local authorization. Instructor feedback does not replace assistant
technical review or require manual code audit by the user.

## User input, when available

Only the instructor/user can confirm session dates, student preparation,
assessment expectations, and which native platforms must be supported. Ask
for these together when their answers change implementation. Until then, use
the documented 50-minute cores and optional 75-minute expansions with small,
local, credential-free examples. Do not invent dates or a grading scheme.

## Combined HHL/Shor technical packet

Use exact committed bytes for source, tests, notebooks, dependencies, license,
and validation runners. Include all earlier regression dependencies. Adapt
setup, course orientation, and concise evidence to the eight-notebook snapshot.
To exclude unrelated review history and avoid broken links, technical-plan
exports may replace repository navigation/status headers and coordination tails;
retain the complete mathematical/API/acceptance sections byte for byte. Record
these adaptations and verify retained sections against their committed sources.
Do not change a supported-input contract as an export convenience. This limited
navigation adaptation applies to the combined packet; the earlier immutable
QFT/QPE ZIP is unchanged. No policy documents or historical chat records belong
in the bundle.

Verify the manifest, exclusions, links, and output-free sources; execute the
extracted final ZIP outside both checkouts using CPython 3.12. Label a reused
environment honestly. Provide the exact ZIP hash and a separate prompt requesting
either an unchanged-snapshot review report or actual delivered patch/ZIP bytes
for changes. Keep the last response block for the next instruction back to Codex.

## Received HHL/Shor review

The report explicitly changed no files and identifies the verified 44-file ZIP,
so no replacement archive or patch is required. The retained archive is readable;
the former desktop copy is currently absent and was not silently recreated.
Extra reviewer probe scripts were not delivered: distinguish equivalent local
probes from exact reruns. The reviewer verified supplied mathematical sections;
comparison with pre-adaptation source is separately recorded local evidence.
Preserve the old ZIP and label all later packets with their own revision/counts.
The D1 correction belongs in any new distribution; do not present the unchanged
review archive as though it contains that correction.

## Planning versus readiness execution

The eight-commit inventory is anchored to `ec07359` and cached `origin/main`;
it is not a live upstream or ruleset audit. Keep new planning-only commits
separate in the evidence. Do not repeat completed integration/review work or
rewrite historical archives to hide the corrected revision. A fresh source
export and environment for R1 are internal validation, distinct from a student
release candidate that requires a new version and matching supplied guide.
Application tests need not be rerun for prose-only planning changes; verify
Markdown, links, scope, and preservation, and retain the actual prior execution
identity. No plan entry itself grants push/PR/merge/publication authority.
