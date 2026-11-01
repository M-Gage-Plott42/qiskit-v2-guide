"""Build the provisional public full-course prerelease from one Git commit.

Reuse the unchanged local-preview profile and archive checks. The selected
commit must contain both executing builders and all templates. Reviewed PDF
and companion bytes stay unchanged; a separate current setup page discloses
their prepublication status. Runtime validation is a separate required step.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import tarfile

import build_classroom_preview as preview


ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = "scripts/build_classroom_prerelease.py"
CODE_VERSION = "v0.2.0-rc1"
RELEASE_TAG = f"phys3810-fa2026-{CODE_VERSION}"
ASSET_NAME = f"PHYS3810-Fall2026-{CODE_VERSION}.zip"
DOWNLOAD_URL = (
    "https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/"
    f"{RELEASE_TAG}/{ASSET_NAME}"
)
SETUP_PATH = f"{preview.COURSE}/SETUP.md"
NOTICE_PATH = f"{preview.COURSE}/handouts/PUBLICATION_NOTICE.md"
TEMPLATE_FILES = {
    f"{preview.COURSE}/package/PUBLIC_README.md.in": "README.md",
    f"{preview.COURSE}/package/PUBLIC_VALIDATION.md.in": "VALIDATION.md",
    f"{preview.COURSE}/package/PUBLICATION_NOTICE.md.in": NOTICE_PATH,
}
REVIEWED_TITLE = "# PHYS 3810: full-course student setup"
REVIEWED_EDITION = "**REVIEW DRAFT · Document v0.1 · Proposed course code v0.2.0-rc1**"
REVIEWED_AVAILABILITY = (
    "The full-course download is **unpublished**. Use the complete course folder your instructor approves. "
    "The earlier Grover-only package does not contain all five algorithm lessons. "
    "Session dates, classroom coverage, and assignments remain to be confirmed."
)


def source_snapshot(reference: str) -> tuple[str, str, int, dict[str, bytes]]:
    """Resolve once through R7, then read extra regular blobs from that commit."""
    commit, tree, timestamp, inputs = preview.source_snapshot(reference)
    required = (BUILDER_PATH, *TEMPLATE_FILES)
    entries = preview.git_output("ls-tree", "-z", commit, "--", *required)
    regular_blobs = {}
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii").split()
        name = name.decode("utf-8")
        if mode not in ("100644", "100755") or kind != "blob":
            raise ValueError(f"Required public input is not a regular Git blob: {name}")
        regular_blobs[name] = object_id
    if set(regular_blobs) != set(required):
        raise ValueError("Selected commit lacks the public builder or templates.")
    for name in required:
        inputs[name] = preview.git_output("cat-file", "blob", regular_blobs[name])
    if inputs[BUILDER_PATH] != Path(__file__).read_bytes():
        raise ValueError("Executing public builder differs from the selected commit.")
    # R7 already compares its own executing file to the same resolved commit.
    return commit, tree, timestamp, inputs


def fenced_blocks(text: str) -> list[str]:
    return re.findall(r"^```[^\n]*\n.*?^```[ \t]*(?:\n|$)", text, re.MULTILINE | re.DOTALL)


def current_setup(reviewed: bytes) -> bytes:
    """Adapt only title, edition, availability, and an explicit publication note."""
    original = reviewed.decode("utf-8")
    prefix = (
        f"{REVIEWED_TITLE}\n\n<!-- markdownlint-disable-next-line MD036 -->\n"
        f"{REVIEWED_EDITION}\n\n{REVIEWED_AVAILABILITY}\n\n"
    )
    if not original.startswith(prefix):
        raise ValueError("Reviewed student guide header changed; reassess the limited adaptation.")
    current_prefix = (
        "# PHYS 3810: provisional public preview setup\n\n"
        "<!-- markdownlint-disable-next-line MD036 -->\n"
        f"**Current publication instructions · Provisional course code {CODE_VERSION}**\n\n"
        f"Download the complete [provisional full-course preview]({DOWNLOAD_URL}) and extract "
        "its `phys3810-fa2026` folder. This URL becomes available when the identified "
        "prerelease is published. The earlier Grover-only package does not contain all five "
        "algorithm lessons. Session dates, classroom coverage, and assignments remain to "
        "be confirmed.\n\n"
        "**Document note:** The [original companion]"
        "(handouts/FULL_COURSE_SETUP_DRAFT.md) and [student PDF]"
        "(handouts/PHYS3810_Full_Course_Student_Setup_v0.1_REVIEW_DRAFT.pdf) remain exact "
        "**prepublication review drafts** for reference. Their statement that the download "
        "is unpublished describes the review-time state and is outdated after this "
        "prerelease. This page and the [package README](../../README.md) govern current "
        "availability. See the [publication notice](handouts/PUBLICATION_NOTICE.md).\n\n"
    )
    result = current_prefix + original[len(prefix):]
    blocks = fenced_blocks(original)
    if len(blocks) != 6 or fenced_blocks(result) != blocks:
        raise ValueError("Current setup must retain all six reviewed fenced blocks exactly.")
    return result.encode("utf-8")


def payload_files(inputs: dict[str, bytes], commit: str) -> tuple[dict, dict]:
    files, origins = preview.payload_files(inputs, commit, ASSET_NAME)
    replacements = {
        "{{SOURCE_COMMIT}}": commit,
        "{{ASSET_NAME}}": ASSET_NAME,
        "{{CODE_VERSION}}": CODE_VERSION,
        "{{RELEASE_TAG}}": RELEASE_TAG,
        "{{DOWNLOAD_URL}}": DOWNLOAD_URL,
    }
    for template, destination in TEMPLATE_FILES.items():
        text = inputs[template].decode("utf-8")
        for placeholder, value in replacements.items():
            text = text.replace(placeholder, value)
        if re.search(r"\{\{[^}]+\}\}", text):
            raise ValueError(f"Unresolved public template placeholder: {template}")
        files[destination] = text.encode("utf-8")
        origins[destination] = {
            "kind": "public prerelease navigation template", "source_path": template,
            "source_sha256": preview.digest(inputs[template]),
        }
    files[SETUP_PATH] = current_setup(inputs[preview.STUDENT_GUIDE])
    origins[SETUP_PATH] = {
        "kind": "reviewed guide; title/edition/availability adapted and publication note added",
        "source_path": preview.STUDENT_GUIDE,
        "source_sha256": preview.digest(inputs[preview.STUDENT_GUIDE]),
        "unchanged_fenced_blocks": 6,
        "fenced_block_sha256": [preview.digest(block.encode("utf-8"))
                                for block in fenced_blocks(inputs[preview.STUDENT_GUIDE].decode("utf-8"))],
        "adaptation_source_path": BUILDER_PATH,
        "adaptation_source_sha256": preview.digest(inputs[BUILDER_PATH]),
    }
    if len(files) != 47:
        raise ValueError("Unexpected public prerelease payload inventory.")
    return files, origins


def build(reference: str, output_directory: Path) -> dict:
    commit, tree, timestamp, inputs = source_snapshot(reference)
    preview.validate_canonical(inputs)
    files, origins = payload_files(inputs, commit)
    link_count = preview.validate_payload(files)
    builders = {
        "public_prerelease": {"source_path": BUILDER_PATH,
                              "source_sha256": preview.digest(inputs[BUILDER_PATH])},
        "local_preview_helper": {"source_path": preview.BUILDER_PATH,
                                 "source_sha256": preview.digest(inputs[preview.BUILDER_PATH])},
    }
    manifest = {
        "format_version": 1,
        "purpose": "provisional public full-course prerelease; not final classroom approval",
        "source_commit": commit, "source_tree": tree, "code_version": CODE_VERSION,
        "release_tag": RELEASE_TAG, "asset_name": ASSET_NAME,
        "document_edition": "v0.1 PREPUBLICATION REVIEW DRAFT; unchanged PDF and companion",
        "current_setup": SETUP_PATH, "publication_notice": NOTICE_PATH,
        "archive_top_directory": preview.TOP_DIRECTORY, "builders": builders,
        "expected_validation": preview.EXPECTED_VALIDATION,
        "validation_status": "not executed by this builder", "manifest_excludes_itself": True,
        "files": {name: {"sha256": preview.digest(data), "bytes": len(data),
                         "mode": preview.portable_mode(name), **origins[name]}
                  for name, data in sorted(files.items())},
    }
    files["MANIFEST.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    preview.validate_payload(files)
    payload = preview.zip_bytes(files, timestamp)
    if not output_directory.is_absolute():
        output_directory = ROOT / output_directory
    output_directory = output_directory.resolve()
    archive_path = output_directory / ASSET_NAME
    checksum_path = archive_path.with_suffix(".zip.sha256")
    metadata_path = archive_path.with_suffix(".metadata.json")
    if any(path.exists() or path.is_symlink() for path in (archive_path, checksum_path, metadata_path)):
        raise FileExistsError("Prerelease output already exists; choose a fresh --output-dir.")
    metadata = {
        "source_commit": commit, "source_tree": tree, "source_ref": reference,
        "builders": builders, "release_tag": RELEASE_TAG, "archive": str(archive_path),
        "checksum": str(checksum_path), "archive_sha256": preview.digest(payload),
        "archive_bytes": len(payload), "file_count": len(files),
        "manifest_entries": len(manifest["files"]),
        "manifest_sha256": preview.digest(files["MANIFEST.json"]),
        "canonical_file_count": len(preview.CANONICAL_FILES),
        "canonical_hashes": {name: preview.digest(files[name]) for name in preview.CANONICAL_FILES},
        "adapted_documents": sorted(set(origins) - set(preview.CANONICAL_FILES)),
        "student_pdf_sha256": preview.STUDENT_PDF_SHA256,
        "student_guide_sha256": preview.STUDENT_GUIDE_SHA256,
        "relative_links_checked": link_count, "expected_validation": preview.EXPECTED_VALIDATION,
        "static_inventory_check": "passed; test-method count is a drift guard, not test execution",
        "validation_status": "not executed by this builder",
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    with archive_path.open("xb") as stream:
        stream.write(payload)
    with checksum_path.open("x", encoding="ascii") as stream:
        stream.write(f"{metadata['archive_sha256']}  {ASSET_NAME}\n")
    with metadata_path.open("x", encoding="utf-8") as stream:
        json.dump(metadata, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", required=True, help="Commit/ref with both exact builders and all package inputs.")
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/classroom-prerelease"))
    args = parser.parse_args()
    try:
        metadata = build(args.ref, args.output_dir)
    except subprocess.CalledProcessError as error:
        detail = error.stderr.decode("utf-8", errors="replace").strip() if error.stderr else str(error)
        parser.exit(2, f"Git source snapshot failed: {detail}\n")
    except (OSError, ValueError, KeyError, TypeError, SyntaxError, tarfile.TarError) as error:
        parser.exit(2, f"Prerelease build failed: {error}\n")
    print(json.dumps({key: metadata[key] for key in (
        "source_commit", "archive", "checksum", "archive_sha256", "file_count", "validation_status"
    )}, indent=2))


if __name__ == "__main__":
    main()
