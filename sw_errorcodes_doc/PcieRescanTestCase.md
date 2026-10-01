# PcieRescanTestCase 错误码

由 `PcieRescanTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-ENV-0004: HOST_SETUP_STEP_FAILED](#TH-ENV-0004)

<a id="TH-ENV-0004"></a>
## TH-ENV-0004: HOST_SETUP_STEP_FAILED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-ENV-0004` |
| 名称 | `HOST_SETUP_STEP_FAILED` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / 1x-module-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.ENV.HOST_SETUP` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

主机驱动/设置工具步骤失败：内核模块重载、PCIe 拆除或总线重新扫描、Kayak RAID 重新挂载、sohu_mdev sysfs 参数写入，或日志读取器激活在工位主机上返回了非零值。

### 测试用例

`ReloadKernelModuleTestCase`、`PcieTeardownTestCase`、`PcieRescanTestCase`、`SetSkipFlrOnOpenCloseTestCase`、`SohuLogReaderActivateTestCase`、`LogReaderCaptureTestCase`、`PublishBootloaderTypeTestCase`、`KayakRaidRemountTestCase`

### 可能原因

- sohu_mdev 内核模块未加载，或已加载的版本不具备预期参数
- 工位主机上缺少该设置命令所需的 sudo/权限
- 套件中更早的设置步骤失败，使主机处于非预期状态
- 本工位未部署主机工具（驱动包、日志读取器）
- /sys/bus/pci/rescan 写入失败
- PEX 拆除后，位于 /data/kayak 的 Kayak RAID0 无法重新组装或重新挂载

### 采集项

- suite_run_url
- 失败设置步骤的确切命令、退出码、stdout 与 stderr
- sohu_mdev 的 lsmod / modinfo 输出
- 运行时间窗口内的 dmesg 摘录
- harness_version、station_id、operator_id、timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。请勿复测。 |  |  | — |

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
