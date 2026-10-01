# SohuPowerVirusThermalTestCase 错误码

由 `SohuPowerVirusThermalTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-THM-0004: CATASTROPHIC_TRIP_DURING_STRESS](#TH-THM-0004)
- [TH-THM-0006: DTS_PEAK_TEMPERATURE_EXCEEDS_MAX](#TH-THM-0006)

<a id="TH-THM-0004"></a>
## TH-THM-0004: CATASTROPHIC_TRIP_DURING_STRESS

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0004` |
| 名称 | `CATASTROPHIC_TRIP_DURING_STRESS` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.THM.TRIP` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

压力工作负载期间发生灾难性跳闸事件。

### 测试用例

`SohuPowerVirusThermalTestCase`

### 可能原因

- Power Virus 下温度越限
- TIM 或冷板接触退化

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 检查 IBC TIM，并确认 Sohu 模块已正确装入治具并固定到位。 |  | 5 | — |
| 2 | 操作员 | 同时确认 Sohu 模块顶部冷板已连接到 HRM 冷却回路。 |  | 5 | — |
| 3 | 操作员 | 若未发现异常，复测一次。 | 受影响子集 | 10 | — |

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

<a id="TH-THM-0006"></a>
## TH-THM-0006: DTS_PEAK_TEMPERATURE_EXCEEDS_MAX

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0006` |
| 名称 | `DTS_PEAK_TEMPERATURE_EXCEEDS_MAX` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.THM.DTS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Power Virus 下的 DTS 峰值温度超过预期最大值。

### 测试用例

`SohuPowerVirusThermalTestCase`

### 可能原因

- 单板未完成所要求的 45 分钟 TIM 烘烤流程
- TIM 或冷板接触退化
- TIM 烘烤时长已从 15 分钟更新为 45 分钟。

### 采集项

- suite_run_url
- 本次运行的温度遥测
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 若任何温度读数超出规格，确认受影响单板已完成所要求的 45 分钟 TIM 烘烤流程。 |  | 5 | — |
| 2 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 3 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`, `TIM`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
