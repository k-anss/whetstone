# Interaction: skeleton, the three buttons, validation

Load this when building the page structure and behavior.

## Fixed skeleton (every tool looks like this)

```
[Top fixed area]
  Title + one-line subtitle (from the spec; if none, omit the subtitle)
  [Common header]: shared per-session fields (e.g. date / project / recorder)
    — collapsible panel, expanded on first open, auto-collapses once its
      required fields are filled; collapsed state shows a one-line summary
      ("2026-06-12 · Project A · R1"); click to re-expand and edit.
    — persisted in localStorage; refilled on next open.

[Module tab bar] (sticky below the header)
  Module 1 | Module 2 | …
  Active tab: accent underline. Switch transition ≤150ms, nothing fancier.

[Item cards of the active module]
  ┌─ Item NN · title ────────────────────────────────┐
  │ field 1: [input]                                  │
  │ field 2: [select]                                 │
  │ …                                                 │
  │ [Nothing happened] [Not checked / unsure] [Add]   │
  └───────────────────────────────────────────────────┘

[Output area] (sticky bottom, collapsed by default)
  collapsed: "▾ N recorded · expand"
  expanded: <pre> structured text </pre>
            [Copy all] [Download .txt] [Clear]
```

## The three buttons (the heart — semantics are load-bearing)

Each item card ends with exactly three buttons. Two record an *absence of
data*, and they are **not interchangeable**:

**[Nothing happened]** — the event genuinely did not occur this round
(e.g. "no teardown today on this step").
- Appends a `nothing happened` record (format in `output-format.md`).
- Card shows status "Recorded: nothing happened"; its fields disable.
- A 5-second **Undo** is offered; undo re-enables the fields.

**[Not checked / unsure]** — the event may have occurred, but this person did
not check / does not know.
- Appends a `not checked (occurrence unknown)` record.
- Same disable + 5-second undo behavior.
- Both no-data buttons are visually secondary (muted text color); they must
  not compete with [Add].

**[Add to output]** — a real record.
- Validates required + conditional-required fields first. Failures: warning
  border on each missing field + one notice bar at top: "N required fields
  missing" (auto-dismiss 3s). No alert(), no modal.
- On pass: assemble the record per the spec's output rules, append to the
  output area, show "Recorded · {first text field's value}" on the card, then
  **clear the fields** — the same item may be recorded several times a day.

Never add other buttons. No "save draft", no "share", no "upload".

## Why the two no-data states cannot merge

One button means downstream parsing receives one symbol for two different
facts. Missing read as zero understates; zero read as missing triggers false
re-checks. The split must happen **at entry time** — it is unrecoverable
later. This is the skill's reason to exist; if a spec asks you to merge them,
stop and report (failure behavior, see SKILL.md).

## Errors

- One top notice bar, text like "3 required fields missing", number in accent
  color, auto-dismiss in 3 seconds.
- No popups, no alert/confirm — with one exception: [Clear] asks once,
  "Clear all N records?", buttons laid out to avoid mis-taps.
- Unfilled required fields: warning-color border; restores on focus.

## Persistence

- `localStorage` only. Keys:
  - header: `K_form_header_{spec-slug}`
  - records: `K_form_records_{spec-slug}`
- Refresh keeps everything; only explicit [Clear] erases records.
- No server, no sync, no export besides copy/download.
