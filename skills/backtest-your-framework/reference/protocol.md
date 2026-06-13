# The Five-Phase Protocol

Each phase has named deliverables. Skipping a deliverable usually means
a law is about to be violated.

## Phase 1 · Case design (human-led)

The user picks a historical time point T and a real opportunity or
subject they know the outcome of. Build a **case card**:

- **Time anchor** — e.g. "January 2022".
- **Generalized actor profile** — e.g. "1–3 person team / $300k own
  capital / full-time / full-stack AI capability". No identifiable
  specifics.
- **Neutral opportunity description** — facts only; no leading words
  ("looks promising", "obvious trap"), no outcome hints, nothing dated
  after T. Rename the subject; famous names leak endings.
- **Test target** — which part of the framework this case is meant to
  probe.

Deliverable: the case card, plus a desensitization checklist (what was
renamed, what was blurred, what facts were kept).

**Gate**: echo freeze time T and the desensitization checklist to the
user for confirmation before proceeding.

## Phase 2 · Blind judgment (AI, under the three laws)

In a clean context: attach the framework, give the case card, require:

- Follow the framework strictly.
- Tag every conclusion as **framework-triggered** (a hard rule fired) or
  **own reasoning** (the AI filled a gap). The ratio matters later.
- A confidence number (e.g. "65%"), not hedged prose.
- Expected failure modes: if this goes wrong, how, concretely.
- A final verdict: go / no-go / borderline.
- **No revision ledges.** "If... then rule X may be wrong" is banned.

Deliverable: one committed judgment document.

## Phase 3 · Reveal (human-led)

The user discloses:

- what actually happened after T;
- who succeeded, who didn't;
- factors the AI had no way to see.

Deliverable: the truth record.

## Phase 4 · Comparison

Work through, in order:

1. Was the direction right (go / no-go)?
2. Was the confidence number reasonable given what was knowable at T?
3. Were the predicted failure modes close to the real ones?
4. Which hard rules were **true intercepts** (blocked for the right
   reason)?
5. Which were **false negatives** (blocked a case that turned out good)?
6. Which were **false positives** (waved through a case that turned out
   bad)?

Deliverable: a per-case comparison note. Judge the framework against
what was knowable at T — a wrong verdict made for the right reasons at
T is information about the world's noise, not necessarily about the
framework.

## Phase 5 · Bias table (after several cases)

One case proves nothing. After roughly 5 cases, consolidate into the
bias table (see `bias-table.md`): where the framework is reliably
accurate, where it is systematically off, and which specific rules to
change.

Deliverable: the bias table plus a concrete rule-change list.

## When not to run this protocol

- The framework's structure is still in flux — finish building first.
- The framework is already in live use generating real feedback — real
  feedback is itself the test; don't force a backtest.
- The domain has no reliable historical cases — it cannot be backtested.
