# Field mapping: spec markers → HTML, and the ambiguity gate

Load this when translating the spec table into inputs, and **always** before
generating — the ambiguity gate below runs first.

## The cross-module ambiguity gate (runs before any HTML)

Before building, ask of the spec: **could one real-world event plausibly
belong to more than one module?** Walk each pair of modules and imagine the
events the filler will actually meet.

If yes — stop and report. Offer the user two repairs:
1. merge the overlapping modules, or
2. one explicit attribution rule written into the tool's subtitle or the
   item's title (e.g. "file under the module of the *primary* action").

Do **not** pick an attribution yourself and ship.

*Field observation:* one kind of event touched several modules at once;
different fillers chose different modules, downstream per-module counts came
out wrong — and every cell looked "filled", so the error was silent. Silent is
the operative word: this failure produces no error message, ever. The only
place to catch it is here, before the tool exists.

*Boundary:* verified for function/process-organized modules. Timeline- or
object-organized schemes may show different ambiguity shapes — untested; say
so if you meet one.

## Marker → implementation table

| Spec marker | HTML implementation |
|---|---|
| `text` | `<input type="text">` |
| `textarea` | `<textarea>`, 2 rows initially, auto-grows, no max |
| `number` | `<input type="number" min="0">` (integers; min guards negatives) |
| `time` | `<input type="time">` |
| `date` | `<input type="date">` |
| `datetime` | `<input type="datetime-local">` |
| `select [A/B/C]` | native `<select>` — never a custom dropdown |
| `select [A/B/C/other] + text` | select; choosing "other" reveals a text input |
| `multi-select [A/B/C]` | one checkbox per option |
| `required` | label gets accent `*` + required attribute |
| `conditional required` | JS watches the trigger field; dependent field appears only when triggered, and is required from the moment it appears |
| item marked "hidden — not in HTML" | not rendered at all |

## Conditional-required, precisely

"Interruption cause required when interruption length > 0" means:
- the dependent field is **absent** (not just disabled) until the condition
  holds;
- the moment it appears, it is required;
- if the condition stops holding, it disappears and its value is dropped from
  the pending record.

List every conditional pair in your structure-confirmation report (gate 3 in
SKILL.md) — the user must see the logic before it runs.

## What you never do here

- Add a field the spec doesn't define — even one that "obviously should
  exist".
- Extend a select's options — even by one.
- Change a field's type because another "would work better".
- Resolve a spec contradiction by choosing silently. Contradiction → stop and
  report (failure behavior).

Mobile note: inputs at 16px so phone browsers don't auto-zoom; time/date use
native pickers; short fields (time/date/select) may pair two per row, all
others full-width.
