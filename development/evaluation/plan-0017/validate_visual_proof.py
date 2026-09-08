#!/usr/bin/env python3
"""Evaluator-side closure checks for PLAN-0017 relationship proofs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANES = {"pass", "fail", "unverified", "not-applicable"}
VERDICTS = LANES | {"disputed"}


def _binding(artifact: dict) -> tuple:
    return artifact.get("source_hash"), artifact.get("render_hash"), tuple(artifact.get("viewport", []))


def evaluate_bundle(bundle: dict) -> dict:
    required = bundle.get("required_relations", [])
    records = bundle.get("records", [])
    issues: list[dict] = []
    ids = [record.get("relation", {}).get("id") for record in records]
    for relation_id in required:
        if ids.count(relation_id) != 1:
            issues.append({"relation": relation_id, "code": "missing-or-duplicate-relation"})

    effective: dict[str, str] = {}
    for record in records:
        relation = record.get("relation", {})
        relation_id = relation.get("id") or "<missing>"
        artifact = record.get("artifact", {})
        visual = record.get("visual", {})
        measurement = record.get("measurement", {})
        verdict = record.get("verdict", {})
        local: list[str] = []

        if not all(relation.get(key) for key in ("id", "objects", "region_or_anchor", "intent", "target", "owner")):
            local.append("incomplete-relation")
        if visual.get("status") not in LANES or measurement.get("status") not in LANES or verdict.get("status") not in VERDICTS:
            local.append("invalid-status")
        if visual.get("status") in {"pass", "fail"}:
            receipt = visual.get("view_receipt")
            if not isinstance(receipt, dict) or _binding(receipt) != _binding(artifact):
                local.append("stale-or-unbound-visual")
            if visual.get("region") != relation.get("region_or_anchor"):
                local.append("visual-wrong-region")
        if measurement.get("status") in {"pass", "fail"}:
            receipt = measurement.get("receipt")
            if not isinstance(receipt, dict) or _binding(receipt) != _binding(artifact):
                local.append("stale-or-unbound-measurement")
            if measurement.get("support") != "supported":
                local.append("unsupported-metric")

        visual_status = visual.get("status", "unverified")
        measure_status = measurement.get("status", "unverified")
        claimed = verdict.get("status", "unverified")
        if local:
            resolved = "unverified"
        elif {visual_status, measure_status} == {"pass", "fail"}:
            resolved = "disputed"
        elif "fail" in {visual_status, measure_status}:
            resolved = "fail"
        elif visual_status == measure_status == "pass":
            resolved = "pass"
        elif visual_status == measure_status == "not-applicable":
            resolved = "not-applicable"
        else:
            resolved = "unverified"
        if claimed != resolved:
            local.append("verdict-does-not-follow-lanes")
        for code in local:
            issues.append({"relation": relation_id, "code": code})
        effective[relation_id] = resolved

    status = "unverified" if any(i["code"] == "missing-or-duplicate-relation" for i in issues) else (
        "fail" if "fail" in effective.values() else
        "disputed" if "disputed" in effective.values() else
        "unverified" if "unverified" in effective.values() else
        "pass" if effective and all(v == "pass" for v in effective.values()) else
        "not-applicable"
    )
    return {"status": status, "effective": effective, "issues": issues}


def extract_records(text: str) -> list[dict]:
    """Extract only JSON proof objects from fenced model output."""
    records = []
    for body in re.findall(r"```json\s*(.*?)\s*```", text, flags=re.I | re.S):
        value = json.loads(body)
        candidates = value if isinstance(value, list) else value.get("records", [value])
        records.extend(item for item in candidates if isinstance(item, dict) and "relation" in item)
    return records


if __name__ == "__main__":
    source = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate_bundle(source), indent=2))

