# SohuMtcStressTestCase 错误码

由 `SohuMtcStressTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HBM-0004: HBM_MTC_STRESS_FAILURE](#TH-HBM-0004)

<a id="TH-HBM-0004"></a>
## TH-HBM-0004: HBM_MTC_STRESS_FAILURE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HBM-0004` |
| 名称 | `HBM_MTC_STRESS_FAILURE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 3 — 内存 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.HBM.STACK` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

HBM MTC 压力测试失败。

### 测试用例

`SohuMtcStressTestCase`

### 可能原因

- HBM 堆栈在压力下出现故障
- 伪通道在该速率下处于边缘状态

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑是测试问题，复测一次。 | 受影响子集 | 10 | — |

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
