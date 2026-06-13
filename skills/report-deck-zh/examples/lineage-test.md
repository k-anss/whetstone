# lineage-test.md — Adaptation test against frontend-slides

This page records testing frontend-slides on a Chinese formal briefing, to
ground the adaptation claim. The point is not that frontend-slides is bad —
it is good at what it does — but that it does not speak this genre's grammar.

## Test setup

- Input: a fictional generic-business 复盘 (retrospective) for a made-up
  e-commerce team's Q3 — the same content rendered in `demo.html`.
- Tool under test: frontend-slides, used as documented for an HTML deck.
- What we record: where the resulting structure violates Chinese
  formal-briefing conventions, then how report-deck-zh corrects it.

> Status: **template recorded; full live run pending K.** The structural
> failure points below are predicted from the genre conventions and from
> the author's prior experience with English-aesthetic tools on Chinese
> briefings. Live-run observations to be backfilled, not invented.

## Predicted structural failures (to confirm on live run)

| # | Where frontend-slides goes wrong | Convention violated | report-deck-zh correction |
|---|---|---|---|
| 1 | Section titles come out as free-form English-style phrases of mixed length | Parallel (对仗) titles | titles.md: aligned count, symmetric structure, consistent 动宾 |
| 2 | Deck opens on a detail/hero page, ends on a chart | Whole-part-whole (总分总) | structure.md: opening states whole, closing restates with delta |
| 3 | Data slides show figures with no source/scope/time line | Caliber caption (口径说明) | data-pages.md: mandatory three-slot caption |
| 4 | Body flows as a flat bullet list, 6–7 siblings | Hierarchical progression | structure.md: 2–4 parallel points under one section judgment |
| 5 | Decorated cards / accent colors / icons for visual interest | Restraint | visual.md: read-not-decorate tokens, no decoration |

## How to run (for backfill)

1. Render the `demo.html` content with frontend-slides.
2. For each row above, capture the actual output and mark confirmed /
   adjusted / not-observed. Replace predictions with observations.
3. If a predicted failure does not occur, say so — do not keep a prediction
   that the run contradicts.
