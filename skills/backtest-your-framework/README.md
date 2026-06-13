# backtest-your-framework

Don't ask the AI if your framework is good — it will agree.
Freeze its context and let history grade it.

A skill that turns framework validation into a blind experiment. You
bring a judgment framework (an investment screen, a hiring rubric, a
risk score — any rule-based decision system) and historical cases whose
outcomes you know. The skill enforces a protocol under which the AI
judges each case with its context frozen at time T, commits the
judgment, and only then sees the truth.

## Why this exists

Two failure modes wreck almost every attempt to validate a framework
with an AI:

1. **Optimistic agreement.** Asked for an opinion, the model answers
   from inside your optimism. The praise is fluent and worthless.
2. **Training-data cheating.** Famous cases carry their endings in the
   model's weights. A recognizable name flips the judgment from forward
   reasoning to backward rationalization — invisibly.

Plenty of red-team and evaluation prompts exist. Almost none turn these
two self-deception sources into an enforced experimental protocol. This
one does.

## Before / after

**Without the skill** — "Is my opportunity screen any good?"

> The model critiques the design, suggests two extra criteria, says the
> overall structure "looks solid." No case was tested. Nothing was
> learned.

**With the skill** — same question:

> The model declines to grade by opinion. It walks you through case
> design (freeze time, renaming, neutral description), echoes the
> desensitization checklist for confirmation, runs a committed blind
> judgment with confidence numbers and failure modes, then compares
> against the revealed truth and files the result into a bias table.
> If it catches itself knowing the ending, it aborts and tells you.

## What's inside

```
SKILL.md            the map: three load-bearing stances, workflow gate,
                    failure behavior (zh twin: SKILL.zh.md)
reference/
  three-laws.md     time freeze / outcome isolation / judge-before-reveal
  protocol.md       the five-phase procedure with deliverables
  anti-cheating.md  the two self-deception sources, plus user-side leaks
  bias-table.md     consolidation template across cases
examples/
  sample-case.md    one fully fictional run, end to end
```

All files have `.zh.md` twins.

## Install

```
git clone https://github.com/k-anss/whetstone
cp -r whetstone/skills/backtest-your-framework ~/.claude/skills/
```

Or copy the folder anywhere your agent loads skills from.

## Scope

For judgment-type frameworks only. Not for quantitative strategy
backtests over price data, and not for domains without reliable
historical cases.

## License

MIT. Author: K ([@k-anss](https://github.com/k-anss)).
