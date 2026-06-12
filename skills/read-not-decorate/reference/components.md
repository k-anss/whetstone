# Components

Call a component only when the text already has that structure. No structure, no
component — a plain paragraph is the correct default. Bias to fewer. A document
that uses two components well beats one that uses eight to look busy.

Decision rule: see structure, call component; see no structure, set paragraphs;
**see structure that fits none of these, route to "candidate component" (last
entry) — do not force it into the nearest one, do not flatten it.**

---

## 1. Contrast block (two / three track)

**Trigger** — "for A it's X, for B it's Y", "early it's X, late it's Y", "X is
hardware, Y is software, Z is cache".
**Form** — side-by-side (or three-column) cards. Top: small LABEL tag (accent,
letter-spacing 0.1em, 12px). Middle: bold conclusion. Bottom: secondary-color
description. Card background `#F5F5F0`, no border, padding 24px. Narrow screens:
stack to one column.

## 2. Mechanism diagram (SVG)

**Trigger** — an "input → black box → output" causal chain, or a multi-step
mechanism.
**Form** — horizontal SVG flow. Nodes are hairline rectangles (1px `#1A1A1A`),
normal node fill `#FAFAF7`, key node fill `#FFF0EC` + accent border. Connectors
1px straight lines, tiny arrowheads. Branches dashed. Caption below, 13px
secondary. No shadow, gradient, animation, or effect arrows.

## 3. Quote block

**Trigger** — a quotation from any source (classical, political, commercial, a
contemporary author).
**Form** — 3px accent left rule, serif italic 17px, a 13px secondary line below
naming the source. Multiple quotes do not change color; all use the accent.
**Variant** — if the "quote" is a synthesized passage from the body (an
illustration, not an attributed source), use a `#666` grey left rule to keep the
visual hierarchy honest.

## 4. First-person case marker

**Trigger** — the author's own lived experience, or an anonymized scenario.
**Form** — whole block on `#F5F5F0` + 3px accent left border, a small top-right
tag ("first-hand" or "anonymized scenario"), 13px secondary.
**Note** — when archiving someone else's article, **do not use this** — another
person's hypothetical example is not a first-hand case.

## 5. Concept pair

**Trigger** — a set of opposed or parallel concepts (self vs. one's role,
permitted vs. true, external disturbance vs. internal contribution).
**Form** — one concept per row: left number 01/02 in accent, middle concept name
bold 17px, right definition 15px secondary. Rows divided by 1px `#E5E5E0`.

## 6. Key-judgment highlight

**Trigger** — a standalone bolded short sentence, or a closing line like "the
core is…", "the real problem is…", "in one line:".
**Form** — own paragraph, 22px, weight 600, letter-spacing -0.01em, 60px
whitespace each side, **centered**. No background, no border — size, whitespace,
and centering do the work. At most 1–2 per section. Do not let it proliferate.

## 7. Boundary-condition fold

**Trigger** — "this analogy has limits", "does not apply to Y", "boundary: ___",
"three cautions".
**Form** — `<details>` panel, collapsed by default. Summary 14px secondary, a
+ / − toggle in accent. Expanded content 15px / `#666` / line-height 1.7.
**Typical use** — after a core mechanism, a collapsed "boundary and where it
doesn't apply" that the reader expands only if they want it.

## 8. Cross-reference node (optional)

**Trigger** — the text refers to another numbered document in the same archive.
**Form** — inline mini-card: the reference id + that node's one-line core claim
(supplied in the instruction; never invent it). No link (offline file).
**Do not use when archiving someone else's article.**
**Superseded state (archival mode only)** — if a referenced node is marked
"corrected/overturned by another", turn its rule grey (as in component 7) and
add a 13px faint line: "superseded — see that node". The worst archival failure
is a future reader trusting a conclusion the author already overturned; this
tags the demolished floor. Distribution mode does not expose revision history,
so this is off there.

## 9. Enumerated proof block

**Trigger** — "is X really Y?", "1… 2… 3…" parallel interrogation.
**Form** — one card per item, number in accent, question 18px bold, answer 15px
secondary, a small inline tag at the bottom stating the conclusion. The sibling
of component 5, for exhaustive refutation or proof.

## 10. Candidate component (extend the vocabulary here)

**Trigger** — a clearly structured passage that fits none of components 1–9.
**Handling** — do not jam it into the nearest old component (distortion); do not
demote it to a plain paragraph (flattening). List it in the confirmation report
as a "candidate component", describe its structure in one line, and let the
author decide: new component / fold into an existing one / set as paragraphs.
**Why** — components 1–9 are sediment from documents seen before, not a closed
vocabulary. This keeps it open so old habits don't overwrite a genuinely new
structure.

## 11. Epistemic texture (archival mode only)

**Precondition** — only when the source markdown *already carries* confidence
and abandoned-branch texture. This step never invents uncertainty the author did
not write (that would violate "assemble, never author").
**Authoring convention (proposal)** — the author tags state in the markdown:
confidence `{0.6}` / `{ran half-way, dead end}` after a judgment; abandoned
branch `{dropped: reason}` at the head of a discarded line of thought.
**Render** — confidence tags become a 13px faint end-of-line mark that does not
break the body; abandoned branches use the component-7 fold, summary "dropped
branch".
**Distribution mode** — off entirely. When rendering, strip the tags and keep
the judgment sentence before them (the client does not read the author's
confidence).
