# missing-not-zero

**Missing data is not zero.**

A skill that turns a field-spec table into one self-contained HTML
data-collection tool — opened in a browser, filled repeatedly on site,
exported as structured text. Its reason to exist is one discipline most form
generators skip: every collection item must end in one of **three** states —
*recorded*, *nothing happened*, or *not checked* — because once "no event" and
"nobody looked" share a button, downstream analysis can never tell them apart
again.

## The ten-second check (what this skill forces that a default build doesn't)

1. **Two no-data buttons per item**, never one "N/A" — with two distinct
   export formats.
2. **Stops on cross-module ambiguity.** If one real-world event could be filed
   under two modules, the agent reports it before building, instead of
   shipping a silently mis-countable schema.
3. **Refuses coherent analysis.** An argument chain forced into form cells
   exports as unrelated fragments; the agent routes it to a reading-page skill
   instead.
4. **Parse-ready export**: `===` separators *including a trailing one*, no
   commentary mixed into the data.
5. **Spec is law**: no invented fields, no expanded options, contradictions
   reported instead of silently resolved.

Each of these is backed in the skill body by mechanism and a field
observation — not taste.

## Demo

`examples/field-spec.md` is a real input spec; `examples/demo.html` is the
tool this skill assembles from it. Self-referential on purpose: it is a tool
for logging skill field-tests — built by this skill, usable for testing skills
like it. Open it in any browser, offline, no build step.

## Install

- **Claude Code plugin** — clone into your skills directory; the agent loads
  it on match.
- **Manual** — `git clone` this repo; point your agent at this folder.
- **Any agent** — paste this folder's link into the chat and ask the agent to
  use it. The structure is agent-neutral.

## How it is laid out

`SKILL.md` is the map; references load on demand:

| Working on | Loads |
|---|---|
| Skeleton, the three buttons, validation, undo | `reference/interaction.md` |
| Spec markers → inputs; conditional fields; the ambiguity gate | `reference/field-mapping.md` |
| Export records, the two empty formats, storage | `reference/output-format.md` |
| Colors, type, and any text the agent itself writes | `reference/look-and-copy.md` |

Every file has a Chinese twin (`*.zh.md`, `demo.zh.html`). The Chinese layer
carries a Chinese-specific copy-stripping pass the English layer doesn't
duplicate.

## Run your own before/after

In a clean session, hand `examples/field-spec.md` to a bare agent and ask for
a single-file collection tool. Then do the same with this skill attached.
Diff the two against the ten-second check above. If you can't see the
difference, tell me — that is this skill's deprecation condition at work.

Queries that should **not** trigger this skill (false-trigger set):

1. "Typeset this markdown report as a reading page" → `read-not-decorate`
2. "Write my quarterly analysis report"
3. "Build a sign-up system with user accounts"
4. "Send a one-shot satisfaction survey to clients"
5. "Make a React dashboard for our metrics"
6. "Split this long argument into bullet points"
7. "Make an Excel template for the stats"
8. "Parse this exported .txt data"

## Lineage

Original work, distilled from a private field-collection protocol used in
repeated on-site data collection (v1.2 of that protocol is where the
two-state split was forced by downstream parsing needs). Not derived from any
published skill. MIT, signed K.
