# One class: Qiskit setup and quantum demonstrations

Presented by **Gage Plott**. Follow the video on your laptop and
pause whenever you need more time. No Python experience is needed. Nothing
is assigned, graded, evaluated, or submitted.

Start with setup, then follow these notebooks with the video:

1. [Quantum random bits](../notebooks/intro/01_quantum_rng.ipynb).
2. [Prepare a Bell state](../notebooks/intro/02_bell_state.ipynb).
3. [QFT: phase patterns and bit order](../notebooks/02_qft.ipynb).
4. [QPE: estimating an eigenphase](../notebooks/03_qpe.ipynb).
5. [HHL: a restricted linear-system example](../notebooks/04_hhl.ipynb).

Grover and compiled N=15 Shor remain optional exploration. Use the same
**Python (PHYS 3810 Intro)** environment for all seven notebooks, including
those two optional references. Each open notebook has its own Python session;
run its initial setup/import cells and compare its printed interpreter path
with the setup terminal. A new environment is not needed for each notebook.

The setup chapter targets 15–20 minutes of video; installation and your pauses
may take longer. The video and matching kit will be shared through Canvas.
Use **Ubuntu/Linux, 64-bit CPython 3.12, and JupyterLab** for this route. Native
Windows/macOS and other notebook editors have not been validated for it.

## 1. Open the complete matching kit

Download the complete matching kit supplied with the video through Canvas.
Extract the whole ZIP before opening a notebook, and keep its folders together.
The older public full-course `v0.2.0-rc1` and guided `v0.2` ZIPs do **not** contain
this route. If the matching kit is missing, contact Gage using section 6.

Open a terminal in the folder containing `requirements.txt`, `constraints-ci.txt`,
`src/`, and `teaching/`. In the extracted kit, this is its **`runtime/`
folder**. In a repository checkout, it is the **repository root**. The following
blocks are terminal commands. A terminal is where you enter setup commands;
a notebook is where you run the lesson examples. Run each line and wait for it
to finish before entering the next. Installation needs internet; the lessons
then run locally without an IBM account or quantum hardware.

## 2. Check Python, then create the course environment

Python is the program that runs notebook code. First check the required version
and whether it is 64-bit:

```bash
python3.12 --version
python3.12 -c "import struct; print(struct.calcsize('P') * 8)"
```

Expect `Python 3.12.x` and `64`. These commands check an existing Python
installation; they do not install Python itself. If the command is missing or
either result differs, stop before installing packages and use section 6.
Python versions vary between Ubuntu releases. Keep the operating system's
Python intact. See the official [Ubuntu Python installation guide](https://ubuntu.com/developers/docs/howto/python-setup/).

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
unchanged. If this folder already has an environment from another kit, contact
Gage before reusing it. Installation errors should be resolved before continuing.

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
`seed = 2026`. A **shot** is one fresh preparation and measurement. The **seed**
makes the simulation repeatable. Seeded laptop samples are classical simulation, not physical
quantum entropy or cryptographic randomness. Finite counts need not split evenly.

In **each intro notebook (RNG and Bell)**, make the one advertised edit:

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
the video.

### Continue with QFT, QPE and HHL

Use the full reference notebooks linked above in that order; the earlier
guided QFT/QPE notebook is a separate historical route. Keep the defaults
for the first pass, run cells from top to bottom, and pause the video whenever
you need time. The extra prediction prompts and worked examples are optional
exploration, not assignments.

- **QFT** changes a state's phase pattern. Start from the supplied `"011"`
  label and watch the inverse transform recover it. Equal measurement
  probabilities do not mean equal complex amplitudes.
- **QPE** estimates a phase using a prepared target state and repeated
  controlled operations. It uses inverse QFT, but QFT alone is not the entire
  phase-estimation task. Read the supplied bit strings without reversing them.
- **HHL** prepares a solution state for the supplied small linear system.
  It keeps successful measurements and compares the result with a classical
  calculation. It does not return a complete classical solution vector from
  one measurement. Keep the supplied matrix and defaults for the first pass.

The notebooks retain the technical details and input limits: QFT uses 1–6
qubits; QPE uses 1–6 counting qubits and one/two target qubits; HHL supports
the stated positive Hermitian 2×2 family with exact integer eigenvalues 1–7.

## 5. Optional exploration

When a guide opens as Markdown source in JupyterLab, right-click its file and
choose **Open With → Markdown Preview** to use its links.

Explore these later only if interested; there is nothing to submit:

- [Grover](../notebooks/01_grover.ipynb): amplify marked outcomes in a small
  search example on 2–5 qubits.
- [Shor](../notebooks/05_shor.ipynb): a compiled `N=15` example with four residue
  qubits and 4–6 counting qubits, followed by classical order and factor recovery.

For additional worked examples after the video, return to
[QFT](../notebooks/02_qft.ipynb), [QPE](../notebooks/03_qpe.ipynb), or
[HHL](../notebooks/04_hhl.ipynb). Their main demonstrations are already in
the video route; further exploration is optional.

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

- **Python is missing, not 3.12, or not 64-bit:** stop before installing
  packages. Send Gage the two check results and your Ubuntu version so the
  setup matches your machine. Do not remove or replace system Python.
- **Missing `requirements.txt` or `.venv/bin/activate`:** extract the whole ZIP
  and open the terminal in `runtime/`, beside `requirements.txt`. If `.venv`
  was never created successfully, return to section 2. Do not run inside an
  unopened ZIP.
- **Installation error:** check the connection and folder. After an interrupted
  download, retry the same install command when connected again. For repeated
  errors or missing `venv` support, keep the error and contact Gage. Do not
  continue past a failed install or change the package pins.
- **Wrong kernel or missing import:** activate this kit's `.venv`, repeat
  section 3's kernel registration, select **Python (PHYS 3810 Intro)**, and
  compare interpreter paths. Different paths mean different Python environments.
  Keep the error if matching paths do not resolve it.
- **Missing variable, stale plot, or cells out of order:** save the intended
  edit, choose **Kernel → Restart Kernel**, then **Run → Run All Cells**.
  Restarting forgets values; running rebuilds them. Run All displays Bell
  section 7 too. Later shot edits need **2 → 4 → 5**, plus Bell **7** whenever
  already displayed.
- **Markdown symbols instead of usable links:** right-click the guide file in
  JupyterLab and choose **Open With → Markdown Preview**. For missing links or
  notebooks, check that the kit's folders are still together.
- **Moved kit or different operating system:** preserve your notebooks and
  contact Gage before reusing an environment. Virtual environments are not
  portable; these Ubuntu commands are not validated Windows/macOS instructions.

### Still stuck? Contact Gage

Email `gage-plott@utc.edu` with your operating system/version, Python version,
notebook filename and section, failing command or cell, exact error, and the
fix you tried. A clear, cropped screenshot can help. Omit token-bearing Jupyter
URLs, passwords, API keys, and unrelated account information. Pause and return
after the issue is resolved; nothing is submitted or graded.
Tool references: [Python environments](https://docs.python.org/3.12/library/venv.html)
and [IPython kernels](https://ipython.readthedocs.io/en/stable/install/kernel_install.html).
