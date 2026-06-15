# Prompt Templates

## Producer Prompt Assembly

Build each prompt in this order:

1. role and evidence boundary;
2. source and chunk range;
3. project-specific line definitions;
4. current hard quality gates;
5. schemas and output paths;
6. self-check questions;
7. current rule-set version.

Keep historical audit discussion out of production prompts. Convert it into concise active rules.

## Required Producer Outputs

### Event Audit

For every major event include:

- location;
- participants;
- event objective;
- objective action;
- counterpart or system response;
- direct result;
- result state;
- proposed route or rejection;
- evidence risk;
- possible duplicate.

Append a chapter-by-chapter coverage table. For every assigned chapter, list the relevant
event IDs or `no independent major event` plus a one-line transition description. Never
use a single range-level claim as proof that all chapters were read.

### Candidate Card

Require:

- source location;
- focal actor and constraint;
- resources, wants, and actual concessions;
- verifiable action;
- prior state, counterpart response, and direct result;
- exchange or management logic;
- evidence boundary;
- strongest rival explanation for any central inference;
- result and cost;
- paid cost, exposure, and residual risk as separate fields;
- one exact quote or empty;
- method signal, never stable-method declaration.

### Self-Check

Ask:

1. Which sentence most likely exceeds the text?
2. Is each cost borne by the focal actor?
3. Did I join adjacent events into an exchange?
4. Did I turn a character's guess into fact?
5. Did I confuse surprise with expectation management?
6. Is every quote exact, continuous, and inside this chunk?
7. Which rejected event is most likely to deserve a card?
8. Did I turn a physical action or emotional reaction into deliberate strategy?
9. Did I upgrade one-time help into durable cooperation or loyalty?
10. Did I separate proposal, adoption, execution, response, and result?
11. What is the strongest rival explanation for the weakest causal claim?
12. Who designed and controlled every claimed safeguard or retained option?
13. Did an independent third choice break the causal credit chain?
14. Did I merge a passive rescue segment with a later deliberate tactic?
15. Did I scan deliberate bodily cost, asset surrender, long-term debt, and enemy disposition?
16. What disposition did each hard self-check finding trigger?
17. Is any dual-routed event distinguished only by viewpoint?
18. Is reputational cost observed and incremental?
19. Did I leave an admitted paraphrase inside a quote field?
20. Did the alleged deliberate tolerance occur before the decision-maker knew?
21. Did an entry strategy claim results beyond proven access?
22. What was the assigned chapter end, and what is the largest chapter cited anywhere?
23. Did I call someone a hostage without proving restriction and conditional release?
24. Is a claimed future management burden already concrete inside this evidence boundary?
25. Does every assigned chapter appear in the coverage table?
26. Does any output still contain a placeholder, empty chapter, or pending-detail marker?
27. Did batching silently change full-text reading into title scanning or framework drafting?
28. Does the completion report match the actual artifact status?

## Repair Prompt

Give:

- v1 files;
- source slice;
- audit findings by failure family;
- mandatory keep/rewrite/delete/add actions;
- acceptance tests;
- new versioned output paths.

Do not provide polished replacement prose unless the producer has failed the same repair twice.

Do not force the producer to preserve the reviewer's proposed interpretation. State the
evidence problem and acceptance test. If the reviewer supplied a frame such as “evidence
pollution” or “direct exchange,” require the producer to re-prove it from source and allow
it to reject the frame. Reviewer suggestions are hypotheses, not privileged evidence.

## Audit Dispositions

- `KEEP`: evidence and structure stand.
- `REWRITE`: valuable event, invalid formulation.
- `MERGE`: same event identity.
- `DOWNGRADE`: useful note, below card threshold.
- `DELETE`: fails entry threshold.
- `ESCALATE`: requires broader evidence or higher reasoning.

## Final Method

```markdown
## <method name>

**Definition**

**Applicability**

**Operating steps**

1.
2.
3.

**Evidence**

- `<card-id>` / chapters:
- `<card-id>` / chapters:

**Underlying mechanism**

**Real-world transfer**

**Failure boundaries**

**Counterexample**
```

If fewer than two independent event nodes support the mechanism, label it `one-off tactic`
instead of a stable method.
