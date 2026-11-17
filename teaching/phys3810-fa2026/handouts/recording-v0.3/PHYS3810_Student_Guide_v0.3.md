# Qiskit labs: start here

PHYS 3810 | Gage Plott | Student guide | Recording edition v0.3

Follow the video on your laptop and pause whenever you need more time. No Python experience is needed. Nothing is assigned, graded, evaluated, or submitted. We will set up the software, try quantum random bits and a Bell state, then explore QFT, QPE, and HHL. Grover and Shor are optional afterward.

## 1. Open your notebook kit

Download the complete kit supplied with the video through Canvas. **Extract the whole ZIP**, then keep its folders together. The setup part of the video is about 15-20 minutes; downloads and your pauses can take longer.

The video uses **Ubuntu/Linux, 64-bit Python 3.12, and JupyterLab**. These instructions require Python 3.12 already installed with support for virtual environments. They do not install Python itself. Native Windows/macOS and other notebook editors have not been checked for this route. If your setup differs, see page 4 before trying commands for a different system.

Open a terminal in the kit's **runtime/** folder. You should see **requirements.txt**, **constraints-ci.txt**, **src/**, and **teaching/** there. In a repository checkout, use the repository root instead. A terminal is where you enter setup commands; a notebook is where you run the lesson examples.

## 2. Check Python and install the course packages

Run each line below **in the terminal**, pressing Enter and waiting for it to finish before the next line:

```bash
python3.12 --version
python3.12 -c "import struct; print(struct.calcsize('P') * 8)"
```

Expect **Python 3.12.x** and **64**. If either check fails, stop here and use page 4. Keep your operating system's Python unchanged. [1]

Next, create a separate folder for the course's Python packages and activate it. Do this once for this kit:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
```

The version should still be **3.12**. Save the printed Python path; it should end in this kit's **.venv/bin/python**. You will compare it with the notebook's path on page 2. This separate environment keeps the lesson packages apart from other projects. Keep the supplied package versions unchanged. [2]

Installation needs internet. After setup, the examples run on your laptop without an IBM account, API token, GPU, or quantum computer. If a command fails, use page 4 before continuing.

[1. Ubuntu Python setup](https://ubuntu.com/developers/docs/howto/python-setup/)
[2. Python environments](https://docs.python.org/3.12/library/venv.html)

<!-- PAGE BREAK -->

# Open Jupyter and try two circuits

## 3. Start your notebook session

In the same activated terminal, run these commands. The first may wrap on the page, but **it is one command**:

```bash
python -m ipykernel install --sys-prefix --name phys3810-intro --display-name "Python (PHYS 3810 Intro)"
python -m jupyterlab
```

Keep the terminal running. JupyterLab opens in a browser. If it does not, use the local URL printed in the terminal. That URL can contain a private access token: **do not share it in screenshots or email**. Keep authentication enabled. [3]

In JupyterLab's file browser, open:

```text
teaching/phys3810-fa2026/notebooks/intro/01_quantum_rng.ipynb
```

Choose **Kernel > Change Kernel > Python (PHYS 3810 Intro)**. Click the first code cell and press **Shift+Enter**. Its **Interpreter:** path should match the Python path you saved on page 1. Use this course kernel for every notebook; each notebook has its own session.

A **cell** is a block of code or text. The **kernel** runs code and remembers values. Run code top to bottom with **Shift+Enter**; **[*]** means busy. Software checks are not assessments.

## 4. Quantum random bits, then Bell preparation

Run sections **1, 2, 3, 4, 5** of the random-bit notebook. Then open **02_bell_state.ipynb** in the same intro folder and repeat. Both begin with **shots = 128** and **seed = 2026**. A shot is one fresh preparation and measurement. The seed makes the simulation repeatable.

In each notebook, try this edit:

1. Under **2. Choose the shot count**, change shots to **1024** and run that cell. Keep seed at 2026.
2. Run section **4** to sample again, then section **5** to redraw the plot. Check the count total and plot title.
3. Restore shots to **128**, then run **2 -> 4 -> 5** again.

**Bell reminder:** if optional section **7** has already been displayed, rerun its code after each shot-count change, including the restore. Run All displays section 7 too. Editing a number without running the affected cells leaves old results on screen.

For random bits, 0 and 1 each have probability one half, but sample counts need not split evenly. Bell's ideal results contain only **00 and 11**; the rightmost digit is qubit 0. These paired results are correlated, although that plot alone does not prove entanglement. Both lessons use a seeded laptop simulation, not physical quantum entropy or secure random numbers.

[3. Jupyter authentication and tokens](https://jupyter-server.readthedocs.io/en/latest/operators/security.html)

<!-- PAGE BREAK -->

# Three algorithm demonstrations

Return to **teaching/phys3810-fa2026/notebooks/** and open these notebooks in order. Use **Python (PHYS 3810 Intro)**, run from the top, and keep the defaults first. The helper code is provided for you.

## 5. QFT: change a phase pattern

Open **02_qft.ipynb**. The starting label **"011"** represents 3. The quantum Fourier transform changes the state's phase pattern. The upper plot shows amplitudes; the lower plot shows measurement probabilities. All eight probabilities are **1/8**, although the amplitudes differ. The inverse transform recovers the starting label: **256 counts of 011**.

Optional edit: change **basis_label** from **"011"** to **"001"**. Run that parameter cell and **every following code cell**. The phase pattern changes and the inverse sample becomes 256 counts of 001. Restore "011" and repeat. Keep **num_qubits = 3**. [4]

## 6. QPE: read a phase as a bit string

Open **03_qpe.ipynb**. Quantum phase estimation uses a prepared target state and repeated controlled operations to estimate a phase. It uses inverse QFT to turn the resulting pattern into counting bits. QFT alone does not do the entire phase-estimation task.

Keep **num_counting_qubits = 3** and **exact_phase = 3/8**. The ideal result is **2048 counts of 011**. Read 011 as integer 3, then divide by 8; do not reverse the digits.

Optional edits: change exact_phase to **1/8**, then **6/8**, then restore **3/8**. Each time, run the edited parameter cell and **every following code cell**. The labels should be **001**, **110**, and **011**.

The separate nonexact example uses **1/3**, which produces a spread of possible answers. More counting bits refine the available estimates. If exploring that section, keep its phase between **0 inclusive and 1 exclusive**; leave the exact-example cell on its supported grid. [5]

## 7. HHL: prepare a solution state

Open **04_hhl.ipynb** and run from the top. Keep the supplied matrix and **rhs_amplitudes = [1, 0]**. This small example represents a linear-system solution in a quantum state. It keeps measurements whose success flag is 1; the exact success probability is **5/8, or 62.5%**.

The notebook compares its result with a classical calculation. The quantum circuit prepares a state; it does not return the full classical solution vector from one measurement. The extra measurement plots help show a relative minus sign that the first probability plot alone would hide. [6]

Optional edit: change only rhs_amplitudes to **[0, 1]**. Run that cell and **all following code cells**, then restore [1, 0] and repeat. The solution changes, while success remains 5/8. Keep the supplied matrix for this introduction; the notebook supports only a restricted family of two-by-two systems.

Later, try **01_grover.ipynb** for a small search example or **05_shor.ipynb** for a compiled factoring example with **N = 15**. Both are optional. These small simulations do not demonstrate quantum advantage.

[4. QFT definition](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.QFTGate)
[5. Phase estimation](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/phase-estimation-and-factoring/phase-estimation-procedure)
[6. HHL and its output](https://arxiv.org/abs/0811.3171)

<!-- PAGE BREAK -->

# Save your work and solve common problems

## 8. Save, stop, and return later

Save with **Ctrl+S**; saving submits nothing. Finish with **File > Shut Down** and wait for Jupyter to stop. Closing a browser tab alone does not stop its session. To return later, open a terminal in the same **runtime/** folder and run:

```bash
source .venv/bin/activate
python -m jupyterlab
```

## 9. Try the matching fix first

**Python is missing, not version 3.12, or not 64-bit.** Stop before installing packages. Python versions vary between Ubuntu releases. Send Gage the two check results and your Ubuntu version for the appropriate setup. Do not remove or replace system Python.

**The terminal cannot find requirements.txt or .venv/bin/activate.** Extract the whole ZIP and open the terminal in **runtime/**, beside requirements.txt. If .venv was never created successfully, return to page 1. Do not work inside the unopened ZIP.

**Installation reports an error.** Check your connection and folder. After an interrupted download, retry the same install command when the connection returns. For a repeated error or missing venv support, save the error and contact Gage. Keep package versions unchanged; stop at failed installs.

**The course kernel is absent, or a package cannot be imported.** Activate this kit's environment, repeat page 2's kernel-registration command, and select **Python (PHYS 3810 Intro)**. Compare the notebook's Interpreter path with page 1's terminal path. Different paths mean different Python environments. Keep the error if matching paths do not resolve it.

**A plot is old, a name is undefined, or cells ran out of order.** Save your edit, choose **Kernel > Restart Kernel**, then **Run > Run All Cells** to rebuild remembered values. This displays Bell section 7 too. Later shot-count edits need **2 -> 4 -> 5**, plus Bell 7 whenever already displayed.

**A guide shows Markdown symbols instead of usable links.** In JupyterLab, right-click the guide file and choose **Open With > Markdown Preview**. If a link or notebook reports a missing file, check that the kit's folders are still together.

**The kit was moved, or your operating system differs.** Do not copy an environment between locations or machines. Preserve your notebooks and contact Gage before reusing it. These Ubuntu commands are not validated native Windows/macOS instructions.

## Still stuck? Contact Gage

For these labs, email **gage-plott@utc.edu** with your operating system/version, Python version, notebook filename and section, failing command or cell, exact error, and the fix you tried. A clear, cropped screenshot can help.

**Remove private information:** omit token-bearing Jupyter URLs, passwords, API keys, and unrelated account details. Pause and resume after the issue is resolved; nothing is submitted or graded.
