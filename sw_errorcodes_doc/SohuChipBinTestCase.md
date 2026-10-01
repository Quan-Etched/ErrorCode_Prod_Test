# SohuChipBinTestCase 错误码

由 `SohuChipBinTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0023: CHIP_BIN_BELOW_THRESHOLD](#TH-SOHU-0023)
- [TH-SOHU-0024: SCREENING_DATA_MISSING](#TH-SOHU-0024)

<a id="TH-SOHU-0023"></a>
## TH-SOHU-0023: CHIP_BIN_BELOW_THRESHOLD

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0023` |
| 名称 | `CHIP_BIN_BELOW_THRESHOLD` |
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
| 组件 | `1X.SOHU.BINNING` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

芯片分档低于验收阈值，或未通过分档准则（例如无法分档的 SA 列屏蔽数量，或非法的分档跃迁）。

### 测试用例

`SohuChipBinTestCase`

### 可能原因

- 硅片性能低于验收分档
- 被屏蔽的 SA 列数超过所支持的分档上限

### 采集项

- suite_run_url
- 本次运行的分档输入与计算出的分档
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-SOHU-0024"></a>
## TH-SOHU-0024: SCREENING_DATA_MISSING

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0024` |
| 名称 | `SCREENING_DATA_MISSING` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `1X.SOHU.SCREENING_DATA` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

所需筛选数据缺失或加载失败（SA 屏蔽 / 分档输入），包括 eFuse/Flash 初始化配置读取失败，以及无效的筛选分档编码。

### 测试用例

`SohuChipBinTestCase`, `SohuSaScreeningTestCase`, `SaSortRampupHbmSingleChipTestCase`

### 可能原因

- 工位或套件配置中缺少筛选数据包
- SA 屏蔽 / 分档输入解析失败
- eFuse 或 Flash 初始化配置无法读取或不一致

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
