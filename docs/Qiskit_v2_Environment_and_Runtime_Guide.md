# Qiskit 2.x Environment and Runtime Guide

Updated: February 10, 2026

This guide replaces the older PDF setup notes and aligns with current IBM Quantum/Qiskit documentation.

## 1) Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Install core packages

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Optional extras used in broader workflows:

```bash
python -m pip install "qiskit-algorithms>=0.4.0" "qiskit-optimization>=0.7.0"
```

## 3) (Optional) Register a dedicated Jupyter kernel

```bash
python -m ipykernel install --user --name qiskit2 --display-name "Python (qiskit2)"
```

## 4) No-account local smoke tests (recommended first)

Run these first to validate local setup without IBM credentials:

1. `notebooks/00_local_statevector_smoke.ipynb`
2. `notebooks/01_local_aer_smoke.ipynb`
3. `notebooks/03_runtime_local_testing_mode.ipynb`

## 5) IBM Runtime smoke test (optional cloud path)

1. Create or sign in to IBM Quantum at <https://quantum.cloud.ibm.com/>.
2. Create/get an instance and API key in IBM Quantum Platform.
3. Copy `.env.example` to `.env` and fill values:

```dotenv
API_KEY=YOUR_IBM_QUANTUM_API_KEY
INSTANCE=YOUR_INSTANCE_CRN
CHANNEL=ibm_quantum_platform
```

4. Run `notebooks/02_ibm_runtime_smoke.ipynb`.

This runtime path intentionally uses robust backend discovery (no hardcoded backend names):
- `service.backends(simulator=False, operational=True, min_num_qubits=5)`
- `service.least_busy(...)`

## 6) Legacy notebook

`notebooks/Qiskitv2_QPU_Min_Example.ipynb` has been updated to the same modern runtime pattern and retained only for compatibility with older references.

## 7) Optional GPU smoke

Run `notebooks/04_aer_gpu_smoke.ipynb` to test optional Aer GPU execution. It will skip cleanly when GPU support is unavailable.

## 8) Official references

- IBM Quantum docs home: <https://quantum.cloud.ibm.com/docs/en>
- Set up IBM channel: <https://quantum.cloud.ibm.com/docs/en/guides/set-up-channel>
- Qiskit SDK primitives simulation: <https://quantum.cloud.ibm.com/docs/en/guides/simulate-with-qiskit-sdk-primitives>
- Qiskit Aer simulation: <https://quantum.cloud.ibm.com/docs/en/guides/simulate-with-qiskit-aer>
- Runtime primitives quickstart: <https://quantum.cloud.ibm.com/docs/en/guides/get-started-with-primitives>
- Runtime local testing mode: <https://quantum.cloud.ibm.com/docs/en/guides/local-testing-mode>
- Aer GPU how-to: <https://qiskit.github.io/qiskit-aer/howtos/running_gpu.html>
