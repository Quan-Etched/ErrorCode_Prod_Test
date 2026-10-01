# SohuHotReloadFirmwareUpdateTestCase 错误码

由 `SohuHotReloadFirmwareUpdateTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-FW-0001: SOHU_FIRMWARE_UPDATE_FAILED](#TH-FW-0001)
- [TH-FW-0009: SOHU_HOT_RELOAD_NOT_ELIGIBLE](#TH-FW-0009)

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

<a id="TH-FW-0009"></a>
## TH-FW-0009: SOHU_HOT_RELOAD_NOT_ELIGIBLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-FW-0009` |
| 名称 | `SOHU_HOT_RELOAD_NOT_ELIGIBLE` |
| 版本 | 1 |
| 起始版本 | harness 2026.217 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / 1x-module-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.FW.SOHU_APP_FIRMWARE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

热重载无法开始，因此没有写入任何固件：芯片正在运行旧版 bootloader 而不是 secure_bootloader，处于没有应用 PLDM 端点的 bootloader 模式，或预检查无法通过 RPC/代理读出正在运行的版本。套件必须先运行安全启动恢复或引导，才能执行本测试用例。与 TH-FW-0001 不同，后者针对已经尝试并失败的更新。

### 测试用例

`SohuHotReloadFirmwareUpdateTestCase`

### 可能原因

- 套件在 secure_bootloader 和应用固件尚未就位时就运行了热重载
- 套件中更早的恢复/引导步骤失败，且没有作为门控条件
- PCIe/代理状态使应用 PLDM 端点不可达

### 采集项

- suite_run_url
- 标出触发了哪种资格判定结果以及正在运行的镜像的逐测试日志
- 若已拉起，则包含 MCTP 桥接跟踪
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 升级处理 | 将资格判定结果和正在运行的镜像名称升级给 Etched；没有烧录任何内容，因此不要把单板送去返修或失效分析（FA）。 | 不适用 |  | — |

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
