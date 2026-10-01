# C2cLinkupTestCase 错误码

由 `C2cLinkupTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-C2C-0001: C2C_LINKUP_FAILED](#TH-C2C-0001)

<a id="TH-C2C-0001"></a>
## TH-C2C-0001: C2C_LINKUP_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-C2C-0001` |
| 名称 | `C2C_LINKUP_FAILED` |
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
| 组件 | `1X.C2C.SOHU_SERDES` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

C2C 通道未能在超时内完成训练或链路建立：RX 均衡在配置的尝试次数后仍未收敛，或链路建立测试报告一条或多条数据链路/通道 down。

### 测试用例

`C2cLinkupTestCase`, `C2cLinkupMultiChipTestCase`, `C2cThroughputTestCase`, `C2cThroughputMultiChipTestCase`

### 可能原因

- 模块上存在边缘 SERDES TX/RX 通道
- 前序扫描得到的 FIR taps 对该速率/FEC 模式无效
- 工位上的环回治具或线缆未就位
- 请求的 FEC 模式下 PHY 配置不匹配

### 采集项

- suite_run_url
- 链路建立测试输出目录（逐通道 PoR 摘要）
- affected_instances 中受影响的数据链路/通道
- 本次运行的 fec_mode、phy_loopback_mode 与 mac_loopback 标志
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
