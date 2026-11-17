"""Export one committed, runnable PHYS 3810 Canvas notebook kit.

This existing review exporter does not modify the frozen release builders or execute
notebooks. The caller supplies measured source-validation evidence, then must
validate the exact extracted ZIP separately before handing it over.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
COURSE = "teaching/phys3810-fa2026"
BUILDER_PATH = "scripts/build_guided_review.py"
VALIDATOR_PATH = "scripts/validate_classroom.py"
# Bind profile requirements to the validator beside this builder, never execute
# Python recovered from a historical Git blob. source_snapshot checks identity.
VALIDATOR_SOURCE = (ROOT / VALIDATOR_PATH).read_bytes()
_validator_spec = importlib.util.spec_from_file_location(
    "_guided_export_validator", ROOT / VALIDATOR_PATH,
)
classroom_validator = importlib.util.module_from_spec(_validator_spec)
_validator_spec.loader.exec_module(classroom_validator)
TOP_DIRECTORY = "phys3810-canvas-kit"
KIT_VERSION = "v0.1"
ENTRANCE_NAMES = ("START_HERE.md",)
ENTRANCE_PATHS = tuple(f"{COURSE}/intro/{name}" for name in ENTRANCE_NAMES)
REFERENCE_NOTEBOOKS = tuple(classroom_validator.NOTEBOOKS)
GUIDED_NOTEBOOKS = tuple(classroom_validator.GUIDED_NOTEBOOKS)
INTRO_NOTEBOOKS = tuple(classroom_validator.INTRO_NOTEBOOKS)
NOTEBOOKS = (*REFERENCE_NOTEBOOKS, *GUIDED_NOTEBOOKS, *INTRO_NOTEBOOKS)
DEMONSTRATED_NOTEBOOKS = (
    *INTRO_NOTEBOOKS,
    classroom_validator.QFT_NOTEBOOK,
    classroom_validator.QPE_NOTEBOOK,
    classroom_validator.HHL_NOTEBOOK,
)
OPTIONAL_ALGORITHM_NOTEBOOKS = (
    classroom_validator.GROVER_NOTEBOOK, classroom_validator.SHOR_NOTEBOOK,
)
STUDENT_PDF = f"{COURSE}/handouts/recording-v0.2/PHYS3810_Student_Guide_v0.2.pdf"
STUDENT_MARKDOWN = f"{COURSE}/handouts/recording-v0.2/PHYS3810_Student_Guide_v0.2.md"
# Full delivered bytes, including any provenance; these identify the matching
# edition in the supplied 727cb98 recording-packet DELIVERY_RECEIPT.json.
STUDENT_GUIDE_HASHES = {
    STUDENT_PDF: "fbfeed02287a5edfe472c19e607fbffc584a73d827893bd36dc3f8ab9e587bad",
    STUDENT_MARKDOWN: "ae4ef2380af869481e8b1c4af38a2e6c45de41e5874ac7eca4b9f7d6e1c19830",
}
RUNTIME_FILES = (
    "LICENSE", "ruff.toml", "requirements.txt", "requirements-ci.txt", "constraints-ci.txt",
    VALIDATOR_PATH, "scripts/smoke_local.sh", BUILDER_PATH, *NOTEBOOKS, *STUDENT_GUIDE_HASHES,
)
CONTRACT_END_MARKERS = {
    "GROVER": "The completed lesson's independent review",
    "QFT": " The combined QFT/QPE review is accepted;",
    "QPE": None,
    "HHL": "Classical design checks confirmed",
    "SHOR": "Classical design checks confirmed",
}
CONTRACT_PATHS = tuple(f"{COURSE}/{stem}_PLAN.md" for stem in CONTRACT_END_MARKERS)
EXPECTED_BASELINE_TESTS = {
    f"tests/test_{name}.py" for name in (
        "backend_select", "classroom", "validate_classroom", "grover", "grover_notebook",
        "qft", "qft_notebook", "qpe", "qpe_notebook", "hhl", "hhl_notebook",
        "shor", "shor_notebook", "guided_notebooks", "guided_validation",
        "guided_review_package", "intro_notebooks",
    )
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_output(*arguments: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *arguments], stderr=subprocess.PIPE,
        env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"),
    )


def source_snapshot(reference: str) -> tuple[str, str, int, dict[str, bytes]]:
    """Read a regular-file allowlist directly from Git blobs, never the worktree."""
    commit = git_output(
        "rev-parse", "--verify", "--end-of-options", f"{reference}^{{commit}}"
    ).decode("ascii").strip()
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected a resolved SHA-1 commit.")
    tree = git_output("rev-parse", f"{commit}^{{tree}}").decode("ascii").strip()
    timestamp = int(git_output("show", "-s", "--format=%ct", commit))
    entries = {}
    for record in git_output("ls-tree", "-r", "-z", commit).decode("utf-8").split("\0"):
        if record:
            header, name = record.split("\t", 1)
            mode, kind, blob = header.split()
            entries[name] = (mode, kind, blob)
    # Include every committed Python implementation/regression under these two
    # explicit roots. Newly added tests cannot disappear through a stale list.
    python_paths = {
        name for name in entries if name.startswith(("src/", "tests/")) and name.endswith(".py")
    }
    if not EXPECTED_BASELINE_TESTS <= python_paths:
        raise ValueError("Committed snapshot omits a baseline regression file.")
    required = set(RUNTIME_FILES) | set(ENTRANCE_PATHS) | set(CONTRACT_PATHS) | python_paths
    inputs = {}
    for name in sorted(required):
        if name not in entries:
            raise ValueError(f"Missing committed review input: {name}")
        mode, kind, blob = entries[name]
        if mode not in ("100644", "100755") or kind != "blob":
            raise ValueError(f"Review input must be a regular file: {name}")
        inputs[name] = git_output("cat-file", "blob", blob)
    if inputs[BUILDER_PATH] != Path(__file__).read_bytes():
        raise ValueError("Executing builder differs from selected commit; use its committed builder.")
    if inputs[VALIDATOR_PATH] != VALIDATOR_SOURCE:
        raise ValueError("Imported validator differs from selected commit; use its committed validator.")
    return commit, tree, timestamp, inputs


def validate_source_notebooks(inputs: dict[str, bytes]) -> int:
    """Require the complete selected inventory and output-free source."""
    cells = 0
    for name in NOTEBOOKS:
        notebook = json.loads(inputs[name])
        for cell in notebook["cells"]:
            if cell["cell_type"] != "code":
                continue
            if cell.get("execution_count") is not None or cell.get("outputs") != []:
                raise ValueError(f"Source notebook contains stored execution state: {name}")
            source = cell["source"]
            if isinstance(source, list):
                source = "".join(source)
            if not isinstance(source, str):
                raise ValueError(f"Notebook source must be text: {name}")
            if source.strip():
                if "skip-execution" in cell.get("metadata", {}).get("tags", []):
                    raise ValueError(f"Required source cell is marked skip-execution: {name}")
                cells += 1
    return cells


def validate_student_guides(inputs: dict[str, bytes]) -> None:
    """Require the exact synchronized student edition, not a regenerated copy."""
    for path, expected in STUDENT_GUIDE_HASHES.items():
        if path not in inputs or digest(inputs[path]) != expected:
            raise ValueError(f"Student guide does not match the delivered edition: {path}")


def validate_evidence(evidence: dict, commit: str, cells: int) -> None:
    """Check receipt counts against the profile matched by source_snapshot."""
    profile = classroom_validator.notebooks_for_profile("all")
    if len(profile) != len(NOTEBOOKS) or set(profile) != set(NOTEBOOKS):
        raise ValueError("Exporter notebook inventory differs from the validator's all profile.")
    minimum_pngs = sum(classroom_validator.REQUIRED_PNGS.get(name, 0) for name in profile)
    if evidence.get("source_commit") != commit:
        raise ValueError("Validation evidence must identify the selected full commit.")
    for field in ("python", "platform", "environment_details"):
        if not isinstance(evidence.get(field), str) or not evidence[field].strip():
            raise ValueError(f"Missing validation evidence: {field}")
    if not evidence["python"].startswith("3.12."):
        raise ValueError("Evidence must use CPython 3.12.")
    if evidence.get("environment_status") not in ("fresh", "reused"):
        raise ValueError("Disclose a fresh or reused environment.")
    if evidence.get("results", {}).get("all_profile_validator") != "passed":
        raise ValueError("The all-profile source validator must have passed.")
    counts = evidence.get("counts", {})
    if (counts.get("notebooks") != len(profile) or counts.get("nonempty_code_cells") != cells
            or not isinstance(counts.get("tests"), int) or counts["tests"] < 160
            or not isinstance(counts.get("pngs"), int) or counts["pngs"] < minimum_pngs):
        raise ValueError("Executed evidence does not match the required notebook/cell inventory.")
    for field in ("commands", "limitations"):
        if (not isinstance(evidence.get(field), list) or not evidence[field]
                or not all(isinstance(item, str) for item in evidence[field])):
            raise ValueError(f"Evidence requires a nonempty string list: {field}")
    if not isinstance(evidence.get("versions"), dict) or not evidence["versions"]:
        raise ValueError("Evidence requires installed package versions.")


def adapt_entrance_links(text: str, source: str, destinations: dict[str, str]) -> str:
    """Translate repository-relative Markdown targets into the standalone layout."""
    def replace(match):
        target = match.group(2).strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parsed.path)))
        if resolved not in destinations:
            raise ValueError(f"Entrance link targets an excluded input: {source}: {target}")
        rewritten = destinations[resolved]
        if parsed.fragment:
            rewritten += "#" + parsed.fragment
        return f"{match.group(1)}{rewritten})"

    return re.sub(r"(\[[^\]]*\]\()([^\s)]+)\)", replace, text)


def contract_body(original: bytes, stem: str) -> bytes:
    text = original.decode("utf-8")
    if "## " not in text:
        raise ValueError(f"Technical contract body not found: {stem}")
    body = text[text.index("## "):]
    marker = CONTRACT_END_MARKERS[stem]
    if marker is not None:
        if marker not in body:
            raise ValueError(f"Technical contract boundary changed: {stem}")
        body = body.split(marker, 1)[0]
    return (body.rstrip() + "\n").encode("utf-8")


def validation_markdown(evidence: dict) -> bytes:
    counts = evidence["counts"]
    lines = [
        "# Canvas kit validation evidence", "",
        "This kit matches the teaching route for recording and Canvas delivery; it is not a public release.",
        f"Source commit: `{evidence['source_commit']}`.", "",
        "## Recorded source execution", "",
        "The caller supplied these measured results; the export builder does not execute notebooks.",
        f"CPython: {evidence['python']}. Platform: {evidence['platform']}.",
        f"Environment: **{evidence['environment_status']}**. {evidence['environment_details']}", "",
        f"Passed source inventory: **{counts['tests']} tests, {counts['notebooks']} notebooks, "
        f"{counts['nonempty_code_cells']} nonempty code cells, {counts['pngs']} PNGs**.",
        f"The {len(DEMONSTRATED_NOTEBOOKS)} demonstrated notebooks are QRNG, Bell, QFT, QPE, and HHL.",
        f"All {len(NOTEBOOKS)} notebooks remain in the kit, including "
        f"{len(GUIDED_NOTEBOOKS)} earlier guided notebooks as support material.",
        "Grover and the compiled N=15 Shor example remain optional exploration.",
        "Setup targets 15–20 minutes; total video duration is flexible. Delivery is through Canvas.",
        "All canonical algorithms retain their documented bounds.", "",
        "Commands run:", "", "```text", *evidence["commands"], "```", "",
        "Results:", "", *[f"- {name}: {value}." for name, value in sorted(evidence["results"].items())],
        "", "Installed versions:", "",
        *[f"- {name}: {value}." for name, value in sorted(evidence["versions"].items())], "",
        "## Exact archive verification", "",
        "The builder checks paths, links, clean notebook sources, and committed bytes.",
        "The final extracted ZIP must additionally pass `python scripts/validate_classroom.py --profile all`",
        "from `runtime/`, with imports confined to that extraction and payload hashes unchanged.",
        "That post-export execution receipt is recorded outside this sealed ZIP; this file does not",
        "claim the builder performed it. The manifest omits itself and the containing ZIP.", "",
        "## Limits", "", *[f"- {item}" for item in evidence["limitations"]], "",
        "Installation requires internet. Default lessons run locally without credentials.",
        "Human pacing, unavailable native platforms/editor UI, GPU, Runtime, and hardware are not",
        "established by headless local validation. Worked examples are intentionally complete.", "",
    ]
    return "\n".join(lines).encode("utf-8")


def payload_files(inputs: dict[str, bytes], commit: str, evidence: dict) -> tuple[dict, dict]:
    files, origins = {}, {}
    runtime_paths = set(RUNTIME_FILES) | {
        name for name in inputs if name.startswith(("src/", "tests/")) and name.endswith(".py")
    }
    destinations = {name: f"runtime/{name}" for name in runtime_paths | set(CONTRACT_PATHS)}
    destinations.update(dict(zip(ENTRANCE_PATHS, ENTRANCE_NAMES, strict=True)))
    destinations.update({f"{COURSE}/{name}.md": f"runtime/{COURSE}/{name}.md"
                         for name in ("SETUP", "COURSE_PLAN")})
    for name in sorted(runtime_paths):
        target = destinations[name]
        files[target] = inputs[name]
        origins[target] = {"kind": "exact committed bytes", "source_path": name,
                           "source_sha256": digest(inputs[name])}
    for source, target in zip(ENTRANCE_PATHS, ENTRANCE_NAMES, strict=True):
        files[target] = adapt_entrance_links(inputs[source].decode("utf-8"), source, destinations).encode("utf-8")
        files[target] += (
            f"\n## Matching student guide\n\n[Student guide PDF]({destinations[STUDENT_PDF]}) "
            f"and [synchronized Markdown]({destinations[STUDENT_MARKDOWN]}).\n"
        ).encode("utf-8")
        origins[target] = {"kind": "committed Markdown; standalone and student-guide navigation adapted",
                           "source_path": source, "source_sha256": digest(inputs[source])}
        # Jupyter starts in runtime/, so a notebook cannot follow a redirect
        # to the outer review guide. The original layout keeps all source
        # quickstart/menu links usable inside that served directory.
        inner = f"runtime/{source}"
        files[inner] = inputs[source]
        origins[inner] = {"kind": "exact committed bytes", "source_path": source,
                          "source_sha256": digest(inputs[source])}
    for stem in CONTRACT_END_MARKERS:
        source = f"{COURSE}/{stem}_PLAN.md"
        body = contract_body(inputs[source], stem)
        header = (
            inputs[source].decode("utf-8").splitlines()[0] + "\n\n"
            f"Technical reference from `{commit}`. Older lesson timing and regression counts\n"
            "inside these reference contracts do not define the single-class route.\n"
            "Use [the quickstart](intro/START_HERE.md) for that route\n"
            "and [current validation evidence](../../VALIDATION.md) for measured totals.\n\n"
        )
        target = destinations[source]
        files[target] = header.encode("utf-8") + body
        origins[target] = {"kind": "technical body exact; navigation/history adapted",
                           "source_path": source, "source_sha256": digest(inputs[source]),
                           "retained_body_sha256": digest(body)}
    for name, title in (
        ("SETUP", "Runtime setup"),
        ("COURSE_PLAN", "Single-class route"),
    ):
        target = f"runtime/{COURSE}/{name}.md"
        files[target] = (
            f"# {title}\n\nSee [the quickstart](intro/START_HERE.md) for the current single-class route.\n"
            f"This runtime tree contains all {len(NOTEBOOKS)} teaching/reference notebooks and the complete\n"
            f"bounded five-algorithm library. The {len(DEMONSTRATED_NOTEBOOKS)} demonstrated notebooks\n"
            "follow QRNG → Bell → QFT → QPE → HHL. Grover and compiled N=15 Shor remain optional;\n"
            "the earlier guided notebooks are support material. Setup targets 15–20 minutes;\n"
            "total video duration is flexible. The matching kit and video are delivered through Canvas.\n\n"
            "See the [student guide PDF](handouts/recording-v0.2/PHYS3810_Student_Guide_v0.2.pdf)\n"
            "and [synchronized Markdown](handouts/recording-v0.2/PHYS3810_Student_Guide_v0.2.md).\n"
        ).encode("utf-8")
        origins[target] = {"kind": "generated standalone navigation", "source_path": BUILDER_PATH,
                           "source_sha256": digest(inputs[BUILDER_PATH])}
    files["runtime/VALIDATION.md"] = validation_markdown(evidence)
    origins["runtime/VALIDATION.md"] = {"kind": "generated from supplied execution receipt",
                                        "evidence_sha256": digest(json.dumps(evidence, sort_keys=True).encode())}
    return files, origins


def markdown_anchors(text: str) -> set[str]:
    anchors, seen = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).strip().replace(" ", "-")
        number = seen.get(slug, 0)
        anchors.add(f"{slug}-{number}" if number else slug)
        seen[slug] = number + 1
    return anchors


def validate_payload(files: dict[str, bytes]) -> int:
    """Reject excluded paths and broken or outside-served-root navigation."""
    folded = set()
    forbidden = {"artifacts", "__pycache__", "node_modules", "instructor", "handouts"}
    student_paths = {f"runtime/{name}": expected for name, expected in STUDENT_GUIDE_HASHES.items()}
    present_guides = set(student_paths) & set(files)
    if present_guides:
        if present_guides != set(student_paths):
            raise ValueError("The student PDF and synchronized Markdown must be included together.")
        for name, expected in student_paths.items():
            if digest(files[name]) != expected:
                raise ValueError(f"Student guide payload differs from delivered bytes: {name}")
    for name in files:
        parts = name.split("/")
        if (PurePosixPath(name).is_absolute() or any(part in ("", ".", "..") for part in parts)
                or "\\" in name or ":" in name or name.casefold() in folded):
            raise ValueError(f"Unsafe or case-colliding path: {name}")
        if (name not in student_paths and (
                forbidden.intersection(parts) or any(part.startswith(".") for part in parts)
                or name.lower().endswith((".pdf", ".docx", ".zip", ".pyc"))
                or any(part.upper() in ("AGENTS.MD", "WORKFLOW.MD") for part in parts))):
            raise ValueError(f"Excluded review payload: {name}")
        folded.add(name.casefold())
    anchors = {name: markdown_anchors(data.decode("utf-8")) for name, data in files.items()
               if name.endswith(".md")}
    count = 0
    for name, data in files.items():
        if name.endswith(".md"):
            text = data.decode("utf-8")
        elif name.endswith(".ipynb"):
            text = "\n".join("".join(cell["source"]) for cell in json.loads(data)["cells"]
                             if cell["cell_type"] == "markdown")
        else:
            continue
        text = re.sub(r"^```.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)
        for target in re.findall(r"\[[^]]*\]\(([^\s)]+)\)", text):
            link = urlsplit(target.strip("<>"))
            if link.netloc and not link.scheme:
                raise ValueError(f"Protocol-relative URL: {name}: {target}")
            if link.scheme:
                if (link.scheme not in ("http", "https") or not link.hostname
                        or link.username or link.password):
                    raise ValueError(f"Unsupported external URL: {name}: {target}")
                continue
            destination = (posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(link.path)))
                           if link.path else name)
            if name.startswith("runtime/") and not destination.startswith("runtime/"):
                raise ValueError(f"Local link leaves the Jupyter runtime root: {name}: {target}")
            if destination not in files and destination != "MANIFEST.json":
                raise ValueError(f"Missing local link target: {name}: {target}")
            if (link.fragment and destination.endswith(".md")
                    and unquote(link.fragment) not in anchors[destination]):
                raise ValueError(f"Missing Markdown heading: {name}: {target}")
            count += 1
    return count


def portable_mode(name: str) -> str:
    return "0755" if name == "runtime/scripts/smoke_local.sh" else "0644"


def zip_bytes(files: dict[str, bytes], timestamp: int) -> bytes:
    date = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    if not 1980 <= date.year <= 2107:
        raise ValueError("Commit timestamp is outside the ZIP date range.")
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(f"{TOP_DIRECTORY}/{name}", date.timetuple()[:6])
            info.create_system = 3
            info.external_attr = (0o100000 | int(portable_mode(name), 8)) << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return output.getvalue()


def build(reference: str, output_directory: Path, evidence: dict) -> dict:
    commit, tree, timestamp, inputs = source_snapshot(reference)
    cells = validate_source_notebooks(inputs)
    validate_student_guides(inputs)
    validate_evidence(evidence, commit, cells)
    files, origins = payload_files(inputs, commit, evidence)
    links = validate_payload(files)
    manifest = {
        "schema": "phys3810.canvas-kit.v1", "kit_version": KIT_VERSION,
        "purpose": "matching notebook kit for recording and Canvas delivery; not a public release",
        "source_commit": commit, "source_tree": tree, "working_tree_payload": False,
        "top_directory": TOP_DIRECTORY, "classroom_notebooks": len(DEMONSTRATED_NOTEBOOKS),
        "total_notebooks": len(NOTEBOOKS),
        "demonstrated_notebooks": [f"runtime/{name}" for name in DEMONSTRATED_NOTEBOOKS],
        "optional_algorithm_notebooks": [f"runtime/{name}" for name in OPTIONAL_ALGORITHM_NOTEBOOKS],
        "student_guides": {f"runtime/{name}": expected for name, expected in STUDENT_GUIDE_HASHES.items()},
        "manifest_excludes_itself_and_archive": True,
        "builder": {"source_path": BUILDER_PATH, "source_sha256": digest(inputs[BUILDER_PATH])},
        "source_execution_counts": evidence["counts"],
        "source_environment_status": evidence["environment_status"],
        "export_validation": "static paths/links/bytes checked; exact extracted execution required separately",
        "files": {name: {"bytes": len(data), "sha256": digest(data), "mode": portable_mode(name),
                         **origins[name]} for name, data in sorted(files.items())},
    }
    files["MANIFEST.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    payload = zip_bytes(files, timestamp)
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(files):
            raise ValueError("Generated ZIP failed integrity or inventory checks.")
        for name, data in files.items():
            if archive.read(f"{TOP_DIRECTORY}/{name}") != data:
                raise ValueError(f"Generated archive payload differs: {name}")
    output_directory = output_directory.resolve()
    asset_name = f"PHYS3810-Canvas-Kit-{KIT_VERSION}-{commit[:12]}.zip"
    archive_path = output_directory / asset_name
    metadata_path = archive_path.with_suffix(".metadata.json")
    if any(path.exists() or path.is_symlink() for path in (archive_path, metadata_path)):
        raise FileExistsError("Review output exists; use a fresh output directory.")
    metadata = {
        "source_commit": commit, "source_tree": tree, "archive": str(archive_path),
        "archive_bytes": len(payload), "archive_sha256": digest(payload),
        "file_count": len(files), "manifest_entries": len(manifest["files"]),
        "relative_links_checked": links, "notebooks": len(NOTEBOOKS),
        "nonempty_code_cells": cells, "source_execution_counts": evidence["counts"],
        "environment_status": evidence["environment_status"],
        "extracted_execution": "not performed by builder; required before delivery",
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    with archive_path.open("xb") as stream:
        stream.write(payload)
    with metadata_path.open("x", encoding="utf-8") as stream:
        json.dump(metadata, stream, indent=2)
        stream.write("\n")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True, help="Commit containing this exact builder and all review inputs.")
    parser.add_argument("--evidence", type=Path, required=True, help="Measured source-execution JSON receipt.")
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/canvas-kit"))
    args = parser.parse_args()
    try:
        evidence = json.loads(args.evidence.read_text(encoding="utf-8"))
        metadata = build(args.ref, args.output_dir, evidence)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.decode("utf-8", errors="replace").strip() if error.stderr else str(error)
        parser.exit(2, f"Git source snapshot failed: {detail}\n")
    except (OSError, ValueError, KeyError, TypeError, SyntaxError, zipfile.BadZipFile) as error:
        parser.exit(2, f"Canvas kit export failed: {error}\n")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
