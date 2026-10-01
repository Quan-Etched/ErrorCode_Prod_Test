# SohuUartTestCase 错误码

由 `SohuUartTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0006: UART_PING_LOG_MISMATCH](#TH-SOHU-0006)

<a id="TH-SOHU-0006"></a>
## TH-SOHU-0006: UART_PING_LOG_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0006` |
| 名称 | `UART_PING_LOG_MISMATCH` |
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
| 组件 | `1X.SOHU.UART` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

UART ping 日志消息缺失，或内容不匹配。

### 测试用例

`SohuUartTestCase`

### 可能原因

- 模块上的 UART 通路故障
- 固件未产生启动日志

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
