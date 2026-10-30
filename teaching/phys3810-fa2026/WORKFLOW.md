# PHYS 3810 implementation workflow

Updated October 29, 2026. This is maintainer guidance; the student entry point
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
corrections. The next module is QFT; a versioned Grover-only preview is being
prepared separately for instructor feedback.
See [GROVER_VALIDATION.md](GROVER_VALIDATION.md). The handoff uses a standalone
desktop ZIP and a separate copyable prompt in the chat response.
Work remains on `feat/phys3810-m1-onboarding`, based on
`fb41ae02f2ece3e093e60c9286ef72ae91686530`, with local uncommitted changes.
The supplied audit commit is 12 commits ahead of this base. Preserve all local
work and newer upstream fixes when preparing eventual integration.

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

Routine implementation choices, review, and reversible local fixes stay with
the assistant. The existing local-only boundary remains: publishing, pushing,
opening a PR, merging, messaging other people, and hardware jobs are separate
actions requiring authorization that covers them. Do not repeatedly request
authorization already given for an action.

The Grover preview's push/PR, required-check merge, and prerelease publication
were authorized on October 29, 2026. Complete that scoped workflow without
another permission round. This authorization does not cover unrelated releases,
instructor messages, or hardware jobs.

## Ordered work and completion checks

1. **Milestone-1 review — completed.** The received review's required M1-01
   correction and optional O1/O2 improvements are recorded with evidence.
   Required cells cannot pass through skipped code or allowed errors. Remote
   artifact-upload behavior still requires future CI execution; that disclosed
   limitation does not block local Grover development.
2. **Grover module and lab — reviewed, corrected, preview preparation.** Files are `src/phys3810/grover.py`,
   `tests/test_grover.py`, and `notebooks/01_grover.ipynb` under this course
   directory. State supported small inputs and bit order; test phase-oracle
   action on all basis states and analytic amplification probabilities,
   including zero iterations and overshooting. Compare with `grover_operator()`.
   Add notebook explanation/exercises and register fresh-kernel execution in
   the classroom validator; update its unfinished-lesson reporting.
   [GROVER_PLAN.md](GROVER_PLAN.md) fixes the initial input contract and analytic
   fixtures before implementation.
3. **QFT module and lab.** Test the full complex operator against the Fourier
   matrix with declared sign and swap/bit conventions. Compare with `QFTGate`,
   exercise inversion, and execute the teaching notebook from a fresh kernel.
4. **QPE module and lab.** Build on tested QFT conventions; compare with
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
7. **Preview now; final teaching release later.** Prepare setup/instructor review
   PDFs and a versioned Grover preview before all modules are complete. Follow
   [PREVIEW_PLAN.md](PREVIEW_PLAN.md), preserving the normal PR/check workflow
   and the local-only authorization boundary. Then validate the claimed native platforms and
   interactive kernel instructions, render and inspect the short linked setup
   PDF, test the final archive, and rehearse 50/75-minute delivery. Reconcile
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
  was reproduced and corrected with five new regressions. No further GPT Pro
  round is required solely for those demonstrated repairs.
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

## User input, when available

Only the instructor/user can confirm session dates, student preparation,
assessment expectations, and which native platforms must be supported. Ask
for these together when their answers change implementation. Until then, use
the documented 50-minute cores and optional 75-minute expansions with small,
local, credential-free examples. Do not invent dates or a grading scheme.
