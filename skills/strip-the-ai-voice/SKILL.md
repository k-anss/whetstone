---
name: strip-the-ai-voice
description: >
  Strip the "AI voice" from Chinese text by deletion, not rewriting.
  Removes honorifics (您/请), filler particles (哦/呢), adjective/adverb
  padding, self-explanation, and reader-conclusions — using a concrete
  delete-test, not a vague "make it natural". Trigger when the user says
  "去掉 AI 味", "这段中文太 AI 了 / 帮我改克制点", "strip the AI tone
  from this Chinese", or "make this Chinese read like a professional /
  archival document". Direction is subtraction, not addition. Do NOT
  trigger for: making text MORE casual or human/网感 (that is the
  opposite, addition — use a humanizer), translating, or editing English.
  Operates only on AI-generated copy; never alters the user's own source
  prose.
license: MIT
---

# strip-the-ai-voice

AI Chinese reads wrong because of what it adds. Don't rewrite it — delete it.

## Three load-bearing positions

### 1. The AI voice is added, so the fix is deletion, not revision

- **Rule**: Never paraphrase a sentence to make it "sound natural". Remove the added material; keep what remains.
- **Mechanism**: Rewrite-style humanizing is unrepeatable — each pass can introduce new decoration, and the same input gives different outputs. Deletion is single-direction and checkable sentence by sentence: either a word was removed or it wasn't.
- **Field observation**: Archival documents written under a strict restraint standard, when run through "polish the wording" tools, regress — honorifics and adjectives come back. Only delete-only rules held the restraint across repeated edits.
- **Boundary**: If the text is missing information (not over-decorated), deletion cannot fix it. Report the gap; do not write new content to fill it.

### 2. The criterion is the delete-test, not taste

- **Rule**: Delete every adjective and adverb in the sentence. If the remainder stands, use the remainder. If the remainder is a stump, the whole sentence was decoration — delete the sentence.
- **Mechanism**: This turns the subjective question "is this restrained enough" into a binary, repeatable check. Two runs on the same text converge to the same output.
- **Field observation**: "读者将会深刻地感受到机制的精妙之处" → after deletion: "读者会感受到机制" → a stump → delete the whole sentence. The sentence carried no information; the test exposed it.
- **Boundary**: The test judges decoration, not correctness. A restrained sentence can still be wrong; that is outside this skill.

### 3. Touch only AI-generated copy. Never the user's prose

- **Rule**: This skill operates on copy the tool itself produced — labels, prompts, captions, sign-offs, boilerplate. The user's own writing is not edited, not even one character.
- **Mechanism**: Restraint is a discipline for what the tool says, not a license to override the author. Editing the author's prose is a different act with different stakes — and a deletion there is irreversible.
- **Field observation**: This line recurs in the source protocols this skill was distilled from: "只管你自己生成的文案,正文一个字不动". The skills that held that line stayed usable; mixing the two scopes is where trust breaks.
- **Boundary**: If the user explicitly hands over their own prose and asks for this treatment, the scope changes by their instruction — state the new scope back before deleting.

## Map

| Task | Load |
|---|---|
| What to delete (four classes, word lists) | `reference/delete-list.md` |
| The delete-test; delete-word vs delete-sentence line | `reference/the-test.md` |
| Hard forbidden items; symbol rule (structural stays, emotional goes) | `reference/forbidden.md` |
| ✗→✓ before/after table | `reference/examples-table.md` |
| Full worked example | `examples/before-after.md` |
| Adaptation lineage and test record (vs humanizer-zh) | `examples/lineage-test.md` |

## Workflow gate

Before deleting anything, state in one line: which spans are AI-generated copy to be processed, and where the user's own prose begins. If that boundary cannot be drawn, stop (see Failure behavior).

## Fields

- **Version**: 0.1 (2026-06). Changelog: corrections are marked in place, not erased.
- **Sunset condition**: Retire when base models stop emitting honorific- and decoration-laden Chinese by default, and "去 AI 味" stops recurring as a request.
- **Failure behavior**: Cannot tell AI copy from user prose → stop and ask. Never delete text that might be the user's original (irreversible). No silent best-effort output.
- **Composition**: composes-with any Chinese writing skill. conflicts-with: humanizer-zh — opposite direction (it adds human texture; this deletes decoration). Do not apply both to the same text. Explicit user instruction overrides this skill.
- **Time**: Judgment fixed 2026-06. The default "AI flavor" shifts with model generations; review in 12–18 months.
- **Boundary conditions**: Validated on professional, formal, and archival Chinese copy. Not for marketing copy, emotional writing, or any text where spoken warmth is the point — there, deletion makes it worse, and this skill should stay silent.
