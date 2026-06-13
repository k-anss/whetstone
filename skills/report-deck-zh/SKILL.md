---
name: report-deck-zh
description: >
  Build Chinese work-briefing slides that follow the structural grammar of
  formal Chinese reporting — parallel (对仗) titles, whole-part-whole (总分总)
  structure, data pages with caliber/source captions (口径说明), and
  hierarchical progression — instead of English pitch-deck aesthetics or
  generic AI-PPT templates. Trigger when the user says "做一份汇报/述职/总结
  slides", "中文工作汇报 deck", "把这个做成汇报 PPT(中文正式)", "立项汇报
  版式", "复盘汇报排版", or "Chinese briefing slides / formal Chinese report
  deck". Produces structure, not content. Do NOT trigger for: English pitch
  decks (use frontend-slides), casual or social-sharing slides, generating
  the report's actual content or copy (this builds the structural skeleton
  only), or generic "make this prettier" requests with no formal-briefing
  context.
---

# report-deck-zh — Chinese briefing slides have a grammar; speak it

Chinese work briefings have a structural grammar — parallel titles,
whole-part-whole, data-caption pages — that English slide tools don't speak.
This skill encodes it.

## Lineage (adaptation-line skill — read before judging this redundant)

Derived from / inspired by **frontend-slides** (Zara). Four questions:

1. **Where does the original fail?** frontend-slides builds HTML slides with
   English deck aesthetics. It does not know the conventions of formal
   Chinese reporting: titles must be parallel (对仗), the document must close
   the loop (总分总), data pages must carry caliber captions, hierarchy
   follows Chinese official-document progression, not free-form bullets.
2. **Was the author a failed user of the original?** Yes. The author has
   produced formal Chinese work briefings at volume; decks laid out with
   English-aesthetic tools read as structurally wrong in that setting —
   recognizably "not a formal document" before anyone reads a word.
3. **What is the patch?** Replace the English aesthetic templates with a
   Chinese-briefing structural grammar library: parallel-title generation
   rules, whole-part-whole skeleton, data-caliber page pattern, hierarchical
   progression rules. Visual tokens reuse the restraint system from
   read-not-decorate.
4. **For whom is this a reason to switch?** Anyone producing formal Chinese
   work briefings (述职 / 总结 / 立项 / 复盘) who needs structure that reads
   as native formal reporting, not an English pitch deck.

## Stance (three load-bearing claims)

1. **Formal Chinese reporting has its own structural grammar; English slide
   tools don't speak it.** Mechanism: parallel titles, whole-part-whole, and
   caliber pages are conventions of the genre — apply English deck logic and
   the structure itself is wrong, regardless of polish. Field observation: a
   Chinese briefing laid out by an English-aesthetic tool shows non-parallel
   titles and no data-caliber page; experienced readers flag it as "not a
   formal document" at a glance. Boundary: verified on formal work
   briefings; untested on academic or government-publication formats.
2. **Structure only, never content.** Mechanism: the skeleton generalizes;
   the content is case-specific, and generating it both exceeds this skill's
   warrant and risks leaking real-world specifics. Field observation: the
   author's own production rules repeatedly draw this exact line. If input
   is insufficient to infer structure, stop and ask the briefing type — do
   not invent content to fill a skeleton.
3. **Restrained visuals; reuse read-not-decorate tokens.** Mechanism: a
   briefing must read professional, not decorated; the homogenized
   card-beautification of mass AI-PPT tools is precisely the failure mode.
   Field observation: homogenized beautification makes every briefing look
   identical; a restrained structural layout reads as more professional, not
   less. Boundary: this is a claim about formal briefings; light or playful
   decks legitimately want different visuals — out of scope here.

## Core actions (do X → load Y)

| Task | Load |
|---|---|
| Decide the deck skeleton (briefing type, sections, closing loop) | `reference/structure.md` |
| Generate or repair parallel titles | `reference/titles.md` |
| Lay out data pages with caliber captions | `reference/data-pages.md` |
| Apply visual tokens | `reference/visual.md` |
| See a complete worked example | `examples/demo.html` |

**Workflow gate (mandatory):** before laying out any slides, report to the
user (a) the briefing type you identified (述职 / 总结 / 立项 / 复盘 / other)
and (b) the proposed section skeleton. Wait for confirmation. Layout without
a confirmed skeleton is the most common failure.

**Hard rules:**

- Every title group at the same level must be parallel: aligned character
  count, symmetric grammatical structure, consistent verb-object form
  (`reference/titles.md`).
- Every page presenting figures carries a caliber caption: data source,
  statistical scope, time caliber (`reference/data-pages.md`). No caption,
  no data page.
- The deck closes the loop: opening states the whole, body parts it,
  closing restates the whole with the delta (`reference/structure.md`).
- No emoji, no gradients, no decorative icons, no stock imagery
  (`reference/visual.md`).
- Examples and placeholders are fictional generic-business scenarios only.

## Six fields

- **Version**: 0.1 (2026-06). Changelog: initial release. Corrections will
  be marked in place, not deleted (reverse-marking policy).
- **Retirement condition**: when a bare model, unprompted, reliably produces
  parallel titles, whole-part-whole structure, and caliber captions for
  Chinese briefings, this skill retires.
- **Failure behavior**: if the input does not determine the briefing type or
  skeleton, stop and ask. Do not silently force a skeleton onto unclear
  input; do not generate content to compensate.
- **Composition**: composes-with read-not-decorate (shared visual tokens).
  Division of labor with frontend-slides: English decks → that skill;
  formal Chinese briefings → this one. Explicit user instructions override
  this skill.
- **Time**: judgments dated 2026-06. Chinese briefing conventions are
  stable; the AI-PPT tool ecosystem is not. Review in ~18 months.
- **Boundary**: verified on formal Chinese work-briefing layout. Not for
  English pitch decks, not for light/social slides, does not generate
  briefing content. Untested beyond these — treat as unverified there.
