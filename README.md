# whetstone

**Domain judgment, encoded as agent-executable discipline.**

A growing collection of skills. Each one takes a discipline I actually use in my
work and writes it so an agent *runs* it — picks the mode, follows the rules,
the same way every time — instead of just reading about it.

> Reread the classics with AI. Stress-test Silicon Valley in a county town.
> Audit my thinking with money.
> — K, building in a Chinese county town, AI-native

## Skills

| Skill | Does |
|---|---|
| [read-not-decorate](skills/read-not-decorate) | Turn a finished markdown long-form into one self-contained HTML built to be read, not decorated. |
| [missing-not-zero](skills/missing-not-zero) | Turn a field-spec table into a single-file HTML data-collection tool that keeps "didn't happen" and "didn't check" as different empty values. |
| [backtest-your-framework](skills/backtest-your-framework) | Validate a judgment framework by backtesting it on real historical cases under an anti-self-deception protocol — let history grade it, not the AI's optimism. |
| [handoff-discipline](skills/handoff-discipline) | Hand off an AI session's working state to one that shares no context — separating what must not be reopened from current status and rationale. |
| [audit-the-hustle](skills/audit-the-hustle) | Read the signals of whether someone online is really making money or performing; report a confidence split, never a verdict. |
| [stress-test-the-plan](skills/stress-test-the-plan) | Red-team a decision: surface its fatal flaw, expose hidden assumptions, trace how it fails. Declares its own pessimism bias. |
| [distill-not-transcribe](skills/distill-not-transcribe) | Turn a written method into a skill that encodes the author's judgment, not just steps. Refuses material that has no judgment. |
| [report-deck-zh](skills/report-deck-zh) | Build Chinese work-briefing slides in the structural grammar of formal Chinese reporting — parallel titles, whole-part-whole, caliber captions. Structure only. |
| [strip-the-ai-voice](skills/strip-the-ai-voice) | Strip the "AI voice" from Chinese text by deletion, not rewriting, using a concrete delete-test. |

Two of these are adaptation-line skills and say so in their own docs:
`report-deck-zh` derives from frontend-slides; `strip-the-ai-voice` is the
opposite direction of a humanizer. Lineage is declared, not hidden.

## Install

Pick one:

- Clone the whole collection.
- Point your agent at a single skill folder, e.g. `skills/read-not-decorate`.
- Paste a skill folder's link into any agent and ask it to use it.

Each skill's own `README` and `SKILL.md` carry its specifics. Every skill is
fully bilingual (`*.zh.md` / `SKILL.zh.md`); work in whichever language the
source is in.

## Why "run", not "read"

1. A tutorial is told to a person and handed back. A skill is executed by an
   agent, the same way every time.
2. Reach decays; a discipline that gets run compounds.
3. These encode judgment, not just steps — and each names its own deprecation
   condition: when a bare model does this reliably, the skill retires. A tool
   that can't name its own obsolescence is claiming immortality.

## License

MIT. See `LICENSE`. A skill may set its own; check its folder.

中文见 [`README.zh.md`](README.zh.md)。
