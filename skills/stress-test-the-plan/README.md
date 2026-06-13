# stress-test-the-plan

Discussing your plan makes you overrate it — and the AI will agree with
you. This runs the opposite role: find where it dies.

## What it does

A red-team role for decisions and plans. It interrogates in three holes:

1. **Fatal flaw** — the single point that takes the project to zero,
   not a secondary risk.
2. **Hidden assumptions** — "users will pay", "I can sustain six
   months": labeled as assumptions, each with a verification cost.
3. **Multi-round failure** — even if round one works, how it decays at
   1 / 3 / 6 months.

No comfort, no rubber-stamping. Deliberately pessimistic.

## What makes it different

Not the interrogation — a bare model challenged to "find the holes"
does most of that. The increment is boundary discipline:

- **It refuses to run when you are in emotional distress.** A stress
  test on a bad day is harm, not help.
- **It will not relitigate a live project.** If you are already
  executing, it only asks "how to die less", never "should you have".
- **It declares its own bias, every run.** The closing line is fixed:
  this is the pessimistic extreme; take the real judgment between this
  and a normal read.
- **It exits when told.** "Stop" means the role drops in the same turn,
  completely.

## Demo

Input: a plan to sell AI-assisted document services to local small
businesses through a marketplace listing.

Output (abridged — full run in `examples/sample-stress.md`):

```
## Fatal flaw
The listing assumes inbound demand exists on the platform; if nobody
searches for this, everything downstream is unreachable.

## Hidden assumptions
1. Buyers can tell your output from cheaper competitors' — verification:
   3 listings, 2 weeks, compare inquiry quality.
...

This is the deliberately pessimistic extreme. Take the real judgment
between this and a normal read.
```

## Install

Copy `stress-test-the-plan/` into your agent's skills directory. The
agent loads `SKILL.md` on trigger and pulls `reference/` files as
needed.

## License

MIT.
