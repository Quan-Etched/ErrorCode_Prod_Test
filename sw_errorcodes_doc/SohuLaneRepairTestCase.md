# SohuLaneRepairTestCase 错误码

由 `SohuLaneRepairTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HBM-0006: HBM_LANE_REPAIR_FAILED](#TH-HBM-0006)
- [TH-HBM-0008: HBM_LANE_REPAIR_INCOMPLETE](#TH-HBM-0008)

<a id="TH-HBM-0006"></a>
## TH-HBM-0006: HBM_LANE_REPAIR_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HBM-0006` |
| 名称 | `HBM_LANE_REPAIR_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 3 — 内存 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.HBM.STACK` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

通道修复未能使每个 HBM 伪通道都完成修复。要么扫描已完成，但一个或多个目标没有任何通过的修复（每个候选字节对都已尝试，且没有一对闭合眼图）；要么扫描中途中止，可修复性从未得到确认。

### 测试用例

`SohuLaneRepairTestCase`

### 可能原因

- 伪通道上的故障通道数超过备用通道数
- HBM 堆栈或中介层缺陷超出通道修复覆盖范围
- 受影响通道上的 Sohu HBM PHY 故障

### 采集项

- suite_run_url
- hbm_lane_repairs JSON 产物（逐目标修复映射）
- Lane Failures 测量值（每次失败的 HBM/通道/伪通道）
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`HBM_STACK`, `INTERPOSER`, `ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-HBM-0008"></a>
## TH-HBM-0008: HBM_LANE_REPAIR_INCOMPLETE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HBM-0008` |
| 名称 | `HBM_LANE_REPAIR_INCOMPLETE` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / 1x-module-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 3 — 内存 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.HBM.STACK` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

通道修复检测扫描未运行到完成，因此从未确认是否存在可通过的修复。涵盖 find_broken_lanes 抛出的检测异常（包括快速失败的不可修复情况以及校验抛出），以及事先清除已持久化修复并重新加载固件时的失败。与 TH-HBM-0006 不同：后者表示已完成的扫描尝试了每一个候选字节对，且没有一对闭合眼图。

### 测试用例

`SohuLaneRepairTestCase`

### 可能原因

- 扫描中途检测 RPC 或 SPI flash 访问失败
- 清除已持久化修复后重新加载固件未能恢复
- 修复映射合并时遇到冲突或超出范围的已持久化条目

### 采集项

- suite_run_url
- 含检测异常及其所中止阶段的逐测试日志
- 若已写出，则包含不完整的 hbm_lane_repairs 产物
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 升级处理 | 将检测异常和不完整的修复映射升级给 Etched；可修复性未知，并不是已判定失败，因此不要把单板送去失效分析（FA）。 | 不适用 |  | — |

### 疑似组件

_无_

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
