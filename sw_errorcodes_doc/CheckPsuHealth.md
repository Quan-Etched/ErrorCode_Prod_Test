# CheckPsuHealth 错误码

由 `CheckPsuHealth` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PWR-0001: STATION_PSU_LOAD_IMBALANCE](#TH-PWR-0001)

<a id="TH-PWR-0001"></a>
## TH-PWR-0001: STATION_PSU_LOAD_IMBALANCE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0001` |
| 名称 | `STATION_PSU_LOAD_IMBALANCE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 2 — 热重启 |
| 处置结果 | 错误 |
| 组件 | `1X.PWR.STATION_PSU` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

工位 PSU 负载不平衡超过 5%，或出现 PGOOD 故障（治具问题；不计入模块良率）。

### 测试用例

`CheckPsuHealth`

### 可能原因

- Devkit 机箱 PSU 劣化或不平衡
- 工位电源线缆问题

### 采集项

- suite_run_url
- 各测试的日志与 transcript
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 已知 Devkit 间歇性问题，复测一次。 | 受影响子集 | 10 | — |

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
