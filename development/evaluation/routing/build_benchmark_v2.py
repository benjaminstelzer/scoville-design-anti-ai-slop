#!/usr/bin/env python3
"""Create the adjudicated W-004 regression suite without rewriting v1."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "benchmark"
TARGET = ROOT / "benchmark-v2"
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


def main() -> int:
    for split in ("train", "val", "test"):
        items = json.loads((SOURCE / split / "items.json").read_text(encoding="utf-8"))
        items = copy.deepcopy(items)
        for item in items:
            if item["id"] != "route-val-culture":
                continue
            selected = [
                "imagery-and-art-direction",
                "culture-ethics-and-provenance",
                "sources-and-attribution",
            ]
            selected_reads = [reference(module_id) for module_id in selected]
            required = [SKILL, *selected_reads]
            item["scoring"].update(
                {
                    "expected": {"status": "ok", "selected_modules": selected},
                    "required_file_reads": required,
                    "forbidden_file_reads": [
                        *[reference(module_id) for module_id in MODULES if module_id not in selected],
                        BRIEF,
                    ],
                    "exact_once_file_reads": required,
                    "required_read_phases": [[SKILL], selected_reads],
                    "max_shell_calls": len(required),
                }
            )
        out = TARGET / split / "items.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print("wrote adjudicated design routing benchmark-v2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

