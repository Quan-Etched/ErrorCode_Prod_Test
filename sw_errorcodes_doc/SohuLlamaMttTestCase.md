# SohuLlamaMttTestCase 错误码

由 `SohuLlamaMttTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PWR-0006: VMIN_ABOVE_RATED_LIMIT](#TH-PWR-0006)
- [TH-PWR-0007: UNEXPECTED_DVFS_RAMPDOWN](#TH-PWR-0007)
- [TH-SOHU-0015: WORKLOAD_HANG_OPERATION_TIMEOUT](#TH-SOHU-0015)
- [TH-SOHU-0017: INFERENCE_DISPATCH_TIME_ABOVE_LIMIT](#TH-SOHU-0017)

<a id="TH-PWR-0006"></a>
## TH-PWR-0006: VMIN_ABOVE_RATED_LIMIT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0006` |
| 名称 | `VMIN_ABOVE_RATED_LIMIT` |
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
| 处置结果 | 失败 |
| 组件 | `1X.PWR.VMIN` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

某条 SA/SAU 电源轨的 Vmin 高于额定限值。

### 测试用例

`SohuLlamaMttTestCase`

### 可能原因

- 硅片处于边缘状态，所需电压高于额定值
- 负载下电源轨压降过大

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

<a id="TH-PWR-0007"></a>
## TH-PWR-0007: UNEXPECTED_DVFS_RAMPDOWN

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0007` |
| 名称 | `UNEXPECTED_DVFS_RAMPDOWN` |
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
| 组件 | `1X.PWR.DVFS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

工作负载期间出现非预期的 DVFS 降频事件。

### 测试用例

`SohuLlamaMttTestCase`, `SohuPowerVirusTestCase`

### 可能原因

- 功耗或温度越限触发 DVFS
- 电源轨在工作负载瞬态下处于边缘状态

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

<a id="TH-SOHU-0015"></a>
## TH-SOHU-0015: WORKLOAD_HANG_OPERATION_TIMEOUT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0015` |
| 名称 | `WORKLOAD_HANG_OPERATION_TIMEOUT` |
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
| 组件 | `1X.SOHU.WORKLOAD` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

工作负载挂起，或操作超时。

### 测试用例

`KayakTestCase`, `SohuPowerVirusTestCase`, `SohuLlamaMttTestCase`

### 可能原因

- SOHU 工作负载或操作未在超时时间内完成

### 采集项

- suite_run_url
- 逐测试日志与记录
- 恢复前捕获的器件状态
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

<a id="TH-SOHU-0017"></a>
## TH-SOHU-0017: INFERENCE_DISPATCH_TIME_ABOVE_LIMIT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0017` |
| 名称 | `INFERENCE_DISPATCH_TIME_ABOVE_LIMIT` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SOHU.ASIC` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

百万 token 测试上的持续推理吞吐未达到预期的芯片 tokens/s（套件 expected_chip_tokens_per_second 的 95%）。尚未接入：该检查在 llama_mtt_app 内部运行，harness 只能看到退出状态，因此非零退出无法与模型创建失败或数据集失败区分。要发出该错误码，需要二进制以可区分的方式指示阈值失败，或者由 harness 解析 MTT_results/metrics.txt。

### 测试用例

`SohuLlamaMttTestCase`

### 可能原因

- 芯片在持续负载下维持的时钟低于预期
- 运行期间发生热或功耗限频
- 处于边缘状态的 SA/HBM 通路降低了有效推理速率

### 采集项

- suite_run_url
- 含实测 tokens/s 的完整 llama_mtt_app stdout/stderr
- 配置的 expected_chip_tokens_per_second 以及 0.95 下限
- 监视器在运行期间采集的 DVFS 与温度遥测
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
