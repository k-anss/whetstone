# read-not-decorate

**Documents should be read, not decorated.**

A skill that turns a finished long-form markdown document into one self-contained
HTML file built for reading or keeping. It assembles your text under a strict
visual system and calls a layout component only where your text already has that
structure. It never rewrites your words, adds arguments, or adds decoration.

It is built for the document that is meant to be *read*: a report, an essay, an
archived article, a research write-up. Not slides, not a dashboard, not a
landing page.

## Demo

`examples/demo.html` is a document built with this skill, about this skill. Open
it in any browser — offline, no build step — to see the target output.

## Install

Three paths, pick one:

- **Claude Code plugin** — clone into your skills directory and the agent loads
  it on match.
- **Manual** — `git clone` this repo; point your agent at the folder.
- **Any agent** — paste this repository's link into the chat and ask the agent
  to use it. The structure is agent-neutral.

## How it is laid out

`SKILL.md` is the map, not the whole text. It tells the agent which reference
file to load when:

| Working on | Loads |
|---|---|
| Type, color, spacing, page skeleton | `reference/visual-system.md` |
| Which component a passage needs | `reference/components.md` |
| Archival vs distribution mode | `reference/modes.md` |
| Text the agent itself writes | `reference/copy-restraint.md` |

Read the map first; pull a reference file only when you reach that part of the
job. Every file has a Chinese twin (`*.zh.md`) with identical rules — the skill
is fully bilingual.

## Philosophy

1. The assembler does not rewrite. The words are the author's; layout is the
   only job.
2. A component is called when its structure appears, never to fill space.
3. One accent color. Everything else earns attention through whitespace, not
   color.
4. Archival and distribution are opposite readers. Choose one before assembling.
5. Delete every adjective the sentence survives without.

Disagreeing with rule 1 or 3 is expected — this skill is a stance, not a
consensus.

## License

MIT. See `LICENSE`.

中文说明见 [`README.zh.md`](README.zh.md)。
