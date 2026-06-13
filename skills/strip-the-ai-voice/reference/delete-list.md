# Delete list — four classes

Each class: what it is, word examples, the action. All examples are fictional or generalized.

## 1. Honorifics and filler particles

Words: 您 / 请 / 哦 / 呢 / 呀 / 吧~ / 哟 / 真棒 / 太棒了

Action: delete the word. If the sentence existed only to carry the honorific ("请您仔细查看哦~"), apply the delete-test — usually the whole sentence goes.

Note: 请 in an imperative instruction ("请勿外传" on a legal notice) can be load-bearing. Run the test; if deleting 请 changes the meaning, keep it.

## 2. Adjective/adverb padding

Patterns: 深刻地 / 精妙的 / 全方位、多角度 / 精心创作的 / 强大而简洁的 / 完美地 / 高效地

Action: delete the modifier, keep the noun/verb. "精心设计的界面" → "界面". If nothing remains after deletion, the sentence was decoration — delete it (see `the-test.md`).

## 3. Self-explanation

Patterns: sentences where the copy explains what it (or the tool) is doing.

- "点击下方按钮以查看详细内容" → the button is right there → delete; label the button instead.
- "旨在为读者提供一个对照视角" → show the comparison; delete the sentence.
- "以下是为您整理的要点" → delete; show the points.

Action: delete the whole sentence. The UI or the content itself is the statement.

## 4. Reader-conclusions

Patterns: sentences that tell the reader what to think or feel.

- "这一点至关重要,请重点关注!"
- "助您快速把握全文脉络"
- "相信您一定会感受到它的便捷"

Action: delete the whole sentence. If the point matters, the surrounding structure (heading, position, emphasis weight) carries it.

## Order of operations

1. Pass 1 — class 1 and 2: delete words.
2. Pass 2 — run the delete-test on every touched sentence (see `the-test.md`).
3. Pass 3 — class 3 and 4: delete sentences.
4. Pass 4 — forbidden items (see `forbidden.md`): delete on sight.
