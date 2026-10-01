# SohuDtsTestCase 错误码

由 `SohuDtsTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-THM-0001: THERMAL_READING_OUT_OF_RANGE](#TH-THM-0001)
- [TH-THM-0002: DTS_SENSOR_VARIATION_EXCEEDED](#TH-THM-0002)
- [TH-THM-0005: DTS_PTP_DEVIATION_OUT_OF_BOUNDS](#TH-THM-0005)

<a id="TH-THM-0001"></a>
## TH-THM-0001: THERMAL_READING_OUT_OF_RANGE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0001` |
| 名称 | `THERMAL_READING_OUT_OF_RANGE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `MLT.THM.SOHU_CHIP` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

热二极管温度读数超出合格范围、被传感器报告为无效，或未校准的夹层板二极管读数低于 0 °C（焊点不良的指示）。失败通道写入消息 / affected_instances，不会拆成新的错误码（规范 §1.2）。

### 测试用例

`SohuThermalDiodeTestCase`, `SohuDtsTestCase`

### 可能原因

- 热加压头未贴合 / 接触不良
- 未校准的夹层板二极管通道焊点不良
- TMP464 传感器或 ASIC 远程二极管故障
- 工位环境温度超出规格

### 采集项

- suite_run_url
- 逐通道温度与有效标志（已记录的测量值）
- 配置的最小/最大界限
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 检查 IBC TIM，并确认 Sohu 模块已正确装入治具并固定到位。 |  | 5 | — |
| 2 | 操作员 | 同时确认 Sohu 模块顶部冷板已连接到 HRM 冷却回路。 |  | 5 | — |
| 3 | 操作员 | 若未发现异常，复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`MEZZ_MODULE`, `THERMAL_HEAD`, `SOHU_CHIP`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-THM-0002"></a>
## TH-THM-0002: DTS_SENSOR_VARIATION_EXCEEDED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0002` |
| 名称 | `DTS_SENSOR_VARIATION_EXCEEDED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.THM.DTS` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

可用 Sohu DTS 读数的峰峰值跨度超过了配置的偏差限值（L10 为 20°C）。读数为零和已报故障的传感器不计入该跨度，因此它反映的是真实的传感器之间差异。

### 测试用例

`SohuDtsTestCase`

### 可能原因

- 热加压头在裸片上贴合不均匀
- TIM 空洞或键合线厚度不均
- DTS 传感器有缺陷，读数偏高或偏低，但仍报告无故障

### 采集项

- suite_run_url
- 各传感器换算后的读数以及计算出的 peak_to_peak 值
- 本次运行配置的偏差限值
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 检查 IBC TIM，并确认 Sohu 模块已正确装入治具并固定到位。 |  | 5 | — |
| 2 | 操作员 | 同时确认 Sohu 模块顶部冷板已连接到 HRM 冷却回路。 |  | 5 | — |
| 3 | 操作员 | 若未发现异常，复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`SOHU_ASIC`, `THERMAL_HEAD`, `TIM`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-THM-0005"></a>
## TH-THM-0005: DTS_PTP_DEVIATION_OUT_OF_BOUNDS

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0005` |
| 名称 | `DTS_PTP_DEVIATION_OUT_OF_BOUNDS` |
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
| 组件 | `1X.THM.DTS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Power Virus 下的 DTS 峰峰值偏差超出界限（阈值仍在评审中；界限可能会提高）。

### 测试用例

`SohuDtsTestCase`, `SohuPowerVirusTestCase`

### 可能原因

- TIM 或热加压头接触差异
- 阈值仍在评审中
- TIM 烘烤时长已从 15 分钟更新为 45 分钟。

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 若任何温度读数超出规格，确认受影响单板已完成所要求的 45 分钟 TIM 烘烤流程。 |  | 5 | — |
| 2 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 3 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

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
