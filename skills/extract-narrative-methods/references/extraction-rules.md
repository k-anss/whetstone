# Extraction Rules (Producer-Facing)

The hard rules that go into the producer prompt. These are generic; the project
holds the source-specific versioned copy (e.g. `meta/约束规则_vN.md`). Keep this
list short — it is the prompt's load-bearing core, not the audit checklist. Push
anything machine-checkable into the validator and anything subtle into a
regression sample instead of growing this list.

## Production completeness

1. Every chunk produces **event audit + A/B cards + self-check**.
2. The event audit ends with a chapter-by-chapter coverage table: each assigned
   chapter maps to event IDs or `no independent major event` + a one-line
   transition.
3. Never substitute placeholder prose, title scans, or framework drafts for
   reading the source.
4. If any output contains 待补 / 占位 / 高速概览 / 批量初稿 / 标题扫描 (or
   equivalents), the chunk is not complete.
5. If the chapter range is not fully read, do not create the next chunk's files.
6. The self-check must state the actual last chapter read.

## Card entry

7. An A/B card must answer **actor · dilemma · action · counterpart response ·
   cost · result**. No closed loop → downgrade to an event.
8. "Putting several matters in one frame", "handling together", "repositioning"
   is not a method. Name one main dilemma, one key decision, and the
   counterpart's or organization's observable response.
9. A principle, goal, job-title authority, or literary reflection cannot be a
   card on its own. It needs a concrete execution mechanism.
10. A card spanning multiple events must prove they are controlled by one
    decision; otherwise split or downgrade to event material.
11. A limited-goal action must state its success condition and stop condition.
    "Boosted morale" / "created influence" alone does not prove a method.

## Evidence discipline

12. Result state must match source evidence strength; do not upgrade early.
    Silence, surprise, fear, or a pause is not durable change.
13. Quotes may be left empty, never fabricated. The key-quote field itself must
    always be present (fixed marker, e.g. `▸ 关键原句：`), even when empty.
14. A quote must be a verbatim continuous source string. A short excerpt is fine;
    a rewritten paraphrase is not.
15. Source re-extraction rebuilds from events and evidence. The old card's
    title, route, and count are not inherited — it may yield 0, 1, or several
    new cards.
16. Mechanical correctness is not semantic acceptance. After scripts pass, a
    medium-reasoning audit still runs.

## Frequency integrity

17. One event's A and B cards count as a single independent evidence node in
    cross-context method validation. Do not inflate frequency by re-labeling or
    re-routing the same event.

## Stop thresholds

Halt at the last complete chunk if any trigger fires: self-check under ~10 lines;
missing coverage table; an overview/scan/draft phrase appears; more than ~2 cards
missing a quote where it affects the main judgment; event density drops below the
previous chunk without human confirmation.

Treat these as project defaults, not universal constants. Calibrate chunk size,
quote tolerance, and density ratio on one representative difficult chunk.

## Repair priority

Fix in this order: (1) boundaries and coverage; (2) evidence and quotes;
(3) A/B misrouting and duplicate splitting; (4) wording and formatting last.
