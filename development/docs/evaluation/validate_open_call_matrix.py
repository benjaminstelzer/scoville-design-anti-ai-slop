#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import yaml


EXPECTED_LEAVES = [
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
    "ui-workflow-and-interaction-design",
    "web-and-responsive-design",
    "editorial-and-fixed-media-design",
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
EXPECTED_MODES = ["generate", "critique", "repair", "style-direction"]
EXPECTED_DIMENSIONS = [
    "generation_or_decision",
    "critique",
    "repair",
    "exception_or_claim_boundary",
    "proof",
    "ownership",
]
EXPECTED_CASES = [f"C{index:02d}" for index in range(1, 23)]
EXPECTED_CANARIES = {"C01": 1, "C06": 2, "C11": 3, "C14": 4, "C18": 5}
EXPECTED_REQUIRED_MODES = {
    "composition-and-layout": ["generate", "critique", "repair"],
    "typography-and-typesetting": ["generate", "critique", "repair"],
    "web-and-responsive-design": ["generate", "critique", "repair"],
    "editorial-and-fixed-media-design": ["generate", "critique", "repair"],
    "critique-and-validation": ["generate", "critique", "repair"],
    "style-direction": ["style-direction", "critique", "repair"],
}


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    matrix_path = root / "docs" / "evaluation" / "leaf-contract-matrix.yaml"
    plan_path = root / "docs" / "evaluation" / "open-successor-call-plan.md"
    data = yaml.safe_load(matrix_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    if data.get("format_version") != 1:
        errors.append("format_version must be 1")
    if data.get("canonical_modes") != EXPECTED_MODES:
        errors.append("canonical_modes differ from the executable enum")
    if data.get("contract_dimensions") != EXPECTED_DIMENSIONS:
        errors.append("contract_dimensions differ")

    cases = data.get("cases") or {}
    assertions = data.get("assertions") or {}
    leaves = data.get("leaves") or {}
    if list(cases) != EXPECTED_CASES:
        errors.append("case IDs/order must be C01 through C22")
    if list(leaves) != EXPECTED_LEAVES:
        errors.append("leaf IDs/order differ from the reviewed registry")

    labels: dict[str, str] = {}
    credited: set[tuple[str, str, str]] = set()
    for leaf_id, leaf in leaves.items():
        label = leaf.get("label")
        if not isinstance(label, str) or not label:
            errors.append(f"{leaf_id}: missing display label")
        elif label in labels:
            errors.append(f"duplicate label {label!r}")
        else:
            labels[label] = leaf_id
        wave = leaf.get("implementation_wave")
        if not isinstance(wave, int) or wave not in range(1, 6):
            errors.append(f"{leaf_id}: invalid implementation_wave")
        required_modes = leaf.get("required_modes", [])
        expected_required = EXPECTED_REQUIRED_MODES.get(leaf_id, [])
        if required_modes != expected_required:
            errors.append(
                f"{leaf_id}: required_modes {required_modes} differ from {expected_required}"
            )
        if len(required_modes) != len(set(required_modes)) or not set(
            required_modes
        ).issubset(EXPECTED_MODES):
            errors.append(f"{leaf_id}: invalid or duplicate required_modes")
        for dimension in EXPECTED_DIMENSIONS:
            credits = leaf.get(dimension)
            if not isinstance(credits, list) or not credits:
                errors.append(f"{leaf_id}: empty {dimension}")
                continue
            for case_id in credits:
                credited.add((case_id, leaf_id, dimension))
                if case_id not in cases:
                    errors.append(f"{leaf_id}: unknown case {case_id} in {dimension}")
                elif leaf_id not in cases[case_id].get("leaves", []):
                    errors.append(
                        f"{leaf_id}: {case_id} credits {dimension} without selecting the leaf"
                    )

    asserted: set[tuple[str, str, str]] = set()
    if not isinstance(assertions, dict):
        errors.append("assertions must be a case-keyed mapping")
        assertions = {}
    for case_id, case_assertions in assertions.items():
        if case_id not in cases:
            errors.append(f"assertions: unknown case {case_id}")
            continue
        if not isinstance(case_assertions, dict) or not case_assertions:
            errors.append(f"{case_id}: assertions must be a non-empty leaf mapping")
            continue
        for leaf_id, dimension_assertions in case_assertions.items():
            if leaf_id not in leaves:
                errors.append(f"{case_id}: assertion for unknown leaf {leaf_id}")
                continue
            if leaf_id not in cases[case_id].get("leaves", []):
                errors.append(f"{case_id}: assertion for unselected leaf {leaf_id}")
            if not isinstance(dimension_assertions, dict) or not dimension_assertions:
                errors.append(f"{case_id}/{leaf_id}: empty dimension assertions")
                continue
            for dimension, assertion in dimension_assertions.items():
                triple = (case_id, leaf_id, dimension)
                asserted.add(triple)
                if dimension not in EXPECTED_DIMENSIONS:
                    errors.append(
                        f"{case_id}/{leaf_id}: unknown assertion dimension {dimension}"
                    )
                if not isinstance(assertion, str) or len(assertion.strip()) < 20:
                    errors.append(
                        f"{case_id}/{leaf_id}/{dimension}: assertion is missing or too vague"
                    )
    missing_assertions = credited - asserted
    extra_assertions = asserted - credited
    for case_id, leaf_id, dimension in sorted(missing_assertions):
        errors.append(f"{case_id}/{leaf_id}/{dimension}: credited without assertion")
    for case_id, leaf_id, dimension in sorted(extra_assertions):
        errors.append(f"{case_id}/{leaf_id}/{dimension}: assertion has no matrix credit")

    selected_union: set[str] = set()
    actual_canaries: dict[str, int] = {}
    for case_id, case in cases.items():
        wave = case.get("wave")
        mode = case.get("mode")
        selected = case.get("leaves")
        if wave not in range(1, 6):
            errors.append(f"{case_id}: invalid wave")
        if mode not in EXPECTED_MODES:
            errors.append(f"{case_id}: invalid canonical mode {mode!r}")
        if not isinstance(selected, list) or not selected:
            errors.append(f"{case_id}: selected leaves must be non-empty")
            continue
        if len(selected) != len(set(selected)):
            errors.append(f"{case_id}: duplicate selected leaf")
        provisional_max = (data.get("budget") or {}).get(
            "provisional_max_simultaneous_leaves"
        )
        if isinstance(provisional_max, int) and len(selected) > provisional_max:
            errors.append(
                f"{case_id}: {len(selected)} leaves exceeds provisional max "
                f"{provisional_max}"
            )
        for leaf_id in selected:
            selected_union.add(leaf_id)
            if leaf_id not in leaves:
                errors.append(f"{case_id}: unknown selected leaf {leaf_id}")
            elif leaves[leaf_id]["implementation_wave"] > wave:
                errors.append(
                    f"{case_id}: selects Wave {leaves[leaf_id]['implementation_wave']} "
                    f"leaf {leaf_id} in Wave {wave}"
                )
        if case.get("canary") is True:
            actual_canaries[case_id] = wave
    if actual_canaries != EXPECTED_CANARIES:
        errors.append(f"canaries differ: {actual_canaries}")
    if selected_union != set(EXPECTED_LEAVES):
        errors.append("not every reviewed leaf appears in a case")

    for leaf_id, required_modes in EXPECTED_REQUIRED_MODES.items():
        selected_modes = {
            case["mode"]
            for case in cases.values()
            if leaf_id in case.get("leaves", [])
        }
        missing_modes = set(required_modes) - selected_modes
        if missing_modes:
            errors.append(
                f"{leaf_id}: missing selected canonical modes {sorted(missing_modes)}"
            )

    budget = data.get("budget") or {}
    if budget.get("coverage_planned") != len(EXPECTED_CASES):
        errors.append("coverage_planned must equal the 22 frozen cases")
    calculated_max = sum(
        budget.get(field, 0)
        for field in (
            "coverage_planned",
            "coverage_reserve",
            "skillopt_planned",
            "skillopt_reserve",
        )
    )
    if budget.get("hard_call_maximum") != calculated_max or calculated_max != 46:
        errors.append("hard_call_maximum must equal planned plus reserve and remain 46")
    if budget.get("provisional_max_simultaneous_leaves") != 4:
        errors.append("provisional_max_simultaneous_leaves must remain 4")
    if budget.get("provisional_core_plus_leaves_maximum") != 15000:
        errors.append("provisional Core plus leaves maximum must remain 15000")

    markdown_cases: dict[str, tuple[set[str], str]] = {}
    for line in plan_path.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| C\d{2} \|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            errors.append(f"{cells[0]}: malformed Markdown case row")
            continue
        case_id = cells[0]
        selected_labels = {value.strip() for value in cells[2].split(",")}
        unknown_labels = selected_labels - set(labels)
        if unknown_labels:
            errors.append(f"{case_id}: unknown Markdown labels {sorted(unknown_labels)}")
        mode_match = re.match(r"^`([^`]+)`;", cells[3])
        if not mode_match:
            errors.append(f"{case_id}: Markdown row lacks one canonical mode")
            continue
        markdown_cases[case_id] = (
            {labels[label] for label in selected_labels if label in labels},
            mode_match.group(1),
        )
    if list(markdown_cases) != EXPECTED_CASES:
        errors.append("Markdown case rows/order differ from C01 through C22")
    for case_id, case in cases.items():
        if case_id not in markdown_cases:
            continue
        markdown_leaves, markdown_mode = markdown_cases[case_id]
        if markdown_leaves != set(case["leaves"]):
            errors.append(f"{case_id}: Markdown leaves differ from YAML")
        if markdown_mode != case["mode"]:
            errors.append(f"{case_id}: Markdown mode differs from YAML")

    if errors:
        print(f"INVALID errors={len(errors)}")
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(
        "VALID "
        f"leaves={len(leaves)} cases={len(cases)} dimensions={len(EXPECTED_DIMENSIONS)} "
        f"canaries={len(actual_canaries)} hard_call_maximum={calculated_max}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
