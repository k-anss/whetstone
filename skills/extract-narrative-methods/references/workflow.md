# Workflow

This is the detailed mechanics behind SKILL.md. The four layers named there map
onto the chunk loop below: **evidence layer = P1 map**, **candidate layer = the
card portion of P1**, **review layer = P2 validation + P3 audit + P4 repair**,
and **synthesis layer = Reduce**. "Four layers" is the conceptual split; "P1–P5"
is the per-chunk procedure.

## Contents

1. Project contract
2. Calibration
3. Chunk loop
4. Constraint learning
5. Reduce
6. Project state

## 1. Project Contract

Freeze these items before production:

- source file and encoding;
- chapter locator and verified chapter count;
- chunk boundaries;
- extraction lines and their entry thresholds;
- card schemas;
- result-state enum;
- evidence levels;
- quote policy;
- model responsibilities;
- output directories;
- active rule-set version.

Store source-specific choices in the project. Do not place them in the generic skill.

## 2. Calibration

Choose one difficult, representative chunk. Run the entire loop before opening the next chunk.

Calibration passes only when:

- no fabricated or normalized quote survives;
- no hypothesis is stated as motive or fact;
- incomplete action is not marked complete;
- event duplication is controlled;
- producer self-check catches major risks;
- audit rewrite/delete rates are tolerable.

If calibration fails, update rules and rerun the same chunk from raw source. Keep failed outputs as tests, not evidence.

If the user explicitly ends calibration without another repair, mark the sample
`calibration`, exclude it from signed cards and reduction, and make the next chunk the
first signable production block under the updated rules.

## 3. Chunk Loop

### P1 Map

Producer reads only the source slice, project prompt, and active rules. It outputs:

- event audit, including rejected events and reasons;
- chapter-by-chapter coverage, linking every assigned chapter to event IDs or a documented
  transition with no independent major event;
- candidate cards;
- uncertainty and self-check report.

The producer cannot read legacy cards unless the task is explicit repair.
If it cannot complete another full chunk, it stops after the last completed chunk and
must not create title-scan summaries, generic framework cards, or placeholder files.

### P2 Mechanical Validation

Run the full production gate:

```bash
python3 scripts/validate_cards.py raw/chunk_NNN_A.md raw/chunk_NNN_B.md \
  --source source.txt \
  --events raw/chunk_NNN_events.md \
  --selfcheck raw/chunk_NNN_selfcheck.md \
  --chapter-start X --chapter-end Y \
  --production \
  --previous-event-count N
```

For a source whose headings are not `第X章`, pass a pre-sliced chunk with
`--evidence-source chunk_NNN_source.txt` instead of `--source`. Card and coverage
chapter fields should still use normalized integer chapter numbers.

This checks:

- card and event chapter bounds;
- required six-question fields;
- IDs and cross-file card duplicates;
- result enums;
- quote length and exact occurrence inside the assigned chapter slice;
- placeholder and pending-detail markers;
- complete chapter coverage for the assigned range;
- minimum self-check length and actual last chapter;
- empty-quote and event-density stop thresholds.

Mechanical success does not imply semantic acceptance.

### P3 Semantic Audit

Codex reads source, raw outputs, self-check, and validator report. For every card:

- verify actor, chronology, decision, result, cost, quote, and line routing;
- separate fact, strong inference, and hypothesis;
- compare against rejected events for recall;
- assign a disposition.

### P4 Repair

Use targeted repair when the event is valuable but the card is structurally wrong. Give the producer exact failure classes and acceptance tests, not the desired prose or hidden answer.

Preserve `v1`, write `v2`, and compare.

### P5 Sign

Only Codex writes or approves files in `analysis/cards`. Record rule version and audit path.
Never sign from a cards-only validator run; signing requires `--production`.

## 4. Constraint Learning

For every new error:

1. Capture the concrete failure.
2. Name its failure family.
3. Identify the violated invariant.
4. Decide `observe`, `candidate`, `hard`, or `retired`.
5. Add a detection question.
6. Add examples only when wording is subtle.

Use this promotion policy:

| Severity | Recurrence | Action |
|---|---:|---|
| Corrupts quote, fact, event identity, or final count | 1 | Hard rule |
| Corrupts motive, cost, causality, or result | 1 | Candidate; hard after another independent occurrence |
| Formatting or style only | Any | Validator/audit check |
| Covered by a broader active rule | Any | Retire/merge |

Review the constraint set every three accepted chunks. Remove redundancy and check whether added rules reduce useful recall.

After modifying rules, templates, or validator behavior, run:

```bash
python3 -m unittest discover -s tests -v
```

## 5. Reduce

Reduce only signed cards:

1. Build a compact ledger.
2. Resolve event identity and long arcs.
3. Merge obvious duplicates.
4. Cluster by mechanism.
5. Validate candidate methods with independent contexts.
6. Add counterexamples and boundaries.
7. Write final methods with source traceability.

Frequency without event deduplication is invalid.

### R1 Ledger

Create a compact inventory with card ID, source location, actor, constraint, central action,
response, result, cost, and route. Treat it as an index, not a method declaration.

### R2 Deduplicate And Re-extract

- Remove duplicate A/B perspectives when actor, action, response, and result are the same.
- Downgrade chapter summaries, principles, role authority, and literary reflection.
- Re-extract valuable but malformed cards from source events. Do not edit the old summary
  into shape. The replacement count may differ from the old count.

### R3 Cluster

- Cluster by causal mechanism, not setting or management topic.
- Assign each accepted card one primary cluster for accounting.
- Keep failed cases as boundary evidence, not positive frequency.
- Count independent event nodes rather than cards.

### R4 Validate

For each candidate method require:

1. at least two independent contexts;
2. a non-routine central action;
3. an observable response;
4. a paid cost or meaningful tradeoff;
5. a deletion test showing why the action mattered;
6. explicit applicability and failure boundaries.

Keep clear but single-context mechanisms as one-off tactics.

### R5 Write

For every stable method include:

- definition;
- applicability conditions;
- operating steps;
- two or more traceable examples;
- underlying mechanism;
- real-world transfer;
- failure boundaries;
- linked counterexample where available.

Keep the case library separate from the method library so evidence can be audited without
loading the full analysis.

## 6. Project State

Recommended states:

`todo → raw → validating → reviewing → repairing → accepted`

Use `calibration` for a closed, non-signable calibration sample. Use `escalated` when
resolution needs cross-chunk evidence or higher reasoning.
