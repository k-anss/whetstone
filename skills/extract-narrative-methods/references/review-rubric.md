# Review Rubric (Reviewer-Facing)

> **Self-use rule.** Every disposition below is a **recommendation the reviewer
> writes onto the human review list**, never an action the reviewer takes on its
> own. Nothing here deletes, downgrades, or re-runs a card automatically. Default
> to `ESCALATE` (mark + send to human) whenever a call involves judgment; the
> human has read the book several times and decides. A deep card that trips
> "over-interpretation" is often correct — mark it, don't cut it.

The checklist Codex medium runs in the review layer, after scripts pass. This is
the semantic counterpart to the producer's [extraction-rules.md](extraction-rules.md);
the deep tests behind each line are in [quality-gates.md](quality-gates.md).
Assign one disposition per card: `KEEP` · `REWRITE` · `MERGE` · `DOWNGRADE` ·
`DELETE` · `ESCALATE` — as a marking, not an executed action.

## Event layer

- Does it cover every chapter in the chunk?
- Does it state objective actions, not impressions?
- Does it separate direct result from later risk?
- Is an ongoing event mislabeled as completed?

## A line (weak-side)

- Does a real exchange space exist?
- Is there an explicit action by the weak party?
- Does the counterpart give an observable response?
- Is the cost drawn from this chunk's evidence, not from expected inference?
- Six questions don't close → not a card.

## B line (management)

- Is there a stable, controllable resource?
- Is there a clear management choice, not ordinary execution?
- Can a management logic and a real cost be written?
- A merely local execution action is not a management card.

## Self-check

- Is the actual last chapter read stated?
- Is there a chapter-coverage table?
- Any placeholder phrase present?
- Is "this chunk done" mixed up with results from future chunks?

## Cross-card / pre-reduce

- Is a dual-routed event distinguished by problem, lever, AND cost — not just
  narrative viewpoint?
- Does one event's A+B count as a single evidence node?
- For a re-extraction, was the source re-read and each new card's six questions
  re-answered independently — not the old summary polished?
- Is reputational or future-burden cost actually incurred and incremental, not
  hypothetical?

## Risk marking (carry into reduce)

Mark, don't silently drop, cards that are valid but fragile, so the synthesis
layer weights them correctly. Examples of marks the validated run used:

- thin-evidence card kept only as a low-confidence corroborator (removable
  without breaking the method);
- a procedure whose effectiveness is separated from the truth of the testimony
  it relied on (not a normative positive example);
- a variant that depends on a lie (flagged as a risk variant);
- a coercive/high-personal-risk case kept only as a one-off tactic, not a stable
  method.
