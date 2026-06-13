# layers — sorting material into three layers

Read this before writing any handoff. Every sentence of source material
goes into exactly one of three layers, or into the danger class.

## Layer 1 · Pinned (must not be reopened)

Decisions already made that the receiving agent must not re-evaluate:
names, account handles, architecture choices, scope cuts, closed strategic
questions.

Test question: **if this were reopened, would that be waste or progress?**
Waste → pinned. Progress → it does not belong here.

Write pinned items as a numbered list, one decision per line, verbatim
where exactness matters (handles, repo names, license strings). Exactness
is the point: a pinned item exists so the receiver can string-match against
it, not paraphrase it.

## Layer 2 · Status (current state, updatable)

What is in progress, what is done, what is queued. The receiving agent is
allowed — expected — to update this layer as it works.

Status lines state facts, not intentions: "3 of 6 files written" rather
than "going well". A status line the receiver cannot verify or falsify is
rationale in disguise; move it.

## Layer 3 · Rationale (why it was decided this way)

Strategy, trade-offs, the reasoning behind pinned items. The receiver
reads this layer to understand, not to revise. It exists so the receiver
can extrapolate correctly when it hits a case the handoff did not cover —
not so it can second-guess covered cases.

Rationale is optional. A handoff with an empty rationale layer is still a
valid handoff; a handoff whose rationale leaks into the pinned list is not.

## Danger class · Pending review

Items that are neither pinned nor plain status: judgments scheduled for
re-examination, open questions awaiting a named person's call.

These must be marked explicitly — "pending: awaiting X's decision" — and
kept out of the pinned list. The failure mode runs both directions:
a pending item misfiled as pinned freezes a judgment that should update;
a pinned item misfiled as pending invites the receiver to reopen it.

When you cannot tell which side an item falls on, do not guess. Stop and
ask the user to classify it. (This is the skill's stated failure behavior;
it applies here most often.)
