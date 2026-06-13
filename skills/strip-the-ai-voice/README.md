# strip-the-ai-voice

AI Chinese reads wrong because of what it adds. Don't rewrite it — delete it.

A skill that removes the "AI voice" from Chinese text by deletion: honorifics (您/请), filler particles (哦/呢), adjective/adverb padding, self-explanation, and reader-conclusions. The criterion is a concrete delete-test, not taste. It only touches AI-generated copy — never the user's own prose.

## Lineage

**Derived from / inspired by: humanizer-zh. Direction reversed: delete, not add.**

The adaptation, in four questions:

1. **Where does the original fail?** humanizer-zh "humanizes" — it rewrites whole passages to sound more human. The rewrite is uncontrolled and unrepeatable, and its direction is *addition*: it may add colloquialisms, warmth, emotion.
2. **Was the adapter that failing's user?** Yes. Archival and professional documents written under a strict restraint standard get their restraint *broken* by humanize-style tools — honorifics and adjectives come back.
3. **What is the fix?** Replace rewrite-style humanizing with delete-only restraint: a fixed list of what to delete, one binary criterion (the delete-test), and a forbidden list. Repeatable, checkable sentence by sentence, single direction: subtraction.
4. **For whom is this a reason to switch?** People writing professional, formal, or archival Chinese — reports, documentation, instructions — who want the skeleton exposed, not warmth added. humanizer-zh serves "make AI text read like a person online"; this serves "make AI text read like a document". Opposite directions; pick by destination.

Empirical test record: `examples/lineage-test.md` (template, pending first real run — no fabricated results).

## When to use

- "去掉 AI 味" / "这段中文太 AI 了" / "改克制点"
- Making AI-generated Chinese copy read like a professional or archival document

## When NOT to use

- Making text more casual, warm, or 网感 — that is addition; use a humanizer
- Translating, or editing English
- Marketing or emotional copy, where deletion makes it worse
- The user's own prose — out of scope by rule

## Contents

- `SKILL.md` / `SKILL.zh.md` — positions, map, fields
- `reference/` — delete list, the test, forbidden items, ✗→✓ table
- `examples/` — full worked deletion, lineage test record

## License

MIT. Author: K.
