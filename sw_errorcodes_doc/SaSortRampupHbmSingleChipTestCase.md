# SaSortRampupHbmSingleChipTestCase 错误码

由 `SaSortRampupHbmSingleChipTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0002: SOHU_NOT_PINGABLE](#TH-SOHU-0002)
- [TH-SOHU-0012: SA_MATMUL_NUMERIC_MISMATCH](#TH-SOHU-0012)
- [TH-SOHU-0021: DEFECTIVE_SA_COLUMNS_EXCEED_LIMIT](#TH-SOHU-0021)
- [TH-SOHU-0024: SCREENING_DATA_MISSING](#TH-SOHU-0024)

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

Sohu 设备未通过 RPC proxy 对 ping 作出响应：固件未运行、不可达，或设备已从 proxy 脱落。在曾能正常上报的设备停止应答时发出，例如重复 FLR 运行后的事后扫描。

### 测试用例

`SohuFlrTestCase`, `SohuVfioPingTestCase`, `SaSortRampupHbmSingleChipTestCase`, `SohuWeightLoadTestCase`

### 可能原因

- Sohu 固件挂起或崩溃，停止处理 RPC
- 设备从 PCIe 树 / vfio proxy 脱落
- 复位或上电时序处于临界状态，导致 ASIC 无响应

### 采集项

- suite_run_url
- 标明无响应设备索引的逐测日志
- 运行窗口的 UART 日志
- 失败时刻的 lspci / proxy 设备列表
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

<a id="TH-SOHU-0012"></a>
## TH-SOHU-0012: SA_MATMUL_NUMERIC_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0012` |
| 名称 | `SA_MATMUL_NUMERIC_MISMATCH` |
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

SA matmul dispatcher 测试二进制以非零退出：脉动阵列输出与 funcsim 参考值不匹配。sa_sort 筛选可容忍有限数量的缺陷 SA 列，因此非零退出意味着不匹配已超出健康图允许屏蔽的范围。

### 测试用例

`SaSortRampupHbmSingleChipTestCase`

### 可能原因

- 缺陷的脉动阵列列或 DPU 行产生错误乘积
- 被测密度下 SA 区域电压或时钟处于临界状态
- 向 SA 供数的 HBM 权重投递故障（整行 DPU 被抹除）

### 采集项

- suite_run_url
- 含 DPU 健康矩阵与缺陷 SA 列列表的逐测日志
- 用于 affected_instances 的数据类型、matmul 维度与缺陷列
- 本次运行保存的 SA 健康图
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

缺陷 SA 列数超过筛选上限。对缺陷图重试无效。

### 测试用例

`SohuSaScreeningTestCase`, `SaSortRampupHbmSingleChipTestCase`

### 可能原因

- 脉动阵列缺陷列数超出筛选允许范围

### 采集项

- suite_run_url
- 逐测日志与 transcript
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

所需筛选数据缺失或加载失败（SA mask / bin 输入），包括 eFuse/Flash init-config 读取失败以及无效的筛选 bin 编码。

### 测试用例

`SohuChipBinTestCase`, `SohuSaScreeningTestCase`, `SaSortRampupHbmSingleChipTestCase`

### 可能原因

- 工位或套件配置中缺少筛选数据包
- SA mask / bin 输入解析失败
- eFuse 或 Flash init config 不可读或不一致

### 采集项

- suite_run_url
- 逐测日志与 transcript
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
