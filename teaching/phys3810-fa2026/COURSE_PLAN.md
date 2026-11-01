# PHYS 3810 · Fall 2026 course plan

Invited lecture/lab sessions for UTC **Introduction to Quantum Information
Science and Technology**. Updated November 1, 2026: the listed class period is
**12:40–2:05 PM (85 minutes)**. Three visits remain the provisional planning
basis; neither additional meetings nor the distribution of five topics is agreed.
The bounded implementations and provisional preview are complete; see
[the publication receipt](PUBLIC_PREVIEW_RELEASE.md) and
[the current audit reconciliation](NOVEMBER_REVIEW_RECONCILIATION.md).

## Requested deliverables

Rick Mukherjee requested a brief, linked PDF covering Python environment
creation and Qiskit installation in basic steps, plus working, tested,
commented code for **Grover's algorithm, QFT, QPE, HHL, and Shor's algorithm**.
Students will use this public repository. Downloading a release archive must
be sufficient; Git knowledge, IBM accounts, credentials, and QPUs are not
prerequisites.

Milestone 1 supplied a draft setup guide for validation. The verified Grover v0.2
setup/instructor PDFs remain historical review editions; final classroom editions
follow platform validation and instructor feedback. Grover has since
been implemented as milestone 2, followed by QFT, QPE, and the bounded HHL
lesson and compiled N=15 Shor example. See
[STATUS.md](STATUS.md) for current validation and review state.

## Scheduling and preparation

The supplied course listing resolves the class length at 85 minutes and lists
Monday/Wednesday meetings. An earlier scheduling proposal names **November 16,
19, and 23, 2026**, retained as provisional dates. Calendar arithmetic gives
Monday, Thursday, and Monday respectively: **November 19 conflicts with the
regular Monday/Wednesday pattern**. Confirm whether it is an intended special
meeting or a date correction; do not silently substitute November 18.
No confirmed topic-to-date assignment or additional class date is recorded.

UTC has no classes **November 25–29, 2026**; **November 30, 2026** is the last
class day. These constraints were checked against the
[official UTC academic calendar](https://www.utc.edu/academic-affairs/registrar/calendars-and-schedules/academic-calendar-fall-2026-summer-2027)
on October 29, 2026. They do not establish dates for the invited sessions.

The user sent the initial setup/Grover email on October 30; the instructor's
reply is pending. Questions include the number of sessions and in-class topics,
student Python/Jupyter preparation, format and assessment, teaching responsibility,
and preferred notes/examples. See [the instructor review record](INSTRUCTOR_REVIEW_PLAN.md).
The earlier three-topic proposal covered QFT, Shor, and Grover; the later
deliverables also include QPE and HHL. Confirm whether the additions belong
inside the three visits, in extra meetings, or outside class. Keep the existing
three-session grouping as one option rather than an instructor-approved route.

Confirm with the instructor before finalizing lesson depth and exercises:

- Confirm the provisional dates, especially November 19, number of visits,
  teaching responsibility, and complete-materials deadline. The listed 85-minute
  period is resolved; do not keep asking for its duration without new evidence.
- Students' Python/Jupyter experience, hands-on versus demonstration format,
  personal computers versus a managed lab, required operating systems, and
  installation restrictions.
- Prior coverage of complex vectors, tensor products, eigenvalues, phase,
  measurement, and circuit notation.
- Relevant lecture notes/textbook and notation or examples to follow.
- Whether all five algorithms require treatment during the three visits or
  some are supporting resources for the wider course. Five tested, commented
  implementations remain required regardless of classroom emphasis.
- Whether small, fully explained simulator examples meet the HHL/Shor goals,
  and whether particular matrices or factoring examples are expected.
- Assessment expectations: participation, submitted notebooks, graded problems,
  collaboration policy, and accommodations.
  Clarify when solutions should be shared before preparing assessed variants.

Proposed preparation is the setup/preflight notebook before session 1. Until
background is known, include short refreshers and provide runnable examples
alongside optional exercises. No grading scheme is assumed. The
[first instructor review packet](INSTRUCTOR_REVIEW_PLAN.md) can establish these
teaching decisions without asking the instructor to install or audit the code.

## Proposed sessions

The [R4 presenter run sheets](R4_PRESENTER_RUN_SHEETS.md) now expand this outline
into predictions, notebook transitions, demonstrations, exercises, debriefs,
and fallback choices. Their 50-minute cores and 75-minute expanded content
routes remain provisional. Within the known 85-minute period, reserve the
remaining **10 minutes for questions, recovery, and transition margin** instead
of adding more content automatically. This 75+10 allocation is a planning
option, not measured human pacing. The 50-minute core remains a fallback.
[Local demonstration timings](R4_DEMONSTRATION_TIMINGS.md) were measured
separately; no human pacing rehearsal or instructor agreement is claimed.

### 1. Grover: phase oracles and amplitude amplification

**50-minute core:** 5 minutes to confirm preflight and notation; 10 minutes on
phase marking and the oracle contract; 10 minutes on the diffusion operation;
20 minutes to inspect a small search circuit and compare its probabilities
with the analytic result; 5 minutes for a prediction/check discussion.

**75-minute expansion:** add 15 minutes to vary the marked state or marked set
and 10 minutes to examine too many iterations. Students should explain why
success probability oscillates and distinguish oracle cost from query count.

### 2. QFT and QPE: extracting phase

**50-minute core:** 5 minutes reviewing complex phase and bit order; 15 minutes
connecting QFT to the Fourier matrix; 10 minutes on controlled powers and
inverse QFT in QPE; 15 minutes predicting and checking exact phase examples;
5 minutes interpreting the output register.

**75-minute expansion:** add 15 minutes on a nonexact phase and its distribution
and 10 minutes varying precision. Use asymmetric exact phases so reversing bits
changes the answer. Students should connect resolution to counting qubits.

### 3. HHL and Shor: applications and limits

**50-minute core:** 5 minutes recalling QPE; 20 minutes tracing a small HHL
example, its postselection, and normalized solution state; 20 minutes tracing
small-instance Shor order finding through classical factor extraction;
5 minutes discussing assumptions and resource costs. The chosen HHL design is
an exact-spectrum 2x2 demonstration; Shor uses compiled full-domain N=15
permutations with four residue qubits. Each core traces one prepared example,
not construction of a general solver or arithmetic network from scratch.

**75-minute expansion:** add 15 minutes comparing HHL with a classical solve,
including relative sign and uncomputation, and 10 minutes exploring successful
and unsuccessful order/factor recovery. These are restricted instructional
examples; explain state preparation, readout, and arithmetic costs explicitly.

## Milestones and acceptance criteria

1. **Scope, environment, onboarding — review correction completed.** Inventory the
   existing repository; record the actual base and audit relationship; provide
   the course landing page, plan, status, setup draft, and preflight notebook.
   Resolve an exact Python 3.12 dependency environment with visualization and
   notebook support. Retain smoke checks, add assertions and an offline `.env`
   test, and execute classroom notebooks in fresh kernels. Record actual
   installed versions, results, and platform limitations. Prepare independent
   review before implementing algorithms. The assistant handles technical
   review and remediation using [WORKFLOW.md](WORKFLOW.md); the user is not
   expected to inspect the diff or run tests manually.
2. **Grover lesson — published and independently retested.** Follow
   [the explicit input and test contract](GROVER_PLAN.md).
   Add commented canonical source, notebook explanation and
   exercises, and independent tests of basis-state oracle action and analytic
   amplification probabilities. Check SDK reference agreement and fresh-kernel
   execution in the supported environment.
   The rc1 preview is published. The corrected v0.2 delivery receipts now match
   the existing PDFs, which are already integrated unchanged;
   see [the release audit](GROVER_RELEASE_RECONCILIATION.md). Further publication
   remains a separately authorized action through the normal repository workflow.
3. **QFT/QPE independently accepted; optional follow-ups reconciled.** Compare the QFT operator with the full Fourier matrix;
   test QPE on asymmetric exact phases and a nonexact phase distribution.
   Document sign/bit conventions and verify SDK references and fresh kernels.
4. **HHL/Shor independently accepted; review follow-ups reconciled.** Follow
   [HHL_PLAN.md](HHL_PLAN.md) for fixed positive evolution, exact eigenphases,
   reciprocal rotations, postselection, and count cleanup. Follow
   [SHOR_PLAN.md](SHOR_PLAN.md) for the explicitly compiled N=15 model,
   full four-bit reversible action, verified order recovery, and factor failure
   cases. HHL source, tests, notebook, and strict validation are recorded in
   [HHL_VALIDATION.md](HHL_VALIDATION.md); Shor and the complete 158-test,
   eight-notebook suite are in [SHOR_VALIDATION.md](SHOR_VALIDATION.md).
   The QPE target-width limit remains unchanged. The
   [reconciliation](HHL_SHOR_REVIEW_RECONCILIATION.md) records acceptance, the
   notebook status correction, and two optional improvements; current validation
   passes 160 tests and eight notebooks. Technical implementation/review is complete.
5. **Provisional preview published; final classroom readiness remains open.** Follow the staged
   [readiness plan](RELEASE_READINESS_PLAN.md). R1 fresh Linux installation has
   [passed](R1_FRESH_LINUX_VALIDATION.md); the
   [Linux JupyterLab path](R2_INTERACTIVE_VALIDATION.md) also passed. Native
   editor/platform and pacing checks remain open. The
   [R3 procedures](R3_NATIVE_PLATFORM_VALIDATION.md) are prepared, with additional
   native execution pending host access. R4's provisional presenter run sheets
   and local demonstration measurements are prepared; agreed teaching scope
   and human pacing rehearsal remain open while Rick's reply is pending.
   [R5 protected integration](R5_CANDIDATE_VALIDATION.md) is complete in a
   separate candidate worktree; upstream was unchanged and required checks
   passed again. The [R6 Markdown inputs](R6_DOCUMENT_INPUTS.md) are now
   prepared with separate student/instructor audiences. The
   [Ubuntu command/UI walkthrough](R6_GUIDE_WALKTHROUGH_VALIDATION.md) has passed
   in isolation. Its [provisional document-review handoff](R6_DOCUMENT_REVIEW_HANDOFF.md)
   has returned and its [review-draft PDFs are verified](R6_DOCUMENT_REVIEW_RECONCILIATION.md).
   [R7 local preview packaging](R7_PREVIEW_VALIDATION.md) now passes its
   acceptance/extraction checks. R8 and the separately authorized publication
   are complete; [v0.2.0-rc1 is published](PUBLIC_PREVIEW_RELEASE.md).
   New full-course document-v0.2 review editions are reconciled separately from
   the frozen release's v0.1 documents. Teaching decisions, human pacing, unavailable platforms/editor paths,
   and final classroom editions remain open;
   Grover and full-course document/code identities remain distinct.
   Validate setup instructions on the claimed classroom
   platforms, obtain the matching ChatGPT-reviewed PDF, rehearse the timed
   sessions, and check every notebook from a downloaded archive. Record any
   intentionally unsupported platforms and unresolved teaching decisions.
   Any further publication requires separate authorization; do not repeat the
   completed readiness or release sequence.

Use current SDK circuits and V2 primitives. Canonical reusable implementations
live in `src/phys3810/`, tests in `tests/`, and teaching notebooks in this
directory's `notebooks/`. See [AGENTS.md](../../AGENTS.md) for validation and
public-artifact conventions, and [STATUS.md](STATUS.md) for observed progress.
Maintainer coordination, per-turn recommendations, and GPT Pro checkpoints are
recorded in [WORKFLOW.md](WORKFLOW.md).

Historical planning update, October 30: Git integration is complete and QPE is locally
validated under [QPE_PLAN.md](QPE_PLAN.md). The original checkout remains
preserved under [GIT_INTEGRATION_PLAN.md](GIT_INTEGRATION_PLAN.md).
The review's October 30-November 2 feedback window and November 2-6 QFT/QPE
target are provisional planning targets, not confirmed sessions or commitments.
QFT/QPE review is accepted; HHL/Shor are now locally validated under their
written contracts, and the combined independent review is accepted. Freeze each
session's materials at least one
week before its confirmed date, after platform checks and a pacing rehearsal;
final dates, preparation, platform, and assessment decisions remain open.
The November 1 scheduling evidence above supersedes the earlier unknown duration.
