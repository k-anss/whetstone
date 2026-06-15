#!/usr/bin/env python3
"""Mechanical validation for narrative-method extraction artifacts."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# 标题识别故意宽松：认 ## ~ ####、"案例/管理案例"措辞可选，靠 ID 定位。
# 但 ID 只认 A/AC/B 前缀——这样卡片文件里诚实记录的「降级事件（E018…）」
# 不会被误当成缺字段的坏卡。这只放松“怎么找到卡”，深度/捏造/字段检查不松。
CARD_RE = re.compile(
    r"^#{2,4}\s+(?:(?P<management>管理)?案例[ \t]*)?(?P<id>(?:AC|A|B)\d{1,3})",
    re.MULTILINE,
)
EVENT_RE = re.compile(
    r"^#{2,4}\s+(?:事件[ \t]*)?(?P<id>E\d{1,3})", re.MULTILINE
)
RESULT_RE = re.compile(r"^-\s*结果状态：\s*(.+?)\s*$", re.MULTILINE)
QUOTE_RE = re.compile(
    r"^(?:-[ \t]*)?(?:▸[ \t]*)?关键原句：[ \t]*(.*?)[ \t]*$",
    re.MULTILINE,
)
# 定位锚：6–15 字、可在原文逐字 grep 的短片段，唯一职责是"证明没编造"。
# 引文（关键原句）负责表意、允许转述/截断/标点出入，不再参与校验。
ANCHOR_RE = re.compile(
    r"^(?:-[ \t]*)?(?:▸[ \t]*)?定位锚：[ \t]*(.*?)[ \t]*$",
    re.MULTILINE,
)
CHAPTER_RE = re.compile(r"^-\s*章节：\s*(.*?)\s*$", re.MULTILINE)
ALLOWED_RESULTS = {"已完成", "阶段完成", "进行中", "失败/反噬"}
EMPTY_CARDS_RE = re.compile(r"本块无合格[AB](?:线)?卡")
CHAPTER_HEADING_RE = re.compile(
    r"(?m)^第(?P<number>[0-9零〇一二两三四五六七八九十百千万]+)章(?:\s|$)"
)

PLACEHOLDER_PATTERNS = {
    "empty chapter": re.compile(r"第\s*[—-]\s*章|章节：\s*[—-]\s*$", re.MULTILINE),
    "pending completion": re.compile(r"待\s*(?:Codex|Claude|审核).*(?:细化|补充|正式成卡)"),
    "generic chunk placeholder": re.compile(r"本块(?:具体|内发生的具体|管理决策待|博弈结构待)"),
    "draft substitution": re.compile(r"高速概览|批量初稿|框架初稿|标题扫描|未精读"),
    "empty range": re.compile(r"范围：\s*[—-]\s*(?:；|$)", re.MULTILINE),
    "not applicable boundary": re.compile(r"边界：\s*≤?\s*N/A", re.IGNORECASE),
}

COMMON_REQUIRED = {
    "章节": re.compile(r"^-\s*章节：", re.MULTILINE),
    "结果状态": RESULT_RE,
    "实际代价": re.compile(r"^-\s*实际代价：\s*\S", re.MULTILINE),
}
A_REQUIRED = {
    "主体": re.compile(r"^-\s*主体：\s*\S", re.MULTILINE),
    "困境": re.compile(r"^-\s*困境：\s*\S", re.MULTILINE),
    "关键动作": re.compile(r"^-\s*关键动作：\s*\S", re.MULTILINE),
    "对方响应": re.compile(r"^-\s*对方(?:[/／·・]系统)?响应：\s*\S", re.MULTILINE),
    "成交/借力结构": re.compile(r"^-\s*成交[/／·・]借力结构：\s*\S", re.MULTILINE),
}
B_REQUIRED = {
    "决策者": re.compile(r"^-\s*决策者：\s*\S", re.MULTILINE),
    "管理困境": re.compile(r"^-\s*管理困境：\s*\S", re.MULTILINE),
    "决策": re.compile(r"^-\s*决策：\s*\S", re.MULTILINE),
    "执行响应": re.compile(r"^-\s*执行响应：\s*\S", re.MULTILINE),
    "管理逻辑": re.compile(r"^-\s*管理逻辑：\s*\S", re.MULTILINE),
}
EVENT_REQUIRED = {
    "章节": CHAPTER_RE,
    "参与者": re.compile(r"^-\s*参与者：\s*\S", re.MULTILINE),
    "客观动作": re.compile(r"^-\s*客观动作：\s*\S", re.MULTILINE),
    "响应": re.compile(r"^-\s*(?:对方[/／·・])?系统响应：\s*\S", re.MULTILINE),
    "直接结果": re.compile(r"^-\s*直接结果：\s*\S", re.MULTILINE),
    "结果状态": RESULT_RE,
}


@dataclass
class ArtifactResult:
    errors: list[str]
    warnings: list[str]
    review: list[str] = field(default_factory=list)
    empty_quotes: int = 0
    card_ids: tuple[str, ...] = ()


def chinese_number_to_int(value: str) -> int:
    if value.isdigit():
        return int(value)
    digits = {"零": 0, "〇": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
              "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
    units = {"十": 10, "百": 100, "千": 1000, "万": 10000}
    total = 0
    section = 0
    number = 0
    for char in value:
        if char in digits:
            number = digits[char]
            continue
        unit = units.get(char)
        if unit is None:
            raise ValueError(f"unsupported Chinese chapter number: {value}")
        if unit == 10000:
            section = (section + number) * unit
            total += section
            section = 0
        else:
            if number == 0:
                number = 1
            section += number * unit
        number = 0
    return total + section + number


def parse_chapter_numbers(value: str) -> set[int]:
    numbers: set[int] = set()
    for token in re.findall(r"[0-9零〇一二两三四五六七八九十百千万]+", value):
        try:
            numbers.add(chinese_number_to_int(token))
        except ValueError:
            continue
    return numbers


def clean_quote(raw: str) -> str:
    value = raw.strip()
    if value in {"", "无", "（无）", "N/A"} or re.match(
        r"^[（(](?:无合适|可空|留空)", value
    ):
        return ""
    value = re.sub(r"[（(](?:第?.{0,12}章|原文).*?[）)]\s*$", "", value)
    return value.strip("`“”\"' ")


def split_blocks(
    text: str, pattern: re.Pattern[str]
) -> list[tuple[str, str, bool]]:
    matches = list(pattern.finditer(text))
    blocks: list[tuple[str, str, bool]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        card_id = match.group("id")
        is_management = bool(match.groupdict().get("management")) or (
            card_id[:1].upper() == "B"
        )
        blocks.append((card_id, text[match.start():end], is_management))
    return blocks


_NEGATORS = "不未非没勿"


def _draft_substitution_admitted(text: str) -> bool:
    """True only when a skim word appears on a line that is NOT a denial.

    "本块为高速概览" is an admission (flag it). A line that also carries a
    negator — "全文未出现标题扫描…", "绝不用标题扫描" — is denying skimming and
    must not be flagged, even when it enumerates several banned words. Real
    skimming is independently caught by the event-density floor, so this check
    can stay conservative against false positives."""
    pattern = PLACEHOLDER_PATTERNS["draft substitution"]
    for line in text.splitlines():
        if pattern.search(line) and not any(neg in line for neg in _NEGATORS):
            return True
    return False


def find_placeholders(path: Path, text: str) -> list[str]:
    found: list[str] = []
    for label, pattern in PLACEHOLDER_PATTERNS.items():
        if label == "draft substitution":
            if _draft_substitution_admitted(text):
                found.append(f"{path}: placeholder detected ({label})")
        elif pattern.search(text):
            found.append(f"{path}: placeholder detected ({label})")
    return found


def source_slice(source: str, chapter_start: int, chapter_end: int) -> str:
    headings = list(CHAPTER_HEADING_RE.finditer(source))
    selected: list[str] = []
    for index, match in enumerate(headings):
        number = chinese_number_to_int(match.group("number"))
        if chapter_start <= number <= chapter_end:
            end = headings[index + 1].start() if index + 1 < len(headings) else len(source)
            selected.append(source[match.start():end])
    if not selected:
        raise ValueError(
            f"source contains no recognized chapters in {chapter_start}-{chapter_end}"
        )
    return "".join(selected)


def check_chapter_field(
    path: Path,
    item_id: str,
    body: str,
    chapter_start: int | None,
    chapter_end: int | None,
) -> list[str]:
    match = CHAPTER_RE.search(body)
    if not match:
        return [f"{path}:{item_id}: missing chapter field"]
    chapters = parse_chapter_numbers(match.group(1))
    if not chapters:
        return [f"{path}:{item_id}: chapter field has no parseable chapter number"]
    if chapter_start is not None and chapter_end is not None:
        outside = sorted(ch for ch in chapters if not chapter_start <= ch <= chapter_end)
        if outside:
            return [
                f"{path}:{item_id}: chapter reference outside assigned range: {outside}"
            ]
    return []


def validate_cards(
    path: Path,
    evidence_source: str | None,
    chapter_start: int | None,
    chapter_end: int | None,
    max_card_span: int | None = None,
) -> ArtifactResult:
    text = path.read_text(encoding="utf-8")
    errors = find_placeholders(path, text)
    warnings: list[str] = []
    review: list[str] = []
    cards = split_blocks(text, CARD_RE)
    if not cards:
        if not EMPTY_CARDS_RE.search(text):
            errors.append(f"{path}: no card headings or explicit no-card declaration found")
        return ArtifactResult(errors, warnings, review)

    seen: set[str] = set()
    empty_quotes = 0
    for card_id, body, is_management in cards:
        prefix = f"{path}:{card_id}"
        if card_id in seen:
            errors.append(f"{prefix}: duplicate card id in file")
        seen.add(card_id)
        errors.extend(
            check_chapter_field(path, card_id, body, chapter_start, chapter_end)
        )

        if max_card_span is not None:
            chapter_match = CHAPTER_RE.search(body)
            if chapter_match:
                cited = parse_chapter_numbers(chapter_match.group(1))
                if len(cited) > max_card_span:
                    errors.append(
                        f"{prefix}: card cites {len(cited)} distinct chapters "
                        f"(> {max_card_span}); likely a chapter-summary, not one event"
                    )

        required = {**COMMON_REQUIRED, **(B_REQUIRED if is_management else A_REQUIRED)}
        for label, pattern in required.items():
            if not pattern.search(body):
                errors.append(f"{prefix}: missing or empty required field {label}")

        result = RESULT_RE.search(body)
        if result:
            state = result.group(1).split("（", 1)[0].strip()
            if state not in ALLOWED_RESULTS:
                errors.append(f"{prefix}: invalid result state {state!r}")

        expectation_lines = "\n".join(
            line
            for line in body.splitlines()
            if "⑦" in line
            and not re.search(r"不(?:应)?标.*⑦|⑦.*不(?:应)?标|无.*⑦|⑦.*无", line)
        )
        if expectation_lines and not re.search(
            r"⑦〔(?:主导|在场)〕", expectation_lines
        ):
            warnings.append(f"{prefix}: ⑦ used without 主导/在场")

        # 引文（关键原句）：只取，不校验逐字、不校验长度。允许转述/截断/标点。
        # 它负责表意，给人看；"是否编造"由下面的定位锚负责。
        quote_match = QUOTE_RE.search(body)
        quote = clean_quote(quote_match.group(1)) if quote_match else ""

        # 定位锚：唯一的防编造手段。grep 不到 → 进复查清单（REVIEW），不拦、不算
        # error、不触发重跑。宁可多标（假阳性人工三秒划掉），不可漏标。
        anchor_match = ANCHOR_RE.search(body)
        if not anchor_match:
            # 没写锚：回退用引文当锚去定位（兼容尚未产出锚字段的旧卡）。
            anchor = quote
            anchor_label = "（无定位锚，回退用关键原句定位）"
        else:
            anchor = clean_quote(anchor_match.group(1))
            anchor_label = ""

        if not anchor:
            # 锚和引文都空：无法核实是否编造，标记交人，但不拦。
            review.append(f"{prefix}: 无定位锚也无关键原句，无法核实是否编造，请人工看")
            continue

        if evidence_source is not None and anchor not in evidence_source:
            review.append(
                f"{prefix}: 疑似编造——定位锚未在本块原文中找到: {anchor!r}{anchor_label}"
            )

    return ArtifactResult(errors, warnings, review, empty_quotes, tuple(seen))


def validate_events(
    path: Path,
    chapter_start: int,
    chapter_end: int,
) -> tuple[list[str], int]:
    text = path.read_text(encoding="utf-8")
    errors = find_placeholders(path, text)
    events = split_blocks(text, EVENT_RE)
    if not events:
        errors.append(f"{path}: no event entries found")
        return errors, 0
    seen: set[str] = set()
    for event_id, body, _ in events:
        prefix = f"{path}:{event_id}"
        if event_id in seen:
            errors.append(f"{prefix}: duplicate event id")
        seen.add(event_id)
        errors.extend(
            check_chapter_field(path, event_id, body, chapter_start, chapter_end)
        )
        for label, pattern in EVENT_REQUIRED.items():
            if not pattern.search(body):
                errors.append(f"{prefix}: missing or empty required field {label}")
        result = RESULT_RE.search(body)
        if result:
            state = result.group(1).split("（", 1)[0].strip()
            if state not in ALLOWED_RESULTS:
                errors.append(f"{prefix}: invalid result state {state!r}")
    return errors, len(events)


def coverage_chapters(text: str) -> set[int]:
    covered: set[int] = set()
    in_coverage = False
    for raw_line in text.splitlines():
        line = raw_line.replace("*", "")  # 容忍 markdown 加粗
        if "逐章覆盖表" in line:
            in_coverage = True
            continue
        if in_coverage and line.startswith("## ") and "逐章覆盖表" not in line:
            break
        if not in_coverage:
            continue
        # 区段内任意带章号的表格行/列表项都算已覆盖，不管第二列写的是
        # 事件ID、"无独立主要事件" 还是 "—"。表头/分隔行无章号，自然不计。
        table_match = re.match(
            r"^\s*\|\s*第?\s*([0-9零〇一二两三四五六七八九十百千万]+)\s*章?\s*\|",
            line,
        )
        bullet_match = re.match(
            r"^\s*-\s*第?\s*([0-9零〇一二两三四五六七八九十百千万]+)\s*章",
            line,
        )
        match = table_match or bullet_match
        if match:
            covered.add(chinese_number_to_int(match.group(1)))
    return covered


def validate_production(
    event_paths: list[Path],
    selfcheck_paths: list[Path],
    chapter_start: int,
    chapter_end: int,
    min_selfcheck_lines: int,
    previous_event_count: int | None,
    min_event_ratio: float,
    min_events_per_chapter: float | None = None,
) -> tuple[list[str], int]:
    errors: list[str] = []
    if len(event_paths) != 1 or len(selfcheck_paths) != 1:
        return (
            ["production validation requires exactly one events file and one selfcheck file"],
            0,
        )

    event_path = event_paths[0]
    selfcheck_path = selfcheck_paths[0]
    event_text = event_path.read_text(encoding="utf-8")
    selfcheck_text = selfcheck_path.read_text(encoding="utf-8")
    errors.extend(find_placeholders(event_path, event_text))
    errors.extend(find_placeholders(selfcheck_path, selfcheck_text))
    event_errors, event_count = validate_events(
        event_path, chapter_start, chapter_end
    )
    errors.extend(event_errors)

    covered = coverage_chapters(event_text + "\n" + selfcheck_text)
    expected = set(range(chapter_start, chapter_end + 1))
    missing = sorted(expected - covered)
    outside = sorted(ch for ch in covered if ch not in expected)
    if missing:
        errors.append(f"chapter coverage missing: {missing}")
    if outside:
        errors.append(f"chapter coverage outside assigned range: {outside}")

    nonempty_lines = [line for line in selfcheck_text.splitlines() if line.strip()]
    if len(nonempty_lines) < min_selfcheck_lines:
        errors.append(
            f"{selfcheck_path}: selfcheck too short "
            f"({len(nonempty_lines)} nonempty lines; minimum {min_selfcheck_lines})"
        )
    if not re.search(
        r"实际读取(?:的)?最后一章[：:\s]*(?:第\s*)?"
        + str(chapter_end)
        + r"\s*(?:章)?",
        selfcheck_text.replace("*", ""),  # 容忍 markdown 加粗
    ):
        errors.append(
            f"{selfcheck_path}: selfcheck must state actual last chapter as {chapter_end}"
        )

    if previous_event_count is not None and previous_event_count > 0:
        ratio = event_count / previous_event_count
        if ratio < min_event_ratio:
            errors.append(
                f"event-density stop threshold triggered: {event_count}/"
                f"{previous_event_count}={ratio:.2f} < {min_event_ratio:.2f}"
            )

    if min_events_per_chapter is not None:
        n_chapters = chapter_end - chapter_start + 1
        floor = min_events_per_chapter * n_chapters
        if event_count < floor:
            errors.append(
                f"event density too low: {event_count} events for {n_chapters} "
                f"chapters (< {min_events_per_chapter}/chapter = {floor:.0f}); "
                f"likely skimmed/decayed, re-run this block"
            )
    return errors, event_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cards", nargs="+", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument(
        "--evidence-source",
        type=Path,
        help="Pre-sliced source for the assigned chunk; bypasses chapter-heading extraction",
    )
    parser.add_argument("--report", type=Path)
    parser.add_argument("--events", nargs="*", type=Path, default=[])
    parser.add_argument("--selfcheck", nargs="*", type=Path, default=[])
    parser.add_argument("--chapter-start", type=int)
    parser.add_argument("--chapter-end", type=int)
    parser.add_argument("--production", action="store_true")
    parser.add_argument("--min-selfcheck-lines", type=int, default=10)
    parser.add_argument("--max-empty-quotes", type=int, default=2)
    parser.add_argument("--previous-event-count", type=int)
    parser.add_argument("--min-event-ratio", type=float, default=0.5)
    parser.add_argument(
        "--min-events-per-chapter",
        type=float,
        help="Production depth gate: minimum events / assigned chapter (e.g. 0.5). "
        "A block well below this was skimmed, not read.",
    )
    parser.add_argument(
        "--max-card-span",
        type=int,
        help="Depth gate: max distinct chapters one card may cite before it is "
        "flagged as a chapter-summary rather than a single event (e.g. 4).",
    )
    args = parser.parse_args()

    if (args.chapter_start is None) != (args.chapter_end is None):
        parser.error("--chapter-start and --chapter-end must be supplied together")
    if args.production and (args.chapter_start is None or args.chapter_end is None):
        parser.error("--production requires --chapter-start and --chapter-end")

    if args.source and args.evidence_source:
        parser.error("use either --source or --evidence-source, not both")
    source_text = args.source.read_text(encoding="utf-8") if args.source else None
    evidence_source = (
        args.evidence_source.read_text(encoding="utf-8")
        if args.evidence_source
        else source_text
    )
    if source_text is not None and args.chapter_start is not None:
        try:
            evidence_source = source_slice(
                source_text, args.chapter_start, args.chapter_end
            )
        except ValueError as exc:
            parser.error(str(exc))

    errors: list[str] = []
    warnings: list[str] = []
    review: list[str] = []
    all_ids: dict[str, Path] = {}
    for path in args.cards:
        result = validate_cards(
            path, evidence_source, args.chapter_start, args.chapter_end,
            args.max_card_span,
        )
        errors.extend(result.errors)
        warnings.extend(result.warnings)
        review.extend(result.review)
        for card_id in result.card_ids:
            if card_id in all_ids:
                errors.append(
                    f"duplicate card id across files: {card_id} "
                    f"({all_ids[card_id]} and {path})"
                )
            all_ids[card_id] = path

    if args.production:
        production_errors, _ = validate_production(
            args.events,
            args.selfcheck,
            args.chapter_start,
            args.chapter_end,
            args.min_selfcheck_lines,
            args.previous_event_count,
            args.min_event_ratio,
            args.min_events_per_chapter,
        )
        # 生产校验里两类东西混在一起：①真·解析失败（字段缺失、文件数不对、
        # 无法识别）—— 下游脚本会崩，保留为 error 硬拦；②判断/深度类信号
        # （章节覆盖缺、self-check 过短、事件密度低、停机阈值）—— 按"全交给我、
        # 只标记不自动判断"的约定，降为 REVIEW 复查清单，绝不拦、绝不触发重跑。
        review_markers = (
            "coverage", "selfcheck", "event-density", "event density",
            "stop threshold", "skimmed", "decayed", "actual last chapter",
        )
        for item in production_errors:
            if any(marker in item for marker in review_markers):
                review.append(item)
            else:
                errors.append(item)
        # empty-quote 停机阈值整条退场：引文已非必填、可转述，空引文不再是错。

    lines = [
        f"ERRORS: {len(errors)}",
        f"WARNINGS: {len(warnings)}",
        f"REVIEW: {len(review)}",
    ]
    lines += [f"ERROR {item}" for item in errors]
    lines += [f"WARN {item}" for item in warnings]
    lines += [f"REVIEW {item}" for item in review]
    report = "\n".join(lines) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
