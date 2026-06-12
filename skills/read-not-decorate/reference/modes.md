# Modes

Declare the mode before assembling anything. The two modes serve opposite
readers, and the choice — not a per-file weighting, a fork at the start —
decides which components survive and how the file is delivered.

## Archival

- **Reader**: the author, months from now.
- **Wants**: the process, the basis for each judgment, the uncertainty that was
  true at the time.
- **Reads by**: scanning, asking "what did I have when I judged this".
- **Components on**: epistemic texture (11), superseded markers (8). Component
  density serves "reconstruct the judgment", not reading flow.

## Distribution

- **Reader**: a client or stranger with none of the author's context.
- **Wants**: clean, independently-standing conclusions and credible reasons.
- **Reads by**: depends — give one reader-profile line for internal tuning:
  > Reader: [a person / a group], reads [how], cares about [what].
  - *Linear reader*: sections flow into each other, key judgments paced out,
    contents can be terse.
  - *Scanner*: the first paragraph under each H2 must stand alone (a complete
    conclusion for someone who jumps), higher key-judgment density.
  - *Picker*: detailed contents, each H2 gets a one-line subtitle (15px
    secondary) telling the reader what the section holds.
- If no reader profile is given, default to linear. **Do not invent a reader
  profile and do not ask** — none given means none given.
- **Components off**: epistemic texture, superseded markers, first-hand case
  markers when archiving a third party's work.

## Delivery shapes (by mode)

- **Archival** — one `.html`, double-click and keep. No channel adaptation.
- **Distribution** — the `.html` plus, only if a channel is named, channel
  outputs: a fully-inlined-CSS version for newsletter editors; 2× PNG cards of
  key passages for social; an A4 print stylesheet (hide sticky nav and fold
  interactions, expand folds by default) for print/PDF. No channel named → only
  the `.html`. This is delivery routing, not engagement furniture — never add
  share / like buttons.

Default when the request is silent: **archival**, and say so.
