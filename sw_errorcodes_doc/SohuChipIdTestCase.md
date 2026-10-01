# SohuChipIdTestCase 错误码

由 `SohuChipIdTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SN-0001: CHIP_ID_READ_OR_MISMATCH](#TH-SN-0001)

<a id="TH-SN-0001"></a>
## TH-SN-0001: CHIP_ID_READ_OR_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SN-0001` |
| 名称 | `CHIP_ID_READ_OR_MISMATCH` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 11 — 数据 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.SN.CHIP_ID` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

某个已枚举的 Sohu 端点的 sohu_chip_id sysfs 属性无法读取或解析、回读为全 1（设备处于复位），或报告的芯片 ID 与资源配置中该 PCIe 位置所期望的不一致。

### 测试用例

`SohuChipIdTestCase`

### 可能原因

- Sohu ASIC 保持在复位状态，或在读取过程中从 PCIe 链路脱落
- 模块上的芯片 ID 绑带/efuse 错误或未编程
- 模块安装在与谱系记录不同的基板槽位
- 固件未能将芯片 ID 发布到 sysfs 属性

### 采集项

- suite_run_url
- 期望的 chip_id、解析得到的 BDF，以及原始 sysfs 属性内容
- 运行窗口的 lspci 拓扑与 dmesg 摘录
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`, `BASEBOARD`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
