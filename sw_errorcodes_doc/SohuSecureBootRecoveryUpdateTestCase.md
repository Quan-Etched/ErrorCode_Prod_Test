# SohuSecureBootRecoveryUpdateTestCase 错误码

由 `SohuSecureBootRecoveryUpdateTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0001: SOHU_FIRMWARE_UPDATE_FAILED](#TH-FW-0001)
- [TH-FW-0007: SECURE_BOOT_RECOVERY_UPDATE_TIMEOUT](#TH-FW-0007)
- [TH-FW-0008: SECURE_BOOT_RECOVERY_UPDATE_FAIL](#TH-FW-0008)
- [TH-HAR-0002: TEST_ARGS_INVALID](#TH-HAR-0002)
- [TH-HAR-0003: TEST_DEPENDENCY_UNAVAILABLE](#TH-HAR-0003)
- [TH-SOHU-0003: PLDM_SENSOR_CHECK_FAILED](#TH-SOHU-0003)

<a id="TH-FW-0001"></a>
## TH-FW-0001: SOHU_FIRMWARE_UPDATE_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0001` |
| 名称 | `SOHU_FIRMWARE_UPDATE_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.FW.SOHU_APP_FIRMWARE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Sohu 应用固件更新未完成：加载或执行镜像包时抛出异常，之后 ASIC 无法 ping 通，或 ASIC 恢复后没有报告应用固件。对于热重载情形，它还涵盖更新前的资格判定结果，此时根本没有烧录任何内容：芯片正在运行旧版 bootloader、处于没有应用 PLDM 端点的 bootloader 模式，或预检查无法通过 RPC/代理读出正在运行的版本。

### 测试用例

`SohuFirmwareUpdateTestCase`, `SohuHotReloadFirmwareUpdateTestCase`, `SohuSecureBootRecoveryUpdateTestCase`

### 可能原因

- 镜像包被 bootloader 拒绝（签名或布局错误）
- ASIC 在跳转到应用固件时挂起
- 更新过程中夹层板/VBB 通信中断
- 套件在 secure_bootloader 和应用固件尚未就位时就运行了热重载
- 更新期间上电时序故障

### 采集项

- suite_run_url
- 更新窗口内的 mezz 与 VBB UART 日志
- 更新前的版本信息
- 镜像包路径与 release id
- unit_sn, bios/fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_APP_FIRMWARE`, `SOHU_BOOTLOADER`, `MEZZANINE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-FW-0007"></a>
## TH-FW-0007: SECURE_BOOT_RECOVERY_UPDATE_TIMEOUT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0007` |
| 名称 | `SECURE_BOOT_RECOVERY_UPDATE_TIMEOUT` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `MLT.FW.SOHU_CHIP` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

安全启动恢复更新期间，PLDM Update Agent 未在 pldm_update_timeout_s 内完成。器件很可能在恢复模式下没有通过 Sohu UART 响应。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`

### 可能原因

- 器件实际上并未进入恢复模式（绑带时序无效）
- Sohu UART 无响应，或端口/波特率错误
- 更新在传输中途停滞

### 采集项

- suite_run_url
- 直到超时为止的 pldm_ua 行日志
- 配置的 pldm_update_timeout_s
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 UART 线缆以及恢复绑带已接合；重跑一次；保留日志并转给固件分诊 | 受影响子集 | 10 | — |

### 疑似组件

`SOHU_CHIP`, `VBB`, `UART_CABLING`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-FW-0008"></a>
## TH-FW-0008: SECURE_BOOT_RECOVERY_UPDATE_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0008` |
| 名称 | `SECURE_BOOT_RECOVERY_UPDATE_FAIL` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `MLT.FW.SOHU_CHIP` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

通过安全启动恢复模式进行的 VFIO 应用固件更新失败：恢复绑带时序失败，或 PLDM Update Agent 报告更新失败（pldm_ua 非零退出，更新被器件拒绝）。工具或部署缺口为 TH-HAR-0003；无效参数为 TH-HAR-0002。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`

### 可能原因

- 器件未能进入或保持安全启动恢复模式（绑带/VBB 问题）
- PLDM 包被器件拒绝（镜像/签名不匹配）
- 更新期间 Sohu UART 通信错误

### 采集项

- suite_run_url
- 逐测试日志中的 pldm_ua 行日志
- pldm 包路径与激活模式
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 UART 线缆与插接，并重跑恢复更新子集一次；然后保留单板和 pldm_ua 日志，并核对包与发布版本；转给固件分诊。不要继续重试，因为器件可能正处于更新过程中 | 受影响子集 | 10 | — |

### 疑似组件

`SOHU_CHIP`, `VBB`, `UART_CABLING`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-HAR-0002"></a>
## TH-HAR-0002: TEST_ARGS_INVALID

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HAR-0002` |
| 名称 | `TEST_ARGS_INVALID` |
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

测试用例以无效或不支持的参数被调用（例如意外的 kwargs、不支持的模式），并在接触被测件之前拒绝了本次运行。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`, `ServerNestedTestCase`, `SohuSnapTestCase`, `VfioProxyVersionTestCase`, `SohuWeightLoadTestCase`, `SltModuleNestedTestCase`

### 可能原因

- 套件 YAML 传入了测试不接受的参数
- 套件 YAML 请求了测试不支持的模式或路径

### 采集项

- suite_run_url
- 逐测试日志中的问题参数
- harness_version, station_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 工程师 | 修正本测试的套件 YAML；不要把单板送去返修 |  |  | — |

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

<a id="TH-SOHU-0003"></a>
## TH-SOHU-0003: PLDM_SENSOR_CHECK_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0003` |
| 名称 | `PLDM_SENSOR_CHECK_FAILED` |
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
| 组件 | `1X.SOHU.PLDM` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

PLDM 传感器可发现性或健全性检查失败（启动阶段门控）。

### 测试用例

`SohuSecureBootRecoveryUpdateTestCase`

### 可能原因

- 固件 PLDM 栈未暴露传感器
- 模块上的传感器故障

### 采集项

- suite_run_url
- 逐测试日志与记录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

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
