# qiskit-v2-guide

[![License](https://img.shields.io/github/license/M-Gage-Plott42/qiskit-v2-guide?label=License)](LICENSE)
[![local-smoke](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/local-smoke.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/local-smoke.yml)
[![ruff](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-python.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-python.yml)
[![markdownlint](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-markdown.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-markdown.yml)
[![yamllint](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-yaml.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-yaml.yml)
[![dependency-review](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/dependency-review.yml)
[![Release](https://img.shields.io/github/v/release/M-Gage-Plott42/qiskit-v2-guide?label=Release)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases)

Minimal Qiskit 2.x smoke-test repo for reproducible workflow checks: local exact simulation (reference primitives), local Aer simulation (Aer primitives), and optional IBM Runtime hardware execution in job mode.

**UTC PHYS 3810 (Fall 2026):** start at the
[student landing page](teaching/phys3810-fa2026/README.md) for the release-download
setup, preflight notebook, proposed sessions, and current delivery status.
The classroom environment uses CPython 3.12, Qiskit 2.6.1, and Aer 0.17.2.
The first algorithm lab, [Grover search](teaching/phys3810-fa2026/notebooks/01_grover.ipynb),
includes reusable source, independent tests, and 50/75-minute teaching activities.

## Quickstart

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
```

Run notebooks:

```bash
python -m jupyterlab
```

If Cursor/VS Code shows unresolved imports, select the project interpreter:

- Linux/macOS/WSL: `.venv/bin/python`
- Windows: `.venv\\Scripts\\python.exe`

Then open:

- `notebooks/00_local_statevector_smoke.ipynb`
- `notebooks/01_local_aer_smoke.ipynb`
- `notebooks/03_runtime_local_testing_mode.ipynb` (optional Runtime package)
- `notebooks/02_ibm_runtime_smoke.ipynb` (optional cloud path)
- `notebooks/04_aer_gpu_smoke.ipynb` (optional GPU path)

See `docs/Qiskit_v2_Environment_and_Runtime_Guide.md` for the full setup flow.

## No QPU required (run this first)

These notebooks run fully local with no IBM credentials:

- `notebooks/00_local_statevector_smoke.ipynb` for Qiskit SDK reference primitives (`StatevectorSampler`).
- `notebooks/01_local_aer_smoke.ipynb` for Aer primitives (`SamplerV2`/`EstimatorV2`) plus transpilation to an `AerSimulator` target.

`notebooks/03_runtime_local_testing_mode.ipynb` additionally offers Runtime local
testing with a fake backend (`SamplerV2(mode=fake_backend)`) after the optional
install: `python -m pip install -r requirements-runtime.txt`.

This is the default smoke path for reproducibility and debugging.

## IBM Runtime (optional cloud smoke test)

1. Install the optional package: `python -m pip install -r requirements-runtime.txt`.
2. Copy `.env.example` to `.env` in the repository root.
3. Fill placeholders only in `.env`:
   - `QISKIT_IBM_TOKEN=...`
   - `QISKIT_IBM_INSTANCE=...`
   - `QISKIT_IBM_CHANNEL=ibm_quantum_platform`
4. Legacy aliases (`API_KEY`, `INSTANCE`, `CHANNEL`) are also accepted for compatibility.
5. Never commit `.env` or real credentials.
6. Run `notebooks/02_ibm_runtime_smoke.ipynb` only when intending to submit a hardware job.
7. Use current IBM Quantum Platform and docs at <https://quantum.cloud.ibm.com/docs/>.

The helper reads the repository-root `.env` regardless of the notebook working
directory. Nonempty process variables take priority over file values, including
legacy aliases. Parsing leaves the process environment unchanged and treats
`${...}` literally. Local classroom validation never initializes the IBM service.

The runtime notebook:

- initializes `QiskitRuntimeService` from environment or saved account,
- discovers candidates with `service.backends(simulator=False, operational=True, min_num_qubits=5)`,
- selects a target with `service.least_busy(...)`,
- submits a minimal `SamplerV2` job in job mode,
- prints backend name, job ID, status, and a bitstring preview.

Backend inventories and names change over time; this repo intentionally avoids hardcoded backend names and uses `least_busy()` for robustness.

## Automation

- Cross-platform classroom validation: `python scripts/validate_classroom.py`.
- Original local smoke test: `bash scripts/smoke_local.sh`.
- CI retains the local smoke path (`00` and `01`) and runs offline unit tests,
  classroom preflight, and the Grover lesson on pushes and pull requests.
- Required workflows now use workflow-level concurrency and `merge_group`
  triggers so checks stay reusable with merge queues.
- Dependency review runs by default on public repos; private copies can enable
  the same workflow after GitHub Code Security or GHAS is available by setting
  `ENABLE_DEPENDENCY_REVIEW=true`.
- Reproducible CI-style dependency install: `python -m pip install -r requirements-ci.txt`
- Optional local hooks:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

See `CHANGELOG.md` for release history, `SECURITY.md` for vulnerability reporting,
`CONTRIBUTING.md` for contribution workflow, and `CODE_OF_CONDUCT.md` for community standards.

## Optional GPU smoke

`notebooks/04_aer_gpu_smoke.ipynb` checks for Aer GPU support and runs a small GPU simulation if available. If GPU support is unavailable, it prints a skip message and exits cleanly.

See the [environment decision](teaching/phys3810-fa2026/ENVIRONMENT.md) and
[validation report](teaching/phys3810-fa2026/VALIDATION.md) for exact tested
versions and platform limits, and the [Grover validation](teaching/phys3810-fa2026/GROVER_VALIDATION.md)
for the first algorithm milestone. Releases records previously published versions.
