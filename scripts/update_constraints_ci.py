"""Resolve the complete CPython 3.12 CPU + optional Runtime environment.

Maintainer tool only: python -m pip install uv==0.13.6
Students install requirements.txt using pip and need neither uv nor Git.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if sys.version_info[:2] != (3, 12):
        raise SystemExit("Use Python 3.12 to regenerate classroom constraints.")
    # Ignore include/constraint directives so the old lock cannot constrain an update.
    dependencies = []
    for name in ("requirements.txt", "requirements-runtime.txt"):
        for line in (ROOT / name).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith(("#", "-")):
                dependencies.append(line)
    with tempfile.TemporaryDirectory(prefix="phys3810-lock-") as directory:
        project = Path(directory) / "pyproject.toml"
        project.write_text(
            '[project]\nname = "phys3810-environment"\nversion = "0.0.0"\n'
            'requires-python = "==3.12.*"\ndependencies = '
            + json.dumps(dependencies) + "\n",
            encoding="utf-8",
        )
        output = Path(directory) / "constraints.txt"
        subprocess.run(
            [sys.executable, "-m", "uv", "pip", "compile", str(project),
             "--universal", "--python-version", "3.12", "--no-annotate",
             "--no-header", "--output-file", str(output)],
            check=True,
        )
        version = subprocess.check_output(
            [sys.executable, "-m", "uv", "--version"], text=True
        ).strip()
        (ROOT / "constraints-ci.txt").write_text(
            "# Complete universal resolution for CPython 3.12 (CPU + optional Runtime).\n"
            f"# Generated with {version}; platform markers are intentional.\n"
            "# Regenerate: python scripts/update_constraints_ci.py\n"
            "# Revalidate from fresh environments before accepting this file.\n\n"
            + output.read_text(encoding="utf-8"), encoding="utf-8",
        )


if __name__ == "__main__":
    main()
