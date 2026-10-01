# SohuGpioTestCase 错误码

由 `SohuGpioTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0005: GPIO_LOOPBACK_MISMATCH](#TH-SOHU-0005)

<a id="TH-SOHU-0005"></a>
## TH-SOHU-0005: GPIO_LOOPBACK_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0005` |
| 名称 | `GPIO_LOOPBACK_MISMATCH` |
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
| 组件 | `1X.SOHU.MCPU_GPIO` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

某个 MCPU GPIO 没有读回其驱动值。涵盖测试的两个部分：芯片 ID 绑带引脚读到的值不是预期的 chip_id，以及逐引脚输出到输入的环回既观察不到翻转后的值，也观察不到恢复后的原值。

### 测试用例

`SohuGpioTestCase`

### 可能原因

- 模块上的 GPIO 网络开路、短路或处于边缘状态
- MCPU GPIO 焊盘或引脚复用故障
- 本模块的芯片 ID 绑带电阻不正确或未装配

### 采集项

- suite_run_url
- 标出失败引脚及期望值/读回值的逐测试日志
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
