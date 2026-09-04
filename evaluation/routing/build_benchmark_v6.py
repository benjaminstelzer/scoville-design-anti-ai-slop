#!/usr/bin/env python3
"""Add final general-imagery and jurisdiction route probes to v5."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "benchmark-v5"
TARGET = ROOT / "benchmark-v6"
SKILL = ".agents/skills/scoville-design-anti-ai-slop/SKILL.md"
BRIEF = "brief/task-context.md"
MODULES = [
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


def reference(module_id: str) -> str:
    return f".agents/skills/scoville-design-anti-ai-slop/references/{module_id}.md"


def item(case_id: str, task: str, selected: list[str]) -> dict[str, object]:
    selected_reads = [reference(module_id) for module_id in selected]
    required = [SKILL, *selected_reads]
    return {
        "id": case_id,
        "task_type": "design_routing_probe",
        "prediction": {
            "task_text": (
                "Routing-only probe. Read only the applicable Scoville Design "
                f"experts. Do not create or change an artifact. {task} Return "
                "only the exact contracted JSON."
            ),
            "files": {BRIEF: "No additional task context.\n"},
            "output_contract": (
                "Return exactly one JSON object with keys status and "
                "selected_modules. status must be ok. selected_modules must be "
                "an array containing only the applicable canonical module IDs "
                "in direct-index order."
            ),
            "skill_activation": "explicit",
        },
        "scoring": {
            "expected": {"status": "ok", "selected_modules": selected},
            "required_file_reads": required,
            "forbidden_file_reads": [
                *[reference(module_id) for module_id in MODULES if module_id not in selected],
                BRIEF,
            ],
            "exact_once_file_reads": required,
            "required_read_phases": [[SKILL], selected_reads],
            "required_command_patterns": [],
            "forbidden_command_patterns": [
                "curl|wget|Invoke-WebRequest|Set-Content|Remove-Item|apply_patch"
            ],
            "max_shell_calls": len(required),
        },
    }


def main() -> int:
    additions = {
        "train": item(
            "route-rc5-train-general-imagery",
            "Direct a non-documentary editorial photography and illustration sequence with intentional crops.",
            ["imagery-and-art-direction"],
        ),
        "val": item(
            "route-rc5-val-jurisdiction-only",
            "Map authority and escalation for an unspecified jurisdictional design duty without researching or verifying the law.",
            ["culture-ethics-and-provenance"],
        ),
    }
    for split in ("train", "val", "test"):
        items = copy.deepcopy(
            json.loads((SOURCE / split / "items.json").read_text(encoding="utf-8"))
        )
        if split in additions:
            items.append(additions[split])
        output = TARGET / split / "items.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(items, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print("wrote final design routing benchmark-v6")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
