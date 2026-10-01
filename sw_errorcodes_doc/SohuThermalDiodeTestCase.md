# SohuThermalDiodeTestCase 错误码

由 `SohuThermalDiodeTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-THM-0001: THERMAL_READING_OUT_OF_RANGE](#TH-THM-0001)
- [TH-THM-0007: THERMAL_TELEMETRY_UNAVAILABLE](#TH-THM-0007)

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

<a id="TH-THM-0007"></a>
## TH-THM-0007: THERMAL_TELEMETRY_UNAVAILABLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0007` |
| 名称 | `THERMAL_TELEMETRY_UNAVAILABLE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 7 — 软件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `MLT.THM.SOHU_CHIP` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

无法获得 TMP464 热二极管数据：经 VBB UART 的 RPC/连接失败，或响应格式错误（缺少温度数组、通道数量非预期）。热判定结果不确定。

### 测试用例

`SohuThermalDiodeTestCase`

### 可能原因

- VBB UART/RPC 通信失败（共用测试台 UART 争用）
- VBB 或传感器固件故障，返回格式错误的 TMP464 数据

### 采集项

- suite_run_url
- 逐测试日志中的 RPC 错误或格式错误的响应
- unit_sn, fw_version, harness_version, station_id, timestamp

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
