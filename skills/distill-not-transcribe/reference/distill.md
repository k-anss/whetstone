# reference/distill.md — the distill line

Load this only after the gate passed and the user confirmed structure.
Input: a structured method document written by one author for their own
use (a protocol, SOP, working instruction).

## The seven transformations (document → skill)

A working document leans on shared context between author and their
usual assistant. A skill is read by a stranger agent with zero context.
Apply all seven; most failures come from skipping one.

| # | Transformation | Operation |
|---|---|---|
| 1 | Re-point "you" | The document's "you" means "an assistant who knows the author". Rewrite for an agent that knows nothing: delete or self-explain every reference that depends on private context. |
| 2 | Make tacit rules explicit | Anything the author "would obviously do" must become a written rule or it does not exist for the agent. |
| 3 | Extract the stance | Opinions go to the agent layer as hard constraints; local color and channel-specific grounding go to the human layer (README / language twin). |
| 4 | Keep prohibitions sharp | Never soften the author's "do not" lists. Differentiation lives almost entirely in the prohibitions; softening them produces one more generic skill. |
| 5 | Split author traces | Identity traces (who/where/which org) → generalize or remove. Judgment traces (why this rule, what failed) → keep verbatim. The most common error is deleting both or keeping both. |
| 6 | Add workflow gates | Insert "report structure before writing files" checkpoints. A document trusts its reader; a skill must not trust its executor. |
| 7 | Thicken every hard rule | See below. |

## Transformation 7: thickening (rule → load-bearing rule)

Every hard rule ships in four parts:

> **Rule + mechanism (why) + one desensitized field observation +
> validated boundary**

- **Mechanism:** a rule with a mechanism extrapolates to inputs the
  author never saw; a bare rule shatters there. "No emoji" alone is
  thin; "decorative symbols inject false emotional temperature into
  archival contexts and have become a low-quality signal through AI
  overuse" can be applied to cases the rule never listed.
- **Field observation:** "this rule exists because I watched ___ fail
  when ___". Plain physical detail, no drama — dramatic anecdotes read
  as fabricated; flat specifics read as witnessed.
- **Boundary:** state where the rule was actually validated and mark
  everything else untested. An honest boundary is thicker than fake
  coverage, and an agent can route precisely only against declared
  boundaries.
- **The forbidden shortcut:** never thicken by importing "industry
  best practices". That is how slop is made — every imported paragraph
  dilutes the judgment density that justified the skill. All three
  materials come from the author. If the author has no observation for
  a rule, the rule ships thin and is marked thin — do not invent.

Evidence sourcing rules: `reference/evidence.md`.

## Interface discipline

Thick substance, thin interface. SKILL.md stays a map (target ≤150
lines): observations, mechanisms, and boundaries sink into reference
files; the map carries only what every run needs, plus a table of
"when doing X, load Y".

## Raw material (boundary: NOT yet validated)

Structured protocols and raw material (dialogue transcripts, scattered
notes) are different input distributions. For protocols, distillation
is transformation; for raw material, a prior extraction pass is needed
(harvest "when X, choose A over B" judgments out of thousands of
words before anything can be transformed). This skill has been run on
protocols only. If the input is raw material: say so explicitly, run
the extraction pass as an experiment, label the result accordingly,
and expect this section to be revised after first real use.
