# SohuHbmTrainingCheckTestCase 错误码

由 `SohuHbmTrainingCheckTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-HBM-0014: HBM_NOT_TRAINED_FOR_REQUIRED_SPEED](#TH-HBM-0014)

<a id="TH-HBM-0014"></a>
## TH-HBM-0014: HBM_NOT_TRAINED_FOR_REQUIRED_SPEED

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-HBM-0014` |
| 名称 | `HBM_NOT_TRAINED_FOR_REQUIRED_SPEED` |
| 版本 | 1 |
| 起始版本 | harness 2026.245 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / MLT |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 5 — 配置 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 失败 |
| 组件 | `1X.HBM.STACK` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

芯片没有携带覆盖每个 HBM 每个伪通道、且满足套件所要求数据速率的 HBM DCDL 训练，或者正在以不同速率运行。也包括 Flash 初始化配置覆盖层完全无法解码的情况，这意味着不存在已持久化的训练。

固件根据夹层板类型选择 HBM 速度分档，并要求每个 HBM 的每个伪通道在该速率下都有训练码（`fw/soc/sohu/dvfs_board_profile.cc` 中的 `MissingTrainedHbmDcdlSettingsBitmask`），并拒绝让未训练的模块进入其已训练的量产工作点。套件中没有其他测试会因这类芯片失败，因此如果没有这项检查，未训练的插座仍会出货。

发出该错误码的用例只做读取：从 Flash 覆盖层读取已持久化记录，并通过 HBM RPC 服务读取当前运行的速度分档。它不会改变芯片上的任何内容。

这是配置类错误码，不是内存类：堆栈本身并不可疑，而是该单板从未在预期运行速率下完成训练。处置结果仍是 `失败` 而不是 `错误`，因为该单板在此状态下不可出货。

### 测试用例

`SohuHbmTrainingCheckTestCase`

L10 / L11 套件运行扇出用例 `SohuHbmTrainingCheckMultiChipTestCase`，它在汇总消息中按芯片报告同样的问题，而不携带本错误码。

### 可能原因

- 该单板从未在所要求的数据速率下运行过 HBM 训练
- 训练运行的速率与所要求的速率不同（例如某个 DVT 速率）
- 训练只覆盖了部分 HBM，或某个 HBM 的部分伪通道
- 训练之后发生过板卡或芯片更换，使插座上没有记录
- Flash 初始化配置覆盖层被擦除或已损坏

### 采集项

- suite_run_url
- `hbm_running_east_mbps` / `hbm_running_west_mbps` 测量值
- `hbm_trained_speeds_mbps` 测量值，以及各速率的 `hbm_untrained_bitmask_<rate>_mbps` 值
- 标出所需速率及发现的每个问题的逐测试日志
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认该单板自上次 HBM 训练以来的板卡/芯片更换历史。 |  | 10 | — |
| 2 | 操作员 | 对未训练位掩码所指出的 HBM，按所要求的数据速率申请一次 HBM 训练，然后重新运行本套件。 | 全套 | 120 | — |
| 3 | 升级处理 | 若训练完成而插座仍报告未训练的 HBM，将套件日志升级给 Etched。 |  |  | — |

### 疑似组件

`ASIC`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
