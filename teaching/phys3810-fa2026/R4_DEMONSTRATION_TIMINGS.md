# R4 local demonstration timing evidence

Executed October 31, 2026. **Passed: 42 fresh-kernel notebook executions.**
Three trials covered each of the eight required notebooks and six derived
presenter demonstrations. Each canonical trial executed **50 nonempty code
cells and produced 16 PNGs**. Across repeated and derived runs the totals were
291 code-cell executions and 102 PNGs. Those totals do not replace the
classroom baseline of 160 tests/eight notebooks/50 cells/16 PNGs.

The [run sheets](R4_PRESENTER_RUN_SHEETS.md) allocate proposed human teaching
minutes. This record measures machine execution in seconds. **No human pacing
rehearsal or new interactive UI check occurred.** The application/unit suite
was deliberately not repeated for these documentation-only changes; R1's
160-test result remains the existing unit-test evidence.

## Exact source, environment, and isolation

- Source: committed `07831f4c806d2c4203ea03aa589c31983cbb08de`, exported with
  `git archive` to `/tmp/phys3810-r4-2026-10-31-03cwfyr5/source`.
  All 113 tracked file hashes and modes were recorded before execution and
  verified unchanged afterward. No notebook outputs were written into that export.
- Interpreter: `/tmp/phys3810-r1-2026-10-31-gt5hru30/venv/bin/python`,
  CPython 3.12.15, reusing the validated R1 environment. No package installation
  or dependency change occurred; this is not another fresh-install result.
- Host: Ubuntu 26.04.1 LTS, Linux 7.0.0-42-generic, x86_64, glibc 2.43.
  Installed application versions: Qiskit 2.6.1, Aer 0.17.2, NumPy 2.5.4,
  Matplotlib 3.11.2, nbclient 0.11.0, nbformat 5.10.4, ipykernel 7.4.0.
- Kernel specifications and Matplotlib/IPython/Jupyter settings live under
  the separate R4 staging parent. Each execution starts and shuts down its own
  kernel using that exact interpreter. User site packages and Python bytecode
  writes are disabled; Matplotlib uses Agg. OpenMP/OpenBLAS use two threads.
- The exported files, original checkout/index, existing environments, frozen
  R1 source, verified PDFs, reviewed archives, and Grover rc1 assets are retained.
  Executed notebooks live under the R4 staging parent's `executed/trial-{1,2,3}`.
  Temporary staging is retained evidence, not a durable backup or student package.

## Measurement and strict success criteria

The local runner uses `time.perf_counter()` around `NotebookClient.execute` and
its `on_cell_execute`/`on_cell_executed` hooks. The latter brackets the execution
request through reply/output processing in installed nbclient 0.11.0; it does
not use `on_cell_complete` as an execution-end timer. Hook behavior was checked
against installed source and the
[primary nbclient documentation](https://nbclient.readthedocs.io/en/latest/client.html).

**Wall seconds** include kernel startup, execution, reply/output processing,
and kernel cleanup; they exclude reading the input JSON and writing the saved
executed notebook. **Cell seconds** sum the timed code-cell requests. They
include Python imports, circuit construction, assertions, sampling, and image
creation performed inside those cells. They exclude notebook prose, browser
layout, clicking, presenter narration, predictions, transitions, learner work,
discussion, installation, and network downloads. They are not CPU-only timings.
The receipt also retains time to the first code request and wall-minus-cell
non-cell overhead; those quantities are not teaching time.

Every run used `allow_errors=False`, `force_raise_errors=True`, and the canonical
validator's required-cell checks before and after execution. Skip tags are
rejected; nonempty code counts must be complete and sequential from one;
execution replies must be successful; no error outputs are allowed. Required
PNG counts were checked, with three each for HHL/Shor. Partial executed copies
would be retained on failure. All actual runs passed without hidden exceptions.
Figures were generated and counted here, not newly inspected in a browser;
R2's prior actual figure inspection remains separate evidence.

There are only three trials per case on one existing host. Kernels are fresh,
but OS/filesystem and Matplotlib caches can warm and were not flushed. Cases
ran sequentially in canonical-validator order followed by the initial three
HHL/Shor variants. Nine Grover/QPE variant executions were added afterward;
they may benefit from already-warm caches. Ranges are observations, not a
confidence interval, maximum latency guarantee, or cross-platform benchmark.
The first preflight trial was slower; no unsupported cause is assigned to it.

## Eight canonical notebooks

Each bullet reports **wall median [minimum–maximum]; summed cell median
[minimum–maximum]**, in seconds across three runs. All source code is unchanged.
The smoke notebooks are preparation/validation checks, not added classroom blocks.

- `00_setup_preflight`: wall 1.568 [1.440–2.580]; cells
  0.721 [0.713–1.722]; 4 code cells/2 PNGs.
- `00_local_statevector_smoke`: wall 0.937 [0.874–0.990]; cells
  0.259 [0.250–0.263]; 3 code cells/0 PNGs.
- `01_local_aer_smoke`: wall 1.012 [0.977–1.071]; cells
  0.358 [0.352–0.358]; 4 code cells/0 PNGs.
- `01_grover`: wall 1.728 [1.717–1.766]; cells
  0.958 [0.947–1.004]; 9 code cells/3 PNGs.
- `02_qft`: wall 1.630 [1.582–1.705]; cells
  0.863 [0.860–0.890]; 7 code cells/2 PNGs.
- `03_qpe`: wall 1.770 [1.763–1.860]; cells
  1.045 [1.043–1.045]; 8 code cells/3 PNGs.
- `04_hhl`: wall 1.902 [1.864–1.972]; cells
  1.161 [1.143–1.178]; 7 code cells/3 PNGs.
- `05_shor`: wall 2.168 [2.136–2.216]; cells
  1.376 [1.361–1.392]; 8 code cells/3 PNGs.

Across each full eight-notebook trial, summed notebook wall durations were
13.882, 12.636, and 12.713 seconds. This sum excludes inter-notebook driver work
and is not a measured classroom or UI session. Full notebook runs include
reference and expansion cells even when a presenter discusses only the core.

## Derived presenter demonstrations

These are executed copies with the following explicit changes; canonical
notebook bytes were never edited. Every case ran in three fresh kernels and
retained all downstream assertions and figures. Durations use the same
median [minimum–maximum] notation and include the entire derived notebook,
not merely the changed cell.

- **HHL scaled matrix:** `matrix_entries=[[3,1],[1,3]]`, default `b=[1,0]`. Only the parameter assignment changes; all seven cells/three PNGs execute.
  Wall 1.863 [1.858–1.974]; cells 1.139 [1.131–1.140] seconds.
- **HHL complex state:** default matrix and `b=[1/sqrt(2), i/sqrt(2)]`. Only the RHS assignment changes; all seven cells/three PNGs execute.
  Wall 1.908 [1.857–1.919]; cells 1.150 [1.138–1.180] seconds.
- **Shor presenter order:** unchanged eight code cells, with the resource diagnostic executed after sampling and before expansion/failure cells. Three PNGs execute; the timing copy omits Markdown cells, which are untimed in all cases.
  Wall 2.153 [2.082–2.181]; cells 1.377 [1.362–1.390] seconds.
- **Grover marked-set exercise:** change only `multiple_targets` from `("001", "011")` to `("000", "110")`; all nine cells/three PNGs execute.
  Wall 1.671 [1.660–1.746]; cells 0.919 [0.918–0.925] seconds.
- **QPE exact phase 1/8:** change only `exact_phase=3/8` to `1/8`; all eight cells/three PNGs execute, including sampling and the SDK reference.
  Wall 1.777 [1.724–1.843]; cells 1.009 [1.004–1.057] seconds.
- **QPE exact phase 6/8:** change only `exact_phase=3/8` to `6/8`; all eight cells/three PNGs execute, including sampling and the SDK reference.
  Wall 1.808 [1.726–1.882]; cells 1.010 [1.010–1.063] seconds.

The optional QFT `001` substitution, QPE nonexact 0.97 substitution, and changed
Grover curve parameters were not separately timed. They remain explicit
paper/optional alternatives in the run sheets. Existing mathematical tests and
parameter support do not establish their live execution duration. HHL's plus/
minus eigenstates are paper debrief options here, not additional timed live runs.

## Implications and remaining gates

These small local simulations require seconds of measured execution on this
host. This helps a presenter budget machine waits and verify dependencies; it
does not show that learners can complete the explanations or exercises in the
proposed 50/75-minute sessions. Keep all prediction, transition, exercise,
and debrief allocations provisional until an actual presenter rehearsal.
The run-sheet index includes an unfilled receipt for that later work.

Native Windows x64, macOS ARM64/Intel, and native VS Code/Cursor UI remain
**untested**. Exact Chrome version remains **unverified**. No headless timing
closes those gaps or changes Rick's pending decisions. Runtime/cloud/GPU work
was excluded; no IBM service call, hardware job, package/publication action,
new PDF, or external message was part of this measurement.

## Receipts and local checks

Ignored evidence is retained under `artifacts/r4-presenter-2026-10-31/`:

- `staging.json`, `start-state.json`: exact export/interpreter and preservation
  baseline; `source_files` records all 113 source hashes/modes.
- `time_demonstrations.py`, `timing.log`: actual harness and execution log.
  Command: `PYTHONDONTWRITEBYTECODE=1` followed by the R1 interpreter above and
  `artifacts/r4-presenter-2026-10-31/time_demonstrations.py` from the integration
  worktree. The second invocation resumed completed results and added only the
  nine missing Grover/QPE cases. This retained receipt is not an idempotent
  benchmark command; a repeat requires new isolated staging and receipts.
- `timing-runs.json`, `timing-summary.json`: all 42 executions, individual cell
  IDs/durations, counts, output paths, versions, and aggregate statistics.
  The original 33-run receipts are retained separately with `initial-33` names.
- `preservation-and-documentation.json`, `preservation-agent/final-check.json`,
  `checks.json`, `pre-commit.log`: final documentation/preservation checks and
  maintainer lint results. These do not imply a new 160-test execution.

On resuming the interrupted turn, the original 33 records were verified
complete and passed, with no failed/partial entry; no timing process was left
running. Only the missing nine cases were then executed. All 113 exported
hashes/modes were checked again. The host emitted its standard local-kernel TCP
transport warning; it did not cause a cell failure. Kernels were cleaned up.

The run-sheet audit checked 17/25/25 actual notebook cell references, continuous
0–75-minute heading intervals and the 50-minute boundary, dependency order, and
mathematical answer cues. Shor's residue-state wording was corrected to describe
a superposition of eigenstates whose counting outcomes form a phase distribution.
Only Markdown documentation/context is changed in the repository. No algorithm,
notebook, test, pin, or contract expansion occurred.

Final documentation checks passed: 133 relative links, output-free source
notebooks, Git whitespace/scope, and the full configured pre-commit run (Ruff,
yamllint, markdownlint). Preservation checks passed for the original 87
files/modes, original HEAD/index/status, seven immutable assets, the 110 frozen
R1 source files, and existing interpreter/environment metadata. Environment
verification covers interpreter/configuration and installed-distribution
metadata, not a full hash of every package-code/cache/OS byte. No unit-suite
rerun or human teaching pass is inferred from these checks.
