#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Compatibility entry point; activate a Python 3.12 maintainer environment first.
python "${SCRIPT_DIR}/update_constraints_ci.py"
