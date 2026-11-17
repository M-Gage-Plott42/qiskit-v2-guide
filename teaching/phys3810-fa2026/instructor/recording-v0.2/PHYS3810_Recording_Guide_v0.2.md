# PHYS 3810 recording guide

Gage Plott | Presenter copy | Recording edition v0.2 | Code basis 727cb98c468b

**Route:** setup, quantum random bits, Bell preparation, QFT, QPE, HHL, then pointers to optional Grover and Shor. Zero Python assumed; students follow on laptops and pause freely. Nothing is assigned, graded, evaluated, or submitted. Print these four pages single-sided. Only setup has a requested target: 15-20 minutes. The rest has no fixed video-time limit.

## 1. Start the recording and setup chapter

Your guided Ubuntu test already covered browser navigation, voice, pause, and playback. Use the working OBS configuration. Before the take, check the live framing, microphone meter, and readable code/plots. Keep notifications and private windows out of capture. This is the ordinary final-take check; the successful test need not be repeated as a new project milestone.

**Opening:** "I'm Gage Plott. We will set up Qiskit, simulate random bits, prepare a Bell state, and explore Fourier transforms, phase estimation, and a small linear-system example. Pause the video whenever you want to try a step. Nothing is graded or submitted."

Show the complete extracted kit. Open a terminal in **runtime/** beside requirements.txt. In a repository checkout, use the repository root instead. Python 3.12 must already be installed; these commands create the course environment. Keep the operating system's Python intact. Run one terminal command at a time:

```bash
python3.12 --version
python3.12 -c "import struct; print(struct.calcsize('P') * 8)"
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name phys3810-intro --display-name "Python (PHYS 3810 Intro)"
python -m jupyterlab
```

The kernel-registration line wraps here but is one command. Expect Python 3.12, 64-bit, and this kit's **.venv/bin/python**. Installation needs internet. If you shorten a wait in editing, say that installation time varies.

**Pause capture before Jupyter launch and authentication.** Keep authentication enabled; check the address and terminal privately, then resume inside the notebook. Keep the terminal running. Open **teaching/phys3810-fa2026/notebooks/intro/01_quantum_rng.ipynb**. Select **Python (PHYS 3810 Intro)** and compare its printed Interpreter path with the terminal path. Use this same verified environment for every lesson; no second environment is needed.

Explain: a cell is a block of code or text; the kernel runs code and remembers values; Shift+Enter runs a cell; [*] means busy. A line beginning with # is a comment. An assertion is a software check, not a student assessment. Editing text alone changes neither stored values nor existing plots.

[1. OBS recording setup](https://obsproject.com/kb/quick-start-guide)
[2. Jupyter authentication and tokens](https://jupyter-server.readthedocs.io/en/latest/operators/security.html)

<!-- PAGE BREAK -->

# Quantum random bits and Bell states

## 2. Quantum random-bit simulation

Open **intro/01_quantum_rng.ipynb**. Run section 1, then **2, 3, 4, 5** in order. Start at **shots = 128**, **seed = 2026**. Show the H gate, the exact probabilities, the first 24 ordered bits, the counts, and the histogram's Count axis.

**Say:** "H prepares an equal superposition from the initial zero state. A measurement gives 0 or 1 with probability one half. Each shot starts with a fresh preparation and measurement. These laptop results are seeded classical simulation of that quantum experiment; they are not physical quantum entropy or cryptographic randomness."

**Demonstrate:** change shots to 1024 in section 2 and run **2 -> 4 -> 5**. Point out the new count total and plot title. Restore 128 and repeat **2 -> 4 -> 5**. Keep seed fixed. Section 3 does not depend on shots; section 6 is explanatory text.

**Explain the figure:** more shots change sample size, not the underlying one-half probabilities. A closer split is typical statistically but is not guaranteed in each comparison. Repeating the same seed can repeat the sample. A bar height is a count; divide by shots to obtain a sample frequency.

## 3. Bell-state preparation

Open **intro/02_bell_state.ipynb** in its own kernel. Select the same course kernel, run the environment check, then **2, 3, 4, 5**. Show H on qubit 0 followed by CX with control 0 and target 1.

**Say:** "This prepares the phi-plus Bell state, an equal superposition of 00 and 11. Each individual bit is equally likely to be 0 or 1, but the pair is correlated. With this measurement map, the rightmost digit is qubit 0. Ideally we see only 00 and 11."

**Demonstrate:** use the same **128 -> 1024 -> 128** edit, running **2 -> 4 -> 5** after each change. **Whenever Bell section 7 is already displayed, rerun section 7 too**, including after returning to 128. This also applies if a prior Run All displayed that extension.

**Interpret honestly:** a classical 50/50 mixture of 00 and 11 gives the same Z-basis histogram. That histogram alone is not proof of entanglement. If you show section 7, explain that H on both qubits changes the measurement basis. Phi-plus remains correlated in X; the printed classical-mixture comparison gives four equal probabilities. That comparison is theoretical, not a second sampled experiment or a Bell-inequality test.

## Transition to the three algorithms

Return to **teaching/phys3810-fa2026/notebooks/**. Use **02_qft.ipynb**, then **03_qpe.ipynb**, then **04_hhl.ipynb**. Keep each notebook in its own kernel using **Python (PHYS 3810 Intro)**. Run its first source-location and import cells before the demonstration.

**Say:** "We now have the basic notebook workflow. The remaining examples use prepared helper functions, so we can focus on the circuits, predictions, and results. The Fourier transform is used inside phase estimation, which is then used inside our linear-system demonstration. They solve different tasks."

The next pages identify code-cell IDs for your preparation. On camera, use the visible section headings and outputs; students do not need to locate IDs or read support code line by line.

<!-- PAGE BREAK -->

# Fourier transform and phase estimation

## 4. QFT: a phase pattern and its inverse

In **02_qft.ipynb**, run **qft-locate-source**, then **qft-imports-parameters**. Keep num_qubits = 3 and basis_label = "011". Then run **qft-matrix-and-circuit**, **qft-phase-pattern-figure**, and **qft-inverse-and-known-gradient**, discussing each result.

**Say:** "011 is the integer 3. Our forward Fourier transform uses a positive exponential sign. It spreads this basis input across eight amplitudes. Their phases vary, but every measurement probability is 1/8. The upper plot shows amplitude components; the lower plot shows probabilities. Equal probabilities do not mean identical quantum states."

Show the circuit and its complete-matrix check. For N = 8 and input k = 3, the amplitude at output j is **exp(2*pi*i*3*j/8)/sqrt(8)**. The inverse uses the negative sign and recovers the label. The sampling output is **{'011': 256}**.

**Edit and restore:** change basis_label to "001" in the parameter cell. Run that cell and **every subsequent code cell**, in order. The phase plot changes; probabilities remain 1/8; inverse samples become **{'001': 256}**. Restore "011" and repeat the same rerun sequence. The later cells are additional checks; they need no separate narrated lesson.

**Distinguish the task:** the known-gradient example deliberately supplies its integer. It is not QPE. QFT is a change of basis; it does not reveal every amplitude or guarantee a general speedup over a classical FFT.

## 5. QPE: turn an eigenphase into counting bits

In **03_qpe.ipynb**, run **qpe-locate-source** and **qpe-imports-helpers**, then **qpe-exact-example** and **qpe-exact-sampling**. Defaults are three counting qubits, exact_phase = 3/8, and 2048 sampled shots. The target is explicitly prepared in state 1.

**Say:** "For this target, U contributes phase exp(2*pi*i*phi). The counting qubits control U, U squared, and U to the fourth power. Phase kickback creates a pattern that inverse QFT converts into a label. We measure only the counting register."

Read **011 -> integer 3 -> 3/8**. Do not reverse the displayed bits. In the ideal exact case, all 2048 counts are 011. Edit exact_phase to **1/8**, then **6/8**, then restore **3/8**. Each time run the edited parameter cell and **every subsequent code cell**. Expected labels are **001, 110, 011**. This complete rerun also refreshes reference and expansion outputs.

Briefly show the existing nonexact example **1/3**, with 3 and 5 counting bits: it produces a distribution on a finite grid, not one certain exact answer. More counting bits refine the grid; controlled powers and preparation still cost resources. Use the nonexact section for non-grid phases from 0 inclusive to 1 exclusive; keep the exact-example cell on its supported grid.

**Presenter-only convention note:** qpe-sdk-reference checks that the pinned Qiskit 2.6.1 reference has reversed counting-output order, then explicitly swaps it into this module's convention. This is a tested API convention difference; students should not add another reversal to the module's results.

[3. IBM Fourier transform definition](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.QFTGate)
[4. IBM phase-estimation explanation](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/phase-estimation-and-factoring/phase-estimation-procedure)

<!-- PAGE BREAK -->

# HHL and closing the class

## 6. HHL: a small solution-state example

Open **04_hhl.ipynb**. Run **hhl-locate-source**, **hhl-imports-helpers**, then **hhl-parameters-circuit**, **hhl-raw-state-checks**, **hhl-state-comparison**, and **hhl-postselected-sampling**. Do not change support functions.

Use the defaults:

```text
matrix_entries = [[1.5, 0.5], [0.5, 1.5]]
rhs_amplitudes = [1, 0]
```

**Say:** "Classically, solving A x = b gives x = (3/4, -1/4). HHL prepares a quantum state proportional to that solution when its success flag is 1. It does not print the full classical solution vector as the quantum algorithm's output. The classical solve in this notebook is an independent reference check."

Show the circuit's three counting qubits, one system qubit, and one success qubit. Here U = exp(+i*A*pi/4), so eigenvalues 1 and 2 have phases 1/8 and 2/8. QPE encodes them; a controlled reciprocal rotation weights the eigencomponents; inverse QPE clears the counting register. The flag remains for selecting successful shots.

**Expected default results:** raw successful amplitudes are (0.75, -0.25); success probability is **5/8 = 0.625**; the normalized successful state is **(3, -1)/sqrt(10)**. Failure probability is 3/8. Counting qubits return to 000 on both branches in this exact-spectrum example. Do not generalize that cleanup to arbitrary approximate HHL.

Explain the plots: Z-basis probabilities are **0.9 and 0.1**, but those alone hide the minus sign. The conditional X/Y/Z expectations are **-0.6, 0, 0.8**. The sampling cell uses **4096 shots per basis** and keeps system outcomes from the same shots whose success flag is 1. Selected counts fluctuate; they need not equal 2560 exactly.

**Optional edit and restore:** change only rhs_amplitudes to **[0, 1]**. Run the parameter cell and **every following code cell**, then restore [1, 0] and repeat. The changed normalized state is **(-1, 3)/sqrt(10)**; success remains 5/8; Z expectation changes to -0.8. Do not change the matrix outside the stated supported family during this introduction.

## 7. Optional exploration and closing

Point to **01_grover.ipynb** and **05_shor.ipynb** without making them additional recorded lessons. Grover amplifies marked outcomes in a small search. Shor is a compiled N = 15 example with classical order/factor recovery. They are optional and nothing is submitted.

Keep the limits clear: QFT supports 1-6 qubits; QPE supports 1-6 counting and one/two target qubits. HHL is a positive Hermitian 2x2 problem with integer eigenvalues 1-7 and normalized b. Shor separately uses four residue qubits. Dense simulation, input loading, controlled powers, postselection, and readout have costs; these examples do not demonstrate quantum advantage.

Save with **Ctrl+S**; finish with **File > Shut Down**. Closing a browser tab alone does not stop a kernel. If state is stale: save the intended edit, **Kernel > Restart Kernel**, then **Run > Run All Cells**. A Bell Run All displays section 7, so include it in later shot-count reruns.

After recording, check the saved video's opening, representative code/plots, audio, and ending. Supply Rick the video, student guide, and matching complete notebook kit for Canvas. This is materials delivery; no duration approval or new logistics questionnaire is needed.

[5. Original HHL paper and output model](https://arxiv.org/abs/0811.3171)
