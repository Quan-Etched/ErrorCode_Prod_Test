# SohuJtagTestCase 错误码

由 `SohuJtagTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0007: JTAG_READBACK_MISMATCH](#TH-SOHU-0007)

<a id="TH-SOHU-0007"></a>
## TH-SOHU-0007: JTAG_READBACK_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0007` |
| 名称 | `JTAG_READBACK_MISMATCH` |
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
| 组件 | `1X.SOHU.JTAG` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

JTAG 检查未得到预期值，或根本无法读出：包括 ARC 核的 cluster_id、SA 行列构建配置，或无法在链上选择某个核或读取某个寄存器。core1_cpu_reset 的读取仅作为诊断测量记录，从不导致测试失败。任何 JTAG 事务发生之前的失败改用 harness 错误码：未知的 jtag_interface 为 TH-HAR-0002；没有匹配 serial_prefix 的适配器，或缺少 OpenOCD 二进制文件，为 TH-HAR-0003。

### 测试用例

`SohuJtagTestCase`

### 可能原因

- ASIC 上的 ARC 核或 SA 互连处于边缘状态或存在缺陷
- 模块上的 JTAG 链完整性问题

### 采集项

- suite_run_url
- 含每个寄存器期望值与读回值的逐测试日志
- 运行窗口内的 OpenOCD 记录
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
