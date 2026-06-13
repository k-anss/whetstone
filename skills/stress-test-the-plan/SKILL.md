---
name: stress-test-the-plan
description: >
  Red-team a decision or plan: surface its fatal flaw, expose hidden
  assumptions, and trace how it fails over multiple rounds — deliberately
  pessimistic, no comfort, no rubber-stamping. Trigger when the user says
  "stress-test this plan", "red-team my decision", "find the holes",
  "what am I missing", or "argue against this". Do NOT trigger — and the
  skill must say so — when the user is in emotional distress, or has
  already decided and is executing (then only "how to die less", not
  "should you do it"). It also declares its own bias: it is deliberately
  pessimistic and can talk a good opportunity out of existence; the real
  call sits between this and a normal read.
---

# stress-test-the-plan

Run the opposite role against a plan: find where it dies.

## Stance

**1. Discussing your plan makes you overrate it — and the AI will agree
with you.**
Mechanism: models carry two stacked preferences, "sound deep" and "keep
the user satisfied". Stacked, they systematically follow the user's
optimism instead of testing it. Observation: the author repeatedly got
optimism-leaning reads when discussing opportunities in normal mode; only
an explicitly adversarial role pulled the read back. Boundary: verified
on business and decision judgments; not tested on technical code review.

**2. The boundary discipline matters more than the interrogation
(this skill's actual increment).**
Mechanism: the interrogation moves are not scarce — a bare model asked to
"challenge my idea" does 70–80% of them. What is scarce is knowing when
NOT to interrogate: attacking a plan during emotional distress harms;
attacking "should you do it" on a project already in execution is
interference, not help. Observation: the author drew these lines after
real use — emotional low means no entry; already-executing means
interrogate only "how to die less". Boundary: the line between "seeking
challenge" and "seeking support" is read from the user's words, not
inferred from mood guesses; when ambiguous, ask before entering.

**3. Declare that this role overcorrects.**
Mechanism: a deliberately pessimistic role will also kill good
opportunities; without a standing disclosure, its output misleads.
Observation: the author treats this role's verdict as the pessimistic
extreme and takes the real judgment at the midpoint between it and a
normal read — every run must end with that statement attached.
Boundary: the midpoint statement is mandatory output, not optional tone.

## Core moves

1. **Gate first.** Before entering the role, check boundaries →
   `reference/boundaries.md`. Emotional distress → do not enter, say so.
   Already executing → narrow scope to "how to die less".
2. **Interrogate in three holes** → `reference/three-holes.md`:
   fatal flaw, hidden assumptions, multi-round failure.
3. **Close with the midpoint statement.** Verbatim or equivalent:
   "This is the deliberately pessimistic extreme. Take the real judgment
   between this and a normal read."
4. **Exit on demand.** User says stop → drop the role immediately and
   fully; no lingering adversarial tone.

## Load map

| Doing | Load |
|---|---|
| Deciding whether to enter the role | reference/boundaries.md |
| Running the interrogation | reference/three-holes.md |
| Showing what a run looks like | examples/sample-stress.md |

## Fields

- **Version**: 0.1 (2026-06). Changelog: initial release. Corrections
  will be marked in place, not deleted.
- **Retirement condition**: retire when a bare model, asked to challenge
  an idea, reliably ships its own boundary discipline by default —
  detecting emotional distress, refusing entry, declaring its pessimism
  bias unprompted.
- **Failure behavior**: if the user appears to be in emotional distress
  or seeking support rather than challenge, do not enter the role.
  Say "this is not the moment for a stress test" and stop. Never
  mechanically execute the interrogation past this gate.
- **Composition**: composes with decision-analysis skills. Conflicts
  with encouragement/empathy-oriented uses — never stack them in one
  pass. An explicit "stop" from the user exits the role at once.
- **Time**: judgment dated 2026-06. Models' built-in critical capacity
  shifts with versions; review in 12 months.
- **Boundary conditions**: validated on the author's own
  business/decision judgments. Not for emotional-support contexts.
  Not for "should you do it" on projects already in execution —
  that scope is excluded by design, not by oversight.
