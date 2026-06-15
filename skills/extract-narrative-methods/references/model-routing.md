# Model Routing

How to spend reasoning. Cheap models read; expensive models judge and converge.
This is a living file: re-confirm the table after each batch with real cost
numbers, not impressions.

## Roles

| Executor | Does | Does NOT |
|---|---|---|
| Scripts | Chapter split, coverage scan, boundaries, quote-length, field completeness, exact-quote lookup, duplicate flags | Any semantic judgment |
| Map model / mini | Event recall, evidence tables, result marking, format skeleton, coverage-table draft | Decide if a B card stands; final A/B routing |
| DeepSeek Pro | First-pass candidates for locally hard cards only | Take a few hundred chapters in one pass; sign anything |
| Codex medium | Second-pass review, A/B keep-cut, causal audit, dedup, rewriting, rule filing | Whole-book clustering, final method naming |
| Codex high | Cross-chunk synthesis, method induction, counterexamples/boundaries, hard adjudication, skill definition | Per-chapter transcription, format fixes, obvious-error cleanup |

## Routing principles

- Mechanical work goes to scripts first, then mini. Never spend a judging model
  on something a regex settles.
- Use Pro only when the six questions are hard to close, causality is genuinely
  tangled, or a cross-chapter read is needed inside one chunk.
- Medium reasoning only touches already-formed artifacts; it is not for
  hole-filling rewrites of an empty draft.
- High reasoning is for endgame convergence only, never for daily batch
  production.
- Validation order: field/format → quote existence → semantic standing. Stop
  early on the cheap checks.

## Measured findings (validated run)

- `chunk_002–012` candidate density and loop quality were clearly higher than
  `chunk_013–019`. The later half produced "several events in one frame"
  chapter-summary cards that had to be downgraded or re-extracted.
- **`0 error / 0 warning` does not predict semantic acceptance rate.** It only
  means fields parse. Several mechanically clean chunks were chapter summaries.
- mini is good for evidence tables and format skeletons but **must not decide
  alone whether a B card stands.**
- DeepSeek Pro degraded under long batches in the validated novel: complete first
  chunk → compressed self-check second chunk → high-speed overview third chunk.
  Use one ~30-chapter chunk as the conservative starting point for a similar
  Chinese novel, then recalibrate. Prompts cannot expand the host's per-run time,
  context, or tool budget.
- For continuous multi-chunk production, set a semantic-decay threshold: if two
  consecutive chunks have over half their cards missing a single key action,
  stop batch card-making and fall back to the evidence layer.
- Medium review should spot-check every 2–3 chunks, not wait for the whole book,
  or summary-style cards accumulate undetected.
- The validated run did not expose reliable token counts. Treat its routing
  conclusions as quality observations, not a token-price benchmark. Record real
  input/output tokens when the next host exposes them.

## Why Opus for the skill write-up (worker side)

The book itself is extracted by Codex (production track). The skill is written by
Claude (research track), and the split mirrors Codex's own medium/high routing:

- **Sonnet** does the bulk: reading audits and the ledger, splitting rules into
  rules vs. samples, building the positive-example set, drafting the rubric and
  templates, tabulating cost data. All read-classify-rewrite over material
  Codex already judged.
- **Opus** does two convergence points only: (1) the final `model-routing`
  cost-based split across all chunks, and (2) rule dedup and `SKILL.md` lockdown
  — one whole-book consistency pass so the separately drafted references can't
  contradict each other.
