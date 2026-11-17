# One class: quantum random bits and a Bell state

Presented by **Gage Plott**. Follow the prerecorded video on your laptop and
pause whenever you need more time. No Python experience is assumed. Nothing
is assigned, graded, evaluated, or submitted.

Start with setup, then run these two notebooks in order:

1. [Quantum random bits](../notebooks/intro/01_quantum_rng.ipynb).
2. [Prepare a Bell state](../notebooks/intro/02_bell_state.ipynb).

The setup chapter targets 15–20 minutes of video; installation and your pauses
may take longer. The total class window and date are not fixed by this guide.
Use **Ubuntu/Linux, 64-bit CPython 3.12, and JupyterLab** for this route. Native
Windows/macOS and other notebook editors have not been validated for it.

## 1. Open the complete matching kit

Use the complete single-class kit supplied with the video and extract it before
opening a notebook. Keep all its folders together. The older full-course
`v0.2.0-rc1` and guided `v0.2` ZIPs do **not** contain these two lessons. A new
public student download has not been published; ask for the matching kit if it
has not been supplied.

Open a terminal in the folder containing `requirements.txt`, `constraints-ci.txt`,
`src/`, and `teaching/`. In the extracted review kit, this is its **`runtime/`
folder**. In a repository checkout, it is the **repository root**. The following
blocks are terminal commands, not notebook cells. Run each line and wait for it
to finish before entering the next. Installation needs internet; the lessons
then run locally without an IBM account or quantum hardware.

## 2. Check Python, then create the course environment

Python is the program that runs notebook code. First check the required version
and whether it is 64-bit:

```bash
python3.12 --version
python3.12 -c "import struct; print(struct.calcsize('P') * 8)"
```

Expect `Python 3.12.x` and `64`. If the command is missing or gives a different
result, pause for assisted setup. Ask the instructor to install **64-bit
CPython 3.12 with `venv` support for your Ubuntu release**, then repeat these
checks. Ubuntu's default `python3` version varies by release; installing its
default Python package does not always install 3.12. Keep the operating
system's Python intact. See the official [Ubuntu Python installation guide](https://ubuntu.com/developers/docs/howto/python-setup/).
These course commands start from an available Python 3.12 installation.

Create a separate environment once in the requirements folder:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
```

The version must still be 3.12. Save the printed interpreter path: it should end
in this folder's **`.venv/bin/python`**. The environment keeps course packages
separate from other projects. Keep the supplied requirements and constraints
unchanged. If this folder already has an environment from another kit, ask for
help before reusing it.

## 3. Open JupyterLab and check the kernel

In the same activated terminal, run:

```bash
python -m ipykernel install --sys-prefix --name phys3810-intro --display-name "Python (PHYS 3810 Intro)"
python -m jupyterlab
```

Keep the terminal running. If no browser opens, use the local URL printed there.
That URL can contain a private access token: keep it out of shared screenshots
and recordings, and keep authentication enabled. Pause capture during launch
and login, then resume inside the notebook. [Jupyter security reference](https://jupyter-server.readthedocs.io/en/latest/operators/security.html).

In JupyterLab's file browser, open
`teaching/phys3810-fa2026/notebooks/intro/01_quantum_rng.ipynb`.
Choose **Kernel → Change Kernel → Python (PHYS 3810 Intro)**. Select the first
code cell under **1. Check the notebook environment** and press **Shift+Enter**.
Compare its **Interpreter:** path with the terminal path above: they must name
the same `.venv/bin/python`. A friendly kernel name alone is not proof.

A **kernel** is the running Python session behind the notebook. It remembers
variables and circuits. A **cell** is a small block of code or explanatory text.
Run code from top to bottom; `[*]` means it is still busy. A line starting with
`#` is a comment for the reader. A name such as `shots` stores a value that later
cells use. Your setup checkpoint is the correct interpreter and a successful
first cell; the video's student route does not require the maintainer test suite.

## 4. Run, change one value, and run it again

Read each short explanation, then use **Shift+Enter** on the following code
cell. The RNG notebook shows a simulated one-qubit measurement; the Bell
notebook shows a correlated two-qubit state. Both use `shots = 128` and
`seed = 2026`. Seeded laptop samples are classical simulation, not physical
quantum entropy or cryptographic randomness. Finite counts need not split evenly.

In **each notebook**, make the one advertised edit:

1. Under **2. Choose the shot count**, change `shots = 128` to `shots = 1024`
   and **run that parameter cell**.
2. Run the code under **4. Sample the circuit** (RNG) or **4. Sample the pair**
   (Bell), then **5. Plot the counts**. Read the current shot count in the output
   and plot title. If Bell's optional **7. Optional: change the measurement
   basis** is already displayed, rerun its code cell too.
3. Change `shots` back to `128`, **run the parameter cell again**, then run the
   same sampling and plotting cells. If you displayed Bell's optional
   **7. Optional: change the measurement basis**, rerun its code cell too.

Editing text alone does not change the kernel's remembered value or an existing
figure. The fixed preparation in section 3 does not depend on the shot count.
If anything looks stale, save your edit, restart the kernel, and run all cells
from the top. Open the Bell notebook in its own kernel and repeat the environment
check before starting it. The optional Bell extension can be skipped during
the video; the two main demonstrations are sufficient.

## 5. Optional exploration

Explore these later only if interested; there is nothing to submit:

- [Grover](../notebooks/01_grover.ipynb): amplify marked outcomes in a small
  search example on 2–5 qubits.
- [QFT](../notebooks/02_qft.ipynb): a quantum change of basis, shown exactly on
  1–6 qubits.
- [QPE](../notebooks/03_qpe.ipynb): estimate an eigenphase using controlled
  powers and an inverse QFT, with 1–6 counting qubits and one or two target qubits.
- [HHL](../notebooks/04_hhl.ipynb): a restricted positive Hermitian 2×2 system
  with exact integer eigenvalues 1–7; the output is a normalized, postselected
  solution state.
- [Shor](../notebooks/05_shor.ipynb): a compiled `N=15` example with four residue
  qubits and 4–6 counting qubits, followed by classical order and factor recovery.

These are bounded teaching examples, not general scalable implementations or
demonstrations of quantum advantage.

## 6. Save, stop, and recover

Save your local notebook with **Ctrl+S**; saving submits nothing. Finish with
**File → Shut Down** in JupyterLab and wait for the server to stop. Closing a
browser tab alone does not stop its kernel. To return later, open a terminal in
the same requirements folder and run:

```bash
source .venv/bin/activate
python -m jupyterlab
```

- **Missing variable or stale plot:** choose **Kernel → Restart Kernel**, then
  **Run → Run All Cells**. Restarting forgets values; running rebuilds them.
- **Wrong interpreter or missing import:** activate the intended `.venv`, repeat
  section 3's kernel registration, select it in the notebook, and compare paths.
- **Missing file:** check that the entire kit was extracted and the terminal is
  in the folder containing `requirements.txt`.
- **Install error, missing `venv`, or figure failure:** keep the error and ask
  for help. Do not skip failing cells or change the package pins.
- **Moved folder:** preserve your notebooks and recreate the environment in its
  new location with sections 2–3; a virtual environment is not portable.

For help, share the failing command, Ubuntu/Python versions, interpreter path,
and error text. Omit private account details and the token-bearing Jupyter URL.
Tool references: [Python environments](https://docs.python.org/3.12/library/venv.html)
and [IPython kernels](https://ipython.readthedocs.io/en/stable/install/kernel_install.html).
