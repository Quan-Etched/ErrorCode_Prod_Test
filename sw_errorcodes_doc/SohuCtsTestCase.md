# SohuCtsTestCase 错误码

由 `SohuCtsTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-THM-0003: CTS_PROTECTION_NO_SHUTDOWN](#TH-THM-0003)

<a id="TH-THM-0003"></a>
## TH-THM-0003: CTS_PROTECTION_NO_SHUTDOWN

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-THM-0003` |
| 名称 | `CTS_PROTECTION_NO_SHUTDOWN` |
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
| 组件 | `1X.THM.CTS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

CTS 修调码被驱动到最大值（最低跳闸阈值），但芯片没有关机：在关机超时时间内，ASIC_CTRL1 中的 CPLD cattrip 锁存位从未被置位。

### 测试用例

`SohuCtsTestCase`

### 可能原因

- 裸片上的灾难性跳闸传感器有缺陷（从不置位 CATTRIP）
- CATTRIP 输出引脚或其夹层卡走线开路
- 夹层卡 CPLD 上的 CATTRIP 被屏蔽（mcu_cattrip_mask 配置错误）

### 采集项

- suite_run_url
- 本次运行的 CPLD 寄存器转储（ASIC_CTRL1、man_mcu_cattrip、mcu_cattrip_mask）
- cpld_asic_ctrl1 与 cattrip_latched 测量值
- 触发与轮询窗口内的 VBB 串口记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`, `MEZZANINE_CARD`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
