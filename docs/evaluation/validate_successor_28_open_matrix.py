#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "docs" / "evaluation" / "successor-28-open-matrix.yaml"


def main() -> int:
    data = yaml.safe_load(MATRIX.read_text(encoding="utf-8"))
    registry = yaml.safe_load((ROOT / "modules.yaml").read_text(encoding="utf-8"))
    errors: list[str] = []
    module_ids = {item["id"] for item in registry["modules"]}
    budget = data.get("budget", {})
    cases = data.get("cases", [])
    case_ids = [case.get("id") for case in cases]
    dimensions = set(data.get("required_dimensions", []))

    if data.get("model") != "gpt-5.6-terra" or data.get("reasoning") != "medium":
        errors.append("model and reasoning must be exact gpt-5.6-terra/medium")
    if data.get("execution") != "one_at_a_time_immediate_inspection":
        errors.append("execution must stop for immediate per-call inspection")
    if data.get("work_item") != "W-017" or data.get("execution_status") != "complete_no_qualified_pass":
        errors.append("terminal contract must be W-017 complete without a qualified pass")
    if len(cases) != 10 or len(case_ids) != len(set(case_ids)):
        errors.append("matrix must contain exactly ten unique named cases")
    if budget.get("remaining_named_calls") != 0:
        errors.append("remaining named allocation must be zero")
    if budget.get("conditional_paired_skillopt_calls") != 0:
        errors.append("conditional SkillOpt allocation must be zero")
    if budget.get("retry_reserve_calls") != 0:
        errors.append("retry reserve allocation must be zero")
    if budget.get("max_remaining_terminal_calls") != 0:
        errors.append("maximum remaining terminal calls must be zero")
    if budget.get("cost_stops") != "none":
        errors.append("W-017 must contain no token or monetary cost stop")
    forbidden_cost_keys = {
        "provider_total_ceiling",
        "uncached_input_plus_output_ceiling",
        "ordinary_call_provider_total_stop",
        "ordinary_call_uncached_input_plus_output_stop",
    }
    if forbidden_cost_keys & set(budget):
        errors.append("superseded cost ceiling fields remain in active budget")
    if budget.get("sealed_calls") != 0:
        errors.append("W-017 must contain no sealed calls")
    if dimensions != {
        "exact_route",
        "generation_or_repair",
        "owner_and_stop",
        "context_render_or_trace",
        "claim_boundary",
        "evidence_honesty",
    }:
        errors.append("required evidence dimensions changed")

    for case in cases:
        selected = case.get("selected", [])
        forbidden = case.get("forbidden", [])
        unknown = (set(selected) | set(forbidden)) - module_ids
        if unknown:
            errors.append(f"{case.get('id')}: unknown modules {sorted(unknown)}")
        if len(selected) > data["context"]["max_leaves"]:
            errors.append(f"{case.get('id')}: selects more than four leaves")
        if set(selected) & set(forbidden):
            errors.append(f"{case.get('id')}: selected and forbidden collide")
        if case.get("mode") not in {"generate", "critique", "repair", "style-direction"}:
            errors.append(f"{case.get('id')}: invalid canonical mode")
        if not case.get("proof"):
            errors.append(f"{case.get('id')}: missing proof contract")

    reserves = data.get("reserves", {})
    coverage_reserves = reserves.get("coverage", [])
    if coverage_reserves != []:
        errors.append("coverage reserve must remain empty")
    if reserves.get("skillopt") != []:
        errors.append("SkillOpt reserve must remain empty")

    pairs = data.get("skillopt_pairs", [])
    if len(pairs) != 3 or len({item.get("case") for item in pairs}) != 3:
        errors.append("SkillOpt requires three unique case pairs")
    for pair in pairs:
        if pair.get("case") not in case_ids:
            errors.append(f"{pair.get('id')}: unknown paired case")
        unknown = set(pair.get("editable_owners", [])) - module_ids - {"core"}
        if unknown:
            errors.append(f"{pair.get('id')}: unknown editable owners {sorted(unknown)}")
    pair_statuses = {pair.get("id"): pair.get("status") for pair in pairs}
    if pair_statuses.get("D28-SO1") != "ineligible_named_case_no_pass":
        errors.append("D28-SO1 must remain ineligible after D28-CI2 failed frozen route Gold")
    if pair_statuses.get("D28-SO2") != "ineligible_named_case_no_pass":
        errors.append("D28-SO2 must remain ineligible after D28-AD1 failed its named case")
    if pair_statuses.get("D28-SO3") != "ineligible_named_case_no_pass":
        errors.append("D28-SO3 must remain ineligible after D28-PK1 timed out")

    if data.get("historical_calls", {}).get("qualification_credit") != 0:
        errors.append("historical calls must grant zero new-snapshot credit")

    progress = data.get("progress", {})
    expected_remaining = set()
    if set(progress.get("remaining_case_ids", [])) != expected_remaining:
        errors.append("remaining case set changed")
    if progress.get("remaining_authorized_calls_under_current_contract") != 0:
        errors.append("remaining authorized call count must be zero")
    statuses = {case.get("id"): case.get("status") for case in cases}
    if statuses.get("D28-EH1") != "bounded_failure_no_rerun":
        errors.append("D28-EH1 failure state changed")
    if statuses.get("D28-CI1") != "failed_no_rerun":
        errors.append("D28-CI1 failure state changed")
    if statuses.get("D28-CI2") != "bounded_failure_no_rerun":
        errors.append("D28-CI2 failure state changed")
    if statuses.get("D28-CI3") != "bounded_failure_no_rerun":
        errors.append("D28-CI3 failure state changed")
    if statuses.get("D28-MK1") != "bounded_failure_no_rerun":
        errors.append("D28-MK1 failure state changed")
    if statuses.get("D28-IN1") != "bounded_failure_no_rerun":
        errors.append("D28-IN1 failure state changed")
    if statuses.get("D28-AD1") != "bounded_failure_no_rerun":
        errors.append("D28-AD1 failure state changed")
    if statuses.get("D28-PK1") != "infrastructure_timeout_no_rerun":
        errors.append("D28-PK1 timeout state changed")
    if statuses.get("D28-WF1") != "bounded_failure_no_rerun":
        errors.append("D28-WF1 failure state changed")
    if statuses.get("D28-BO1") != "bounded_failure_no_rerun":
        errors.append("D28-BO1 failure state changed")
    if any(statuses.get(case_id) != "pending" for case_id in expected_remaining):
        errors.append("one or more remaining cases are not pending")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"INVALID cases={len(cases)} errors={len(errors)}")
        return 1
    print(
        "VALID successor_28_open "
        f"cases={len(cases)} remaining_calls={budget['max_remaining_terminal_calls']} "
        f"modules={len(module_ids)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
