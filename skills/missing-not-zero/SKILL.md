---
name: missing-not-zero
description: >-
  Use when someone hands you a field-spec table (modules, collection items,
  fields, required rules) and wants a single-file HTML data-collection tool — a
  page a person opens in a browser, fills repeatedly on site, and exports as
  structured text for downstream parsing. Trigger on requests like "turn this
  field table into a fillable form", "make a data-collection page from my
  checklist", "build an on-site logging tool that exports text", "form tool for
  repeated daily records". Core discipline: every collection item must
  distinguish "nothing happened" from "not checked" — missing data is not zero.
  Do NOT use for: coherent analysis reports or argumentative long-form
  (splitting an argument into fields breaks it — route to a reading-page skill
  such as read-not-decorate), one-shot surveys with no repeated records, forms
  needing accounts, servers, or cloud sync, or general web-app UI work.
license: MIT
---

# Missing Is Not Zero

Turn a field-spec table into one self-contained HTML collection tool whose
every item separates "nothing happened" from "not checked".

## What you are, in one line

You are an **assembler**, not a product designer. The field-spec table is law:
you add no fields it doesn't define, swap no field types, expand no select
options. You assemble it into a disposable, offline, single-file tool that a
person fills repeatedly and exports as machine-parseable text.

## The three load-bearing judgments

**1 — Missing is not zero.** Every collection item must end a session in
exactly one of three states: *recorded*, *nothing happened*, or *not checked /
unsure*. Never collapse the last two into one "no data" button.
*Why:* downstream parsing cannot recover the difference afterwards. Missing
read as zero understates reality; zero read as missing triggers false
re-checks. The damage surfaces at analysis time, far from the entry moment
that caused it — the source protocol split these two states in its v1.2
precisely because the merged state cannot be un-merged downstream.

**2 — Disposable by design.** Each generated tool is a temporary instrument
for one running scenario. Do not abstract for reuse, do not add fields "for
later", do not pursue engineering elegance. When the spec drifts, regenerate;
don't patch.
*Field observation:* a spec was once thickened up front for future reuse; some
modules were never filled even once, others turned ambiguous as the work
changed, and the whole table was rebuilt — the early generalization was pure
cost. Schemas drift faster than abstractions pay back.

**3 — Coherent analysis does not go in here.** This tool is for atomic, small,
repeated observations. If the input is a connected analysis (an argument
chain, interdependent sections, an overall conclusion), refuse the form and
route to a reading-page skill.
*Field observation:* a complete analysis was once forced through a form like
this; the argument chain snapped at the cell boundaries and the export read as
unrelated fragments — the judgment the analysis carried was no longer
recoverable.
*Test:* can each cell stand alone? If yes (independent entries of one round),
form material. If no, it isn't.

## Workflow gates (in order, no skipping)

1. **Parse the spec.** List: tool title, modules, items per module, hidden
   items, every conditional-required dependency (field A → shows field B).
2. **Run the ambiguity gate.** Check: could one real-world event plausibly
   belong to more than one module? If yes — **stop and report it**. Propose
   merging the modules or ask for one explicit attribution rule. Do not guess
   an attribution and ship.
   *Field observation:* one kind of event touched several modules at once;
   different people filed it under different modules, per-module counts
   downstream came out wrong — and every cell looked "filled", so the error
   was silent.
3. **Report structure, then wait.** Deliver the parse as a short confirmation
   report (≤15 lines). Generate nothing until confirmed.
4. **Generate** the single .html file per the references below.
5. **Deliver short**: file path, field count, size estimate, list of
   conditional logics. No half-finished HTML in between.

## The map (load on demand, not up front)

| When you are… | Load |
|---|---|
| Building the page skeleton, buttons, validation, the three-state flow | `reference/interaction.md` |
| Translating spec markers into HTML inputs; conditional/hidden fields | `reference/field-mapping.md` |
| Writing the export records, the two empty-record formats, storage keys | `reference/output-format.md` |
| Setting colors, type, spacing, and any text *you* write (labels, errors) | `reference/look-and-copy.md` |

A worked pair lives in `examples/`: `field-spec.md` is a real input,
`demo.html` is the tool this skill builds from it — a tool for logging skill
field-tests, i.e. a tool built by this skill for testing skills like it.

Every file here has a Chinese twin (`*.zh.md`, `demo.zh.html`). Work in the
language of the source spec; the Chinese layer carries Chinese-specific copy
rules the English layer does not duplicate.

## Hard limits (inherited, not softened)

No accounts or login. No cloud sync, no external APIs, no analytics. No
external links, fonts, or CDNs — fully offline. No fields beyond the spec. No
expanded select options. No commentary inside exported text. No emoji, no
celebratory microcopy. No share buttons.

## Skill metadata

- **Version** 1.0 · 2026-06. Changelog lives at the bottom of this file;
  corrections are marked in place, never deleted.
- **Deprecation condition**: retire this skill when bare agents, handed only a
  field-spec table, reliably (a) ship two distinct no-data states per item and
  (b) stop on cross-module ambiguity instead of guessing. Separately, every
  *tool* this skill generates is disposable by design — spec drift means
  regenerate, not patch.
- **Failure behavior**: if the spec is ambiguous, contradictory, missing field
  types, or the request falls outside the verified boundary below — **stop and
  report what is missing**. Silently improvising a schema and shipping it is
  the one forbidden move.
- **Composition**: composes-with `read-not-decorate` (the analysis that
  doesn't belong here goes there). No known conflicts. If the user's explicit
  instruction contradicts a rule here, name the rule being overridden, then
  follow the user.
- **Temporal**: judgments dated 2026-06. The two-state mechanism and the
  ambiguity gate should hold for years; HTML/localStorage specifics are
  18–24-month material.
- **Verified boundary**: distilled from repeated, on-site, multi-entry daily
  collection with function/process-organized modules, deployed in Chinese.
  Untested: timeline- or object-organized module schemes, one-shot surveys,
  multi-user concurrent entry. Outside this boundary, say so before building.

## Changelog

- 1.0 (2026-06): first release. Two-state split, ambiguity gate, disposable
  stance, and the three field observations above.
