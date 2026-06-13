# template — handoff document skeleton

Field order is fixed. Empty optional fields are dropped, not left as
placeholders.

```markdown
# Handoff · {project} → {receiving context}

## Project in one line
{what this is, one sentence}

## Pinned decisions (do not reopen)
1. {decision, verbatim where exactness matters}
2. ...

## Current status
- {fact}
- {fact}

## Pending items (not pinned — awaiting a call)
- {item} — pending: awaiting {who} to decide
- (omit section if none)

## Strategic rationale (read to understand, not to revise)
{optional; why the pinned decisions were made}

## Red lines
- {hard constraints that override everything below them}

## Receiving agent: role and receipt
{paste from reference/receiving.md, adapted}

## Conflict priority
User's live word > this document > any earlier document.
```

## Field notes

- **Project in one line** — the receiving agent has zero context; this
  line is its entire world model until it reads further. Make it carry
  the noun ("a skills monorepo", "a data pipeline"), not the mood.
- **Pinned decisions** — the load-bearing section. Numbered, one per
  line. Include exact strings (handles, names, versions) the receiver
  must reproduce. This list is what the receiver echoes back in its
  receipt.
- **Current status** — verifiable facts only. See layers.md.
- **Pending items** — every entry names who decides. An anonymous
  pending item is unresolvable downstream.
- **Strategic rationale** — optional. Cut it before letting it bloat;
  a receiver drowning in rationale starts treating it as an invitation.
- **Red lines** — constraints that survive even a user instruction to
  the receiving agent would need to explicitly override (privacy, scope,
  publication rules). Keep them few and absolute.
- **Conflict priority** — always the last line, always this order. The
  document must subordinate itself to the live user, or it becomes the
  frozen judgment it was designed to prevent.
