# R4 provisional presenter run sheets

Prepared October 31, 2026. **Three proposed 50-minute cores and 75-minute
expansions are ready for presenter preparation.** These are instructor notes
with answer cues, not a confirmed schedule or assessed student handout.
Updated November 1: the listed class period is **85 minutes, 12:40–2:05 PM**.
Retain the 75-minute content route with 10 minutes of questions/transition and
recovery margin; the 50-minute core remains a fallback. These are proposed
allocations, not a completed rehearsal. The provisional November 16/19/23 dates
and November 19 weekday conflict are recorded in [COURSE_PLAN.md](COURSE_PLAN.md).
Rick's reply remains pending. Final session count/dates, coverage, background,
delivery responsibility, platforms, and assessment remain open.

The assistant checked the mathematics, notebook dependencies, cell references,
and minute totals. Local executable demonstrations were measured separately in
[R4_DEMONSTRATION_TIMINGS.md](R4_DEMONSTRATION_TIMINGS.md). **Human pacing
rehearsal remains untested.** Fast code does not establish that explanations,
prediction pauses, learner work, or transitions fit these proposed budgets.

## Choose the provisional route

1. [Session 1: Grover](instructor/R4_SESSION_1_GROVER.md). Core: readiness and
   notation 0–5, oracle 5–15, diffusion 15–25, small search and sampled outcomes
   25–45, exit/debrief 45–50. Expansion: marked sets/input-contract exercise
   50–65 and overshooting 65–75.
2. [Session 2: QFT/QPE](instructor/R4_SESSION_2_QFT_QPE.md). Core: phase/bit
   order 0–5, Fourier transform 5–20, QPE registers/controlled powers 20–30,
   exact-phase prediction/checks 30–45, output-register debrief 45–50.
   Expansion: nonexact distributions 50–65 and precision/wrap-around 65–75.
3. [Session 3: HHL/Shor](instructor/R4_SESSION_3_HHL_SHOR.md). Core: QPE
   refresher 0–5, HHL 5–25, compiled order finding/factors 25–45, limitations
   45–50. Expansion: scaled/complex HHL inputs 50–65 and successful/unsuccessful
   Shor recovery 65–75. Each core traces a prepared example, with no claim to
   derive general linear solving or scalable modular arithmetic in that time.

Every sheet includes prediction-before-output prompts, actual notebook/cell
transitions, demonstrations, short exercises, answer cues, debriefs, and overrun
or failure handling. Subsegments allocate the proposed minutes explicitly.
The 75-minute route appends 25 minutes to the core; it is not a second 75-minute
lesson. Opening tabs, moving between notebooks, and explaining outputs consume
teaching time inside the stated blocks, even when the machine runs quickly.

## Common preparation and execution discipline

- Follow the existing [setup](SETUP.md), [environment](ENVIRONMENT.md), and
  [R2 UI evidence](R2_INTERACTIVE_VALIDATION.md). Linux/Chrome JupyterLab is the
  observed UI path. Native VS Code/Cursor remains untested; exact Chrome version
  remains unverified. Windows x64 and macOS ARM64/Intel are untested targets
  with [prepared procedures](R3_NATIVE_PLATFORM_VALIDATION.md). Do not turn
  these run sheets into broader platform-support claims.
- Use an execution copy. Verify the actual Python 3.12 interpreter behind the
  selected kernel, restore the documented defaults, and run every required
  notebook before presenting. Keep canonical source notebooks output-free.
  The required baseline remains eight notebooks, 50 nonempty code cells,
  16 PNGs, with all three figures required in each HHL/Shor notebook.
- Use a separate kernel per notebook. Restart and clear displayed outputs
  before prediction prompts. Run imports and prerequisite cells in the sheet's
  order; variable names shared between lessons do not imply shared kernel state.
  After a live parameter change, rerun its downstream calculation and plotting
  cells. Restore defaults in the execution copy before a new presentation.
- Shor's resource diagnostic can run before its expansion cells, as measured
  in the presenter-order check. Other core/reference/expansion choices are
  discussion choices, not validator exclusions. All required nonempty cells
  still execute during strict validation; do not add skip tags or tolerate
  error outputs to make a timed route appear complete.
- Preflight/installation is proposed preparation before the meeting. The
  five-minute readiness block cannot absorb an unmeasured package install or
  solve an unsupported platform. If setup is incomplete, use the presenter's
  demonstrated environment and label that delivery adaptation. Its suitability
  for the class still depends on the instructor's decision.
- Retain an actually executed local copy for diagnosis or fallback. If a live
  run fails, say so; a retained plot can support explanation but does not prove
  the current run passed. Never replace a failed demonstration with an invented
  timing or claim that the learners completed it.
- The answer cues are instructor material. Until assessment and solution
  distribution are agreed, do not create graded variants, move answers into a
  student package, or assume an exercise is homework or a submitted assessment.

## Separate evidence categories

**Prepared and checked:** three complete run sheets, mathematical answer cues,
all 67 distinct per-sheet notebook cell references (17/25/25), dependency order,
continuous 0–75-minute heading intervals, and the 50-minute stopping points.

**Executed locally:** three fresh-kernel trials of each of the eight unchanged
required notebooks and six derived demonstration cases, for 42 runs total.
The [timing record](R4_DEMONSTRATION_TIMINGS.md) identifies exact inputs,
source identity, wall/cell timing definitions, versions, and limitations.
These are headless machine measurements, not a new UI run or fresh installation.

**Untested:** a human presenter delivering either route with actual spoken
explanations and prediction pauses; learner exercise completion and questions;
projector/readability/accessibility in the intended room; interactive latency
of these particular parameter changes; the unavailable native platforms and
native editor UI. Prior R2 figure inspection remains separate evidence.

**Pending decisions:** final session count/dates, scope, preparation,
teaching role, delivery format, platforms, assessment/solution policy, and
preferred examples. No email reply or agreement has been inferred.

## Presenter rehearsal receipt — blank until a real run occurs

Use one receipt per actual session/route. Do not prefill measured durations
with the proposed minute budgets or machine timings.

- Session and route (50-minute fallback or 75-minute content plus 10-minute
  margin within the 85-minute period): pending.
- Date, presenter, source commit, run-sheet revision: pending.
- Actual host, interpreter/kernel, UI/browser/editor, room/display: pending.
- Audience/background assumption and whether learners were present: pending.
- For each sheet segment: proposed start/end, actual start/end, prediction
  pause, transition delay, demonstration wait, exercise/debrief duration,
  interruptions, and whether the exit question was answered: pending.
- Live parameters, outputs inspected, execution errors, skipped discussion,
  or retained-output fallback actually used: pending.
- Actual total duration and unmet learning goals: pending.
- Concrete revisions and which segments require another rehearsal: pending.

A solo presenter rehearsal can establish that presenter's delivery time; it
does not establish learner completion time. Record that distinction. R4 closes
only when the agreed scope and relevant real rehearsal evidence satisfy
[RELEASE_READINESS_PLAN.md](RELEASE_READINESS_PLAN.md), with revisions recorded.

## Next workflow step

Keep these routes provisional while awaiting instructor feedback and an actual
presenter run-through. R5 integration and the provisional publication are
[complete](PUBLIC_PREVIEW_RELEASE.md); do not restart them from this historical
run sheet. Select the agreed route before a full rehearsal. A voluntary solo
rehearsal of a reusable Grover segment can inform presenter timing now, but does
not establish class pacing or learner completion time. No new timed execution
is needed solely for this scheduling update.

GPT Pro sync is not needed for this documentation update. The
[November audit](NOVEMBER_REVIEW_RECONCILIATION.md) is the current review;
reopen it for material new requirements or an evidenced defect.
