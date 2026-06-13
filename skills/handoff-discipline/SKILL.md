---
name: handoff-discipline
description: >
  Hand off the working state of one AI session to another that shares no
  context. Trigger when the user says "write a handoff for the next agent /
  another Claude / a fresh session", "brief the next instance", "sync state
  to my other project", or "carry this over without losing what's decided".
  Produces a self-contained handoff doc that separates what must NOT be
  reopened from current status from strategic rationale, and defines the
  receiving agent's role. Do NOT trigger for: summarizing a document for a
  human reader, writing meeting notes, or compressing a conversation for
  the same ongoing session (that is summarization, not handoff).
---

# handoff-discipline

A summary loses what the next agent must not re-decide. This skill turns a
session's working state into a handoff document the next agent can execute
against without reopening closed questions.

## Stance (load-bearing biases)

**1. A handoff is a transfer of decision boundaries, not a transfer of
information.**
Mechanism: a summary preserves information and discards decision status.
The receiving agent needs the status — which questions are closed — more
than the content, because an agent that cannot tell closed from open will
re-litigate closed questions with full confidence.
Field observation: in one cross-instance handoff I worked from, an account
handle had been mistyped into a transposed variant. The handoff carried no
pinned-decisions list and demanded no item-by-item echo, so the receiving
instance built on the wrong handle and nothing in the pipeline stopped it.
The error propagated silently into the output.
Boundary: verified on handoffs between two AI projects owned by the same
person, same long-running project. Cross-person and cross-organization
handoffs: untested.

**2. Three layers must be explicitly separated: pinned / status / rationale.**
Mechanism: when the layers are interleaved, the receiving agent cannot tell
which sentence is a fixed constraint and which is updatable state. Tactical
status gets read as a strategic invitation; pinned decisions get read as
context it may improve on.
Field observation: same handoff practice as above — the documents that
worked were the ones that listed pinned decisions as a numbered block at
the top, separate from progress notes. The ones that mixed them produced
receiving agents that "helpfully" redesigned settled structure.
Boundary: layer separation has been exercised on project-state handoffs
(naming, architecture, scope decisions). Handoffs of pure creative drafts:
untested — the pinned layer may be near-empty there.

**3. The receiving agent gets a written role boundary, including a yield
rule.**
Mechanism: without an explicit "execute, don't re-decide" clause plus a
conflict priority (user's live word > handoff doc > older docs), the
receiving agent defaults to its general helpfulness prior — which includes
re-deciding.
Field observation: handoffs in the source practice that included a receipt
requirement (echo back pinned list + open items + next step) caught
transcription drift at intake instead of at delivery.
Boundary: yield rule tested only where the same user is on both ends and
can adjudicate live.

## Core actions

1. **Classify before writing.** Sort the source material into three layers —
   pinned / current status / strategic rationale — and quarantine the
   danger class: items pending review, which belong to neither pinned nor
   status. Rules: read `reference/layers.md`.
2. **Fill the template.** Use the handoff skeleton with its fixed field
   order. Fields: read `reference/template.md`.
3. **Append the receiving protocol.** Role boundary, yield rule, receipt
   requirement. Text: read `reference/receiving.md`.
4. **Gate before output.** Echo the pinned-decisions list to the user and
   get confirmation before producing the document. This is the only step
   that prevents a pending item from being frozen as pinned.

| When doing | Load |
|---|---|
| Classifying messy material into layers | `reference/layers.md` |
| Writing the handoff document | `reference/template.md` |
| Writing the receiving agent's section | `reference/receiving.md` |
| Wanting a worked example | `examples/filled-handoff.md` |

## Skill fields

- **Version**: 0.1 (2026-06). Changelog: corrections are added, not erased;
  superseded guidance gets a reverse mark, old handoff documents are
  archived, never overwritten.
- **Retirement condition**: when AI systems hold persistent shared memory
  across sessions and instances, so that handoff no longer requires a
  human-mediated document, this skill retires.
- **Failure behavior**: if the source material does not let you tell pinned
  from pending, stop and have the user classify item by item. Do not guess
  which decisions are pinned — a wrong guess either freezes a judgment
  that should update or reopens one that should not, and both costs are
  silent.
- **Composition**: composes with any project-management or memory skill;
  this skill only governs the structure of a cross-context handoff. Yields
  to explicit user instruction.
- **Time**: judgments fixed 2026-06. The premise "AI lacks persistent
  cross-session memory" is moving; re-review expected within 12–24 months.
- **Boundary**: verified for one person handing one long-running project
  between two of their own AI projects. Cross-person, cross-organization,
  and adversarial handoffs: untested, unclaimed.
