# Python and Qiskit setup

PHYS 3810 | Grover code v0.1.0-rc1 | Document review draft v0.2 | October 29, 2026

Prepared by Matthew Gage Plott, PhD. This Markdown companion retains the
instructions in the [received student PDF](../handouts/PHYS3810_Student_Setup_Grover_RC1_v0.2.pdf).
The PDF is a local draft pending publication; its receipt is recorded separately.

Download the named [PHYS3810-Grover-v0.1.0-rc1.zip asset](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip).
GitHub's automatic source archive has a different folder layout. Document v0.2
does not change the rc1 code or replace its original ZIP.

Use **64-bit CPython 3.12**, **Qiskit 2.6.1**, and **Aer 0.17.2**. You need internet access to install packages. The class notebooks then run locally without Git, an IBM account, credentials, or a GPU. Native Windows/macOS execution is not yet validated; this is a review draft, not a final platform guarantee.

## 1. Get the folder and Python 3.12

Obtain the instructor-supplied standalone ZIP and extract the entire archive. Open a terminal in its **phys3810-grover** folder. It must contain `requirements.txt`, `scripts/`, `src/`, `tests/`, and `teaching/`. Keep those folders together. Enter commands in the terminal, not in a Python prompt or notebook cell.

**Windows:** check `py -3.12 --version`. If it is missing, install the [official Python install manager](https://docs.python.org/3/using/windows.html), run the command below, and reopen PowerShell.

```powershell
pymanager install 3.12
py -3.12 --version
```

**Linux/macOS:** check `python3.12 --version`. Use an instructor-provided installation or your platform's approved Python 3.12 package. The expected output is `Python 3.12.x`, not another minor version.

## 2. Create a separate environment

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

**Alternative for Linux/macOS without Python 3.12:** [install uv](https://docs.astral.sh/uv/getting-started/installation/), then use its [Python installation workflow](https://docs.astral.sh/uv/guides/install-python/):

```bash
uv python install 3.12
uv venv --python 3.12 --seed .venv
source .venv/bin/activate
```

That alternative already creates the environment; continue to step 3. If PowerShell blocks activation, leave its policy unchanged and replace every `python` below with `.\.venv\Scripts\python.exe`. The Linux/macOS equivalent is `.venv/bin/python`.

<!-- pagebreak -->

## Install, validate, and select the kernel

Review draft v0.2 | Continue in the extracted phys3810-grover folder

## 3. Install the pinned packages

With the environment active, run:

```bash
python --version
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
```

The requirements automatically use `constraints-ci.txt` and include notebook, circuit-drawing, and plotting dependencies. Keep both files together; do not upgrade individual class packages during the lab.

**Expected verification:** Python `3.12.x`, Qiskit `2.6.1`, Aer `0.17.2`, 50 passing tests, and four required notebooks executed in fresh kernels. Successful validation ends with:

```text
PASSED: classroom validation
```

`SKIPPED` for optional IBM Runtime/GPU paths and `UNTESTED` for QFT, QPE, HHL, and Shor are expected in this Grover-only preview. Those messages do not claim those paths passed. A `FAILED` line or traceback needs attention. Executed copies are saved in `artifacts/executed-classroom/`.

## 4. Open JupyterLab

Register the class kernel once, then start JupyterLab:

```bash
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
python -m jupyterlab
```

Keep the terminal open. If a browser does not open, use the local URL JupyterLab prints. In its file browser, open:

```text
teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb
teaching/phys3810-fa2026/notebooks/01_grover.ipynb
```

Choose **Kernel > Change Kernel > Python (PHYS 3810)**. The notebook's interpreter path should point inside this folder's `.venv`. In VS Code/Cursor, also select that `.venv` in **Python: Select Interpreter** and in the notebook kernel picker; those selections can differ.

## 5. Use the notebook in two modes

- **Before class:** restart the kernel and run all cells to verify installation. Expect preflight checks and two figures; Grover adds a circuit, a sampled histogram, and an iteration-probability curve.
- **During class:** restart the kernel and clear outputs. Discuss each prediction before executing its cell. Avoid revealing every answer with Run All at the start of the lesson.

<!-- pagebreak -->

## Return to the lab and resolve common problems

Review draft v0.2 | Retain the same extracted course folder

## Reopen the environment later

Open a terminal in `phys3810-grover` and launch JupyterLab with the environment's
interpreter. This route needs no activation or reinstall. You normally do not
repeat kernel registration for the same environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab
```

Linux/macOS:

```bash
.venv/bin/python -m jupyterlab
```

## Focused troubleshooting

- **Cannot find requirements or the validator:** change to the extracted folder containing `requirements.txt`, not the ZIP itself or the `teaching` subfolder. Check with `dir` on Windows or `ls` on Linux/macOS.
- **Wrong version or missing package:** run `python -c "import sys; print(sys.executable)"`. It should point into `.venv`. Activate it or use its direct Python path. Recreate an environment made with the wrong Python minor version.
- **Terminal validation passes but the notebook fails:** choose the class kernel and restart. Compare notebook and terminal interpreter paths; also check the editor's notebook kernel picker.
- **Course folder or environment was moved:** recreate `.venv` in its new location with Python 3.12, reinstall the pinned requirements, then register the class kernel again. Re-registering alone does not repair a moved environment, including when its parent folder moved. Repeat steps 2-4 for the new environment.
- **Python or venv is missing:** complete step 1 and reopen the terminal. For Linux `venv` or `ensurepip` errors, use the matching Python 3.12 venv package or the documented uv alternative.
- **Installation requests a compiler or cannot resolve packages:** check Python 3.12, 64-bit architecture, internet access, and the exact error. Retain the pins and ask the instructor for the approved setup.
- **A plot or circuit fails:** install requirements using the notebook environment's Python, restart the kernel, and run all cells. The validator checks actual embedded figures, not only imports.

## What to report to the instructor

Provide your OS, Python version, failing command or cell, and error text. Do not include credentials, private account details, or student information. Setup problems should be resolved before the teaching session; the five-minute readiness segment cannot absorb installation work.

## Primary references

- [Python virtual environments](https://docs.python.org/3.12/library/venv.html).
- [Python on Windows](https://docs.python.org/3/using/windows.html).
- [IBM Qiskit installation guidance](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit).
- [Qiskit 2.6.1 release metadata](https://pypi.org/project/qiskit/2.6.1/).

The independent review reports 50 tests/four notebooks passing on Linux
CPython 3.12.14 in a reused pinned environment. Native Windows/macOS,
interactive UI, hardware/GPU, and live classroom pacing remain unvalidated.
