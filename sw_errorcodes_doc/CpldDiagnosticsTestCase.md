# CpldDiagnosticsTestCase 错误码

由 `CpldDiagnosticsTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-MEZZ-0001: MEZZANINE_CPLD_ACCESS_WRITE_FAILED](#TH-MEZZ-0001)
- [TH-THM-0017: CPLD_CATTRIP_DETECTED](#TH-THM-0017)

<a id="TH-MEZZ-0001"></a>
## TH-MEZZ-0001: MEZZANINE_CPLD_ACCESS_WRITE_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-MEZZ-0001` |
| 名称 | `MEZZANINE_CPLD_ACCESS_WRITE_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.MEZZ.CPLD` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

Mezz/eval CPLD 寄存器访问或写入失败。

### 测试用例

`ProgramSecureBootloaderTestCase`, `CpldDiagnosticsTestCase`

### 可能原因

- 夹层板或 eval-board CPLD 寄存器访问失败
- Devkit 无法与 Sohu 模块通信，很可能是引导加载程序未运行，因为 PV1 未上电

### 采集项

- suite_run_url
- per-test log and transcript
- CPLD operation transcript
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 Sohu 模块上的绿色电源指示灯已点亮。 |  | 5 | — |
| 2 | 操作员 | 确认 PCIe 线缆与电源线均已正确、牢固连接。 |  | 5 | — |
| 3 | 操作员 | 若未发现问题，复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`MEZZ`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-THM-0017"></a>
## TH-THM-0017: CPLD_CATTRIP_DETECTED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0017` |
| 名称 | `CPLD_CATTRIP_DETECTED` |
| 版本 | 1 |
| 起始版本 | harness 2026.253 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.THM.TRIP` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

夹层板 CPLD 报告 cattrip：MCU cattrip 锁存已置位、MCU cattrip 在 VCC_1V2 正常时处于活动状态，或某条 HBM cattrip 通道处于活动状态。由 `CpldDiagnosticsTestCase` 在启用 `fail_on_cattrip` 时发出，因此判定会点名热事件本身，而不是在其下失败的工作负载。

### 测试用例

`CpldDiagnosticsTestCase`

### 可能原因

- 工位冷却故障（CDU、冷却液流量、HRM 回路），表现为所有已插入芯片同时触发
- 单个模块上的 TIM 或冷板接触劣化
- 应力工作负载下的热偏移

### 采集项

- suite_run_url
- 每颗芯片的 cpld_diagnostic_report_chip<N>.txt，以及哪些芯片已触发
- 若存在，已采集用例中的 DTS / VM / BMC collector parquet
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 若所有已插入芯片均已触发，停止并在任何复测前检查工位冷却（CDU 状态、冷却液流量、HRM 回路）。 |  | 10 | — |
| 2 | 操作员 | 针对单颗芯片，检查 IBC TIM 并将模块在治具中重新就位；确认顶部冷板已接入 HRM 回路。 |  | 10 | — |
| 3 | 升级处理 | 将 CPLD 报告与采集器数据升级给 Etched 工程师。 |  | — | — |

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
