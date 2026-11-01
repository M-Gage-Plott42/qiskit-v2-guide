# R6: Ubuntu student-guide walkthrough

Executed October 31, 2026. **The student guide's Ubuntu setup route passed:**
a fresh in-project `.venv`, unchanged pinned installation, the full classroom
validator, ordinary `--sys-prefix` kernel registration, and actual JupyterLab
execution/save/return actions. All eight required notebooks ran through the UI
with the explicitly selected class kernel, and all 16 figures were inspected.
This closes the conventional environment/kernel-path gap left by R2 for this
observed Ubuntu configuration, not the remaining native-platform/editor,
teaching, PDF, package, or publication gates.

The [student setup draft](handouts/FULL_COURSE_SETUP_DRAFT.md) and
[instructor companion](instructor/FULL_COURSE_INSTRUCTOR_DRAFT.md) remain
provisional inputs under [R6_DOCUMENT_INPUTS.md](R6_DOCUMENT_INPUTS.md).
Rick's reply and actual human pacing remain pending.

## Source and guide actually exercised

- Source commit: `7b8a8e2ed74bbcd7ceea27cd377fd73802d4927a`.
- Source tree: `583938d066b6f51b6ac4abd004b6f8da06191d58`.
- Guide path: `teaching/phys3810-fa2026/handouts/FULL_COURSE_SETUP_DRAFT.md`.
- Tested guide SHA-256:
  `94b1a1000ee0c2b694d08a17a41f0186747a14986d9bba0df57da9cc5bc98451`.
- Isolated working root:
  `/tmp/phys3810-r6-guide-2026-10-31-qwwuuf8b/phys3810-fa2026`.
- New interpreter: that root's `.venv/bin/python`.

An identified Git export supplied all 123 tracked files outside the original,
accepted integration, and candidate checkouts. It is an internal source working
copy, not a downloaded student archive. Its file hashes/modes were recorded
before installation. All 123 remained unchanged after the validator and before
interactive execution. No unpublished release URL, ZIP extraction, Python/OS installer
download, or future full-course asset was tested by this export.

Any later evidence wording added to the guide is separate from the exact tested
hash above. A change to installation commands or required runtime content must
be assessed and checked again; a status update must not be represented as a
fresh execution of different commands.

## Fresh installation and exact commands

The host was Ubuntu 26.04.1 LTS x86_64, Linux 7.0.0-42-generic, glibc 2.43.
`python3.12` already resolved through `/home/gage/.local/bin/python3.12` to
CPython **3.12.15**. This is a fresh application environment on an existing OS
and interpreter, not a new OS/Python installation. The guide's prerequisite
was present; no alternative interpreter instruction or package-pin repair was
needed.

Each Bash command ran in the isolated course root. The guide's example folder
placeholder was replaced with that real working directory. Shells used
`bash --noprofile --norc -e -c`; activation was repeated in subsequent shells
so every command selected the new environment. The substantive guide commands
were unchanged:

```bash
ls
python3.12 --version
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
python -m jupyterlab
```

Before installing dependencies, a supplemental `python -m pip list --format=json`
showed **only bootstrap pip 25.0.1**. The new environment excludes system and
user site packages; all installed application distributions resolve inside its
`.venv`. Pip was upgraded to the documented 26.2.2. The unchanged
`requirements.txt` automatically read the unchanged `constraints-ci.txt`.

The installed inventory contains **115 distributions**: all 114 installed
application versions match their active constraint entries, plus pip 26.2.2.
Optional Runtime was not installed. Key versions are Qiskit 2.6.1, Aer 0.17.2,
NumPy 2.5.4, Matplotlib 3.11.2, JupyterLab 4.6.4, ipykernel 7.4.0,
nbclient 0.11.0, nbformat 5.10.4, and nbconvert 7.17.2. The receipt retains
the full inventory and platform-marker evaluation rather than assuming another
OS would install the same distribution count.

The install/check receipt records exit 0 for environment creation, activation/
interpreter verification, bootstrap pip, requirements, the classroom validator,
and class-kernel registration. These commands were actually executed; no
previous environment's result was relabeled as this fresh installation.

## Configuration isolation and kernelspec

To preserve existing user settings and R1/R2 staging, IPython, Jupyter config/
data/runtime, Lab settings/workspaces, Matplotlib, and pip-cache directories
were placed under the new staging parent. Python bytecode writes and user site
packages were disabled, Matplotlib used Agg, and OpenMP/OpenBLAS were limited
to two threads. The new environment still follows the guide's in-project
`.venv` placement.

Task-local Jupyter configuration bound the server to authenticated loopback
`127.0.0.1`, selected port 8891 with ordinary port retries, and suppressed
automatic browser opening. The printed local URL was opened manually in Chrome.
These preservation/launch adaptations are explicit: the result does not certify
an arbitrary user's existing Jupyter configuration or automatic browser launch.
Authentication was not disabled, and no public server was exposed.

The **ordinary `--sys-prefix` command** wrote
`.venv/share/jupyter/kernels/phys3810-fa2026/kernel.json`. Its argv points exactly
to the new working root's `.venv/bin/python`, and its display name is
**Python (PHYS 3810)**. Unlike R2, this test did not substitute `--user` or an
external kernelspec for that registration. The parent environment and old named
kernel registrations were not changed.

## Validator and saved-output evidence

**Passed:** dependency consistency, all **160 tests**, and eight independent
fresh-kernel notebook executions selected by the Python validator. Saved-output
inspection independently confirmed consecutive counts from one, every required
nonempty cell executed, no retained error output, unchanged source cells, and
the following totals:

- Preflight: 4 code cells, 2 PNGs.
- Local statevector smoke: 3 code cells, no PNG requirement.
- Local Aer smoke: 4 code cells, no PNG requirement.
- Grover: 9 code cells, 3 PNGs.
- QFT: 7 code cells, 2 PNGs.
- QPE: 8 code cells, 3 PNGs.
- HHL: 7 code cells, 3 PNGs.
- Compiled Shor: 8 code cells, 3 PNGs.

Total: **eight notebooks, 50 code cells, 16 PNGs**. HHL/Shor each produced all
three required figures. Executed validator copies are under the isolated root's
`artifacts/executed-classroom/`. Optional Runtime/GPU execution was explicitly
**skipped**, not passed. This execution does not submit IBM jobs or certify
hardware access.

Supplemental required checks also passed in the new environment:

```bash
python -m pip check
python -m unittest discover -s tests -v
bash scripts/smoke_local.sh
```

The standalone unit invocation again ran the same 160 tests; it does not make
320 distinct regressions. The Bash smoke run is additional execution of the two
already counted smoke notebook names. Ruff passed using the existing separate
maintainer environment. Final pre-commit passed (Ruff, yamllint, markdownlint),
along with all 379 local file links and eight Bash syntax blocks in the changed
documents. The updated student guide's executable blocks exactly match the
tested guide. The completion receipt records the final local commit and clean
candidate state; these documentation checks do not substitute for installation
or actual UI execution.

## Actual JupyterLab coverage

Chrome's connected browser surface was used; no notebook-server API or headless
runner was substituted for these UI actions. JupyterLab's About dialog showed
**4.6.4**. The assistant navigated the file browser to preflight, followed
**Kernel → Change Kernel → Python (PHYS 3810)**, restarted/ran all cells, inspected
results, and saved through **File → Save Notebook**. The remaining notebooks
were opened through the file browser or the observed **Open from Path** dialog.
Each received an explicit class-kernel selection, UI-triggered restart/run-all,
and save. Saved notebook labels alone were not treated as interpreter proof.

All eight notebooks completed and were saved in the working copy. All six course
notebooks printed the same new `.venv/bin/python` interpreter. The original
smoke notebooks do not print that path; explicit UI selection and the inspected
sys-prefix kernelspec supply their interpreter evidence. Saved metadata names
`phys3810-fa2026` in every notebook.

The assistant visually inspected all 16 figures: preflight circuit/histogram;
Grover circuit, sampling, and iteration curve; QFT circuit and phase/probability
panels; QPE circuit, exact histogram, and nonexact distributions; HHL circuit,
conditioned-state/success comparison, and sampled observables; Shor circuit,
phase histogram, and order-versus-factor recovery comparison. These are actual
browser observations, distinct from merely counting image outputs.

An independent filesystem audit preserved the first UI outputs under
`install-audit/ui-first/` and confirmed 8/50/16, complete counts, no error outputs,
and identical cell IDs/types/code/Markdown. Only the eight notebooks' outputs
and expected metadata changed; the other **115 exported files/modes** stayed
unchanged. These working-copy saves do not alter output-free tracked notebooks
or the frozen R1 source.

## Shutdown, reopen, and reruns

After saving all notebooks, the assistant selected **File → Shut Down**,
confirmed shutdown, waited for **Server stopped**, and closed the first tab.
The server log records the shutdown request and kernel/extension cleanup; the
launcher recorded the Jupyter child exiting **0**. The outer tool session
reported **143** afterward. The stopped UI and child/lifecycle receipts, rather
than that outer wrapper code alone, establish successful application shutdown.

The guide's return commands activated the same `.venv`, printed its interpreter,
and launched `python -m jupyterlab` again. No package installation or kernel
re-registration occurred. The saved workspace restored all eight notebook tabs
and the class kernel option.

Preflight and Shor were explicitly selected again. Retained outputs were cleared
through the UI, then both notebooks were restarted/run and saved. The successful
reruns add **12 cell executions and five figures** to the activity record; they
do not change the eight-notebook/50-cell/16-PNG curriculum inventory. UI restart
events and cleared-output states distinguish the reruns from simply reopening
old saved results. No unsupported timestamp-based rerun claim is needed.

The final saved-output audit again confirms 8/50/16 and unchanged source cells.
The first and final saved notebook bytes are identical, consistent with seeded
outputs and the absence of execution timestamps in this UI configuration.
Identical files alone do not demonstrate a rerun: the explicit cleared-output,
restart/run, and save observations, together with server lifecycle records,
provide that evidence.

The reopened server was then shut down through the same UI workflow and its
browser tab closed. Its Jupyter child and outer launcher both exited **0**.
No `jpserver` runtime record remained after shutdown. The first session's outer
143 result is not attributed to this second session. No test server or test tab
was intentionally left running.

## Observation repairs, limits, and preservation

No algorithm or student setup-command failure required a source repair. Internal
UI evidence handling needed three corrections: a count locator was restricted
to the visible notebook because hidden tabs retained the same count text;
cell-navigation screenshots were checked again after the target view finished
rendering; and the evidence helper was rebound after closing the first browser
tab. Early navigation images are not used as proof that a later figure was
visible. These are automation-observation corrections, not hidden lesson passes.

**Untested:** native Windows x64, macOS ARM64/Intel, native VS Code/Cursor UI,
other browser configurations, new OS/Python installation, human pacing, the
unpublished download/student-package extraction, and remote CI. Exact Chrome
version remains **unverified**; the earlier browser-policy limit was retained
without retrying or bypassing the blocked internal version URL. Teaching dates,
coverage, assessment, delivery responsibility, and Rick's reply remain open.

The preservation baseline covers the original 87 files/index/status, accepted
118 files/index/status, 17 recovery files, seven immutable assets, frozen R1
source, and existing interpreter/configuration/distribution metadata. It also
hashes retained R1 non-venv staging (132 files) and R2 staging (136 files),
without exposing their contents. Environment checks are not a complete hash of
every installed package-code/cache/OS byte. The final preservation comparison
passed, including the retained R1/R2 staging snapshots.

## Receipts and next work

Ignored evidence is in the candidate worktree's
`artifacts/r6-walkthrough-2026-10-31/`: source/guide manifest, exact command logs,
installation receipt, isolation settings, package/kernelspec audit, first UI
snapshots, redacted UI event/AX records and screenshots, server lifecycle logs,
and preservation checks. Generated outputs and credentials are excluded from
tracked documentation and future review/student bundles. Temporary staging is
retained test evidence, not a durable source backup or released package.

No new PDF, student archive, publication, external message, hardware job,
algorithm-scope expansion, or GPT Pro transfer occurred. A later task can prepare
the provisional document-review packet and separate prompt using the newly
evidenced setup path, while clearly retaining unresolved teaching/platform/
human-rehearsal decisions. Final classroom release still follows the remaining
[readiness gates](RELEASE_READINESS_PLAN.md).
