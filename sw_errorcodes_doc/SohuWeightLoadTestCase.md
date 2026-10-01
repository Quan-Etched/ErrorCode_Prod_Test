# SohuWeightLoadTestCase 错误码

由 `SohuWeightLoadTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HAR-0002: TEST_ARGS_INVALID](#TH-HAR-0002)
- [TH-HAR-0003: TEST_DEPENDENCY_UNAVAILABLE](#TH-HAR-0003)
- [TH-SOHU-0002: SOHU_NOT_PINGABLE](#TH-SOHU-0002)
- [TH-SOHU-0016: WEIGHT_LOAD_SPOT_CHECK_MISMATCH](#TH-SOHU-0016)

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

<a id="TH-SOHU-0002"></a>
## TH-SOHU-0002: SOHU_NOT_PINGABLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0002` |
| 名称 | `SOHU_NOT_PINGABLE` |
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
| 组件 | `1X.SOHU.ASIC` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

Sohu 器件未通过 RPC 代理响应 ping：固件未在运行、不可达，或器件已从代理上掉线。当一个曾经正常上报的器件停止应答时发出，例如重复 FLR 运行之后的收尾扫描。

### 测试用例

`SohuFlrTestCase`, `SohuVfioPingTestCase`, `SaSortRampupHbmSingleChipTestCase`, `SohuWeightLoadTestCase`

### 可能原因

- Sohu 固件挂起或崩溃，停止处理 RPC
- 器件从 PCIe 树 / vfio 代理上掉线
- 复位或上电时序处于边缘状态，使 ASIC 无响应

### 采集项

- suite_run_url
- 标出无响应器件索引的逐测试日志
- 运行窗口内的 UART 日志
- 失败时刻的 lspci / 代理器件列表
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

<a id="TH-SOHU-0016"></a>
## TH-SOHU-0016: WEIGHT_LOAD_SPOT_CHECK_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0016` |
| 名称 | `WEIGHT_LOAD_SPOT_CHECK_MISMATCH` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 11 — 数据 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SOHU.WEIGHT_LOAD` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

权重加载抽查失败：加载后驻留在 HBM 中的权重与磁盘上的模型不一致（weight_load_test_app 非零退出）。

### 测试用例

`SohuWeightLoadTestCase`

### 可能原因

- HBM 写/读通路损坏了权重
- DMA 寻址故障
- 传入 HBM 的权重传输不完整或已损坏

### 采集项

- suite_run_url
- 逐测试日志与记录（Weight mismatch 行）
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`ASIC`, `HBM`, `MEZZ_MODULE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
