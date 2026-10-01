# SohuSramMemoryTestCase 错误码

由 `SohuSramMemoryTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-SOHU-0011: SRAM_TEST_FAIL](#TH-SOHU-0011)

<a id="TH-SOHU-0011"></a>
## TH-SOHU-0011: SRAM_TEST_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-SOHU-0011` |
| 名称 | `SRAM_TEST_FAIL` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 3 — 内存 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `MLT.SOHU.SOHU_CHIP` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

片上 SRAM 测试失败（卡死位 / 回读不匹配）——RPC 读/写/反相检查报告了失败的 SRAM 区域，或 March C+ 二进制以非零退出。失败的 SRAM 名称放入 message / affected_instances，切勿写入新错误码（规格 §1.2）。注意：March C+ 非零退出目前尚无法与启动错误区分；待该二进制暴露退出状态约定后再细化。

### 测试用例

`SohuSramMemoryTestCase`

### 可能原因

- 片上 SRAM 单元缺陷（卡死位），涉及 ISC/NLU/theta/softmax SRAM
- 标称电压/频率下 SRAM 时序处于临界状态

### 采集项

- suite_run_url
- 失败的 SRAM 名称（affected_instances）
- March C+ 二进制的 stdout/stderr 与退出码
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_CHIP`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
