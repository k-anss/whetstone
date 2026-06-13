# reference/fork.md — the fork line

Load this when a comparable original already exists. Forking a popular
skill is legitimate and often better than building from zero: a
high-star original is pre-validated demand, and forks inherit search
gravity from the original's name. What separates a fork from a
transcription is one thing only: a judgment increment.

## The four questions

Answer all four before forking. Any unanswered question → do not fork;
that would be transcription (or translation) with no reason for anyone
to choose it over the original.

1. **Where exactly does the original fail?** Name the specific user
   and the specific action where it breaks — not "could be better for
   some people".
2. **Were you that user?** The failure must be lived, not imagined.
   "I ran it in a real project and it broke at ___."
3. **What is the patch, and which real use produced it?**
4. **For which subset of the original's users does this patch
   constitute a reason to switch?**

## Test-trace page (mandatory for every fork)

"I tested it" is an adjective with zero credit — every transcriber
writes it. The trace itself is the fingerprint. Each fork ships a
trace page in its reference/ directory:

```
## Test trace — <original name> v<version>, tested <date>
- Input: <what was actually fed, desensitized to structure level>
- Where it broke: <observed behavior, plain detail>
- Patch: <the exact change>
- Before/after: <both outputs, side by side or linked>
- Not tested: <what this trace does not cover>
```

Desensitize to the author's redline standard before publishing.
A template with no real trace behind it is one more slop template:
if no real test has happened yet, the fork is not ready.

## Lineage declaration

- `derived_from:` names the original, with link and version. MIT/CC0
  forking is legal; concealment is what costs trust — provenance is
  reverse-verifiable, and a detected concealed fork down-weights the
  whole repository.
- State the increment in one sentence next to the lineage line:
  "differs from <original> in: ___". If that sentence is hard to
  write, return to the four questions.
- Inherited material keeps the original's spirit; do not rename
  concepts cosmetically to manufacture distance (decorative bias).
