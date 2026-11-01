# Provisional presenter run sheet: session 2, QFT and QPE

October 31, 2026. **Proposed 50-minute core, extended to 75 minutes by adding
25 minutes.** This is presenter preparation, not a completed human rehearsal or
a confirmed teaching assignment. Rick's dates, meeting length, topic emphasis,
student preparation, assessment, and presenter role remain pending. Do not treat
these exercises as graded work or distribute instructor answers as an assessed
student variant before those decisions are made.

Use [the presenter index](../R4_PRESENTER_RUN_SHEETS.md) and
[demonstration timing evidence](../R4_DEMONSTRATION_TIMINGS.md) alongside this
sheet. Measured machine execution belongs in that evidence, not in the teaching
allocations below. A quickly executing cell still needs prediction, explanation,
interaction, and interpretation time. Alternative-input exercises are not timed
merely because their defaults were measured.

## Preparation and exact notebook route

Open [QFT](../notebooks/02_qft.ipynb) and [QPE](../notebooks/03_qpe.ipynb) as separate
notebook tabs with the validated Python environment. Keep their kernels/states
separate: each uses names such as `size`, `figure`, and `counts`. Confirm the
printed interpreter path, CPython 3.12, and Qiskit 2.6.1. The local path needs no
IBM account or hardware. Student installation is preclass work, not a hidden
segment inside this session.

Before presenting, run every code cell in both notebooks from fresh kernels:
QFT has seven nonempty code cells; QPE has eight. Retain errors if a check fails.
Use copies for any parameter changes or saved execution outputs. For live delivery,
restart and clear outputs, then run the dependencies and demonstrations in order
only after each relevant prediction. Do not use skip tags to make a validation
run fit the lesson outline.

Default parameters and sampling:

- QFT: `num_qubits=3`, `basis_label="011"`; positive Fourier exponent, swaps
  enabled. The inverse-gradient sample uses 256 shots, seed 2026.
- QPE: three counting bits, `exact_phase=3/8`, target prepared as |1>; exact
  sampling uses 2048 shots, seed 2026.
- Expansion: `nonexact_phase=1/3`, `precision_bits=(3,5)`; 2048 shots for each
  precision, seed 2026. Keep these defaults for the measured demonstration route.

Cell IDs below are the stable IDs inside the actual notebooks. Displayed
execution counts change when a cell is rerun; they are not cell identifiers.

- **QFT dependencies:** `qft-locate-source`, then `qft-imports-parameters`.
  Main chain: `qft-matrix-and-circuit` → `qft-phase-pattern-figure` →
  `qft-inverse-and-known-gradient`.
- **QFT preclass/follow-up references:** `qft-complex-state-check`, then
  `qft-swap-convention-check`, after the main chain. These are outside the
  scheduled 20-minute QFT introduction, but remain required in full validation.
- **QPE dependencies:** `qpe-locate-source`, then `qpe-imports-helpers`.
  Main chain: `qpe-exact-example` → `qpe-exact-sampling`.
- **QPE references:** `qpe-sdk-reference` depends on the exact-example variables;
  `qpe-invalid-input-demo` depends on imports/helpers. They run in preclass
  validation. Detailed SDK implementation and rejection-code reading are not
  additional uncounted teaching segments.
- **QPE expansion:** `qpe-nonexact-distributions` → `qpe-precision-report`.
  The report depends on the distributions cell; rerun both after changing
  expansion parameters.

## 50-minute core: consecutive teaching blocks

### 0-5: phase and bit-order refresher

Open QFT's `qft-conventions`. Ask learners to explain what squared magnitudes
lose about a complex state, then decode `011` and its reversal `110` before
running the two dependency cells. Check the selected basis label and interpreter.

**Presenter response:** `011` is integer 3, with qubit 0 on the right; `110` is
6. Equal probabilities do not imply equal relative phases. Keep a simple
three-bit count register drawn on the board for the rest of the session.

**Checkpoint:** a learner can identify the least-significant bit and distinguish
an amplitude from its probability. Use the remaining time in this block to repair
that distinction before showing a circuit.

### 5-10: connect the Fourier matrix to the circuit

Use `qft-matrix-explanation`. Before executing `qft-matrix-and-circuit`, ask for
the first amplitude of F|3> and the phase angle at output index 1. Then show the
circuit and its complete-matrix comparison.

**Presenter response:** the first amplitude is 1/sqrt(8); the next phase is
+3*pi/4. Point to H gates, controlled phase rotations, and the final swaps.
The positive sign defines this forward transform; the inverse has the conjugate
negative sign. The independent matrix check fixes the convention; the SDK
`QFTGate` check is additional evidence.

**Debrief:** a correct-looking circuit or a forward/inverse round trip alone
would not establish the intended sign. No gate-by-gate decomposition exercise
is added to this five-minute block.

### 10-15: predict a phase pattern with uniform probabilities

Use `qft-phase-pattern-explanation`. Before `qft-phase-pattern-figure`, predict
whether the lower probability panel distinguishes `011` from `001`. Execute the
default cell, then ask pairs to explain the upper and lower panels in one sentence.

**Presenter response:** all eight probabilities are 1/8, but the relative phases
change with the input label. A counts-only comparison cannot detect the Fourier
sign. The `001` variation can remain a paper prediction here; a live rerun is a
substitution within this block, not extra time. If used, change the parameter
cell and rerun the main chain in order, then restore defaults before proceeding.

**Checkpoint:** learners state which information the histogram hides without
calling the two output states identical.

### 15-20: recover a known phase gradient and transition to QPE

Use `qft-inverse-explanation`. Ask which string inverse QFT should return and
what `110` instead of `011` would signal. Run `qft-inverse-and-known-gradient`.
Use `qft-core-exit` questions within this block, then switch notebook tabs at
minute 20.

**Presenter response:** the exact default output is `011`, including all 256
samples. The gradient preparation used the already-known integer 3, so this
example has not estimated an unknown phase. Say: “Now replace that known-angle
preparation with controlled powers acting on an eigenstate.”

**Transition check:** do not carry QFT variables into QPE. Select QPE's own
kernel and execute its dependency cells during the next block.

### 20-25: establish the QPE input promise and register roles

Open `qpe-register-contract`, then run `qpe-locate-source` and
`qpe-imports-helpers`. Ask where the estimate will live, which state the caller
must prepare, and whether the helper supplies an eigenstate automatically.

**Presenter response:** count precedes target; the caller prepares the target.
The example uses |1> as a known eigenstate of P(2*pi*phi). The canonical helper
accepts one or two target qubits and one through six counting bits. A target
superposition can give several phase outcomes; it is not an automatic error.

**Checkpoint:** students identify count versus target and explain why target
preparation is an assumption/cost rather than a free algorithm step.

### 25-30: create the phase gradient and choose the inverse transform

Continue the same register explanation. Have learners match count qubits 0, 1,
and 2 to U, U^2, and U^4. Predict the sign of the final Fourier operation before
showing the exact-example circuit in the next block.

**Presenter response:** controlled powers create counting amplitudes with
positive phase exp(2*pi*i*x*phi). The inverse of the established positive QFT,
with swaps, converts the interference pattern into the label. Read only count;
full statevectors are ordered target tensor count.

**Transition:** leave the exact-example outputs hidden. Read
`qpe-exact-prediction` and collect the default label prediction first.

### 30-35: predict and inspect the asymmetric exact example

For phi=3/8 and three counting bits, collect the predicted label, then run
`qpe-exact-example`. Inspect the controlled-power circuit and exact-state check.

**Presenter response:** y=3 gives `011`. Its reversal would mean 6/8, so this
case exposes a bit-order mistake. The circuit itself remains unmeasured; the
next cell measures a copy. Ask what would change if the same phase were not on
the chosen counting grid.

### 35-40: sample and reconcile the measurement label

Before `qpe-exact-sampling`, predict which bars can appear for the ideal exact
input. Run it and compare the observed label with y/8. Allow a brief learner
explanation of why the output label is deterministic here despite sampling.

**Presenter response:** all 2048 shots are `011` for this exact supported input.
Count[j] maps to classical bit j, and `int(bits,2)/2**m` needs no reversal.
This exact example does not imply deterministic output for arbitrary phases.

### 40-45: exercise the bit convention with two new exact phases

Ask for labels for 1/8 and 6/8 before changing `exact_phase`. In the working
copy, rerun `qpe-exact-example` followed by `qpe-exact-sampling` for each selected
variation. Keep target preparation at |1>. Restore 3/8 and rerun the pair before
leaving the block if the default will be used in the final explanation.

**Presenter responses:** 1/8 → `001`; 6/8 → `110`. Have a learner decode the
reversed strings numerically to show why visual symmetry is a poor test.
If the group needs more discussion, execute one variation and use the other
as a paper prediction within the same five minutes.

### 45-50: debrief, SDK convention, and exit check

Use `qpe-readout-and-sdk` and `qpe-wrapup`. Ask learners to identify the estimate
register, decode `011`, and name one assumption that would matter for an
application. Explain the pinned SDK comparison without changing the canonical
rule: Qiskit 2.6.1's raw `phase_estimation()` output includes an extra counting
reversal. For the default, raw SDK label `110` is explicitly reversed for the
comparison with canonical `011`.

`qpe-sdk-reference` is already covered in preclass validation. If showing its
output live, run it after the restored exact-example variables and keep its
explanation within this block. Never silently reverse canonical samples.

**Exit responses:** resolution is 2^-m; phase is modulo one; global phase on U
becomes relative under control and cannot be discarded. An eigenphase is not
a Hamiltonian eigenvalue until evolution sign, time/scaling, wrapping, prepared
state, and register roles are specified. HHL/Shor are available later examples,
not evidence that these assumptions disappear.

At minute 50, finish the core. The following blocks are the explicitly added
25 minutes for a 75-minute session.

## 75-minute route: append the 25-minute expansion

### 50-55: predict a nonexact outcome before revealing the plot

Use `qpe-nonexact-expansion`. Ask whether 1/3 can be represented by three binary
fraction bits, then identify nearby grid points. Predict whether all samples
must select the nearest point. Keep `nonexact_phase=1/3` and widths (3,5).

**Presenter response:** 1/3 is off both finite binary grids; expect a distribution.
The nearest three-bit estimate is 3/8, not a promise for every sample.

### 55-65: demonstrate two precisions and interpret the distribution

Run `qpe-nonexact-distributions` after predictions. Compare sampled bars with
independent probability markers and the vertical phase line. Give pairs a short
exercise: find each peak, then explain why low-probability distant bins do not
necessarily indicate a simulator fault. Debrief before leaving this block.

**Presenter response:** the peaks are `011` at 3/8 for m=3 and `01011` at 11/32
for m=5. The cell checks exact amplitudes/probabilities and seeded finite samples;
printed agreement is backed by assertions. Avoid equating more counting bits
with certainty that every individual result improves.

### 65-70: precision report and bounded resource accounting

Predict the change in grid spacing and naive repeated-U count, then run
`qpe-precision-report`. Compare the circular error for the two peak estimates.

**Presenter response:** grid spacing changes from 1/8 to 1/32; peak errors here
are 1/24 and 1/96. There are m controlled-power blocks, corresponding to
2^m-1 repeated U uses in naive query accounting: 7 versus 31. This source
forms small dense powers classically; those numbers are not a measured hardware
execution count or a scalability result.

### 70-75: wrap-around exercise and final synthesis

Ask learners to predict how a phase near one, such as 0.97, relates to zero
under circular distance. A paper prediction is sufficient; if chosen as a live
substitution, change the expansion parameter and rerun both expansion cells,
then compare the observed peak with the prediction. Do not add a new notebook
implementation or widen the declared input family.

**Presenter response:** zero can be the closest coarse-grid estimate because
phase is modulo one; five bits offer a finer grid. End with one statement each
about phase information, bit ordering, and resource limits. Controlled unitaries,
state preparation, synthesis, and readout all have costs; no general quantum
advantage or free eigenstate preparation is established.

## Overrun, failure, and evidence notes

Protect the core's 20-minute QFT → 30-minute QPE boundary and final debrief.
When discussion runs long, reduce live parameter repetitions or retain one
expansion exercise as a stated later option; do not squeeze the 75-minute route
into 50 minutes or claim omitted expansion discussion occurred. The QFT complex/
no-swaps exercises remain additional follow-up, not a third expansion hidden
inside this schedule. Their code still executes in every full validation run.

If setup, a cell, or an assertion fails, retain the traceback and stop that live
execution claim. Use a clearly identified previously validated executed copy
for explanation only if available, and label it as recorded output; otherwise
continue with the matrix/register reasoning on the board. Do not invent counts,
mark an error passed, or troubleshoot installation through the entire lesson.

Record the actual presenter, start/end times of teaching blocks, prediction and
exercise pauses, transition delays, deviations, and unresolved learner questions
when a real rehearsal occurs. Keep these fields unfilled until observed. Local
notebook timings are separately recorded in the linked evidence; neither those
timings nor this run sheet establish a completed human classroom rehearsal.
