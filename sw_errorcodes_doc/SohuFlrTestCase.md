# SohuFlrTestCase 错误码

由 `SohuFlrTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0002: SOHU_NOT_PINGABLE](#TH-SOHU-0002)
- [TH-SOHU-0019: FLR_FAILED](#TH-SOHU-0019)

<a id="TH-SOHU-0002"></a>
## TH-SOHU-0002: SOHU_NOT_PINGABLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0002` |
| 名称 | `SOHU_NOT_PINGABLE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SOHU.ASIC` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Sohu 器件未通过 RPC 代理响应 ping：固件未在运行、不可达，或器件已从代理上掉线。当一个曾经正常上报的器件停止应答时发出，例如重复 FLR 运行之后的收尾扫描。

### 测试用例

`SohuFlrTestCase`, `SohuVfioPingTestCase`, `SaSortRampupHbmSingleChipTestCase`, `SohuWeightLoadTestCase`

### 可能原因

- Sohu 固件挂起或崩溃，停止处理 RPC
- 器件从 PCIe 树 / vfio 代理上掉线
- 复位或上电时序处于边缘状态，使 ASIC 无响应

### 采集项

- suite_run_url
- 标出无响应器件索引的逐测试日志
- 运行窗口内的 UART 日志
- 失败时刻的 lspci / 代理器件列表
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`ASIC`, `MEZZ_MODULE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-SOHU-0019"></a>
## TH-SOHU-0019: FLR_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0019` |
| 名称 | `FLR_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SOHU.PCIE_FLR` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

一次功能级复位（FLR）周期未能干净完成：复位请求失败，或在 flr_timeout_s（默认 5.0 秒）内没有应答；或者器件未能在 recovery_timeout_s（默认 10.0 秒）内重新变为可用并可 ping。针对 FLR 批次中第一次失败的迭代报告；各次迭代的往返时间记录为 flr_round_trip_* 测量值，不与限值比较。

### 测试用例

`SohuFlrTestCase`

### 可能原因

- Sohu 固件在 FLR 之后未能干净地重新初始化
- PCIe 链路未能在恢复窗口内重新训练
- 模块上的复位或上电时序处于边缘状态

### 采集项

- suite_run_url
- 含失败迭代索引与实测 FLR 时长的逐测试日志
- 失败复位之后的 PCIe 链路状态与 lspci 输出
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`ASIC`, `MEZZ_MODULE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
