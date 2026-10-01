# C2cIntegrityMultiChipTestCase 错误码

由 `C2cIntegrityMultiChipTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-C2C-0002: C2C_LOOPBACK_DATA_INTEGRITY_MISMATCH](#TH-C2C-0002)

<a id="TH-C2C-0002"></a>
## TH-C2C-0002: C2C_LOOPBACK_DATA_INTEGRITY_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-C2C-0002` |
| 名称 | `C2C_LOOPBACK_DATA_INTEGRITY_MISMATCH` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 11 — 数据 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.C2C.SOHU_SERDES` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

逐位 C2C 环回比对发现至少一条数据链路/通道存在数据不匹配。

### 测试用例

`C2cIntegrityTestCase`, `C2cIntegrityMultiChipTestCase`

### 可能原因

- 边缘 SERDES 通道在负载下损坏数据
- 该通道上 FEC 未能按配置速率完成纠错
- 环回通道映射与治具接线不一致
- 模块上的 CSRAM/WDMA 数据通路缺陷

### 采集项

- suite_run_url
- 完整性测试输出目录（逐通道错误曲线图）
- 任何重试之前捕获的逐通道不匹配数据
- affected_instances 中受影响的数据链路/通道
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
