# SohuBusConnectivityTestCase 错误码

由 `SohuBusConnectivityTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0010: BUS_CONNECTIVITY_CSR_ACCESS_FAIL](#TH-SOHU-0010)

<a id="TH-SOHU-0010"></a>
## TH-SOHU-0010: BUS_CONNECTIVITY_CSR_ACCESS_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0010` |
| 名称 | `BUS_CONNECTIVITY_CSR_ACCESS_FAIL` |
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
| 组件 | `1X.SOHU.SOC_BUS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

驻留在 mCPU 上的总线连通性扫描报告的失败计数非零：跨 SoC 各模块（MCPU、ISC、IPU、CSRAM、WCU、GPIO、PAD、sensors hub、PCIe、SAMU、datalink、MAC）的 CSR 检查中，至少有一项未通过。检查失败的原因要么是写/校验/恢复读回没有返回所写入的模式，要么是只读字段没有保持其预期值。

### 测试用例

`SohuBusConnectivityTestCase`

### 可能原因

- 内部总线上的 CSR 块有缺陷，或寄存器从设备不可达
- 受影响模块的时钟或复位未被释放
- 被测件使用了错误的固件镜像或芯片变体（构建配置字段不匹配）

### 采集项

- suite_run_url
- 含逐寄存器 FAIL 行的 mCPU 日志（地址、位位置/宽度、期望值与实际值）
- tests_run / tests_failed 测量值
- 用于 affected_instances 的失败 CSR 块
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
