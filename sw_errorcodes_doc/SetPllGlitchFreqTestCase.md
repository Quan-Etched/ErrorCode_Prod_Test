# SetPllGlitchFreqTestCase 错误码

由 `SetPllGlitchFreqTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0020: SAU_PLL_CONFIG_FAIL](#TH-SOHU-0020)
- [TH-SOHU-0026: PLL_GLITCH_FREQUENCY_READBACK_FAILED](#TH-SOHU-0026)

<a id="TH-SOHU-0020"></a>
## TH-SOHU-0020: SAU_PLL_CONFIG_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0020` |
| 名称 | `SAU_PLL_CONFIG_FAIL` |
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
| 组件 | `MLT.SOHU.SOHU_CHIP` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

SAU/SA PLL 配置失败——固件在 FLR 后未报告安全的 SAU PLL 相位对齐，或请求的 PLL glitch 频率在回读超时前未能回读到目标值的 5% 以内。

### 测试用例

`SohuSauPllPhaseAlignmentTestCase`, `SetPllGlitchFreqTestCase`

### 可能原因

- SAU/SA PLL 处于临界状态，未能锁定到安全相位
- DVFS/PLL 控制路径故障（glitch 频率未生效）
- 固件相位搜索未运行或报告失败（见 ETCH-35301）

### 采集项

- suite_run_url
- core_reset_handler 日志摘录
- DVFS zone 频率回读（请求值 vs 实际值）
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_CHIP`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-SOHU-0026"></a>
## TH-SOHU-0026: PLL_GLITCH_FREQUENCY_READBACK_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0026` |
| 名称 | `PLL_GLITCH_FREQUENCY_READBACK_FAILED` |
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
| 组件 | `1X.SOHU.PLL` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

PLL glitch 频率在超时前未能回读到目标值的 5% 以内。

### 测试用例

`SetPllGlitchFreqTestCase`

### 可能原因

- PLL 未能在请求的 glitch 频率下锁定
- DVFS 控制路径故障

### 采集项

- suite_run_url
- 逐测日志与 transcript
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
