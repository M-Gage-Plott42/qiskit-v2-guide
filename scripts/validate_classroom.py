"""Run the credential-free classroom checks with this Python interpreter.

Usage from any working directory: python /path/to/repo/scripts/validate_classroom.py
Executed notebooks are written to artifacts/executed-classroom, never over sources.
"""

from __future__ import annotations

import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT_NOTEBOOK = "teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb"
GROVER_NOTEBOOK = "teaching/phys3810-fa2026/notebooks/01_grover.ipynb"
NOTEBOOKS = (
    PREFLIGHT_NOTEBOOK,
    "notebooks/00_local_statevector_smoke.ipynb",
    "notebooks/01_local_aer_smoke.ipynb",
    GROVER_NOTEBOOK,
)
REQUIRED_PNGS = {PREFLIGHT_NOTEBOOK: 2, GROVER_NOTEBOOK: 3}
EXPECTED = {"qiskit": "2.6.1", "qiskit-aer": "0.17.2"}


def validate_required_cells(notebook, *, executed: bool = False) -> None:
    """Reject omitted required code and, after execution, incomplete/error output."""
    for number, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type != "code":
            continue
        if cell.source.strip():
            if "skip-execution" in cell.metadata.get("tags", []):
                raise RuntimeError(
                    f"Required code cell {number} has the 'skip-execution' tag. "
                    "Remove that tag: every nonempty classroom code cell must execute."
                )
            if executed and cell.execution_count is None:
                raise RuntimeError(f"Required code cell {number} has no execution count.")
        if executed and any(item.output_type == "error" for item in cell.outputs):
            raise RuntimeError(f"Code cell {number} retains an error output after execution.")


def check_environment() -> None:
    """Reject the wrong interpreter or core versions before starting kernels."""
    print(f"Python: {sys.version.split()[0]} ({sys.executable})", flush=True)
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("Use CPython 3.12 and the classroom requirements.")
    if sys.implementation.name != "cpython":
        raise RuntimeError("The classroom environment requires CPython.")
    for package, expected in EXPECTED.items():
        actual = importlib.metadata.version(package)
        print(f"{package}: {actual}", flush=True)
        if actual != expected:
            raise RuntimeError(f"Expected {package}=={expected}; found {actual}.")
    subprocess.run([sys.executable, "-m", "pip", "check"], check=True, cwd=ROOT)


def execute_notebooks() -> int:
    """Give every notebook a new kernel bound to sys.executable, not a saved kernel."""
    import nbformat
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager
    from nbclient import NotebookClient

    output = ROOT / "artifacts" / "executed-classroom"
    output.mkdir(parents=True, exist_ok=True)
    failures = 0
    with tempfile.TemporaryDirectory(prefix="phys3810-kernel-") as directory:
        temporary = Path(directory)
        kernels = temporary / "kernels"
        specification = kernels / "phys3810-validation"
        specification.mkdir(parents=True)
        (specification / "kernel.json").write_text(
            json.dumps(
                {
                    "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
                    "display_name": "PHYS 3810 validation",
                    "language": "python",
                }
            ),
            encoding="utf-8",
        )
        environment = os.environ.copy()
        # Keep notebook caches and connection files out of a user's Jupyter setup.
        for variable, folder in (
            ("IPYTHONDIR", "ipython"),
            ("JUPYTER_CONFIG_DIR", "jupyter-config"),
            ("JUPYTER_DATA_DIR", "jupyter-data"),
            ("JUPYTER_RUNTIME_DIR", "jupyter-runtime"),
            ("MPLCONFIGDIR", "matplotlib"),
        ):
            path = temporary / folder
            path.mkdir()
            environment[variable] = str(path)
        environment["MPLBACKEND"] = "Agg"
        for relative in NOTEBOOKS:
            notebook = nbformat.read(ROOT / relative, as_version=4)
            # Strip stale output before execution, even if a contributor saved it.
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    cell.outputs = []
                    cell.execution_count = None
            manager = KernelManager(
                kernel_name="phys3810-validation",
                kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(kernels)]),
                connection_file=str(temporary / "connection.json"),
            )
            client = NotebookClient(
                notebook, km=manager, timeout=300, allow_errors=False,
                force_raise_errors=True, skip_cells_with_tag="skip-execution",
            )
            print(f"Running fresh kernel: {relative}", flush=True)
            try:
                validate_required_cells(notebook)
                client.execute(cwd=str(ROOT), env=environment, cleanup_kc=True)
                validate_required_cells(notebook, executed=True)
                if relative in REQUIRED_PNGS:
                    images = sum(
                        "image/png" in item.get("data", {})
                        for cell in notebook.cells
                        if cell.cell_type == "code"
                        for item in cell.outputs
                    )
                    if images < REQUIRED_PNGS[relative]:
                        raise RuntimeError(
                            f"{relative} must render at least {REQUIRED_PNGS[relative]} PNG figures; "
                            f"found {images}."
                        )
            except Exception as error:
                failures += 1
                print(f"FAILED: {relative}: {type(error).__name__}: {error}", flush=True)
            else:
                print(f"PASSED: {relative}", flush=True)
            finally:
                # Preserve partial output on failure for diagnosis.
                nbformat.write(notebook, output / Path(relative).name)
    print(f"Executed notebooks: {output}", flush=True)
    return failures


def main() -> int:
    try:
        check_environment()
    except Exception as error:
        print(f"FAILED: environment: {error}", flush=True)
        print("UNTESTED: unit tests and notebooks (environment check failed).", flush=True)
        return 1
    print("PASSED: environment and dependency consistency", flush=True)
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        check=False,
    )
    failures = int(result.returncode != 0)
    print(f"{'FAILED' if failures else 'PASSED'}: offline unit tests", flush=True)
    try:
        failures += execute_notebooks()
    except Exception as error:
        failures += 1
        print(f"FAILED: notebook runner: {type(error).__name__}: {error}", flush=True)
    print("SKIPPED: optional IBM Runtime and GPU execution (outside classroom defaults).", flush=True)
    print("UNTESTED: QFT, QPE, HHL, and Shor lessons (not implemented yet).", flush=True)
    print(f"{'FAILED' if failures else 'PASSED'}: classroom validation", flush=True)
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
