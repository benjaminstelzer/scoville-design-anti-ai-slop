from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from generate_module_index import END, START, render_index, replace_index
from validate_package import (
    LEGACY_CANONICAL_IDS,
    LEGACY_SCHEMA,
    SUCCESSOR_CANONICAL_IDS,
    SUCCESSOR_SCHEMA,
    validate_package,
)


SOURCE_ID = "CUR.BK-01"


def _write_registry(root: Path, registry: dict) -> None:
    (root / "modules.yaml").write_text(
        yaml.safe_dump(registry, sort_keys=False), encoding="utf-8", newline="\n"
    )


def _write_skill(root: Path, registry: dict) -> None:
    base = f"# Test Skill\n\n{START}\n{END}\n"
    (root / "SKILL.md").write_text(
        replace_index(base, render_index(registry)), encoding="utf-8", newline="\n"
    )


def _write_agent(root: Path) -> None:
    agent = {
        "interface": {
            "default_prompt": "Use $scoville-design-anti-ai-slop for this task.",
            "short_description": "Professional graphic design guardrail",
        }
    }
    (root / "agents").mkdir(parents=True)
    (root / "agents" / "openai.yaml").write_text(
        yaml.safe_dump(agent, sort_keys=False), encoding="utf-8", newline="\n"
    )


def _module(module_id: str, index: int, successor: bool) -> dict:
    item = {
        "id": module_id,
        "status": "stub",
        "intervention": "focus",
        "path": f"references/{module_id}.md",
        "route_label": f"route {index:02d}",
        "when_any": [f"signal_{index:02d}"],
        "unless": [],
        "requires": [],
        "conflicts": [],
        "owns": [f"concern_{index:02d}"],
        "sources": [SOURCE_ID],
    }
    if successor:
        item.update({"token_target": 1800, "token_ceiling": 2400})
    return item


def build_successor(root: Path) -> dict:
    (root / "references").mkdir(parents=True)
    (root / "docs" / "research").mkdir(parents=True)
    modules = [
        _module(module_id, index, True)
        for index, module_id in enumerate(SUCCESSOR_CANONICAL_IDS, start=1)
    ]
    registry = {
        "format_version": 2,
        "package_schema": SUCCESSOR_SCHEMA,
        "signal_enum": [
            f"signal_{index:02d}"
            for index in range(1, len(SUCCESSOR_CANONICAL_IDS) + 1)
        ],
        "non_routed_references": ["references/source-index.md"],
        "budget": {
            "core_token_ceiling": 1500,
            "index_token_ceiling": 800,
            "provisional_max_simultaneous_leaves": 4,
            "provisional_core_plus_leaves_ceiling": 15000,
        },
        "planned_common_loads": [
            {
                "id": "common-four",
                "modules": SUCCESSOR_CANONICAL_IDS[:4],
                "token_ceiling": 15000,
            }
        ],
        "modules": modules,
    }
    _write_registry(root, registry)
    _write_skill(root, registry)
    _write_agent(root)
    for item in modules:
        (root / item["path"]).write_text(
            f"# {item['id']}\n\nSources: {SOURCE_ID}\n\n## Rules\n\nApply the owned rule.\n",
            encoding="utf-8",
            newline="\n",
        )
    (root / "references" / "source-index.md").write_text(
        f"# Source index\n\n### {SOURCE_ID} Canonical curriculum source\n\nRecord.\n",
        encoding="utf-8",
        newline="\n",
    )
    map_lines = [
        "# Rule-to-source map",
        "",
        "| Expert module | Operational rule cluster | Source IDs | Boundary |",
        "| --- | --- | --- | --- |",
    ]
    map_lines.extend(
        f"| `{module_id}` | Owned rule | {SOURCE_ID} | bounded |"
        for module_id in SUCCESSOR_CANONICAL_IDS
    )
    (root / "docs" / "research" / "rule-source-map.md").write_text(
        "\n".join(map_lines) + "\n", encoding="utf-8", newline="\n"
    )
    return registry


def build_legacy(root: Path) -> dict:
    (root / "references").mkdir(parents=True)
    modules = [
        _module(module_id, index, False)
        for index, module_id in enumerate(LEGACY_CANONICAL_IDS, start=1)
    ]
    registry = {
        "format_version": 1,
        "signal_enum": [f"signal_{index:02d}" for index in range(1, 15)],
        "modules": modules,
    }
    _write_registry(root, registry)
    _write_skill(root, registry)
    _write_agent(root)
    for item in modules:
        content = f"# {item['id']}\n\nSources: {SOURCE_ID}\n\nApply the owned rule.\n"
        if item["id"] == "sources-and-attribution":
            content += f"\n### {SOURCE_ID} Legacy source\n\nRecord.\n"
        (root / item["path"]).write_text(
            content, encoding="utf-8", newline="\n"
        )
    return registry


class SuccessorValidatorTests(unittest.TestCase):
    def test_valid_successor_fixture_and_generalized_source_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_successor(root)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertEqual([], result.warnings)
            self.assertEqual(28, result.metrics["modules"])

    def test_valid_explicit_legacy_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_legacy(root)
            result = validate_package(root, LEGACY_SCHEMA)
            self.assertEqual([], result.errors)

    def test_exact_module_order_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][0], registry["modules"][1] = (
                registry["modules"][1],
                registry["modules"][0],
            )
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("canonical module IDs/order differ" in error for error in result.errors))

    def test_signal_and_concern_ownership_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][1]["when_any"] = registry["modules"][0]["when_any"]
            registry["modules"][1]["owns"] = registry["modules"][0]["owns"]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("signal ownership collision" in error for error in result.errors))
            self.assertTrue(any("ownership collision" in error for error in result.errors))

    def test_hidden_dependencies_are_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][0]["requires"] = [SUCCESSOR_CANONICAL_IDS[1]]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("requires/conflicts" in error for error in result.errors))

    def test_source_index_declaration_and_orphans_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["non_routed_references"] = []
            _write_registry(root, registry)
            (root / "references" / "orphan.md").write_text("orphan", encoding="utf-8")
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("non_routed_references" in error for error in result.errors))
            self.assertTrue(any("orphan references" in error for error in result.errors))

    def test_unresolved_source_and_header_mismatch_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            item = registry["modules"][0]
            item["sources"] = ["AUD.TYPE-02"]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("unresolved source ID AUD.TYPE-02" in error for error in result.errors))
            self.assertTrue(any("Sources: header must equal" in error for error in result.errors))

    def test_rule_source_map_cluster_and_resolution_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_successor(root)
            map_path = root / "docs" / "research" / "rule-source-map.md"
            text = map_path.read_text(encoding="utf-8")
            text = text.replace(
                f"| `{SUCCESSOR_CANONICAL_IDS[0]}` | Owned rule | {SOURCE_ID} | bounded |",
                f"| `{SUCCESSOR_CANONICAL_IDS[0]}` |  | AUD.MISSING-99 | bounded |",
            )
            map_path.write_text(text, encoding="utf-8", newline="\n")
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("has no rule cluster" in error for error in result.errors))
            self.assertTrue(any("unresolved source ID AUD.MISSING-99" in error for error in result.errors))

    def test_token_target_excess_is_warning_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][0]["token_target"] = 1
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertTrue(any("exceeds target 1" in warning for warning in result.warnings))

    def test_leaf_token_ceiling_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["modules"][0]["token_target"] = 1
            registry["modules"][0]["token_ceiling"] = 2
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("tokens exceeds ceiling 2" in error for error in result.errors))

    def test_core_and_index_ceilings_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["budget"]["index_token_ceiling"] = 1
            _write_registry(root, registry)
            skill_path = root / "SKILL.md"
            skill_path.write_text(
                skill_path.read_text(encoding="utf-8") + ("coreword " * 3000),
                encoding="utf-8",
                newline="\n",
            )
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("SKILL.md:" in error and "exceeds 1500" in error for error in result.errors))
            self.assertTrue(any("generated index:" in error for error in result.errors))

    def test_large_valid_index_does_not_inflate_successor_core(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            baseline = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], baseline.errors)

            for index, item in enumerate(registry["modules"], start=1):
                item["route_label"] = f"route {index:02d} " + ("index-only-label " * 120)
            registry["budget"]["index_token_ceiling"] = 100000
            _write_registry(root, registry)
            _write_skill(root, registry)

            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], result.errors)
            self.assertGreater(result.metrics["index_tokens"], 1500)
            self.assertEqual(
                baseline.metrics["core_tokens"], result.metrics["core_tokens"]
            )
            self.assertEqual(
                result.metrics["core_tokens"] + result.metrics["index_tokens"],
                result.metrics["core_plus_index"],
            )

    def test_common_and_phase_loads_include_the_generated_index(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            for index, item in enumerate(registry["modules"], start=1):
                item["route_label"] = f"route {index:02d} " + ("resident-index " * 800)
            registry["budget"]["index_token_ceiling"] = 100000
            _write_registry(root, registry)
            _write_skill(root, registry)

            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertGreater(result.metrics["index_tokens"], 15000)
            self.assertTrue(
                any(
                    "planned common load common-four" in error
                    and "exceeds ceiling 15000" in error
                    for error in result.errors
                )
            )
            self.assertTrue(
                any(
                    "Core + index + 4 largest experts" in error
                    for error in result.errors
                )
            )

    def test_common_load_shape_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["planned_common_loads"][0]["modules"] = SUCCESSOR_CANONICAL_IDS[:5]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("5 leaves exceeds 4" in error for error in result.errors))

    def test_common_load_and_largest_phase_ceiling_are_hard_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            for item in registry["modules"][:4]:
                item["token_target"] = 5000
                item["token_ceiling"] = 5000
                (root / item["path"]).write_text(
                    f"# {item['id']}\n\nSources: {SOURCE_ID}\n\n" + ("payload " * 4300),
                    encoding="utf-8",
                    newline="\n",
                )
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("planned common load common-four" in error for error in result.errors))
            self.assertTrue(any("Core + index + 4 largest experts" in error for error in result.errors))

    def test_sibling_link_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            path = root / registry["modules"][0]["path"]
            path.write_text(
                path.read_text(encoding="utf-8") + "\n[Sibling](other.md)\n",
                encoding="utf-8",
                newline="\n",
            )
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("sibling reference link" in error for error in result.errors))

    def test_advisory_policy_reports_all_overruns_without_failing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["budget"]["policy"] = "advisory"
            registry["budget"]["index_token_ceiling"] = 1
            registry["planned_common_loads"][0].update(
                modules=SUCCESSOR_CANONICAL_IDS[:5], token_ceiling=16000
            )
            for item in registry["modules"][:5]:
                (root / item["path"]).write_text(
                    f"# {item['id']}\n\nSources: {SOURCE_ID}\n\n" + ("payload " * 4300),
                    encoding="utf-8",
                )
            _write_registry(root, registry)
            path = root / "SKILL.md"
            path.write_text(path.read_text(encoding="utf-8") + "coreword " * 3000,
                            encoding="utf-8")
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], result.errors)
            for signature in (
                "SKILL.md:", "generated index:", "exceeds ceiling 2400",
                "5 leaves exceeds 4", "token_ceiling 16000 exceeds phase ceiling 15000",
                "tokens exceeds ceiling 16000", "tokens exceeds phase ceiling 15000",
                "Core + index + 4 largest experts",
            ):
                with self.subTest(signature=signature):
                    self.assertTrue(any(signature in warning for warning in result.warnings))
            self.assertGreater(result.metrics["core_plus_largest_phase"], 15000)

    def test_advisory_estimates_can_change_without_hardcoded_caps(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["budget"].update(
                policy="advisory", core_token_ceiling=2000,
                provisional_max_simultaneous_leaves=8,
                provisional_core_plus_leaves_ceiling=30000,
            )
            registry["planned_common_loads"][0]["modules"] = SUCCESSOR_CANONICAL_IDS[:8]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertEqual([], result.errors)

    def test_advisory_policy_preserves_structural_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = build_successor(root)
            registry["budget"]["policy"] = "advisory"
            registry["planned_common_loads"][0]["modules"] = [
                SUCCESSOR_CANONICAL_IDS[0], SUCCESSOR_CANONICAL_IDS[0], "unknown-expert"
            ]
            registry["modules"][0]["sources"] = ["MISSING-SOURCE"]
            _write_registry(root, registry)
            result = validate_package(root, SUCCESSOR_SCHEMA)
            for signature in ("duplicate module IDs", "unknown module IDs", "unresolved source ID"):
                with self.subTest(signature=signature):
                    self.assertTrue(any(signature in error for error in result.errors))

    def test_invalid_budget_metadata_remains_a_hard_error(self) -> None:
        for key, value in (("policy", "unknown"), ("core_token_ceiling", 0),
                           ("index_token_ceiling", True),
                           ("provisional_max_simultaneous_leaves", -1),
                           ("provisional_core_plus_leaves_ceiling", "unlimited")):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                registry = build_successor(root)
                registry["budget"].update(policy="advisory")
                registry["budget"][key] = value
                _write_registry(root, registry)
                result = validate_package(root, SUCCESSOR_SCHEMA)
                self.assertTrue(any(f"budget.{key}" in error for error in result.errors))

    def test_generated_index_drift_is_hard_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_successor(root)
            skill_path = root / "SKILL.md"
            skill_path.write_text(
                skill_path.read_text(encoding="utf-8").replace("route 01", "wrong route"),
                encoding="utf-8",
                newline="\n",
            )
            result = validate_package(root, SUCCESSOR_SCHEMA)
            self.assertTrue(any("generated module index drift" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
