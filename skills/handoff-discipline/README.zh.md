# handoff-discipline(跨上下文交接纪律)

**摘要丢掉的,恰是下一个 agent 不许重新决定的东西。**

一个把 AI 会话工作状态交给另一个零共享上下文会话的 skill——接手方
不重开已关闭的问题、不把状态误读成邀约、不让誊写错误静默传播。

## 差距并排看

同一份杂乱工作笔记,两种交法。

**不挂 skill**(朴素摘要):

> 我们在 k-anss 下建一个叫 whetstone 的 skills 仓库,MIT 许可,中英
> 双轨。当前这个 skill 是关于交接的。进展不错——结构基本定了,命名
> 讨论过。下一步写 reference 文件。

接手方现在认为"命名讨论过"等于命名还开着。它分不清哪些事实是约束。
如果账号名被手误写错,这段话里没有任何东西能拦住。

**挂 skill**(三层交接):

> **已拍死(不许重开):** 1. 命名 `handoff-discipline` 2. 仓库
> `whetstone`,账号 `k-anss`,MIT 3. 结构:SKILL.md + 3 个 reference +
> 1 个 example,中英孪生
> **状态:** 简报已批;零文件已建。
> **待定:** README 立场句——等 K。
> **回执强制:** 开工前原样回显已拍死清单。

接手方逐字回显已拍死清单——手误的账号名死在入口。待定的保持待定,
关闭的保持关闭。

本 skill 长自一次真实事故:一个账号名手误穿过了朴素交接,静默传播
进了产出——因为没有任何环节强制逐项核对。建出本 skill 的那份真实
交接(脱敏版)见 `examples/filled-handoff.zh.md`。

## 安装

把 `handoff-discipline/` 文件夹复制进你 agent 的 skills 目录。然后说
"给下一个 agent 写一份交接"——skill 在交接意图上触发,在普通摘要
场景保持安静。

## 文件

- `SKILL.md` — 地图:立场、核心动作、六字段(含 `.zh.md` 孪生)
- `reference/layers.md` — 把材料分进 不许重开 / 状态 / 理由 三层
- `reference/template.md` — 交接文档骨架
- `reference/receiving.md` — 接手方协议
- `examples/filled-handoff.md` — 一份真实脱敏交接

MIT · K(`k-anss`)
