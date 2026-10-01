# SohuI2cTestCase 错误码

由 `SohuI2cTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0004: I2C_PERIPHERAL_READ_FAIL](#TH-SOHU-0004)

<a id="TH-SOHU-0004"></a>
## TH-SOHU-0004: I2C_PERIPHERAL_READ_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0004` |
| 名称 | `I2C_PERIPHERAL_READ_FAIL` |
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
| 组件 | `1X.SOHU.MEZZ_I2C` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Sohu 夹层板上的 I2C 事务失败。这既包括启动阶段（初始化 ASIC 调试 mux 或四个 Sohu I2C 控制器中的任意一个，以及读取夹层板类型），也包括 I2C0–I2C3 上的逐设备探测：探测要么事务失败，要么返回的数据与预期的器件标识/寄存器值不符。第一次失败即结束测试；若是探测失败，日志会标出总线、器件和地址。

### 测试用例

`SohuI2cTestCase`

### 可能原因

- 外设未上电，或在所寻址的总线上无响应
- 被探测地址上装配了错误或非预期的器件
- 模块上的 I2C 走线开路，或连接器接触不良
- Sohu I2C 控制器故障
- ASIC 调试 I2C mux 无响应，导致无法到达夹层板总线

### 采集项

- suite_run_url
- 标出失败总线、器件和 I2C 地址的逐测试日志
- CPLD 报告的夹层板类型（决定是否探测 I2C2）
- 运行窗口内的 mezz/VBB UART 日志
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`ASIC`, `MEZZ_MODULE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
