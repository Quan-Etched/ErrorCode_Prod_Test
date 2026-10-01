# SohuEfuseTestCase 错误码

由 `SohuEfuseTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0008: EFUSE_REGION_READ_FAILURE](#TH-SOHU-0008)
- [TH-SOHU-0009: EFUSE_WS_FT_STATUS_INCOMPLETE](#TH-SOHU-0009)

<a id="TH-SOHU-0008"></a>
## TH-SOHU-0008: EFUSE_REGION_READ_FAILURE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0008` |
| 名称 | `EFUSE_REGION_READ_FAILURE` |
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
| 组件 | `1X.SOHU.EFUSE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

通过 RPC 读取 eFuse 区域失败，因此无法从模块解码出任何 init config。

### 测试用例

`SohuEfuseTestCase`

### 可能原因

- 模块上 eFuse 宏或读出通路缺陷
- eFuse 区域在 OSAT 从未完成烧录（空白或损坏的映射）
- 读取过程中到模块的 Sohu RPC 链路中断

### 采集项

- suite_run_url
- 完整的 read_efuse_to_protobuf 错误文本
- 读取窗口的 Sohu RPC 记录
- unit_sn、fw_version、harness_version、station_id、operator_id、timestamp

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

<a id="TH-SOHU-0009"></a>
## TH-SOHU-0009: EFUSE_WS_FT_STATUS_INCOMPLETE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0009` |
| 名称 | `EFUSE_WS_FT_STATUS_INCOMPLETE` |
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
| 组件 | `1X.SOHU.EFUSE` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

eFuse 读取成功，但晶圆分选或最终测试完成标志（wafer_sort_complete、final_test_complete、mbist_complete、sa_complete、sensor_complete 或 hbm_complete）为 False，因此该模块没有包含 MBIST 与 SA 修复在内的已完成 WS/FT 流程记录。

### 测试用例

`SohuEfuseTestCase`

### 可能原因

- 模块在 OSAT 跳过或中止了部分 WS/FT 流程
- 汇总信息烧录前 MBIST 或 SA 修复未完成
- 该构建使用了错误或部分烧录的 eFuse 映射版本

### 采集项

- suite_run_url
- 测试记录的两份 efuse init config 文本 proto
- 报告为 False 的标志列表，以及 copy index
- 晶圆批次 / 晶圆 / X-Y 位置的 WS/FT 族谱
- unit_sn、fw_version、harness_version、station_id、operator_id、timestamp

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
