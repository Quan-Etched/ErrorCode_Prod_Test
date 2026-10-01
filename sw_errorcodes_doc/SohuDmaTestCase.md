# SohuDmaTestCase 错误码

由 `SohuDmaTestCase` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-DMA-0001: DMA_DATA_PATH_FAIL](#TH-DMA-0001)
- [TH-PCIE-0003: PCIE_CSRAM_DMA_THROUGHPUT_BELOW_THRESHOLD](#TH-PCIE-0003)
- [TH-PCIE-0004: PCIE_HBM_DMA_INTEGRITY_MISMATCH](#TH-PCIE-0004)
- [TH-PCIE-0005: PCIE_HBM_DMA_THROUGHPUT_BELOW_THRESHOLD](#TH-PCIE-0005)

<a id="TH-DMA-0001"></a>
## TH-DMA-0001: DMA_DATA_PATH_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-DMA-0001` |
| 名称 | `DMA_DATA_PATH_FAIL` |
| 版本 | 1 |
| 起始版本 | harness 2026.216 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `1X.DMA.HOST_CHIP_PATH` |
| 可重试 | True |
| 最大自动重试次数 | 3 |

### 描述

主机到芯片的 DMA 数据通路测试失败：dma_test_app 报告某个 SRAM 区域（RopeSram / CentralSram）上的数据校验或 March C+ 失败，或者失败方式无法从其输出归到更具体的 PCIe/HBM 失效模式（本测试的回退情况）。

### 测试用例

`SohuDmaTestCase`

### 可能原因

- 处于边缘状态的 PCIe 或片上数据通路损坏了 DMA 传输
- 目标 SRAM 区域存在粘滞位或跳变故障位
- DMA 引擎 / 描述符处理故障

### 采集项

- suite_run_url
- 完整的 dma_test_app stdout/stderr、退出码和 RNG 种子
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 怀疑是测试问题（单芯片测试超时拖垮了工位），复测一次。 | 受影响子集 | 10 | — |

### 疑似组件

`SOHU_ASIC`, `MEZZ_MODULE`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-PCIE-0003"></a>
## TH-PCIE-0003: PCIE_CSRAM_DMA_THROUGHPUT_BELOW_THRESHOLD

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0003` |
| 名称 | `PCIE_CSRAM_DMA_THROUGHPUT_BELOW_THRESHOLD` |
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
| 组件 | `1X.PCIE.CSRAM_DMA` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

PCIe 到 CSRAM 的 DMA 吞吐低于合格下限（由套件配置；1X 模块套件为 50 GB/s）。当活动 DMA 流程中的 CentralSram 吞吐检查失败时，由 SohuDmaTestCase 发出。

### 测试用例

`SohuDmaTestCase`

### 可能原因

- PCIe 链路降级（通道宽度 / 速率低于 Gen5 x16）
- 处于边缘状态的 PCIe 通道迫使可纠正错误重试
- DMA 引擎或仲裁问题限制了传输速率

### 采集项

- suite_run_url
- 实测读/写吞吐与配置下限的对比
- lspci 链路状态与 AER 计数器
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`, `PCIE_LINK`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-PCIE-0004"></a>
## TH-PCIE-0004: PCIE_HBM_DMA_INTEGRITY_MISMATCH

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0004` |
| 名称 | `PCIE_HBM_DMA_INTEGRITY_MISMATCH` |
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
| 组件 | `1X.PCIE.HBM_DMA` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

PCIe 到 HBM 的 DMA 数据完整性不匹配：dma_test_app 从某个 HBM 区域（EastHbm / WestHbm）读回的数据与所写入的随机 / 按位取反模式不一致。

### 测试用例

`SohuDmaTestCase`

### 可能原因

- HBM 堆栈或伪通道数据故障
- 处于边缘状态的 PCIe 或片上通路损坏了发往 HBM 的传输
- DMA 寻址故障，指向了错误的块/偏移

### 采集项

- suite_run_url
- 完整的 dma_test_app stdout/stderr、退出码和 RNG 种子
- 校验上下文中的失败区域/块/偏移
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`, `HBM_STACK`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-PCIE-0005"></a>
## TH-PCIE-0005: PCIE_HBM_DMA_THROUGHPUT_BELOW_THRESHOLD

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-PCIE-0005` |
| 名称 | `PCIE_HBM_DMA_THROUGHPUT_BELOW_THRESHOLD` |
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
| 组件 | `1X.PCIE.HBM_DMA` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

dma_test_app 中 EastHbm / WestHbm 传输的 PCIe 到 HBM DMA 吞吐低于合格下限（由套件配置；1X 模块套件为 16 GB/s）。

### 测试用例

`SohuDmaTestCase`

### 可能原因

- PCIe 链路降级（通道宽度 / 速率低于 Gen5 x16）
- HBM 堆栈或控制器限制了持续带宽
- DMA 引擎或仲裁问题限制了传输速率

### 采集项

- suite_run_url
- 各区域实测吞吐与配置下限的对比
- 完整的 dma_test_app stdout/stderr、退出码和 RNG 种子
- unit_sn, fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 收集本次失败的套件/测试日志与产物。 |  | 5 | — |
| 2 | 升级处理 | 将收集到的日志升级给 Etched 工程师。 |  |  | — |

### 疑似组件

`SOHU_ASIC`, `PCIE_LINK`, `HBM_STACK`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当
