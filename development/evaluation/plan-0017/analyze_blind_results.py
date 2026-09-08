#!/usr/bin/env python3
"""Unblind PLAN-0017 only after a user review has been supplied."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAIR_ROOT = ROOT / "final-pairs"


def parse_user_review(text: str) -> list[dict]:
    sections = re.split(r"(?m)^##\s+", text)[1:]
    parsed = []
    for section in sections:
        title, _, body = section.partition("\n")
        ranks = {
            int(image): int(rank)
            for image, rank in re.findall(r"(?m)^Bild\s+([12]):\s+Rang\s+([12])\s*$", body)
        }
        parsed.append({"title": title.strip(), "ranks": ranks, "text": body.rstrip()})
    return parsed


def parse_root_review(text: str) -> dict[str, dict[int, int]]:
    found: dict[str, dict[int, int]] = {}
    for line in text.splitlines():
        match = re.match(r"\|\s*(\d{2})\s+.*?\|\s*([12])\s*\|\s*([12])\s*\|", line)
        if match:
            found[match.group(1)] = {1: int(match.group(2)), 2: int(match.group(3))}
    return found


def condition_ranks(image_ranks: dict[int, int], mapping: dict) -> dict[str, int]:
    result = {}
    for image in (1, 2):
        rank = image_ranks.get(image)
        condition = mapping.get(f"image_{image}")
        if rank in (1, 2) and condition in {"skill", "no-skill"}:
            result[condition] = rank
    return result


def analyse(user_text: str, key: dict, manifest: dict, root_text: str) -> dict:
    user_sections = parse_user_review(user_text)
    root_ranks = parse_root_review(root_text)
    mappings = {item["id"]: item for item in key["tasks"]}
    records = []
    for index, brief in enumerate(manifest["briefs"]):
        task_id = brief["id"]
        user = user_sections[index] if index < len(user_sections) else {"title": "", "ranks": {}, "text": ""}
        user_condition = condition_ranks(user["ranks"], mappings[task_id])
        root_condition = condition_ranks(root_ranks.get(task_id, {}), mappings[task_id])
        user_complete = sorted(user_condition.values()) == [1, 2]
        root_complete = sorted(root_condition.values()) == [1, 2]
        records.append({
            "task": task_id,
            "output_type": brief["output_type"],
            "public_mapping": {"image_1": mappings[task_id]["image_1"], "image_2": mappings[task_id]["image_2"]},
            "user": {"complete": user_complete, "condition_ranks": user_condition, "verbatim_section": user["text"]},
            "root": {"complete": root_complete, "condition_ranks": root_condition},
            "same_winner": user_complete and root_complete and user_condition.get("skill") == root_condition.get("skill"),
        })
    complete = [record for record in records if record["user"]["complete"]]
    root_complete = [record for record in records if record["root"]["complete"]]
    agreements = [record for record in complete if record["root"]["complete"] and record["same_winner"]]
    return {
        "schema_version": 1,
        "user_review_sha256": hashlib.sha256(user_text.encode("utf-8")).hexdigest(),
        "user_complete_tasks": len(complete),
        "user_skill_wins": sum(record["user"]["condition_ranks"].get("skill") == 1 for record in complete),
        "user_no_skill_wins": sum(record["user"]["condition_ranks"].get("no-skill") == 1 for record in complete),
        "root_complete_tasks": len(root_complete),
        "root_skill_wins": sum(record["root"]["condition_ranks"].get("skill") == 1 for record in root_complete),
        "root_no_skill_wins": sum(record["root"]["condition_ranks"].get("no-skill") == 1 for record in root_complete),
        "same_winner_count": len(agreements),
        "comparable_count": sum(record["user"]["complete"] and record["root"]["complete"] for record in records),
        "records": records,
        "limits": [
            "Missing user ranks are retained as missing and are not imputed.",
            "The paired set is exploratory and is not a population estimate.",
            "Execution order was not fully randomized; order-effect claims are unavailable.",
            "Standalone diagnosis and repair lanes were not run under ADR-0062.",
        ],
    }


def markdown(result: dict) -> str:
    lines = [
        "# PLAN-0017 final paired comparison",
        "",
        f"User: {result['user_skill_wins']} Skill wins, {result['user_no_skill_wins']} no-Skill wins across {result['user_complete_tasks']} complete tasks.",
        f"Independent reviewer: {result['root_skill_wins']} Skill wins, {result['root_no_skill_wins']} no-Skill wins across {result['root_complete_tasks']} complete tasks.",
        f"Same winner: {result['same_winner_count']} of {result['comparable_count']} comparable tasks.",
        "",
        "| Task | User Skill rank | User no-Skill rank | Reviewer Skill rank | Reviewer no-Skill rank | Same winner |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in result["records"]:
        user = record["user"]["condition_ranks"]
        root = record["root"]["condition_ranks"]
        same = "yes" if record["same_winner"] else "no" if record["user"]["complete"] and record["root"]["complete"] else "missing"
        lines.append(f"| {record['task']} | {user.get('skill', 'missing')} | {user.get('no-skill', 'missing')} | {root.get('skill', 'missing')} | {root.get('no-skill', 'missing')} | {same} |")
    lines += ["", "## Limits", ""] + [f"- {item}" for item in result["limits"]]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("user_review", type=Path)
    parser.add_argument("--key", type=Path, default=PAIR_ROOT / "blinding-key.json")
    parser.add_argument("--manifest", type=Path, default=PAIR_ROOT / "manifest.json")
    parser.add_argument("--root-review", type=Path, default=ROOT / "root-independent-blind-review.md")
    parser.add_argument("--json-output", type=Path, default=ROOT / "final-comparison.json")
    parser.add_argument("--markdown-output", type=Path, default=ROOT / "final-comparison.md")
    args = parser.parse_args()
    user_text = args.user_review.read_text(encoding="utf-8")
    result = analyse(
        user_text,
        json.loads(args.key.read_text(encoding="utf-8")),
        json.loads(args.manifest.read_text(encoding="utf-8")),
        args.root_review.read_text(encoding="utf-8"),
    )
    args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.markdown_output.write_text(markdown(result), encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("user_complete_tasks", "user_skill_wins", "user_no_skill_wins", "same_winner_count", "comparable_count")}, indent=2))


if __name__ == "__main__":
    main()
