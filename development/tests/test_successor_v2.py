from __future__ import annotations

import tempfile
import hashlib
import json
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from build_runtime_package import build_runtime, runtime_bytes
from generate_module_index import GENERATED, render_index
from test_validate_package import SOURCE_ID, _module, _write_registry, _write_skill, build_successor
from validate_package import CURRENT_CANONICAL_IDS, CURRENT_SCHEMA, SUCCESSOR_SCHEMA, validate_package


def build_current(root: Path) -> dict:
    registry = build_successor(root)
    registry["package_schema"] = CURRENT_SCHEMA
    registry["distribution_files"] = ["LICENSE"]
    (root / "LICENSE").write_bytes(b"Synthetic license fixture\n")
    registry["budget"]["policy"] = "advisory"
    for index, module_id in enumerate(CURRENT_CANONICAL_IDS[28:], start=29):
        registry["modules"].append(_module(module_id, index, True))
        registry["signal_enum"].append(f"signal_{index:02d}")
    for module in registry["modules"]:
        module.update(status="draft", evidence=[])
        (root / module["path"]).write_text(
            f"# {module['id']}\n\nStatus: `draft`  \nIntervention: `focus`  \nSources: `{SOURCE_ID}`\n\nOwned rule.\n",
            encoding="utf-8", newline="\n",
        )
    source_index = root / "references/source-index.md"
    source_index.write_text(source_index.read_text(encoding="utf-8") +
        "\n### SRC-PACKAGE-LOCAL-SYNTHESIS\n\nClass: local-synthesis\nScope: local heuristic.\n",
        encoding="utf-8", newline="\n")
    source_map = root / "docs/research/rule-source-map.md"
    source_map.write_text(source_map.read_text(encoding="utf-8") + "".join(
        f"| `{module_id}` | Owned rule | {SOURCE_ID} | bounded |\n"
        for module_id in CURRENT_CANONICAL_IDS[28:]), encoding="utf-8", newline="\n")
    _write_registry(root, registry)
    _write_skill(root, registry)
    return registry


class CurrentSchemaTests(unittest.TestCase):
    def test_current_thirty_modules_and_statusless_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_current(root)
            result = validate_package(root, CURRENT_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertEqual(30, result.metrics["modules"])
            self.assertNotIn("(draft)", render_index(registry))
            self.assertIn(GENERATED, render_index(registry))

    def test_historical_schema_does_not_accept_draft_or_thirty(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            self.assertIn("(stub)", render_index(registry))
            registry["modules"][0]["status"] = "draft"
            _write_registry(root, registry)
            self.assertTrue(any("invalid status" in e for e in validate_package(root, SUCCESSOR_SCHEMA).errors))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_current(root)
            self.assertTrue(any("canonical module" in e for e in validate_package(root, SUCCESSOR_SCHEMA).errors))

    def test_current_rejects_old_status_header_drift_and_hard_budget(self):
        for mutation, signature in (("status", "invalid status"), ("header", "Status header"), ("budget", "must be advisory")):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                if mutation == "status":
                    registry["modules"][0]["status"] = "stub"
                elif mutation == "budget":
                    registry["budget"]["policy"] = "hard"
                else:
                    path = root / registry["modules"][0]["path"]
                    path.write_text(path.read_text(encoding="utf-8").replace("Status: `draft`", "Status: `stub`"), encoding="utf-8")
                _write_registry(root, registry)
                self.assertTrue(any(signature in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_current_still_rejects_missing_module_source_and_sibling_load(self):
        for mutation, signature in (("module", "missing reference"), ("source", "local-synthesis"), ("sibling", "sibling reference")):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                path = root / registry["modules"][-1]["path"]
                if mutation == "module":
                    path.unlink()
                elif mutation == "source":
                    path = root / "references/source-index.md"
                    path.write_text(path.read_text(encoding="utf-8").replace("Class: local-synthesis", "Class: empirical"), encoding="utf-8")
                else:
                    path.write_text(path.read_text(encoding="utf-8") + "\n[Other](other.md)\n", encoding="utf-8")
                self.assertTrue(any(signature in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_planned_fixture_ids_are_not_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_current(root)
            registry["modules"][0]["evidence"] = ["RF51-planned"]
            _write_registry(root, registry)
            self.assertTrue(any("executed P6 receipt" in e for e in validate_package(root, CURRENT_SCHEMA).errors))

    def test_build_preserves_every_byte_except_exact_comment_and_never_overwrites(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "source"
            root.mkdir()
            build_current(root)
            destination = parent / "runtime"
            receipt = build_runtime(root, destination)
            self.assertEqual(35, receipt["runtime"]["file_count"])
            self.assertEqual((root / "LICENSE").read_bytes(), (destination / "LICENSE").read_bytes())
            self.assertNotEqual(receipt["source"]["manifest_sha256"], receipt["runtime"]["manifest_sha256"])
            self.assertFalse((destination / "docs").exists())
            for record in receipt["source"]["files"]:
                path = record["path"]
                self.assertEqual(runtime_bytes(path, (root / path).read_bytes()), (destination / path).read_bytes())
            self.assertEqual([], validate_package(destination, CURRENT_SCHEMA, runtime=True).errors)
            self.assertTrue(any("rule-source-map" in e for e in validate_package(destination, CURRENT_SCHEMA).errors))
            with self.assertRaisesRegex(ValueError, "already exists"):
                build_runtime(root, destination)
            with self.assertRaisesRegex(ValueError, "outside"):
                build_runtime(root, root / "runtime")
            path = destination / "SKILL.md"
            path.write_text(path.read_text(encoding="utf-8").replace("route 01", "wrong route"), encoding="utf-8")
            self.assertTrue(any("index drift" in e for e in validate_package(destination, CURRENT_SCHEMA, runtime=True).errors))

    def test_evidence_resolves_executed_receipts_not_just_id_shape(self):
        for mutation in (None, "missing", "planned", "hash", "settings", "outcome", "artifact"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_current(root)
                registry["modules"][0]["evidence"] = ["P6-UNIT-OBSERVED"]
                _write_registry(root, registry)
                artifact = root / "docs/evaluation/unit-trace.txt"
                artifact.parent.mkdir(parents=True)
                artifact.write_text("Observed unit-test fixture, not a design case.\n", encoding="utf-8")
                receipt = {"id": "P6-UNIT-OBSERVED", "executed": True, "case_version": "unit-v1", "requested_model": "unit-fixture", "session_id": "unit-session", "executed_at": "2026-09-04", "settings": {"effort": "unit", "tools": []}, "outcome": "fail", "tested_package_sha256": "A" * 64, "artifacts": [{"path": "docs/evaluation/unit-trace.txt", "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest().upper()}]}
                if mutation == "planned": receipt["executed"] = False
                if mutation == "hash": receipt["tested_package_sha256"] = "missing"
                if mutation == "settings": receipt["settings"] = {}
                if mutation == "outcome": receipt["outcome"] = "planned"
                if mutation == "artifact": artifact.write_text("Changed", encoding="utf-8")
                if mutation != "missing":
                    (artifact.parent / "plan-0006-case-receipts.json").write_text(json.dumps({"schema_version": 1, "receipts": [receipt]}), encoding="utf-8")
                errors = validate_package(root, CURRENT_SCHEMA).errors
                if mutation is None:
                    self.assertEqual([], errors, "Executed failures are valid evidence, not pass claims")
                else:
                    self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
