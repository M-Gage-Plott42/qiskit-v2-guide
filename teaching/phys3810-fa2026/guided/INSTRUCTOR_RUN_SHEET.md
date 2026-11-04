# Presenter route: Python, Grover, and phase

Material development: **Gage Plott**. Complete worked examples for students with
zero Python experience. Demonstrate, let students repeat, change one supported
value together, and discuss. No grading, evaluation, assignments, or submissions.
The proposed periods are 85 minutes: 75 minutes of activity plus ten minutes
for questions, recovery, and transitions. Human pacing has not been rehearsed.

## Before presenting

Use the [quickstart](STUDENT_QUICKSTART.md). Agree who provides assisted setup;
the opening activity assumes a working Python 3.12 environment, not an install
on unfamiliar laptops. If setup consumes the period, use the shorter route.
Do not turn setup into required independent homework. Confirm the displayed
interpreter path and select **Python (PHYS 3810 Guided)** or the supplied working
kernel. Keep each notebook in a separate kernel and work in a local copy.

From the extracted kit's `runtime` folder, the complete support check is:

```bash
python scripts/validate_classroom.py --profile all
```

This checks eleven notebooks, including eight reference/validation notebooks.
During teaching, discuss only the chosen route. Start fresh before a rehearsal;
keep earlier outputs only as clearly identified fallback pictures. They do not
prove a new execution succeeded. Stop on an unexplained error and preserve it.

After editing a parameter, run the parameter cell itself with **Shift+Enter**.
Then run the following code cells in order. Editing the text alone does not
update Python's variables; downstream calculations can still show the old result.

## Day 1: Python and Qiskit

Open [01_python_and_qiskit](../notebooks/guided/01_python_and_qiskit.ipynb).
Cell numbers are one-based notebook positions, including explanation cells.

- **0–15 minutes:** introduction and cell 2 (`guided-python-support`), run
  unchanged. Show Shift+Enter, the busy marker, execution order, and interpreter.
- **15–35:** cells 4, 6, 8, and 10. Show a value assignment, text in quotes,
  `1 / 2`, the two-item list, positions 0/1, function arguments, and imports.
  Change only the greeting and rerun cell 4. Keep 512 repetitions unchanged.
  Support imports and checks need not be written or understood in detail.
- **35–55:** cells 12 and 14. Make a fresh one-qubit X circuit, predict its
  output, then sample it. Expected: X gives |1> and 512 `1` samples. Rerunning
  the construction cell makes a new circuit, so a second X is not appended.
- **55–70:** cells 16 and 18. Make a fresh H circuit, predict its output, then
  sample it. H gives roughly balanced counts. The exact H probabilities
  are equal, while a finite sample need not be. A bar height is a count, not
  an amplitude. The seeded local simulation is not quantum hardware.
- **70–75:** cell 19 discussion and save/restart/run-all. Saving keeps a local
  copy; restarting discards variables. Running from the top restores them.

Common mistakes: pasting a terminal command into a Python cell; missing quotes;
using list position 1 for the first element; running a sample before its circuit;
assuming an old displayed output reflects a recent edit. Read the error, restart,
and rerun in order. No missing code is left for learners to invent.

**50-minute fallback:** 10 minutes opening; 10 on values/lists/calls/imports;
15 on X; 10 on sampling; 5 on save/restart. Defer H and its sampling discussion.
If no usable environment is available, use the presenter's demonstration and
record that students did not complete a laptop run. Do not claim setup fitted.

<!-- pagebreak -->

## Day 2: Grover follow-along

Open [02_grover_follow_along](../notebooks/guided/02_grover_follow_along.ipynb).

- **0–10:** recap cells/order and run cell 2 (`guided-grover-support`). It imports
  the shared course implementation; run path-finding code unchanged.
- **10–25:** explain the four candidates `00`, `01`, `10`, `11`. Rightmost bit
  is qubit 0. The oracle marks the chosen label's phase; diffusion changes the
  amplitudes. The chosen target is built into this tiny instructional oracle.
- **25–45:** under **Choose the two guided values**, run cell 4 beginning
  `target = "01"`, with `iterations = 1`; then run cells 6, 8, 10 to
  build, draw, and sample. Expect target probability 1 and only `01` counts.
  One iteration means one oracle-plus-diffusion pair after uniform preparation.
- **45–65:** change cell 4's target to `"10"`, run **cell 4 itself**, then
  **6, 8, 10, 12** in order. Next change iterations to 2 and repeat that complete
  sequence, starting with **cell 4**. Expected marked probability drops
  to 1/4. Zero iterations also gives 1/4. Cell 12 compares all three cases.
  Safe edits are exactly four two-bit targets and iteration counts 0, 1, 2.
- **65–75:** discuss amplification versus overshooting and sample fluctuations.
  The plot captions, selected label, expected counts, and probabilities all
  follow the current parameters. More iterations need not improve success.

Common mistakes: dropping the quotes; using a three-bit target; changing the
parameter without executing that cell and its dependent cells; reading a bitstring as a phase.
The label is a basis-state index here. Restart/run-all restores a consistent
example. Exact simulation and finite sampled counts are different observations.

**50-minute fallback:** 10 recap; 15 four-candidate explanation; 20 default
example; 5 discussion. Stop after the one-iteration histogram; show the
comparison plot only if time permits. Do not introduce another algorithm to
fill an overrun. This is a bounded simulation, not evidence of quantum advantage.

<!-- pagebreak -->

## Day 3: QFT and QPE follow-along

Open [03_qft_qpe_follow_along](../notebooks/guided/03_qft_qpe_follow_along.ipynb).

- **0–10:** run cell 2 (`guided-phase-support`); recap phase and rightmost-bit
  ordering. The read-only display machinery is not a matrix-programming task.
- **10–30:** under **QFT: select a known input label**, cell 4 begins
  `basis_label = "01"`. Run **4, 6, 8** to choose the input, apply QFT, and plot real
  and imaginary amplitudes. Expected amplitudes are (1, i, -1, -i)/2 at indices
  0–3, with the positive Fourier sign. Every measurement probability is 1/4;
  those probabilities alone cannot reveal this complex phase pattern.
- **30–50:** cell 10 applies inverse QFT and recovers the original basis label
  with probability 1. Change cell 4 to `"10"`, run **cell 4 itself**, then
  **6, 8, 10** in order. The
  amplitudes become (1, -1, 1, -1)/2 and recovery gives index 2. Both transforms
  include their full swaps. This known-state transformation/undoing is not QPE.
- **50–65:** under **QPE: choose an exact eigenphase**, cell 12 begins
  `exact_phase = 3 / 8`. Run **12, 14, 15, 17** to choose, prepare/build, draw, and
  sample QPE. Three counting qubits precede one target qubit, explicitly flipped
  from |0> to eigenstate |1>. The target phase operation and controlled powers
  encode the eigenphase; inverse QFT decodes the counting register. Only that
  register is measured, yielding `011`; `int("011", 2) / 8` is 3/8.
- **65–75:** change cell 12 to `exact_phase = 1 / 8`, run **cell 12 itself**,
  then **14, 15, 17** in order, and
  observe `001`. Contrast input basis labels with counting-register phase labels.
  Three counting bits resolve multiples of 1/8; nonexact phases are outside
  this guided example. All 512 ideal samples have the exact expected label.

Common mistakes: reversing `011`; measuring the target instead of counting
qubits; forgetting the target X preparation; dividing every label by eight;
claiming that a flat histogram means phases are absent. Do not edit register
widths or support code. Rebuild after every phase edit; restart if state is unclear.

**50-minute fallback:** 10 phase recap; 20 phase-pattern display; 15 inverse
recovery; 5 discussion. Stop after QFT recovery and defer QPE. Only if additional
time is available, offer the default QPE example as a presenter-only demonstration;
it is outside the 50-minute route. The QFT examples are simulator inspections of amplitudes,
not a way to read a full quantum state from one device measurement.

## Two meetings and final choices

Use Day 1 plus Day 2. A preferred phase day can replace Grover after discussion;
a short compiled-Shor demonstration replaces an agreed segment rather than
being added. HHL and full Shor remain supporting references. Confirm final
dates/count, algorithm priorities, laptop/setup support, prior quantum coverage,
and delivery responsibility using the [agenda](REVIEW_AGENDA.md). The earlier
November 19 proposal remains unresolved; no alternate date is implied.
