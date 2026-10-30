"""Build the standalone Grover preview from an identified Git commit.

Only committed canonical files are read, via ``git archive``. Current working
tree changes do not enter the ZIP. Relative output paths are rooted at the
repository, and existing artifacts are never overwritten. This standard-library
tool does not publish, tag, push, contact services, or execute notebook cells.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
COURSE = "teaching/phys3810-fa2026"
ASSET_NAME = "PHYS3810-Grover-v0.1.0-rc1.zip"
METADATA_NAME = "PHYS3810-Grover-v0.1.0-rc1.metadata.json"
CANONICAL_FILES = (
    "LICENSE",
    "ruff.toml",
    "requirements.txt",
    "requirements-ci.txt",
    "constraints-ci.txt",
    "src/backend_select.py",
    "src/phys3810/__init__.py",
    "src/phys3810/grover.py",
    "tests/test_backend_select.py",
    "tests/test_classroom.py",
    "tests/test_validate_classroom.py",
    "tests/test_grover.py",
    "tests/test_grover_notebook.py",
    "scripts/validate_classroom.py",
    "scripts/smoke_local.sh",
    "notebooks/00_local_statevector_smoke.ipynb",
    "notebooks/01_local_aer_smoke.ipynb",
    f"{COURSE}/notebooks/00_setup_preflight.ipynb",
    f"{COURSE}/notebooks/01_grover.ipynb",
    f"{COURSE}/GROVER_PLAN.md",
    f"{COURSE}/GROVER_VALIDATION.md",
)


def git_output(*arguments: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *arguments], stderr=subprocess.PIPE
    )


def source_snapshot(reference: str) -> tuple[str, int, dict[str, bytes]]:
    """Resolve one commit, then read only regular whitelisted files from its tar."""
    commit = git_output("rev-parse", "--verify", "--end-of-options", f"{reference}^{{commit}}")
    commit = commit.decode("ascii").strip()
    timestamp = int(git_output("show", "-s", "--format=%ct", commit))
    archive = git_output("archive", "--format=tar", commit)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        for name in CANONICAL_FILES:
            try:
                member = bundle.getmember(name)
            except KeyError as error:
                raise ValueError(f"Commit {commit} lacks required preview file: {name}") from error
            if not member.isfile():
                raise ValueError(f"Required preview path is not a regular file: {name}")
            stream = bundle.extractfile(member)
            if stream is None:
                raise ValueError(f"Cannot read required preview file: {name}")
            with stream:
                files[name] = stream.read()
    for name, data in files.items():
        if name.endswith(".ipynb"):
            notebook = json.loads(data)
            for cell in notebook["cells"]:
                if cell["cell_type"] == "code" and (
                    cell.get("execution_count") is not None or cell.get("outputs") != []
                ):
                    raise ValueError(f"Source notebook contains execution state or outputs: {name}")
    return commit, timestamp, files


def orientation_documents(commit: str, include_pdf: bool) -> dict[str, bytes]:
    """Supply concise standalone navigation rather than repository policy/history."""
    pdf_line = (
        "An optional [setup review PDF](docs/PHYS3810_Setup_Review_Draft.pdf) is included.\n"
        if include_pdf else ""
    )
    readme = f"""# PHYS 3810: Grover preview v0.1.0-rc1

Source commit: `{commit}`.

This locally prepared, fixed-source preview contains a credential-free Grover
lesson for 2–5 qubits, independent tests, and onboarding checks. It needs
CPython 3.12 and the pinned packages. Git is not required to use it. Publication
is not established by this archive; use the instructor-supplied ZIP rather
than assuming GitHub main contains this snapshot.

1. Extract the complete ZIP and open its `phys3810-grover` folder.
2. Follow [setup](teaching/phys3810-fa2026/SETUP.md).
3. Run `python scripts/validate_classroom.py` from this folder.
4. Open [preflight](teaching/phys3810-fa2026/notebooks/00_setup_preflight.ipynb),
   then the [Grover lab](teaching/phys3810-fa2026/notebooks/01_grover.ipynb).

Expect **50 passing tests** and four executed notebooks in the identified
Grover preview. Read [the contract](teaching/phys3810-fa2026/GROVER_PLAN.md)
and [validation evidence](teaching/phys3810-fa2026/GROVER_VALIDATION.md) for scope
and limitations. Native Windows/macOS execution remains untested.
{pdf_line}
Before class, restart the kernel and run all cells to verify installation.
During class, restart and clear outputs, discuss each prediction, then execute
its following cell. The lesson has a 50-minute core and 25-minute expansion.

Canonical source, tests, notebooks, dependencies, license, lint configuration,
and technical contract/evidence files are exact copies from the commit above.
This README, the setup page, and short course overview are adapted orientation
documents. The optional setup PDF is an explicitly supplied instructional
asset. No Git metadata, credentials, installed environment, generated notebook
outputs, logs, prompts, or policy/chat history is included.

The regeneration command in the constraints header belongs to the full
repository; its maintainer updater is intentionally omitted. Install the
supplied pinned files without regenerating them for this standalone lab.
"""
    setup = """# Standalone Grover preview setup

Use 64-bit **CPython 3.12**, Qiskit **2.6.1**, and Aer **0.17.2**. Installation
needs internet access; the required notebooks and tests run locally afterward.
No Git, IBM account, credentials, or GPU is required.

## Create the environment

Extract the entire ZIP. In a terminal, change to its `phys3810-grover` folder,
which contains `requirements.txt`, `src/`, `tests/`, `scripts/`, and `teaching/`.
Install CPython 3.12 through the instructor's approved setup first if needed.

Linux/macOS:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

If activation is blocked, use `.\\.venv\\Scripts\\python.exe` in place of
`python` below. On Linux/macOS, `.venv/bin/python` is the direct equivalent.

## Install, validate, and open the notebook

```bash
python --version
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python scripts/validate_classroom.py
python -m ipykernel install --sys-prefix --name phys3810-fa2026 --display-name "Python (PHYS 3810)"
python -m jupyterlab
```

Expect Python `3.12.x`, Qiskit `2.6.1`, Aer `0.17.2`, **50 passing tests**,
four executed notebooks, and `PASSED: classroom validation`. Optional Runtime
and GPU execution is skipped. QFT, QPE, HHL, and Shor are not part of this
Grover preview. Executed copies appear in `artifacts/executed-classroom/`.

Open [preflight](notebooks/00_setup_preflight.ipynb), then
[Grover](notebooks/01_grover.ipynb), and choose **Python (PHYS 3810)**.
Before class, restart the kernel and run all cells to verify the environment.
During class, restart and clear outputs; discuss each prediction before running
the following cell. Expect a labeled circuit, sampled histogram, and iteration
curve. Counts may vary; exact assertions and statistical checks determine success.

## Focused troubleshooting

- Missing files: work from the extracted root and keep all folders together.
- Wrong Python/import error: run `python -c "import sys; print(sys.executable)"`
  and select the matching `.venv` interpreter/kernel. Recreate an incorrectly
  versioned environment with CPython 3.12.
- Terminal passes but notebook fails: choose the registered kernel and restart.
- Plotting fails: reinstall pinned requirements using that kernel's Python.
- Installation requests compilation: check Python version, 64-bit architecture,
  and platform; retain the pins and report the actual error to the instructor.

Native Windows/macOS execution remains untested. See
[the validation record](GROVER_VALIDATION.md) for precise evidence and limits.
"""
    course_plan = """# PHYS 3810 course context for this preview

This standalone export contains Grover, the first algorithm lesson. The planned
invited-session sequence is **Grover; QFT/QPE; HHL/Shor**. The later algorithms
are not included here. Session dates, student preparation, and assessment
expectations remain unconfirmed.

## Grover timing

- 50-minute core: setup/notation (5 minutes), phase oracle (10), diffusion (10),
  single-target lab (20), and exit questions (5).
- 75-minute expansion: add marked-set experiments including the short input
  validation exercise (15 minutes), then overshooting (10).

Install and run preflight before class. In class, clear outputs and discuss
predictions before running each cell. All code runs during validation;
optional expansion discussion does not mean skipped code cells.

Use [the Grover lab](notebooks/01_grover.ipynb), its
[contract](GROVER_PLAN.md), and [validation evidence](GROVER_VALIDATION.md).
These are small, ideal local examples with enumerated targets, without claims
of general search performance or quantum advantage.
"""
    return {
        "README.md": readme.encode("utf-8"),
        f"{COURSE}/SETUP.md": setup.encode("utf-8"),
        f"{COURSE}/COURSE_PLAN.md": course_plan.encode("utf-8"),
    }


def zip_bytes(files: dict[str, bytes], timestamp: int) -> bytes:
    """Use a stable commit timestamp and ordering for reproducible ZIP bytes."""
    date = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    if not 1980 <= date.year <= 2107:
        raise ValueError("Commit timestamp is outside the ZIP date range (1980–2107).")
    payload = io.BytesIO()
    with zipfile.ZipFile(payload, "w") as bundle:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(f"phys3810-grover/{name}", date_time=date.timetuple()[:6])
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    result = payload.getvalue()
    with zipfile.ZipFile(io.BytesIO(result)) as bundle:
        if bundle.testzip() is not None:
            raise ValueError("Generated ZIP failed its CRC integrity check.")
        for name, data in files.items():
            if bundle.read(f"phys3810-grover/{name}") != data:
                raise ValueError(f"Generated ZIP bytes do not match source: {name}")
    return result


def build(reference: str, output_directory: Path, setup_pdf: Path | None) -> dict:
    commit, timestamp, files = source_snapshot(reference)
    canonical_hashes = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    documents = orientation_documents(commit, include_pdf=setup_pdf is not None)
    files.update(documents)
    pdf_hash = None
    if setup_pdf is not None:
        if not setup_pdf.is_file():
            raise ValueError(f"Setup PDF does not exist or is not a file: {setup_pdf}")
        data = setup_pdf.read_bytes()
        if not data.startswith(b"%PDF-"):
            raise ValueError(f"Setup asset does not have a PDF header: {setup_pdf}")
        files["docs/PHYS3810_Setup_Review_Draft.pdf"] = data
        pdf_hash = hashlib.sha256(data).hexdigest()
    payload = zip_bytes(files, timestamp)
    if not output_directory.is_absolute():
        output_directory = ROOT / output_directory
    output_directory = output_directory.resolve()
    archive_path = output_directory / ASSET_NAME
    metadata_path = output_directory / METADATA_NAME
    if archive_path.exists() or metadata_path.exists():
        raise FileExistsError("Preview output already exists; choose a fresh --output-dir.")
    metadata = {
        "source_commit": commit,
        "source_ref": reference,
        "archive": str(archive_path),
        "archive_sha256": hashlib.sha256(payload).hexdigest(),
        "file_count": len(files),
        "canonical_hashes": canonical_hashes,
        "adapted_documents": sorted(documents),
        "setup_pdf_sha256": pdf_hash,
        "expected_test_count": 50,
        "validation_status": "not executed by this builder",
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    with archive_path.open("xb") as output:
        output.write(payload)
    with metadata_path.open("x", encoding="utf-8") as output:
        json.dump(metadata, output, indent=2, sort_keys=True)
        output.write("\n")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True, help="Git commit, tag, or ref for the Grover preview.")
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/grover-preview"))
    parser.add_argument("--setup-pdf", type=Path, help="Optional instructional setup PDF to include.")
    args = parser.parse_args()
    try:
        metadata = build(args.ref, args.output_dir, args.setup_pdf)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.decode("utf-8", errors="replace").strip() if error.stderr else str(error)
        parser.exit(2, f"Git source snapshot failed: {detail}\n")
    except (OSError, ValueError, KeyError, tarfile.TarError) as error:
        parser.exit(2, f"Preview build failed: {error}\n")
    print(json.dumps({key: metadata[key] for key in (
        "source_commit", "archive", "archive_sha256", "file_count", "validation_status"
    )}, indent=2))


if __name__ == "__main__":
    main()
