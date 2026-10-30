# Milestone 1 validation and review handoff

Original milestone-1 validation, October 29, 2026. This report preserves the
initial execution evidence. The subsequent independent review, confirmed
validator defect, correction, and **25-test** rerun are recorded in
[REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md). **No algorithm lessons or
final PDF were implemented in that initial milestone.** Current Grover work is
documented separately in [GROVER_VALIDATION.md](GROVER_VALIDATION.md); the results
and remaining deliverables below describe the earlier snapshot.

## Base and reviewable result

- Initial branch: `main`; initial working tree and index: clean.
- Actual base and unchanged HEAD: `fb41ae02f2ece3e093e60c9286ef72ae91686530`.
- Local feature branch: `feat/phys3810-m1-onboarding`.
- Result: a staged local diff against that base, with no new commit, push,
  pull request, merge, release, or ruleset modification.
- Supplied audit: `bf6f362ded70767d3891db996a0a3e0cd152b34d`.
  It was initially absent locally. A read-only GitHub comparison and then a
  fetch of that commit established that the local base is **12 commits behind**
  the audit, not ahead. The branch was neither reset nor rebased to the audit.

The intervening audited changes affect six files: `requirements.txt`,
`constraints-ci.txt`, and the CodeQL, Python lint, YAML lint, and local-smoke
workflows. They update dependency/action versions (including ipykernel 7.4.0).
No lesson/source additions occur in that interval. This milestone independently
resolves its classroom packages; unrelated action pins remain at the actual
local base. A future integration onto newer main must retain its newer action
and security updates rather than reverting them.

Inspection commands included `git status --porcelain=v1`, `git branch
--show-current`, `git rev-parse HEAD`, `git log --oneline`, `git diff HEAD
bf6f362ded70767d3891db996a0a3e0cd152b34d`, and `git log
HEAD..bf6f362ded70767d3891db996a0a3e0cd152b34d`. Review the resulting work with
`git diff --cached HEAD` and `git diff --cached --check`.

## Inventory and scope

The starting tree contains six notebooks and one Python helper:

- `00_local_statevector_smoke.ipynb`: local reference SamplerV2 Bell smoke.
- `01_local_aer_smoke.ipynb`: Aer sampling, ZZ estimation, and noise example.
- `02_ibm_runtime_smoke.ipynb`: optional real Runtime service and job submission.
- `03_runtime_local_testing_mode.ipynb`: optional Runtime fake-backend smoke.
- `04_aer_gpu_smoke.ipynb`: CPU probe and optional GPU branch with skip handling.
- `Qiskitv2_QPU_Min_Example.ipynb`: compatibility notebook, also a real hardware
  path. Its historical test statement is not evidence of current validation.
- `src/backend_select.py`: credential configuration and backend discovery.

There are **no QFT, QPE, Grover, HHL, or Shor implementations** in the starting
tree. No separate legacy algorithm notebooks were supplied in this request;
none have been assumed available, assessed, or tested. The pasted task brief
was used as requirements, not copied into public instructional files.

## Environment and actual versions

Host: Linux x86_64, glibc 2.43; CPython **3.12.15**. Fresh classroom venv:

- Qiskit **2.6.1**, Aer **0.17.2**, NumPy **2.5.4**, SciPy **1.18.1**.
- Matplotlib **3.11.2**, pylatexenc **2.11**, ipywidgets **8.1.8**.
- JupyterLab **4.6.4**, ipykernel **7.4.0**, nbconvert **7.17.2**,
  nbclient **0.11.0**, nbformat **5.10.4**.
- python-dotenv **1.2.2**, pip **26.2.2**.

The [complete installed snapshot](validation/installed-linux-py312.txt) records
115 distributions including pip. Every other installed distribution exactly
matches an active constraint; `pip check` reports no broken requirements.
Runtime is absent from the classroom venv. A separate optional environment
successfully installs Runtime **0.49.0**, passes `pip check`, and executes
preflight plus the Runtime fake-backend notebook without creating a service or
submitting a hardware job. See [ENVIRONMENT.md](ENVIRONMENT.md) for the selection
rationale, primary references, platform markers, and regeneration process.

## Commands and results

Commands below used the classroom interpreter with its venv activated, except
the explicitly separate maintainer tools. All required final local checks
**passed**; remote GitHub checks have not been run for this unpublished diff.

1. `python3.12 -m venv .venv`; `python -m pip install --upgrade pip==26.2.2`;
   `python -m pip install -r requirements-ci.txt` — **passed**, clean install.
   Student `requirements.txt` and CI resolve the same default environment.
2. `python scripts/update_constraints_ci.py` under CPython 3.12 with uv 0.13.6
   — **passed**, resolved 136 packages in the CPU/optional Runtime union.
   Resolved markers, installed metadata, and package availability were inspected.
3. `python -m pip check` — **passed**, no broken requirements.
4. `python scripts/validate_classroom.py` — **passed**: 19 offline unit tests
   (13 configuration/service-mock tests and 6 mathematical tests), then preflight,
   Statevector smoke, and Aer smoke in three fresh interpreter-bound kernels.
   Kernels are shut down and source notebooks remain output-free.
5. `bash scripts/smoke_local.sh` with the classroom venv on PATH — **passed**,
   retaining both original smoke notebooks and their execution artifacts.
6. `python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks
   notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb`
   with Ruff 0.15.22 — **passed**. Explicit repository configuration prevents
   host/editor lint settings from changing the checks.
7. `yamllint -c .yamllint.yml .github/workflows .github/dependabot.yml
   .github/release.yml .github/ISSUE_TEMPLATE .pre-commit-config.yaml` with
   yamllint 1.38.0; `shellcheck scripts/*.sh`; `actionlint` 1.7.12 — **passed**.
   The actionlint download was verified against its published SHA-256 checksum.
8. `pre-commit run --all-files` with pre-commit 4.7.0 — **passed** for Ruff,
   YAML, and Markdown. Standalone markdownlint-cli2 0.20.0 also passed.
9. A ZIP built from the staged source files was extracted into a directory with
   spaces, without `.git`. A second fresh venv installed using the student
   `requirements.txt`, then ran the validator — **passed**. The documented
   `python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name
   "Python (PHYS 3810)"` registered that archive interpreter, and
   `python -m jupyterlab --version` reported 4.6.4. No Git operation is needed
   inside the extracted course folder.
10. Optional environment: `uv venv --python python3.12 --seed /tmp/phys3810-runtime`
    and `uv pip install --python /tmp/phys3810-runtime/bin/python
    -r requirements-runtime.txt`, followed by `pip check` and fresh-kernel
    preflight/`03_runtime_local_testing_mode.ipynb` execution — **passed**.
    This optional smoke has its existing printed-result scope; it is not a
    mathematical algorithm test or hardware validation.

The mathematical checks assert the Bell amplitudes including relative sign,
normalization, probabilities `[0.5, 0, 0, 0.5]`, ZZ/XX/ZI expectations,
asymmetric little-endian bit order (`X(0)` yields `01`), shot totals/support,
and seeded sampling within six binomial standard deviations. The Aer smoke
also asserts the noisy run's shot accounting. Printed counts alone are not used
as correctness evidence.

The initial render inspection caught text-only figures despite successful cell
execution. Adding the inline backend fixed this; the final runner requires two
embedded PNGs, and the Bell circuit/histogram were visually inspected. Wrong
Python 3.14 execution intentionally returns nonzero with **FAILED** environment
and **UNTESTED** downstream checks. An injected notebook failure was also
reported as failure with diagnostics preserved. An exploratory optional-run
invocation initially mislabeled the Runtime notebook as preflight; rerunning
with the actual preflight first passed, without a source-code change.

Local logs and executed notebooks are under ignored `artifacts/`. The review ZIP
is an unpublished local test artifact, not a released student distribution.

## Changed files and reasons

- `AGENTS.md`: canonical source/notebook conventions, validation and math
  expectations, local defaults, outcome vocabulary, and public-artifact rules.
- `teaching/phys3810-fa2026/COURSE_PLAN.md`: deliverables, unconfirmed dates,
  timed sessions, milestones, and acceptance criteria.
- Course `README.md`, `SETUP.md`, and `STATUS.md`: student entry point, OS-specific
  archive setup/kernel instructions, draft PDF source, and honest progress.
- Course `ENVIRONMENT.md`, `VALIDATION.md`, and
  `validation/installed-linux-py312.txt`: decision, evidence, limitations,
  reproducible commands, and actual installed package inventory.
- Course `notebooks/00_setup_preflight.ipynb`: short commented local checks and
  actual circuit/histogram rendering.
- `requirements.txt`, `requirements-ci.txt`, `requirements-runtime.txt`, and
  `constraints-ci.txt`: exact shared classroom environment, complete platform
  resolution, and explicit optional Runtime install.
- `scripts/update_constraints_ci.py` and its existing `.sh` wrapper: replace
  Linux-only freezing with a Python 3.12 universal resolution workflow.
- `scripts/validate_classroom.py`: cross-platform unit/notebook validation,
  explicit fresh kernels, failure exit status, and separate output artifacts.
- `tests/test_classroom.py`: independent exact and sampling expectations.
- `src/backend_select.py` and `tests/test_backend_select.py`: explicit root
  `.env` parsing, process-over-file alias precedence, and offline mocked tests.
- `notebooks/00_local_statevector_smoke.ipynb` and
  `notebooks/01_local_aer_smoke.ipynb`: assertions and repeatable simulation seeds.
- Root `README.md`, `CONTRIBUTING.md`, and the existing environment/runtime
  guide: align entry points, optional packages, setup, and credential semantics.
- `.github/workflows/local-smoke.yml`: retain existing job/steps and add
  classroom validation/artifacts; match the student pip pin.
- `.github/workflows/lint-python.yml`, `.pre-commit-config.yaml`, and `ruff.toml`:
  include new scripts/tests/notebooks and course Markdown in deterministic lint.

## Remaining limits and independent review

- **Untested:** native Windows x64 and macOS execution, interactive JupyterLab
  browser use, and VS Code/Cursor selection. The implementation assistant tested
  3.12.15; the independent reviewer later reported an initial run on 3.12.14.
  PyPI metadata checks found compatible non-yanked wheels for all 133 active
  union pins on Windows x64 and macOS 14 ARM64, CPython 3.12. Wheel availability
  is not a native installation result; macOS Intel was not wheel-checked here.
- **Skipped:** real IBM Runtime service/account discovery, both QPU notebooks,
  and GPU execution. No IBM Runtime service connection or hardware job was attempted.
- **Untested remotely:** GitHub-hosted CI, CodeQL, and dependency-review execution
  on this diff. Existing workflow/job names, triggers, and rulesets are retained.
- **Deferred:** five algorithm lessons, final setup PDF, confirmed session dates,
  student-background/assessment decisions, and publication.
- **Remaining required local failures:** none.

For ChatGPT's independent review: compare the staged diff against the actual
base above; reproduce the clean archive install and validator; inspect the exact
mathematical expectations and `.env` precedence tests; verify no skip is called
a pass; and check the version/platform evidence against the linked primary
sources. Reconcile the 12 newer audited commits when eventually integrating.
The subsequent review gate is now closed after correction; Grover is next.

Subsequent coordination update: [WORKFLOW.md](WORKFLOW.md) assigns technical
review, fixes, and testing to the assistant and describes GPT Pro sync points.
[GPT_PRO_HANDOFF.md](GPT_PRO_HANDOFF.md) preserves the original review prompt.
The separate reconciliation record documents the received findings and new
execution evidence without rewriting the original 19-test results above.
