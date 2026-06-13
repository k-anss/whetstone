# Output format: the export is the product

Load this when writing the record assembly and the export area.

The tool's endpoint is not "data stored" — it is "data handed cleanly to the
next step": pasted into an agent, parsed by a script, read by a person. The
export channel is the whole point; everything else is scaffolding around it.

## One real record

```
===
[ITEM-NN] {item title}
date: YYYY-MM-DD
project: {project}
recorder: {recorder}
---
{field 1 name}: {value}
{field 2 name}: {value}
---
notes: {omit this line if empty}
photos: [{filenames; omit line if none}]
===
```

(The common-header lines — date/project/recorder above — mirror whatever the
spec's common header defines. The spec may override this whole layout; spec
wins.)

## The two empty records (never one)

**[Nothing happened]** pressed:

```
===
[ITEM-NN] {item title}
date: YYYY-MM-DD
project: {project}
recorder: {recorder}
---
nothing happened
===
```

**[Not checked / unsure]** pressed:

```
===
[ITEM-NN] {item title}
date: YYYY-MM-DD
project: {project}
recorder: {recorder}
---
not checked (occurrence unknown)
===
```

*Why two formats:* a downstream parser must be able to split "truly none"
from "nobody looked" without human judgment. One merged "no data" line forces
the analyst to guess, and both guesses are wrong somewhere: absence read as
zero understates, zero read as absence sends someone to re-check what never
happened.

## Separators and parsing affordances

- Records separated by `===` — **including a trailing `===` after the last
  record**, so a `split("===")` downstream needs no special-casing.
- The `<pre>` preview uses a monospace stack — a visual cue that this text is
  for machines next, not prose.
- **No commentary in the export.** No "data collected above", no totals, no
  signatures. The export contains records, nothing else.

## Export controls

- **Copy all** — writes the full text to the clipboard; button flips to
  accent color and reads "Copied" for 2 seconds.
- **Download .txt** — filename `collect_{date}_{project-slug}.txt`.
- **Clear** — the only confirm in the tool: "Clear all N records?".

## Storage

- Records persist in `localStorage` under `K_form_records_{spec-slug}`;
  survive refresh; die only by explicit Clear.
- The header persists separately (`K_form_header_{spec-slug}`) so tomorrow's
  session starts pre-filled.
