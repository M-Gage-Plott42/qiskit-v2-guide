# PHYS 3810 implementation workflow

Current integration snapshot, October 30: this local documentation/PDF change
is based on published main `3894391`. The original development checkout and
index have a verified recovery checkpoint and remain intact. QFT code and its
64-test/five-notebook evidence are outside this revision and will follow in a
separate commit. Its runtime remains the published Grover 50-test/four-notebook
scope. Older planning and validation entries below retain their dated context.

Updated October 30, 2026. This is maintainer guidance; the student entry point
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

Current position: milestone 1 and Grover reviews are reconciled after evidenced
corrections. QFT is now locally validated and QPE is next. The versioned
Grover-only preview is published for early feedback from merged commit
`3894391f2026d4fd9351b346b44b5eda453a17da` through PR #112. QFT remains local
and is not part of that prerelease; QPE is the next implementation after the
planned Git integration. The additional published-Grover audit received on
October 30 independently reports 50 tests/four notebooks passing. Its
[reconciliation](GROVER_RELEASE_RECONCILIATION.md) distinguishes that snapshot
from QFT's earlier local validation. The subsequently corrected PDF receipt
matches the delivered bytes; the discrepancy is closed. The
[first instructor review packet](INSTRUCTOR_REVIEW_PLAN.md) is ready for the
user to send. Its review concerns teaching decisions, not another code audit.
See [GROVER_VALIDATION.md](GROVER_VALIDATION.md). The handoff uses a standalone
desktop ZIP and a separate copyable prompt in the chat response.
Work remains on `feat/phys3810-m1-onboarding`, based on
`fb41ae02f2ece3e093e60c9286ef72ae91686530`, with local uncommitted changes.
The published main commit is 13 commits ahead of this base. The index still
contains 28 earlier onboarding paths. Follow [GIT_INTEGRATION_PLAN.md](GIT_INTEGRATION_PLAN.md):
preserve staged, unstaged, and untracked work before using a durable separate
worktree from current main. Git integration is planned, not executed this turn.

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

Execute [GIT_INTEGRATION_PLAN.md](GIT_INTEGRATION_PLAN.md) in the next work turn:
verify a recoverable checkpoint of staged, unstaged, and untracked work; leave
the original checkout/index intact; create a durable worktree from refreshed
main; and prepare separate coherent local commits for documentation/verified
PDFs and the existing QFT implementation. Keep QFT-dependent documentation in
the QFT change so each commit's links and availability claims remain correct.

Completion evidence includes the recovery location and verification, chosen
base and local commit IDs, the new worktree's clean status, exact PDF hashes,
and required Python 3.12 checks. The current development baseline is 64 tests
and five required notebooks. Preserve the published Grover rc1 tag/ZIP/assets
and newer upstream fixes. The next prompt covers local integration only;
QPE implementation and external publication are subsequent actions. Instructor
feedback can proceed in parallel without blocking this preservation work.

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
4. **QPE module and lab — next.** Build on tested QFT conventions; compare with
   `phase_estimation()`. Independently verify asymmetric exact phases and a
   nonexact phase distribution. Test counting-register interpretation, not
   merely a visually plausible histogram.
5. **HHL design, then module/lab.** Before implementation, state the supported
   matrices, input preparation, phase precision, reciprocal rotation, and
   postselection procedure. Use a small, nontrivial example and independently
   check postselection probability, uncomputation, normalization, and relative
   sign against a classical solve. Restrictions belong in student explanations.
6. **Shor design, then module/lab.** State the supported composites and bases;
   implement and test reversible modular arithmetic, order recovery, and
   classical factor extraction separately, including unsuccessful cases.
   Identify any compiled small-instance shortcuts explicitly. Do not use removed
   HHL/Shor imports or imply a general scalable implementation.
7. **Preview published; documentation integration next; final release later.**
   Integrate the ChatGPT-supplied setup/instructor PDF editions using the
   corrected delivered-file receipts. Preserve the original rc1 source and assets. Follow
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
- **Due after QFT/QPE, before HHL/Shor implementation:** review the shared phase
  and bit conventions plus the proposed HHL/Shor restrictions and test contracts.
  This catches conceptual errors before they propagate to the harder modules.
- **Recommended after HHL/Shor and before publication:** evaluate the combined
  mathematical evidence, limitations, setup PDF, and teaching sequence. Do not
  label a release independently reviewed until an actual response is recorded.
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

## Instructor feedback

Use [INSTRUCTOR_REVIEW_PLAN.md](INSTRUCTOR_REVIEW_PLAN.md) for the first packet:
two verified v0.2 PDF attachments and the named unchanged rc1 ZIP link. Explain
that the attached setup guide supersedes the older guide inside the ZIP.
Repository PDF integration/publication can follow separately; a dirty local
checkout does not invalidate the already-published preview.

Ask for dates/durations/deadline, prior preparation/notation, classroom format
and operating systems, algorithm emphasis/depth, and assessment expectations.
The five requested implementations remain deliverables; their in-class coverage
is still a teaching decision. Request feedback on clarity, level, emphasis, and
proposed pacing without requiring installation or manual code review. Keep
private correspondence and message drafts out of public repository documents.
The user sends the email; this planning update does not authorize sending tools.

## User input, when available

Only the instructor/user can confirm session dates, student preparation,
assessment expectations, and which native platforms must be supported. Ask
for these together when their answers change implementation. Until then, use
the documented 50-minute cores and optional 75-minute expansions with small,
local, credential-free examples. Do not invent dates or a grading scheme.
