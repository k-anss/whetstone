# Quality Gates

> **How to apply these gates in self-use.** Every gate below is a **lens for
> marking, not a switch for auto-deleting.** When a card trips a gate, the
> reviewer attaches a disposition (default `ESCALATE`) and pushes it to the human
> review list — it does **not** delete, downgrade, or re-run the card on its own.
> The human has read the book several times and makes the call. The deep
> extractions that trip "over-interpretation" or "cost inflation" are often the
> *good* ones; a script must never cut them. The only mechanical hard stop is a
> parse failure that crashes a downstream script. Each gate is also tagged
> `[method]` (true for any model/book) or `[adapt]` (works around a model/中文
> quirk) per SKILL.md; in self-use you obey both, the tag is for later product
> cleanup.

## Contents

1. Evidence
2. Event identity
3. Cost and exchange
4. Results
5. Routing
6. Expectation management
7. Depth preservation
8. Action and relationship claims
9. Production completeness
10. Reduction integrity

## 1. Evidence

Classify every central claim:

- `text`: directly stated or visibly performed;
- `strong inference`: supported by at least two independent textual facts;
- `hypothesis`: another reasonable explanation remains.

Keep hypotheses out of formal card logic. A character's guess remains a character's guess.

Never infer that a decision-maker knew facts merely because later events make the decision look useful.

Explicit narration outranks inference. If the narrator says an act was unplanned,
accidental, unknown, or misunderstood, do not reconstruct it as deliberate strategy from
timing or effectiveness.

Uncertainty is not proof of error. “Further investigation is needed” does not establish
that evidence was contaminated, coerced, false, or that innocent people were included.
Name only the demonstrated deficiency, such as an unsupported accusation or an incomplete
evidence chain.

## 2. Event Identity

Do not join adjacent events into one transaction merely because they share participants or political context.

To claim an exchange, identify:

- offer or lever;
- demanded or accepted concession;
- causal link between them;
- observable response.

If the concession occurs before the alleged demand, or the actor later chooses a third option, downgrade the exchange claim.

Stop causal credit when a counterpart, once persuaded, released, or authorized, takes an
independent third option that was not part of the agreement. Credit the earlier actor only
for the observed belief change, agreement, release, or restored capacity.

Split a long chain when agency or mechanism changes. An externally enabled escape and a
later deliberate signal transfer are separate candidates even when they occur in one
continuous sequence. Do not use the clarity of the later tactic to upgrade the earlier
passive segment.

Check chronology before causality. A condition introduced after a decision cannot be the
cause of that decision. It may alter implementation, provide reassurance, or improve one
party's position.

## 3. Cost And Exchange

A cost must be borne, risked, or deliberately surrendered by the focal actor.

Invalid costs:

- harm suffered only by a third party;
- a resource the actor never controlled;
- a hypothetical downside that did not influence the choice;
- a future debt described as cheap because payment is delayed.

Third-party injury or death is not the focal actor's paid cost unless the actor controlled
the deployment, knowingly chose the exposure, and the sacrifice was part of the decision
being evaluated.

Open-ended promises are high-uncertainty liabilities, not free currency.

Do not fold later voluntary help into an earlier deal unless the earlier text made it part of the bargain.

Separate paid cost from exposure and residual risk:

- paid cost: actually surrendered or borne;
- exposure: information or capability revealed by acting;
- residual risk: a possible future consequence.

Do not move a possible future consequence into the paid-cost field.

Treat reputational harm as exposure or risk unless an observable relationship loss,
sanction, opportunity loss, surrendered reputation asset, or adverse response has already
occurred. Do not charge the same pre-existing bad reputation repeatedly.

## 4. Results

Use controlled states:

- `completed`: target result is observed;
- `stage-complete`: an intermediate target is observed;
- `ongoing`: action started, outcome absent;
- `failed/backfired`: failure is observed.

Silence, surprise, fear, consideration, or temporary pause does not prove persuasion or durable change.

## 5. Routing

A weak-side case requires a real constraint plus exchange, borrowed leverage, rule reversal, or cost transfer.

A management case requires control of resources plus a meaningful allocation, authorization, incentive, information, or risk decision.

Allow dual routing only when core problem, central lever, and actual cost all differ.

Different narrative viewpoints do not satisfy dual routing. Retain the route with stronger
decision ownership unless all three routing dimensions genuinely differ.

## 6. Expectation Management

Require all three:

1. whose expectation;
2. changed from what to what;
3. how that change altered action.

Apply deletion:

- mechanism fails without the expectation change: `primary`;
- mechanism survives but weakens: `present`;
- only surprise, concealment, fear, information asymmetry, or guessing: no tag.

## 7. Depth Preservation

Depth comes from:

- reconstructing alternatives and constraints;
- distinguishing immediate and long-term positions;
- identifying what remained unresolved;
- comparing actor perspectives;
- exposing uncertainty and rival explanations;
- identifying a transferable mechanism with boundaries.

Depth does not come from inventing hidden motives, declaring broad systems collapsed, or forcing every case to match a favored method.

## 8. Action And Relationship Claims

Do not upgrade a physical or emotional action into strategy unless the text supports:

1. a prior or contemporaneous objective;
2. an observable response caused by the action;
3. no explicit narration that the act was accidental, impulsive, or unplanned.

Require a causal chain:

`prior state → action → counterpart/system response → direct result`

When the response is missing or an external event could independently explain the result,
state the strongest rival explanation and downgrade causality.

Use the lowest relationship status supported by behavior:

`contact → one-time exchange → temporary cooperation → conditional alignment → durable cooperation → loyalty`

A declaration, rescue, message, or shared escape does not by itself establish durable
cooperation or loyalty.

Separate proposal, adoption, execution, and result. Do not assign a multi-actor outcome
entirely to the proposer or assume every participant shared one plan.

Do not fabricate dialogue: never present narrated paraphrase as if it were a
verbatim line of speech. (The quote field itself no longer needs to be verbatim —
see below — but inventing words the text never contains is fabrication, which the
anchor check is there to catch.)

A quote field (`关键原句`) is for meaning and may be paraphrased or truncated; it
is not proof of anything. Fabrication is established separately by the `定位锚`
short anchor that must be `grep`-able in the slice. Do not reject a card because
its quote is non-verbatim; if its anchor cannot be located, mark it `疑似编造`
into the review list and let the human look.

A self-check finding is operational. A gate failure produces a **marking** —
delete / downgrade / split / rewrite are **recommendations carried to the human**,
not actions taken automatically before submission.

Evidence-boundary violation (a card built partly from outside the assigned slice)
is a serious marking: later evidence can alter recall, result state, causality,
and routing. Flag the whole chunk as `证据越界，建议人工复跑` and surface it — but
the re-run is the human's decision, not an automatic restart. Default is: keep the
chunk, mark it, the human decides whether to rebuild from the allowed slice.

Do not call absent intervention deliberate tolerance unless the decision-maker knew
beforehand, had authority to intervene, and chose not to. Otherwise analyze only later
containment or feedback.

Publicly elevating, protecting, or honoring a person does not establish hostage control.
Require observable restriction, a release or disposition condition, and a response caused
by that control.

Do not attribute a safeguard, blank, condition, or procedural limit to the focal actor
merely because it benefits that actor. First establish who designed it, who could alter it,
and who controlled its use.

Match result precision to intent precision. A broad wish to create disorder cannot support
a specific success or backfire finding without a defined target state and observable
response.

## 9. Production Completeness

Mechanical validity is not evidence that a map pass read the source. Reject a production
chunk when any output contains placeholder chapters, generic “this chunk” prose, pending
detail markers, title-scan disclaimers, or an admission that the files are only a
framework.

Require a chapter-by-chapter coverage record. Every assigned chapter must point to one or
more event IDs or state `no independent major event` with a short transition description.
This is a recall audit, not a minimum event or card quota.

Batching may reduce handoff overhead, but it must not silently reduce the reading mode.
When the producer cannot finish another full chunk, it must stop after the last complete
chunk and create no placeholder files.

Completion reports must agree with the artifacts' own status. A file labeled draft,
incomplete, title scan, or pending detail cannot be counted as completed.

## 10. Reduction Integrity

Re-extraction starts from source events and evidence, not from the malformed card's title
or conclusion. Permit zero, one, or multiple replacement cards.

Count method support by independent event node. A weak-side card, management card, and
summary card describing the same actor, action, response, and result provide one context,
not three.

For a limited-goal action require:

- why the original goal is unreachable;
- the replacement target;
- observable success criteria;
- a stopping rule;
- the real cost paid to obtain the signal or partial result.

Do not upgrade “boost morale,” “create influence,” “stabilize the situation,” or similar
outcome language without these fields.

Do not promote a mechanism to a stable method from one continuous arc, even when the arc
contains several cards. Preserve it as a one-off tactic until another independent context
supports the same causal structure.
