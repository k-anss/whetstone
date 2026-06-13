# Worked Example: One Full Backtest Run

**Everything below is fabricated for demonstration.** The product, team,
dates, and outcome are invented. This is deliberate and doubly so: the
example must not leak any real test material, and outcome isolation
(Law 2) requires renamed, blurred cases anyway — so a fictional example
is the protocol demonstrating itself.

The framework under test here is a generic "side-project opportunity
screen": a handful of hard rules that output go / no-go on small
business opportunities. Substitute your own.

---

## Phase 1 · Case card

```
Time anchor: September 2021 (freeze time T)

Actor profile: 2-person team, both employed full-time elsewhere,
~$15k own capital, generalist software skills, ~15 hrs/week combined.

Opportunity (neutral): A subscription meal-planning service for
shift workers (nurses, factory crews) whose schedules rotate weekly.
Existing meal-plan apps assume fixed daily routines. The team has
interviewed 30 shift workers; 22 said current apps don't fit their
rotation. No competitor addresses rotation-aware planning as of T.
Comparable consumer subscription apps in adjacent niches price at
$6–10/month. Acquisition channel assumed: nursing forums and two
Facebook groups (40k combined members).

Test target: the framework's "willingness-to-pay evidence" rule and
its "channel concentration" rule.
```

Desensitization checklist (echoed to the user at the gate):

- Freeze time: 2021-09. No post-T facts in the card. Confirmed.
- Subject renamed: yes (fictional placeholder; in a real run, state
  what the real subject was renamed to — without saying the real name).
- Blurred: founder identities, product name, exact launch geography.
- Kept: capital scale, team profile, interview counts, pricing
  comparables, channel sizes, time window.
- Leading language: case card stripped of adjectives. Confirmed.

User confirms. Search tools off. Proceed.

## Phase 2 · Blind judgment (committed before reveal)

```
Rule-by-rule:

R1 Willingness-to-pay evidence — TRIGGERED (framework rule).
   22/30 saying "current apps don't fit" is a complaint, not a
   payment. Zero pre-orders, zero paid pilots. Rule R1 reads this
   as insufficient.

R2 Channel concentration — TRIGGERED (framework rule).
   Two forums + two groups is a narrow, bannable channel. Rule R2
   flags single-channel dependence.

R3 Time-capacity vs. service load — OWN REASONING (no rule fired).
   A subscription food-adjacent product implies weekly content
   production; 15 hrs/week shared looks thin. This is my inference,
   not a framework rule — the framework has no rule about ongoing
   service load.

Confidence: 70% that this fails to reach sustainable revenue
within 12 months of T.

Expected failure modes, ranked:
1. Conversion: complaints don't convert to $8/month subscriptions.
2. Channel: forum moderation chokes acquisition.
3. Capacity: content treadmill exceeds 15 hrs/week.

Verdict: NO-GO.
No revision ledges. Judgment committed.
```

## Phase 3 · Reveal (fictional truth)

The team launched in November 2021. Free signups were strong (1,900 in
two months) but paid conversion stalled at 1.1%. The forums banned
promotional posts in month three. The team shut down in May 2022,
having spent $9k. However: a competing team that launched with a B2B
angle — selling rotation-aware planning to hospital cafeterias rather
than to individual nurses — reached sustainable revenue in 2023.

## Phase 4 · Comparison

1. Direction: right (no-go; it failed).
2. Confidence: 70% was reasonable given T-knowable facts; arguably
   could have been higher given zero payment evidence.
3. Failure modes: modes 1 and 2 both occurred, in that order. Mode 3
   never got tested. Good match.
4. True intercepts: R1 (payment evidence) and R2 (channel
   concentration) both blocked for the right mechanism.
5. False negatives: none in this case — but note the B2B variant
   succeeded. The framework, as written, had no rule that would have
   surfaced "same need, different buyer" as an alternative. That is a
   coverage gap, not a wrong verdict.
6. False positives: none observable here.

## Phase 5 · Row added to the bias table

| Case | Type | Verdict (AI) | Verdict (truth) | Confidence | Direction right? | Notes |
|---|---|---|---|---|---|---|
| S1 | consumer subscription, complaint-rich / payment-poor | no-go | failed | 70% | yes | R1, R2 true intercepts; coverage gap: no "switch the buyer" rule |

One row. The framework gets no credit yet — that takes several more
cases and a consolidated table.
