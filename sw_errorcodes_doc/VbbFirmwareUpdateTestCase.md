# VbbFirmwareUpdateTestCase 错误码

由 `VbbFirmwareUpdateTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0005: FIXTURE_FIRMWARE_UPDATE_FAILED](#TH-FW-0005)
- [TH-HAR-0003: TEST_DEPENDENCY_UNAVAILABLE](#TH-HAR-0003)

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

治具固件更新失败（黄金 VBB / retimer）：OpenOCD 烧录、ST-Link 适配器、烧录后的 UART/RPC 就绪检查，或应用固件哈希校验未成功。

### 测试用例

`VbbFirmwareUpdateTestCase`, `RetimerFirmwareUpdateTestCase`

### 可能原因

- 治具固件更新或校验失败
- VBB MCU 上的 ST-Link / OpenOCD 烧录失败
- 重启后 VBB UART 不可用，或 RPC 无响应
- 已烧录镜像的哈希与正在运行的应用不一致

### 采集项

- suite_run_url
- 逐测试日志与记录
- 固件更新记录
- 烧录失败时的 OpenOCD 记录
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 重启 Devkit，复测一次。 | 受影响子集 | 10 | — |

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

<a id="TH-HAR-0003"></a>
## TH-HAR-0003: TEST_DEPENDENCY_UNAVAILABLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HAR-0003` |
| 名称 | `TEST_DEPENDENCY_UNAVAILABLE` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `L10.HAR.HARNESS` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

测试所依赖的工具、二进制文件或数据文件（例如 pldm_ua 二进制）在测试系统上缺失，因此测试无法执行其功能。与 TH-CPU-0003 不同，后者针对被测件上缺失的工具。还包括治具固件更新所缺的 VBB 烧录 runfiles / nm 工具链 / version_info 产物，以及 Kayak 工作负载因 chipsim /mnt/weights 的 9p 挂载失败而根本没有启动的情况。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`, `SohuWeightLoadTestCase`, `VbbFirmwareUpdateTestCase`

### 可能原因

- 工位上的测试包/runfiles 部署缺口
- Harness 发布版本缺少数据依赖

### 采集项

- suite_run_url
- 逐测试日志中缺失的路径
- harness_version, station_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 工程师 | 修正工位部署 / harness 包；不要把单板送去返修 |  |  | — |

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
