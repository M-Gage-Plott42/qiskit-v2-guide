# R1: fresh Linux environment validation

October 31, 2026. **R1 passed:** a newly created CPython 3.12 environment installed
the unchanged classroom pins and passed **160 tests, eight fresh-kernel notebooks,
50 nonempty code cells, and 16 PNGs**. This is fresh dependency-installation
evidence for the corrected revision, distinct from the earlier reused-environment
runs. No algorithm or dependency repair was needed.

## Snapshot and isolated locations

Validated source: `9e73b82aa578f0264afcbf7125631774afa3eb1c`, the committed
readiness-plan snapshot. Its runtime source is unchanged from the corrected
`ec07359` baseline. All **110 tracked files** were exported using `git archive`
into a new staging directory outside both checkouts, with no Git metadata,
virtual environment, or ignored working-tree content included in the export.
Each exported file was compared with the identified commit before execution.

Retained local paths:

- Staging: `/tmp/phys3810-r1-2026-10-31-gt5hru30/`.
- Source: `/tmp/phys3810-r1-2026-10-31-gt5hru30/source/`.
- Fresh environment: `/tmp/phys3810-r1-2026-10-31-gt5hru30/venv/`.
- Detailed evidence: `artifacts/r1-fresh-linux-2026-10-31/` in the integration
  worktree, including the export manifest, installation report, logs, installed
  package inventory, notebook checks, and preservation receipts.

This is internal validation staging, not a new student package or GPT Pro ZIP.
No existing review archive was replaced. The temporary staging is retained for
R2 but is not a durable backup; if removed, recreate it from the recorded commit
and pins. Do not move/reuse a virtual environment at a different path.

## Freshness, installation, and versions

The environment directory did not exist before creation. `python -m venv`
used an existing CPython **3.12.15** executable on the existing Linux host.
The initial environment contained only bootstrap **pip 25.0.1**. Its
`pyvenv.cfg` declares `include-system-site-packages = false`; `sys.prefix`
points to the new environment and differs from `sys.base_prefix`. User site
packages and inherited `PYTHONPATH`/`PYTHONHOME` were excluded.

The documented installer **pip 26.2.2** and unchanged `requirements.txt`
(which loads `constraints-ci.txt`) installed successfully. `requirements-ci.txt`
continues to include the same classroom requirements. Installation used official
PyPI with pip's cache disabled, no user pip configuration, and no inherited
pip configuration variables. A machine-readable `pip --report` records the
114 newly installed application distributions and their download provenance.
No installed application packages were copied from the old environment.

**115 distributions** are installed: **114 match their active constraints**,
plus the separately pinned pip 26.2.2 bootstrap tool. Names were normalized and
platform markers evaluated in the fresh interpreter. Unused optional/platform
constraints were not treated as requirements to install; IBM Runtime remains
absent. Full installed names, versions, and locations are recorded in
`environment-evidence.json` and `installed-packages.json` in the evidence folder.

Executed platform: Linux x86_64, kernel 7.0.0-42-generic, glibc **2.43**,
CPython **3.12.15**. Key packages: Qiskit **2.6.1**, Aer **0.17.2**,
NumPy **2.5.4**, nbclient **0.11.0**, nbformat **5.10.4**, ipykernel **7.4.0**,
Matplotlib **3.11.2**, JupyterLab **4.6.4**, and pip **26.2.2**.
This is not a new interpreter download, clean operating-system installation,
native Windows/macOS run, or interactive browser/editor test.

## Commands and interpreter binding

Commands ran from the isolated source directory. Here `python` means the new
`venv/bin/python`; no existing classroom environment was modified:

```bash
python -m pip install --upgrade pip==26.2.2
python -m pip install --report <local-evidence>/pip-install-report.json -r requirements.txt
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
bash scripts/smoke_local.sh
```

All commands **passed**. The standalone unittest run passed 160 tests, and the
strict validator independently reran those 160 tests before executing the eight
required notebooks. BLAS/OpenMP threads were limited to two. Configuration,
runtime, and plot-cache directories were isolated under the new staging area.
Bytecode writes were disabled to avoid incidental writes to shared interpreter
files or exported sources.

Application distribution locations and imported Qiskit/Aer/NumPy/notebook
modules resolve inside the fresh environment. HHL/Shor source imports resolve
inside the isolated export. The validator's temporary kernelspec binds every
notebook kernel to that new `sys.executable`. All six teaching notebooks also
print the new interpreter path. The two original smoke notebooks do not print
that path, so their interpreter evidence comes from kernel/executable resolution,
not a nonexistent output assertion.

For Bash smoke, the fresh `bin` directory was first on PATH, Jupyter user
configuration/data directories were isolated, and environment kernels were
preferred. Both `jupyter` and the resolved `python3` kernelspec executable point
to the new environment. Both smoke notebooks completed without errors.

Separate, existing Python 3.12 maintainer tools ran Ruff against the isolated
source: **passed**. `pre-commit run --all-files` ran in the integration worktree
because it requires Git metadata: **passed**, including the final evidence/docs
updates. This is explicitly a maintainer check, not an extra package installed
in the fresh classroom environment. No application check relied on that tool
interpreter or on imports from an original checkout.

## Notebook and source results

All eight required notebooks passed in fresh interpreter-bound kernels, with
consecutive execution counts and no retained errors:

- Preflight: four nonempty code cells, two PNGs.
- Local statevector smoke: three cells, no PNG requirement.
- Local Aer smoke: four cells, no PNG requirement.
- Grover: nine cells, three PNGs.
- QFT: seven cells, two PNGs.
- QPE: eight cells, three PNGs.
- HHL: seven cells, three required PNGs.
- Shor: eight cells, three required PNGs.

Total: **50 cells and 16 PNGs**. Notebook schema and source-output cleanliness
checks passed. All **110 exported file hashes and modes** still match the
pre-execution manifest. Executed copies and generated caches stay separate
from the source payload. The strict runner's skip/error/count checks and
partial-failure artifact behavior remain unchanged.

## Preservation and remaining gates

The original checkout's 87 recorded files/modes, HEAD, raw index, and
staged/unstaged/untracked status remain unchanged. Verified v0.2 PDFs, the
Grover rc1 tag and original assets, and both retained review ZIPs match their
receipts. Existing classroom/tool environments retain the same configuration,
interpreter identity, 115/15 installed distribution inventories, and 775/101
hashed distribution-metadata files. This checks configuration/package metadata,
not every byte of installed package code, caches, or the operating system.

Only status/evidence/context documents change in the integration worktree after
the tested source export. Algorithm source, contracts, tests, notebooks, pins,
workflows, existing PDFs, and archived review/release payloads are preserved.
No upstream refresh, push, PR, merge, publication, external message, new student
package, or hardware job occurred. Network activity was dependency installation.
Rick's reply remains pending.

**Skipped:** optional IBM Runtime/cloud and GPU. **Untested:** interactive
Jupyter/editor setup (R2), native Windows/macOS (R3), timed teaching, new matching
PDFs/student-package extraction, and remote CI for these local revisions. R1's
fresh install closes none of those separate gates.

**Next:** perform R2 of [RELEASE_READINESS_PLAN.md](RELEASE_READINESS_PLAN.md)
using the retained fresh source/environment where available: launch, select the
kernel, restart/run, inspect figures, and close/reopen through actual UI access.
Keep unavailable surfaces explicitly untested. **GPT Pro sync: not needed for
this unchanged-pin readiness check.** The next planned sync remains the matching
PDF/teaching checkpoint when its inputs stabilize; no manual code audit is needed.
