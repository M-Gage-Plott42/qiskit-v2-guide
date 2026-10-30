# PHYS 3810 · Python and Qiskit setup

**Draft for validation.** An early review-draft PDF can be prepared for feedback;
the final linked PDF follows setup validation on the intended classroom
platforms. Native Windows and macOS execution is not
yet validated for this milestone; see [STATUS.md](STATUS.md) for current
evidence. These instructions use **64-bit CPython 3.12**, **Qiskit 2.6.1**, and
**Aer 0.17.2**. IBM accounts, tokens, GPUs, and Git are not needed.

## 1. Get the course folder and Python 3.12

Download [PHYS3810-Grover-v0.1.0-rc1.zip](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip)
from the versioned course prerelease; the link activates when publication
completes. Use this named asset instead of GitHub's automatic source archive.
Extract it and open a terminal in `phys3810-grover`: it must contain
`requirements.txt`, `scripts/`, and `teaching/`.
For example, use `cd "path/to/extracted-folder"`, replacing the quoted path.
Run commands in the terminal, not inside a Python prompt or notebook cell.

First check for Python 3.12 using your platform's command:

- Windows PowerShell: `py -3.12 --version`.
- macOS/Linux terminal: `python3.12 --version`.

Expected: `Python 3.12.x`. If it is missing, Windows users can install the
[official Python install manager](https://docs.python.org/3/using/windows.html)
and run `py install 3.12`, then reopen PowerShell. On macOS/Linux, use a
Python 3.12 installation provided by your instructor or operating-system
package manager. An optional alternative is to
[install uv](https://docs.astral.sh/uv/getting-started/installation/) and follow
its [Python installation guide](https://docs.astral.sh/uv/guides/install-python/):

```bash
uv python install 3.12
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
```

That alternative already creates and activates the environment; continue at
step 3. If a managed computer blocks installation, ask the instructor for the
approved Python 3.12 setup.

## 2. Create a separate environment

An environment keeps the class packages separate from other Python projects.
Create it once in the extracted repository folder.

**Windows PowerShell:**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

If PowerShell blocks activation, leave its policy unchanged and use
`.\.venv\Scripts\python.exe` in place of every `python` command below.
For example: `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.
On macOS/Linux, `.venv/bin/python` is the equivalent direct path.

## 3. Install and check

In the activated environment, run:

```bash
python --version
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
```

The [requirements](../../requirements.txt) include JupyterLab, notebook
execution tools, widgets, and circuit/plot dependencies. Their complete pinned
resolution is in [constraints-ci.txt](../../constraints-ci.txt), which pip
reads automatically. Use these files together; do not upgrade individual class
packages during the labs.

The validator prints your interpreter path, Python `3.12.x`, `qiskit: 2.6.1`,
and `qiskit-aer: 0.17.2`. It checks dependencies, runs offline tests, and
executes preflight, the two local smoke notebooks, and the Grover lesson in
fresh kernels.
Success ends with:

```text
PASSED: classroom validation
```

`SKIPPED` for optional IBM Runtime/GPU execution and `UNTESTED` for QFT, QPE,
HHL, and Shor are expected and are not claims that those paths
passed. A `FAILED` line or traceback needs attention. Executed notebook copies
are saved under `artifacts/executed-classroom/`; source notebooks stay unchanged.

## 4. Open JupyterLab and choose the kernel

Run these commands in the same terminal:

```bash
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
python -m jupyterlab
```

Keep the terminal open. If a browser does not open, use the local URL printed by
JupyterLab. In its file browser, open
`teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb`.
Choose **Kernel → Change Kernel → Python (PHYS 3810)**, then
**Kernel → Restart Kernel and Run All Cells**. The first cell prints the
interpreter path; it should point inside this repository's `.venv`.

In VS Code/Cursor, select the project interpreter before choosing the notebook
kernel: **Python: Select Interpreter**, then `.venv\Scripts\python.exe` on
Windows or `.venv/bin/python` on macOS/Linux. Use that environment in the
notebook's kernel picker too; the editor interpreter and notebook kernel can
be different.

Expect Bell probabilities `[0.5 0.  0.  0.5]`, 1024 measurements split roughly
equally between `00` and `11`, a circuit drawing, a histogram, and `PASSED`
messages. Exact counts can differ between computers. The notebook asserts
the amplitudes, probabilities, correlation, shot total, and allowed outcomes.

For later sessions, reopen a terminal in the same folder, activate `.venv`
again, and run `python -m jupyterlab`. Installation and kernel registration
normally need doing only once for that environment.

Before class, run all cells to verify setup. During class, restart the kernel
and clear outputs, discuss each prediction, then run its code cell so results
do not appear before the discussion.

After preflight, open `teaching/phys3810-fa2026/notebooks/01_grover.ipynb` using
the same kernel. Expect exact probability checks, a circuit, sampled counts,
and an iteration-probability plot. The 75-minute expansion exercises also run
during validation; optional discussion time does not mean skipped code cells.

## Focused troubleshooting

- **Cannot find `requirements.txt` or the validator:** change to the extracted
  repository root, not `teaching/` or the ZIP file. Check with `dir` on Windows
  or `ls` on macOS/Linux.
- **Wrong Python version or package not found:** run
  `python -c "import sys; print(sys.executable)"`. It must point into `.venv`.
  Activate the environment or use its direct Python path. If `.venv` was
  created with another Python version, create a new environment with 3.12.
- **Terminal validation passes but the notebook fails:** choose the registered
  class kernel and restart it. Compare the notebook's interpreter path with
  the terminal path. Register the kernel again if you moved or recreated
  the environment.
- **`python3.12` or `py` is not found:** complete step 1 and reopen the terminal.
  For a Linux `venv`/`ensurepip` error, install your distribution's matching
  Python 3.12 venv package or use the documented uv alternative.
- **Installation fails or asks for a compiler:** check Python 3.12, 64-bit
  architecture, internet access, and the exact error. Keep the pinned package
  versions and bring the error to the instructor; do not mix in another Qiskit
  installation to bypass it.
- **Plot or circuit drawing fails:** rerun the requirements installation using
  the notebook environment's Python, then restart the kernel and run all cells.
  The preflight checks the required rendering dependencies.

For help, share the failing command, OS, Python version, and error text with the
instructor. Do not include credentials or private account/student information.
The approach follows [IBM's Qiskit installation guidance](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
and the [Qiskit 2.6.1 package release](https://pypi.org/project/qiskit/2.6.1/).
