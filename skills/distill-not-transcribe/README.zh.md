# distill-not-transcribe(中文说明)

把成文方法做成承载作者判断的 skill——材料只有步骤没有决策时,拒绝。

**状态:v0.1 预发布。** 对照证据待首次真实运行;当前正以"用本 skill
从源协议重造一个已有 skill,再 diff"的方式自测
(见 `examples/recursive-acceptance.zh.md`)。主张跟在证据后面,
不跑在前面。

## 立场

公开目录里两万多个 skill,多数在誊写步骤。agent 不缺步骤,缺的是
作者做过、裸模型不会做的决策:遇 X 选 A 不选 B,因为 ___。
本 skill 只造这一种,其余拒绝。想用没有判断的材料造 skill,
这是错误的工具——故意的。

## 它做什么

- **蒸馏线**:你的协议/SOP/工作流文档 → skill。七类变换 +
  增厚四件套(规则+机制+目击观察+验证边界)。
- **改编线**:已有高赞 skill → 你的改编。四问把判断增量和誊写
  分开,带真实测试痕迹页出厂。
- 每个产出带必备六字段,含自己的废止条件与失败行为。

## 安装

- Claude Code:把本仓库加为 marketplace,或拷贝
  `distill-not-transcribe/` 进 skills 目录。
- 任何其他 agent:把仓库链接发给它,让它按 SKILL.md 执行。

## 谱系

- composes-with:官方 skill-creator(评测工装与打包归它;
  判断筛选与取信结构归本 skill)。
- whetstone 合集成员。许可 MIT。作者 K。
