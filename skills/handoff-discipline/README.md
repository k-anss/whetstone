# handoff-discipline

**A summary loses what the next agent must not re-decide.**

A skill for handing the working state of one AI session to another that
shares no context — without the receiving agent reopening closed
questions, mistaking status for invitation, or silently propagating a
transcription error.

## The difference, side by side

Same messy working notes, handed over two ways.

**Without the skill** (naive summary):

> We're building a skills repo called whetstone under k-anss, MIT
> licensed, bilingual. The current skill is about handoffs. Progress is
> good — structure mostly settled, naming was discussed. Next step is
> writing the reference files.

The receiving agent now believes "naming was discussed" means naming is
open. It cannot tell which facts are constraints. If the handle had been
mistyped, nothing here would catch it.

**With the skill** (three-layer handoff):

> **Pinned (do not reopen):** 1. name `handoff-discipline` 2. repo
> `whetstone`, account `k-anss`, MIT 3. structure: SKILL.md + 3 refs +
> 1 example, EN/ZH twins
> **Status:** brief approved; zero files built.
> **Pending:** README stance sentence — awaiting K.
> **Receipt required:** echo the pinned list verbatim before working.

The receiving agent echoes the pinned list back — a mistyped handle dies
at intake. Pending stays pending. Closed stays closed.

This skill grew out of a real incident: a handle typo crossed a naive
handoff and propagated silently into output, because nothing forced an
item-by-item check. See `examples/filled-handoff.md` for the real
(sanitized) handoff that built this very skill.

## Install

Copy the `handoff-discipline/` folder into your agent's skills directory.
Then ask for "a handoff for the next agent" — the skill triggers on
handoff intent, and stays quiet for ordinary summarization.

## Files

- `SKILL.md` — the map: stance, core actions, fields (`.zh.md` twin)
- `reference/layers.md` — sorting material into pinned / status / rationale
- `reference/template.md` — the handoff skeleton
- `reference/receiving.md` — the receiving agent's protocol
- `examples/filled-handoff.md` — a real, sanitized handoff

MIT · K (`k-anss`)
