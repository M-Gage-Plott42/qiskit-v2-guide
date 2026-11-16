# Single-class candidate validation

November 16, 2026. The new route is one prerecorded class presented by Gage
Plott: setup, quantum RNG, Bell-state preparation, and optional algorithm
exploration. The [quickstart](intro/START_HERE.md) is the student entrance.
This record concerns immutable local candidate
`754ec33d620033faf1d2f3754cba811e04d22ad5`, based on
`1f33830674490ecbe411cb9a8e86ca52abf7cae8`; it is not a publication, final
classroom approval, or a new acceptance claim for historical archives.

## Implementation and regression scope

The two intro notebooks have independent environment/import cells, direct
`h(0)` and `cx(0, 1)` construction, separate measured copies, explicit register
mapping, local V2 sampling, circuit figures, and count histograms. Defaults are
`shots = 128` and `seed = 2026`. RNG uses actual ordered `get_bitstrings()`
samples. Bell includes the optional prewritten X-basis comparison.

Fifteen new actual-cell regression tests check independent amplitudes,
normalization, probabilities, Bell relative phase/marginals, asymmetric
`X(q0) → 01` and `X(q1) → 10` calibration through the sampling cell, exact
count totals/support/width, `shots=1`, ordered-sample aggregation, and repeated
construction without accumulating gates/measurements. They exercise
128 → 1024 → 128 and verify captions, plot titles, and bar heights. Persistent
namespaces demonstrate that a source edit alone leaves the old runtime value,
then verify the corrected parameter-first execution sequence and reversal.
Independent NumPy H-tensor-H expectations distinguish the Bell state from a
classical mixture; a relative-sign negative control preserves Z probabilities
while failing the expected X-basis result.

The default inventory remains eight notebooks. The all profile retains those
and the three earlier guided notebooks, adding both intro lessons. Strict
fresh-kernel regressions cover execution counts, retained errors, deliberate
errors tagged `raises-exception`, forbidden `skip-execution`, missing figures,
and preserved partial output on failure. Optional-in-the-video X-basis code
still executes during acceptance. The existing exporter derives its inventory
from its matched validator, uses a new single-class identity, and preserves
the notebook quickstart/menu anchors in the standalone layout.

Internal integration review corrected the quickstart to rerun an already
displayed Bell X-basis cell after either shot-count edit. This is internal
review, not independent external acceptance.

## Checkout execution

**Passed:** 221 tests, 13 independently started notebook kernels, 85 nonempty
code cells, and 32 PNG outputs. The two intro notebooks contribute 11 cells and
5 PNGs. Every required code cell has an execution count and no error output.
Source notebooks retain empty outputs and null counts.

The application environment was installed **fresh** in
`artifacts/single-class-2026-11-16/venv` from unchanged requirements/constraints,
using the pre-existing 64-bit CPython **3.12.15** interpreter. This is not a
fresh Python-interpreter installation. Host: **Ubuntu 26.04.1 LTS x86_64**,
Linux **7.0.0-43-generic**, glibc **2.43**. All 114 installed application
distributions match their active constraint pins; pip is separately 26.2.2.

Installed direct versions include Qiskit **2.6.1**, Aer **0.18.2**, JupyterLab
**4.6.5**, ipykernel **7.4.0**, ipywidgets **8.1.9**, and python-dotenv **1.2.4**.
The existing main `.venv` was preserved. Maintainer tools are a separate reused
Python 3.12 environment: Ruff **0.15.22**, pre-commit **4.7.0**, and the pinned
Markdown/YAML hook versions.

Commands, run from the repository root with the selected environment on PATH:

```bash
python scripts/validate_classroom.py --profile all
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh artifacts/single-class-2026-11-16/smoke
pre-commit run --all-files
```

The first command includes `pip check` and the full unit suite; no immediate
duplicate unittest-discovery run was used. Ruff ran through the separate tool
environment. Matplotlib/IPython and hook/npm caches were directed to task-local
directories. Initial pre-commit hook installation **failed** because the default
npm cache was read-only; rerunning with a workspace npm cache **passed** all
three hooks. The initial log remains preserved, not relabeled a pass.

The local Bash smoke run **passed** both smoke notebooks; Ruff **passed** the
full requested paths. After the first source pass, visual inspection exposed
tiny floating-point values in the optional Bell probability display. Display
rounding now makes zero readable while calculations keep full precision. The
all-profile gate reran and **passed** for that source change; the earlier successful log is
retained separately rather than counted as additional independent evidence.

Local evidence is under `artifacts/single-class-2026-11-16/`: installation logs,
environment inventory, pin comparison, validator log, per-notebook execution
counts/hashes, smoke output, and hook logs. Executed source copies are under
`artifacts/executed-classroom/`; pre-existing outputs were preserved separately.
The earlier 205/11/74/27 results retain their original sources and environments.

## Rendering and exact delivery

**Passed:** complete HTML/PNG visual inspection and corroborative OCR of the
current quickstart and both executed intro notebooks, including all five new
figures. Seven overlapping screenshot tiles cover all content (2 quickstart,
2 RNG, 3 Bell). Google Chrome **157.0.8103.78** rendered at 2× scale; Tesseract
**5.5.0** OCR token recall against rendered text was 99.45%, 96.78%, and 97.98%,
respectively. Code, math, and bit-label OCR substitutions were resolved through
source/visual comparison and actual-cell checks. This is corroborative evidence,
not mathematical proof or an interactive UI/recording-size test. No PDF or Word
document was produced or modified.

The existing builder exported:

- ZIP: `PHYS3810-Single-Class-Review-v0.1-754ec33d6200.zip`.
- Source commit: `754ec33d620033faf1d2f3754cba811e04d22ad5`.
- Source tree: `77f27bee186493cae493e0ed2e81ba004b1af4a2`.
- Size: **179,296 bytes**; **56 files / 55 manifest entries**.
- ZIP SHA-256: `477e7a8aced1cd516f90714437137bfcc06ad2edd2b7660d4cc80e75c0b47274`.
- Manifest SHA-256: `c2c15bfd5f4f51302b57f75c80a288069d281bfc74736124efe142079529bb1f`.
- Relative navigation: **49 checked links**.

**Passed separately:** extract outside the checkout into
`/tmp/PHYS3810 single class 754ec33/phys3810-single-class-review`, then run the
quickstart's Python/64-bit checks, create `runtime/.venv`, install pip 26.2.2 and
`requirements.txt`, and register `phys3810-intro` with `--sys-prefix`. This second
application environment is **fresh**, using the same pre-existing CPython
3.12.15 interpreter. Its 114 application distributions match the current pins.

From that extraction's `runtime/`, with its own interpreter and no inherited
`PYTHONPATH`, `python scripts/validate_classroom.py --profile all` **passed 221
tests / 13 notebooks / 85 code cells / 32 PNGs**. Every required code cell
executed without error. All canonical algorithm imports resolve inside the
extracted `runtime/src/`. All 55 payload hashes and modes match before and after
execution; the manifest is unchanged. The ZIP was then copied to the Ubuntu
desktop and byte/hash-verified. The sealed archive has no prompts, policy/chat
documents, private correspondence, old PDFs/Word files, caches, or executed output.
Source execution evidence inside it is explicitly separate from this later
extraction receipt.

The complete local delivery receipt is
`artifacts/single-class-2026-11-16/extraction-receipt.json`; full extraction logs
and copied executed outputs remain in that ignored task directory. Historical
archives were not overwritten or relabeled.

## Jupyter startup and UI boundary

**Passed:** JupyterLab starts from the extracted `.venv`, with authentication
enabled and loopback binding. Authenticated local requests return HTTP 200 for
`/lab`, `/api/status`, and `/api/kernelspecs`. The named **Python (PHYS 3810
Intro)** kernel resolves to the extraction's exact `.venv/bin/python`. The test
server shut down successfully through its authenticated local API.

For this check, `python -m jupyterlab` used `--no-browser --ip=127.0.0.1
--port=8879 --ServerApp.port_retries=0` and task-local Jupyter/IPython/Matplotlib
directories. These are disclosed test adaptations, not extra student commands.
**Untested:** actual interactive browser selection/execution, automatic browser
opening, and UI shutdown/reopening. The computer-use inventory reported that
the browser access host was unavailable; native application control is also
unavailable. API readiness and headless notebook execution do not close that
UI gap. Private server tokens are omitted from shareable evidence.

## Limits and next review

**Skipped:** optional IBM Runtime, GPU, hardware execution, remote CI, and any
release/push/PR/merge; this task is local and credential-free. No dependency,
algorithm, supported-family, historical lesson, or supplied document-byte
changes were made. **Untested:** native Windows/macOS/editor paths, fresh Python
installation on a new computer, recording/audio/video export, and human pacing.

Ubuntu/Linux is confirmed for recording. The current host begins with Python
3.12 available; the guide calls for assisted setup if that prerequisite is
missing rather than silently substituting a different Ubuntu default Python.
[Recording research](SINGLE_CLASS_RECORDING_NOTES.md) separates documented
ONLYOFFICE slide-video export from an unverified live screen/audio workflow and
identifies an Ubuntu recording pilot still needed.

Only the supplied sync text was accessible. The linked eight-page Word script
and fuller text handoff were not delivered as accessible files and were not
read or modified here. The next review is due for beginner usability and
alignment of narration, setup commands, stable cell IDs, edits, and figures
with the tested candidate. Total class window and delivery destination remain
open; no grading or submission decision is reopened.
