# MezzanineI2cAlertsTestCase 错误码

由 `MezzanineI2cAlertsTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-MEZZ-0002: UNEXPECTED_MEZZANINE_I2C_ALERT](#TH-MEZZ-0002)

<a id="TH-MEZZ-0002"></a>
## TH-MEZZ-0002: UNEXPECTED_MEZZANINE_I2C_ALERT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-MEZZ-0002` |
| 名称 | `UNEXPECTED_MEZZANINE_I2C_ALERT` |
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
| 组件 | `1X.MEZZ.I2C` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

意外的夹层板 I2C 告警被断言。

### 测试用例

`MezzanineI2cAlertsTestCase`

### 可能原因

- 意外的夹层板 I2C 告警状态

### 采集项

- suite_run_url
- 单次测试日志与转录
- 夹层板遥测数据
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 疑似测试问题，复测一次。 | affected_subset | 10 | — |

### 疑似组件

`MEZZ`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
