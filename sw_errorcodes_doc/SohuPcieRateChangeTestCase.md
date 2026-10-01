# SohuPcieRateChangeTestCase 错误码

由 `SohuPcieRateChangeTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PCIE-0001: PCIE_LINK_STATE_MISMATCH](#TH-PCIE-0001)
- [TH-PCIE-0002: PCIE_AER_ERRORS_DETECTED](#TH-PCIE-0002)
- [TH-PCIE-0006: PCIE_SPEED_CHANGE_FAILED](#TH-PCIE-0006)

<a id="TH-PCIE-0001"></a>
## TH-PCIE-0001: PCIE_LINK_STATE_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0001` |
| 名称 | `PCIE_LINK_STATE_MISMATCH` |
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
| 组件 | `1X.PCIE.LINK` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

PCIe 链路状态不匹配：Sohu 端点链路不是 L0 / Gen5 / x16。

### 测试用例

`SohuPcieAerCheckTestCase`, `SohuPcieRateChangeTestCase`

### 可能原因

- PCIe 链路降级，或以更低速率/宽度重新训练
- PCIe 通道处于边缘状态，或连接器未插到位

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑 PCIe 线缆未完全插入 PV1 板，重新插拔线缆并复测一次。 | 受影响子集 | 10 | — |

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

<a id="TH-PCIE-0002"></a>
## TH-PCIE-0002: PCIE_AER_ERRORS_DETECTED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0002` |
| 名称 | `PCIE_AER_ERRORS_DETECTED` |
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
| 组件 | `1X.PCIE.LINK` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

检测到 PCIe AER 错误（可纠正或不可纠正）。

### 测试用例

`SohuPcieAerCheckTestCase`, `SohuPcieRateChangeTestCase`

### 可能原因

- 处于边缘状态的 PCIe 通道产生可纠正错误
- 连接器污染或未插到位

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑 PCIe 线缆未完全插入 PV1 板，重新插拔线缆并复测一次。 | 受影响子集 | 10 | — |

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

<a id="TH-PCIE-0006"></a>
## TH-PCIE-0006: PCIE_SPEED_CHANGE_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0006` |
| 名称 | `PCIE_SPEED_CHANGE_FAILED` |
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
| 组件 | `1X.PCIE.LINK` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

PCIe 速率切换失败（Gen5 与 Gen1 之间的切换未完成）。

### 测试用例

`SohuPcieRateChangeTestCase`

### 可能原因

- 在目标速率下链路训练失败
- Gen5 下的 PCIe 通道处于边缘状态

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑 PCIe 线缆未完全插入 PV1 板，重新插拔线缆并复测一次。 | 受影响子集 | 10 | — |

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
