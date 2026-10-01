# RetimerFirmwareUpdateTestCase 错误码

由 `RetimerFirmwareUpdateTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0005: FIXTURE_FIRMWARE_UPDATE_FAILED](#TH-FW-0005)

<a id="TH-FW-0005"></a>
## TH-FW-0005: FIXTURE_FIRMWARE_UPDATE_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0005` |
| 名称 | `FIXTURE_FIRMWARE_UPDATE_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / 1x-module-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 2 — 热重启 |
| 处置结果 | 错误 |
| 组件 | `1X.FW.FIXTURE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

治具固件更新失败（golden VBB / Retimer）：OpenOCD flash、ST-Link 适配器、烧录后 UART/RPC 就绪检查，或应用固件哈希校验未成功。

### 测试用例

`VbbFirmwareUpdateTestCase`、`RetimerFirmwareUpdateTestCase`

### 可能原因

- 治具固件更新或校验失败
- VBB MCU 上的 ST-Link / OpenOCD flash 失败
- 重启后 VBB UART 不可用或 RPC 无响应
- 已烧录镜像的哈希与正在运行的应用不匹配

### 采集项

- suite_run_url
- 单次测试日志与转录
- 固件更新转录
- flash 失败时的 OpenOCD 转录
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 重启 Devkit，复测一次。 | affected_subset | 10 | — |

### 疑似组件

`VBB`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
