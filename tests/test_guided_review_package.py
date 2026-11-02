"""Offline acceptance cases for the separate, committed-source guided exporter."""

import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from scripts import build_guided_review as builder
from scripts import validate_classroom as validator


COMMIT = "a" * 40
TREE = "b" * 40
TIMESTAMP = 1793613600


def fixture_inputs():
    """Use minimal synthetic inputs; these tests need neither Git nor Qiskit."""
    files = {name: b"fixture\n" for name in builder.RUNTIME_FILES}
    files.update({name: b"# Test fixture\n" for name in builder.EXPECTED_BASELINE_TESTS})
    files["src/phys3810/__init__.py"] = b"# fixture\n"
    files["tests/test_extra_regression.py"] = b"# a newly committed regression\n"
    for name in builder.NOTEBOOKS:
        files[name] = json.dumps({"cells": [
            {"cell_type": "code", "source": "value = 1", "execution_count": None,
             "outputs": [], "metadata": {}},
        ]}).encode()
    for source, target in zip(builder.ENTRANCE_PATHS, builder.ENTRANCE_NAMES, strict=True):
        files[source] = f"# {target.removesuffix('.md')}\n\n[Next](START_HERE.md)\n".encode()
    files[builder.ENTRANCE_PATHS[0]] += (
        "[Guided notebook](../notebooks/guided/02_grover_follow_along.ipynb)\n"
        "[Setup](../SETUP.md)\n"
    ).encode()
    for stem, marker in builder.CONTRACT_END_MARKERS.items():
        text = f"# {stem}\n\nDated opening not exported.\n\n## Inputs\n\nExact mathematics.\n"
        if marker:
            text += marker + " old status.\n"
        files[f"{builder.COURSE}/{stem}_PLAN.md"] = text.encode()
    return files


def fixture_evidence():
    return {
        "source_commit": COMMIT, "python": "3.12.15", "platform": "synthetic test fixture",
        "environment_status": "reused", "environment_details": "Fixture evidence; not execution.",
        "versions": {"qiskit": "2.6.1", "qiskit-aer": "0.17.2"},
        "commands": ["python scripts/validate_classroom.py --profile all"],
        "results": {"all_profile_validator": "passed"},
        "counts": {"tests": 160, "notebooks": 11, "nonempty_code_cells": 11, "pngs": 27},
        "limitations": ["Synthetic fixture; no native-platform or runtime execution."],
    }


class GuidedReviewPackageTests(unittest.TestCase):
    def setUp(self):
        self.inputs = fixture_inputs()
        self.evidence = fixture_evidence()

    def build_fixture(self, directory):
        with patch.object(builder, "source_snapshot", return_value=(COMMIT, TREE, TIMESTAMP, self.inputs)):
            return builder.build("test-fixture", Path(directory), self.evidence)

    def test_reference_and_guided_inventories_match_runner(self):
        self.assertEqual(set(builder.REFERENCE_NOTEBOOKS), set(validator.NOTEBOOKS))
        self.assertEqual(set(builder.GUIDED_NOTEBOOKS), set(validator.GUIDED_NOTEBOOKS))
        self.assertEqual(len(set(builder.NOTEBOOKS)), 11)

    def test_manifest_hashes_origins_and_safe_exact_inventory(self):
        with tempfile.TemporaryDirectory(prefix="guided packet test ") as directory:
            result = self.build_fixture(directory)
            with zipfile.ZipFile(result["archive"]) as archive:
                prefix = builder.TOP_DIRECTORY + "/"
                manifest = json.loads(archive.read(prefix + "MANIFEST.json"))
                self.assertEqual(manifest["source_commit"], COMMIT)
                self.assertEqual(manifest["source_tree"], TREE)
                self.assertNotIn("MANIFEST.json", manifest["files"])
                self.assertEqual(len(archive.namelist()), len(manifest["files"]) + 1)
                self.assertIsNone(archive.testzip())
                for name, record in manifest["files"].items():
                    with self.subTest(name=name):
                        data = archive.read(prefix + name)
                        self.assertEqual(len(data), record["bytes"])
                        self.assertEqual(builder.digest(data), record["sha256"])
                        self.assertIn("kind", record)
                raw = Path(result["archive"]).read_bytes()
                self.assertEqual(len(raw), result["archive_bytes"])
                self.assertEqual(builder.digest(raw), result["archive_sha256"])

    def test_each_runtime_file_including_new_test_is_exact(self):
        files, origins = builder.payload_files(self.inputs, COMMIT, self.evidence)
        for name, data in self.inputs.items():
            if name in builder.RUNTIME_FILES or name.startswith(("src/", "tests/")):
                with self.subTest(name=name):
                    self.assertEqual(files["runtime/" + name], data)
                    self.assertEqual(origins["runtime/" + name]["source_sha256"], builder.digest(data))
        self.assertIn("runtime/tests/test_extra_regression.py", files)

    def test_same_inputs_produce_identical_zip_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            first = self.build_fixture(Path(directory) / "first")
            second = self.build_fixture(Path(directory) / "second")
            self.assertEqual(Path(first["archive"]).read_bytes(), Path(second["archive"]).read_bytes())

    def test_existing_archive_or_metadata_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.build_fixture(directory)
            original = Path(result["archive"]).read_bytes()
            with self.assertRaises(FileExistsError):
                self.build_fixture(directory)
            self.assertEqual(Path(result["archive"]).read_bytes(), original)

    def test_exported_links_remap_to_runtime_and_root_documents(self):
        files, _ = builder.payload_files(self.inputs, COMMIT, self.evidence)
        text = files["START_HERE.md"].decode()
        self.assertIn("(runtime/teaching/phys3810-fa2026/notebooks/guided/02_grover_follow_along.ipynb)", text)
        self.assertIn("(runtime/teaching/phys3810-fa2026/SETUP.md)", text)
        self.assertIn("(START_HERE.md)", text)
        self.assertGreater(builder.validate_payload(files), 0)

    def test_entrance_link_to_excluded_document_fails(self):
        with self.assertRaisesRegex(ValueError, "excluded input"):
            builder.adapt_entrance_links("[Private](../../../AGENTS.md)", builder.ENTRANCE_PATHS[0], {})

    def test_reference_contract_body_retained_and_dated_status_removed(self):
        files, origins = builder.payload_files(self.inputs, COMMIT, self.evidence)
        path = f"{builder.COURSE}/QFT_PLAN.md"
        expected = b"## Inputs\n\nExact mathematics.\n"
        self.assertTrue(files["runtime/" + path].endswith(expected))
        self.assertNotIn(b"old status", files["runtime/" + path])
        self.assertEqual(origins["runtime/" + path]["retained_body_sha256"], builder.digest(expected))

    def test_contract_boundary_drift_fails(self):
        with self.assertRaisesRegex(ValueError, "boundary changed"):
            builder.contract_body(b"# QFT\n\n## Inputs\n\nChanged body.\n", "QFT")

    def test_output_or_execution_count_in_source_rejected(self):
        for value in (7, [{"output_type": "stream", "text": "stale"}]):
            with self.subTest(value=value):
                inputs = dict(self.inputs)
                notebook = json.loads(inputs[builder.GUIDED_NOTEBOOKS[0]])
                key = "execution_count" if isinstance(value, int) else "outputs"
                notebook["cells"][0][key] = value
                inputs[builder.GUIDED_NOTEBOOKS[0]] = json.dumps(notebook).encode()
                with self.assertRaisesRegex(ValueError, "stored execution"):
                    builder.validate_source_notebooks(inputs)

    def test_required_skip_tag_and_missing_notebook_rejected(self):
        inputs = dict(self.inputs)
        notebook = json.loads(inputs[builder.GUIDED_NOTEBOOKS[0]])
        notebook["cells"][0]["metadata"] = {"tags": ["skip-execution"]}
        inputs[builder.GUIDED_NOTEBOOKS[0]] = json.dumps(notebook).encode()
        with self.assertRaisesRegex(ValueError, "skip-execution"):
            builder.validate_source_notebooks(inputs)
        del inputs[builder.GUIDED_NOTEBOOKS[0]]
        with self.assertRaises(KeyError):
            builder.validate_source_notebooks(inputs)

    def test_evidence_rejects_wrong_commit_counts_and_unpassed_source(self):
        variants = [
            {"source_commit": "c" * 40},
            {"counts": {"tests": 160, "notebooks": 8, "nonempty_code_cells": 11, "pngs": 27}},
            {"counts": {"tests": 160, "notebooks": 11, "nonempty_code_cells": 12, "pngs": 27}},
            {"results": {"all_profile_validator": "untested"}},
            {"python": "3.14.4"}, {"environment_status": "unknown"}, {"commands": []},
        ]
        for variant in variants:
            with self.subTest(variant=variant):
                evidence = dict(self.evidence, **variant)
                with self.assertRaises(ValueError):
                    builder.validate_evidence(evidence, COMMIT, 11)

    def test_validation_text_does_not_claim_post_export_execution(self):
        text = builder.validation_markdown(self.evidence).decode()
        self.assertIn("**reused**", text)
        self.assertIn("caller supplied", text)
        self.assertIn("post-export execution receipt is recorded outside", text)
        self.assertIn("not final classroom approval", text)

    def test_unsafe_case_colliding_and_excluded_paths_rejected(self):
        for name in ("../escape", "/absolute", "a\\b", "a:b", "runtime/.env", "runtime/.venv/x",
                     "runtime/artifacts/result.json", "old.pdf", "old.zip", "AGENTS.md"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    builder.validate_payload({name: b""})
        with self.assertRaisesRegex(ValueError, "case-colliding"):
            builder.validate_payload({"A.md": b"", "a.md": b""})

    def test_missing_relative_target_and_heading_rejected(self):
        for content in ("[gone](absent.md)", "[gone](B.md#absent)"):
            with self.subTest(content=content):
                with self.assertRaises(ValueError):
                    builder.validate_payload({"A.md": content.encode(), "B.md": b"# Present\n"})
        self.assertEqual(builder.validate_payload({"A.md": b"[ok](B.md#present)", "B.md": b"# Present\n"}), 1)

    def test_unsafe_external_links_rejected(self):
        for target in ("file:///etc/passwd", "https://user:secret@example.com", "//example.com"):
            with self.subTest(target=target):
                with self.assertRaises(ValueError):
                    builder.validate_payload({"A.md": f"[bad]({target})".encode()})

    def test_zip_member_modes_and_timestamp_are_portable(self):
        raw = builder.zip_bytes({"runtime/scripts/smoke_local.sh": b"x", "START_HERE.md": b"y"}, TIMESTAMP)
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            self.assertEqual(archive.getinfo(builder.TOP_DIRECTORY + "/runtime/scripts/smoke_local.sh").external_attr >> 16 & 0o777, 0o755)
            self.assertEqual(archive.getinfo(builder.TOP_DIRECTORY + "/START_HERE.md").external_attr >> 16 & 0o777, 0o644)
        with self.assertRaisesRegex(ValueError, "timestamp"):
            builder.zip_bytes({}, 0)

    def snapshot_response(self, *, changed_builder=False, symlink=False, missing_regression=False):
        files = copy.copy(self.inputs)
        files[builder.BUILDER_PATH] = b"wrong" if changed_builder else Path(builder.__file__).read_bytes()
        if missing_regression:
            del files[sorted(builder.EXPECTED_BASELINE_TESTS)[0]]
        blobs = {str(number).zfill(40): data for number, data in enumerate(files.values())}
        names = dict(zip(files, blobs, strict=True))
        records = []
        for name, blob in names.items():
            mode = "120000" if symlink and name == "requirements.txt" else "100644"
            records.append(f"{mode} blob {blob}\t{name}\0")

        def response(*args):
            if args[0] == "rev-parse":
                return ((TREE if args[-1].endswith("^{tree}") else COMMIT) + "\n").encode()
            if args[0] == "show":
                return str(TIMESTAMP).encode()
            if args[0] == "ls-tree":
                return "".join(records).encode()
            if args[:2] == ("cat-file", "blob"):
                return blobs[args[2]]
            raise AssertionError(args)
        return response

    def test_committed_snapshot_includes_new_tests_without_worktree_copy(self):
        with patch.object(builder, "git_output", side_effect=self.snapshot_response()):
            commit, tree, timestamp, inputs = builder.source_snapshot("HEAD")
        self.assertEqual((commit, tree, timestamp), (COMMIT, TREE, TIMESTAMP))
        self.assertEqual(inputs["tests/test_extra_regression.py"], b"# a newly committed regression\n")

    def test_snapshot_rejects_wrong_executing_builder(self):
        with patch.object(builder, "git_output", side_effect=self.snapshot_response(changed_builder=True)):
            with self.assertRaisesRegex(ValueError, "Executing builder differs"):
                builder.source_snapshot("HEAD")

    def test_snapshot_rejects_symlinks_and_lost_baseline_tests(self):
        for options in ({"symlink": True}, {"missing_regression": True}):
            with self.subTest(options=options):
                with patch.object(builder, "git_output", side_effect=self.snapshot_response(**options)):
                    with self.assertRaises(ValueError):
                        builder.source_snapshot("HEAD")


if __name__ == "__main__":
    unittest.main()
