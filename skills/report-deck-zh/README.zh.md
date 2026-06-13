# report-deck-zh

中文工作汇报有一套结构语法——对仗标题、总分总、带口径的数据页——
英文 slide 工具不会说。本 skill 把它编码下来。

这是一个 skill:一份纪律文件,agent 加载后按中文正式汇报的约定排
工作汇报 slides(述职/总结/立项/复盘),而不是英文 pitch deck 审美,
也不是大众 AI-PPT 工具的同质化产物。

它产出**结构,不产出内容**。它搭骨架——标题怎么对仗、章节怎么递进、
数据页怎么带口径——绝不写汇报的实际内容。

## 谱系

derived from / inspired by **frontend-slides**(Zara)。frontend-slides
做英文审美的漂亮 HTML slides,它不懂中文正式汇报的结构语法:对仗
标题、总分总收口、带口径说明的数据页、按中文公文逻辑的层级递进。

一句话区别:frontend-slides 让英文 deck 好看;本 skill 让中文汇报读
起来像本土正式材料。`examples/lineage-test.zh.md` 记录了拿
frontend-slides 排一份中文汇报的测试——它结构哪里错了,本 skill 怎么
修正。

## 它做什么

- **对仗标题**——字数对齐、结构对称、动宾一致。
- **总分总骨架**——开篇述总,中间分项,结尾回到总并给增量。
- **数据口径页**——每个数字带来源、范围、时间口径;"不掌握"和
  "不适用"保持区分。
- **克制视觉**——复用 read-not-decorate 令牌;禁 emoji、禁渐变、禁
  装饰美化。

## 何时别用

- 英文 pitch deck → 用 frontend-slides。
- 随意/社交分享型 slides → 强行对仗读起来僵。
- 生成汇报的实际内容 → 本 skill 只搭骨架。

## 安装

把本文件夹放进 skills-aware agent 的 `skills/` 下。agent 加载
`SKILL.md`;`reference/` 按需加载。

## 许可

MIT。作者:K(@k-anss)。属于 `whetstone` 合集。
