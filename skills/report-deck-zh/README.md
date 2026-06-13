# report-deck-zh

Chinese work briefings have a structural grammar — parallel titles,
whole-part-whole, data-caption pages — that English slide tools don't speak.
This encodes it.

This is a skill: a discipline file an agent loads to lay out formal Chinese
work-briefing slides (述职 / 总结 / 立项 / 复盘) following the conventions
of formal Chinese reporting, instead of English pitch-deck aesthetics or
the homogenized output of mass AI-PPT tools.

It produces **structure, not content**. It builds the skeleton — how titles
parallel, how sections progress, how a data page carries its caliber — and
never writes the briefing's actual content.

## Lineage

Derived from / inspired by **frontend-slides** (Zara). frontend-slides
builds beautiful HTML slides with English deck aesthetics. It does not know
the structural grammar of formal Chinese reporting: parallel (对仗) titles,
whole-part-whole (总分总) closure, data pages with caliber captions
(口径说明), hierarchical progression by Chinese official-document logic.

The difference, in one line: frontend-slides makes English decks look good;
this makes Chinese briefings read as native formal reporting. See
`examples/lineage-test.md` for a recorded test of frontend-slides on a
Chinese briefing — where its structure goes wrong, and how this skill
corrects it.

## What it does

- **Parallel titles** — aligned character count, symmetric structure,
  consistent verb-object form.
- **Whole-part-whole skeleton** — opening states the whole, body parts it,
  closing restates it with the delta.
- **Data-caliber pages** — every figure carries source, scope, and time
  caliber; "unknown" and "not applicable" stay distinct.
- **Restrained visuals** — reuses read-not-decorate tokens; no emoji, no
  gradients, no decorative beautification.

## When NOT to use

- English pitch decks → use frontend-slides.
- Casual or social-sharing slides → forced parallelism reads stiff.
- Generating the report's actual content → this builds the skeleton only.

## Install

Place this folder under `skills/` in a skills-aware agent setup. The agent
loads `SKILL.md`; `reference/` files load on demand.

## License

MIT. Author: K (@k-anss). Part of the `whetstone` collection.
