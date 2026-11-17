# Qiskit labs: start here

PHYS 3810 | Gage Plott | Student companion | Recording edition v0.2

Follow the video on your laptop and pause whenever you need more time. No Python experience is assumed. Nothing is assigned, graded, evaluated, or submitted. The route is **setup -> quantum random bits -> Bell state -> QFT -> QPE -> HHL**. Grover and Shor are optional exploration afterward.

## 1. Open the complete matching kit

Use the complete notebook kit supplied with the video through Canvas. Extract the entire folder before opening a notebook and keep its folders together. The setup chapter targets 15-20 minutes of video; downloads and your pauses can take longer.

This route uses **Ubuntu/Linux, 64-bit CPython 3.12, and JupyterLab**. Native Windows/macOS and other notebook editors have not been validated for this route. Use the supported course setup or get assistance if your laptop differs.

Open a terminal in the kit's **runtime/** folder, beside **requirements.txt**, **constraints-ci.txt**, **src/**, and **teaching/**. If using a repository checkout, this is the repository root instead. A terminal is where installation and launch commands go. Run each line there, not in a notebook cell, and wait for it to finish.

## 2. Check Python and create the course environment

Python runs notebook code. First check its version and whether it is 64-bit:

```bash
python3.12 --version
python3.12 -c "import struct; print(struct.calcsize('P') * 8)"
```

Expect **Python 3.12.x** and **64**. If the command is missing or the result differs, pause for assisted setup. These commands require an existing Python 3.12 installation with venv support; they do not install Python itself. Keep the operating system's Python intact. [1]

Create a separate course environment once in the requirements folder:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
```

The version must still be 3.12. Save the printed interpreter path; it should end in this folder's **.venv/bin/python**. The environment keeps course packages separate from other projects. Keep the supplied package versions unchanged. If the folder already has an environment from another kit, get help before reusing it. [2]

Installation needs internet. The lessons then run locally on the CPU without an IBM account, API token, GPU, or quantum hardware. If installation fails, keep the error and ask for help before continuing.

[1. Ubuntu Python setup](https://ubuntu.com/developers/docs/howto/python-setup/)
[2. Python 3.12 environments](https://docs.python.org/3.12/library/venv.html)

<!-- PAGE BREAK -->

# Open Jupyter and try the first labs

## 3. Select and check the notebook kernel

In the same activated terminal, run the following. The first line wraps visually on this page but is one command:

```bash
python -m ipykernel install --sys-prefix --name phys3810-intro --display-name "Python (PHYS 3810 Intro)"
python -m jupyterlab
```

Keep the terminal running. If no browser opens, use the local URL printed there. It can contain a private access token: keep it out of screenshots and recordings, and keep authentication enabled. [3, 4]

In JupyterLab's file browser, open:

```text
teaching/phys3810-fa2026/notebooks/intro/01_quantum_rng.ipynb
```

Choose **Kernel > Change Kernel > Python (PHYS 3810 Intro)**. Run the first code cell with **Shift+Enter**. Its **Interpreter:** path must match the terminal path and identify this kit's **.venv/bin/python**. Use this same course kernel for all notebooks; each notebook has its own session. A friendly kernel name alone does not prove the path is correct.

A **cell** contains code or explanatory text. The **kernel** runs code and remembers values. Run code top to bottom; **[*]** means busy. A line beginning with **#** is a comment. Names such as **shots** hold values used later. The software's checks are not assessments.

## 4. Quantum random bits, then a Bell state

Run sections **1, 2, 3, 4, 5** of the RNG notebook. Then open **02_bell_state.ipynb** in the same intro folder and repeat. Both start with **shots = 128** and **seed = 2026**.

Try the same small edit in each notebook:

1. In **2. Choose the shot count**, change shots to **1024** and run that parameter cell. Keep seed at 2026.
2. Run **4. Sample the circuit** in RNG, or **4. Sample the pair** in Bell; then run **5. Plot the counts**. Check the count total and plot title.
3. Restore shots to **128** and repeat **section 2 -> section 4 -> section 5**.

**Bell reminder:** if optional **section 7** has already been displayed, rerun its code after each shot-count change, including the return to 128. Run All also displays section 7. Section 3's preparation is independent of shots; section 6 is text. Editing a value without running its cell does not update existing results.

The RNG probabilities are one half for 0 and 1. Bell results ideally contain only 00 and 11; each individual bit remains equally likely. The rightmost digit is qubit 0. A Z-basis histogram alone does not prove entanglement. These seeded laptop samples simulate quantum experiments; they are not physical quantum entropy or cryptographic randomness.

[3. IPython kernels](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)
[4. Jupyter security](https://jupyter-server.readthedocs.io/en/latest/operators/security.html)

<!-- PAGE BREAK -->

# Fourier transform and phase estimation

Return to **teaching/phys3810-fa2026/notebooks/**. Continue with **02_qft.ipynb**, then **03_qpe.ipynb**, using **Python (PHYS 3810 Intro)**. Run each notebook's source-location and import cells first and check its printed interpreter. You do not need another Python environment.

## 5. QFT: see a phase pattern

The quantum Fourier transform changes basis. The default uses **num_qubits = 3** and **basis_label = "011"**, meaning integer 3. Run the parameter cell, the matrix/circuit cell, the phase-pattern figure, and the inverse/known-gradient cell in order.

Look at the two plot panels. The real and imaginary amplitudes show a pattern, while all eight probabilities equal **1/8**. An amplitude carries phase information that its squared magnitude alone loses. The inverse transform recovers 011; the ideal sample is **256 counts of 011**.

Optional edit: change basis_label to **"001"** in the parameter cell. Run that cell and **every following code cell**. The phase pattern changes, probabilities stay 1/8, and the inverse sample becomes 256 counts of 001. Restore "011" and repeat the same sequence. Keep the three-character width matched to the three qubits.

This example creates a known phase pattern. It is not phase estimation yet. QFT does not let one measurement reveal every amplitude, and this small simulator example does not demonstrate a speedup over classical FFT software. [5]

## 6. QPE: estimate an eigenphase

QPE estimates phi in **U|u> = exp(2*pi*i*phi)|u>**, modulo one. Here the target is deliberately prepared in a known eigenstate. Controlled powers of U create a phase pattern, and inverse QFT converts that pattern into counting bits. Only the counting register is measured.

Run the helper/import cell, exact-example cell, and exact-sampling cell. Defaults are **num_counting_qubits = 3**, **exact_phase = 3/8**, and **2048 shots**. The expected label is **011**. Decode it as integer 3 divided by 8; do not reverse the bits.

Optional edits: change exact_phase to **1/8**, then **6/8**, then restore **3/8**. Each time run the edited parameter cell and **every subsequent code cell**. The expected exact labels are **001**, **110**, and **011**, respectively, with all 2048 counts on that label in this ideal example.

The separate nonexact section uses **1/3** with 3 and 5 counting bits. That phase is not exactly on either finite grid, so several outcomes have nonzero probability. More counting bits refine the grid; they do not make every result certain. Use that section for non-grid phases from 0 inclusive to 1 exclusive; keep the exact-example cell on its supported grid. [6]

The later SDK comparison and input checks support correctness. They need no additional environment or changes to source files. Keep support functions unchanged and use the named lesson parameters.

[5. QFT definition](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.QFTGate)
[6. Phase estimation](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/phase-estimation-and-factoring/phase-estimation-procedure)

<!-- PAGE BREAK -->

# HHL, optional exploration, and saving

## 7. HHL: a small linear-system example

Open **04_hhl.ipynb** in the same folder and select the same course kernel. Run its first two source/import cells, then the parameter/circuit cell, raw-state checks, state-comparison plot, and postselected sampling.

The default inputs are:

```text
matrix_entries = [[1.5, 0.5], [0.5, 1.5]]
rhs_amplitudes = [1, 0]
```

Classically A x = b gives **x = (3/4, -1/4)**. The quantum example prepares the normalized state **(3, -1)/sqrt(10)** when its success flag is 1. The exact success probability is **5/8 = 0.625**. HHL's output is a quantum state; the notebook's classical solve is a reference check, not the circuit's output. [7]

The sign matters. Z-basis probabilities **0.9 and 0.1** alone cannot reveal the negative amplitude. The conditional X/Y/Z expectations are **-0.6, 0, 0.8**. Sampling uses **4096 shots per basis** and keeps system outcomes from the same shots whose success flag is 1. Counts vary around the theoretical predictions.

Optional edit: set only rhs_amplitudes to **[0, 1]**, run that parameter cell and **all following code cells**, then restore [1, 0] and repeat. The changed normalized state is **(-1, 3)/sqrt(10)**; success remains 5/8 and the Z expectation becomes -0.8.

This example is restricted to positive Hermitian 2x2 matrices with integer eigenvalues **1-7** and normalized input vectors. It is not a general-purpose linear solver. Keep the supplied matrix unless following the notebook's supported examples.

## 8. Explore later if interested

**01_grover.ipynb** demonstrates amplification of marked outcomes on 2-5 qubits. **05_shor.ipynb** is a compiled N = 15 example using four residue qubits and 4-6 counting qubits. These are optional. Nothing is submitted. QFT supports 1-6 qubits; QPE separately supports 1-6 counting qubits and one or two target qubits. These local teaching examples do not establish quantum advantage.

## 9. Save, stop, and recover

Save with **Ctrl+S**; saving submits nothing. Finish with **File > Shut Down**. Closing a browser tab alone does not stop its kernel. To return later, open a terminal in the same requirements folder and run:

```bash
source .venv/bin/activate
python -m jupyterlab
```

For stale results, save the intended edit, use **Kernel > Restart Kernel**, then **Run > Run All Cells**. This also displays Bell section 7. For a wrong interpreter, reactivate the intended environment, register/select its kernel, and compare paths. For missing files, check that the whole kit is together. Keep error text when asking for help; omit private token-bearing URLs. Do not skip failed cells or change package pins.

[7. Original HHL paper](https://arxiv.org/abs/0811.3171)
