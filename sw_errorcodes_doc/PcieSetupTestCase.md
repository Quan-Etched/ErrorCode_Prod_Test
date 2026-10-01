# PcieSetupTestCase 错误码

由 `PcieSetupTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PCIE-0008: SOHU_ENDPOINT_NOT_ENUMERATED](#TH-PCIE-0008)

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

Sohu 端点未枚举（未出现在 PCIe 树 / RPC 代理中）。

### 测试用例

`PcieSetupTestCase`、`SohuVfioPingTestCase`、`SohuSaScreeningTestCase`

### 可能原因

- Sohu 端点未出现在 PCIe 树或 RPC 代理中

### 采集项

- suite_run_url
- 单次测试日志与转录
- PCIe 拓扑与 RPC 代理状态
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑 PCIe 线缆未完全插入 PV1 板，重新插接线缆并复测一次。 | affected_subset | 10 | — |

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
