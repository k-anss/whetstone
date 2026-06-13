# data-pages.md — Data pages with caliber captions

The caliber caption (口径说明) is the professional marker of a Chinese
formal data page. A figure without its caliber is a claim without warrant.

## Anatomy of a data page

1. **Page title** — the judgment the data supports (parallel with siblings).
2. **The figure(s)** — table or simple chart. One message per page.
3. **Caliber caption (mandatory)** — small text, bottom of page, three
   slots, all filled:
   - 数据来源 (source): which system/ledger/report the numbers come from.
   - 统计范围 (scope): what is included and what is excluded.
   - 时间口径 (time caliber): the exact period, and whether figures are
     point-in-time or cumulative.

If any slot is unknown, the caption says so explicitly (e.g.
"统计范围:待补") — a missing slot is information, never silently dropped.
"Unknown" and "not applicable" are different states; never collapse them.

## Layout rules

- Caption: smaller, secondary color, never decorated, never omitted.
- Tables over decorated charts when both work. No 3D, no gradients.
- Numbers right-aligned; units stated once in the header, not per cell.
- Comparison figures state the comparison base in the caption
  (同比/环比 against what period).

## Fictional caption example

> 数据来源:订单系统导出;统计范围:自营渠道,不含第三方代销;
> 时间口径:2025-07-01 至 2025-09-30,累计值。

## Boundary

This pattern is for figures presented as evidence in a briefing. Exploratory
analysis notebooks have different needs — out of scope.
