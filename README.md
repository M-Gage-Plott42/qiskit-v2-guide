# qiskit-v2-guide

Minimal Qiskit 2.x smoke-test repo for reproducible workflow checks: local exact simulation (reference primitives), local Aer simulation (Aer primitives), and optional IBM Runtime hardware execution in job mode.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install qiskit qiskit-aer qiskit-ibm-runtime jupyter
```

Run notebooks:

```bash
jupyter lab
```

Then open:
- `notebooks/00_local_statevector_smoke.ipynb`
- `notebooks/01_local_aer_smoke.ipynb`
- `notebooks/02_ibm_runtime_smoke.ipynb` (optional cloud path)

## No QPU required (run this first)

These notebooks run fully local with no IBM credentials:
- `notebooks/00_local_statevector_smoke.ipynb` for Qiskit SDK reference primitives (`StatevectorSampler`).
- `notebooks/01_local_aer_smoke.ipynb` for Aer primitives (`SamplerV2`/`EstimatorV2`) plus transpilation to an `AerSimulator` target.

This is the default smoke path for reproducibility and debugging.

## IBM Runtime (optional cloud smoke test)

1. Copy `.env.example` to `.env`.
2. Fill placeholders only in `.env`:
   - `API_KEY=...`
   - `INSTANCE=...`
   - `CHANNEL=ibm_quantum_platform`
3. Never commit `.env` or real credentials.
4. Run `notebooks/02_ibm_runtime_smoke.ipynb`.

The runtime notebook:
- initializes `QiskitRuntimeService` from environment or saved account,
- discovers candidates with `service.backends(simulator=False, operational=True, min_num_qubits=5)`,
- selects a target with `service.least_busy(...)`,
- submits a minimal `SamplerV2` job in job mode,
- prints backend name, job ID, status, and a bitstring preview.

Backend inventories and names change over time; this repo intentionally avoids hardcoded backend names and uses `least_busy()` for robustness.

Tested with: Qiskit 2.x API patterns, last updated February 9, 2026.
