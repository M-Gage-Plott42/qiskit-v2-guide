# Milestone 1 review reconciliation

October 29, 2026. **Required finding M1-01 is resolved with execution evidence;
the milestone-1 review checkpoint is closed. Grover is next.** No new commit,
push, PR, merge, release, or IBM Runtime service connection was made.

This is the historical milestone-1 correction record. Grover was implemented
subsequently; see [GROVER_VALIDATION.md](GROVER_VALIDATION.md) and [STATUS.md](STATUS.md)
for the current lesson and next review checkpoint.

## Reviewed snapshot and independent evidence

GPT Pro's review was received for the exported 60-file working-tree snapshot:

- Branch: `feat/phys3810-m1-onboarding`.
- Base/HEAD: `fb41ae02f2ece3e093e60c9286ef72ae91686530`.
- Source-manifest SHA-256:
  `06e22d9b5d2aa2a9533eaf801ebf672f87999e4f8d80a0d8c7f75d852e3eff8d`.

The reviewer reported access to all 60 files, verified their hashes, and
independently executed the original 19 tests and three required notebooks on
Linux x86_64, CPython 3.12.14, glibc 2.39, pip 26.2.2. All 114 application
packages matched the existing constraints and installed inventory. The two
preflight PNGs were produced and inspected. These are **reviewer-reported
executions**, distinct from the implementation assistant's subsequent local
CPython 3.12.15 runs below. No raw private review correspondence is reproduced.

The review found no planning conflict or environment migration requirement.
It requested one validator correction before Grover and allowed that checkpoint
to close after a demonstrated fix without another approval round. Windows,
macOS, interactive UI, remote CI, real IBM Runtime, and GPU results were not
established by the review.

## M1-01: error and skip tags could produce a false pass

**Disposition: confirmed, fixed, and regression-tested.**

The implementation assistant reproduced the finding against the original
runner in temporary source copies. The same injected failing assertion gave:

- Ordinary cell: one notebook failure, with `AssertionError` saved.
- Cell tagged `raises-exception`: zero failures despite a saved error output.
- Cell tagged `skip-execution`: zero failures; execution count remained null.

This agrees with installed nbclient 0.11.0 and its
[documented error policy](https://nbclient.readthedocs.io/en/latest/reference/nbclient.html#nbclient.client.NotebookClient.force_raise_errors).
The original required notebooks used neither bypass and passed normally, so
the finding did not invalidate their Bell-state calculations.

The focused correction in `scripts/validate_classroom.py` now:

1. Forces cell errors to raise, including errors tagged `raises-exception`.
2. Rejects `skip-execution` on nonempty required code with a cell-numbered
   diagnostic, before starting that notebook's kernel.
3. Requires an execution count for every nonempty code cell and no remaining
   error outputs before reporting success.
4. Preserves partial executed notebooks on failure and retains kernel cleanup.
5. Identifies the preflight by its path rather than its position in the tuple,
   so other required notebooks are not accidentally assigned its PNG contract.

`tests/test_validate_classroom.py` adds six regressions. Four invoke the actual
execution gate in subprocesses and exercise real nbclient behavior: successful
execution, ordinary error, tagged error, and forbidden skipping. They assert
process exit status, success/failure reporting, saved diagnostics, source
preservation, and that a failure stops later cells. The success case also
checks harmless empty cells. Two additional checks cover missing execution
counts and retained error outputs. No mocked notebook execution substitutes for
the tagged-error regression.

## Optional findings

**O1 — implemented; remote behavior remains untested.** The existing artifact
upload step now uses `if: ${{ !cancelled() }}` and warns if artifacts do not
exist, for example after an installation failure. Validation failures retain
their nonzero status; job names, required checks, and triggers are unchanged.
This follows [GitHub's documented condition](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#always).
YAML and Actions lint pass, but only a future remote failure exercise can prove
that GitHub exposes the partial notebook artifact. No remote run is claimed.

**O2 — implemented and tested offline.** The supplied-credential failure message
now identifies explicit configuration, process variables, and repository `.env`,
including process-over-file precedence. The existing mocked failure test checks
that guidance, that the displayed exception string omits the dummy token and
instance, and that no fallback service attempt occurs after explicit failure.

## New local execution evidence

Environment pins are unchanged: CPython 3.12.15, Qiskit 2.6.1, Aer 0.17.2,
nbclient 0.11.0. Recorded local commands and outcomes:

- Original-runner negative controls in temporary copies: **confirmed** the two
  false passes described above. Log: `artifacts/milestone1/reconciliation/m1-01-before.log`.
- `python -m unittest discover -s tests -p test_validate_classroom.py -v`:
  **6 passed**, including real subprocess/kernel regressions.
- `python scripts/validate_classroom.py`: **passed**, including `pip check`,
  **25 tests** (13 configuration, 6 mathematics, 6 runner regressions), all
  three original classroom notebooks in fresh kernels, and two preflight PNGs.
- `bash scripts/smoke_local.sh artifacts/milestone1/reconciliation/executed-local-smoke`:
  **passed**, preserving the original smoke entry point.
- Ruff 0.15.22 over `src`, `scripts`, `tests`, course notebooks, and both core
  smoke notebooks: **passed**.
- yamllint 1.38.0, shellcheck, actionlint 1.7.12, Markdown/pre-commit checks,
  local documentation links, and `git diff --check`: **passed**.

Commands used the classroom venv or the separate maintainer tool environment
as appropriate. Evidence logs are in ignored
`artifacts/milestone1/reconciliation/`. Source notebooks remain output-free.
Tests of expected failures passed because they observed failure; those failed
notebook fixtures are not relabeled successful executions.

The correction has not been independently retested by GPT Pro. The review's
stated completion rule permits the successful local reproduction/fix/regression
sequence to close this checkpoint. Remote artifact upload, native Windows and
macOS, interactive Jupyter/editor selection, optional Runtime re-execution,
hardware, and GPU checks were not run during this correction.

## Next action and sync

Implement [GROVER_PLAN.md](GROVER_PLAN.md) as the next scoped module: source,
independent oracle/amplification tests, notebook, and required-validator
integration. The initial contract deliberately restricts inputs and includes
asymmetric targets, multiple targets, exact fixtures, and overshooting.

**GPT Pro sync: not needed for this correction; recommended after complete
Grover.** Keep the later QFT/QPE-before-HHL/Shor checkpoint. User input needed
now: none for the defined technical work. Teaching decisions remain open but
do not block this small local implementation. The older desktop packet remains
an immutable record of the reviewed snapshot; prepare a new desktop packet at
the next sync rather than overwriting it.
