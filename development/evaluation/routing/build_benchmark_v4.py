#!/usr/bin/env python3
"""Build adjudicated RC3 routing regression without rewriting v3 evidence."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "benchmark-v3"
TARGET = ROOT / "benchmark-v4"
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


CORRECTED = {
    "route-rc2-train-privacy": [
        "brand-and-visual-systems",
        "critique-and-validation",
        "culture-ethics-and-provenance",
    ],
    "route-rc2-train-type-exception": [
        "typography-and-writing-systems",
        "colour-and-reproduction",
        "critique-and-validation",
    ],
    "route-rc2-val-editorial-template": [
        "composition-and-layout",
        "brand-and-visual-systems",
    ],
}


def reference(module_id: str) -> str:
    return f".agents/skills/scoville-design-anti-ai-slop/references/{module_id}.md"


def main() -> int:
    for split in ("train", "val", "test"):
        items = copy.deepcopy(
            json.loads((SOURCE / split / "items.json").read_text(encoding="utf-8"))
        )
        for item in items:
            selected = CORRECTED.get(item["id"])
            if selected is None:
                continue
            selected_reads = [reference(module_id) for module_id in selected]
            required = [SKILL, *selected_reads]
            item["scoring"].update(
                {
                    "expected": {"status": "ok", "selected_modules": selected},
                    "required_file_reads": required,
                    "forbidden_file_reads": [
                        *[
                            reference(module_id)
                            for module_id in MODULES
                            if module_id not in selected
                        ],
                        BRIEF,
                    ],
                    "exact_once_file_reads": required,
                    "required_read_phases": [[SKILL], selected_reads],
                    "max_shell_calls": len(required),
                }
            )
        output = TARGET / split / "items.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(items, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print("wrote adjudicated design routing benchmark-v4")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
