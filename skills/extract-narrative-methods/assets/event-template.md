# Event Audit Template

Evidence-layer output. One entry per major event, then a chapter-coverage table.
No method claims here — events only. Field labels match the validator.

```markdown
# chunk_NNN · 第X–Y章 · 事件审计

<one-paragraph chunk orientation: the political/dramatic phase, no conclusions>

### 事件 E001
- 章节：<chapters, within this chunk's range>
- 参与者：<actors>
- 事件目标：<what the focal actor is trying to do>
- 客观动作：<observable action, not impression>
- 对方/系统响应：<observed response, or "未出现">
- 直接结果：<direct result only>
- 结果状态：已完成 | 阶段完成 | 进行中 | 失败/反噬
- 建议归属：A（chunkNNN-A01：…） | B（…） | 待定 | 不入卡（理由）
- 证据风险：<what is uncertain or could be confused with another event>
- 可能重复：<other event ID, or 无>

### 事件 E002
...

## 逐章覆盖表
| 章 | 事件ID / 无独立主要事件 | 一句话承接 |
|---|---|---|
| 第X章 | E001 | … |
| 第X+1章 | 无独立主要事件 | <transition in one line> |
```

Rules: every assigned chapter appears in the coverage table; a single
range-level claim ("第X–Y章已读") is not proof of reading. Rejected events stay
listed with their reason — they feed the reviewer's recall check.
