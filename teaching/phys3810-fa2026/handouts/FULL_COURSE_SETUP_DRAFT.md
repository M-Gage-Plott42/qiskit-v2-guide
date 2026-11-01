# PHYS 3810: full-course Python and Qiskit setup

**Document v0.1 draft · proposed course version v0.2.0-rc1.**
This guide covers setup and five small quantum-algorithm lessons. The proposed
full-course download, `PHYS3810-Fall2026-v0.2.0-rc1.zip`, is **unpublished**;
there is no download link yet. Its planned extracted folder is `phys3810-fa2026`.
The existing Grover-only download and its setup guide do not contain this full
lesson set. Use the complete folder your instructor approves for these lessons.

These draft instructions use **64-bit CPython 3.12**, **Qiskit 2.6.1**, and
**Aer 0.17.2** on Linux. Package installation and browser notebook use have
passed on Ubuntu 26.04.1 LTS x86_64 with Python 3.12.15 and JupyterLab 4.6.4.
The exact new-folder commands below still await a complete walkthrough: the
observed browser run used a separately registered kernel. This remains a draft,
not a promise that every computer or setup path has been tested.

Native Windows x64, macOS ARM64/Intel, and VS Code/Cursor notebook setup are
**untested** for this course version. Windows ARM64 and 32-bit Python are outside
this draft's target. Ask the instructor which classroom setup to use if those
describe your computer. Session dates, in-class coverage, and
assignments are still to be confirmed. Git, IBM accounts, tokens, GPUs, and
quantum hardware are not needed for the local lessons.

## 1. Open the complete course folder

Once your instructor supplies the approved folder, extract it completely.
Keep its files together; individual downloaded notebooks cannot find the
shared course code on their own. Open a Linux terminal in the folder containing
`requirements.txt`, `constraints-ci.txt`, `src/`, `scripts/`, `tests/`, and
`teaching/`. This is the course root, not the `teaching/` subfolder.

For example, replace the quoted path with your actual folder:

```bash
cd "/path/to/phys3810-fa2026"
ls
python3.12 --version
```

Expected Python version: `Python 3.12.x`. If `python3.12` is missing, or this is
a managed computer, obtain the instructor-approved Python 3.12 installation
before continuing. These notes do not require changing system security policy
or installing packages into the operating system's Python.

Run the commands in this guide in the **terminal**, not at a Python `>>>` prompt
or inside a notebook cell. Installation needs internet access; the default
checks and demonstrations run locally after the packages are installed.

## 2. Create a separate Python environment

Create this environment once in your course folder:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
```

The version must be 3.12, and the printed interpreter must end in this course
folder's `.venv/bin/python`. An environment keeps these packages separate from
other Python projects. If `.venv` already belongs to a different project or
Python version, stop and ask for help before reusing it.

## 3. Install the specified packages and check the lessons

With `.venv` activated, run:

```bash
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
```

[requirements.txt](../../../requirements.txt) includes JupyterLab and the
libraries for circuits, plots, widgets, and notebook execution. It automatically
reads [constraints-ci.txt](../../../constraints-ci.txt) to select the specified
package versions. Keep both files together and use them unchanged. Do not
upgrade individual packages during the lessons.

The check prints your Python interpreter path and the expected Qiskit/Aer
versions, checks package consistency, runs **160 tests**, and executes **eight
notebooks** in separate fresh kernels. The current lesson set contains **50
nonempty code cells** and produces **16 PNG figures** during this full check.
Success ends with:

```text
PASSED: classroom validation
```

The message `SKIPPED: optional IBM Runtime and GPU execution` is expected;
those optional paths are not part of this setup check. A `FAILED` line or
traceback needs attention. Do not continue by skipping a failing code cell.
Executed copies are saved under `artifacts/executed-classroom/`; this command
does not overwrite the source notebooks.

## 4. Open JupyterLab and select the class kernel

Run these commands in the same activated terminal:

```bash
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
python -m jupyterlab
```

Keep the terminal open. If a browser does not open, use the local URL printed
by JupyterLab. Open
`teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb` in its file browser.

1. Choose **Kernel → Change Kernel → Python (PHYS 3810)**.
2. Choose **Kernel → Restart Kernel and Run All Cells**, and confirm the restart.
3. Compare the printed interpreter path with the terminal path from step 2.
   Both must point to the same course `.venv/bin/python`. A kernel's display
   name alone does not establish which Python it uses.
4. Check that all code cells finish without errors and that the preflight shows
   a circuit drawing and a measurement histogram. The notebook checks its
   own numerical results; sampled counts need not match another computer exactly.
5. Save the notebook with **File → Save Notebook**.

Open other lesson notebooks with the same registered Python environment, using
a separate kernel for each notebook. Start at the top and execute prerequisite
cells before later cells. If you change a parameter, rerun the calculations and
plots that depend on it. Restart/run-all is a useful check against accidentally
using a value left over from an earlier run.

Before a lesson, run all cells to check setup. During discussion, restart the
kernel and clear displayed outputs, make the requested predictions, then run
the relevant cells. The instructor will identify which exercises to discuss;
all required code still runs during the setup check.

## 5. Find the notebooks

The six course notebooks are under `teaching/phys3810-fa2026/notebooks/`:

- [00_setup_preflight.ipynb](../notebooks/00_setup_preflight.ipynb): verify the
  environment, a simple circuit, sampling, and figures.
- [01_grover.ipynb](../notebooks/01_grover.ipynb): phase marking and amplitude
  amplification for small searches on 2–5 qubits.
- [02_qft.ipynb](../notebooks/02_qft.ipynb): exact Fourier transforms on 1–6
  qubits, including complex phase and bit ordering.
- [03_qpe.ipynb](../notebooks/03_qpe.ipynb): phase estimation with 1–6 counting
  qubits and a unitary acting on one or two target qubits.
- [04_hhl.ipynb](../notebooks/04_hhl.ipynb): a 2x2 positive-Hermitian system
  with exact integer eigenvalues from 1 through 7; the result is a normalized
  solution state obtained by postselection, not a general linear-system solver.
- [05_shor.ipynb](../notebooks/05_shor.ipynb): a compiled example for N=15 with
  four residue qubits and 4–6 counting qubits, followed by classical order and
  factor recovery. It is not a scalable general factoring implementation.

Two additional checks are under the root `notebooks/` directory:

- [00_local_statevector_smoke.ipynb](../../../notebooks/00_local_statevector_smoke.ipynb):
  exact local simulation.
- [01_local_aer_smoke.ipynb](../../../notebooks/01_local_aer_smoke.ipynb):
  local Aer sampling and a small noise example.

The full check runs all eight notebooks. Their availability does not establish
which topics are taught in class or assigned for submission. Follow the
instructor's eventual lesson and assessment instructions.

## 6. Finish and return later

Save the notebooks you edited. In JupyterLab choose **File → Shut Down**, confirm,
and wait for the server-stopped message before closing the browser tab.
Closing a tab by itself does not stop its server or kernels.

Next time, reopen a terminal in the same course root:

```bash
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
python -m jupyterlab
```

Reopen preflight, select **Python (PHYS 3810)**, and restart/run all to confirm
the interpreter and figures. Installation and kernel registration normally
need doing only once for an environment that stays in the same location.
Keep your own edited notebooks separate from a fresh copy of the supplied files
so you can compare or restore the original exercises.

## If something fails

- **A file is missing:** check `pwd` and `ls`. Commands must run in the course
  root containing the complete folder, not inside the ZIP or `teaching/`.
- **Wrong Python or missing package:** print `sys.executable` again. Activate
  the course environment, or use `.venv/bin/python` instead of `python` in
  terminal commands. Check the notebook kernel separately.
- **The terminal check passes but a notebook fails:** select the class kernel,
  compare its interpreter path, restart it, and run all cells from the top.
- **The kernel is absent or points elsewhere:** run the registration command
  in step 4 from the intended activated environment, relaunch JupyterLab,
  and select it again. A correct-looking display name is not enough.
- **A plot or circuit drawing fails:** use the notebook's Python environment
  to rerun `python -m pip install -r requirements.txt`, then restart its kernel.
- **Installation fails, asks for a compiler, or `venv` cannot be created:**
  keep the error text and ask the instructor for the approved setup. Do not
  bypass the pinned versions or mix in another Qiskit installation.
- **The course folder or environment moved:** a virtual environment is not
  portable. Create a fresh environment at the new location, reinstall the
  specified packages, and register its kernel. Re-registering alone does not
  repair a moved environment; preserve your notebook work before making changes.

For help, provide the failing command, operating system, Python version,
printed interpreter path, and error text. Omit credentials, private account
details, other students' information, and the token-bearing JupyterLab URL.
