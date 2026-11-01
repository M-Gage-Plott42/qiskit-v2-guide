# Provisional presenter run sheet: session 1, Grover

October 31, 2026. **Instructor preparation, not a completed human pacing
rehearsal.** The proposed 50-minute core and 75-minute expanded session below
include explanation, prediction pauses, transitions, exercises, and debriefs.
The clock allocations are planning estimates; measured code execution belongs
in [the separate timing record](../R4_DEMONSTRATION_TIMINGS.md).

Rick's dates, number of visits, in-class topic coverage, student preparation,
hands-on versus demonstration format, assessment, and presenter assignment
remain unresolved. This sheet assigns no grading or delivery commitment.
Keep these answer cues separate from any later assessed student edition.
See [the presenter index](../R4_PRESENTER_RUN_SHEETS.md) and
[the readiness plan](../RELEASE_READINESS_PLAN.md) for shared boundaries.

## Materials and preparation

Use [preflight](../notebooks/00_setup_preflight.ipynb), then
[Grover](../notebooks/01_grover.ipynb). Cell numbers below are one-based positions
in the current notebooks; IDs are the stable references for matching cells.
The Grover notebook has 20 cells, nine executable, and three figures.

Before the proposed session, the assistant/presenter verifies the selected
Python 3.12 environment and runs the complete required validation on the exact
snapshot. All nine Grover code cells, including expansion cells, must execute.
Use disposable execution copies; keep canonical notebooks output-free. During
class, restart and clear outputs, then reveal each result only after a prediction.
Do not expose the collapsed answer panel before the exit discussion.

Prepare a board or slide with amplitude versus probability, rightmost-bit
ordering, and an eight-entry amplitude row. Expected prerequisite knowledge is
complex amplitudes, squared-magnitude probabilities, and H/X/CX gates; check
this assumption with the group rather than treating it as confirmed preparation.
No live package installation or general oracle coding is budgeted into the core.

The known environment evidence is Linux; native Windows/macOS and native editor
UI remain untested. Hands-on participation is conditional on working preflight.
A student without a working kernel can make paper predictions and follow the
presenter's demonstrated result; that fallback does not certify their setup.

## Proposed 50-minute core

### 00-05 — readiness, purpose, and bit-order prediction

- **00-02, readiness:** refer to the already completed preflight. If a quick
  version check is useful, run preflight cell 2, `versions`; the interpreter
  must be the intended environment. A red traceback stops any pass claim.
- **02-03, transition:** open the Grover tab, select the same intended environment
  for its own kernel, and restart/clear outputs. State the goal: convert a
  relative phase distinction into a larger marked-outcome probability.
- **03-05, predict then establish helpers:** ask for the amplitude-vector index
  and set bits of `011` before showing the result. Run Grover cells 3-4,
  `grover-path-setup` and `grover-imports`, in order. These define imports and
  analysis helpers required by subsequent demonstrations.

**Instructor cue:** `011` has index 3, with qubits 1 and 0 set; qubit 0 is the
rightmost displayed bit. A circuit's top wire is qubit 0. Do not reverse the
bitstring to index a statevector. **Checkpoint:** a learner can distinguish
wire placement, displayed labels, and vector indices.

### 05-15 — oracle: relative sign without a probability gain

Use section 2, `grover-oracle-explanation`, and cell 6,
`grover-oracle-check`. Keep the following output hidden until predictions are
recorded.

- **05-08, prediction:** with eight equal positive amplitudes and marked label
  `001`, ask which amplitude changes and whether immediate measurement becomes
  more likely to return that label. Let pairs justify the probability claim.
- **08-11, demonstration:** run `grover-oracle-check`; point to the one negative
  entry in the oracle diagonal and the unchanged eight probabilities.
- **11-15, debrief/exercise:** ask learners to write the sign pattern for target
  `110` on paper. They should change the marked index, not the probability
  distribution. Return explicitly to the live default `001` for diffusion.

**Instructor cue:** only `001` changes sign; every probability remains 1/8.
An oracle marks phase, not an extra answer register. Relative phase can affect
later interference even when a direct measurement cannot distinguish it.
**Transition:** ask what operation could use the sign information before a
measurement destroys the coherent state.

### 15-25 — diffusion: predict a reflection about the mean

Use section 3 and cell 8, `grover-diffusion-check`, after cell 6 has created
`after_oracle` and `uniform`.

- **15-19, board prediction:** let `a=1/sqrt(8)`. Seven entries are `a`, one is
  `-a`, so the mean is `3a/4`. Ask students to apply `2*mean - amplitude` to
  both kinds of entry before running the cell.
- **19-22, demonstration:** run `grover-diffusion-check`; compare the printed
  marked amplitude before the oracle, after the oracle, and after diffusion.
- **22-25, debrief:** have learners name the order of operations and explain
  why an intermediate measurement would change this experiment.

**Instructor cue:** the marked amplitude becomes `5a/2`, giving probability
25/32; each unmarked amplitude becomes `a/2`. The exact convention is
`D=2|s><s|-I`, and one iteration is `Q=DO`: oracle first, diffusion second.
Uniform preparation occurs once before repeated iterations. **Checkpoint:**
learners explain a probability increase through amplitude interference rather
than saying that the oracle alone found the answer.

### 25-35 — four-candidate prediction and the labeled circuit

Use section 4, `grover-single-target-lab`, then cell 10,
`grover-two-qubit-example`.

- **25-29, prediction/exercise:** give `N=4`, `M=1`, and `theta=pi/6` in
  `P_r=sin^2((2r+1)*theta)`. Ask for `P_0`, `P_1`, and `P_2`; collect the
  prediction for the second iteration now, before any later curve is shown.
- **29-32, demonstration:** run `grover-two-qubit-example` with target `01`.
  Trace the figure's Prepare, Oracle O, and Diffusion D blocks left to right.
- **32-35, debrief:** distinguish the unmeasured circuit from a sampling copy.
  Explain that an expanded diffusion block's overall phase annotation is not
  an extra change to measurement probabilities; relative phase remains essential.

**Instructor cue:** probabilities are 1/4, 1, and 1/4. More iterations are not
monotonically better. The figure uses gates from the canonical implementation,
not a separately coded notebook algorithm. **Transition:** announce the change
from four candidates/target `01` to eight candidates/target `001`.

### 35-45 — eight-candidate exact result and finite-shot sampling

Use Markdown cell 11, `grover-three-qubit-sampling`, and code cell 12,
`grover-sampler-example`. Ask for the prediction before revealing the cell's
stated result or output.

- **35-38, prediction:** for `N=8`, `M=1`, and two iterations, ask whether
  success should be exactly one and whether unmarked bins must be empty.
  Connect the calculation to the same analytic formula.
- **38-41, demonstration:** run `grover-sampler-example`. Compare exact marked
  probability with the sampled fraction and inspect the histogram's label.
- **41-45, debrief/exercise:** ask which claims require the exact statevector
  and which the 2,048-shot histogram can support. Have learners explain why a
  small unmarked count is not automatically a failed implementation.

**Instructor cue:** exact success is `121/128 = 0.9453125`, with expected marked
count 1,936 out of 2,048. Sampling uses seed 2026 and an explicit six-standard-
deviation bound; do not require another machine's exact count dictionary.
The measurement circuit is a copy, leaving `search` unmeasured for exact checks.
**Checkpoint:** learners distinguish exact probability, random frequency,
normalization, and shot accounting.

### 45-50 — core exit check, limits, and handoff

Use `grover-core-exit` (cell 13); keep its answer disclosure closed until the
responses are discussed. Use `grover-limits-and-next` (cell 20) for the limitation
summary without executing expansion code merely to reach that Markdown cell.

- **45-48, exit questions:** why did the oracle leave probabilities unchanged;
  what did diffusion do; why retain an unmeasured circuit; what would a second
  iteration do for the four-candidate example?
- **48-49, limitations:** state that targets are enumerated in this teaching
  oracle, supported widths are 2-5 qubits, and state loading/oracle synthesis/
  readout costs are not included in a query-count slogan. No quantum advantage
  or end-to-end unknown-answer search benchmark was demonstrated.
- **49-50, transition:** summarize the phase-to-interference connection and
  preview QFT/QPE as the next proposed session's phase-pattern/decoding tools.
  Do not promise confirmed session dates or assigned homework.

**Core exit cue:** a sign flip preserves squared magnitudes; diffusion uses
relative phase; measuring midway changes coherence; `N=4,M=1,r=2` gives 1/4.
For a 50-minute meeting, stop the live lesson here. Expansion discussion remains
optional for class time, while its code is still mandatory in preclass validation.

## Proposed 75-minute route: add 25 minutes after the core

### 50-65 — marked sets and a handled input-contract exercise

Return to Grover section 6, `grover-multiple-targets`, code cell 15,
`grover-multiple-target-check`, and cells 16-17,
`grover-input-contract-exercise` / `grover-handled-invalid-input`.

- **50-53, predict:** for `N=8,M=2`, ask for total marked probability after one
  iteration and whether one marked state's probability equals that total.
- **53-58, demonstrate/change one parameter:** run the default pair
  `("001", "011")`. In the disposable working copy, change only
  `multiple_targets` to `("000", "110")`, predict the new occupied indices,
  then rerun that cell. Restore the default pair after the exercise.
- **58-62, input-contract exercise:** predict what duplicated labels could mean
  for phase flips. Run the existing handled duplicate-target demonstration;
  the expected rejection is caught inside a successful cell. Do not insert an
  unhandled exception or mark a required cell skippable.
- **62-65, debrief:** compare total marked probability, individual marked
  probabilities, and label dependence; restate supported-input restrictions.

**Instructor cue:** total marked probability is 1; each of the two selected
labels has probability 1/2. Changing the distinct labels preserves those totals
but moves the populated indices. Duplicates, empty/all-marked sets, wrong widths,
and unsupported qubit counts are rejected instead of silently reinterpreted.

### 65-75 — overshooting and final synthesis

Use section 7, `grover-overrotation`, and cell 19,
`grover-iteration-curve`. The earlier import/helper cells must still be in the
same kernel; only `plot_examples` is an editable exercise input here.

- **65-68, predict:** revisit `P_0,P_1,P_2` for four candidates and sketch an
  oscillation rather than a steadily increasing curve. Ask where the first
  useful peak lies for eight candidates with one marked label.
- **68-72, demonstrate:** run the default curve cell. Match formula lines to
  circuit markers and integer iteration counts. If time permits, change the
  second example to two distinct targets, predict from `M/N`, rerun, and restore
  defaults. No additional qubits or oracle model are introduced.
- **72-75, debrief:** ask why repeated rotations overshoot, why matching `M/N`
  can give matching success curves, and why that does not imply equal physical
  gate costs. Finish with one statement each about phase, amplification, and
  the boundary between a small simulation and an advantage claim.

**Instructor cue:** the default `N=4,M=1` curve peaks at one iteration and falls
at two; the first high `N=8,M=1` probability is near two iterations. With `N=8,M=2`,
`M/N` equals the four-candidate example's marked fraction, so the corresponding
success curves coincide. This does not make their oracle/synthesis costs equal.

## Overrun and failure handling

Protect the oracle-versus-probability distinction, one diffusion prediction,
the exact-versus-sampled comparison, and the final limitations statement. If the
core is running late, shorten optional board variations or group reporting;
move marked-set/curve discussion to the expansion. Do not remove prerequisite
cells, edit the canonical algorithm, change seeds/pins on the spot, or label
unexecuted checks passed. Record the actual segment time and the adaptation for
later rehearsal rather than assuming the proposed slots were met.

If setup/kernel/imports fail, retain the traceback and verify the selected
interpreter/path. Use the prepared board amplitude example or an explicitly
identified earlier executed artifact for discussion only; do not fabricate a
live result or disguise stored output as a new run. Classroom installation
support is outside the five-minute opening. A hand-computed prediction is still
a useful exercise, but it is not new environment or notebook-validation evidence.

The separate [timing report](../R4_DEMONSTRATION_TIMINGS.md) measures local code
execution, not these discussion slots, learner completion, or a human presenter
run-through. Human pacing, final platform support, and Rick's teaching decisions
remain open after this sheet is prepared.
