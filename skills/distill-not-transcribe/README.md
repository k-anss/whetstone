# distill-not-transcribe

Turn a written method into a skill that carries its author's judgment —
or refuse, when the material has steps but no decisions.

**Status: v0.1 pre-release.** Before/after evidence pending first real
run; this skill is currently being tested by rebuilding an existing
skill from its source protocol and diffing the result
(see `examples/recursive-acceptance.md`). Claims will follow evidence,
not precede it.

## The position

Most of the 20,000+ skills in public directories transcribe steps.
Agents do not need more steps — they need the decisions an author made
that a bare model would not make: when X, choose A over B, because ___.
This skill builds only that kind, and refuses the rest. If you want a
skill made from material that contains no judgment, this is the wrong
tool, on purpose.

## What it does

- **Distill line:** your protocol / SOP / workflow doc → a skill, via
  seven transformations and a thickening pass (rule + why + witnessed
  observation + validated boundary).
- **Fork line:** an existing popular skill → your adaptation, gated by
  four questions that separate a judgment increment from a
  transcription, shipped with a real test trace.
- Every output carries six mandatory fields, including its own
  deprecation condition and failure behavior.

## Install

- Claude Code: add this repository as a marketplace, or copy
  `distill-not-transcribe/` into your skills directory.
- Any other agent: send it this repository link and ask it to follow
  SKILL.md.

## Lineage

- composes-with: the official skill-creator (its eval tooling and
  packaging; this skill governs judgment screening and trust
  structure).
- Part of the whetstone collection. License: MIT. Author: K.

中文说明见 README.zh.md。
