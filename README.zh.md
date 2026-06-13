# whetstone

**把领域判断,编码成 agent 可执行的纪律。**

一个持续生长的 skill 合集。每个 skill,把我工作里真正在用的一套纪律,写成 agent
能**照着执行**的样子——选模式、守规则、每次都一样——而不只是讲给人听、看完就忘。

> 用 AI 重读典籍,用县城验证硅谷,用赚钱检验思考。
> —— K,在县城,AI 原生

## Skills

| Skill | 做什么 |
|---|---|
| [read-not-decorate](skills/read-not-decorate) | 把一篇写完的 markdown 长文装配成独立 HTML——为阅读和留档,不为装饰。 |
| [missing-not-zero](skills/missing-not-zero) | 把字段表做成单文件 HTML 采集工具,强制区分"确实没发生"与"没采集到"——缺失不是零。 |
| [backtest-your-framework](skills/backtest-your-framework) | 用真实历史案例盲测一个判断框架准不准,一套防自欺协议让历史打分,而不是让 AI 顺着你乐观。 |
| [handoff-discipline](skills/handoff-discipline) | 把一个 AI 会话的工作状态交给无共享上下文的另一个——分清"不许重开 / 当前状态 / 战略理由"。 |
| [audit-the-hustle](skills/audit-the-hustle) | 审一个声称在网上赚钱的人是真经营还是表演;只给信号+把握度,不给定论。 |
| [stress-test-the-plan](skills/stress-test-the-plan) | 拷打一个决策:找致命弱点、挖隐含假设、推演多轮失效。自带"故意悲观"的偏向声明。 |
| [distill-not-transcribe](skills/distill-not-transcribe) | 把一份写好的方法变成"编码判断而非步骤"的 skill。材料里没有判断时,它会拒绝。 |
| [report-deck-zh](skills/report-deck-zh) | 按中文正式汇报的结构语法排幻灯片——标题对仗、总分总、数据页带口径说明。只做结构,不碰内容。 |
| [strip-the-ai-voice](skills/strip-the-ai-voice) | 用"只删不改"的确定规则,去掉中文文本的 AI 味,可逐句检验。 |

其中两个是改编线 skill,各自在文档里写明了谱系:`report-deck-zh` 改编自
frontend-slides;`strip-the-ai-voice` 是某类 humanizer 的反方向。谱系是声明的,
不是藏起来的。

## 安装

任选其一:

- clone 整个合集;
- 把 agent 指向某一个 skill 目录,如 `skills/read-not-decorate`;
- 把某个 skill 目录的链接贴进任意 agent,让它直接用。

每个 skill 自己的 `README` 和 `SKILL.md` 写具体细节。全仓双轨
(`*.zh.md` / `SKILL.zh.md`),按源文档的语言干活。

## 为什么是"执行",不是"阅读"

1. 教程是讲给人听的,看完就还回去;skill 是 agent 照着执行的,每次都一样。
2. 注意力会贬值;被反复执行的纪律会沉淀。
3. 它们编码的是判断,不只是步骤——而且每个都写明自己的退役条件:当裸模型能
   稳定做到这件事,这个 skill 就该退役。一个不肯说自己何时过时的工具,多半在卖。

## 许可

MIT,见 `LICENSE`。个别 skill 可自设许可,看各自目录。
