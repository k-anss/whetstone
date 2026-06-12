---
name: read-not-decorate
description: >-
  Use when someone hands you a finished long-form markdown document (a report,
  an essay, an archived article, a research write-up) and wants it turned into a
  single self-contained HTML file meant to be read or kept — not a slide deck,
  not a marketing page, not a redesign. Trigger on requests like "typeset this
  report as HTML", "make a clean reading page from this markdown", "archive this
  article as a standalone HTML I can keep", or "turn this write-up into a page I
  can send to a client". The skill assembles; it does not rewrite the author's
  words, add arguments, or add decoration.
license: MIT
---

# Anti-Decoration Documents

Turn a finished long-form markdown document into one self-contained HTML file
that gets read, not decorated.

## What this is, in one line

You are an **assembler**, not a writer. The author's text is fixed: you never
rewrite a sentence, never "improve" phrasing, never add a point. You choose a
reading mode, lay the text out under a strict visual system, and call a
component only where the text already has that structure. Everything that
fights reading — color, shadow, stock imagery, engagement furniture — is removed
on purpose.

## Decide the mode first (this changes everything downstream)

Before laying out anything, pick one. They serve opposite readers and the
choice decides which components survive.

- **Archival** — the reader is the author, months from now. Keep the reasoning,
  the basis for each judgment, the uncertainty that was true at the time.
  Optimized for re-scanning, not for flow.
- **Distribution** — the reader is a client or stranger with none of the
  author's context. Keep clean, independently-standing conclusions and credible
  reasons. Strip internal revision history and confidence markers.

If the request doesn't say, default to **archival** and state that you did.

## The map (load on demand, do not read all of this up front)

This file is the index. Pull the right reference file when you hit that part of
the job — not before.

| When you are… | Load |
|---|---|
| Setting type, color, spacing, the page skeleton | `reference/visual-system.md` |
| Deciding which structural component a passage needs | `reference/components.md` |
| Choosing archival vs distribution, and what each drops | `reference/modes.md` |
| Writing any text *you* generate (labels, nav, summaries) | `reference/copy-restraint.md` |

A worked output lives at `examples/demo.html` — it is a document built with this
skill, about this skill. Open it to see the target.

Every file here has a Chinese twin (`*.zh.md`, `demo.zh.html`) with identical
rules. Work in whichever language the source document is in.

## Workflow

1. Read the whole document first. All of it.
2. Output a short confirmation (no half-finished HTML): the chosen **mode**, the
   **skeleton** (H1 + every H2, numbered), and the **component trigger points**
   (which passage maps to which component, one line each). If a structured
   passage fits no listed component, list it as a *candidate component* and ask
   — do not force it into the nearest one and do not flatten it into a plain
   paragraph.
3. Wait for the go-ahead or adjustments.
4. Produce the complete single `.html` file.
5. Report in ≤5 lines: file path, section count, components used, file size.

## Hard rules (these are the product)

1. **Assemble, never author.** Not one of the author's words changes.
2. **Components are called by structure, not to fill space.** No structure, no
   component — a plain paragraph is the correct default. Bias to fewer.
3. **One accent color.** Everything else earns attention through whitespace and
   type weight, never through a second color.
4. **Self-contained.** Inline all CSS/JS, system-font stack only, no network, no
   framework, no CDN. Double-clicking the file must work offline forever.
5. **Delete every adjective the sentence survives without.** Applies only to
   text *you* write (nav, labels, summaries) — never to the author's body text.
6. **No engagement furniture.** No share/like buttons, no reading-time estimate,
   no "if you found this useful" closers, no emoji, no stock images, no
   AI-generated illustration (any inline SVG you draw is thin and linear).

## What this skill is not for

Short notes, unfinished fragments, raw chat logs, slide decks, dashboards, or
anything that needs a redesign of the content rather than a layout of it. If the
input isn't a finished long-form document, say so and stop — don't HTML it for
the sake of it.
