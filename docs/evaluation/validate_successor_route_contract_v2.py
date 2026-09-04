#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "docs" / "evaluation" / "successor-route-contract-v2.yaml"
OLD = ROOT / "docs" / "evaluation" / "successor-28-open-matrix.yaml"


def main() -> int:
    data = yaml.safe_load(CONTRACT.read_text(encoding="utf-8"))
    old = yaml.safe_load(OLD.read_text(encoding="utf-8"))
    modules = yaml.safe_load((ROOT / "modules.yaml").read_text(encoding="utf-8"))
    known = {item["id"] for item in modules["modules"]}
    errors: list[str] = []
    cases = data.get("cases", [])
    if data.get("contract_id") != "successor-route-v2" or len(cases) != 10:
        errors.append("contract id or ten-case count changed")
    ids = [case.get("id") for case in cases]
    old_ids = [case.get("id") for case in old.get("cases", [])]
    if ids != old_ids:
        errors.append("case order differs from immutable W-017 matrix")
    changed = {"D28-EH1", "D28-CI1", "D28-CI2", "D28-CI3"}
    for case in cases:
        exact_sets = case.get("exact_sets", [])
        forbidden = set(case.get("forbidden", []))
        if len(exact_sets) != 1:
            errors.append(f"{case.get('id')}: requires exactly one exact set")
            continue
        exact = exact_sets[0]
        if not 1 <= len(exact) <= 4 or len(exact) != len(set(exact)):
            errors.append(f"{case.get('id')}: invalid exact set")
        unknown = (set(exact) | forbidden) - known
        if unknown:
            errors.append(f"{case.get('id')}: unknown modules {sorted(unknown)}")
        if set(exact) & forbidden:
            errors.append(f"{case.get('id')}: exact and forbidden collide")
        expected_relation = "changed_gold_was_too_narrow" if case.get("id") in changed else "unchanged"
        if case.get("w017_relation") != expected_relation:
            errors.append(f"{case.get('id')}: incorrect W-017 relation")
    evidence = data.get("blind_evidence", {})
    for key in (
        "tasks_sha256", "all_28_summaries_sha256", "phase1_output_sha256",
        "selected_full_clauses_sha256", "phase2_output_sha256", "alias_map_sha256",
    ):
        value = evidence.get(key, "")
        if len(value) != 64 or any(char not in "0123456789ABCDEF" for char in value):
            errors.append(f"invalid evidence hash: {key}")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"INVALID successor-route-v2 errors={len(errors)}")
        return 1
    print("VALID successor-route-v2 cases=10 changed=4 alternate_sets=0 modules=28")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
