# Visual System

Hard constraints. These are not suggestions; deviating from them is the failure
mode this skill exists to prevent.

## Color

| Role | Value |
|---|---|
| Background | `#FAFAF7` (warm off-white, never pure white) |
| Body text | `#1A1A1A` |
| Secondary text | `#666666` |
| Faint text (meta, footnotes) | `#999999` |
| Rule / divider | `#E5E5E0` |
| Accent | `#C8553D` |

The accent is the only color in the document. It appears **only** on: key
judgments, section numbers, self-case borders, quote-block left rules, table-of-
contents numbers, the progress bar. Nowhere else.

Forbidden: any second color, blue, green, gradients, drop shadows, glows, large
rounded card corners.

## Type

System font stack only. No web fonts, no CDN.

- Body / headings: `-apple-system, "PingFang SC", "Helvetica Neue", sans-serif`
- Quote blocks: `Georgia, "Songti SC", serif`, italic

Headings use weight 600, letter-spacing `-0.02em` (H1) / `-0.015em` (H2).

Desktop size scale:

| Element | Size / line-height |
|---|---|
| H1 | 42px / 1.2 |
| H2 | 28px / 1.3 |
| H3 | 20px |
| Body | 17px / 1.75 |
| Quote | 17px italic |
| Key judgment | 22px, weight 600 |
| Note / secondary | 13–15px, `#666` or `#999` |

## Spacing

- Between sections: ≥ 80px
- Between paragraphs: 1.4em
- Around a key judgment: 60px each side
- H2 `scroll-margin-top`: 80px (so anchor jumps clear the sticky nav)

## Measure

Max body width **680px**, centered. Never full-bleed.

## Page skeleton (every document has this)

```
[sticky nav, light frosted glass]
  left: short title  (archival mode adds a small accent "archival" badge)
  right: contents ▾  (opens a drawer)

[progress bar, 2px top line, accent color, updates on scroll]

[contents drawer, slides from right]
  H2 list, numbers 01/02 in accent, click = anchor jump

[article body]
  Hero: H1 / one-line positioning (secondary) / meta row: author · date · word count (faint)
  ───
  Section 01 …
  Section 02 …
  ───

[footer signature block]
```

CSS budget: keep total under 600 lines. If you are over, you are decorating.
