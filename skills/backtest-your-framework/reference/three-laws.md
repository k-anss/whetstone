# The Three Laws

Hard constraints. A run that violates any one of them is not a weaker
test — it is not a test.

## Law 1 · Time freeze

**Practice.** Declare a freeze time T at the start. Tell the AI
explicitly: "You may only use information available before T." The case
description must contain no detail dated after T. Search tools are
disabled during the judgment phase — not the whole session, only the
phase where the framework is being applied. (If case design itself needs
fact-checking, do that before the freeze, in a separate step.)

**Why.** The framework's job is to discriminate under the uncertainty
that actually existed at T. Any post-T information collapses that
uncertainty, and the test stops measuring the framework.

**If violated.** The judgment becomes hindsight wearing the framework as
a costume. Results are invalid and — worse — look valid.

## Law 2 · Outcome isolation

**Practice.** Before the reveal, the AI must not know whether the case
succeeded or failed. Concretely:

- Write the case description in neutral language; no hints of the ending.
- Rename the subject. A famous name is itself a leak — recognition
  delivers the outcome along with it.
- Generalize the actors: "a 1–3 person generalist team / $300k own
  capital / full-time" instead of identifiable specifics.
- Keep the decision-relevant facts intact: funding scale, team profile,
  market timing, the time window. Blur identity, not substance.

**Why.** Models carry famous endings in their weights. Isolation is the
only way to make the model reason forward instead of recalling backward.

**If violated.** The output will still be fluent framework-shaped prose,
but its engine is memory, not rules. Detection cue: the AI mentions
post-T developments or names what the subject "became."

## Law 3 · Judge before reveal

**Practice.** The AI delivers its judgment in full — confidence number,
expected failure modes, go / no-go / borderline — before the truth is
shown. Between commitment and reveal: no edits, no additions, no
"actually, one more consideration." Revision ledges ("if X, then rule 4
may be wrong") are banned inside the judgment.

**Why.** Any truth signal during judgment lets the AI converge quietly
toward the answer. The test then measures accommodation, not
discrimination.

**If violated.** The comparison in Phase 4 becomes meaningless: you are
comparing the truth with a judgment that already saw the truth.

## After the reveal

All three laws expire at the reveal. Post-reveal analysis (Phase 4)
should revise freely — that is where learning happens. The laws protect
the judgment, not the discussion.
