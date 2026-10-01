# CpuStress 错误码

由 `CpuStress` 发出的错误码。

> 权威来源：[`th_registry.yaml`](../th_registry.yaml)。

## 本页错误码

- [TH-CPU-0001: CPU_STRESS_FAIL](#TH-CPU-0001)
- [TH-CPU-0003: CPU_STRESS_TOOL_UNAVAILABLE](#TH-CPU-0003)
- [TH-CPU-0004: CPU_STRESS_EXECUTION_ERROR](#TH-CPU-0004)

<a id="TH-CPU-0001"></a>
## TH-CPU-0001: CPU_STRESS_FAIL

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-CPU-0001` |
| 名称 | `CPU_STRESS_FAIL` |
| 版本 | 1 |
| 起始版本 | harness 2026.212 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 6 — 硬件 |
| 严重级别 | 2 — 隔离 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 失败 |
| 组件 | `L10.CPU.HOST_CPU` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

stress-ng 以状态码 2 退出，因为一个或多个 CPU 压力器失败，或 --verify 检测到计算错误。

### 测试用例

`CpuStress`

### 可能原因

- 边缘/缺陷 CPU 核心在负载下产生计算错误
- 冷却不足或散热器安装不当（应力期间出现热事件）
- 满核负载下 VRM / 供电不稳定
- BIOS 电源/性能设置不符合规格

### 采集项

- suite_run_url
- 完整的 stress-ng stdout/stderr（含 bogo-ops 指标）
- 运行窗口内的 dmesg / MCE 摘录
- 运行期间的 CPU 频率 + 热遥测
- unit_sn, bios/fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认工位环境温度/气流正常，重跑 CPU 子集。 | CPU_subset | 5 | — |
| 2 | 技师 | 按组装 SOP 检查散热器安装与 TIM；若不符合规格则重新安装。 | CPU_subset | 15 | — |
| 3 | 升级处理 | 保留单元；附上 stress-ng 日志与 MCE 摘录；转交 FA；创建 Jira。 | 不适用 |  | 在确认根因前不再进行返工。 |

### 疑似组件

`HOST_CPU`, `CPU_COOLER`, `VRM`

### 供应商错误 ID

_无_

### 审查清单

- [ ] 描述与当前测试行为一致
- [ ] 可能原因完整且可执行
- [ ] 采集项与 harness 实际记录内容一致
- [ ] 维修措施、负责人与复测路径正确
- [ ] 严重级别、快速处置与处置结果恰当

<a id="TH-CPU-0003"></a>
## TH-CPU-0003: CPU_STRESS_TOOL_UNAVAILABLE

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-CPU-0003` |
| 名称 | `CPU_STRESS_TOOL_UNAVAILABLE` |
| 版本 | 1 |
| 起始版本 | harness 2026.212 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 7 — 软件 |
| 严重级别 | 5 — 配置 |
| 快速处置 | 9 — 升级 |
| 处置结果 | 错误 |
| 组件 | `L10.CPU.HOST_CPU` |
| 可重试 | False |
| 最大自动重试次数 | 0 |

### 描述

目标机上未安装或无法运行 stress-ng，因此 CPU 应力测试无法启动。

### 测试用例

`CpuStress`

### 可能原因

- DUT 镜像缺少 stress-ng 软件包（部署缺口）
- 套件中更早的 InstallLinuxPackagesTestCase 未运行或已失败
- 目标机上 PATH 损坏或 stress-ng 二进制损坏

### 采集项

- suite_run_url
- stress-ng 版本探测的 stderr
- unit_sn, bios/fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 在目标机上安装 stress-ng（或重跑软件包安装步骤），重跑 CPU 子集。 | CPU_subset | 5 | — |
| 2 | 升级处理 | 若部署镜像缺少该软件包，转交 test-infra；创建 Jira。请勿将单元转入返工或 FA。 |  |  | — |

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

<a id="TH-CPU-0004"></a>
## TH-CPU-0004: CPU_STRESS_EXECUTION_ERROR

### 标识

| 字段 | 值 |
| --- | --- |
| 错误码 | `TH-CPU-0004` |
| 名称 | `CPU_STRESS_EXECUTION_ERROR` |
| 版本 | 1 |
| 起始版本 | harness 2026.212 |
| 负责人 | supercomputing-sw |
| Jira 组件 | ETCH / l10-test |

### 分类

| 字段 | 值 |
| --- | --- |
| 类别 | 7 — 软件 |
| 严重级别 | 4 — 分诊 |
| 快速处置 | 6 — 重试 |
| 处置结果 | 错误 |
| 组件 | `L10.CPU.HOST_CPU` |
| 可重试 | True |
| 最大自动重试次数 | 1 |

### 描述

stress-ng 以非零状态退出且状态码不是 2：1 = 选项或 harness 错误，3 = 初始化/资源失败，4 = 该平台未实现该压力器，5 = 意外信号，6 = 意外退出，7 = 指标不可信。结果不确定；请勿仅凭此错误码隔离单元。

### 测试用例

`CpuStress`

### 可能原因

- DUT 上的 stress-ng 版本不支持所请求的选项/方法
- DUT 内存/资源不足，无法启动压力器
- stress-ng 被外部信号杀死（OOM killer、会话拆除）

### 采集项

- suite_run_url
- 完整的 stress-ng stdout/stderr 与退出码
- 运行窗口内的 dmesg 摘录（OOM / 信号证据）
- unit_sn, bios/fw_version, harness_version, station_id, operator_id, timestamp

### 维修措施

| 步骤 | 执行者 | 措施 | 复测 | 预计时间（分钟） | 停止条件 |
| --- | --- | --- | --- | --- | --- |
| 1 | 操作员 | 确认 DUT 上无其他工作负载在运行，重跑 CPU 子集。 | CPU_subset | 5 | — |
| 2 | 升级处理 | 将日志连同 stress-ng 退出码与 dmesg 摘录转交工程分诊。 | 不适用 |  | — |

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
