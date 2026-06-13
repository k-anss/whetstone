# examples/recursive-acceptance.md — acceptance protocol & first-run record

The acceptance test for a skill-making skill is recursive: use it to
rebuild, from the original source protocol, a skill that already
exists — then diff the two.

## Protocol

1. Input: the source protocol of an existing skill in this collection
   (first run: the field-data-collection skill's source protocol).
2. Run this skill end to end in a fresh session: route → gate →
   structure report → build → acceptance.
3. Diff the rebuilt skill against the shipped one, section by section.
4. Read the diff:
   - Rebuilt ≈ shipped → the method is fully encoded; release.
   - Diff is large somewhere → that delta is judgment still living in
     the author's head, not yet written down. Each delta becomes a
     patch to SKILL.md or its references.
5. Record below. This record doubles as the skill's test trace.

## First-run record

[PENDING — to be filled at first real run. Fields:]
- Date / model / session type:
- Gate results (5 questions, pass/fail each):
- Structure report accepted as-is? What was corrected:
- Diff summary (counts + the three largest deltas):
- Patches applied:
- Mis-trigger set used (5+ queries) and results:
- Verdict:
