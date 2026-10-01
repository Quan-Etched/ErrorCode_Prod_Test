# SohuSnapTestCase 错误码

由 `SohuSnapTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HAR-0002: TEST_ARGS_INVALID](#TH-HAR-0002)
- [TH-SOHU-0025: CHIP_STATE_SNAPSHOT_FAILED](#TH-SOHU-0025)

<a id="TH-HAR-0002"></a>
## TH-HAR-0002: TEST_ARGS_INVALID

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HAR-0002` |
| 名称 | `TEST_ARGS_INVALID` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `L10.HAR.HARNESS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

测试用例以无效或不支持的参数被调用（例如意外的 kwargs、不支持的模式），并在接触被测件之前拒绝了本次运行。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`, `ServerNestedTestCase`, `SohuSnapTestCase`, `VfioProxyVersionTestCase`, `SohuWeightLoadTestCase`, `SltModuleNestedTestCase`

### 可能原因

- 套件 YAML 传入了测试不接受的参数
- 套件 YAML 请求了测试不支持的模式或路径

### 采集项

- suite_run_url
- 逐测试日志中的问题参数
- harness_version, station_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 工程师 | 修正本测试的套件 YAML；不要把单板送去返修 |  |  | — |

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

<a id="TH-SOHU-0025"></a>
## TH-SOHU-0025: CHIP_STATE_SNAPSHOT_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0025` |
| 名称 | `CHIP_STATE_SNAPSHOT_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SOHU.SNAPSHOT` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

芯片状态快照采集失败。

### 测试用例

`SohuSnapTestCase`

### 可能原因

- 芯片未响应快照请求
- 快照工具故障

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

`SOHU_ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
