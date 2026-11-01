# Session 3 presenter run sheet: HHL and compiled Shor

October 31, 2026. **Provisional instructor notes, with answer cues.** The proposed
50-minute core and 75-minute expanded session trace prepared bounded examples.
They are not measured human teaching times or a completed pacing rehearsal.
Rick's dates, number of sessions, in-class coverage, student background,
assessment, and delivery responsibility remain unconfirmed.

Use the [run-sheet index](../R4_PRESENTER_RUN_SHEETS.md),
[demonstration timing evidence](../R4_DEMONSTRATION_TIMINGS.md), and
[course plan](../COURSE_PLAN.md). Machine execution measurements do not reserve
or replace the prediction, discussion, transition, or exercise time below.

## Presenter preparation and dependency map

Open [HHL](../notebooks/04_hhl.ipynb) and
[Shor](../notebooks/05_shor.ipynb) in separate notebook tabs/kernels. Verify the
selected interpreter, not just its display label. Use an execution copy; retain
output-free source notebooks. Before class, execute the strict validator and
all cells of both notebooks, including expansion/reference checks. Retain real
executed artifacts for diagnosis or a clearly labeled fallback demonstration.
Before presenting, restart and clear the displayed outputs so answers do not
precede predictions. Run dependent cells in the orders below; do not transfer
variables between the two kernels.

- **HHL setup:** `hhl-locate-source`, then `hhl-imports-helpers`. These locate
  canonical source and define the readout helpers. They reveal no default
  numerical solution. The default parameter cell is
  `hhl-parameters-circuit`, followed by `hhl-raw-state-checks`,
  `hhl-state-comparison`, then `hhl-postselected-sampling`. These are the live
  core sequence. `hhl-invalid-input-demo` is a handled reference check; it is
  independent of the current parameter choice once imports are present.
- **Shor setup:** `shor-locate-source`, then `shor-imports-helpers`. The live
  core sequence is `shor-parameters-circuit`, `shor-joint-checks`, and
  `shor-sampling-recovery`. `shor-expansion-batches` depends on that core's
  `trial` and chosen width. `shor-classical-failures` uses imported helpers.
  `shor-resource-diagnostic` depends on the core `circuit`/`expected_joint`,
  not on the expansion batches, so it can support the final core debrief.
- Notebook cell IDs above identify the actual source cells. The HHL notebook's
  internal minute labels start at HHL minute zero, after this session's initial
  five-minute refresher. Shor's labels similarly start when its 20-minute block
  begins; do not add their clocks to the session twice.

Defaults to restore before class: HHL `matrix_entries=[[1.5,0.5],[0.5,1.5]]`,
`rhs_amplitudes=[1,0]`; Shor `base=2`, `num_counting_qubits=4`. HHL uses 4096
shots per X/Y/Z basis and seed 2026. Shor uses 2048 shots per selected base,
seed 2026, with no automatic retry. Counts may fluctuate; assess the stated
assertions and tolerances, not equality to a remembered histogram.

Prerequisites to check, without assuming Rick has covered them: complex vectors,
eigenvectors/eigenvalues, normalization, tensor/register order, measurement,
phase kickback, inverse QFT, modular multiplication, and greatest common divisors.
Prepare a board sketch of the HHL register roles and a small modular orbit.
This session does not derive a general solver or arithmetic network from scratch.

## 50-minute core

### 0-5 minutes: reconnect QPE to the applications

- **0-1:** State the two outcomes: a postselected solution state for HHL, and
  order information followed by classical GCDs for Shor. Name the bounded scope.
- **1-3, prediction:** Ask what the bitstring `011` means with three counting
  bits. Then ask whether phase 3/8 automatically means an eigenvalue of 3.
- **3-4, debrief cue:** The phase is 3/8 with the established direct integer
  decoding; energy/eigenvalue decoding additionally needs sign, time/scale,
  wrapping interval, and register roles. HHL deliberately fixes those choices.
- **4-5, transition:** Select the HHL tab, confirm its kernel, and run its two
  setup cells. State that the printed path/version is an environment check,
  not the algorithm's result. Read `hhl-register-contract` before its parameter
  cell; keep later answer output off screen.

### 5-10 minutes: HHL labels and reciprocal rotation

- **5-7, prediction:** Show A0 and its eigenvalues 1 and 2. Ask for the three-bit
  labels, which eigencomponent gets the larger flag-1 amplitude, whether count
  clears on failure too, and whether the success flag should disappear.
- **7-9, demonstration:** Run `hhl-parameters-circuit`. Trace preparation of b,
  QPE, reciprocal rotation, and inverse of that same QPE block in the circuit.
  Point to count qubits 0-2, system 3, success 4; the tensor order is success,
  system, count. Do not invert preparation of b.
- **9-10, debrief cue:** `U=exp(+i*pi*A/4)` makes phase lambda/8 and integer
  label y=lambda: labels are `001` and `010`. Rotation amplitude is 1/y, so the
  lambda=1 component is weighted more strongly. Both count branches clear to
  `000`; the flag remains as the postselection result. This requires the exact
  supported spectrum, not arbitrary finite-precision phases.

### 10-17 minutes: raw branches before normalization

- **10-12, exercise:** Read `hhl-postselection-prediction`; have learners solve
  A0 x=(1,0) on paper or explain the sign of the second component. Ask which
  vector's norm determines the success probability.
- **12-15, demonstration:** Run `hhl-raw-state-checks`, then
  `hhl-state-comparison`. Read raw amplitudes and probability before the
  normalized answer. Inspect failure, count leakage, and the real/imaginary
  amplitude panels; these checks do more than compare basis probabilities.
- **15-17, debrief cue:** Raw success is (3/4,-1/4), giving probability 5/8.
  The normalized successful state is (3,-1)/sqrt(10). Raw failure is
  (sqrt(3)/4,sqrt(3)/4), with probability 3/8. Classical `solve(A,b)` is the
  independent reference, not the circuit's preparation shortcut. A system
  marginal without conditioning on the flag is not generally this solution.

### 17-25 minutes: postselection, relative sign, and handoff

- **17-19, prediction:** Ask why Z counts cannot distinguish (3,-1) from (3,1),
  and predict conditional X/Z expectations. Read `hhl-measurement-prediction`.
- **19-22, demonstration:** Run `hhl-postselected-sampling`. Explain matching
  system/flag bits from the **same shot**, then keeping flag=1 shots. Inspect
  the selected counts, conditional means, and three-observable figure.
- **22-24, debrief cue:** For the default solution, X=-3/5, Y=0, Z=4/5. The
  negative X detects the relative sign. Conditional uncertainty uses selected
  shots, not the total 4096. Empty selection means an undefined conditioned
  estimate, not a zero expectation or a fabricated success.
- **24-25, transition:** State that HHL has returned a conditional state, not
  a list of all classical solution entries. Switch to the Shor tab and its own
  kernel; run `shor-locate-source` and `shor-imports-helpers`. Do not let Shor's
  `circuit` variable be confused with HHL's circuit in another kernel.

### 25-30 minutes: Shor orbit and full residue register

- **25-27, prediction/exercise:** Starting at 1, ask learners to list repeated
  multiplication by 2 modulo 15 and its first return to 1. Ask why four residue
  qubits are retained when the visible orbit contains only four values.
- **27-29, demonstration:** Read `shor-register-contract`; run
  `shor-parameters-circuit`. Trace residue preparation `0001`, count Hadamards,
  controlled constants, and inverse QFT with swaps.
- **29-30, debrief cue:** The orbit is 1,2,4,8 and order is 4. The displayed
  constants are 2,4,1,1; identity constants are omitted by their computed values.
  The gate nevertheless defines all 16 residue states, fixing both 0 and 15
  with +1 phase. Four residue qubits are distinct from the four default count
  qubits. The one/two-target QPE helper has not been widened.

### 30-37 minutes: predict and check Shor phase bins

- **30-32, prediction:** Read `shor-phase-prediction`. Request the four-bit
  phase labels and probabilities before revealing `shor-joint-checks` output.
- **32-35, demonstration:** Run `shor-joint-checks`. Explain that its independent
  modular/Fourier sum checks the complete complex residue/count state, not only
  a plausible histogram. The tensor order here is residue, count.
- **35-37, debrief cue:** `0000`, `0100`, `1000`, and `1100` each have probability
  1/4. Decode the displayed strings directly, without reversal. The prepared
  residue is a superposition of multiplier eigenstates; the counting outcomes
  form a phase distribution. Exact dyadic orders in this
  fixed N=15 family explain these peaks; four count bits are not a universal
  precision guarantee for factoring arbitrary integers.

### 37-45 minutes: recover only justified orders, then factors

- **37-39, prediction/exercise:** Read `shor-recovery-prediction`. Give the
  outcomes `0000`, `0100`, `1000`, `1100`; ask which exact reduced denominators
  can be certified as the true order. Ask whether every nonzero result suffices.
- **39-42, demonstration:** Run `shor-sampling-recovery`. Read the row for each
  sampled string, distinguish the order and factor columns, and compare the
  empirical counts with the displayed theoretical per-shot probabilities.
- **42-45, debrief cue:** Quarter phases certify order 4 and factors (3,5);
  zero is inconclusive, and 1/2's denominator 2 is not base 2's period. The
  conservative routine does not guess a multiple. With r=4, x=2^2 mod15=4,
  so gcd(3,15)=3 and gcd(5,15)=5. The theoretical per-shot probabilities are
  1/2 for order recovery and 1/2 for factors; a finite batch is not a guarantee.

### 45-50 minutes: limitations and core exit debrief

- **45-47:** Run `shor-resource-diagnostic` if its actual display is useful;
  it uses the existing core state. Explain the declared `u`/`cx` basis, seed,
  optimization level, and lack of hardware connectivity constraints. Refer to
  `hhl-limitations` and `shor-resources`; do not equate a short high-level drawing
  or machine runtime with scalable resource cost.
- **47-49, exit exercise:** Ask for one sentence explaining HHL's success flag
  and one explaining why a Shor order may fail to give factors. Ask each learner
  to name an assumption/cost omitted by an unsupported speedup claim.
- **49-50, debrief/close:** HHL is exact-spectrum 2x2, with dense evolution,
  compiled reciprocal lookup, preparation, and postselection. Shor is compiled
  full-domain N=15, with dense gates, exact small orders, readout, and classical
  recovery. Neither establishes general solver/factoring advantage. End here
  for the 50-minute version. If 75 minutes is selected, explicitly return to
  the HHL tab for the next block.

## 75-minute version: append 25 minutes

The preceding 0-50 clock remains intact. These blocks add 15 HHL minutes and
10 Shor minutes, including the tab transitions and final debrief.

### 50-65 minutes: HHL input/scale/phase exercises

- **50-51:** Return to HHL. Confirm that its kernel still contains its setup
  definitions and restore the default parameters in the execution copy.
- **51-55, prediction then demonstration:** Predict the effect of doubling A0
  with b=(1,0). Set `matrix_entries=[[3,1],[1,3]]`; rerun
  `hhl-parameters-circuit` and every subsequent code cell in order. The direction
  stays (3,-1)/sqrt(10), while success drops to 5/32 because C remains 1.
- **55-60, prediction then demonstration:** Restore A0 and set
  `rhs_amplitudes=[1/np.sqrt(2),1j/np.sqrt(2)]`. Rerun the same dependent sequence.
  Expected successful state is (3-i,-1+3i)/sqrt(20), probability 5/8, and
  X/Y/Z=(-3/5,4/5,0). Ask which measurement exposes complex relative phase.
- **60-63, paired exercise/debrief:** Use `hhl-expansion` to predict the |+>
  and |-> cases before viewing its reference answers. Success probabilities
  are 1/4 and 1; the prepared eigenstate is retained. Never normalize a zero
  failure branch. Learners can explain these cases on paper; additional live
  parameter runs are optional discussion choices, not validation omissions.
- **63-65:** Use `hhl-invalid-input-demo` as the handled rejection example:
  off-grid and aliased-at-eight spectra are rejected. Restore defaults in the
  execution copy and switch back to Shor. Do not normalize an invalid b or
  rescale a different matrix silently to make it fit the lesson.

### 65-75 minutes: separate order and factor failures

- **65-68, prediction/exercise:** Read the questions in
  `shor-expansion-prediction` before revealing its explanatory paragraph.
  Predict outcomes for bases 11 and 14, and take the GCDs explicitly. If the
  Shor kernel was restarted, rerun its setup and core cells before expansion.
- **68-71, demonstration:** Run `shor-expansion-batches`. It adds exactly one
  2048-shot batch for base 11 and one for 14. Together with the default core,
  this is three batches/6144 shots, with no automatic retry loop. Inspect the
  theory markers and both success metrics.
- **71-73, debrief cue:** Each base has theoretical order-recovery probability
  1/2. Base 11 yields x=11, with gcd(10,15)=5 and gcd(12,15)=3, so factor success
  is 1/2. Base 14 yields x=14=-1 mod15, hence trivial GCDs and factor probability
  zero even when order 2 is recovered.
- **73-75, reference checks and final debrief:** Run `shor-classical-failures`.
  Base 2's `0010` gives a nonminimal period and stays inconclusive. Base 1 has
  no useful phase; a noncoprime base such as 6 can succeed in the **separate
  classical** GCD precheck and is rejected by the quantum builder. Ask learners
  to classify zero phase, missing order information, and trivial square-root
  factor failure. Restore the default Shor parameters before closing.

## Overrun, failure, and rehearsal record

This is a proposed schedule to test, not evidence that every group will finish
on time. Do not spend the core installing packages or repairing a student's
unsupported platform. If a live cell fails, retain the error and stop claiming
that execution passed. A matching, previously executed artifact may support
an explicitly labeled reference demonstration; it is not a live rerun.

If discussion overruns, shorten the optional parameter-choice discussion or
use the listed paper predictions within the allotted blocks. Keep the core
postselection/sign and order-versus-factor distinctions. Do not skip the required
preclass validator cells or relabel optional discussion time as optional code
validation. If the planned core repeatedly exceeds 50 minutes in a real
run-through, revise its teaching scope explicitly after feedback.

Record actual presenter start/end times per block, pauses, learner questions,
transition delays, and choices deferred during a later human rehearsal. Keep
those observations separate from [local code timings](../R4_DEMONSTRATION_TIMINGS.md).
The current sheet supplies neither a human pacing pass nor an agreed assessment
or solution-distribution policy. Windows/macOS and native editor UI limitations
remain as recorded in the [readiness plan](../RELEASE_READINESS_PLAN.md).
