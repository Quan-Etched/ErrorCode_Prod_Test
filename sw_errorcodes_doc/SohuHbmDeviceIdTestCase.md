# SohuHbmDeviceIdTestCase 错误码

由 `SohuHbmDeviceIdTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HBM-0007: HBM_DEVICE_ID_READ_FAIL](#TH-HBM-0007)

<a id="TH-HBM-0007"></a>
## TH-HBM-0007: HBM_DEVICE_ID_READ_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HBM-0007` |
| 名称 | `HBM_DEVICE_ID_READ_FAIL` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 11 — 数据 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.HBM.STACK` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

无法从每个 HBM 堆栈读出 IEEE 1500 DRAM 器件 ID，或报告的堆栈拓扑与预期堆栈数量不符。涵盖无法读取的器件 ID（RPC 错误、超时或非预期响应），以及报告的系统信息中缺少通道 ID 或堆栈数量错误。

### 测试用例

`SohuHbmDeviceIdTestCase`

### 可能原因

- HBM 堆栈在其 IEEE 1500 端口上无响应
- 堆栈缺失、装配错误，或在启动期间未完成训练
- 受影响堆栈上的 Sohu HBM 控制器故障

### 采集项

- suite_run_url
- 标出失败堆栈及底层错误的逐测试日志
- 报告的 HBM 系统信息（堆栈数量与通道 ID）
- 记录的逐堆栈 serial_number / manufacturer / density 测量值
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`HBM_STACK`, `ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
