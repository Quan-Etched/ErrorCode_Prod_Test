# SohuVfioPingTestCase 错误码

由 `SohuVfioPingTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PCIE-0008: SOHU_ENDPOINT_NOT_ENUMERATED](#TH-PCIE-0008)
- [TH-SOHU-0002: SOHU_NOT_PINGABLE](#TH-SOHU-0002)
- [TH-SOHU-0027: VFIO_PING_LATENCY_OUT_OF_SPEC](#TH-SOHU-0027)

<a id="TH-PCIE-0008"></a>
## TH-PCIE-0008: SOHU_ENDPOINT_NOT_ENUMERATED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0008` |
| 名称 | `SOHU_ENDPOINT_NOT_ENUMERATED` |
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
| 组件 | `1X.PCIE.ENUMERATION` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

Sohu 端点未被枚举（未出现在 PCIe 树 / RPC 代理中）。

### 测试用例

`PcieSetupTestCase`, `SohuVfioPingTestCase`, `SohuSaScreeningTestCase`

### 可能原因

- Sohu 端点未出现在 PCIe 树或 RPC 代理中

### 采集项

- suite_run_url
- 逐测试日志与记录
- PCIe 拓扑与 RPC 代理状态
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑 PCIe 线缆未完全插入 PV1 板，重新插拔线缆并复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`PCIE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

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

<a id="TH-SOHU-0027"></a>
## TH-SOHU-0027: VFIO_PING_LATENCY_OUT_OF_SPEC

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0027` |
| 名称 | `VFIO_PING_LATENCY_OUT_OF_SPEC` |
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
| 组件 | `1X.SOHU.ASIC` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

已收到 VFIO ping 响应，但没有一次满足允许的延迟：器件可以 ping 通，但其响应延迟超出规格。与 TH-SOHU-0002（完全没有响应）不同。

### 测试用例

`SohuVfioPingTestCase`

### 可能原因

- 处于边缘状态的 PCIe 链路或器件响应通路增加了延迟
- 器件处于非预期负载下，或处于降级状态

### 采集项

- suite_run_url
- 测试日志中的逐次 ping 延迟结果
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
