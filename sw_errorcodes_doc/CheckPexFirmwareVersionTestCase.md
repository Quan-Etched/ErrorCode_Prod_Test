# CheckPexFirmwareVersionTestCase 错误码

由 `CheckPexFirmwareVersionTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-ENV-0002: STATION_FIXTURE_SETUP_CHECK_FAILED](#TH-ENV-0002)
- [TH-ENV-0003: PLX_DAEMON_NO_PEX_SWITCHES](#TH-ENV-0003)

<a id="TH-ENV-0002"></a>
## TH-ENV-0002: STATION_FIXTURE_SETUP_CHECK_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-ENV-0002` |
| 名称 | `STATION_FIXTURE_SETUP_CHECK_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.ENV.STATION_FIXTURE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

工位治具/环境检查失败（Chroma 遥测 / 评估板电源 / vfio-proxy 版本查询或版本不匹配 / PEX 版本）。

### 测试用例

`ChromaTelemetryCheckTestCase`, `EvalBoardPowerTestCase`, `VfioProxyVersionTestCase`, `CheckPexFirmwareVersionTestCase`

### 可能原因

- 工位治具或环境尚未就绪，无法进行模块测试
- vfio-proxy gRPC 不可达，或报告了意外的版本

### 采集项

- suite_run_url
- 各测试的日志与 transcript
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。请勿复测。 |  |  | — |

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

<a id="TH-ENV-0003"></a>
## TH-ENV-0003: PLX_DAEMON_NO_PEX_SWITCHES

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-ENV-0003` |
| 名称 | `PLX_DAEMON_NO_PEX_SWITCHES` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.ENV.PEX_SWITCH` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

PLX daemon 报告未发现 PEX 交换机。

### 测试用例

`CheckPexFirmwareVersionTestCase`

### 可能原因

- VBB MCU 固件未更新到所需版本
- PLX daemon 无法使用 PEX 交换机

### 采集项

- suite_run_url
- 各测试的日志与 transcript
- VBB MCU 固件版本
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。请勿复测。 |  |  | — |

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
