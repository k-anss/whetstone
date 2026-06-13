# Bias Table Template

Use after several cases (5 is a workable minimum). One case proves
nothing; the bias table is where individual runs become a verdict on
the framework.

## Per-case summary rows

| Case | Type | Verdict (AI) | Verdict (truth) | Confidence | Direction right? | Notes |
|---|---|---|---|---|---|---|
| C1 | (e.g. consumer attention play) | no-go | failed | 70% | yes | rule R2 true intercept |
| C2 | (e.g. enterprise relationship-gated) | borderline | succeeded | 55% | partial | hard rules silent; 60–70% own reasoning |
| C3 | (e.g. breakout new category) | no-go | succeeded | 65% | no | rules R1/R5 false negative |

Type labels are abstract case categories, never real names.

## Consolidated findings

### Strengths — where the framework is reliably accurate
Which case types does it call correctly, and which specific rules do
the work there?

### Weaknesses — where it is systematically off
Not "it missed one" but "it misses this *kind*". A miss pattern across
2+ cases of the same type is a weakness; a single miss is noise.

### False negatives — rules that block good cases
List the rule, the case(s) it wrongly blocked, and the mechanism of the
error (e.g. a threshold calibrated for steady-state markets misfires on
breakout categories).

### False positives — rules that wave through bad cases
Same structure.

### True intercepts — rules that earn their keep
Name them explicitly. In revision, these rules get protected; revisions
that would weaken a true intercept need stronger justification.

### Coverage gaps — where rules went silent
Cases where the verdict came mostly from the AI's own reasoning rather
than fired rules. High own-reasoning ratio = the framework lacks rules
for that case type, regardless of whether the verdict happened to be
right.

## Rule-change list

For each proposed change: the rule, the change, the case evidence, and
what could make the change wrong. Changes without case evidence don't
go on this list — that would be redesigning by opinion, which is the
exact failure this whole protocol exists to prevent.

## A note on redundancy

If the framework has layered rules, check whether later layers caught
errors made by earlier ones. Multi-layer redundancy that corrects
single-rule misjudgments is a structural strength — preserve it during
revision rather than "simplifying" it away.
