# BootloaderResultTestCase 错误码

由 `BootloaderResultTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0003: BOOTLOADER_PROGRAMMING_FAILED](#TH-FW-0003)
- [TH-PWR-0008: MODULE_POWER_ON_FAILURE](#TH-PWR-0008)
- [TH-SOHU-0001: ASIC_RESET_DEASSERT_FAILED](#TH-SOHU-0001)

<a id="TH-FW-0003"></a>
## TH-FW-0003: BOOTLOADER_PROGRAMMING_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0003` |
| 名称 | `BOOTLOADER_PROGRAMMING_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.FW.BOOTLOADER` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

Bootloader 编程失败（烧录编程失败，或编程后无 ping 响应）。

### 测试用例

`ProgramSecureBootloaderTestCase`, `BootloaderResultTestCase`

### 可能原因

- Bootloader flash 编程失败
- 编程后 ASIC 无响应

### 采集项

- suite_run_url
- 各测试的日志与 transcript
- bootloader 编程 transcript
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 Sohu 模块上的绿色电源指示灯为 ON。 |  | 5 | — |
| 2 | 操作员 | 确认 PCIe 线缆与电源线缆均已正确、牢固连接。 |  | 5 | — |
| 3 | 操作员 | 若未发现问题，复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`FW`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-PWR-0008"></a>
## TH-PWR-0008: MODULE_POWER_ON_FAILURE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PWR-0008` |
| 名称 | `MODULE_POWER_ON_FAILURE` |
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
| 组件 | `1X.PWR.POWER_ON` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

模块上电失败（指示灯熄灭、电源轨故障或短路）。

### 测试用例

`BootloaderResultTestCase`

### 可能原因

- 电源轨短路（观测到：VOUT_13P5_IBC, VDD_1P2）
- VRM 卡在稳压点以下（观测到：VCC_VRM 为 0.7V）
- Devkit 无法与 Sohu 模块通信，很可能是因为 PV1 未上电导致 bootloader 未运行

### 采集项

- suite_run_url
- 各测试的日志与 transcript
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 Sohu 模块上的绿色电源指示灯为 ON。 |  | 5 | — |
| 2 | 操作员 | 确认 PCIe 线缆与电源线缆均已正确、牢固连接。 |  | 5 | — |
| 3 | 操作员 | 若未发现问题，复测一次。 | 受影响子集 | 10 | — |

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

<a id="TH-SOHU-0001"></a>
## TH-SOHU-0001: ASIC_RESET_DEASSERT_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0001` |
| 名称 | `ASIC_RESET_DEASSERT_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SOHU.RESET` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

ASIC 复位解除（deassert）失败。

### 测试用例

`ProgramSecureBootloaderTestCase`, `BootloaderResultTestCase`

### 可能原因

- 无法解除 ASIC 复位

### 采集项

- suite_run_url
- 各测试的日志与 transcript
- ASIC 复位操作 transcript
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
