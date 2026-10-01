# C2cLaneMarginTestCase 错误码

由 `C2cLaneMarginTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-C2C-0004: C2C_LANE_MARGIN_BELOW_THRESHOLD](#TH-C2C-0004)

<a id="TH-C2C-0004"></a>
## TH-C2C-0004: C2C_LANE_MARGIN_BELOW_THRESHOLD

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-C2C-0004` |
| 名称 | `C2C_LANE_MARGIN_BELOW_THRESHOLD` |
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
| 组件 | `1X.C2C.SOHU_SERDES` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

眼图扫描得到的最差逐通道最小 BER 超过了配置的 ber_threshold。SERDES 裕量规格尚未最终确定，因此本错误码严重级别为 4（分诊）而非直接隔离：在对模块做出处置结果前，请对照当前规格予以确认。

### 测试用例

`C2cLaneMarginTestCase`

### 可能原因

- 模块上存在边缘 SERDES 通道（眼图闭合）
- 眼图扫描阈值严于（尚未最终确定的）SERDES 规格
- PRBS 码型或速率与工位治具不匹配
- 环回治具插入损耗超出规格

### 采集项

- suite_run_url
- 眼图扫描输出目录（逐通道 BER 矩阵）
- lane_margin_worst_min_ber 测量值及逐通道明细
- affected_instances 中受影响的通道
- unit_sn, bios/fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_SERDES`, `C2C_LOOPBACK_FIXTURE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
