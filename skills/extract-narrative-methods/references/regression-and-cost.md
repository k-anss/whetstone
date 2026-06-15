# Regression Samples & Cost Record

The research track's two ledgers. Together they keep the workflow from
regressing and let you route models by data instead of feel.

## Regression samples

Goal: a rule edit must not fix one error while reintroducing another. Every
important rule keeps a minimal correct case and a minimal failure case. After
any rule edit, re-run the samples.

Layout in `analysis/meta/regression/`:

```
Rxx_positive.md   one correct case, minimal context, with a source/card ref
Rxx_negative.md   one wrong way to write it, the problem, the disposition
Rxx_note.md       the rule in one line + the decision order to apply it
README.md         index: which Rxx covers which rule
```

Placement rules:

- At least one positive and one negative per important rule.
- Keep only the minimal context. The sample set must not turn into a second copy
  of the rule book.
- A sample belongs here only when the rule is **hard to state but easy to
  imitate** — otherwise the rule lives in the validator or the rubric, not here.

Worked examples from the validated run (these are the actual samples that
exist — reuse their shape, not their content, on a new book):

| Sample | Rule it guards |
|---|---|
| `R11` | Key-quote field must exist (may be empty, never fabricated). |
| `R13` | A chapter summary cannot become a method card. |
| `R16` | Source re-extraction does not inherit the old card's title/route/count. |
| `R17` | A limited-goal action needs explicit success and stop conditions. |
| `R18` | One event's multiple cards are one evidence node, not several. |

`R13_note` shows the canonical decision order for an imitable rule: (1) is there
one main dilemma; (2) one key decision; (3) an observable counterpart/system
response; (4) a concrete cost already paid. Any core item missing → keep as event
material or re-extract from source.

The skill also contains executable validator regression tests in `tests/`.
Run them after changing the validator, templates, or field names:

```bash
python3 -m unittest discover -s tests -v
```

## Cost record

One row per chunk and per reduce stage, in `analysis/meta/成本记录.md` (or
`cost-record.md`). **Record the structure first, fill numbers as measured, never
guess.** A blank cell is honest; an invented token count corrupts the only data
that can answer "which model is cheapest for which step."

Columns:

```
chunk | stage | model | input_tok | output_tok | events | A | B
      | validate_errors | validate_warnings | repairs | status | note
```

Notes from the validated run:

- Many `input_tok`/`output_tok` cells stayed blank because the host UI did not
  expose them. That is acceptable — the qualitative columns (events, cards,
  errors, repairs, status) still drove the routing conclusions in
  [model-routing.md](model-routing.md).
- The reduce stages (R1 ledger → R2 dedup/re-extract → R3 clustering → R4 method
  validation → R5 final + fact-check) each get a row too, marked with the
  reasoning tier used, so the high-reasoning spend is visible and bounded.

## How the two feed the skill

After the book closes, these two files are the raw material for refining the
generic skill: regression samples become the worked examples in
[review-rubric.md](review-rubric.md) and [error-ledger.md](error-ledger.md); the
cost record becomes the measured-findings section of
[model-routing.md](model-routing.md). Keep them project-local; lift only the
shape and the generalized lesson into this skill.
