# qiskit-v2-guide

[![License](https://img.shields.io/github/license/M-Gage-Plott42/qiskit-v2-guide?label=License)](LICENSE)
[![local-smoke](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/local-smoke.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/local-smoke.yml)
[![ruff](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-python.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-python.yml)
[![markdownlint](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-markdown.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-markdown.yml)
[![yamllint](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-yaml.yml/badge.svg?branch=main)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/workflows/lint-yaml.yml)
[![Release](https://img.shields.io/github/v/release/M-Gage-Plott42/qiskit-v2-guide?label=Release)](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases)

Minimal Qiskit 2.x smoke-test repo for reproducible workflow checks: local exact simulation (reference primitives), local Aer simulation (Aer primitives), and optional IBM Runtime hardware execution in job mode.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Run notebooks:

```bash
jupyter lab
```

If Cursor/VS Code shows unresolved imports, select the project interpreter:

- Linux/macOS/WSL: `.venv/bin/python`
- Windows: `.venv\\Scripts\\python.exe`

Then open:

- `notebooks/00_local_statevector_smoke.ipynb`
- `notebooks/01_local_aer_smoke.ipynb`
- `notebooks/03_runtime_local_testing_mode.ipynb`
- `notebooks/02_ibm_runtime_smoke.ipynb` (optional cloud path)
- `notebooks/04_aer_gpu_smoke.ipynb` (optional GPU path)

See `docs/Qiskit_v2_Environment_and_Runtime_Guide.md` for the full setup flow.

## No QPU required (run this first)

These notebooks run fully local with no IBM credentials:

- `notebooks/00_local_statevector_smoke.ipynb` for Qiskit SDK reference primitives (`StatevectorSampler`).
- `notebooks/01_local_aer_smoke.ipynb` for Aer primitives (`SamplerV2`/`EstimatorV2`) plus transpilation to an `AerSimulator` target.
- `notebooks/03_runtime_local_testing_mode.ipynb` for Runtime local testing mode with a fake backend (`SamplerV2(mode=fake_backend)`).

This is the default smoke path for reproducibility and debugging.

## IBM Runtime (optional cloud smoke test)

1. Copy `.env.example` to `.env`.
2. Fill placeholders only in `.env`:
   - `QISKIT_IBM_TOKEN=...`
   - `QISKIT_IBM_INSTANCE=...`
   - `QISKIT_IBM_CHANNEL=ibm_quantum_platform`
3. Legacy aliases (`API_KEY`, `INSTANCE`, `CHANNEL`) are also accepted for compatibility.
4. Never commit `.env` or real credentials.
5. Run `notebooks/02_ibm_runtime_smoke.ipynb`.
6. IBM Quantum Platform classic was sunset on July 1, 2025; use current IBM Quantum Platform and docs at <https://docs.quantum.ibm.com/>.

The runtime notebook:

- initializes `QiskitRuntimeService` from environment or saved account,
- discovers candidates with `service.backends(simulator=False, operational=True, min_num_qubits=5)`,
- selects a target with `service.least_busy(...)`,
- submits a minimal `SamplerV2` job in job mode,
- prints backend name, job ID, status, and a bitstring preview.

Backend inventories and names change over time; this repo intentionally avoids hardcoded backend names and uses `least_busy()` for robustness.

## Automation

- Local one-command smoke test: `bash scripts/smoke_local.sh`
- CI runs the same local smoke path (`00` and `01`) on pushes and pull requests.
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

Tested with Qiskit 2.3.x API patterns. See `CHANGELOG.md` and Releases for update history.
