# SohuPowerVirusTestCase 错误码

由 `SohuPowerVirusTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PWR-0007: UNEXPECTED_DVFS_RAMPDOWN](#TH-PWR-0007)
- [TH-SOHU-0015: WORKLOAD_HANG_OPERATION_TIMEOUT](#TH-SOHU-0015)
- [TH-THM-0005: DTS_PTP_DEVIATION_OUT_OF_BOUNDS](#TH-THM-0005)

<a id="TH-PWR-0007"></a>
## TH-PWR-0007: UNEXPECTED_DVFS_RAMPDOWN

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0007` |
| 名称 | `UNEXPECTED_DVFS_RAMPDOWN` |
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
| 组件 | `1X.PWR.DVFS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

工作负载期间出现非预期的 DVFS 降频事件。

### 测试用例

`SohuLlamaMttTestCase`, `SohuPowerVirusTestCase`

### 可能原因

- 功耗或温度越限触发 DVFS
- 电源轨在工作负载瞬态下处于边缘状态

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

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

<a id="TH-SOHU-0015"></a>
## TH-SOHU-0015: WORKLOAD_HANG_OPERATION_TIMEOUT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0015` |
| 名称 | `WORKLOAD_HANG_OPERATION_TIMEOUT` |
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
| 组件 | `1X.SOHU.WORKLOAD` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

工作负载挂起，或操作超时。

### 测试用例

`KayakTestCase`, `SohuPowerVirusTestCase`, `SohuLlamaMttTestCase`

### 可能原因

- SOHU 工作负载或操作未在超时时间内完成

### 采集项

- suite_run_url
- 逐测试日志与记录
- 恢复前捕获的器件状态
- unit_sn, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-THM-0005"></a>
## TH-THM-0005: DTS_PTP_DEVIATION_OUT_OF_BOUNDS

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0005` |
| 名称 | `DTS_PTP_DEVIATION_OUT_OF_BOUNDS` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.THM.DTS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Power Virus 下的 DTS 峰峰值偏差超出界限（阈值仍在评审中；界限可能会提高）。

### 测试用例

`SohuDtsTestCase`, `SohuPowerVirusTestCase`

### 可能原因

- TIM 或热加压头接触差异
- 阈值仍在评审中
- TIM 烘烤时长已从 15 分钟更新为 45 分钟。

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 若任何温度读数超出规格，确认受影响单板已完成所要求的 45 分钟 TIM 烘烤流程。 |  | 5 | — |
| 2 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 3 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

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
