#!/usr/bin/env python3
"""Copy v8 for repeated closed-vocabulary router validation."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "benchmark-v8"
TARGET = ROOT / "benchmark-v9"


def main() -> int:
    for split in ("train", "val", "test"):
        items = json.loads((SOURCE / split / "items.json").read_text(encoding="utf-8"))
        output = TARGET / split / "items.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(items, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print("wrote closed-vocabulary design routing benchmark-v9")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
