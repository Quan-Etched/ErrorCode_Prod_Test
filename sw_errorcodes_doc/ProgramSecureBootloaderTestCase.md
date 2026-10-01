# ProgramSecureBootloaderTestCase 错误码

由 `ProgramSecureBootloaderTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0003: BOOTLOADER_PROGRAMMING_FAILED](#TH-FW-0003)
- [TH-FW-0004: JTAG_IMAGE_LOAD_VERIFY_FAILED](#TH-FW-0004)
- [TH-MEZZ-0001: MEZZANINE_CPLD_ACCESS_WRITE_FAILED](#TH-MEZZ-0001)
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

Bootloader 烧录失败（flash 烧录失败，或烧录后无 ping 响应）。

### 测试用例

`ProgramSecureBootloaderTestCase`、`BootloaderResultTestCase`

### 可能原因

- Bootloader flash 烧录失败
- 烧录后 ASIC 无响应

### 采集项

- suite_run_url
- 单次测试日志与转录
- bootloader 烧录转录
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 Sohu 模块上的绿色电源指示灯为点亮状态。 |  | 5 | — |
| 2 | 操作员 | 确认 PCIe 线缆与电源线均已正确且牢固连接。 |  | 5 | — |
| 3 | 操作员 | 若未发现异常，复测一次。 | affected_subset | 10 | — |

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

<a id="TH-FW-0004"></a>
## TH-FW-0004: JTAG_IMAGE_LOAD_VERIFY_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0004` |
| 名称 | `JTAG_IMAGE_LOAD_VERIFY_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.FW.JTAG` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

JTAG 镜像加载/校验失败（ICCM 校验不匹配）。

### 测试用例

`ProgramSecureBootloaderTestCase`

### 可能原因

- JTAG 镜像加载或 ICCM 校验失败

### 采集项

- suite_run_url
- 单次测试日志与转录
- OpenOCD 转录
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 疑似测试问题，复测一次。 | affected_subset | 10 | — |

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

<a id="TH-MEZZ-0001"></a>
## TH-MEZZ-0001: MEZZANINE_CPLD_ACCESS_WRITE_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-MEZZ-0001` |
| 名称 | `MEZZANINE_CPLD_ACCESS_WRITE_FAILED` |
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
| 组件 | `1X.MEZZ.CPLD` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

夹层板/评估板 CPLD 寄存器访问或写入失败。

### 测试用例

`ProgramSecureBootloaderTestCase`、`CpldDiagnosticsTestCase`

### 可能原因

- 夹层板或评估板 CPLD 寄存器访问失败
- Devkit 无法与 Sohu 模块通信，很可能是 bootloader 未运行，因为 PV1 未上电

### 采集项

- suite_run_url
- 单次测试日志与转录
- CPLD 操作转录
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 Sohu 模块上的绿色电源指示灯为点亮状态。 |  | 5 | — |
| 2 | 操作员 | 确认 PCIe 线缆与电源线均已正确且牢固连接。 |  | 5 | — |
| 3 | 操作员 | 若未发现异常，复测一次。 | affected_subset | 10 | — |

### 疑似组件

`MEZZ`

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

`ProgramSecureBootloaderTestCase`、`BootloaderResultTestCase`

### 可能原因

- 无法解除 ASIC 复位

### 采集项

- suite_run_url
- 单次测试日志与转录
- ASIC 复位操作转录
- harness_version、station_id、operator_id、timestamp

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
