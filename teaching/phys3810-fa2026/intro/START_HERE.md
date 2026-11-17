# One class: Qiskit setup and quantum demonstrations

Presented by **Gage Plott**. Follow the prerecorded video on your laptop and
pause whenever you need more time. No Python experience is assumed. Nothing
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

Use the complete single-class kit supplied with the video and extract it before
opening a notebook. Keep all its folders together. The older full-course
`v0.2.0-rc1` and guided `v0.2` ZIPs do **not** contain the RNG/Bell lessons. A new
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

- **QFT** changes the basis of a quantum state, exactly on 1–6 qubits here.
  The example starts from a known label and shows its complex phase pattern
  and inverse recovery.
- **QPE** uses a prepared eigenstate and controlled powers to estimate an
  eigenphase. It uses inverse QFT, but QFT by itself does not estimate an
  unknown eigenphase. This helper supports 1–6 counting qubits and one or
  two target qubits.
- **HHL** demonstrates a restricted positive Hermitian 2×2 system with exact
  integer eigenvalues 1–7. Its output is a normalized solution state after
  selecting successful measurements, not a classical list of solution values.

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
