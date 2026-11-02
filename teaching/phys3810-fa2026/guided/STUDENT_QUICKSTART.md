# Open, run, and change a quantum notebook

No programming experience is expected. These are complete examples to run with
your instructor, not assignments. Nothing is graded or submitted. Ask for help
whenever an instruction or result is unclear.

## Get a working environment with help

Ask your instructor which supported setup to use and when assisted setup will
be available. The demonstrated route is Ubuntu
Linux with 64-bit CPython 3.12 and JupyterLab. Windows, macOS, and native-editor
workflows have not been tested for this kit. Installation requires internet;
the examples run locally without an IBM account or quantum hardware.

Extract the **whole** review ZIP, keeping its folders together. Do not open a
notebook inside the compressed ZIP. The `runtime` folder holds the environment
requirements and runnable lessons. If a working environment is already provided,
skip installation with your instructor's help; do not create a second environment.

For assisted Ubuntu setup, open a **terminal** in the extracted kit folder.
The following are terminal commands, not Python notebook cells. Python 3.12
must already be available; ask for help if `python3.12` is not found.

```bash
cd runtime
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name phys3810-guided --display-name "Python (PHYS 3810 Guided)"
python -m jupyterlab
```

JupyterLab opens in a browser. If it does not, use the local link printed in
your terminal; do not share its token. Keep the terminal running while you work.

## Open the day's notebook

In JupyterLab's file browser, open
`teaching/phys3810-fa2026/notebooks/guided/`, then the day's file:

- `01_python_and_qiskit.ipynb` first.
- `02_grover_follow_along.ipynb` next.
- `03_qft_qpe_follow_along.ipynb` only if your instructor chooses the third day.

Select **Python (PHYS 3810 Guided)**, or the working kernel named by your
instructor. Day 1's first support cell prints its interpreter path; with the setup
above it should be inside `runtime/.venv`. Keep each notebook in its own kernel.

## Watch, run, change, discuss

Read the short explanation, select the next code cell, then press **Shift+Enter**
to run it. Work from top to bottom. `[*]` means the kernel is busy; wait for a
number before continuing. Text explanations are not terminal commands.

Only change the values explicitly marked **guided edit**. After changing a
parameter, rerun that cell and every following code cell in that example.
Changing text alone does not update a figure that is already displayed.
The notebook explains the expected observation before you compare outputs.

If variables are missing or results look stale, save your chosen edits, select
**Kernel > Restart Kernel**, then **Run > Run All Cells**. Restarting forgets
Python's variables; running from the top reconstructs them. If an error remains,
keep the error visible and ask the instructor rather than skipping the cell.

Use **File > Save Notebook** or **Ctrl+S** to keep your local copy. Saving does
not submit work. To return later, open a terminal in `runtime`, activate the
same environment, and launch JupyterLab again:

```bash
source .venv/bin/activate
python -m jupyterlab
```

Close a session using **File > Shut Down**, then reopen it when needed. If
setup consumes class time, the instructor will use the shorter Day 1 route or
a demonstration. Completing an installation is not a timed class promise.
