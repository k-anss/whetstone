---
name: distill-not-transcribe
description: >
  Turn a written method — a workflow document, protocol, SOP, or an
  existing popular skill — into a new skill that encodes the author's
  judgment, not just their steps. Trigger when the user says "make this
  into a skill", "turn my workflow / protocol / SOP into a skill",
  "skill-ify this document", "adapt / fork / localize this skill for my
  case", or "distill my method so an agent can run it". Do NOT trigger
  for: writing a single prompt, generating documentation or READMEs,
  building an application, or packaging step-by-step instructions that
  contain no decisions. If the source material contains no judgment,
  the correct output is a refusal (see Failure behavior).
---

# distill-not-transcribe

Build skills from judgment, not from steps. A skill earns its place in
the context window by encoding decisions a bare model would not make
on its own. (Chinese twin: SKILL.zh.md — same map, zh-specific copy
checks live there.)

## Stance — load-bearing biases

People will disagree with these. That is the filter, not a problem.

1. **Judgment density before output.** Material with steps but no
   decisions becomes a script, not a skill. Why: agents already execute
   steps well; what they lack is the author's "when X, choose A over B".
   Observed (2026-06): of 20,000+ skills in public directories, most
   are step lists; the #1 item on a paid curated marketplace had 116
   installs. Skills without judgment die unnoticed.
2. **Precision before recall.** Write negative triggers. A skill that
   stays silent beats one that over-fires. Why: a mis-triggered skill
   pollutes the context window — decoration in another form. Official
   guidance favors "pushy" descriptions; this skill deliberately takes
   the opposite side.
3. **Honest lineage.** Derived work declares its source. Why:
   provenance is reverse-verifiable; concealed derivation, once
   detected, down-weights the entire repository, not just one file.

## Route first (always)

Before anything else, check whether a comparable skill already exists
(search directories / awesome lists / the marketplace).

- A comparable original exists → **fork line** → load `reference/fork.md`
- Nothing comparable → **distill line** → load `reference/distill.md`

## Gate: judgment-density screen

Run before producing anything. Two or more failures → refuse
(see Failure behavior).

1. Does the material contain at least three decisions of the form
   "when X, choose A over B, because ___"?
2. Has the author actually run this — can they point to one place
   where it failed?
3. Strip every opinion out. Does what remains still justify a skill?
   If yes, it is a generic script: do not build. The value must live
   in the judgments.
4. For each strong opinion: who does it help, and when would following
   it hurt? No answer → decorative bias → drop the opinion, or drop
   the skill.
5. Would a bare frontier model already do this at ~80% unprompted?
   Name the exact missing 15–20 points. Cannot name them → there is
   no skill here.

## Workflow gate

Report the planned structure (sections, reference files, what loads
when) and the gate results to the user BEFORE writing any file.
Wait for confirmation.

## Build

- Distill line: seven transformations → `reference/distill.md`
- Fork line: four questions + test-trace page → `reference/fork.md`
- Every skill ships the six mandatory fields → `reference/fields.md`
- Evidence rules for thickening (where observations may come from,
  where they may not) → `reference/evidence.md`

## Acceptance — all four, in order

1. **Before/after.** Same input, bare model vs with-skill, side by
   side. No visible gap → do not ship. Visible gap → it goes to the
   top of the README.
2. **Mis-trigger set.** Five or more queries that must NOT trigger;
   verify silence.
3. **Self-referential demo.** The skill demonstrates itself on itself
   or on one real case.
4. **Author redline grep.** Scan all output for the author's declared
   redline terms (identity, organization, location granularity). The
   list is author-supplied; never assume it is empty.

## Failure behavior

If the gate fails: stop and report "this material is a script, not a
skill — it contains steps but no decisions", listing which gate
questions failed. Do not pad with generic best practices to force a
result. Silent fabrication — producing something plausible instead of
reporting failure — is the worst failure mode this skill knows.

## Lifecycle — this skill's own mandatory fields

- **Version:** 0.1 (2026-06-12). Pre-release: before/after evidence
  pending first real run (see examples/recursive-acceptance.md).
- **Deprecation condition:** when a bare frontier model, asked to
  "turn this document into a skill", reliably produces output with
  negative triggers, boundary conditions, and declared lineage —
  retire this skill.
- **Composition:** composes-with the official skill-creator: use its
  trigger-rate eval loop and packaging tooling; this skill governs
  judgment screening and trust structure, not tooling. Yields to
  explicit user instructions.
- **Boundary:** validated on structured, single-author protocol
  documents. Raw dialogue transcripts and multi-author material:
  see distill.md "Raw material" — that path is NOT yet validated.
- **Time:** judgments dated 2026-06. Ecosystem observations expected
  to decay within 12–18 months; the gate questions should outlive them.
