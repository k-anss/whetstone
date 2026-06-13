---
name: backtest-your-framework
description: >
  Validate whether a judgment framework (an investment screen, a hiring
  rubric, a risk score, any rule-based decision system) actually works, by
  backtesting it on real historical cases under a strict anti-self-deception
  protocol. Trigger when the user says "backtest my framework", "test if this
  rubric/model actually works", "validate my decision criteria against
  history", or "stress-test my framework on real cases". Enforces three
  laws — freeze the AI's context to time T, isolate the outcome, judge before
  revealing — so the framework gets graded by history, not by the AI's
  optimism. Do NOT trigger for: backtesting a trading strategy on price data
  (that is quantitative, not judgment), evaluating a single decision after
  the fact, or asking for an opinion on a framework's design (this skill
  exists precisely because opinions are unreliable here).
---

# backtest-your-framework

Turn "is my framework any good?" from a question into an experiment.
The AI judges a historical case with its context frozen at time T. The
outcome stays hidden until the judgment is complete and committed. Then
history — not the AI — grades the framework.

## Load-bearing stances

### 1. Never ask the AI whether your framework is good. It will agree.

Mechanism: models drift toward the designer's optimistic assumptions. Two
default preferences stack — "sound insightful" and "satisfy the person" —
and together they systematically overrate whatever framework is on the
table. The agreement is sincere-sounding and worthless.

Observation: when I first asked directly "how does this framework look?",
every answer was affirmation. Zero validation value. The framework's
systematic biases — rules that blocked good cases, rules that waved bad
ones through — only surfaced after switching to blind historical testing.

Boundary: this stance covers validation. Asking the AI to help *draft* a
framework is a different activity and is fine; just never let drafting
feedback masquerade as evidence the framework works.

### 2. The AI will cheat with outcomes it already knows.

Mechanism: famous cases live in training data with their endings attached.
A recognizable name leaks the outcome, and the judgment silently flips from
"reason forward with the framework" to "rationalize backward from memory."
The output still looks like framework reasoning. It is not.

Observation: running cases under real names, the model cited "I know this
later became X" mid-judgment — test voided. The fix that held: rename the
subject, blur identifying details, keep the decision-relevant facts
(funding scale, team profile, time window) intact.

Boundary: anonymization protects against recognition, not against the user
accidentally writing post-T facts into the case card. Both leaks kill the
test; the workflow gate below checks for both.

### 3. Judge first, reveal after. No revisions in between.

Mechanism: if the AI receives any truth signal while judging, it converges
toward the truth — quietly. What gets measured is then the AI's ability to
read the room, not the framework's ability to discriminate.

Observation: judgments that left themselves revision ledges ("if Z turns
out true, then rule 4 may not apply...") functioned as self-correction
backdoors. The judgment must be complete — confidence number, failure
modes, go/no-go — and committed before any reveal. No ledges.

Boundary: post-reveal analysis may freely revise views; that is Phase 4's
job. The ban applies only between commitment and reveal.

## Map

| When doing | Load |
|---|---|
| Understanding the three hard constraints | `reference/three-laws.md` |
| Designing a test case (Phase 1) | `reference/protocol.md` + `reference/anti-cheating.md` |
| Running the blind judgment (Phase 2) | `reference/protocol.md` |
| Revealing, comparing (Phases 3–4) | `reference/protocol.md` |
| Summarizing across cases (Phase 5) | `reference/bias-table.md` |
| Seeing one full worked run | `examples/sample-case.md` |

## Workflow gate (mandatory)

Before entering blind judgment, echo back to the user:

1. the freeze time T;
2. the desensitization checklist — what was renamed, what was blurred,
   what decision-relevant facts were kept.

Get explicit confirmation. This catches residual post-T details or outcome
hints in the case description before they void the run.

## Failure behavior

If, during blind judgment, the AI references information dated after T or
a known outcome ("I know this later became..."): **stop the test
immediately** and report "case contaminated — redesign the description."
Never finish a contaminated run. A contaminated result is worse than no
result: it hands the framework false confidence.

## Fields

- **Version**: 0.1 (2026-06). Changelog: initial release. Corrections will
  be marked in place, not deleted.
- **Deprecation condition**: when models can reliably self-quarantine known
  outcomes during judgment (declare "I may know the ending; deliberately
  not using it" — and actually not use it), the value of this external
  discipline drops. Re-examine this skill then.
- **Failure behavior**: see above — stop and report, never run contaminated.
- **Composes with**: any decision or evaluation framework. This skill only
  validates frameworks; it does not design them. Explicit user instructions
  override this skill.
- **Time**: judgments fixed 2026-06. The premise "models cheat with
  training-data outcomes" tracks model self-quarantine ability; expected
  review window 12–24 months.
- **Boundary conditions**: designed for validating *judgment-type*
  frameworks — rule-based qualitative verdicts on an opportunity or
  subject. Not applicable to quantitative strategy backtests over
  price/numeric series. Not applicable to domains lacking reliable
  historical cases. Both are out of scope, untested, and will stay so.
