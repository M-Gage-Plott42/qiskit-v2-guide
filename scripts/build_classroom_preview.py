"""Build the bounded full-course local preview from one committed snapshot.

The builder, templates, reviewed student documents, and runtime payload must
belong to the same resolved commit. No working-tree payload, instructor guide,
PDF renderer, network operation, or notebook execution enters this build.
The caller must separately validate an extracted archive before reporting a pass.
"""

from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import tarfile
from urllib.parse import unquote, urlsplit
import zipfile


ROOT = Path(__file__).resolve().parents[1]
COURSE = "teaching/phys3810-fa2026"
BUILDER_PATH = "scripts/build_classroom_preview.py"
TOP_DIRECTORY = "phys3810-fa2026"
CODE_VERSION = "v0.2.0-rc1"
STUDENT_GUIDE = f"{COURSE}/handouts/FULL_COURSE_SETUP_DRAFT.md"
STUDENT_PDF = f"{COURSE}/handouts/PHYS3810_Full_Course_Student_Setup_v0.1_REVIEW_DRAFT.pdf"
STUDENT_GUIDE_SHA256 = "f26919ac85fd8bd4419e19ac118a9cb0eca4e1f72348cf84e3a65fa91deaa631"
STUDENT_PDF_SHA256 = "e6a950111470dbaa1d20781f4eb17391e73b7ca247e0a4ec54c879b922ea1053"
STUDENT_PDF_BYTES = 73883
EXPECTED_VALIDATION = {"tests": 160, "notebooks": 8, "nonempty_code_cells": 50, "pngs": 16}
NOTEBOOKS = (
    f"{COURSE}/notebooks/00_setup_preflight.ipynb",
    "notebooks/00_local_statevector_smoke.ipynb",
    "notebooks/01_local_aer_smoke.ipynb",
    *(f"{COURSE}/notebooks/{name}.ipynb" for name in (
        "01_grover", "02_qft", "03_qpe", "04_hhl", "05_shor"
    )),
)
REQUIRED_PNGS = dict(zip(
    (NOTEBOOKS[i] for i in (0, 3, 4, 5, 6, 7)), (2, 3, 2, 3, 3, 3), strict=True
))
CANONICAL_FILES = (
    "LICENSE", "ruff.toml", "requirements.txt", "requirements-ci.txt", "constraints-ci.txt",
    "src/backend_select.py",
    *(f"src/phys3810/{name}.py" for name in ("__init__", "grover", "qft", "qpe", "hhl", "shor")),
    *(f"tests/{name}.py" for name in (
        "test_backend_select", "test_classroom", "test_validate_classroom",
        "test_grover", "test_grover_notebook", "test_qft", "test_qft_notebook",
        "test_qpe", "test_qpe_notebook", "test_hhl", "test_hhl_notebook",
        "test_shor", "test_shor_notebook",
    )),
    "scripts/validate_classroom.py", "scripts/smoke_local.sh",
    *NOTEBOOKS, STUDENT_GUIDE, STUDENT_PDF,
)
PLAN_END_MARKERS = {
    "GROVER": "The completed lesson's independent review",
    "QFT": " The combined QFT/QPE review is accepted;",
    "QPE": None,
    "HHL": "Classical design checks confirmed",
    "SHOR": "Classical design checks confirmed",
}
TEMPLATE_FILES = {
    f"{COURSE}/package/README.md.in": "README.md",
    f"{COURSE}/package/SETUP.md.in": f"{COURSE}/SETUP.md",
    f"{COURSE}/package/COURSE_PLAN.md.in": f"{COURSE}/COURSE_PLAN.md",
    f"{COURSE}/package/VALIDATION.md.in": "VALIDATION.md",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_output(*arguments: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *arguments], stderr=subprocess.PIPE,
        env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"),
    )


def source_snapshot(reference: str) -> tuple[str, str, int, dict[str, bytes]]:
    """Resolve once and read only required regular members from that Git archive."""
    commit = git_output("rev-parse", "--verify", "--end-of-options", f"{reference}^{{commit}}")
    commit = commit.decode("ascii").strip()
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected a resolved SHA-1 commit identity.")
    tree = git_output("rev-parse", f"{commit}^{{tree}}").decode("ascii").strip()
    timestamp = int(git_output("show", "-s", "--format=%ct", commit))
    plans = tuple(f"{COURSE}/{name}_PLAN.md" for name in PLAN_END_MARKERS)
    required = (*CANONICAL_FILES, *plans, *TEMPLATE_FILES, BUILDER_PATH)
    expected_python = {name for name in CANONICAL_FILES if name.startswith(("src/", "tests/"))}
    # Inspect the tree before archive attributes can hide a new regression or helper.
    tracked_names = git_output("ls-tree", "-r", "--name-only", "-z", commit).decode("utf-8").split("\0")
    actual_python = {
        name for name in tracked_names
        if name.startswith(("src/", "tests/")) and name.endswith(".py")
    }
    if actual_python != expected_python:
        raise ValueError("Source/test Python inventory differs from the fixed preview profile.")
    files = {}
    with tarfile.open(fileobj=io.BytesIO(git_output("archive", "--format=tar", commit)), mode="r:") as archive:
        for name in required:
            try:
                member = archive.getmember(name)
            except KeyError as error:
                raise ValueError(f"Commit lacks required preview input: {name}") from error
            if not member.isfile():
                raise ValueError(f"Required input is not a regular file: {name}")
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError(f"Cannot read committed preview input: {name}")
            with stream:
                files[name] = stream.read()
            # An export-subst attribute must not silently change a canonical
            # payload or template while it is described as committed bytes.
            if files[name] != git_output("cat-file", "blob", f"{commit}:{name}"):
                raise ValueError(f"Git archive transformed required committed bytes: {name}")
    if files[BUILDER_PATH] != Path(__file__).read_bytes():
        raise ValueError("Executing builder differs from the selected commit; use its committed builder.")
    return commit, tree, timestamp, files


def literal_assignments(source: bytes) -> dict:
    """Read simple constant data from the validator AST without executing it."""
    values = {}

    def literal(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return values[node.id]
        if isinstance(node, (ast.Tuple, ast.List)):
            sequence = [literal(item) for item in node.elts]
            return tuple(sequence) if isinstance(node, ast.Tuple) else sequence
        if isinstance(node, ast.Dict):
            return {literal(key): literal(value) for key, value in zip(node.keys, node.values, strict=True)}
        raise ValueError("Not a supported constant expression.")

    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                values[node.targets[0].id] = literal(node.value)
            except (KeyError, ValueError):
                pass
    return values


def validate_canonical(files: dict[str, bytes]) -> None:
    """Reject profile drift and execution state; these are not executed tests."""
    if len(CANONICAL_FILES) != 37:
        raise ValueError("Internal canonical inventory does not match the preview profile.")
    if digest(files[STUDENT_PDF]) != STUDENT_PDF_SHA256 or len(files[STUDENT_PDF]) != STUDENT_PDF_BYTES:
        raise ValueError("Student PDF differs from the reviewed delivered bytes.")
    if not files[STUDENT_PDF].startswith(b"%PDF-") or digest(files[STUDENT_GUIDE]) != STUDENT_GUIDE_SHA256:
        raise ValueError("Student document pair differs from the reviewed preview edition.")
    values = literal_assignments(files["scripts/validate_classroom.py"])
    if values.get("NOTEBOOKS") != NOTEBOOKS or values.get("REQUIRED_PNGS") != REQUIRED_PNGS:
        raise ValueError("Validator notebook/figure inventory differs from the preview profile.")
    if values.get("EXPECTED") != {"qiskit": "2.6.1", "qiskit-aer": "0.17.2"}:
        raise ValueError("Validator SDK versions differ from the reviewed student guide.")
    cells = 0
    for name in NOTEBOOKS:
        notebook = json.loads(files[name])
        for cell in notebook["cells"]:
            if cell["cell_type"] != "code":
                continue
            if cell.get("execution_count") is not None or cell.get("outputs") != []:
                raise ValueError(f"Source notebook contains execution counts or outputs: {name}")
            source = cell["source"]
            if isinstance(source, list) and all(isinstance(part, str) for part in source):
                source = "".join(source)
            if not isinstance(source, str):
                raise ValueError(f"Invalid notebook code source: {name}")
            if source.strip():
                if "skip-execution" in cell.get("metadata", {}).get("tags", []):
                    raise ValueError(f"Required notebook cell is marked skip-execution: {name}")
                cells += 1
    test_methods = sum(
        sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_")
            for node in ast.walk(ast.parse(data)))
        for name, data in files.items() if name.startswith("tests/") and name.endswith(".py")
    )
    if cells != 50 or sum(REQUIRED_PNGS.values()) != 16 or test_methods != 160:
        raise ValueError("Static cell/figure/test inventory differs from 50/16/160; execution is still required.")


def payload_files(inputs: dict[str, bytes], commit: str, asset_name: str) -> tuple[dict, dict]:
    """Keep canonical bytes and describe each limited standalone document export."""
    files = {name: inputs[name] for name in CANONICAL_FILES}
    origins = {name: {"kind": "exact committed bytes", "source_path": name,
                      "source_sha256": digest(data)} for name, data in files.items()}
    for stem, marker in PLAN_END_MARKERS.items():
        name = f"{COURSE}/{stem}_PLAN.md"
        original = inputs[name].decode("utf-8")
        if "## " not in original:
            raise ValueError(f"Technical contract lacks its expected body boundary: {name}")
        body = original[original.index("## "):]
        if marker is not None:
            if marker not in body:
                raise ValueError(f"Technical contract history boundary changed: {name}")
            body = body.split(marker, 1)[0]
        body = body.rstrip() + "\n"
        if body.rstrip() not in original:
            raise ValueError(f"Technical contract body was not retained exactly: {name}")
        header = (
            original.splitlines()[0] + f"\n\nTechnical contract from source `{commit}`.\n"
            "Repository status/navigation and trailing coordination history are omitted.\n"
            "The retained API, mathematical, acceptance, resource, and teaching body is\n"
            "unchanged. Historical milestone test counts below describe earlier regression\n"
            "baselines; this full-course preview requires **160 tests/eight notebooks**.\n"
            "These references contain worked mathematical expectations, not an answer-free\n"
            "assessment. See [package validation information](../../VALIDATION.md).\n\n"
        )
        files[name] = (header + body).encode("utf-8")
        origins[name] = {"kind": "technical body exact; navigation/history adapted",
                         "source_path": name, "source_sha256": digest(inputs[name]),
                         "retained_body_sha256": digest(body.encode("utf-8"))}
    for template, destination in TEMPLATE_FILES.items():
        text = inputs[template].decode("utf-8")
        text = text.replace("{{SOURCE_COMMIT}}", commit).replace("{{ASSET_NAME}}", asset_name)
        if re.search(r"\{\{[^}]+\}\}", text):
            raise ValueError(f"Unresolved template placeholder: {template}")
        files[destination] = text.encode("utf-8")
        origins[destination] = {"kind": "standalone navigation template", "source_path": template,
                                "source_sha256": digest(inputs[template])}
    if len(files) != 46:
        raise ValueError("Unexpected preview payload inventory.")
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
    """Check safe paths, explicit exclusions, and local link/fragment closure."""
    folded = set()
    forbidden = {".git", ".venv", "__pycache__", "artifacts", "instructor", ".ipynb_checkpoints"}
    for name in files:
        parts = name.split("/")
        if (PurePosixPath(name).is_absolute() or any(p in ("", ".", "..") for p in parts)
                or "\\" in name or ":" in name or name.casefold() in folded):
            raise ValueError(f"Unsafe or case-colliding payload path: {name}")
        if forbidden.intersection(parts) or any(p.startswith(".") for p in parts):
            raise ValueError(f"Excluded payload path: {name}")
        if name.endswith(".pdf") and name != STUDENT_PDF:
            raise ValueError(f"Only the reviewed student PDF belongs in this preview: {name}")
        folded.add(name.casefold())
    anchors = {name: markdown_anchors(data.decode("utf-8")) for name, data in files.items()
               if name.endswith(".md")}
    count = 0
    for name, data in files.items():
        if name.endswith(".md"):
            text = data.decode("utf-8")
        elif name.endswith(".ipynb"):
            text = "\n".join("".join(c["source"]) for c in json.loads(data)["cells"]
                             if c["cell_type"] == "markdown")
        else:
            continue
        for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", text):
            link = urlsplit(target.strip("<>"))
            if link.netloc and not link.scheme:
                raise ValueError(f"Protocol-relative links are not supported: {name}: {target}")
            if link.scheme:
                if (link.scheme not in ("http", "https") or not link.hostname
                        or link.username or link.password):
                    raise ValueError(f"Unsupported external link: {name}: {target}")
                continue
            destination = (posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(link.path)))
                           if link.path else name)
            if destination not in files and destination != "MANIFEST.json":
                raise ValueError(f"Missing local link target: {name}: {target}")
            if link.fragment and destination.endswith(".md") and unquote(link.fragment) not in anchors[destination]:
                raise ValueError(f"Missing Markdown heading: {name}: {target}")
            count += 1
    return count


def portable_mode(name: str) -> str:
    return "0755" if name == "scripts/smoke_local.sh" else "0644"


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
    payload = output.getvalue()
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(set(archive.namelist())):
            raise ValueError("Generated ZIP failed integrity/uniqueness checks.")
        for name, data in files.items():
            if archive.read(f"{TOP_DIRECTORY}/{name}") != data:
                raise ValueError(f"Generated archive differs from payload: {name}")
    return payload


def build(reference: str, output_directory: Path) -> dict:
    commit, tree, timestamp, inputs = source_snapshot(reference)
    validate_canonical(inputs)
    asset_name = f"PHYS3810-Fall2026-{CODE_VERSION}-local-{commit[:12]}.zip"
    files, origins = payload_files(inputs, commit, asset_name)
    link_count = validate_payload(files)
    manifest = {
        "format_version": 1, "purpose": "unpublished local full-course preview; not final classroom approval",
        "source_commit": commit, "source_tree": tree, "proposed_code_version": CODE_VERSION,
        "document_edition": "v0.1 REVIEW DRAFT", "archive_top_directory": TOP_DIRECTORY,
        "builder": {"source_path": BUILDER_PATH, "source_sha256": digest(inputs[BUILDER_PATH])},
        "expected_validation": EXPECTED_VALIDATION, "validation_status": "not executed by this builder",
        "manifest_excludes_itself": True,
        "files": {name: {"sha256": digest(data), "bytes": len(data), "mode": portable_mode(name),
                         **origins[name]} for name, data in sorted(files.items())},
    }
    files["MANIFEST.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    validate_payload(files)
    payload = zip_bytes(files, timestamp)
    if not output_directory.is_absolute():
        output_directory = ROOT / output_directory
    output_directory = output_directory.resolve()
    archive_path = output_directory / asset_name
    metadata_path = archive_path.with_suffix(".metadata.json")
    if any(path.exists() or path.is_symlink() for path in (archive_path, metadata_path)):
        raise FileExistsError("Preview output already exists; choose a fresh --output-dir.")
    metadata = {
        "source_commit": commit, "source_tree": tree, "source_ref": reference,
        "builder_source_sha256": digest(inputs[BUILDER_PATH]), "archive": str(archive_path),
        "archive_sha256": digest(payload), "archive_bytes": len(payload), "file_count": len(files),
        "manifest_entries": len(manifest["files"]), "manifest_sha256": digest(files["MANIFEST.json"]),
        "canonical_file_count": len(CANONICAL_FILES), "canonical_hashes": {
            name: digest(files[name]) for name in CANONICAL_FILES
        }, "adapted_documents": sorted(set(origins) - set(CANONICAL_FILES)),
        "student_pdf_sha256": STUDENT_PDF_SHA256, "student_guide_sha256": STUDENT_GUIDE_SHA256,
        "relative_links_checked": link_count, "expected_validation": EXPECTED_VALIDATION,
        "static_inventory_check": "passed; test-method count is a drift guard, not test execution",
        "validation_status": "not executed by this builder",
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    with archive_path.open("xb") as stream:
        stream.write(payload)
    with metadata_path.open("x", encoding="utf-8") as stream:
        json.dump(metadata, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True, help="Commit/ref containing this exact builder and package inputs.")
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/classroom-preview"))
    args = parser.parse_args()
    try:
        metadata = build(args.ref, args.output_dir)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.decode("utf-8", errors="replace").strip() if error.stderr else str(error)
        parser.exit(2, f"Git source snapshot failed: {detail}\n")
    except (OSError, ValueError, KeyError, TypeError, SyntaxError, tarfile.TarError) as error:
        parser.exit(2, f"Preview build failed: {error}\n")
    print(json.dumps({key: metadata[key] for key in (
        "source_commit", "archive", "archive_sha256", "file_count", "validation_status"
    )}, indent=2))


if __name__ == "__main__":
    main()
