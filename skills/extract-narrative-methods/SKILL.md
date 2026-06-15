---
name: extract-narrative-methods
description: Build and run an auditable multi-model workflow that extracts reusable decision, negotiation, and management methods from long narrative texts. Use when Codex needs to divide a novel, biography, history, case collection, or other long-form narrative into chunks; route work between a cheap map model and stronger reasoning; audit evidence and quotes; keep improving constraints across chunks without bloating the prompt; reduce accepted cases into a traceable methodology; or reuse the same extraction system on a new book.
---

# Extract Narrative Methods

A long narrative carries reusable methods — how a weak actor negotiates, how a
manager allocates power — buried inside plot. This skill runs an auditable
pipeline that turns those into a traceable methodology, and treats the source
book as three things at once: **a deliverable, a training set, and a regression
suite for the workflow itself.**

Two roles own the work:

- **Codex** owns the workflow and is the final evidence judge. It routes work
  between a cheap map model and stronger reasoning, audits against source, signs
  cards, and decides the final methodology.
- **A cheap map model** (DeepSeek Pro, Codex mini, or similar) does bulk reading
  and first-pass cards. **It never declares its own output accepted.**

This skill was validated end-to-end on a 556-chapter novel (《孺子帝》): 19 chunks,
~1.9M characters, reduced through R1–R5 to 8 stable methods across two lines. The
constraints below come from that run; batch capacity remains a project-specific
calibration result, not a universal constant. See
[references/model-routing.md](references/model-routing.md) for measured findings.

## Two Tracks, Run In Parallel

**Production track** — finish the book.
**Research track** — turn every audit finding into a reusable rule, sample, or
cost number, so the next book is cheaper and the workflow stops repeating
mistakes.

The single most important rule of the research track: **when an audit finds a
problem, do not paste a new sentence into the long prompt.** Route it (see
"Improve Constraints"), and keep one positive and one negative sample so a later
prompt edit can't fix one error while reintroducing another. The first run's most
expensive lesson — batching silently degrades reading mode — now lives as a stop
threshold and a regression sample, not as prose in the producer prompt.

## Start A Project

1. Run `scripts/init_project.py <analysis-dir>`.
2. Identify the source text, chapter markers, target lines (e.g. weak-side
   negotiation `A`, management `B`), and expected outputs.
3. Run `scripts/split_source.py <source> <chapter-dir>` or provide a project-specific
   splitter. Verify chapter count and continuity before production.
4. Only load the current chunk's source slice into a producer.
5. Freeze a project contract (source path, chunk boundaries, line definitions,
   schemas, model routing, current rule version). Store source-specific choices
   in the project, never in this generic skill.
6. Keep tests and legacy outputs outside `analysis/cards`.
7. Read [references/workflow.md](references/workflow.md) before designing the
   first producer prompt.

If adapting an existing project, inspect its current cards, audits, failed
tests, cost record, and rule history **before** changing anything. Trust the
artifacts' real state over a stale progress table.

## Run One Chunk — Four Layers

Each chunk passes four layers in order. A layer never starts before the previous
one closes. Mechanical validity is not semantic acceptance.

**Self-use disposition rule (overrides any "auto-delete / auto-stop / re-run"
wording anywhere below).** No layer and no script ever deletes, downgrades,
rejects, or re-runs a card on its own. Every gate is a **marker, not a judge** —
it attaches a disposition or pushes an item onto the human review list, and the
human (who has read the book several times) decides what to actually do. The only
hard stop is a true parse failure (missing field, unreadable file) that would
crash a downstream script — that is mechanical, not judgment. Re-running a chunk
is always a human decision: by default every chunk runs exactly once and the
markers are read afterward.

1. **Evidence layer** — chapter-by-chapter events, source evidence, result
   state, boundary record. No method claims yet. Mechanical checks are scripted.
2. **Candidate layer** — generate `A`/`B` card candidates from the evidence.
   Every card must answer **actor · dilemma · action · counterpart response ·
   cost · result**. **No closed loop → downgrade to an event, never force a
   card.** ("本块无合格A线卡" is a correct, expected output.)
3. **Review layer** — Codex medium reasoning audits every candidate against
   source and **marks** (never deletes): causal inflation, duplicate splitting,
   A/B misrouting, result overstatement. Every finding becomes a disposition tag
   carried into the human review list, not an automatic removal. Low-risk
   formatting is left to scripts.
4. **Synthesis layer** — **only after the whole book is done**: cross-chunk
   dedup, stable methods, applicability and failure conditions, counterexamples,
   character-capability arc. This is the only layer that uses high reasoning.

Treat all producer output as `raw`. Require an event audit, candidate cards, and
a self-check. Title scans, framework drafts, and placeholder prose are marked
incomplete (a real parse-level placeholder is the one mechanical hard stop). Run
`scripts/validate_cards.py` with `--production`, the assigned chapter range, the
source, events, and self-check; do not use the cards-only shortcut to sign a
chunk. The validator now reports three tiers: **ERRORS** (true parse failures
only — missing field, unreadable file, unparseable card — these still block
because a downstream script would crash); **WARNINGS**; and **REVIEW** (the human
review list). The validator's job is anti-fabrication and field parsing, nothing
more:

- It does **not** require quotes to be verbatim. The `关键原句` field may be
  paraphrased, truncated, or differ in punctuation — it is for meaning, not proof.
- Fabrication is checked by a separate short **定位锚** (6–15 chars) that must be
  `grep`-able in the assigned slice. If the anchor is not found, the card goes to
  **REVIEW** — it is **not** rejected and the chunk is **not** re-run. Prefer
  false positives (you dismiss them in three seconds) over false negatives.
- Chapter coverage, self-check length, event-density, and stop thresholds are now
  **REVIEW markers**, never automatic stops. Use `--evidence-source` when the book
  does not use `第X章` headings.

Then audit semantically. Dispositions are `KEEP`, `REWRITE`, `MERGE`,
`DOWNGRADE`, `ESCALATE`, `DELETE` — but in self-use these are **recommendations
the human acts on**, not actions the reviewer takes unilaterally. Default
disposition for any semantic/depth concern is `ESCALATE` (mark, send to human),
not `DELETE`. When the human decides a card needs source re-extraction, rebuild
it from events and evidence — do not preserve the old title, route, or count; one
old card may yield zero, one, or several new cards. Only Codex writes or approves
files in `analysis/cards`; never silently overwrite v1.

Read [references/quality-gates.md](references/quality-gates.md) and
[references/extraction-rules.md](references/extraction-rules.md) for entry
thresholds, [references/review-rubric.md](references/review-rubric.md) for the
audit checklist, and [references/templates.md](references/templates.md) when
building prompts. Card and self-check shapes live in [assets/](assets/).

## Mark Depth Decay — Don't Auto-Stop

The validated run showed silent degradation under batch load: the first chunk
was complete, the second compressed its self-check, and the third dropped to a
title scan. Start conservatively at **one calibrated chunk per run**. Increase
batch size only after a project-local test.

These depth signals are now **REVIEW markers**, not automatic stops or re-runs.
The validator flags them; the human reads the flags and decides whether to补挖 or
move on. By default the chunk still ran once and is kept:

- self-check under ~10 lines, or missing its chapter-coverage table;
- any phrase like 高速概览 / 标题扫描 / 框架初稿 / 批量初稿;
- a chunk's event density visibly below the previous one.

A real parse-level placeholder file (empty chapter, "本块……待补" stub) is the one
exception that still blocks, because it is malformed, not merely shallow. Do not
*generate* placeholder files for chunks you could not finish — stop after the last
complete chunk and tell the human. Spot-audit every 2–3 chunks rather than waiting
for the whole book; this spot-audit is the depth net, and it is the human's call.

Run the bundled regression suite after changing templates, rules, or the
validator:

```bash
python3 -m unittest discover -s tests -v
```

## Improve Constraints — Route, Don't Append

After every audit, for each distinct failure:

1. **Decide if it is reusable.** One-off text issue → fix that card only.
   Recurs ≥2 times → make a rule. Can corrupt a quote, fact, event identity, or
   final count → hard rule immediately.
2. **Choose where it lives.** Machine-checkable → validator script. Needs
   semantic judgment → [review-rubric](references/review-rubric.md). Hard to
   describe but easy to imitate → a positive/negative sample pair. **Do not keep
   pushing rules into the main prompt.**
3. **Keep a regression sample.** One correct case + one failure case per
   important rule in `analysis/meta/regression`. Re-run them after any rule edit.
4. **Record cost.** Per chunk: model, input length, card count, error count,
   repair count.

Both 3 and 4 are detailed in
[references/regression-and-cost.md](references/regression-and-cost.md). Log each
failure family in [references/error-ledger.md](references/error-ledger.md).
Version the rule set; review and merge rules every three accepted chunks; retire
rules subsumed by a broader one. Constrain unsupported inference, never prescribe
conclusions or a fixed card count.

## Model Routing

Measured roles from the validated run (detail in
[references/model-routing.md](references/model-routing.md)):

| Work | Executor |
|---|---|
| Chapter split, coverage scan, boundaries, field/quote checks | scripts |
| Event recall, evidence tables, result marking, format skeleton | map model / mini |
| First-pass A/B candidates | map model (Pro for locally hard cards only) |
| Card keep/cut, causal audit, dedup, rewriting | Codex medium |
| Cross-chunk synthesis, methods, counterexamples, boundaries | Codex medium→high |
| Whole-book design, hard adjudication, skill definition | Codex high |

Never use a light model for final A/B routing, causal structure, motive, method
stability, or acceptance. `0 error / 0 warning` from the validator does not
predict semantic acceptance — it only means fields parse.

## Reduce Accepted Cards

Read only signed cards. Assign one stable event ID per independent situation;
merge continuations and duplicate perspectives **before** counting method
frequency — multiple cards for one event are one evidence node, not several.
Cluster by underlying decision mechanism, not plot topic. Require independent
contexts, counterexamples, boundaries, and failure modes. For limited-goal
actions, require an unreachable original goal, a replacement target, observable
success criteria, and a stopping rule. Keep every final principle traceable to
accepted cards and source locations. Escalate to high reasoning when a conclusion
spans ≥3 chunks, compares many cards, changes event counts, or enters the final
methodology. See [references/workflow.md](references/workflow.md) §Reduce.

## Tag Every Rule: [method] or [adapt]

Each rule in this skill — in the quality gates, the review rubric, the validator
config — carries one of two tags, so the layer that is universal can be told apart
from the layer that merely accommodates one model's quirks.

- **`[method]`** — true of *any* model extracting *any* novel: a closed exchange
  needs offer + concession + causal link + observable response; cost must be
  borne by the focal actor; explicit narration outranks inference. These are the
  real judgment crystallized from reading.
- **`[adapt]`** — there only to work around a specific model or Chinese-text
  quirk: the 6–15-char anchor length, the chapter-number regex, the placeholder
  phrase list, "Pro for locally hard cards only". These name a model by behavior.

Discriminator: *"Would this rule still hold if I swapped the model or the book?"*
Yes → `[method]`. It mentions DeepSeek's / mini's behavior, or a punctuation/格式
fix → `[adapt]`.

Why now, in self-use: both tiers are active and you obey both. The tag is the
**escape hatch for later** — when this becomes a product, you re-examine only the
`[adapt]` layer (it may be wrong for the next model) and keep `[method]` intact.
登楼撤梯：`[adapt]` is the ladder, tag it now so it can be pulled cleanly later.

## Reuse On Another Book

Keep the workflow, four layers, quality gates, validator, rule lifecycle,
regression mechanism, cost record, and generic schemas — i.e. keep the `[method]`
layer. Replace the `[adapt]` layer: chapter parser and chunk size; project lines
and entry thresholds; role-specific terminology; candidate method labels;
source-specific examples and accepted conclusions.

Start the new book with a calibration chunk. Do not copy accepted conclusions or
character assumptions from an earlier book. **Blind test:** after the methodology
is built, extract two chunks of a book that never shaped any rule and check
whether the gates and routing hold. Schedule this separately — it is research
spend, not deliverable spend.
