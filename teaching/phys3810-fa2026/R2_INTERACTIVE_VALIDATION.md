# R2: interactive JupyterLab validation

October 31, 2026. **The Linux/Chrome JupyterLab path passed**, including named
kernel selection, UI-triggered restart/run-all, figure inspection, saving,
server shutdown, relaunch, and repeat execution. **Native VS Code/Cursor UI is
untested**, because native application control is unavailable. Exact Chrome
version is unverified because browser approval policy blocked its internal
version page. Do not label all editor/platform paths validated.

## Scope and preserved working layout

The frozen [R1 snapshot](R1_FRESH_LINUX_VALIDATION.md), source
`9e73b82aa578f0264afcbf7125631774afa3eb1c`, and its fresh CPython 3.12.15
environment were verified before use. All 110 source files/modes matched their
receipt. A separate complete source copy was created for interactive execution:

- R1 source: `/tmp/phys3810-r1-2026-10-31-gt5hru30/source/`.
- R1 environment: `/tmp/phys3810-r1-2026-10-31-gt5hru30/venv/`.
- R2 working copy: `/tmp/phys3810-r2-2026-10-31-2g0j090r/interactive-source/`.
- R2 settings/kernel/runtime directories: siblings of that working copy.
- Evidence: ignored `artifacts/r2-interactive-2026-10-31/` in the integration
  worktree, including UI screenshots, redacted accessibility snapshots, event
  notes, saved-output audits, lifecycle extracts, and preservation receipts.

JupyterLab was launched with R1's Python, serving only the copied tree on
loopback with authentication enabled. Native computer APIs were disabled;
Chrome's connected browser surface was available. No unrelated user tab or
private correspondence was opened. The displayed JupyterLab version was **4.6.4**.
No package was installed or upgraded during R2.

## Kernel registration and documented adaptations

To preserve R1's environment, the named kernel was registered with an isolated
R2 `JUPYTER_DATA_DIR` and `ipykernel install --user --name phys3810-fa2026
--display-name "Python (PHYS 3810)"`. The resulting kernelspec argv points
exactly to R1's `venv/bin/python`. This is an explicit preservation adaptation
of SETUP's ordinary `--sys-prefix` command; that command was not run against
the frozen environment. User settings, IPython data, plot caches, Jupyter
runtime, Lab settings, and workspaces were isolated under R2.

The interpreter therefore appears in R1's sibling `venv`, rather than the
usual in-repository `.venv` described to students. The conventional placement
and native editor picker are not newly certified by this adapted test.
Saved notebook kernel metadata varied, so **Python (PHYS 3810)** was explicitly
selected in every required notebook. A saved label alone was not treated as proof.

## Actual browser actions and results

Through Chrome's JupyterLab UI, the assistant opened each required notebook,
selected the named kernel, invoked **Restart the kernel and run all cells**,
confirmed the restart, inspected results, and saved the working copy. No
nbclient/nbconvert execution was substituted for these UI actions.

All eight notebooks completed with consecutive execution counts and no retained
error output:

- Preflight: 4 code cells, 2 PNGs; versions, R1 interpreter path, Bell state,
  sampled counts, circuit, and histogram inspected.
- Grover: 9 cells, 3 PNGs; circuit, marked-state samples, iteration oscillation.
- QFT: 7 cells, 2 PNGs; transform circuit and phase/amplitude/probability panels.
- QPE: 8 cells, 3 PNGs; controlled powers, exact decoding, nonexact distributions.
- HHL: 7 cells, 3 PNGs; circuit, raw/conditioned branch checks, sampled X/Y/Z.
- Shor: 8 cells, 3 PNGs; circuit, phase bins, theoretical/empirical order versus
  factor recovery, and the local synthesis diagnostic.
- Local statevector smoke: 3 cells, no PNG requirement; exact Bell/count checks.
- Local Aer smoke: 4 cells, no PNG requirement; ideal/noisy counts and ZZ=1.

Total: **50 nonempty code cells and 16 PNGs**. All 16 figures were inspected
in the browser. The six teaching notebooks display the expected R1 interpreter
path; the two original smoke notebooks show the selected kernel and package
version but do not print the interpreter path themselves. External kernelspec
argv and explicit UI selection provide the latter's interpreter evidence.

Filesystem audits corroborate the UI: each saved notebook still has the same
cell IDs, types, code, and Markdown as R1; only execution outputs and expected
metadata differ. All have `phys3810-fa2026` kernel metadata. All other 102 copied
source files remain byte-identical. The frozen R1 copy retains all 110 original
hashes/modes and output-free notebooks. Executed copies are evidence, not files
to commit or include in a student/review package.

## Shutdown and return workflow

After saving all notebooks, **File → Shut Down** was confirmed in the UI.
JupyterLab displayed **Server stopped**, and its process reported exit 0.
The browser tab was closed. The same Python/environment and isolated settings
were used to relaunch JupyterLab; no reinstall or kernel re-registration occurred.
The reopened workspace restored the saved notebooks and named kernel.

Preflight and Shor were explicitly selected, restarted, and run again through
the reopened UI. Both completed, with fresh restart transitions and the expected
results/figures. These reruns are additional to the first-run totals above, not
extra notebooks in the eight-notebook inventory. The server was then shut down
through the UI again, its stopped state verified, and the test tab closed.
No test server was intentionally left running.

The UI configuration did not store per-cell execution timestamps. A supplementary
attempt to compare such timestamps **failed because the metadata was absent**;
it is not a lesson execution failure. No timestamp-based rerun claim is made.
Actual UI restart/run transitions, server lifecycle logs with new kernel IDs,
and saved completed outputs are the return-workflow evidence. One launcher shell
reported 143 after its Jupyter child reported exit 0; the UI stopped message and
server shutdown logs establish the application shutdown independently.

## Limits and verification

**Passed:** the adapted local JupyterLab path, all eight UI executions, visual
inspection, save/reopen, repeat execution, source-cell preservation, immutable
asset checks, and environment configuration/distribution-metadata checks.
Documentation lint, local links, and pre-commit passed in the integration worktree.
The prior **160-test** R1 suite remains unchanged; it was not rerun solely for
this UI/evidence task, and no new unit-test count is claimed.

**Untested:** native VS Code/Cursor interpreter and notebook-kernel selection,
native Windows/macOS setup, other browsers, standard `--sys-prefix` registration
in an in-project `.venv` in this R2 run, timed teaching, and final package/remote CI.
**Unverified:** exact Chrome version. Automatic browser approval review rejected
`chrome://version` because only HTTP(S) protocols are allowed. No workaround was
attempted. This limitation does not turn the observed browser executions into
headless evidence or certify the inaccessible editor path.

The original checkout/index, source/tests/notebooks/contracts/pins, verified
PDFs, reviewed archives, Grover rc1 assets, and R1 export remain preserved.
Old classroom/tool/R1 environments retain their configurations, interpreter
identities, installed versions, and hashed distribution metadata. That is not
a full byte-for-byte audit of all package code, caches, or the OS.
No algorithm repair, dependency change, publication, external message, IBM job,
or new student package was performed. Rick's reply remains pending.

**Next:** R3 native-platform preparation/execution only on actual authorized
hosts. Retain the editor gap separately and require access before claiming it
passed. Keep platform choices provisional pending instructor feedback; Linux or
WSL results cannot certify native Windows/macOS. **GPT Pro sync: not needed**
for this bounded UI check. The next planned sync remains the matching PDF/teaching
checkpoint after support claims and teaching inputs stabilize.
