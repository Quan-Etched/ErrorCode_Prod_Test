# ServerNestedTestCase 错误码

由 `ServerNestedTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HAR-0002: TEST_ARGS_INVALID](#TH-HAR-0002)
- [TH-HAR-0004: NESTED_SUITE_ORCHESTRATION_FAILED](#TH-HAR-0004)

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

测试用例以无效或不支持的参数调用（例如意外的 kwargs、不支持的模式），并在接触 DUT 之前拒绝本次运行。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`, `ServerNestedTestCase`, `SohuSnapTestCase`, `VfioProxyVersionTestCase`, `SohuWeightLoadTestCase`, `SltModuleNestedTestCase`

### 可能原因

- 套件 YAML 传入了测试不接受的参数
- 套件 YAML 请求了测试不支持的模式/路径

### 采集项

- suite_run_url
- 逐测日志中的问题参数
- harness_version, station_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 工程师 | 修复该测试的套件 YAML；不要将单元送去返工 |  |  | — |

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

<a id="TH-HAR-0004"></a>
## TH-HAR-0004: NESTED_SUITE_ORCHESTRATION_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HAR-0004` |
| 名称 | `NESTED_SUITE_ORCHESTRATION_FAILED` |
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
| 组件 | `1X.HAR.NESTED_SUITE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

嵌套套件未能启动或完成编排（容器镜像加载、API 就绪/配置、中止/关闭、缺少 kv_store 输入或资源接线）。子测试失败携带各自的错误码；对于已运行并失败的内部套件，包装器从不签发此码。`SltModuleNestedTestCase` 上未填充的芯片槽位仍为 SKIP（不是此码）。

### 测试用例

`ServerNestedTestCase`, `SltModuleNestedTestCase`

### 可能原因

- 嵌套包装器中的套件配置或资源接线错误
- 子套件根本无法启动
- 容器运行时/镜像加载或内部 harness API 失败

### 采集项

- suite_run_url
- 逐测日志与 transcript
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 检查套件配置/资源；包装器必须传播首个/最严重的子错误码——切勿为子失败签发重复码（测试系统 ERROR——不计入良率） |  |  | — |

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
