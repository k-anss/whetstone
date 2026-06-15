#!/usr/bin/env python3
"""Create the deterministic directory and metadata skeleton for an extraction project."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "meta/project-contract.md": """# Project Contract

- Source:
- Encoding: UTF-8
- Chapter pattern:
- Verified chapter count:
- Chunk size:
- Extraction lines:
- Result-state enum: 已完成 / 阶段完成 / 进行中 / 失败/反噬
- Quote policy: exact continuous source string, maximum 40 characters
- Active rule version: v1
- Map model:
- Review model:
- Synthesis model:
""",
    "meta/cost-record.md": """# Cost Record

| chunk | stage | model | input_tok | output_tok | events | A | B | errors | warnings | repairs | status | note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
""",
    "meta/progress.md": """# Progress

| chunk | range | evidence | candidates | validation | review | status |
|---|---|---|---|---|---|---|
""",
    "meta/regression/index.md": """# Regression Index

Record each important rule with one positive and one negative fixture.
""",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    args = parser.parse_args()
    root = args.project_dir
    for directory in ("raw", "audits", "cards", "final", "meta/regression"):
        (root / directory).mkdir(parents=True, exist_ok=True)
    for relative, content in FILES.items():
        path = root / relative
        if not path.exists():
            path.write_text(content, encoding="utf-8")
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
