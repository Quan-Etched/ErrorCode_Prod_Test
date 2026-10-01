# SohuLlama8bFp8ForwardTestCase 错误码

由 `SohuLlama8bFp8ForwardTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0018: END_TO_END_INFERENCE_NUMERIC_MISMATCH](#TH-SOHU-0018)

<a id="TH-SOHU-0018"></a>
## TH-SOHU-0018: END_TO_END_INFERENCE_NUMERIC_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0018` |
| 名称 | `END_TO_END_INFERENCE_NUMERIC_MISMATCH` |
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
| 组件 | `1X.SOHU.INFERENCE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

端到端推理数值与参考值不匹配。

### 测试用例

`SohuLlama8bFp8PrefillTestCase`, `SohuLlama8bFp8ForwardTestCase`, `SohuLlamaForwardIteratedTestCase`, `KayakTestCase`

### 可能原因

- SOHU 推理输出与预期参考值不一致

### 采集项

- suite_run_url
- 逐测试日志与记录
- 数值比较输出
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
