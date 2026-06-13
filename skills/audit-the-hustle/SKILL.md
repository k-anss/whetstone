---
name: audit-the-hustle
description: Audit whether someone claiming to make money online — an indie hacker, a course seller, a "building in public" founder — is really operating or performing. Returns signals with confidence levels, never a verdict. Trigger when the user says "is this person/product legit", "are they really making money or selling a course", "vet this indie hacker / founder", or "audit this hustle". Enforces a signal checklist, a mandatory confidence-percentage conclusion, and an anti-bias self-check. Do NOT trigger for verifying a public company's financials (use real filings), fact-checking a news claim, or background-checking a private individual (privacy). States plainly when the truth is below the waterline (real payments, self-dealing) and the framework can't reach.
---

# audit-the-hustle

You can't verify if someone's really making money. You can only read the signals — so report signals with confidence, never a verdict.

## Stance

Three rules. Each carries its mechanism, one field observation, and its verified boundary. An explicit user instruction overrides any rule here — note the deviation and proceed.

### 1. Report signals plus a confidence split, never a verdict

Rule: every audit ends in the form "X% looks like a real operation, Y% looks like performance / a course-sales funnel." Never output "legit" or "scam" as a binary.

Mechanism: the decisive facts — actual payment volume, whether sales are self-dealt — sit below the waterline, outside anything externally checkable. A binary verdict on unverifiable facts manufactures false certainty. A calibrated percentage carries information the binary destroys: how far the evidence actually reaches.

Field observation: the author began these audits wanting a yes/no on "is this person for real," and watched that demand produce confident wrong answers. Across repeated audits of public build-in-public operators, the only output that survived contact with later evidence was the percentage split.

Boundary: verified on public online-income claims (indie products, courses, newsletters). When evidence is strong, confidence may run high — but never 100% or 0%.

### 2. Say plainly where the framework can't reach

Rule: questions answerable only with inside, real-time knowledge — real payments, self-dealing, who actually runs an account — get an explicit "below the waterline; this framework can't reach it." Not a forced estimate.

Mechanism: the model is not in the room. Some truths circulate only as live feedback inside a circle. Running the signal checklist on them anyway yields a number that looks rigorous and has nothing under it — worse than no number, because it displaces the reader's own inside read.

Field observation: the author has seen "is the founder faking his own sales?" questions where the checklist, forced through, produced a confident figure built on air. The move that held up was stopping and handing it back: "this one is below the waterline — your circle's read, not mine."

Boundary: verified for authenticity audits of online operators; untested as a general epistemics rule.

### 3. Run the anti-bias self-check every time, before the conclusion

Rule: before writing the conclusion, answer the four questions in reference/anti-bias.md, and label every conclusion line as either checklist-triggered or own-reasoning.

Mechanism: the model's defaults — famous name = trustworthy, good narrative = real, opportunity = worth flattering — systematically inflate authenticity scores. The two recurring failure modes are anchoring on head-of-distribution names and silently substituting reasoning for evidence while presenting both at equal weight.

Field observation: in unchecked runs the author kept catching well-known names being treated as the default answer to "who's real here." The bias never surfaced as a false statement; it surfaced as which evidence was never asked for.

Boundary: the four questions were distilled from recurring failures in real audits; they cover those recurring biases, not all bias.

## Workflow

1. Scan the five signal classes → load `reference/signals.md`. Mark each class: present / absent / unverifiable.
2. Draft the conclusion → load `reference/confidence.md` for the mandatory format and the above/below-waterline boundary.
3. Gate before output → run `reference/anti-bias.md`. Label each conclusion line checklist-triggered vs own-reasoning; the two carry different credibility and the reader must see which is which.

A worked, fully fictional run: `examples/sample-audit.md`.

## Maintenance fields

- **Version**: 0.1 (2026-06). Changelog discipline: corrections are marked in place, never deleted.
- **Retirement condition**: when a credible public third-party verification service for online-income claims exists and manual auditing is no longer needed, retire this skill.
- **Failure behavior**: if the question can only be answered with below-the-waterline information, stop and declare "framework can't reach" — do not pad a confidence number to stay useful. A padded number is more dangerous than none.
- **Composition**: composes with any research/search skill. This skill covers authenticity auditing only; it does not do financial-statement verification. Explicit user instructions take precedence.
- **Time**: judgments dated 2026-06. Signal channels (indie-hacker forums, payment-page screenshots, MRR dashboards) evolve with platforms; re-review in 12–18 months.
- **Verified scope**: auditing the public authenticity of people publicly claiming to make money online. Not for public-company filings. Not for background checks on private individuals (privacy).
