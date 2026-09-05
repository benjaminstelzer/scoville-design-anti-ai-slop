#!/usr/bin/env python3
"""Clarify the settled-layout template-governance probe without changing Gold."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "benchmark-v7"
TARGET = ROOT / "benchmark-v8"


def main() -> int:
    for split in ("train", "val", "test"):
        items = copy.deepcopy(
            json.loads((SOURCE / split / "items.json").read_text(encoding="utf-8"))
        )
        for item in items:
            if item["id"] != "route-rc2-val-editorial-template":
                continue
            item["prediction"]["task_text"] = (
                "Routing-only probe. Read only the applicable Scoville Design "
                "experts. Do not create or change an artifact. Define only "
                "controlled variation, versioning, and approval for a recurring "
                "editorial-template system whose layout, hierarchy, grid, and "
                "spacing are already settled and out of scope. Return only the "
                "exact contracted JSON."
            )
        output = TARGET / split / "items.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(items, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print("wrote clarified design routing benchmark-v8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
