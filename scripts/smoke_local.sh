#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="${1:-artifacts/executed-local-smoke}"
TIMEOUT="${NB_TIMEOUT:-300}"
LOG_FILE="${OUT_DIR}/smoke_local.log"

if ! command -v jupyter >/dev/null 2>&1; then
  echo "jupyter is not installed. Install dependencies first: pip install -r requirements.txt" >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"
: > "${LOG_FILE}"

export IPYTHONDIR="${IPYTHONDIR:-/tmp/qiskit-v2-ipython}"
export JUPYTER_CONFIG_DIR="${JUPYTER_CONFIG_DIR:-/tmp/qiskit-v2-jupyter-config}"
export JUPYTER_DATA_DIR="${JUPYTER_DATA_DIR:-/tmp/qiskit-v2-jupyter-data}"
export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/tmp/qiskit-v2-runtime}"
mkdir -p "${IPYTHONDIR}" "${JUPYTER_CONFIG_DIR}" "${JUPYTER_DATA_DIR}" "${XDG_RUNTIME_DIR}"

NOTEBOOKS=(
  "notebooks/00_local_statevector_smoke.ipynb"
  "notebooks/01_local_aer_smoke.ipynb"
)

for nb in "${NOTEBOOKS[@]}"; do
  echo "=== Executing ${nb} ===" | tee -a "${LOG_FILE}"
  jupyter nbconvert \
    --to notebook \
    --execute \
    --ExecutePreprocessor.timeout="${TIMEOUT}" \
    --output-dir "${OUT_DIR}" \
    "${nb}" >> "${LOG_FILE}" 2>&1
  echo "=== Done ${nb} ===" | tee -a "${LOG_FILE}"

done

echo "Local smoke notebooks executed successfully. Output: ${OUT_DIR}" | tee -a "${LOG_FILE}"
