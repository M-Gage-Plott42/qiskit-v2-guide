# Qiskit 2.x Environment and Runtime Guide

This guide replaces the older PDF setup notes and aligns with current IBM Quantum/Qiskit documentation.

For UTC PHYS 3810, use the shorter [student setup guide](../teaching/phys3810-fa2026/SETUP.md).
The supported classroom stack is CPython 3.12, Qiskit 2.6.1, and Aer 0.17.2;
the [environment decision](../teaching/phys3810-fa2026/ENVIRONMENT.md) records
resolution and platform limits.

## 1) Create and activate a virtual environment

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

## 2) Install core packages

```bash
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
```

Both the default and CI installs use the complete pinned constraints:

```bash
python -m pip install -r requirements-ci.txt
```

Runtime notebooks (`02`, `03`, and the legacy QPU example) additionally need:

```bash
python -m pip install -r requirements-runtime.txt
```

## 3) (Optional) Register a dedicated Jupyter kernel

```bash
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
```

## 4) No-account local smoke tests (recommended first)

Run these first to validate local setup without IBM credentials:

1. `notebooks/00_local_statevector_smoke.ipynb`
2. `notebooks/01_local_aer_smoke.ipynb`
3. `notebooks/03_runtime_local_testing_mode.ipynb`

The third notebook requires the optional Runtime install; it is not part of the
classroom default. Run `python scripts/validate_classroom.py` for unit tests and
fresh-kernel preflight plus notebooks `00` and `01` without credentials.

## 5) IBM Runtime smoke test (optional cloud path)

1. Create or sign in to IBM Quantum via <https://docs.quantum.ibm.com/>.
2. Create/get an instance and API key in IBM Quantum Platform.
3. Copy `.env.example` to `.env` and fill values:

```dotenv
QISKIT_IBM_TOKEN=YOUR_IBM_QUANTUM_API_KEY
QISKIT_IBM_INSTANCE=YOUR_INSTANCE_CRN
QISKIT_IBM_CHANNEL=ibm_quantum_platform
```

Legacy aliases (`API_KEY`, `INSTANCE`, `CHANNEL`) are also accepted by this repository for compatibility.

`src/backend_select.py` reads `.env` from the repository root, independent of
working directory. Nonempty process values take precedence over every file
alias for the same setting; preferred names win within each source. Parsing does
not modify `os.environ` or expand `${...}`. The classroom validator tests this
with dummy values and mocked service construction only.

1. Run `notebooks/02_ibm_runtime_smoke.ipynb` only when intending to submit a hardware job.

IBM Quantum Platform classic was sunset on July 1, 2025. Use current IBM Quantum Platform endpoints and account flows.

This runtime path intentionally uses robust backend discovery (no hardcoded backend names):

- `service.backends(simulator=False, operational=True, min_num_qubits=5)`
- `service.least_busy(...)`

## 6) Legacy notebook

`notebooks/Qiskitv2_QPU_Min_Example.ipynb` has been updated to the same modern runtime pattern and retained only for compatibility with older references.

## 7) Optional GPU smoke

Run `notebooks/04_aer_gpu_smoke.ipynb` to test optional Aer GPU execution. It will skip cleanly when GPU support is unavailable.

## 8) Official references

- IBM Quantum docs home: <https://docs.quantum.ibm.com/>
- Set up IBM channel: <https://docs.quantum.ibm.com/guides/set-up-channel>
- Qiskit install guide: <https://docs.quantum.ibm.com/guides/install-qiskit>
- Qiskit SDK primitives simulation: <https://docs.quantum.ibm.com/guides/simulate-with-qiskit-sdk-primitives>
- Qiskit Aer simulation: <https://docs.quantum.ibm.com/guides/simulate-with-qiskit-aer>
- Runtime primitives quickstart: <https://docs.quantum.ibm.com/guides/get-started-with-primitives>
- Runtime local testing mode: <https://docs.quantum.ibm.com/guides/local-testing-mode>
- Aer GPU how-to: <https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html>
