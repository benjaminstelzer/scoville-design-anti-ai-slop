#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

try:
    import tiktoken
except ModuleNotFoundError:
    print(
        "ERROR tiktoken is required for the frozen o200k_base token checks; "
        "run this validator in the pinned SkillOpt environment or install tiktoken.",
        file=sys.stderr,
    )
    raise SystemExit(2)

from generate_module_index import END, GENERATED, START, load_registry, render_index, replace_index


SUCCESSOR_SCHEMA = "successor-v1"
CURRENT_SCHEMA = "successor-v2"
LEGACY_SCHEMA = "legacy-rc7"
SCHEMAS = (CURRENT_SCHEMA, SUCCESSOR_SCHEMA, LEGACY_SCHEMA)

SUCCESSOR_CANONICAL_IDS = [
    "brief-framing-and-criteria",
    "concept-development-and-selection",
    "composition-and-layout",
    "typography-and-typesetting",
    "font-technology-and-script-safety",
    "colour-and-reproduction",
    "imagery-and-art-direction",
    "information-design-and-data-visualization",
    "cartography-and-spatial-data",
    "diagrams-and-relational-information",
    "brand-and-visual-systems",
    "logo-and-identity-mark-design",
    "instructional-and-explanatory-design",
    "advertising-and-campaign-art-direction",
    "ui-workflow-and-interaction-design",
    "web-and-responsive-design",
    "editorial-and-fixed-media-design",
    "packaging-graphics-and-sku-systems",
    "physical-wayfinding-and-signage-systems",
    "motion-and-sequence",
    "media-production-and-handoff",
    "critique-and-validation",
    "culture-and-representation",
    "people-privacy-and-media-integrity",
    "sustainability-claims",
    "source-verification-and-evidence",
    "asset-rights-and-attribution",
    "style-direction",
]

CURRENT_CANONICAL_IDS = SUCCESSOR_CANONICAL_IDS + [
    "generic-signatures-and-subject-specificity",
    "coordination-with-sibling-skills",
]

LEGACY_CANONICAL_IDS = [
    "brief-and-concept",
    "composition-and-layout",
    "typography-and-writing-systems",
    "colour-and-reproduction",
    "imagery-and-art-direction",
    "information-and-data",
    "brand-and-visual-systems",
    "ui-and-interaction-design",
    "motion-and-sequence",
    "media-production-and-handoff",
    "critique-and-validation",
    "culture-ethics-and-provenance",
    "sources-and-attribution",
    "style-direction",
]

STATUSES = {"admitted", "retained-floor", "stub", "withheld"}
INTERVENTIONS = {"focus", "correction", "teaching", "external-verification"}

# Source identifiers are intentionally prefix-agnostic. At least one separator
# keeps ordinary prose headings from being mistaken for source records.
SOURCE_ID_TEXT = r"[A-Za-z0-9]+(?:[-_.:][A-Za-z0-9]+)+"
SOURCE_ID = re.compile(rf"^{SOURCE_ID_TEXT}$")
SOURCE_HEADING = re.compile(
    rf"^###\s+`?({SOURCE_ID_TEXT})`?(?:\s|$)", re.MULTILINE
)
SOURCE_HEADER = re.compile(r"^Sources:\s*(.*?)\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")
DIRECT_MODULE_LINK = re.compile(r"\]\((references/[^)#?]+\.md)(?:#[^)]+)?\)")


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, int] = field(default_factory=dict)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def tokens(text: str) -> int:
    return len(tiktoken.get_encoding("o200k_base").encode(text))


def successor_core_text(skill_text: str) -> str:
    """Return Core with generated index entries excluded from its token budget.

    The exact successor metric retains the index boundary markers and replaces
    everything from START through END with ``START + newline + END``. The
    generated comment and every generated module entry therefore count only
    toward the separate index budget. Legacy RC7 intentionally keeps its prior
    full-SKILL.md metric for historical comparability.
    """
    start = skill_text.find(START)
    end = skill_text.find(END)
    if start < 0 or end < 0 or end < start:
        raise ValueError("SKILL.md is missing valid module index markers")
    end += len(END)
    return skill_text[:start] + START + "\n" + END + skill_text[end:]


def _positive_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _normal_path(value: Any) -> str:
    return str(value).replace("\\", "/")


def _source_ids_from_header(
    content: str, module_id: str, result: Result
) -> list[str]:
    matches = SOURCE_HEADER.findall(content)
    if len(matches) != 1:
        result.error(f"{module_id}: expected exactly one Sources: header")
        return []
    raw_parts = [part.strip().strip("`") for part in matches[0].split(",")]
    if not raw_parts or any(not part for part in raw_parts):
        result.error(f"{module_id}: Sources: header must list source IDs")
        return []
    invalid = [part for part in raw_parts if not SOURCE_ID.fullmatch(part)]
    if invalid:
        result.error(
            f"{module_id}: invalid source ID(s) in Sources: header: "
            + ", ".join(invalid)
        )
    if len(raw_parts) != len(set(raw_parts)):
        result.error(f"{module_id}: duplicate source ID in Sources: header")
    return raw_parts


def _source_headings(source_text: str, result: Result) -> set[str]:
    headings = SOURCE_HEADING.findall(source_text)
    if not headings:
        result.error("source index has no level-three source ID headings")
        return set()
    duplicates = sorted({item for item in headings if headings.count(item) > 1})
    if duplicates:
        result.error("duplicate source index headings: " + ", ".join(duplicates))
    return set(headings)


def _is_sibling_reference_link(target: str) -> bool:
    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not target or "://" in target or target.startswith(("mailto:", "#", "/")):
        return False
    normalized_target = target.replace("\\", "/")
    normalized = PurePosixPath(normalized_target)
    if normalized.suffix.lower() != ".md":
        return False
    # Resolve relative to the routed leaf's references/ directory. This catches
    # `other.md`, `references/other.md`, and `../references/other.md` without
    # confusing a link to repository documentation with a sibling expert.
    resolved = posixpath.normpath(posixpath.join("references", normalized_target))
    return resolved.startswith("references/")


def _validate_rule_source_map(
    map_path: Path,
    module_ids: set[str],
    module_sources: dict[str, set[str]],
    registered_sources: set[str],
    result: Result,
) -> None:
    if not map_path.is_file():
        result.error("missing required file: docs/research/rule-source-map.md")
        return

    mapped: dict[str, set[str]] = {module_id: set() for module_id in module_ids}
    rows: dict[str, int] = {module_id: 0 for module_id in module_ids}
    for line_number, line in enumerate(
        map_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        module_id = cells[0].strip("`")
        if module_id not in module_ids:
            continue
        rows[module_id] += 1
        if not cells[1] or cells[1] in {"---", "Operational rule cluster"}:
            result.error(
                f"rule-source map line {line_number}: {module_id} has no rule cluster"
            )
        raw_ids = [part.strip().strip("`") for part in cells[2].split(",")]
        if not raw_ids or any(not part for part in raw_ids):
            result.error(
                f"rule-source map line {line_number}: {module_id} has no source IDs"
            )
            continue
        for source_id in raw_ids:
            if not SOURCE_ID.fullmatch(source_id):
                result.error(
                    f"rule-source map line {line_number}: invalid source ID {source_id}"
                )
                continue
            if source_id not in registered_sources:
                result.error(
                    f"rule-source map line {line_number}: unresolved source ID {source_id}"
                )
            mapped[module_id].add(source_id)

    for module_id in sorted(module_ids):
        if rows[module_id] == 0:
            result.error(f"{module_id}: no rule-source map row")
            continue
        declared = module_sources.get(module_id, set())
        if mapped[module_id] != declared:
            missing = sorted(declared - mapped[module_id])
            undeclared = sorted(mapped[module_id] - declared)
            details: list[str] = []
            if missing:
                details.append("unmapped " + ", ".join(missing))
            if undeclared:
                details.append("undeclared " + ", ".join(undeclared))
            result.error(f"{module_id}: rule-source map mismatch ({'; '.join(details)})")


def _validate_successor_budgets(
    registry: dict[str, Any],
    modules: list[dict[str, Any]],
    module_token_counts: dict[str, int],
    core_tokens: int,
    index_tokens: int,
    result: Result,
) -> None:
    budget = registry.get("budget")
    if not isinstance(budget, dict):
        result.error("budget must be a mapping")
        return

    # Missing policy preserves the frozen successor contract. Only the current
    # package opts into ADR-0032; structure and historical metrics stay intact.
    policy = budget.get("policy", "hard")
    if policy not in ("hard", "advisory"):
        result.error("budget.policy must be hard or advisory")
        return
    report_overrun = result.warning if policy == "advisory" else result.error

    core_ceiling = budget.get("core_token_ceiling")
    index_ceiling = budget.get("index_token_ceiling")
    max_leaves = budget.get("provisional_max_simultaneous_leaves")
    phase_ceiling = budget.get("provisional_core_plus_leaves_ceiling")

    budget_fields = (
        "core_token_ceiling", "index_token_ceiling",
        "provisional_max_simultaneous_leaves", "provisional_core_plus_leaves_ceiling",
    )
    for name in budget_fields:
        if not _positive_int(budget.get(name)):
            result.error(f"budget.{name} must be a positive integer")
    if any(not _positive_int(budget.get(name)) for name in budget_fields):
        return

    if policy == "hard" and core_ceiling != 1500:
        result.error("budget.core_token_ceiling must remain 1500")
    elif core_tokens > core_ceiling:
        report_overrun(f"SKILL.md: {core_tokens} tokens exceeds {core_ceiling}")

    if index_tokens > index_ceiling:
        report_overrun(f"generated index: {index_tokens} tokens exceeds {index_ceiling}")

    if policy == "hard" and max_leaves != 4:
        result.error("budget.provisional_max_simultaneous_leaves must remain 4")
        max_leaves = 4
    if policy == "hard" and phase_ceiling != 15000:
        result.error("budget.provisional_core_plus_leaves_ceiling must remain 15000")
        phase_ceiling = 15000

    # Core and index have separate individual ceilings, but both are resident
    # whenever SKILL.md is loaded. Every phase/common-load metric therefore
    # starts with Core-without-index plus the complete generated index.
    loaded_core_and_index = core_tokens + index_tokens
    result.metrics["core_plus_index"] = loaded_core_and_index

    for item in modules:
        module_id = item.get("id", "<missing>")
        target = item.get("token_target")
        ceiling = item.get("token_ceiling")
        if not _positive_int(target):
            result.error(f"{module_id}: token_target must be a positive integer")
            continue
        if not _positive_int(ceiling):
            result.error(f"{module_id}: token_ceiling must be a positive integer")
            continue
        if target > ceiling:
            result.error(f"{module_id}: token_target exceeds token_ceiling")
        count = module_token_counts.get(module_id)
        if count is None:
            continue
        if count > ceiling:
            report_overrun(f"{module_id}: {count} tokens exceeds ceiling {ceiling}")
        elif count > target:
            result.warning(f"{module_id}: {count} tokens exceeds target {target}")

    planned = registry.get("planned_common_loads")
    if not isinstance(planned, list) or not planned:
        result.error("planned_common_loads must be a non-empty list")
        planned = []
    known_ids = set(module_token_counts)
    load_ids: set[str] = set()
    for load in planned:
        if not isinstance(load, dict):
            result.error("planned_common_loads entries must be mappings")
            continue
        load_id = load.get("id")
        selected = load.get("modules")
        load_ceiling = load.get("token_ceiling")
        if not isinstance(load_id, str) or not load_id.strip():
            result.error("planned common load requires a non-empty id")
            load_id = "<missing>"
        elif load_id in load_ids:
            result.error(f"duplicate planned common load id: {load_id}")
        load_ids.add(load_id)
        if (
            not isinstance(selected, list)
            or not selected
            or not all(isinstance(module_id, str) and module_id for module_id in selected)
        ):
            result.error(
                f"planned common load {load_id}: modules must be a non-empty string list"
            )
            continue
        if len(selected) != len(set(selected)):
            result.error(f"planned common load {load_id}: duplicate module IDs")
        unknown = sorted(set(selected) - known_ids)
        if unknown:
            result.error(
                f"planned common load {load_id}: unknown module IDs "
                + ", ".join(unknown)
            )
        if len(selected) > max_leaves:
            report_overrun(
                f"planned common load {load_id}: {len(selected)} leaves exceeds {max_leaves}"
            )
        if not _positive_int(load_ceiling):
            result.error(
                f"planned common load {load_id}: token_ceiling must be a positive integer"
            )
            continue
        if load_ceiling > phase_ceiling:
            report_overrun(
                f"planned common load {load_id}: token_ceiling {load_ceiling} "
                f"exceeds phase ceiling {phase_ceiling}"
            )
        if not unknown:
            count = loaded_core_and_index + sum(
                module_token_counts[item] for item in selected
            )
            if count > load_ceiling:
                report_overrun(
                    f"planned common load {load_id}: {count} tokens exceeds ceiling "
                    f"{load_ceiling}"
                )
            if count > phase_ceiling:
                report_overrun(
                    f"planned common load {load_id}: {count} tokens exceeds phase "
                    f"ceiling {phase_ceiling}"
                )

    largest = sorted(module_token_counts.values(), reverse=True)[:max_leaves]
    largest_phase = loaded_core_and_index + sum(largest)
    result.metrics["core_plus_largest_phase"] = largest_phase
    if largest_phase > phase_ceiling:
        report_overrun(
            f"Core + index + {len(largest)} largest experts: {largest_phase} tokens "
            f"exceeds phase ceiling {phase_ceiling}"
        )


def _validate_legacy_budgets(
    module_token_counts: dict[str, int],
    core_tokens: int,
    index_tokens: int,
    result: Result,
) -> None:
    for module_id, count in module_token_counts.items():
        if count > 1800:
            result.error(f"{module_id}: {count} tokens exceeds 1800")
        if core_tokens + count > 3800:
            result.error(f"Core + {module_id}: {core_tokens + count} tokens exceeds 3800")
    if core_tokens > 1500:
        result.error(f"SKILL.md: {core_tokens} tokens exceeds 1500")
    if index_tokens > 450:
        result.error(f"generated index: {index_tokens} tokens exceeds 450")
    top_three = sorted(module_token_counts.values(), reverse=True)[:3]
    legacy_phase = core_tokens + sum(top_three)
    result.metrics["core_plus_three"] = legacy_phase
    if legacy_phase > 7000:
        result.error("Core + three largest experts exceeds 7000 tokens")


def validate_evidence_receipts(root: Path, modules: list[dict], result: Result) -> None:
    """Resolve current references to executed repository receipts, including failures.

    The runtime contains receipt identifiers, not development evidence. This
    repository-only check deliberately does not equate an evidence ID with pass.
    """
    referenced = {
        value for item in modules if isinstance(item.get("evidence"), list)
        for value in item["evidence"] if isinstance(value, str)
    }
    if not referenced:
        return
    path = root / "docs/evaluation/plan-0006-case-receipts.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        records = payload["receipts"]
        if payload.get("schema_version") != 1 or not isinstance(records, list):
            raise ValueError("unsupported receipt registry")
        by_id = {record["id"]: record for record in records}
        if len(by_id) != len(records):
            raise ValueError("duplicate receipt IDs")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result.error(f"executed evidence receipt registry unavailable: {exc}")
        return
    for receipt_id in sorted(referenced):
        record = by_id.get(receipt_id)
        if not isinstance(record, dict):
            result.error(f"{receipt_id}: unresolved executed evidence receipt")
            continue
        if record.get("executed") is not True:
            result.error(f"{receipt_id}: receipt is not executed")
        for field_name in ("case_version", "requested_model", "session_id", "executed_at"):
            if not isinstance(record.get(field_name), str) or not record[field_name].strip():
                result.error(f"{receipt_id}: missing {field_name}")
        settings = record.get("settings")
        if not isinstance(settings, dict) or not settings.get("effort") or not isinstance(settings.get("tools"), list):
            result.error(f"{receipt_id}: missing model/tool settings")
        if not isinstance(record.get("outcome"), str) or record["outcome"] not in {"pass", "fail", "limited", "unverified"}:
            result.error(f"{receipt_id}: invalid observed outcome")
        if not re.fullmatch(r"[A-F0-9]{64}", str(record.get("tested_package_sha256", ""))):
            result.error(f"{receipt_id}: missing tested package hash")
        artifacts = record.get("artifacts")
        if not isinstance(artifacts, list) or not artifacts:
            result.error(f"{receipt_id}: no observed artifacts or execution trace")
            continue
        for artifact in artifacts:
            if not isinstance(artifact, dict) or not isinstance(artifact.get("path"), str) or not artifact["path"]:
                result.error(f"{receipt_id}: invalid artifact record")
                continue
            artifact_path = Path(artifact["path"])
            if not artifact_path.is_absolute():
                artifact_path = root / artifact_path
            try:
                digest = hashlib.sha256(artifact_path.read_bytes()).hexdigest().upper()
                if digest != artifact.get("sha256"):
                    result.error(f"{receipt_id}: artifact hash mismatch: {artifact['path']}")
            except OSError:
                result.error(f"{receipt_id}: artifact unavailable: {artifact['path']}")


def validate_package(root: Path, schema: str, *, runtime: bool = False) -> Result:
    root = root.resolve()
    result = Result()
    if schema not in SCHEMAS:
        result.error(f"unknown validation schema: {schema}")
        return result
    successor = schema in (SUCCESSOR_SCHEMA, CURRENT_SCHEMA)
    if runtime and schema != CURRENT_SCHEMA:
        result.error("runtime derivative validation requires successor-v2")
        return result

    registry_path = root / "modules.yaml"
    skill_path = root / "SKILL.md"
    agent_path = root / "agents" / "openai.yaml"
    for required in (registry_path, skill_path, agent_path):
        if not required.is_file():
            result.error(f"missing required file: {required.relative_to(root)}")
    if result.errors:
        return result

    try:
        registry = load_registry(registry_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        result.error(f"invalid modules.yaml: {exc}")
        return result

    declared_schema = registry.get("package_schema")
    if successor:
        if declared_schema != schema:
            result.error(
                f"modules.yaml package_schema must be {schema!r}"
            )
        canonical_ids = CURRENT_CANONICAL_IDS if schema == CURRENT_SCHEMA else SUCCESSOR_CANONICAL_IDS
    else:
        if declared_schema not in (None, LEGACY_SCHEMA):
            result.error(
                f"modules.yaml package_schema is incompatible with {LEGACY_SCHEMA!r}"
            )
        canonical_ids = LEGACY_CANONICAL_IDS

    modules = registry["modules"]
    ids = [item.get("id") if isinstance(item, dict) else None for item in modules]
    if ids != canonical_ids:
        result.error(f"canonical module IDs/order differ: {ids}")
    if len(ids) != len(set(ids)):
        result.error("duplicate module IDs")

    signals = registry.get("signal_enum")
    if not isinstance(signals, list) or not all(
        isinstance(signal, str) and signal for signal in signals
    ):
        result.error("signal_enum must be a list of non-empty strings")
        signals = []
    elif len(signals) != len(set(signals)):
        result.error("signal_enum must be unique")
    signal_set = set(signals)
    signal_owner: dict[str, str] = {}
    owned: dict[str, str] = {}
    referenced_paths: set[Path] = set()
    module_token_counts: dict[str, int] = {}
    module_sources: dict[str, set[str]] = {}

    if successor:
        non_routed = registry.get("non_routed_references")
        if non_routed != ["references/source-index.md"]:
            result.error(
                "non_routed_references must contain exactly references/source-index.md"
            )
        source_path = root / "references" / "source-index.md"
    else:
        if "non_routed_references" in registry:
            result.error("legacy-rc7 must not declare non_routed_references")
        source_path = root / "references" / "sources-and-attribution.md"

    if not source_path.is_file():
        result.error(f"missing required file: {source_path.relative_to(root)}")
        registered_sources: set[str] = set()
    else:
        source_text = source_path.read_text(encoding="utf-8")
        registered_sources = _source_headings(source_text, result)
        if schema == CURRENT_SCHEMA:
            local_entry = re.search(
                r"^### SRC-PACKAGE-LOCAL-SYNTHESIS\s*\n(.*?)(?=^### |\Z)",
                source_text, re.MULTILINE | re.DOTALL,
            )
            if not local_entry or not re.search(r"^Class: local-synthesis\s*$", local_entry[1], re.MULTILINE):
                result.error("successor-v2 requires the registered local-synthesis entry and class")

    for item in modules:
        if not isinstance(item, dict):
            result.error("modules entries must be mappings")
            continue
        module_id = item.get("id", "<missing>")
        status = item.get("status")
        intervention = item.get("intervention")
        allowed_statuses = {"draft"} if schema == CURRENT_SCHEMA else STATUSES
        if status not in allowed_statuses:
            result.error(f"{module_id}: invalid status {status!r}")
        if intervention not in INTERVENTIONS:
            result.error(f"{module_id}: invalid intervention {intervention!r}")
        if item.get("requires") != [] or item.get("conflicts") != []:
            result.error(f"{module_id}: requires/conflicts must be explicit empty lists")

        for field_name in ("when_any", "unless"):
            values = item.get(field_name)
            if not isinstance(values, list) or not all(
                isinstance(value, str) and value for value in values
            ):
                result.error(
                    f"{module_id}: {field_name} must be a list of non-empty strings"
                )
                continue
            unknown = sorted(set(values) - signal_set)
            if unknown:
                result.error(
                    f"{module_id}: {field_name} contains unknown signals "
                    + ", ".join(unknown)
                )
        for signal in item.get("when_any", []):
            if not isinstance(signal, str):
                continue
            previous = signal_owner.get(signal)
            if previous:
                result.error(
                    f"signal ownership collision: {signal} in {previous} and {module_id}"
                )
            else:
                signal_owner[signal] = module_id

        concerns = item.get("owns")
        if (
            not isinstance(concerns, list)
            or not concerns
            or not all(isinstance(concern, str) and concern for concern in concerns)
        ):
            result.error(f"{module_id}: owns must be a non-empty string list")
            concerns = []
        for concern in concerns:
            previous = owned.get(concern)
            if previous:
                result.error(
                    f"ownership collision: {concern} in {previous} and {module_id}"
                )
            else:
                owned[concern] = module_id

        relative_text = _normal_path(item.get("path", ""))
        relative = PurePosixPath(relative_text)
        if (
            len(relative.parts) != 2
            or relative.parts[0] != "references"
            or relative.suffix != ".md"
        ):
            result.error(
                f"{module_id}: path must be a Markdown file directly under references/"
            )
            continue
        target = root.joinpath(*relative.parts)
        resolved_target = target.resolve()
        if resolved_target in referenced_paths:
            result.error(f"{module_id}: duplicate module path {relative_text}")
        referenced_paths.add(resolved_target)
        if successor and relative_text == "references/source-index.md":
            result.error(f"{module_id}: source-index.md must remain non-routed")
        if not target.is_file():
            result.error(f"{module_id}: missing reference {relative_text}")
            continue

        content = target.read_text(encoding="utf-8")
        if schema == CURRENT_SCHEMA:
            for label, value in (("Status", status), ("Intervention", intervention)):
                if re.findall(rf"^{label}: `(.*?)`  $", content, re.MULTILINE) != [value]:
                    result.error(f"{module_id}: {label} header must match registry with standard formatting")
            evidence = item.get("evidence")
            if not isinstance(evidence, list) or not all(
                isinstance(value, str) and re.fullmatch(r"P6-[A-Z0-9][A-Z0-9._-]*", value)
                for value in evidence
            ):
                result.error(f"{module_id}: evidence must list executed P6 receipt IDs or be empty")
            elif len(evidence) != len(set(evidence)):
                result.error(f"{module_id}: duplicate evidence receipt")
        module_token_counts[module_id] = tokens(content)
        sibling_links = [
            link for link in MARKDOWN_LINK.findall(content) if _is_sibling_reference_link(link)
        ]
        if sibling_links:
            result.error(
                f"{module_id}: sibling reference link found: {sibling_links[0]}"
            )

        declared = item.get("sources")
        if (
            not isinstance(declared, list)
            or not declared
            or not all(isinstance(source_id, str) for source_id in declared)
        ):
            result.error(f"{module_id}: sources must be a non-empty string list")
            declared = []
        if len(declared) != len(set(declared)):
            result.error(f"{module_id}: duplicate declared source ID")
        for source_id in declared:
            if not SOURCE_ID.fullmatch(source_id):
                result.error(f"{module_id}: invalid source ID {source_id}")
            elif source_id not in registered_sources:
                result.error(f"{module_id}: unresolved source ID {source_id}")
        header_sources = _source_ids_from_header(content, module_id, result)
        if header_sources != declared:
            result.error(
                f"{module_id}: Sources: header must equal modules.yaml sources in order"
            )
        module_sources[module_id] = set(declared)

    unused_signals = sorted(signal_set - set(signal_owner))
    if unused_signals:
        result.error("signal_enum contains unowned signals: " + ", ".join(unused_signals))

    actual_reference_files = {
        path.resolve() for path in (root / "references").glob("*.md")
    }
    allowed_non_routed = {source_path.resolve()} if successor else set()
    expected_reference_files = referenced_paths | allowed_non_routed
    orphans = sorted(actual_reference_files - expected_reference_files)
    missing_expected = sorted(expected_reference_files - actual_reference_files)
    if orphans:
        result.error("orphan references: " + ", ".join(path.name for path in orphans))
    if missing_expected:
        result.error(
            "declared reference files missing: "
            + ", ".join(path.name for path in missing_expected)
        )

    if schema == CURRENT_SCHEMA and not runtime:
        validate_evidence_receipts(root, modules, result)

    if successor and not runtime:
        _validate_rule_source_map(
            root / "docs" / "research" / "rule-source-map.md",
            set(ids),
            module_sources,
            registered_sources,
            result,
        )

    skill_text = skill_path.read_text(encoding="utf-8")
    try:
        index_text = render_index(registry)
        if runtime:
            index_text = index_text.replace(GENERATED + "\n", "")
        expected_skill = replace_index(skill_text, index_text)
    except (KeyError, TypeError, ValueError) as exc:
        result.error(f"cannot render generated module index: {exc}")
        index_text = ""
        expected_skill = skill_text
    if skill_text != expected_skill:
        result.error("generated module index drift")
    full_skill_tokens = tokens(skill_text)
    if successor:
        try:
            core_tokens = tokens(successor_core_text(skill_text))
        except ValueError as exc:
            result.error(f"cannot measure successor Core: {exc}")
            core_tokens = full_skill_tokens
    else:
        # Preserve RC7's historical metric: its Core count included the
        # generated index because the old validator measured all SKILL.md text.
        core_tokens = full_skill_tokens
    index_tokens = tokens(index_text)
    result.metrics.update(
        {
            "modules": len(modules),
            "core_tokens": core_tokens,
            "index_tokens": index_tokens,
            "max_expert_tokens": max(module_token_counts.values(), default=0),
        }
    )

    linked = set(DIRECT_MODULE_LINK.findall(skill_text))
    expected_links = {
        _normal_path(item.get("path", ""))
        for item in modules
        if isinstance(item, dict)
    }
    if linked != expected_links:
        result.error("SKILL.md direct links do not equal modules.yaml paths")

    if successor:
        if schema == CURRENT_SCHEMA and registry.get("budget", {}).get("policy") != "advisory":
            result.error("successor-v2 budget.policy must be advisory")
        _validate_successor_budgets(
            registry,
            modules,
            module_token_counts,
            core_tokens,
            index_tokens,
            result,
        )
    else:
        _validate_legacy_budgets(
            module_token_counts, core_tokens, index_tokens, result
        )

    try:
        agent = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
        default_prompt = agent["interface"]["default_prompt"]
        short_description = agent["interface"]["short_description"]
        if "$scoville-design-anti-ai-slop" not in default_prompt:
            result.error("agents/openai.yaml default_prompt must name the skill")
        if not 25 <= len(short_description) <= 64:
            result.error("agents/openai.yaml short_description must be 25-64 characters")
    except (KeyError, TypeError, yaml.YAMLError) as exc:
        result.error(f"invalid agents/openai.yaml: {exc}")

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Scoville Design package")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--schema",
        choices=SCHEMAS,
        default=CURRENT_SCHEMA,
        help=(
            "Validation contract. successor-v2 is current; select successor-v1 "
            "or legacy-rc7 explicitly for historical packages."
        ),
    )
    parser.add_argument("--runtime", action="store_true", help="Validate the comment-stripped v2 derivative without repository-only source-map checks")
    args = parser.parse_args()
    result = validate_package(args.root, args.schema, runtime=args.runtime)

    for warning in result.warnings:
        print(f"WARNING {warning}")
    if result.errors:
        print(f"INVALID errors={len(result.errors)} warnings={len(result.warnings)}")
        for error in result.errors:
            print(f"ERROR {error}")
        return 1

    metrics = " ".join(f"{key}={value}" for key, value in result.metrics.items())
    print(f"VALID schema={args.schema} warnings={len(result.warnings)} {metrics}".rstrip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
