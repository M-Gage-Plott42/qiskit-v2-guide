# PHYS 3810: provisional public preview setup

<!-- markdownlint-disable-next-line MD036 -->
**Current publication instructions · Provisional course code v0.2.0-rc1**

Download the complete [provisional full-course preview](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-v0.2.0-rc1/PHYS3810-Fall2026-v0.2.0-rc1.zip) and extract its `phys3810-fa2026` folder. This named download is published. The earlier Grover-only package does not contain all five algorithm lessons. Final session dates and classroom emphasis remain to be confirmed. The beginner route uses worked demonstrations on laptops, with no assignments, grading, evaluation, or submissions.

For the newer beginner review kit, follow the [guided quickstart](guided/STUDENT_QUICKSTART.md).
Its three guided lessons begin with Python and Qiskit; its `--profile all`
validation includes eleven notebooks. The instructions below describe the
unchanged published full-course ZIP, which contains eight reference/validation
notebooks. Assisted setup must be arranged with the instructor; it is not
assumed independent homework or part of a fifteen-minute launch segment.

**Document note:** The [original companion](handouts/FULL_COURSE_SETUP_DRAFT.md) and [student PDF](handouts/PHYS3810_Full_Course_Student_Setup_v0.1_REVIEW_DRAFT.pdf) remain exact **prepublication review drafts** for reference. Their statement that the download is unpublished describes the review-time state and is outdated after this prerelease. This page and the [course landing page](README.md) govern current availability. See the [publication notice](handouts/PUBLICATION_NOTICE.md) and [document index](handouts/README.md).

These instructions use **64-bit Linux and CPython 3.12**, with Qiskit 2.6.1 and Aer 0.17.2. Recorded setup and browser checks passed on Ubuntu 26.04.1 LTS x86_64, Python 3.12.15, and JupyterLab 4.6.4, including a fresh application environment and the in-folder kernel setup below. The walkthrough used isolated Jupyter settings and a manually opened local URL; automatic browser opening was not checked.

Native Windows x64, macOS ARM64/Intel, and VS Code/Cursor notebook setup are **untested**. Windows ARM64 and 32-bit Python are outside this draft's target. Ask the instructor for an approved setup if needed. Git, IBM accounts, tokens, GPUs, and quantum hardware are not required.

For a current repository checkout, PR #117 uses Aer 0.18.2; see the
[checkout environment](ENVIRONMENT.md) and its separate validation record.
The published ZIP and accepted review kits described above keep their original
pins and supplied documents.

## 1. Open the complete course folder

Extract the approved folder completely and keep its files together. Individual downloaded notebooks cannot find the shared course code on their own. Open a Linux terminal in the folder containing `requirements.txt`, `constraints-ci.txt`, `src/`, `scripts/`, `tests/`, and `teaching/`. This is the **course root**, not the `teaching/` subfolder.

Replace the quoted path with your actual folder:

```bash
cd "/path/to/phys3810-fa2026"
ls
python3.12 --version
```

Expected: `Python 3.12.x`. If `python3.12` is missing, or this is a managed computer, obtain the instructor-approved Python 3.12 installation before continuing. Do not change system security policy or install the course packages into the operating system's Python.

Run this guide's commands in the **terminal**, not at a Python `>>>` prompt or in a notebook cell. Installation needs internet access; default checks and lessons run locally afterward.

## 2. Create a separate Python environment

Create the environment once in your course folder:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
```

The version must be 3.12 and the printed interpreter must end in this course folder's `.venv/bin/python`. This environment keeps the course packages separate from other projects. If `.venv` belongs to another project or Python version, ask for help before reusing it.

<!-- pagebreak -->

## 3. Install the specified packages and check the lessons

With `.venv` activated, run:

```bash
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
```

`requirements.txt` includes JupyterLab and the circuit, plotting, widget, and notebook-execution libraries. It automatically reads `constraints-ci.txt` to select the specified package versions. Keep both files unchanged; do not upgrade individual packages during the lessons.

In the frozen public release ZIP, the validator prints your interpreter path and expected Qiskit/Aer versions, checks package consistency, runs **160 tests**, and executes **eight notebooks in separate fresh kernels**, with **50 nonempty code cells** and **16 PNG figures**. In a newer repository checkout, it runs that checkout's complete test suite; default notebook membership remains eight, while `--profile all` also runs the three guided lessons. See [current evidence](STATUS.md) for measured revision totals. Success ends with:

```text
PASSED: classroom validation
```

`SKIPPED: optional IBM Runtime and GPU execution` is expected. A `FAILED` line or traceback needs attention; do not bypass a failing cell. Executed copies go to `artifacts/executed-classroom/`; source notebooks are not overwritten.

## 4. Open JupyterLab and select the class kernel

Run these commands in the same activated terminal:

```bash
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
python -m jupyterlab
```

Keep the terminal open. If the browser does not open, use the local URL printed by JupyterLab. In its file browser, open:

`teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb`

1. Choose **Kernel → Change Kernel → Python (PHYS 3810)**.
2. Choose **Kernel → Restart Kernel and Run All Cells**; confirm the restart.
3. Compare the notebook's printed interpreter with the terminal path from step 2. Both must point to the same course `.venv/bin/python`. A kernel's display name alone is not proof of its interpreter.
4. Check that every code cell finishes without errors and preflight shows a circuit drawing and measurement histogram. The notebook checks its numerical results; sampled counts need not match another computer exactly.
5. Save with **File → Save Notebook**.

Use the same registered environment for other lessons, with a separate kernel for each notebook. Start at the top. If you edit a parameter, execute that parameter cell itself with Shift+Enter, then rerun the calculations and plots that depend on it. Restart/run-all helps catch values left over from an earlier run.

<!-- pagebreak -->

## 5. Find the notebooks

These are paths **inside the complete course folder**, not online download links. The six course notebooks are under:

`teaching/phys3810-fa2026/notebooks/`

| Notebook | What it covers |
| --- | --- |
| `00_setup_preflight.ipynb` | Environment, a simple circuit, sampling, and figures. |
| `01_grover.ipynb` | Phase marking and amplitude amplification on 2–5 search qubits. |
| `02_qft.ipynb` | Exact Fourier transforms on 1–6 qubits, including complex phase and bit ordering. |
| `03_qpe.ipynb` | Phase estimation with 1–6 counting qubits and a unitary on **one or two target qubits**. |
| `04_hhl.ipynb` | A positive Hermitian 2×2 system with exact integer eigenvalues 1–7. The output is a normalized, postselected solution state; this is not a general linear-system solver. |
| `05_shor.ipynb` | A separate compiled **N=15** example with **four residue qubits** and 4–6 counting qubits, followed by classical order/factor recovery. It is not scalable general factoring. |

Two additional checks live under the root `notebooks/` directory:

| Notebook | What it checks |
| --- | --- |
| `00_local_statevector_smoke.ipynb` | Exact local simulation. |
| `01_local_aer_smoke.ipynb` | Local Aer sampling and a small noise example. |

The default validator runs these eight reference/validation notebooks. The newer guided route uses three additional notebooks; `--profile all` runs all eleven. Follow the instructor's selected route. There is no submitted or assessed work.

### Use predictions during the lessons

Before a lesson, run all cells to check setup. During discussion, restart the kernel and clear displayed outputs, make the requested predictions, then run the relevant cells. The instructor will identify which exercises to discuss. All required code still runs during the setup check.

The notebooks contain worked calculations, software assertions, and reference results. Use them openly during guided discussion; the assertions validate the material, not the student. Nothing is graded or submitted.

<!-- pagebreak -->

## 6. Finish and return later

Save the notebooks you edited. Choose **File → Shut Down** in JupyterLab, confirm, and wait for the server-stopped message before closing the browser tab. Closing a tab alone does not stop its server or kernels.

Next time, open a terminal in the same course root:

```bash
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
python -m jupyterlab
```

Reopen preflight, select **Python (PHYS 3810)**, and restart/run all to check the interpreter and figures. Installation and registration normally happen once for an environment that stays in the same location. Keep your edited notebooks separate from a fresh supplied copy so you can compare or restore the original exercises.

## If something fails

- **Missing file:** check `pwd` and `ls`. Work in the complete course root, not inside the ZIP or `teaching/`.
- **Wrong Python or missing package:** print `sys.executable` again. Activate the course environment, or use `.venv/bin/python` instead of `python` in terminal commands. Check the notebook kernel separately.
- **Terminal passes, notebook fails:** select the class kernel, compare interpreter paths, restart it, and run all cells from the top.
- **Kernel absent or points elsewhere:** repeat step 4's registration command in the intended activated environment, relaunch JupyterLab, and select the kernel again.
- **Plot or circuit drawing fails:** use the notebook's Python environment to rerun `python -m pip install -r requirements.txt`, then restart its kernel.
- **Installation asks for a compiler, fails, or cannot create `venv`:** save the error and ask for the approved setup. Do not bypass pins or mix in another Qiskit installation.
- **Folder or environment moved:** preserve your notebook work, then create a fresh environment at the new location, reinstall the specified packages, and register its kernel. Virtual environments are not portable; re-registering alone does not repair a moved environment.

For help, provide the failing command, operating system, Python version, interpreter path, and error text. Omit credentials, private account details, other students' information, and the token-bearing JupyterLab URL.

### Official reference links

- [Python 3.12 virtual environments](https://docs.python.org/3.12/library/venv.html)
- [IPython kernel registration](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)
- [Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)

These references explain the tools. Follow the course commands and pinned versions above for this draft.
