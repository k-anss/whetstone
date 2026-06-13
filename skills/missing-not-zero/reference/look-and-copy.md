# Look and copy: visual system, and the words *you* write

Load this when styling, and whenever you write any text of your own — labels,
buttons, errors, placeholders. (Field names, item titles, and module names
from the spec: you change not one character.)

## Palette (hard constraint)

| Role | Value |
|---|---|
| Background | `#FAFAF7` (warm off-white, not pure white) |
| Body text | `#1A1A1A` |
| Secondary text | `#666666` |
| Dividers | `#E5E5E0` |
| Accent | `#C8553D` — only for: active module tab, required `*`, copy-success flash |
| Warning | `#B85C00` — only for: missing-required field borders |

No other colors. No gradients, no shadows, no glow, no border radius over
4px. No emoji, no decorative icons, no stock or AI-generated imagery.

## Type and layout

- Font: system stack (`-apple-system, "PingFang SC", "Helvetica Neue",
  sans-serif`); export preview in a monospace stack.
- Sizes: page title 22px · module tabs 15px · item titles 17px · field labels
  14px · inputs 16px (so mobile browsers don't auto-zoom) · preview 13px.
- Desktop max width 720px centered; mobile 16px side padding.
- Cards 24px apart, fields 12px apart. Inputs full-width; short fields
  (time/date/select) may pair two per row.
- This is an *operating* surface, not a reading page: density beats
  whitespace here — the opposite trade from a reading-page skill.

## Copy restraint (three principles)

1. **Verb-driven; no adjective garnish.**
2. **Never narrate what the tool is doing.**
3. **State changes use the shortest word that survives.**

| ✗ Don't | ✓ Do |
|---|---|
| "Success! Your record has been added!" | "Recorded" |
| "Please carefully review all required fields and try again" | "3 required fields missing" |
| "Your data has been successfully copied to the clipboard" | "Copied" |
| "Are you sure you want to clear all your data? This cannot be undone!" | "Clear all 5 records?" |
| "No data yet — start by filling the form above" | (nothing; the empty state is self-evident) |
| "This tool is designed to help you efficiently collect…" | (subtitle says what it collects, or nothing) |

**The gray-zone test:** strip every adjective and adverb from the sentence.
If what remains still stands, ship the stripped version. If nothing usable
remains, the sentence was decoration — delete it whole.

The Chinese twin of this file carries an extra, Chinese-specific pass
(dropping honorifics and particle padding: 您/请/哦/呢) that has no English
equivalent — if the tool's UI language is Chinese, work from the twin.

## No signature by default

Generated tools are disposable instruments, not works. No footer, no author
block, no "do not distribute" line — unless the spec explicitly asks, in
which case one 12px muted line at the bottom is the ceiling.
