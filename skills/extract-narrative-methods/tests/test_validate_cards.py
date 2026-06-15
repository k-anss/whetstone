from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_cards.py"

SOURCE = """第一章 起点
甲说：“只在第一章。”
第二章 转折
乙说：“当前证据。”
第三章 越界
丙说：“来自第三章。”
"""

A_CARD = """# A
### 案例 A01：借力
- 章节：第一至二章
- 结果状态：阶段完成
- 主体：甲
- 困境：没有直接命令权
- 对方：乙
- 我方有什么：规则
- 我方要什么：行动
- 我方愿意放弃什么：时间
- 对方有什么：执行权
- 对方要什么：免责
- 对方响应：乙执行了行动
- 关键动作：引用共同规则
- 成交/借力结构：用【规则】换取【执行】
- 实际代价：等待一天
- 信息/立场暴露：暴露目标
- 遗留风险：执行可能终止
- 最强替代解释：乙也可能自行行动
- 预期管理：不标⑦
- ▸ 关键原句：当前证据。
- 方法信号：借用既有规则
"""

B_CARD = """# B
### 管理案例 B01：试验
- 章节：第二章
- 结果状态：已完成
- 决策者：乙
- 管理困境：直接任命不可逆
- 手里有什么：临时授权
- 要什么：验证能力
- 愿意牺牲什么：速度
- 备选方案：直接任命
- 决策：设置临时任务
- 执行响应：团队完成任务
- 管理逻辑：用可撤销试验降低锁定
- 实际代价：延迟任命
- 信息/立场暴露：暴露候选偏好
- 遗留风险：试验样本有限
- 最强替代解释：任务过于简单
- 预期管理：不标⑦
- ▸ 关键原句：
- 方法信号：可撤销试验
"""

EVENTS = """# events
### 事件 E001
- 章节：第一章
- 参与者：甲
- 事件目标：取得行动
- 客观动作：提出规则
- 对方/系统响应：乙接受
- 直接结果：行动开始
- 结果状态：阶段完成
- 建议归属：A
- 证据风险：无
- 可能重复：无

### 事件 E002
- 章节：第二章
- 参与者：乙
- 事件目标：验证能力
- 客观动作：设置任务
- 对方/系统响应：团队完成
- 直接结果：获得表现证据
- 结果状态：已完成
- 建议归属：B
- 证据风险：无
- 可能重复：无

## 逐章覆盖表
| 章 | 事件ID / 无独立主要事件 | 一句话承接 |
|---|---|---|
| 第一章 | E001 | 起点 |
| 第2章 | E002 | 转折 |
"""

SELFCHECK = """# selfcheck
1. 已检查越界。
2. 已检查引文。
3. 已检查主体。
4. 已检查困境。
5. 已检查动作。
6. 已检查响应。
7. 已检查代价。
8. 已检查结果。
9. 已检查重复。
10. 已执行处置。
实际读取最后一章：第2章
"""


class ValidatorIntegrationTests(unittest.TestCase):
    def run_validator(
        self,
        *,
        a_card: str = A_CARD,
        b_card: str = B_CARD,
        events: str = EVENTS,
        selfcheck: str = SELFCHECK,
        extra: list[str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            paths = {
                "source": root / "source.txt",
                "a": root / "a.md",
                "b": root / "b.md",
                "events": root / "events.md",
                "selfcheck": root / "selfcheck.md",
            }
            paths["source"].write_text(SOURCE, encoding="utf-8")
            paths["a"].write_text(a_card, encoding="utf-8")
            paths["b"].write_text(b_card, encoding="utf-8")
            paths["events"].write_text(events, encoding="utf-8")
            paths["selfcheck"].write_text(selfcheck, encoding="utf-8")
            command = [
                sys.executable,
                str(VALIDATOR),
                str(paths["a"]),
                str(paths["b"]),
                "--source",
                str(paths["source"]),
                "--events",
                str(paths["events"]),
                "--selfcheck",
                str(paths["selfcheck"]),
                "--chapter-start",
                "1",
                "--chapter-end",
                "2",
                "--production",
            ]
            if extra:
                command.extend(extra)
            return subprocess.run(command, text=True, capture_output=True, check=False)

    def test_valid_production_accepts_chinese_and_arabic_coverage(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("ERRORS: 0", result.stdout)

    def test_card_chapter_outside_range_fails(self) -> None:
        result = self.run_validator(a_card=A_CARD.replace("第一至二章", "第三章"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("chapter reference outside assigned range", result.stdout)

    def test_offsource_quote_does_not_block_and_anchor_flags_review(self) -> None:
        # 引文（关键原句）允许转述/不在切片：不再致命，exit 0。
        # 防编造改由"定位锚"负责——锚不在原文则进 REVIEW 复查清单，但仍不拦。
        result = self.run_validator(
            a_card=A_CARD.replace("当前证据。", "这是一句原文里没有的转述。")
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        # A_CARD 无独立"定位锚"字段，回退用关键原句定位；该句不在切片 → REVIEW
        self.assertIn("REVIEW", result.stdout)
        self.assertIn("疑似编造", result.stdout)

    def test_six_question_shell_fails(self) -> None:
        result = self.run_validator(
            a_card=A_CARD.replace("- 关键动作：引用共同规则\n", "")
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("required field 关键动作", result.stdout)

    def test_short_selfcheck_flags_review_not_block(self) -> None:
        # self-check 过短是深度信号，不再自动停机/拦截——降为 REVIEW 交人。
        result = self.run_validator(
            selfcheck="# selfcheck\n实际读取最后一章：第2章\n"
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("REVIEW", result.stdout)
        self.assertIn("selfcheck too short", result.stdout)

    def test_empty_quote_no_longer_blocks(self) -> None:
        # 引文已非必填、可空可转述：空引文不再触发任何停机阈值，exit 0。
        result = self.run_validator(
            a_card=A_CARD.replace("当前证据。", ""),
            extra=["--max-empty-quotes", "1"],
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("empty-quote stop threshold", result.stdout)


if __name__ == "__main__":
    unittest.main()
