# SohuSaScreeningTestCase 错误码

由 `SohuSaScreeningTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-PCIE-0008: SOHU_ENDPOINT_NOT_ENUMERATED](#TH-PCIE-0008)
- [TH-SOHU-0021: DEFECTIVE_SA_COLUMNS_EXCEED_LIMIT](#TH-SOHU-0021)
- [TH-SOHU-0024: SCREENING_DATA_MISSING](#TH-SOHU-0024)

<a id="TH-PCIE-0008"></a>
## TH-PCIE-0008: SOHU_ENDPOINT_NOT_ENUMERATED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0008` |
| 名称 | `SOHU_ENDPOINT_NOT_ENUMERATED` |
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
| 组件 | `1X.PCIE.ENUMERATION` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

Sohu 端点未被枚举（未出现在 PCIe 树 / RPC 代理中）。

### 测试用例

`PcieSetupTestCase`, `SohuVfioPingTestCase`, `SohuSaScreeningTestCase`

### 可能原因

- Sohu 端点未出现在 PCIe 树或 RPC 代理中

### 采集项

- suite_run_url
- 逐测试日志与记录
- PCIe 拓扑与 RPC 代理状态
- harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑 PCIe 线缆未完全插入 PV1 板，重新插拔线缆并复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`PCIE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-SOHU-0021"></a>
## TH-SOHU-0021: DEFECTIVE_SA_COLUMNS_EXCEED_LIMIT

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0021` |
| 名称 | `DEFECTIVE_SA_COLUMNS_EXCEED_LIMIT` |
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
| 组件 | `1X.SOHU.SA` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

有缺陷的 SA 列数超过筛选限值。对缺陷图而言，重试没有意义。

### 测试用例

`SohuSaScreeningTestCase`, `SaSortRampupHbmSingleChipTestCase`

### 可能原因

- 脉动阵列列的缺陷数超出筛选允许范围

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
