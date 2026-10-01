# KvFlushAndAttentionInterleavedSingleChipTestCase 错误码

由 `KvFlushAndAttentionInterleavedSingleChipTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0014: ATTENTION_SAU_NUMERIC_MISMATCH](#TH-SOHU-0014)

<a id="TH-SOHU-0014"></a>
## TH-SOHU-0014: ATTENTION_SAU_NUMERIC_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0014` |
| 名称 | `ATTENTION_SAU_NUMERIC_MISMATCH` |
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
| 组件 | `1X.SOHU.SAU` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

attention/SAU 调度器测试二进制以非零退出：一次或多次 attention、KV-flush 或 SAU 操作与 funcsim 参考结果不匹配。

### 测试用例

`RunAllAttnTestsSingleChipTestCase`, `RunAllAttnHbmBypassTestsSingleChipTestCase`, `RunKvFlushTestsSingleChipTestCase`, `KvFlushAndAttentionSingleChipTestCase`, `KvFlushAndAttentionInterleavedSingleChipTestCase`

### 可能原因

- 有缺陷的 SAU 宏（PPU / WSSA / SCSA / softmax）产生错误结果
- KV cache 读/写路径故障
- 被测 SAU 区域的电压或时钟处于边缘状态

### 采集项

- suite_run_url
- 含二进制不匹配输出的单测日志
- affected_instances 的失败 block/macro
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
