# SohuVrmTestCase 错误码

由 `SohuVrmTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PWR-0002: POWER_TELEMETRY_UNAVAILABLE](#TH-PWR-0002)
- [TH-PWR-0003: POWER_DATA_OUT_OF_RANGE](#TH-PWR-0003)

<a id="TH-PWR-0002"></a>
## TH-PWR-0002: POWER_TELEMETRY_UNAVAILABLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0002` |
| 名称 | `POWER_TELEMETRY_UNAVAILABLE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.PWR.VBB_POWER` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

功耗遥测不可用（VBB / VRM / VM 传感器 RPC / 采集器无响应，或读数响应中缺少预期的 VM 传感器）。

### 测试用例

`SohuPowerTelemetryTestCase`, `SohuVrmTestCase`, `SohuVmTestCase`

### 可能原因

- 黄金 VBB 治具上的 VBB 通信失败
- 读取 VM 传感器时 Sohu DVFS RPC 失败
- 遥测采集器未运行

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

<a id="TH-PWR-0003"></a>
## TH-PWR-0003: POWER_DATA_OUT_OF_RANGE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0003` |
| 名称 | `POWER_DATA_OUT_OF_RANGE` |
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
| 组件 | `1X.PWR.VBB_POWER` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

功耗数据超出合格范围，或 CPLD 报告夹层板上存在活动的 VRM 状态机故障。

### 测试用例

`SohuPowerTelemetryTestCase`, `SohuVrmTestCase`

### 可能原因

- 模块供电超出合格包络
- 负载下电源轨故障
- 夹层板 CPLD 的 VRM 时序故障

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
