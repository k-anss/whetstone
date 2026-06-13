# Worked example — full deletion pass

Fictional input: a typical AI-flavored Chinese product blurb.

## Before

> ✨ 欢迎使用本工具!本工具旨在为您提供全方位、多角度的数据管理体验。请您点击下方按钮,开始您的旅程吧~ 我们精心设计了简洁而强大的界面,相信您一定会深刻地感受到它的便捷之处!如有任何疑问,请随时联系我们哦。感谢您的耐心阅读,如果觉得有用,欢迎分享给身边的朋友!

## Pass 1 — class 1 & 2: delete words

- Honorifics/particles: 您 ×5, 请 ×2, 吧~, 哦, ✨, !×3
- Adjective/adverb padding: 全方位、多角度 / 精心设计的 / 简洁而强大的 / 深刻地 / 随时

## Pass 2 — delete-test on each sentence

| Sentence | Remainder after deletion | Verdict |
|---|---|---|
| 欢迎使用本工具 | 欢迎使用本工具 | greeting boilerplate; carries nothing the title doesn't → delete |
| 本工具旨在为您提供…数据管理体验 | 本工具提供数据管理 | stands → keep remainder |
| 请您点击下方按钮,开始您的旅程吧~ | 点击按钮开始 | self-explanation; the button is there → delete, label the button |
| 我们精心设计了…界面,相信您一定会深刻地感受到它的便捷之处 | 我们设计了界面,你会感受到便捷 | reader-conclusion; says nothing → delete |
| 如有任何疑问,请随时联系我们哦 | 有疑问联系我们 | stands (information: a contact path exists) → keep remainder |
| 感谢您的耐心阅读…欢迎分享给身边的朋友 | — | forbidden class 2 → delete |

## Pass 3 & 4 — sentence deletions and forbidden items applied above

## After

> 数据管理工具。
> 疑问联系:{联系方式}。
>
> (Button label: 开始)

Six sentences in, two statements out. Nothing was rewritten; everything removed belonged to one of the four deletion classes or the forbidden list.
