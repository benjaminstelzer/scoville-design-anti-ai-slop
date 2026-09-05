#!/usr/bin/env python3
"""Build the open audit-driven RC2 routing regression suite."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "benchmark-v3"
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
            "required_read_phases": [[SKILL], selected_reads] if selected_reads else [[SKILL]],
            "required_command_patterns": [],
            "forbidden_command_patterns": [
                "curl|wget|Invoke-WebRequest|Set-Content|Remove-Item|apply_patch"
            ],
            "max_shell_calls": len(required),
        },
    }


def write(split: str, items: list[dict[str, object]]) -> None:
    path = TARGET / split / "items.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(items, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    write(
        "train",
        [
            item(
                "route-rc2-train-privacy",
                "Audit a campaign using identifiable participant data and unclear consent.",
                ["culture-ethics-and-provenance"],
            ),
            item(
                "route-rc2-train-sustainability",
                "Audit an unsupported recycled-material sustainability claim and verify its source.",
                ["culture-ethics-and-provenance", "sources-and-attribution"],
            ),
            item(
                "route-rc2-train-template-system",
                "Define governance for a recurring report-template family across touchpoints.",
                ["brand-and-visual-systems"],
            ),
            item(
                "route-rc2-train-type-exception",
                "Critique a deliberate low-contrast display-type exception without treating it as a layout problem.",
                ["typography-and-writing-systems", "critique-and-validation"],
            ),
            item(
                "route-rc2-train-critique-only",
                "Perform a deep read-only critique and propose, but do not apply, the smallest repair.",
                ["critique-and-validation"],
            ),
        ],
    )
    write(
        "val",
        [
            item(
                "route-rc2-val-synthetic-documentary",
                "Audit an AI-generated image presented as documentary evidence, including rights and factual-source checks.",
                [
                    "imagery-and-art-direction",
                    "culture-ethics-and-provenance",
                    "sources-and-attribution",
                ],
            ),
            item(
                "route-rc2-val-jurisdiction",
                "Audit a privacy-sensitive design whose current jurisdictional duty and cited facts must be verified.",
                ["culture-ethics-and-provenance", "sources-and-attribution"],
            ),
            item(
                "route-rc2-val-editorial-template",
                "Define controlled variation and approval for a recurring editorial-template system.",
                ["brand-and-visual-systems"],
            ),
            item(
                "route-rc2-val-motion-exception",
                "Critique a deliberate jitter and abrupt-cut motion exception without loading composition.",
                ["motion-and-sequence", "critique-and-validation"],
            ),
            item(
                "route-rc2-val-layout-exception",
                "Critique an intentional off-grid layout exception and its compensating structure.",
                ["composition-and-layout", "critique-and-validation"],
            ),
        ],
    )
    consumed = json.loads(
        (ROOT / "benchmark-v2" / "test" / "items.json").read_text(encoding="utf-8")
    )
    write("test", consumed)
    print("wrote open audit-driven design routing benchmark-v3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
