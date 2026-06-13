# Anti-Cheating: the Two Self-Deception Sources (plus one)

This is the part most "evaluation prompts" skip. Both sources produce
output that looks exactly like valid testing. That is what makes them
dangerous.

## Source 1 · Optimistic agreement

**What it is.** Ask an AI "is my framework good?" and it answers from
inside your optimism. Its default preferences — sound insightful, satisfy
the asker — stack into systematic overrating. The agreement is fluent,
specific-sounding, and evidentially empty.

**Defense.** Never solicit an opinion as validation. Run a blind test
instead: the AI applies the framework to a case whose outcome it cannot
see, and the outcome does the grading. Opinions are for design
discussions; only blind tests are for validation.

**Detection cue.** If the "validation" produced no surprises — no rule
exposed as too strict, none as too loose — suspect that no validation
happened.

## Source 2 · Training-data outcome leakage

**What it is.** Well-known cases sit in training corpora with their
endings. A recognizable name hands the AI the outcome, and judgment
flips from forward reasoning to backward rationalization — invisibly.
The prose still cites framework rules.

**Defense.**

- Rename the subject before testing.
- Blur identifying details (distinctive product features, founder
  biographies, exact dates that pinpoint the company).
- Keep decision-relevant facts: funding scale, team profile, time
  window, market context. Blur identity, not substance.

**Detection cue and response.** If the AI says anything like "I know
this later became X" or references post-T developments: **stop
immediately**. Report "case contaminated — redesign the description."
Do not finish the run. A contaminated run that completes will be
remembered as evidence; that false confidence is worse than having no
result.

## Source 3 · User-side contamination (the one people forget)

**What it is.** The test designer leaks their own verdict into the case
card: "this one looked promising", "an obviously crowded market",
adjectives doing the judging before the framework gets a chance.

**Defense.** Case descriptions are flat, factual, neutral. A useful
edit pass: delete every adjective and adverb from the case card; if a
sentence collapses, it was carrying a verdict — rewrite it as a fact or
cut it.

**Detection cue.** Read the case card cold and ask: could a stranger
guess which way the designer expects this to go? If yes, rewrite.
