# Skill Field-Test Log

> Purpose: while field-testing third-party skills inside real projects, record
> the test facts on the spot and export structured text for later review
> writing and archival parsing.
> This table is the demo input for `missing-not-zero`; `demo.html` is the tool
> assembled from it.

## Common header

| Field | Type | Rule |
|---|---|---|
| Date | date | required |
| Project | text | required |
| Recorder | text | required |

## Module 1 · Test runs

### ITEM-01 · One test run

> The same skill may be tested several times a day — one record each. A query
> that *should* have triggered but didn't is also filed here (it counts as a
> failed run).

| Field | Type | Rule |
|---|---|---|
| Skill name | text | required |
| Source (repo/link) | text | |
| Test input summary | textarea | required |
| Behavior without skill | textarea | |
| Behavior with skill | textarea | |
| Verdict | select [keep/patch/drop/pending] | required |
| Patch notes | textarea | conditional required: verdict = patch |

## Module 2 · False-trigger checks

### ITEM-02 · Negative case

> This module records only queries that should NOT trigger. "Should have
> triggered but didn't" belongs to Module 1.
> (Attribution rule stated explicitly — this is the ambiguity gate at work.)

| Field | Type | Rule |
|---|---|---|
| Query that should not trigger | textarea | required |
| Did it trigger | select [no/yes/unclear] | required |
| Note | textarea | |

## Output rules

Skill defaults (see `reference/output-format.md`): `===` separators including
a trailing one; two distinct empty-record formats (nothing happened / not
checked).
