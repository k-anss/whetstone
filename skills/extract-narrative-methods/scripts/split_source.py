#!/usr/bin/env python3
"""Split a chaptered UTF-8 source into per-chapter files and an index."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from validate_cards import chinese_number_to_int


DEFAULT_PATTERN = r"(?m)^第(?P<number>[0-9零〇一二两三四五六七八九十百千万]+)章.*$"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--chapter-pattern", default=DEFAULT_PATTERN)
    args = parser.parse_args()

    text = args.source.read_text(encoding="utf-8")
    pattern = re.compile(args.chapter_pattern)
    matches = list(pattern.finditer(text))
    if not matches:
        parser.error("no chapter headings matched")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = ["# Chapter Index", "", "| chapter | file | start_char | end_char |", "|---:|---|---:|---:|"]
    seen: set[int] = set()
    for index, match in enumerate(matches):
        number = chinese_number_to_int(match.group("number"))
        if number in seen:
            parser.error(f"duplicate chapter number: {number}")
        seen.add(number)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        filename = f"chapter_{number:04d}.txt"
        (args.output_dir / filename).write_text(text[match.start():end], encoding="utf-8")
        rows.append(f"| {number} | {filename} | {match.start()} | {end} |")
    (args.output_dir / "index.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"chapters: {len(matches)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
