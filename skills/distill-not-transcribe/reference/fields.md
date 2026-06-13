# reference/fields.md — six mandatory fields

Every skill produced by this method ships all six. A skill missing any
of them is not done. These fields exist because a skill, unlike a
document, is consumed by two readers — humans and agents — and both
need machine-legible answers to "when do I trust this, when do I stop".

## 1. Version & changelog
Semantic-ish version plus dated changelog. Corrections never delete:
superseded statements stay, marked "superseded by vX — see ___".
(For humans this is intellectual honesty; for machines it is the only
way to resolve contradictions between crawled copies of your content.)

## 2. Deprecation condition
One sentence: "when a bare frontier model can reliably do ___,
retire this skill." Every skill's true competitor is the improving
bare model. A skill that cannot state its own obsolescence is claiming
immortality, which reads as either naivety or marketing.

## 3. Failure behavior
What the agent must DO when input falls outside the validated
boundary: stop, and report "outside this skill's validated range" —
never silently degrade and produce something plausible. Boundary
declarations are the map; failure behavior is the action at the
map's edge.

## 4. Composition declaration
- composes-with: <skills/tools this works alongside, and the division>
- conflicts-with: <known collisions>
- yield rule: explicit user instructions override this skill.

## 5. Time field
Judgment date + expected decay, layered: core judgments (years),
tool-specific details (12–24 months), ecosystem observations
(shorter). Undated judgments get treated by readers as either eternal
truths (dangerous) or wholly stale (wasteful); dating is the fix.

## 6. Boundary conditions
Where this was validated, stated positively ("validated on ___"),
with everything else implicitly untested. Pairs with field 3.

## Placement
Fields 1, 2 and the skill-level boundary live at the bottom of
SKILL.md (a "Lifecycle" section). Fields 3–5 may live in SKILL.md
when short, or in reference/ when long. Rule-level boundaries live
next to their rules (see distill.md, thickening).
