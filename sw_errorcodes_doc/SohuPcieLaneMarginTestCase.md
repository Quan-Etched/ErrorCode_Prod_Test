# SohuPcieLaneMarginTestCase 错误码

由 `SohuPcieLaneMarginTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PCIE-0007: PCIE_LANE_MARGIN_BELOW_THRESHOLD](#TH-PCIE-0007)

<a id="TH-PCIE-0007"></a>
## TH-PCIE-0007: PCIE_LANE_MARGIN_BELOW_THRESHOLD

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0007` |
| 名称 | `PCIE_LANE_MARGIN_BELOW_THRESHOLD` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.PCIE.LINK` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

PCIe 通道裕量低于阈值（EH>25mV、EW>0.2UI，暂定）。

### 测试用例

`SohuPcieLaneMarginTestCase`

### 可能原因

- 一条或多条通道上的 PCIe 通道处于边缘状态
- 阈值仍在评审中（暂定）

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
