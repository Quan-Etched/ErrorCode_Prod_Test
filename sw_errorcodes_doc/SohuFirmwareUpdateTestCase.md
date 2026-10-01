# SohuFirmwareUpdateTestCase 错误码

由 `SohuFirmwareUpdateTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0001: SOHU_FIRMWARE_UPDATE_FAILED](#TH-FW-0001)
- [TH-FW-0002: SOHU_FIRMWARE_IMAGE_HASH_MISMATCH](#TH-FW-0002)

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

<a id="TH-FW-0002"></a>
## TH-FW-0002: SOHU_FIRMWARE_IMAGE_HASH_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0002` |
| 名称 | `SOHU_FIRMWARE_IMAGE_HASH_MISMATCH` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.FW.SOHU_APP_FIRMWARE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

更新后 ASIC 启动了应用固件，但 get_version_info() 返回的正在运行的镜像哈希与刚刚暂存的镜像包中的哈希不一致。

### 测试用例

`SohuFirmwareUpdateTestCase`

### 可能原因

- 工位暂存了来自不同发布版本的镜像包
- 更新静默回退到先前已烧录的镜像
- 镜像包元数据（版本信息）与其有效载荷不一致
- QSPI/bootloader 提供了过期镜像

### 采集项

- suite_run_url
- 期望哈希（来自镜像包）与正在运行的哈希
- 镜像包路径与 release id
- 更新前后的版本信息
- unit_sn, bios/fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_APP_FIRMWARE`, `STATION_IMAGE_STAGING`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
