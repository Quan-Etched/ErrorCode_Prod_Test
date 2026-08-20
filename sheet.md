|  |  |  |
| :-: | :-: | :-: |
|  |  |  |
| Version | Comment | Author |
| 0.1 | Draft | Ulysses Kao |
| 0.2 | update the test case and error code for SLT 1X | Ulysses Kao |
| 0.3 | Update the error code | Ulysses Kao |

|  |  |  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Error Code ID | Message | Quick\_Action | Troubleshooting Procedure | Source | Error\_Type | Component | Test\_Case | Bugs |
| TH-C2C-0001-S2Q9 | C2C lanes failed to train or link up within the timeout: RX equalization did not converge after its configured attempts, or the link-up test reported one or more datalinks/lanes down. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | C2C | C2cLinkupTestCase, C2cLinkupMultiChipTestCase, C2cThroughputTestCase, C2cThroughputMultiChipTestCase | ETCH-33573: C2cLinkupTestCase Failure |
| TH-C2C-0002-S2Q9 | Bit-by-bit C2C loopback comparison found a data mismatch on at least one datalink/lane. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Data | C2C | C2cIntegrityTestCase, C2cIntegrityMultiChipTestCase | ETCH-33915: C2cIntegrityTestCase failure |
| TH-C2C-0003-S2Q9 | The large C2C transfer did not meet its acceptance criteria: measured throughput below the configured percentage of line rate (90% in the 1X suite), or the post-FEC uncorrected error fraction above its limit. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | C2C | C2cThroughputTestCase, C2cThroughputMultiChipTestCase | ETCH-32191: C2cIntegrityTestCase/C2cThroughputTestCase Failures |
| TH-C2C-0004-S4Q9 | Worst per-lane minimum BER from the eye-diagram sweep exceeded the configured ber\_threshold; the SERDES margin spec is not final. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | C2C | C2cLaneMarginTestCase |  |
| TH-DMA-0001-S2Q6 | Host-chip DMA data-path test failure | RETRY | Suspected test issue (single chip test timeout took down the station), retest once. | 1X Module Test | Hardware | DMA | SohuDmaTestCase | ETCH-35873: SohuDmaTestCase failure |
| TH-ENV-0001-S4Q9 | The station host or its BMC did not answer ping or SSH after boot, so no module test could start. | ESCALATE | Connect a monitor to the Devkit and verify that the system boots successfully, then try ping with host / BMC. Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Network | ENV |  |  |
| TH-ENV-0002-S4Q9 | Station fixture/setup check failed (Chroma telemetry / eval board power / vfio-proxy or PEX version) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. DO NOT retest. | 1X Module Test | Config | ENV | ChromaTelemetryCheckTestCase, EvalBoardPowerTestCase, VfioProxyVersionTestCase, CheckPexFirmwareVersionTestCase |  |
| TH-ENV-0003-S4Q9 | PLX daemon reported no PEX switches | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. DO NOT retest. | 1X Module Test | Config | ENV | CheckPexFirmwareVersionTestCase | ETCH-35552: CheckPexFirmwareVersionTestCase failure |
| TH-ENV-0004-S4Q9 | A host driver/setup utility step failed: kernel module reload, PCIe teardown or bus rescan, sysfs parameter write, or log-reader activation returned non-zero. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. DO NOT retest. | 1X Module Test | Config | ENV | ReloadKernelModuleTestCase, PcieTeardownTestCase, PcieRescanTestCase, SetSkipFlrOnOpenCloseTestCase, SohuLogReaderActivateTestCase, LogReaderCaptureTestCase, PublishBootloaderTypeTestCase | 0 |
| TH-FW-0001-S2Q9 | Sohu app firmware update failed or ASIC not pingable after update | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Config | FW | SohuFirmwareUpdateTestCase, SohuHotReloadFirmwareUpdateTestCase, SohuSecureBootRecoveryUpdateTestCase | ETCH-34843: SohuHotReloadFirmwareUpdateTestCase failure |
| TH-FW-0002-S4Q9 | The ASIC booted application firmware after the update, but the running image hash does not match the hash in the image package that was just staged. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Config | FW | SohuFirmwareUpdateTestCase |  |
| TH-FW-0003-S2Q6 | Bootloader programming failed (flash program fail or no ping after program) | RETRY | Verify that the green power indicators on the Sohu module are ON. Verify that both the PCIe cable and power cable are connected correctly and securely. If there is no trouble found, retest once. | 1X Module Test | Hardware | FW | ProgramSecureBootloaderTestCase, BootloaderResultTestCase | ETCH-35585: BootloaderResultTestCase failures |
| TH-FW-0004-S4Q6 | JTAG image load/verify failed (ICCM verify mismatch) | RETRY | Suspected test issue, retest once. | 1X Module Test | Hardware | FW | ProgramSecureBootloaderTestCase | ETCH-35586: ProgramSecureBootloaderTestCase failure |
| TH-FW-0005-S5Q2 | Fixture firmware update failed (golden VBB / retimer): OpenOCD flash, ST-Link adapter, post-flash UART/RPC ready check, or application firmware-hash verification did not succeed. | WARM\_REBOOT | Reboot Devkit, retest once. | 1X Module Test | Config | FW | VbbFirmwareUpdateTestCase, RetimerFirmwareUpdateTestCase |  |
| TH-FW-0006-S5Q9 | Board DVFS profile detection or application failed | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Config | FW | DetectBoardDvfsProfileTestCase |  |
| TH-FW-0007-S2Q6 | PLDM update did not complete within timeout — device likely not responding over Sohu UART in recovery mode | RETRY | Verify UART cabling and that recovery straps engage; rerun once; preserve logs and route to FW triage | 1X Module Test | Config | FW | SohuSecureBootRecoveryUpdateTestCase |  |
| TH-FW-0008-S2Q6 | Secure-boot recovery PLDM update failed (strap sequence or pldm\_ua error; update possibly rejected) | RETRY | Verify UART cabling/seating and rerun recovery-update subset once; then preserve unit + pldm\_ua log and verify package vs release; route to FW triage - do NOT keep retrying as device may be mid-update | 1X Module Test | Config | FW | SohuSecureBootRecoveryUpdateTestCase |  |
| TH-FW-0009-S5Q9 | Hot reload could not start, so no firmware was written | ESCALATE | Escalate to Etched with the eligibility outcome and the running image name; nothing was flashed, so do not route the unit to rework or FA. | 1X Module Test | Config | FW | SohuHotReloadFirmwareUpdateTestCase |  |
| TH-HBM-0001-S2Q9 | HBM PMBIST failure | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Memory | HBM | SohuPmbistTestCase | ETCH-33885: Power Virus failures \[was SohuPmbistTestCase failures\] |
| TH-HBM-0003-S4Q9 | HBM training/eye margin below threshold (tentative) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Memory | HBM | SohuRdqsSweepTrainingTestCase |  |
| TH-HBM-0004-S2Q6 | HBM MTC stress test failure | RETRY | Suspected test issue, retest once. | 1X Module Test | Memory | HBM | SohuMtcStressTestCase | ETCH-35299: SohuMtcStressTestCase failures |
| TH-HBM-0005-S2Q9 | PCIe-to-HBM read or write throughput on the side under test did not reach the configured min\_bandwidth\_gb\_s floor. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Memory | HBM | SohuHbmBandwidthTestCase, SohuDmaTestCase |  |
| TH-HBM-0006-S2Q9 | HBM lane repair failed - no passing repair found | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Memory | HBM | SohuLaneRepairTestCase | ETCH-35587: SohuLaneRepairTestCase failure |
| TH-HBM-0007-S2Q9 | HBM device ID read failure or mismatch | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Data | HBM | SohuHbmDeviceIdTestCase |  |
| TH-HBM-0008-S4Q9 | HBM lane repair sweep did not complete, so repairability was never established | ESCALATE | Escalate to Etched with the detection exception and the partial repair map; repairability is unknown rather than failed, so do not route the unit to FA. | 1X Module Test | Memory | HBM | SohuLaneRepairTestCase |  |
| TH-MEZZ-0001-S2Q6 | Mezz/eval CPLD register access or write failure | RETRY | Verify that the green power indicators on the Sohu module are ON. Verify that both the PCIe cable and power cable are connected correctly and securely. If there is no trouble found, retest once. | 1X Module Test | Hardware | MEZZ | ProgramSecureBootloaderTestCase, CpldDiagnosticsTestCase | ETCH-35586: ProgramSecureBootloaderTestCase failure |
| TH-MEZZ-0002-S2Q6 | Unexpected mezzanine I2C alert asserted | RETRY | Suspected test issue, retest once. | 1X Module Test | Hardware | MEZZ | MezzanineI2cAlertsTestCase |  |
| TH-PCIE-0001-S2Q6 | PCIe link state mismatch (not L0 / Gen5 / x16) | RETRY | Suspect PCIe cable not fully seated into PV1 board, reseat the cable and retest once. | 1X Module Test | Hardware | PCIE | SohuPcieAerCheckTestCase, SohuPcieRateChangeTestCase |  |
| TH-PCIE-0002-S2Q6 | PCIe AER errors detected (correctable or uncorrectable) | RETRY | Suspect PCIe cable not fully seated into PV1 board, reseat the cable and retest once. | 1X Module Test | Hardware | PCIE | SohuPcieAerCheckTestCase, SohuPcieRateChangeTestCase | ETCH-34150: Power Virus failures \[was SohuPcieAerCheckTestCase failures\] |
| TH-PCIE-0003-S2Q9 | PCIe-\>CSRAM DMA throughput below threshold (50GB/s) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PCIE | SohuPcieCsramThroughputTestCase, SohuDmaTestCase |  |
| TH-PCIE-0004-S2Q9 | PCIe-\>HBM DMA data integrity mismatch | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Data | PCIE | SohuDmaTestCase |  |
| TH-PCIE-0005-S2Q9 | PCIe-\>HBM DMA throughput below threshold (16GB/s) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PCIE | SohuDmaTestCase |  |
| TH-PCIE-0006-S2Q6 | PCIe speed change failed (Gen5\<-\>Gen1 transition) | RETRY | Suspect PCIe cable not fully seated into PV1 board, reseat the cable and retest once. | 1X Module Test | Hardware | PCIE | SohuPcieRateChangeTestCase |  |
| TH-PCIE-0007-S4Q6 | PCIe lane margin below threshold (EH\>25mV EW\>0.2UI tentative) | RETRY | Suspect PCIe cable not fully seated into PV1 board, reseat the cable and retest once. | 1X Module Test | Hardware | PCIE | SohuPcieLaneMarginTestCase |  |
| TH-PCIE-0008-S2Q6 | Sohu endpoint not enumerated (absent from PCIe tree / RPC proxy) | RETRY | Suspect PCIe cable not fully seated into PV1 board, reseat the cable and retest once. | 1X Module Test | Hardware | PCIE | PcieSetupTestCase, SohuVfioPingTestCase, SohuSaScreeningTestCase | ETCH-35872: Chips not enumerated by RPC proxy |
| TH-PWR-0001-S4Q2 | Station PSU load imbalance \>5% or PGOOD failure | WARM\_REBOOT | Known Devkit intermittent issue, retest once. | 1X Module Test | Hardware | PWR | CheckPsuHealth |  |
| TH-PWR-0002-S4Q9 | Power telemetry unavailable (VBB / VRM / VM sensor RPC / collectors not responding, or expected VM sensors missing from the reading response). | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PWR | SohuPowerTelemetryTestCase, SohuVrmTestCase, SohuVmTestCase |  |
| TH-PWR-0003-S2Q9 | Power data out of the qualified range, or CPLD reports an active VRM FSM fault on the mezzanine. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PWR | SohuPowerTelemetryTestCase, SohuVrmTestCase |  |
| TH-PWR-0004-S2Q9 | VM sensor reading outside +/-5% of nominal | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PWR | SohuVmTestCase | ETCH-34151: SohuVmTestCase failure |
| TH-PWR-0005-S2Q9 | Voltage rail adjustment not reflected in VM readback | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PWR | SohuVmTestCase |  |
| TH-PWR-0006-S4Q9 | Vmin above rated limit for SA/SAU rail | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PWR | SohuLlamaMttTestCase | ETCH-32910: SohuLlamaMttTestCase Failures |
| TH-PWR-0007-S2Q9 | Unexpected DVFS rampdown event during workload | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | PWR | SohuLlamaMttTestCase, SohuPowerVirusTestCase | ETCH-32910: SohuLlamaMttTestCase Failures |
| TH-PWR-0008-S2Q6 | Module failed to power on (indicators off / rail fault or short) | RETRY | Verify that the green power indicators on the Sohu module are ON. Verify that both the PCIe cable and power cable are connected correctly and securely. If there is no trouble found, retest once. | 1X Module Test | Hardware | PWR | BootloaderResultTestCase | ETCH-33918: SohuSecureBootRecoveryUpdateTestCase failure |
| TH-SN-0001-S2Q9 | Chip/module ID read failure or mismatch vs genealogy | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Data | SN | SohuChipIdTestCase |  |
| TH-SOHU-0001-S2Q9 | ASIC reset deassert failed | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | ProgramSecureBootloaderTestCase, BootloaderResultTestCase |  |
| TH-SOHU-0002-S2Q9 | Sohu not pingable / no response from firmware | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuFlrTestCase, SohuVfioPingTestCase, SaSortRampupHbmSingleChipTestCase, SohuWeightLoadTestCase | ETCH-35300: SaSortRampupHbmSingleChipTestCase failures |
| TH-SOHU-0003-S2Q9 | PLDM sensor discoverability or sanity check failed | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuSecureBootRecoveryUpdateTestCase |  |
| TH-SOHU-0004-S2Q9 | Mezzanine I2C transaction failed (controller bring-up, mux select, board-type read, or device probe) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuI2cTestCase | ETCH-35872: Chips not enumerated by RPC proxy |
| TH-SOHU-0005-S2Q9 | MCPU GPIO operation failed or read back the wrong value | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuGpioTestCase |  |
| TH-SOHU-0006-S2Q9 | UART ping log message absent or content mismatch | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuUartTestCase |  |
| TH-SOHU-0007-S2Q9 | JTAG check failed (debug session could not be established, or a readback did not match) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuJtagTestCase |  |
| TH-SOHU-0008-S2Q9 | eFuse region read failed | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuEfuseTestCase |  |
| TH-SOHU-0009-S2Q9 | eFuse WS/FT / MBIST repair / SA repair status incomplete | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Data | SOHU | SohuEfuseTestCase |  |
| TH-SOHU-0010-S2Q9 | CSR read-write-verify-restore failed | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuBusConnectivityTestCase |  |
| TH-SOHU-0011-S2Q9 | On-chip SRAM test failure (stuck bits / readback mismatch) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Memory | SOHU | SohuSramMemoryTestCase |  |
| TH-SOHU-0012-S2Q9 | SA matmul numeric mismatch vs reference (ULP\!=0) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SaSortRampupHbmSingleChipTestCase | ETCH-34131: SohuPowerVirusTestCase failures |
| TH-SOHU-0014-S2Q9 | Attention/SAU numeric mismatch vs funcsim | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | RunAllAttnTestsSingleChipTestCase, RunAllAttnHbmBypassTestsSingleChipTestCase, RunKvFlushTestsSingleChipTestCase, KvFlushAndAttentionSingleChipTestCase, KvFlushAndAttentionInterleavedSingleChipTestCase | ETCH-35940: 267693980000009 - Failed RunAllAttnTestsSingleChipTestCase |
| TH-SOHU-0015-S2Q9 | Workload hang / operation timeout | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | KayakTestCase, SohuPowerVirusTestCase, SohuLlamaMttTestCase | ETCH-35548: SohuPowerVirusThermalTestCase failures |
| TH-SOHU-0016-S2Q9 | Weight load spot-check mismatch | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Data | SOHU | SohuWeightLoadTestCase |  |
| TH-SOHU-0017-S2Q9 | Sustained inference throughput on the million-token test did not reach 95% of the suite's expected\_chip\_tokens\_per\_second. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuLlamaMttTestCase |  |
| TH-SOHU-0018-S2Q9 | End-to-end inference numeric mismatch vs reference | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuLlama8bFp8PrefillTestCase, SohuLlama8bFp8ForwardTestCase, SohuLlamaForwardIteratedTestCase, KayakTestCase | ETCH-34695: SohuLlama8bFp8PrefillTestCase failures |
| TH-SOHU-0019-S2Q9 | FLR failed / flr\_timeout\_s 5.0s / recovery\_timeout\_s 10.0s / not pingable between FLRs | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuFlrTestCase |  |
| TH-SOHU-0020-S2Q9 | SAU/SA PLL configuration failure: firmware did not report a safe phase alignment after FLR, or a requested PLL glitch frequency did not read back within 5% of target before timeout. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuSauPllPhaseAlignmentTestCase, SetPllGlitchFreqTestCase | ETCH-35301: SohuVfioPingTestCase failures |
| TH-SOHU-0021-S2Q9 | Defective SA column count exceeds screening limit | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuSaScreeningTestCase, SaSortRampupHbmSingleChipTestCase | ETCH-35581: SohuSaScreeningTestCase failures |
| TH-SOHU-0022-S2Q9 | Process detector (PD) chain read failure | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuPdTestCase | ETCH-33887: SohuPdTestCase failure |
| TH-THM-0001-S2Q6 | Thermal diode temperature reading out of the qualified range, reported invalid by the sensor, or an uncalibrated mezzanine diode reading below 0 C. | RETRY | Inspect the IBC TIM and ensure that the Sohu module is properly seated and secured in the fixture. Also verify that the Sohu module top cold plate is connected to the HRM cooling loop. If there is no trouble found, retest once. | 1X Module Test | Hardware | THM | SohuThermalDiodeTestCase, SohuDtsTestCase | ETCH-35857: MLT DTS faiure Peak-to-peak deviation: 33029224 uC is out of bounds (30000000) |
| TH-THM-0002-S2Q6 | The peak-to-peak spread across usable Sohu DTS readings exceeded the configured deviation limit. | RETRY | Inspect the IBC TIM and ensure that the Sohu module is properly seated and secured in the fixture. Also verify that the Sohu module top cold plate is connected to the HRM cooling loop. If there is no trouble found, retest once. | 1X Module Test | Hardware | THM | SohuDtsTestCase | ETCH-35857: MLT DTS faiure Peak-to-peak deviation: 33029224 uC is out of bounds (30000000) |
| TH-THM-0003-S2Q9 | CTS protection did not shut off chip at minimum threshold | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | THM | SohuCtsTestCase |  |
| TH-THM-0004-S2Q6 | Catastrophic trip event during stress workload | RETRY | Inspect the IBC TIM and ensure that the Sohu module is properly seated and secured in the fixture. Also verify that the Sohu module top cold plate is connected to the HRM cooling loop. If there is no trouble found, retest once. | 1X Module Test | Hardware | THM | SohuPowerVirusThermalTestCase | ETCH-35548: SohuPowerVirusThermalTestCase failures |
| TH-THM-0005-S4Q9 | DTS peak-to-peak deviation under power virus out of bounds | ESCALATE | If any temperature reading is out of spec verify that the affected unit has completed the required 45-min TIM baking process. Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | THM | SohuDtsTestCase, SohuPowerVirusTestCase | ETCH-35857: MLT DTS faiure Peak-to-peak deviation: 33029224 uC is out of bounds (30000000) |
| TH-THM-0006-S2Q9 | Peak DTS temperature under power virus exceeds expected maximum | ESCALATE | If any temperature reading is out of spec verify that the affected unit has completed the required 45-min TIM baking process. Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | THM | SohuPowerVirusThermalTestCase | ETCH-34688: SohuPowerVirusThermalTestCase failures |
| TH-THM-0007-S4Q9 | TMP464 thermal telemetry unreadable or malformed — verdict inconclusive (test-system ERROR, excluded from yield) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Software | THM | SohuThermalDiodeTestCase |  |
| TH-HAR-0002-S5Q9 | A test case was invoked with invalid or unsupported arguments and rejected the run before touching the DUT. | ESCALATE | Fix the suite YAML for this test; do not route the unit to rework | 1X Module Test | Config | Harness | SohuSecureBootRecoveryUpdateTestCase, ServerNestedTestCase, SohuSnapTestCase, VfioProxyVersionTestCase, SohuWeightLoadTestCase, SltModuleNestedTestCase |  |
| TH-HAR-0003-S5Q9 | Tool/binary/data file the test depends on is missing on the test system (test-system ERROR — excluded from module yield) | ESCALATE | Fix the station deployment / harness package; do not route the unit to rework | 1X Module Test | Config | Harness | SohuSecureBootRecoveryUpdateTestCase, SohuWeightLoadTestCase, VbbFirmwareUpdateTestCase |  |
| TH-HAR-0004-S4Q9 | Nested suite failed to launch or complete orchestration (child test failures carry their own codes) | ESCALATE | Check suite config/resources; wrapper must propagate the first/most-severe child error code - never mint duplicate codes for child failures (test-system ERROR - excluded from yield) | 1X Module Test | Config | HAR | ServerNestedTestCase, SltModuleNestedTestCase |  |
| TH-SOHU-0023-S2Q9 | Chip bin below acceptance threshold / failed binning criteria | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuChipBinTestCase |  |
| TH-SOHU-0024-S5Q9 | Required screening data missing or failed to load (SA mask / bin inputs), including eFuse/Flash init-config read failures and invalid screening bin encodings. | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Config | SOHU | SohuChipBinTestCase, SohuSaScreeningTestCase, SaSortRampupHbmSingleChipTestCase | ETCH-34698 |
| TH-SOHU-0025-S4Q9 | Chip state snapshot capture failed | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuSnapTestCase |  |
| TH-SOHU-0026-S2Q9 | PLL glitch frequency did not read back within 5% of target before timeout | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SetPllGlitchFreqTestCase |  |
| TH-SOHU-0027-S2Q9 | VFIO ping responses received but none within the allowed latency (device pingable, latency out of spec) | ESCALATE | Collect the suite/test logs and artifacts for this failure. Escalate to Etched engineer with the collected logs. | 1X Module Test | Hardware | SOHU | SohuVfioPingTestCase |  |
| TH-SOHU-0024-S5Q9 | Required screening data missing or failed to load (SA mask / bin inputs) | HALT\_ESCALATE | Escalate to Etched | 1X Module Test | Config | SOHU | SohuChipBinTestCase, SohuSaScreeningTestCase, SaSortRampupHbmSingleChipTestCase | ETCH-34698 |
| TH-SOHU-0025-S4Q6 | Chip state snapshot capture failed | HALT\_ESCALATE | Escalate to Etched | 1X Module Test | Hardware | SOHU | SohuSnapTestCase |  |
| TH-SOHU-0026-S2Q9 | PLL glitch frequency did not read back within 5% of target before timeout | HALT\_ESCALATE | Escalate to Etched | 1X Module Test | Hardware | SOHU | SetPllGlitchFreqTestCase |  |
| TH-SOHU-0027-S2Q9 | VFIO ping responses received but none within the allowed latency (device pingable, latency out of spec) | HALT\_ESCALATE | Escalate to Etched | 1X Module Test | Hardware | SOHU | SohuVfioPingTestCase |  |
| TH-SOHU-0028-S4Q9 | MTT binary exited non-zero for a reason the harness cannot determine | HALT\_ESCALATE | Escalate to Etched | 1X Module Test | Software | SOHU | SohuLlamaMttTestCase |  |

|  |  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Error Code ID | Packed | Name | Message | Quick\_Action | Source | Component | Test\_Case |
| TH-SOHU-0002-S2Q9 | 371785730 | SOHU\_NOT\_PINGABLE | Sohu not pingable / no response from firmware | Halt & escalate | L10 Test | SOHU | SohuPingTestCase, SohuVfioPingMultiChipTestCase, SohuFlrMultiChipTestCase |
| TH-SOHU-0011-S2Q9 | 321454091 | SOHU\_SRAM\_TEST\_FAILED | On-chip SRAM test failure (stuck bits / readback mismatch) | Halt & escalate | L10 Test | SOHU | SohuSramMemoryMultiChipTestCase |
| TH-SOHU-0015-S2Q9 | 371785743 | SOHU\_WORKLOAD\_TIMEOUT | Workload hang / operation timeout | Halt & escalate | L10 Test | SOHU | SohuMlpTp8TestCase, SohuLlama70bForwardIteratedTestCase, SohuLlama70bHp8ForwardIteratedTestCase, SohuLlamaTp8InferenceMaxTestCase, Llama8bFp8Tp1SmokeTestCase, SohuPowerVirusMultiChipTestCase |
| TH-SOHU-0016-S2Q9 | 455671824 | SOHU\_WEIGHT\_LOAD\_MISMATCH | Weight load spot-check mismatch | Halt & escalate | L10 Test | SOHU | SohuLlama70bForwardIteratedTestCase, SohuLlama70bHp8ForwardIteratedTestCase, SohuLlamaTp8InferenceMaxTestCase, Llama8bFp8Tp1SmokeTestCase |
| TH-SOHU-0017-S2Q9 | 371785745 | SOHU\_INFERENCE\_THROUGHPUT\_BELOW\_THRESHOLD | Sustained inference throughput on the million-token test did not reach 95% of the suite's expected\_chip\_tokens\_per\_second. | Halt & escalate | L10 Test | SOHU | SohuLlamaTp8InferenceMaxTestCase |
| TH-SOHU-0018-S2Q9 | 371785746 | SOHU\_INFERENCE\_NUMERIC\_MISMATCH | End-to-end inference numeric mismatch vs reference | Halt & escalate | L10 Test | SOHU | SohuMlpTp8TestCase, SohuLlama70bForwardIteratedTestCase, SohuLlama70bHp8ForwardIteratedTestCase, SohuLlamaTp8InferenceMaxTestCase, Llama8bFp8Tp1SmokeTestCase |
| TH-SOHU-0019-S2Q9 | 371785747 | SOHU\_FLR\_FAILED | FLR failed / flr\_timeout\_s 5.0s / recovery\_timeout\_s 10.0s / not pingable between FLRs | Halt & escalate | L10 Test | SOHU | SohuFlrMultiChipTestCase |
| TH-SOHU-0025-S4Q9 | 373882905 | SOHU\_SNAPSHOT\_CAPTURE\_FAILED | Chip state snapshot capture failed | Halt & escalate | L10 Test | SOHU | SohuSnapTestCase |
| TH-SOHU-0027-S2Q9 | 371785755 | SOHU\_VFIO\_PING\_LATENCY\_EXCEEDED | VFIO ping responses received but none within the allowed latency (device pingable, latency out of spec) | Halt & escalate | L10 Test | SOHU | SohuVfioPingMultiChipTestCase |
| TH-SOHU-0028-S4Q9 | 390660124 | SOHU\_WORKLOAD\_BINARY\_FAILED | MTT binary exited non-zero for a reason the harness cannot determine | Halt & escalate | L10 Test | SOHU | SohuMlpTp8TestCase, SohuLlama70bForwardIteratedTestCase, SohuLlama70bHp8ForwardIteratedTestCase, SohuLlamaTp8InferenceMaxTestCase, Llama8bFp8Tp1SmokeTestCase |
| TH-C2C-0001-S2Q9 | 371785729 | C2C\_LINKUP\_FAILED | C2C lanes failed to train or link up within the timeout: RX equalization did not converge after its configured attempts, or the link-up test reported one or more datalinks/lanes down. | Halt & escalate | L10 Test | C2C | C2cLinkupMultiChipTestCase, C2cThroughputMultiChipTestCase |
| TH-C2C-0002-S2Q9 | 455671810 | C2C\_INTEGRITY\_MISMATCH | Bit-by-bit C2C loopback comparison found a data mismatch on at least one datalink/lane. | Halt & escalate | L10 Test | C2C | C2cIntegrityMultiChipTestCase |
| TH-C2C-0003-S2Q9 | 371785731 | C2C\_THROUGHPUT\_BELOW\_THRESHOLD | The large C2C transfer did not meet its acceptance criteria: measured throughput below the configured percentage of line rate (90% in the 1X suite), or the post-FEC uncorrected error fraction above its limit. | Halt & escalate | L10 Test | C2C | C2cThroughputMultiChipTestCase |
| TH-C2C-0004-S4Q9 | 373882884 | C2C\_LANE\_MARGIN\_BELOW\_THRESHOLD | Worst per-lane minimum BER from the eye-diagram sweep exceeded the configured ber\_threshold; the SERDES margin spec is not final. | Halt & escalate | L10 Test | C2C | C2cFirCdrSweepMultiChipTestCase |
| TH-C2C-0005-S2Q9 | 455671813 | C2C\_PRBS\_ERROR\_THRESHOLD\_EXCEEDED | The C2C PRBS run completed but the observed bit-error count or rate exceeded the configured acceptance limit. | Halt & escalate | L10 Test | C2C | C2cPrbsMultiChipTestCase |
| TH-C2C-0006-S4Q9 | 390660102 | C2C\_SWEEP\_OUTPUT\_INVALID | The FIR/CDR or PRBS test did not produce complete, parseable lane results, so the C2C verdict is inconclusive. | Halt & escalate | L10 Test | C2C | C2cFirCdrSweepMultiChipTestCase, C2cPrbsMultiChipTestCase |
| TH-PCIE-0001-S2Q6 | 371589121 | PCIE\_LINK\_STATE\_MISMATCH | PCIe link state mismatch (not L0 / Gen5 / x16) | Retry | L10 Test | PCIE | CheckPcieTopology |
| TH-PCIE-0003-S2Q9 | 371785731 | PCIE\_CSRAM\_DMA\_THROUGHPUT\_BELOW\_THRESHOLD | PCIe-\>CSRAM DMA throughput below threshold (50GB/s) | Halt & escalate | L10 Test | PCIE | SohuDmaMultiChipTestCase |
| TH-PCIE-0004-S2Q9 | 455671812 | PCIE\_HBM\_DMA\_DATA\_MISMATCH | PCIe-\>HBM DMA data integrity mismatch | Halt & escalate | L10 Test | PCIE | SohuDmaMultiChipTestCase |
| TH-PCIE-0005-S2Q9 | 371785733 | PCIE\_HBM\_DMA\_THROUGHPUT\_BELOW\_THRESHOLD | PCIe-\>HBM DMA throughput below threshold (16GB/s) | Halt & escalate | L10 Test | PCIE | SohuDmaMultiChipTestCase |
| TH-PCIE-0008-S2Q6 | 371589128 | SOHU\_ENDPOINT\_NOT\_ENUMERATED | Sohu endpoint not enumerated (absent from PCIe tree / RPC proxy) | Retry | L10 Test | PCIE | CheckPcieTopology, SohuVfioPingMultiChipTestCase |
| TH-PCIE-0009-S5Q9 | 358154249 | PCIE\_EXPECTED\_TOPOLOGY\_UNAVAILABLE | The expected PCIe topology or device specification could not be loaded; no PCIe DUT verdict is available. | Halt & escalate | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0010-S4Q9 | 390660106 | PCIE\_INVENTORY\_QUERY\_FAILED | The PCIe inventory command failed, so the test could not enumerate devices or links. | Halt & escalate | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0011-S4Q9 | 390660107 | PCIE\_INVENTORY\_OUTPUT\_INVALID | The PCIe inventory output was empty, incomplete, or could not be parsed into a reliable topology. | Halt & escalate | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0012-S5Q9 | 358154252 | PCIE\_TOPOLOGY\_SPEC\_INVALID | The configured PCIe topology contains invalid or conflicting device identifiers, counts, or topology indices. | Halt & escalate | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0013-S2Q6 | 371589133 | PCIE\_TOPOLOGY\_MISMATCH | The discovered PCIe device count or parent/child topology does not match the expected server topology. | Retry | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0014-S2Q9 | 455671822 | PCIE\_DEVICE\_IDENTITY\_MISMATCH | A discovered PCIe device has an unexpected vendor ID, device ID, subsystem ID, or configured device name. | Halt & escalate | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0015-S4Q9 | 457768975 | PCIE\_DUPLICATE\_BDF | Two expected or discovered PCIe devices resolve to the same bus/device/function address. | Halt & escalate | L10 Test | PCIe | CheckPcieTopology |
| TH-PCIE-0016-S4Q9 | 390660112 | PLX\_DAEMON\_VERSION\_QUERY\_FAILED | The PLX daemon firmware/version query failed or returned no usable switch information. | Halt & escalate | L10 Test | PLX switch | CheckPlxDaemonFirmwareVersion |
| TH-PCIE-0017-S5Q9 | 358154257 | PLX\_DAEMON\_FIRMWARE\_VERSION\_MISMATCH | The PLX daemon or switch firmware version does not match the expected L10 release. | Halt & escalate | L10 Test | PLX switch | CheckPlxDaemonFirmwareVersion |
| TH-PCIE-0018-S4Q9 | 357105682 | PLX\_DAEMON\_FIRMWARE\_UPDATE\_FAILED | The PLX daemon firmware update or activation command failed. | Halt & escalate | L10 Test | PLX switch | UpdatePlxDaemonFirmwareVersion |
| TH-PCIE-0019-S4Q9 | 357105683 | PLX\_DAEMON\_POST\_UPDATE\_VERIFY\_FAILED | PLX daemon firmware did not report the requested version after the update completed. | Halt & escalate | L10 Test | PLX switch | UpdatePlxDaemonFirmwareVersion |
| TH-HBM-0001-S2Q9 | 321454081 | HBM\_PMBIST\_FAILED | HBM PMBIST failure | Halt & escalate | L10 Test | HBM | SohuPmbistMultiChipTestCase |
| TH-HBM-0004-S2Q6 | 321257476 | HBM\_MTC\_STRESS\_FAILED | HBM MTC stress test failure | Retry | L10 Test | HBM | SohuMtcStressMultiChipTestCase |
| TH-HBM-0005-S2Q9 | 321454085 | HBM\_DMA\_BANDWIDTH\_BELOW\_THRESHOLD | PCIe-to-HBM read or write throughput on the side under test did not reach the configured min\_bandwidth\_gb\_s floor. | Halt & escalate | L10 Test | HBM | SohuDmaMultiChipTestCase |
| TH-HBM-0006-S2Q9 | 321454086 | HBM\_LANE\_REPAIR\_FAILED | HBM lane repair failed - no passing repair found | Halt & escalate | L10 Test | HBM | SohuLaneRepairMultiChipTestCase |
| TH-HBM-0007-S2Q9 | 455671815 | HBM\_DEVICE\_ID\_MISMATCH | HBM device ID read failure or mismatch | Halt & escalate | L10 Test | HBM | SohuHbmDeviceIdMultiChipTestCase |
| TH-HBM-0008-S4Q9 | 323551240 | HBM\_LANE\_REPAIR\_INCONCLUSIVE | HBM lane repair sweep did not complete, so repairability was never established | Halt & escalate | L10 Test | HBM | SohuLaneRepairMultiChipTestCase |
| TH-MEM-0001-S4Q9 | 390660097 | MEMORY\_INVENTORY\_QUERY\_FAILED | The host memory inventory command failed; no DIMM verdict is available. | Halt & escalate | L10 Test | Host Memory | CheckMemory |
| TH-MEM-0002-S4Q9 | 390660098 | MEMORY\_INVENTORY\_OUTPUT\_INVALID | The host memory inventory output was malformed or could not be parsed. | Halt & escalate | L10 Test | Host Memory | CheckMemory |
| TH-MEM-0003-S2Q9 | 321454083 | NO\_DIMMS\_DETECTED | No populated DIMMs were detected although the L10 BOM requires host memory. | Halt & escalate | L10 Test | Host Memory | CheckMemory |
| TH-MEM-0004-S2Q9 | 321454084 | DIMM\_COUNT\_MISMATCH | The number of populated DIMMs does not match the expected L10 BOM. | Halt & escalate | L10 Test | Host Memory | CheckMemory |
| TH-MEM-0005-S2Q9 | 455671813 | DIMM\_IDENTITY\_OR\_CAPACITY\_MISMATCH | A DIMM manufacturer, part number, serial number, location, or capacity does not match the expected BOM. | Halt & escalate | L10 Test | Host Memory | CheckMemory |
| TH-MEM-0006-S4Q9 | 357105670 | MIXED\_DIMM\_CONFIGURATION | The installed DIMMs are not homogeneous where the platform configuration requires matching parts and capacities. | Halt & escalate | L10 Test | Host Memory | CheckMemory |
| TH-MEM-0007-S2Q6 | 321257479 | MEMORY\_STRESS\_FAILED | The host memory stress workload reported data errors, verification failures, or a workload-failure exit status. | Retry | L10 Test | Host Memory | MemoryStressNg, MemoryStress |
| TH-MEM-0008-S4Q9 | 390660104 | MEMORY\_STRESS\_METRICS\_INVALID | The memory stress tool completed without usable result statistics or produced malformed metrics, so the verdict is inconclusive. | Halt & escalate | L10 Test | Host Memory | MemoryStressNg, MemoryStress |
| TH-MEM-0009-S5Q9 | 358154249 | NUMA\_TOPOLOGY\_PRECONDITION\_NOT\_MET | The host NUMA/SNC topology does not provide the nodes required by the configured cross-NUMA I/O stress. | Halt & escalate | L10 Test | Host Memory | IoStress |
| TH-MEM-0010-S2Q6 | 321257482 | CROSS\_NUMA\_MEMORY\_STRESS\_FAILED | The cross-NUMA stream or memory-transfer workload failed its execution or acceptance criteria. | Retry | L10 Test | Host Memory | IoStress |
| TH-CPU-0001-S2Q6 | 371589121 | CPU\_STRESS\_FAIL | stress-ng CPU stress failed because a stressor/verification error occurred or the tool returned its workload-failure status. | Retry | L10 Test | CPU | CpuStress |
| TH-CPU-0003-S5Q9 | 391708675 | CPU\_STRESS\_TOOL\_UNAVAILABLE | stress-ng is not installed or cannot be executed on the target; no CPU verdict is available (ERROR disposition; excluded from DUT yield). | Halt & escalate | L10 Test | CPU | CpuStress |
| TH-CPU-0004-S4Q6 | 390463492 | CPU\_STRESS\_EXECUTION\_ERROR | stress-ng returned an execution, initialization, option, resource, unsupported-stressor, or signal error rather than a CPU workload verdict. | Retry | L10 Test | CPU | CpuStress |
| TH-CPU-0005-S4Q9 | 390660101 | CPU\_INVENTORY\_QUERY\_FAILED | The CPU inventory command failed; no CPU BOM verdict is available. | Halt & escalate | L10 Test | CPU | CheckCpu |
| TH-CPU-0006-S4Q9 | 390660102 | CPU\_INVENTORY\_OUTPUT\_INVALID | The CPU inventory output was malformed or could not be parsed into processor records. | Halt & escalate | L10 Test | CPU | CheckCpu |
| TH-CPU-0007-S2Q9 | 371785735 | CPU\_COUNT\_MISMATCH | The discovered processor count does not match the expected L10 BOM. | Halt & escalate | L10 Test | CPU | CheckCpu |
| TH-CPU-0008-S2Q9 | 455671816 | CPU\_IDENTITY\_MISMATCH | A processor part number or manufacturer does not match the expected L10 BOM. | Halt & escalate | L10 Test | CPU | CheckCpu |
| TH-CPU-0009-S2Q9 | 371785737 | CPU\_TOPOLOGY\_MISMATCH | A processor core count or thread count does not match the expected L10 BOM. | Halt & escalate | L10 Test | CPU | CheckCpu |
| TH-CPU-0010-S4Q9 | 357105674 | CPU\_CLOCK\_MISMATCH | A processor base or maximum clock reported by inventory does not match the expected L10 BOM. | Halt & escalate | L10 Test | CPU | CheckCpu |
| TH-DMA-0001-S2Q6 | 371589121 | DMA\_DATA\_PATH\_TEST\_FAILED | Host-chip DMA data-path test failure | Retry | L10 Test | DMA | SohuDmaMultiChipTestCase |
| TH-DISK-0001-S4Q9 | 390660097 | DISK\_INVENTORY\_QUERY\_FAILED | The block-device or NVMe inventory command failed; no storage verdict is available. | Halt & escalate | L10 Test | Disk | CheckDisk, DiskFormat, DiskSmart, DiskStress |
| TH-DISK-0002-S4Q9 | 390660098 | DISK\_INVENTORY\_OUTPUT\_INVALID | Block-device or NVMe inventory output was malformed or could not be parsed. | Halt & escalate | L10 Test | Disk | CheckDisk, DiskFormat, DiskStress |
| TH-DISK-0003-S2Q9 | 304676867 | NO\_DISKS\_DETECTED | No storage devices were detected although the L10 BOM requires disks. | Halt & escalate | L10 Test | Disk | CheckDisk, DiskSmart |
| TH-DISK-0004-S2Q9 | 304676868 | DISK\_COUNT\_MISMATCH | The discovered disk count does not match the expected L10 BOM. | Halt & escalate | L10 Test | Disk | CheckDisk |
| TH-DISK-0005-S2Q9 | 455671813 | DISK\_IDENTITY\_OR\_CAPACITY\_MISMATCH | A disk model, serial number, namespace, or capacity does not match the expected L10 BOM. | Halt & escalate | L10 Test | Disk | CheckDisk |
| TH-DISK-0006-S4Q9 | 357105670 | MIXED\_DRIVE\_CONFIGURATION | Installed drives do not satisfy the required homogeneous model/capacity configuration. | Halt & escalate | L10 Test | Disk | CheckDisk |
| TH-DISK-0007-S5Q9 | 358154247 | BOOT\_DEVICE\_UNDETERMINED | The test could not reliably identify the host boot device and therefore could not safely select data drives. | Halt & escalate | L10 Test | Disk | DiskFormat, DiskStress |
| TH-DISK-0008-S5Q9 | 358154248 | NO\_TESTABLE\_NVME\_DEVICES | No eligible non-boot NVMe device remained after discovery and configured exclusions. | Halt & escalate | L10 Test | Disk | DiskFormat, DiskSmart, DiskStress |
| TH-DISK-0009-S2Q9 | 304676873 | NVME\_NAMESPACE\_MISSING | An expected NVMe controller has no usable namespace and automatic formatting is disabled. | Halt & escalate | L10 Test | NVMe SSD | DiskFormat |
| TH-DISK-0010-S4Q9 | 306774026 | NVME\_FORMAT\_FAILED | The NVMe format or namespace creation command failed. | Halt & escalate | L10 Test | NVMe SSD | DiskFormat |
| TH-DISK-0011-S2Q9 | 304676875 | NVME\_NAMESPACE\_NOT\_CREATED | The expected NVMe namespace was still absent after the format/namespace operation completed. | Halt & escalate | L10 Test | NVMe SSD | DiskFormat |
| TH-DISK-0012-S2Q9 | 304676876 | NVME\_SMART\_SELF\_TEST\_FAILED | An NVMe device self-test completed with a failure or did not complete successfully. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0013-S4Q9 | 390660109 | NVME\_SMART\_DATA\_UNAVAILABLE | SMART/health data could not be read for an eligible NVMe device. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0014-S2Q9 | 304676878 | NVME\_SMART\_CRITICAL\_WARNING | The NVMe SMART critical-warning field is non-zero. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0015-S2Q9 | 304676879 | NVME\_AVAILABLE\_SPARE\_BELOW\_THRESHOLD | NVMe available spare is below the device or configured threshold. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0016-S2Q9 | 304676880 | NVME\_MEDIA\_ERRORS\_DETECTED | NVMe SMART reports one or more media/data-integrity errors. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0017-S4Q9 | 373882897 | NVME\_TEMPERATURE\_OUT\_OF\_RANGE | NVMe temperature is outside the configured safe operating range. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0018-S2Q9 | 304676882 | NVME\_WEAR\_LIMIT\_EXCEEDED | NVMe percentage-used or wear indicator exceeds the configured acceptance limit. | Halt & escalate | L10 Test | NVMe SSD | DiskSmart |
| TH-DISK-0019-S2Q6 | 304480275 | DISK\_STRESS\_FIO\_FAILED | The fio disk stress workload returned a workload-failure status for an eligible drive. | Retry | L10 Test | Disk | DiskStress |
| TH-DISK-0020-S4Q9 | 390660116 | DISK\_STRESS\_OUTPUT\_INVALID | fio output was missing or could not be parsed into valid per-drive results. | Halt & escalate | L10 Test | Disk | DiskStress |
| TH-NIC-0001-S5Q9 | 358154241 | NIC\_EXPECTED\_CONFIG\_UNAVAILABLE | The expected NIC/BOM/network configuration could not be loaded; no NIC verdict is available. | Halt & escalate | L10 Test | NIC | CheckNic, CheckLomNicMac, LoopbackTopologyTest, NetworkBwRdmaTest, CheckNicAsicRails |
| TH-NIC-0002-S4Q9 | 390660098 | NIC\_INVENTORY\_QUERY\_FAILED | NIC inventory or interface discovery failed. | Halt & escalate | L10 Test | NIC | CheckNic, CheckLomNicMac, LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0003-S4Q9 | 390660099 | NIC\_DISCOVERY\_SERVICE\_UNAVAILABLE | The NIC discovery/netd service or its Unix-domain socket was not ready or reachable. | Halt & escalate | L10 Test | NIC | CheckNic, CheckInterfaceLinkStatus, CheckNetdReadiness |
| TH-NIC-0004-S2Q9 | 287899652 | NIC\_COUNT\_MISMATCH | The discovered NIC count does not match the expected L10 BOM. | Halt & escalate | L10 Test | NIC | CheckNic |
| TH-NIC-0005-S2Q9 | 455671813 | NIC\_IDENTITY\_MISMATCH | A NIC vendor, device, name, speed capability, or expected grouping does not match configuration. | Halt & escalate | L10 Test | NIC | CheckNic |
| TH-NIC-0006-S4Q9 | 457768966 | NIC\_DUPLICATE\_PCI\_ADDRESS | Multiple NIC records resolve to the same PCI address. | Halt & escalate | L10 Test | NIC | CheckNic |
| TH-NIC-0007-S2Q9 | 287899655 | UNEXPECTED\_NIC\_DETECTED | A NIC that is not present in the expected L10 configuration was discovered. | Halt & escalate | L10 Test | NIC | CheckNic |
| TH-NIC-0008-S2Q9 | 287899656 | LOM\_NIC\_NOT\_DETECTED | The configured LAN-on-motherboard interface was not found. | Halt & escalate | L10 Test | LOM NIC | CheckLomNicMac |
| TH-NIC-0009-S2Q9 | 455671817 | LOM\_MAC\_ADDRESS\_MISMATCH | The LAN-on-motherboard MAC address does not match the expected service/BOM value. | Halt & escalate | L10 Test | LOM NIC | CheckLomNicMac |
| TH-NIC-0010-S4Q9 | 390660106 | NIC\_DRIVER\_QUERY\_FAILED | The installed NIC driver or firmware version could not be queried. | Halt & escalate | L10 Test | NIC | CheckBroadcomDrivers |
| TH-NIC-0011-S5Q9 | 358154251 | NIC\_DRIVER\_VERSION\_MISMATCH | The installed NIC kernel driver does not match the required L10 release. | Halt & escalate | L10 Test | NIC | CheckBroadcomDrivers |
| TH-NIC-0012-S5Q9 | 358154252 | NIC\_FIRMWARE\_VERSION\_MISMATCH | The installed NIC firmware does not match the required L10 release. | Halt & escalate | L10 Test | NIC | CheckBroadcomDrivers |
| TH-NIC-0013-S4Q9 | 390660109 | NIC\_VERSION\_OUTPUT\_INVALID | NIC driver/firmware version output was incomplete or could not be parsed. | Halt & escalate | L10 Test | NIC | CheckBroadcomDrivers |
| TH-NIC-0014-S2Q6 | 287703054 | NIC\_INTERFACE\_LINK\_DOWN | A required NIC interface has no carrier or is not operationally up. | Retry | L10 Test | NIC | CheckInterfaceLinkStatus, LoopbackTopologyTest |
| TH-NIC-0015-S4Q9 | 390660111 | NETD\_NOT\_READY | netd did not reach its ready state within the configured wait interval. | Halt & escalate | L10 Test | NIC | CheckNetdReadiness |
| TH-NIC-0016-S5Q9 | 358154256 | NETD\_ACTIVE\_SLAVE\_MISMATCH | The active bond slave reported by netd is not the configured expected interface. | Halt & escalate | L10 Test | NIC | CheckNetdReadiness |
| TH-NIC-0017-S2Q9 | 287899665 | LOOPBACK\_GROUP\_COUNT\_MISMATCH | A configured loopback NIC group does not contain the expected number of interfaces. | Halt & escalate | L10 Test | NIC | LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0018-S5Q9 | 358154258 | LOOPBACK\_TOPOLOGY\_INDEX\_INVALID | A configured loopback client/server index is outside the discovered NIC group. | Halt & escalate | L10 Test | NIC | LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0019-S2Q9 | 287899667 | RDMA\_DEVICE\_UNAVAILABLE | A required interface has no RDMA device binding or the configured group has no RDMA-capable interface. | Halt & escalate | L10 Test | NIC | LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0020-S4Q9 | 390660116 | LOOPBACK\_PAIR\_CONFIGURATION\_FAILED | The test could not configure the loopback pair IP, MTU, namespace, neighbor, or interface state. | Halt & escalate | L10 Test | NIC | LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0021-S4Q9 | 289996821 | ROCE\_GID\_UNAVAILABLE | A required IPv4 RoCE v2 GID could not be found for one or both interfaces in the pair. | Halt & escalate | L10 Test | NIC | LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0022-S2Q6 | 287703062 | LOOPBACK\_PROBE\_FAILED | The short RDMA loopback probe failed to establish traffic or returned a workload failure. | Retry | L10 Test | NIC | LoopbackTopologyTest |
| TH-NIC-0023-S5Q9 | 358154263 | NO\_RDMA\_PAIRS\_TO\_TEST | No valid RDMA-capable client/server pair remained after discovery and topology validation. | Halt & escalate | L10 Test | NIC | NetworkBwRdmaTest |
| TH-NIC-0024-S4Q9 | 390660120 | RDMA\_SERVER\_START\_FAILED | The ib\_write\_bw server process could not be started for an RDMA pair. | Halt & escalate | L10 Test | NIC | NetworkBwRdmaTest |
| TH-NIC-0025-S2Q6 | 287703065 | RDMA\_CLIENT\_EXECUTION\_FAILED | The ib\_write\_bw client timed out or returned a non-zero status for an RDMA pair. | Retry | L10 Test | NIC | NetworkBwRdmaTest |
| TH-NIC-0026-S4Q9 | 390660122 | RDMA\_BANDWIDTH\_OUTPUT\_INVALID | The RDMA bandwidth tool did not emit a parseable average-bandwidth result. | Halt & escalate | L10 Test | NIC | NetworkBwRdmaTest |
| TH-NIC-0027-S2Q9 | 287899675 | RDMA\_BANDWIDTH\_BELOW\_THRESHOLD | Measured RDMA bandwidth for a configured pair is below the configured percentage of expected line rate. | Halt & escalate | L10 Test | NIC | NetworkBwRdmaTest |
| TH-NIC-0028-S5Q9 | 358154268 | NIC\_RAIL\_CONFIG\_UNAVAILABLE | The expected NIC ASIC rail limits could not be loaded from product configuration. | Halt & escalate | L10 Test | NIC ASIC Rails | CheckNicAsicRails |
| TH-NIC-0029-S4Q9 | 373882909 | NIC\_RAIL\_READING\_UNAVAILABLE | A required NIC ASIC voltage-rail reading is unavailable or reported as not applicable. | Halt & escalate | L10 Test | NIC ASIC Rails | CheckNicAsicRails |
| TH-NIC-0030-S2Q9 | 371785758 | NIC\_RAIL\_OUT\_OF\_RANGE | A NIC ASIC voltage rail is below its configured minimum or above its configured maximum. | Halt & escalate | L10 Test | NIC ASIC Rails | CheckNicAsicRails |
| TH-NIC-0031-S4Q9 | 357105695 | NIC\_FIRMWARE\_UPDATE\_FAILED | The Broadcom NIC firmware update command failed. | Halt & escalate | L10 Test | NIC | BroadcomUpdateFwAndConfigure |
| TH-NIC-0032-S4Q9 | 357105696 | NIC\_CONFIGURATION\_APPLY\_FAILED | Required NIC port, driver, or firmware configuration could not be applied. | Halt & escalate | L10 Test | NIC | BroadcomUpdateFwAndConfigure |
| TH-NIC-0033-S4Q9 | 357105697 | NIC\_POST\_UPDATE\_VERIFY\_FAILED | NIC firmware or configuration did not match the requested state after update. | Halt & escalate | L10 Test | NIC | BroadcomUpdateFwAndConfigure |
| TH-NIC-0034-S4Q9 | 457768994 | NIC\_MAC\_ADDRESS\_UNAVAILABLE | A required interface MAC address could not be read while constructing a loopback/RDMA pair. | Halt & escalate | L10 Test | NIC | LoopbackTopologyTest, NetworkBwRdmaTest |
| TH-NIC-0035-S2Q6 | 287703075 | NIC\_LINK\_RECOVERY\_FAILED | A carrier-down interface did not recover after the configured link-speed/FEC recovery sequence. | Retry | L10 Test | NIC | LoopbackTopologyTest |
| TH-VBB-0001-S4Q9 | 390660097 | BASEBOARD\_INVENTORY\_QUERY\_FAILED | Baseboard/VBB inventory or version information could not be queried. | Halt & escalate | L10 Test | VBB | CheckBaseboard, CheckBaseboardVersion |
| TH-VBB-0002-S2Q9 | 455671810 | BASEBOARD\_IDENTITY\_MISMATCH | Baseboard manufacturer, product, serial, or board identity does not match the expected BOM. | Halt & escalate | L10 Test | VBB | CheckBaseboard |
| TH-VBB-0003-S5Q9 | 358154243 | BASEBOARD\_VERSION\_MISMATCH | The baseboard/VBB hardware or firmware version does not match the expected release. | Halt & escalate | L10 Test | VBB | CheckBaseboardVersion |
| TH-VBB-0004-S5Q9 | 358154244 | BASEBOARD\_EXPECTED\_CONFIG\_UNAVAILABLE | Expected baseboard/VBB BOM or version data could not be loaded; no DUT verdict is available. | Halt & escalate | L10 Test | VBB | CheckBaseboard, CheckBaseboardVersion |
| TH-MEZZ-0001-S2Q6 | 371589121 | MEZZ\_CPLD\_ACCESS\_FAILED | Mezz/eval CPLD register access or write failure | Retry | L10 Test | MEZZ | CpldDiagnosticsRemoteTestCase |
| TH-BMC-0001-S5Q9 | 358154241 | BMC\_EXPECTED\_CONFIG\_UNAVAILABLE | Expected BMC/product configuration could not be loaded; no BMC comparison verdict is available. | Halt & escalate | L10 Test | BMC | BmcCheck, BmcCheckFanLocation, BmcCheckFanControl |
| TH-BMC-0002-S4Q9 | 390660098 | BMC\_INVENTORY\_QUERY\_FAILED | The BMC inventory or management query command failed. | Halt & escalate | L10 Test | BMC | BmcCheck |
| TH-BMC-0003-S4Q9 | 390660099 | BMC\_INVENTORY\_OUTPUT\_INVALID | BMC inventory output was incomplete or could not be parsed. | Halt & escalate | L10 Test | BMC | BmcCheck |
| TH-BMC-0004-S2Q9 | 455671812 | BMC\_IDENTITY\_MISMATCH | BMC-reported platform vendor, product, or model identity does not match expected configuration. | Halt & escalate | L10 Test | BMC | BmcCheck |
| TH-BMC-0005-S2Q9 | 455671813 | BMC\_MANAGEMENT\_ADDRESS\_MISMATCH | The BMC management IP address or MAC address does not match the expected server configuration. | Halt & escalate | L10 Test | BMC | BmcCheck |
| TH-BMC-0006-S5Q9 | 358154246 | BMC\_FIRMWARE\_VERSION\_MISMATCH | The running BMC firmware version does not match the expected L10 release. | Halt & escalate | L10 Test | BMC | BmcCheck |
| TH-BMC-0007-S4Q9 | 390660103 | BMC\_FAN\_LOCATION\_PROGRAM\_FAILED | The BMC command to program fan locations failed. | Halt & escalate | L10 Test | BMC | BmcCheckFanLocation |
| TH-BMC-0008-S4Q9 | 390660104 | BMC\_FAN\_LOCATION\_READBACK\_FAILED | Programmed fan-location data could not be read back from the BMC. | Halt & escalate | L10 Test | BMC | BmcCheckFanLocation |
| TH-BMC-0009-S5Q9 | 358154249 | BMC\_FAN\_CONFIG\_UNAVAILABLE | BMC fan-zone, PWM, or sensor configuration needed by the fan-control test is missing or invalid. | Halt & escalate | L10 Test | BMC | BmcCheckFanControl |
| TH-BMC-0010-S4Q9 | 390660106 | BMC\_SENSOR\_QUERY\_FAILED | The BMC sensor query failed or returned no usable fan/thermal readings. | Halt & escalate | L10 Test | BMC | BmcCheckFanControl |
| TH-BMC-0011-S4Q6 | 289800203 | BMC\_CONNECTIVITY\_FAILED | BMC connectivity validation observed packet loss or could not complete the configured reachability check. | Retry | L10 Test | BMC | BmcConnectivityCheck |
| TH-BMC-0012-S4Q9 | 289996812 | BMC\_SSH\_UNAVAILABLE | An SSH session to the BMC could not be established for the requested operation. | Halt & escalate | L10 Test | BMC | SohuServerBmcFirmwareUpdate, SohuServerBiosUpdate, PsuFirmwareUpdate, CpldFirmwareUpdate, L10VBBUpdate, BmcPowerCycle |
| TH-BMC-0013-S4Q9 | 390660109 | BMC\_UPDATE\_IMAGE\_STAGING\_FAILED | The firmware image or update configuration could not be staged to the BMC. | Halt & escalate | L10 Test | BMC | SohuServerBmcFirmwareUpdate, SohuServerBiosUpdate, PsuFirmwareUpdate, CpldFirmwareUpdate, L10VBBUpdate |
| TH-BMC-0014-S4Q9 | 357105678 | BMC\_FIRMWARE\_UPDATE\_COMMAND\_FAILED | The BMC firmware update command failed or did not complete successfully. | Halt & escalate | L10 Test | BMC | SohuServerBmcFirmwareUpdate |
| TH-BMC-0015-S4Q9 | 357105679 | BMC\_POST\_UPDATE\_VERIFY\_FAILED | The BMC did not report the requested firmware version after update. | Halt & escalate | L10 Test | BMC | SohuServerBmcFirmwareUpdate |
| TH-BMC-0016-S4Q9 | 357105680 | BMC\_POWER\_CYCLE\_INTERVAL\_SET\_FAILED | The requested BMC power-cycle interval could not be configured. | Halt & escalate | L10 Test | BMC | SetPowerCycleInterval |
| TH-BMC-0017-S4Q9 | 390660113 | BMC\_SYSTEM\_EVENT\_LOG\_QUERY\_FAILED | The BMC system-event log could not be read or parsed. | Halt & escalate | L10 Test | BMC | StoreSystemLogStates, CheckSystemLogStates |
| TH-BMC-0018-S4Q9 | 373882898 | BMC\_CRITICAL\_EVENT\_DETECTED | A new critical BMC/SEL event was detected between the stored baseline and the post-test log state. | Halt & escalate | L10 Test | BMC | CheckSystemLogStates |
| TH-BMC-0019-S4Q9 | 390660115 | BMC\_RAW\_COMMAND\_FAILED | A required low-level BMC raw command failed or returned no response. | Halt & escalate | L10 Test | BMC | BmcCheck, BmcCheckFanLocation, BmcCheckFanControl |
| TH-BMC-0020-S5Q9 | 358154260 | BMC\_UPDATE\_MODEL\_CONFIG\_UNAVAILABLE | The BMC update flow could not resolve the server model or target-specific update configuration. | Halt & escalate | L10 Test | BMC | SohuServerBmcFirmwareUpdate, SohuServerBiosUpdate, PsuFirmwareUpdate, CpldFirmwareUpdate, L10VBBUpdate |
| TH-BIOS-0001-S5Q9 | 358154241 | BIOS\_EXPECTED\_CONFIG\_UNAVAILABLE | Expected BIOS version or boot-order configuration could not be loaded; no BIOS verdict is available. | Halt & escalate | L10 Test | BIOS | CheckBiosVersion, CheckBiosBootOrder |
| TH-BIOS-0002-S4Q9 | 390660098 | BIOS\_VERSION\_QUERY\_FAILED | The running BIOS version could not be queried. | Halt & escalate | L10 Test | BIOS | CheckBiosVersion |
| TH-BIOS-0003-S4Q9 | 390660099 | BIOS\_VERSION\_OUTPUT\_INVALID | BIOS version output was empty, incomplete, or could not be parsed. | Halt & escalate | L10 Test | BIOS | CheckBiosVersion |
| TH-BIOS-0004-S5Q9 | 358154244 | BIOS\_VERSION\_MISMATCH | The running BIOS version does not match the expected L10 release. | Halt & escalate | L10 Test | BIOS | CheckBiosVersion |
| TH-BIOS-0005-S4Q9 | 390660101 | BIOS\_BOOT\_ORDER\_QUERY\_FAILED | The configured BIOS boot order could not be queried. | Halt & escalate | L10 Test | BIOS | CheckBiosBootOrder |
| TH-BIOS-0006-S5Q9 | 358154246 | BIOS\_BOOT\_ORDER\_MISMATCH | The BIOS boot order does not match the required L10 configuration. | Halt & escalate | L10 Test | BIOS | CheckBiosBootOrder |
| TH-BIOS-0007-S4Q9 | 357105671 | BIOS\_UPDATE\_FAILED | The server BIOS update command failed or did not complete successfully. | Halt & escalate | L10 Test | BIOS | SohuServerBiosUpdate |
| TH-BIOS-0008-S4Q9 | 357105672 | BIOS\_POST\_UPDATE\_VERIFY\_FAILED | The BIOS did not report the requested version after update and reboot. | Halt & escalate | L10 Test | BIOS | SohuServerBiosUpdate |
| TH-PWR-0007-S2Q9 | 371785735 | UNEXPECTED\_DVFS\_RAMPDOWN | Unexpected DVFS rampdown event during workload | Halt & escalate | L10 Test | PWR | SohuPowerVirusMultiChipTestCase |
| TH-PWR-0009-S4Q9 | 390660105 | BMC\_POWER\_CYCLE\_COMMAND\_FAILED | The BMC power-cycle command returned a failure. | Halt & escalate | L10 Test | Power | BmcPowerCycle |
| TH-PWR-0010-S2Q9 | 371785738 | HOST\_DID\_NOT\_POWER\_OFF | The host remained reachable after the BMC power-off step and did not enter the expected off state. | Halt & escalate | L10 Test | Power | BmcPowerCycle |
| TH-PWR-0011-S2Q9 | 371785739 | HOST\_DID\_NOT\_RECOVER\_AFTER\_POWER\_CYCLE | The host did not become reachable within the configured interval after BMC power-on. | Halt & escalate | L10 Test | Power | BmcPowerCycle |
| TH-PWR-0012-S4Q9 | 390660108 | HOST\_REBOOT\_COMMAND\_FAILED | The host reboot request failed before the reboot transition could be observed. | Halt & escalate | L10 Test | Power | SohuHostRebootTestCase |
| TH-PWR-0013-S4Q9 | 373882893 | HOST\_REBOOT\_NOT\_OBSERVED | The host never became unreachable after the reboot request, so the expected reboot transition was not observed. | Halt & escalate | L10 Test | Power | SohuHostRebootTestCase |
| TH-PWR-0014-S2Q9 | 371785742 | HOST\_DID\_NOT\_RECOVER\_AFTER\_REBOOT | The host did not return to a reachable and usable state within the configured reboot recovery interval. | Halt & escalate | L10 Test | Power | SohuHostRebootTestCase |
| TH-THM-0001-S2Q6 | 371589121 | THERMAL\_DIODE\_READING\_INVALID | Thermal diode temperature reading out of the qualified range, reported invalid by the sensor, or an uncalibrated mezzanine diode reading below 0 C. | Retry | L10 Test | THM | SohuDtsMultiChipTestCase |
| TH-THM-0002-S2Q6 | 371589122 | DTS\_SPREAD\_EXCEEDED | The peak-to-peak spread across usable Sohu DTS readings exceeded the configured deviation limit. | Retry | L10 Test | THM | SohuDtsMultiChipTestCase |
| TH-THM-0004-S2Q6 | 371589124 | CATASTROPHIC\_THERMAL\_TRIP | Catastrophic trip event during stress workload | Retry | L10 Test | THM | SohuPowerVirusMultiChipTestCase |
| TH-THM-0005-S4Q9 | 373882885 | DTS\_DEVIATION\_UNDER\_STRESS | DTS peak-to-peak deviation under power virus out of bounds | Halt & escalate | L10 Test | THM | SohuPowerVirusMultiChipTestCase |
| TH-THM-0006-S2Q9 | 371785734 | PEAK\_DTS\_TEMPERATURE\_EXCEEDED | Peak DTS temperature under power virus exceeds expected maximum | Halt & escalate | L10 Test | THM | SohuPowerVirusMultiChipTestCase |
| TH-THM-0008-S4Q9 | 357105672 | FAN\_LOCATION\_MISMATCH | Fan location identifiers read back from the BMC do not match the configured physical fan positions. | Halt & escalate | L10 Test | Fan | BmcCheckFanLocation |
| TH-THM-0009-S4Q9 | 373882889 | FAN\_PWM\_SET\_FAILED | The requested fan PWM value could not be applied through the BMC control interface. | Halt & escalate | L10 Test | Fan | BmcCheckFanControl |
| TH-THM-0010-S2Q9 | 371785738 | FAN\_RPM\_RESPONSE\_OUT\_OF\_RANGE | A fan RPM reading is outside the expected range or does not increase as required after a PWM change. | Halt & escalate | L10 Test | Fan | BmcCheckFanControl |
| TH-THM-0011-S4Q9 | 373882891 | FAN\_AUTOMATIC\_MODE\_RESTORE\_FAILED | Fan control could not be returned to automatic mode after the manual fan test. | Halt & escalate | L10 Test | Fan | BmcCheckFanControl |
| TH-FW-0001-S2Q9 | 355008513 | SOHU\_FIRMWARE\_UPDATE\_FAILED | Sohu app firmware update failed or ASIC not pingable after update | Halt & escalate | L10 Test | FW | MultiChipSohuHotReloadFirmwareUpdateTestCase |
| TH-FW-0002-S4Q9 | 357105666 | SOHU\_FIRMWARE\_HASH\_MISMATCH | The ASIC booted application firmware after the update, but the running image hash does not match the hash in the image package that was just staged. | Halt & escalate | L10 Test | FW | MultiChipSohuHotReloadFirmwareUpdateTestCase |
| TH-FW-0005-S5Q2 | 357695493 | FIXTURE\_FIRMWARE\_UPDATE\_FAILED | Fixture firmware update failed (golden VBB / retimer): OpenOCD flash, ST-Link adapter, post-flash UART/RPC ready check, or application firmware-hash verification did not succeed. | Warm Reboot | L10 Test | FW | L10VBBUpdate |
| TH-FW-0006-S5Q9 | 358154246 | DVFS\_PROFILE\_APPLY\_FAILED | Board DVFS profile detection or application failed | Halt & escalate | L10 Test | FW | SohuSetClockProfileMultiChipTestCase |
| TH-FW-0009-S5Q9 | 358154249 | SOHU\_HOT\_RELOAD\_INELIGIBLE | Hot reload could not start, so no firmware was written | Halt & escalate | L10 Test | FW | MultiChipSohuHotReloadFirmwareUpdateTestCase |
| TH-FW-0010-S5Q9 | 358154250 | EXPECTED\_VERSION\_CONFIG\_UNAVAILABLE | Expected host or component version data could not be loaded; no version verdict is available. | Halt & escalate | L10 Test | Firmware | CheckOs, CheckKernelVersion, CheckSohuFwVersion, CheckPsuFirmwareVersion, CheckCpldBpFirmwareVersion |
| TH-FW-0011-S4Q9 | 390660107 | HOST\_OS\_VERSION\_QUERY\_FAILED | The host operating-system release could not be queried. | Halt & escalate | L10 Test | Host OS | CheckOs |
| TH-FW-0012-S4Q9 | 390660108 | HOST\_OS\_VERSION\_OUTPUT\_INVALID | Operating-system release output was incomplete or could not be parsed. | Halt & escalate | L10 Test | Host OS | CheckOs |
| TH-FW-0013-S5Q9 | 358154253 | HOST\_OS\_VERSION\_MISMATCH | The host operating-system release does not match the required L10 image. | Halt & escalate | L10 Test | Host OS | CheckOs |
| TH-FW-0014-S4Q9 | 390660110 | HOST\_KERNEL\_VERSION\_QUERY\_FAILED | The running host kernel version could not be queried. | Halt & escalate | L10 Test | Host Kernel | CheckKernelVersion |
| TH-FW-0015-S4Q9 | 390660111 | HOST\_KERNEL\_VERSION\_OUTPUT\_INVALID | Kernel version output was empty or could not be parsed. | Halt & escalate | L10 Test | Host Kernel | CheckKernelVersion |
| TH-FW-0016-S5Q9 | 358154256 | HOST\_KERNEL\_VERSION\_MISMATCH | The running host kernel does not match the required L10 release. | Halt & escalate | L10 Test | Host Kernel | CheckKernelVersion |
| TH-FW-0017-S4Q9 | 390660113 | SOHU\_FIRMWARE\_VERSION\_QUERY\_FAILED | The running Sohu firmware version could not be queried. | Halt & escalate | L10 Test | Sohu Firmware | CheckSohuFwVersion |
| TH-FW-0018-S5Q9 | 358154258 | SOHU\_FIRMWARE\_VERSION\_MISMATCH | The running Sohu firmware version does not match the required L10 release. | Halt & escalate | L10 Test | Sohu Firmware | CheckSohuFwVersion |
| TH-FW-0019-S4Q9 | 390660115 | PSU\_FIRMWARE\_VERSION\_QUERY\_FAILED | One or more PSU firmware versions could not be queried. | Halt & escalate | L10 Test | PSU Firmware | CheckPsuFirmwareVersion |
| TH-FW-0020-S5Q9 | 358154260 | PSU\_FIRMWARE\_VERSION\_MISMATCH | A PSU firmware version does not match the required L10 release. | Halt & escalate | L10 Test | PSU Firmware | CheckPsuFirmwareVersion |
| TH-FW-0021-S4Q9 | 390660117 | CPLD\_BP\_FIRMWARE\_VERSION\_QUERY\_FAILED | The backplane/CPLD firmware version could not be queried. | Halt & escalate | L10 Test | CPLD Firmware | CheckCpldBpFirmwareVersion |
| TH-FW-0022-S5Q9 | 358154262 | CPLD\_BP\_FIRMWARE\_VERSION\_MISMATCH | The backplane/CPLD firmware version does not match the required L10 release. | Halt & escalate | L10 Test | CPLD Firmware | CheckCpldBpFirmwareVersion |
| TH-FW-0023-S4Q9 | 357105687 | PSU\_FIRMWARE\_UPDATE\_FAILED | The PSU firmware update command failed or did not complete successfully. | Halt & escalate | L10 Test | PSU Firmware | PsuFirmwareUpdate |
| TH-FW-0024-S4Q9 | 357105688 | PSU\_POST\_UPDATE\_VERIFY\_FAILED | A PSU did not report the requested firmware version after update. | Halt & escalate | L10 Test | PSU Firmware | PsuFirmwareUpdate |
| TH-FW-0025-S4Q9 | 357105689 | CPLD\_FIRMWARE\_UPDATE\_FAILED | The CPLD/backplane firmware update command failed or did not complete successfully. | Halt & escalate | L10 Test | CPLD Firmware | CpldFirmwareUpdate |
| TH-FW-0026-S4Q9 | 357105690 | CPLD\_POST\_UPDATE\_VERIFY\_FAILED | The CPLD/backplane did not report the requested firmware version after update. | Halt & escalate | L10 Test | CPLD Firmware | CpldFirmwareUpdate |
| TH-FW-0027-S4Q9 | 357105691 | SOFTWARE\_PROVISIONING\_FAILED | The L10 host software provisioning workflow failed to apply the required software state. | Halt & escalate | L10 Test | Host Software | SoftwareProvisioning |
| TH-FW-0028-S4Q9 | 390660124 | LINUX\_PACKAGE\_INSTALL\_FAILED | A required Linux package could not be installed or configured. | Halt & escalate | L10 Test | Host Software | InstallLinuxPackagesTestCase |
| TH-FW-0029-S4Q9 | 357105693 | SOHU\_BOOTLOADER\_UPDATE\_FAILED | The Sohu bootloader update command failed or the device was not usable after programming. | Halt & escalate | L10 Test | Sohu Bootloader | UpdateSohuBootloader |
| TH-FW-0030-S4Q9 | 357105694 | SOHU\_BOOTLOADER\_POST\_UPDATE\_VERIFY\_FAILED | The running Sohu bootloader does not match the requested image after update. | Halt & escalate | L10 Test | Sohu Bootloader | UpdateSohuBootloader |
| TH-FW-0031-S4Q9 | 390660127 | HOST\_SYSTEM\_LOG\_CRITICAL\_EVENT\_DETECTED | A new critical host kernel, service, or system event was detected after the L10 workload. | Halt & escalate | L10 Test | Host Software | CheckSystemLogStates |
| TH-ENV-0001-S4Q9 | 289996801 | HOST\_OR\_BMC\_UNREACHABLE | The station host or its BMC did not answer ping or SSH after boot, so no module test could start. | Halt & escalate | L10 Test | ENV | SohuHostRebootTestCase, BmcPowerCycle, BmcConnectivityCheck |
| TH-ENV-0003-S4Q9 | 357105667 | PLX\_SWITCH\_DISCOVERY\_FAILED | PLX daemon reported no PEX switches | Halt & escalate | L10 Test | ENV | CheckPlxDaemonFirmwareVersion, UpdatePlxDaemonFirmwareVersion |
| TH-ENV-0004-S4Q9 | 357105668 | HOST\_DRIVER\_SETUP\_FAILED | A host driver/setup utility step failed: kernel module reload, PCIe teardown or bus rescan, sysfs parameter write, or log-reader activation returned non-zero. | Halt & escalate | L10 Test | ENV | SoftwareProvisioning, BroadcomUpdateFwAndConfigure |
| TH-ENV-0005-S4Q9 | 289996805 | MODEL\_REGISTRY\_MOUNT\_FAILED | The model-registry NFS share could not be mounted or validated on the L10 host. | Halt & escalate | L10 Test | Model Registry | ModelRegistryNfsMountTestCase |
| TH-ENV-0006-S5Q9 | 458817542 | MODEL\_ARTIFACT\_UNAVAILABLE | A required model-registry artifact or model path is missing or unreadable. | Halt & escalate | L10 Test | Model Registry | StageModelRegistryToShmTestCase, SohuMlpTp8TestCase, SohuLlama70bForwardIteratedTestCase, SohuLlama70bHp8ForwardIteratedTestCase, SohuLlamaTp8InferenceMaxTestCase, Llama8bFp8Tp1SmokeTestCase |
| TH-ENV-0007-S4Q9 | 424214535 | MODEL\_STAGE\_TO\_SHM\_FAILED | The required model artifact could not be copied or staged into shared memory. | Halt & escalate | L10 Test | Shared Memory | StageModelRegistryToShmTestCase |
| TH-ENV-0008-S4Q9 | 424214536 | MODEL\_SHM\_CLEANUP\_FAILED | The staged model could not be removed from shared memory during cleanup. | Halt & escalate | L10 Test | Shared Memory | FreeModelRegistryFromShmTestCase |
| TH-HAR-0001-S4Q0 | 390070273 | TEST\_TIMEOUT | The test exceeded its configured timeout and was terminated before producing a verdict (ABORTED disposition). | No act | L10 Test | Harness | any L10 test case (harness-level) |
| TH-HAR-0002-S5Q9 | 358154242 | TEST\_ARGS\_INVALID | A test case was invoked with invalid or unsupported arguments and rejected the run before touching the DUT. | Halt & escalate | L10 Test | Harness | CpuStress, MemoryStressNg, MemoryStress, IoStress, SohuSnapTestCase, ExecBinaryTestCase |
| TH-HAR-0003-S5Q9 | 358154243 | TEST\_DEPENDENCY\_UNAVAILABLE | Tool/binary/data file the test depends on is missing on the test system (test-system ERROR — excluded from module yield) | Halt & escalate | L10 Test | Harness | CpuStress, MemoryStressNg, MemoryStress, IoStress, LoopbackTopologyTest, NetworkBwRdmaTest, ModelRegistryNfsMountTestCase, StageModelRegistryToShmTestCase, SohuServerBmcFirmwareUpdate, SohuServerBiosUpdate, PsuFirmwareUpdate, CpldFirmwareUpdate, L10VBBUpdate, InstallLinuxPackagesTestCase, UpdatePlxDaemonFirmwareVersion, BroadcomUpdateFwAndConfigure, UpdateSohuBootloader, MultiChipSohuHotReloadFirmwareUpdateTestCase, ExecBinaryTestCase |
| TH-HAR-0004-S4Q9 | 357105668 | NESTED\_SUITE\_ORCHESTRATION\_FAILED | Nested suite failed to launch or complete orchestration (child test failures carry their own codes) | Halt & escalate | L10 Test | Harness | RunInStress |
| TH-HAR-0005-S4Q6 | 390463493 | TEST\_TOOL\_EXECUTION\_FAILED | A test-owned command or binary failed to execute and did not produce a domain-specific DUT verdict. | Retry | L10 Test | Harness | IoStress, ExecBinaryTestCase, CpldDiagnosticsRemoteTestCase |
| TH-HAR-0006-S4Q9 | 390660102 | TEST\_METRICS\_PARSE\_FAILED | A test tool completed without complete, parseable metrics needed to determine the result. | Halt & escalate | L10 Test | Harness | IoStress, ExecBinaryTestCase |
| TH-HAR-0007-S4Q9 | 390660103 | TEST\_OUTPUT\_UNAVAILABLE | Expected test output, state, or result artifacts were not produced. | Halt & escalate | L10 Test | Harness | StoreSystemLogStates, CheckSystemLogStates, ExecBinaryTestCase |
| TH-HAR-0008-S5Q9 | 358154248 | TEST\_PRECONDITION\_NOT\_MET | A required test precondition was not satisfied, so the test did not exercise the DUT as intended. | Halt & escalate | L10 Test | Harness | RunInStress, IoStress, NetworkBwRdmaTest |
| TH-HAR-0009-S4Q9 | 390660105 | TEST\_CLEANUP\_FAILED | Test cleanup failed and may have left processes, mounts, namespaces, files, or device state behind. | Halt & escalate | L10 Test | Harness | LoopbackTopologyTest, NetworkBwRdmaTest, FreeModelRegistryFromShmTestCase |
| TH-HAR-0010-S4Q9 | 390660106 | SYSTEM\_LOG\_SNAPSHOT\_FAILED | The pre-test system-log baseline could not be captured. | Halt & escalate | L10 Test | Harness | StoreSystemLogStates |
| TH-HAR-0011-S4Q9 | 390660107 | SYSTEM\_LOG\_COMPARE\_FAILED | System-log state could not be queried, parsed, or compared with the stored baseline. | Halt & escalate | L10 Test | Harness | CheckSystemLogStates |
| TH-HAR-9998-S3Q0 | 271591182 | TEST\_FAILED\_UNCLASSIFIED | A test returned TestFailedError without a specific TH identity; this catch-all is a taxonomy-health failure and must be replaced by a specific code. | No act | L10 Test | Harness | any L10 test case (harness-level) |
| TH-HAR-9999-S3Q9 | 389621519 | UNHANDLED\_EXCEPTION | An unhandled exception escaped the test and was wrapped by the harness; the traceback is retained in the per-test log (ERROR disposition). | Halt & escalate | L10 Test | Harness | any L10 test case (harness-level) |
| TH-INFRA-0001-S4Q9 | 424214529 | RACKSIM\_UNAVAILABLE | The configured racksim service or simulated server endpoint is unavailable. | Halt & escalate | L10 Test | Test Infrastructure | RunInStress, ExecBinaryTestCase |
| TH-INFRA-0002-S4Q9 | 289996802 | REMOTE\_EXECUTION\_TRANSPORT\_FAILED | The infrastructure transport used to execute a remote L10 operation failed before a DUT verdict was obtained. | Halt & escalate | L10 Test | Test Infrastructure | CpldDiagnosticsRemoteTestCase, ExecBinaryTestCase |
| TH-INFRA-0003-S4Q9 | 289996803 | INFRA\_NETWORK\_PATH\_UNAVAILABLE | A required station-side network path, route, or service endpoint is unavailable. | Halt & escalate | L10 Test | Test Infrastructure | ModelRegistryNfsMountTestCase, BmcConnectivityCheck |
| TH-INFRA-0004-S4Q9 | 424214532 | TEST\_RESOURCE\_EXHAUSTED | A station-side resource limit prevented the L10 test from running or completing. | Halt & escalate | L10 Test | Test Infrastructure | StageModelRegistryToShmTestCase, RunInStress |

|  |  |  |  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Error Code ID | Message | Quick\_Action | Recover\_Step | Source | Error\_Type | Component | Test\_Case | Possible Root cause | Bugs |
| EC-160402000001 | Runner date failed | Undefined | Fix runner shell / harness | L11 Test | Connection | Undefined | CheckSystemClockTestCase |  |  |
| EC-160406000002 | Runner epoch parse failed | Undefined | Fix runner clock output | L11 Test | Function | Undefined | CheckSystemClockTestCase |  |  |
| EC-160402060003 | RMS date over SSH failed | Undefined | Check RMS SSH / routing | L11 Test | Connection | RMS | CheckSystemClockTestCase |  |  |
| EC-160406060004 | RMS epoch parse failed | Undefined | Fix RMS clock output | L11 Test | Function | RMS | CheckSystemClockTestCase |  |  |
| EC-160404060005 | Clock skew over tolerance | Undefined | Fix NTP / time sync | L11 Test | Config | RMS | CheckSystemClockTestCase |  |  |
| EC-1604030b0006 | ZTP container start failed | Undefined | Check ZTP service on RMS | L11 Test | Provision | Mgmt switch | SwitchZtpTriggerTestCase |  |  |
| EC-1604030b0007 | ZTP container stop failed | Undefined | Inspect ZTP logs / daemon | L11 Test | Provision | Mgmt switch | SwitchZtpTriggerTestCase |  |  |
| EC-160406000008 | Need ≥2 ping targets | Undefined | Fix suite ping\_targets | L11 Test | Function | Undefined | PingAllP2pPairsTestCase |  |  |
| EC-160401000009 | Resource not SSH | Undefined | Fix resource config | L11 Test | Initial | Undefined | PingAllP2pPairsTestCase |  |  |
| EC-16040200000a | SSH resource missing | Undefined | Fix keys / inventory | L11 Test | Connection | Undefined | PingAllP2pPairsTestCase |  |  |
| EC-16040200000b | SSH resource open error | Undefined | Undefined connection / fix RM | L11 Test | Connection | Undefined | PingAllP2pPairsTestCase |  |  |
| EC-16040200000c | Ping mesh failure | Undefined | Fix L3 / bonds / switches | L11 Test | Connection | Undefined | PingAllP2pPairsTestCase |  |  |
| EC-16040106000d | Primary RMS provision: no ssh\_target | Undefined | Set ssh\_target in suite | L11 Test | Initial | RMS | ProvisionPrimaryRms |  |  |
| EC-16040406000e | Vault / inputs validation failed | Undefined | Fix l11\_inputs / vault file | L11 Test | Config | RMS | ProvisionPrimaryRms |  |  |
| EC-16040406000f | No provisioning images found | Undefined | Restore deploy image tarball | L11 Test | Config | RMS | ProvisionPrimaryRms |  |  |
| EC-160403060010 | Ansible playbook failed | Undefined | Read ansible artifacts / logs | L11 Test | Provision | RMS | ProvisionPrimaryRms |  |  |
| EC-160403060011 | Image import to RMS failed | Undefined | Check microk8s / disk on RMS | L11 Test | Provision | RMS | ProvisionPrimaryRms |  |  |
| EC-160403060012 | Cleanup of images failed | Undefined | SSH / permissions on RMS | L11 Test | Provision | RMS | ProvisionPrimaryRms |  |  |
| EC-160402060013 | MTS apt proxy unreachable locally | Undefined | Start / fix apt proxy | L11 Test | Connection | RMS | ProvisionPrimaryRms |  |  |
| EC-160402060014 | RMS cannot reach apt proxy | Undefined | Routing / firewall to proxy | L11 Test | Connection | RMS | ProvisionPrimaryRms |  |  |
| EC-160401060015 | Provision CDU/PDU/compute/RMS2: no ssh | Undefined | Set ssh\_target | L11 Test | Initial | RMS | ProvisionCdu, ProvisionPdu, ProvisionComputeServer, ProvisionRedundantRms |  |  |
| EC-160404060016 | Unknown rack entity | Undefined | Fix rack\_entities / IDs | L11 Test | Config | RMS | ProvisionCdu, ProvisionPdu |  |  |
| EC-160404050017 | CDU interface / entity mismatch | Undefined | Fix CDU hostname in registry | L11 Test | Config | CDU | ProvisionCdu |  |  |
| EC-160402050018 | CDU unreachable (ping) | Undefined | CDU network / power | L11 Test | Connection | CDU | ProvisionCdu |  |  |
| EC-160402040019 | PDU unreachable (ping) | Undefined | PDU network / power | L11 Test | Connection | PDU | ProvisionPdu |  |  |
| EC-16040306001a | Rack-controller provisioning task failed | Undefined | RC logs / rack controller | L11 Test | Provision | RMS | ProvisionCdu, ProvisionPdu, ProvisionRedundantRms |  |  |
| EC-16060505001b | CDU post-provision health bad | Undefined | CDU telemetry / RC state | L11 Test | Function | CDU | ProvisionCdu |  |  |
| EC-16060504001c | PDU post-provision health bad | Undefined | PDU telemetry / RC state | L11 Test | Function | PDU | ProvisionPdu |  |  |
| EC-16040302001d | Compute server provisioning failed | Undefined | RC provision logs | L11 Test | Provision | CPU | ProvisionComputeServer |  |  |
| EC-16040406001e | Redundant RMS vault/data error | Undefined | Fix vault inputs | L11 Test | Config | RMS | ProvisionRedundantRms |  |  |
| EC-16040106001f | CDU/PDU health: no ssh\_target | Undefined | Set suite ssh\_target | L11 Test | Initial | RMS | CduHealthCheckTestCase, PduHealthCheckTestCase |  |  |
| EC-160404060020 | RMS SSH resource wrong type | Undefined | Fix resource YAML | L11 Test | Config | RMS | CduHealthCheckTestCase, PduHealthCheckTestCase |  |  |
| EC-160404060021 | Rack controller port missing | Undefined | Add RC port to resources | L11 Test | Config | RMS | CduHealthCheckTestCase, PduHealthCheckTestCase |  |  |
| EC-160404050022 | CDU resource not CduConnection | Undefined | Fix CDU resource entry | L11 Test | Config | CDU | CduHealthCheckTestCase, CduInventoryCheckTestCase |  |  |
| EC-160404040023 | PDU resource not PduConnection | Undefined | Fix PDU resource entry | L11 Test | Config | PDU | PduHealthCheckTestCase, PduInventoryCheckTestCase |  |  |
| EC-160605050024 | CDU health aggregate failure | Undefined | See per-line daemon logs | L11 Test | Function | CDU | CduHealthCheckTestCase |  |  |
| EC-160605040025 | PDU health aggregate failure | Undefined | See per-line daemon logs | L11 Test | Function | PDU | PduHealthCheckTestCase |  |  |
| EC-160404060028 | RMS BOM missing | Undefined | Fix BOM YAML | L11 Test | Config | RMS | RmsInventoryCheckTestCase |  |  |
| EC-160404060029 | RMS inventory mismatch | Undefined | Replace HW / fix BOM | L11 Test | Config | RMS | RmsInventoryCheckTestCase |  |  |
| EC-1604020a002a | Switch eAPI curl failed | Undefined | Fix switch mgmt / creds | L11 Test | Connection | ToR Switch | SwitchInventoryCheckTestCase, MgmtSwitchRedundancyTestCase |  |  |
| EC-1604040a002b | Switch BOM mismatch | Undefined | Replace switch / BOM | L11 Test | Config | ToR Switch | SwitchInventoryCheckTestCase |  |  |
| EC-16040405002c | No CDU in BOM | Undefined | Fix BOM | L11 Test | Config | CDU | CduInventoryCheckTestCase |  |  |
| EC-16060505002d | CDU inventory mismatch | Undefined | Fix CDU vs BOM | L11 Test | Function | CDU | CduInventoryCheckTestCase |  |  |
| EC-16040404002e | No PDU in BOM | Undefined | Fix BOM | L11 Test | Config | PDU | PduInventoryCheckTestCase |  |  |
| EC-16060504002f | PDU inventory mismatch | Undefined | Fix PDU vs BOM | L11 Test | Function | PDU | PduInventoryCheckTestCase |  |  |
| EC-160401070030 | BMC power-cycle wrapper: no ssh\_target | Undefined | Point ssh at RMS | L11 Test | Initial | BMC | SohuServerBmcPowerCycle |  |  |
| EC-160607070031 | BMC power-cycle sequence failed | Undefined | BMC / bmc-daemon logs | L11 Test | Function | BMC | SohuServerBmcPowerCycle |  |  |
| EC-160402020032 | Host SSH not up after power-on | Undefined | OS / network / sshd | L11 Test | Connection | CPU | SohuServerBmcPowerCycle |  |  |
| EC-160401070033 | Firmware check: no ssh\_target | Undefined | Point ssh at RMS | L11 Test | Initial | BMC | SohuServerFirmwareInventoryCheck |  |  |
| EC-160404070034 | Firmware version mismatch | Undefined | Update BMC/BIOS/PSU FW | L11 Test | Config | BMC | SohuServerFirmwareInventoryCheck |  |  |
| EC-160404020035 | Per-server BOM scope: missing server\_id | Undefined | Pass server\_id in suite | L11 Test | Config | CPU | \_SohuServerScopedBomMixin |  |  |
| EC-1604040b0036 | Mgmt switch ID not in registry | Undefined | Fix rack\_entities.txtpb | L11 Test | Config | Mgmt switch | MgmtSwitchRedundancyTestCase |  |  |
| EC-1604040b0037 | Mgmt switch lacks pdu\_connections | Undefined | Fix PDU outlet mapping | L11 Test | Config | Mgmt switch | MgmtSwitchRedundancyTestCase |  |  |
| EC-1604040b0038 | Cannot resolve mgmt switch peer | Undefined | Expect two mgmt switches | L11 Test | Config | Mgmt switch | MgmtSwitchRedundancyTestCase |  |  |
| EC-160404040039 | PDU resource invalid for redundancy test | Undefined | Fix pdu\_target resource | L11 Test | Config | PDU | MgmtSwitchRedundancyTestCase |  |  |
| EC-16060b0b003a | Mgmt switch redundancy failed (aggregate) | Undefined | See enumerated sub-failures | L11 Test | Function | Mgmt switch | MgmtSwitchRedundancyTestCase |  |  |
| EC-1604040a003b | No ToR switches in registry | Undefined | Fix registry accessors | L11 Test | Config | ToR Switch | TorSwitchRedundancyTestCase |  |  |
| EC-1604040a003c | ToR switch ID not in registry | Undefined | Fix rack\_entities.txtpb | L11 Test | Config | ToR Switch | TorSwitchRedundancyTestCase |  |  |
| EC-1604040a003d | ToR switch lacks pdu\_connections | Undefined | Fix PDU outlet mapping | L11 Test | Config | ToR Switch | TorSwitchRedundancyTestCase |  |  |
| EC-16040404003e | PDU resource invalid for ToR test | Undefined | Fix pdu\_target resource | L11 Test | Config | PDU | TorSwitchRedundancyTestCase |  |  |
| EC-16060a0a003f | ToR redundancy failed (aggregate) | Undefined | See enumerated sub-failures | L11 Test | Function | ToR Switch | TorSwitchRedundancyTestCase |  |  |

|  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Field | Describe |  |  |  |  |  |
| Error Code ID | The key ID of Error code |  |  |  |  |  |
| Message | The possible error message |  |  |  |  |  |
| Quick\_Action | How does the user or operate handle this issues immediately |  |  |  |  |  |
| Recover\_Step | Detail recover steps for this error |  |  |  |  |  |
| Source | Error from which test or software |  |  |  |  |  |
| Error\_Type | Error types |  |  |  |  |  |
| Component | Relative components |  |  |  |  |  |
| Test\_Case | Jira IDs of test cases, allow multiple IDs, separate by “,” |  |  |  |  |  |
| Bugs | Jira IDs of bugs, allow multiple IDs, separate by “,” |  |  |  |  |  |
| Count | Count of happen |  |  |  |  |  |
| Last\_happen | Datetime of last happen |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| Error ID |  |  |  |  |  |  |
| Char \# | 0 | 1 | 2\~3 | 4\~5 | 6\~7 | 8\~11 |
| Describe | Priority | Quick action | Source | Error Type | Component | Serial number |
| Define | 0\~2: Priority 0\~2  3\~F: Reserve | 0: No act 1: Cold Reboot 2: Warm Reboot 3: Soft power off  4: Hard shutdown  5: Disable component  6: Undefined 7: Hot remove 8: Hot switch  9\~F: Reserve | FF: Forward from out of Etched  00: MTS 01: SLT 02: 1X Test 03: L10 Test 04: L11 Test 05: Kayak 06: RMS 07: PDU Daemon 08: CDU Daemon  09: BMC 0A: BIOS  0B\~FE reserve | 00: Undefine 01: Initial 02: Connection 03: Provision 04: Config (HW/SW/FW) 05: Unit Test 06: Function 07: Stress 08: Sensors  0A\~FF: reserve | 00: Undfine 01: Soho chip 02: CPU 03: DIMM 04: PDU 05: CDU 06: RMS 07: BMC 08: BIOS 09: Storage 0A: ToR Switch  0B: Manage switch 0C: Temp 0D: Fan 0E: PSU 0F\~0xFF: reserve | The serial number of error code  From 0000\~FFFF |

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
|  | DRI 1 | DRI 2 | comment | PR |
| BootloaderResultTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/23002 |
| C2cIntegrityTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/22810 |
| C2cLaneMarginTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/22813 |
| C2cLinkupTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/22808 |
| C2cPrbsLoopbackTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/23117 |
| C2cThroughputTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/22812 |
| CheckFirmwareVersionTestCase | Mykola Servetnyk | Ulysses Kao |  | https://github.com/etched-ai/sw/pull/24591 |
| CheckPexFirmwareVersionTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/23116  |
| CheckPsuHealth | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/23963 |
| ChromaTelemetryCheckTestCase | Aidan Holm | Ulysses Kao |  |  |
| CpldDiagnosticsTestCase | Mykola Servetnyk | Ulysses Kao |  | https://github.com/etched-ai/sw/pull/24594 |
| DetectBoardDvfsProfileTestCase | Mykola Servetnyk | Ulysses Kao | merged | https://github.com/etched-ai/sw/pull/23003 |
| EvalBoardPowerTestCase | Aidan Holm | Jack Chou |  |  |
| KayakTestCase | Aidan Holm | Jack Chou |  |  |
| KvFlushAndAttentionInterleavedSingleChipTestCase | Aidan Holm | Jack Chou |  |  |
| KvFlushAndAttentionSingleChipTestCase | Aidan Holm | Jack Chou |  |  |
| LogReaderCaptureTestCase | Aidan Holm | Jack Chou |  |  |
| MezzanineI2cAlertsTestCase | Aidan Holm | Jack Chou |  |  |
| PcieSetupTestCase | Aidan Holm | Jack Chou |  |  |
| PcieTeardownTestCase | Aidan Holm | Jack Chou |  |  |
| ProgramSecureBootloaderTestCase | Aidan Holm | Jack Chou |  |  |
| PublishBootloaderTypeTestCase | Aidan Holm | Jack Chou |  |  |
| ReloadKernelModuleTestCase | Aidan Holm | Jack Chou |  |  |
| RetimerFirmwareUpdateTestCase | Aidan Holm | Jack Chou |  |  |
| RunAllAttnHbmBypassTestsSingleChipTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22847 |
| RunAllAttnTestsSingleChipTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22838 |
| RunKvFlushTestsSingleChipTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22839 |
| SaSortRampupHbmSingleChipTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22840 |
| SetSkipFlrOnOpenCloseTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22846 |
| SohuBusConnectivityTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22841 |
| SohuChipIdTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22842 |
| SohuCtsTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22843 |
| SohuDmaTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22811 |
| SohuDtsTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22844 |
| SohuEfuseTestCase | Sam Jiang | James Chou | In review | https://github.com/etched-ai/sw/pull/22845 |
| SohuFirmwareUpdateTestCase | Mykola Servetnyk | James Chou | merged | https://github.com/etched-ai/sw/pull/22816/ , https://github.com/etched-ai/sw/pull/22817 |
| SohuFlrTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22807 |
| SohuGpioTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22801 |
| SohuHbmBandwidthTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22819 |
| SohuHbmDeviceIdTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22805 |
| SohuHotReloadFirmwareUpdateTestCase | James Chou | Aidan Holm |  | https://github.com/etched-ai/sw/pull/22820 |
| SohuI2cTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22800 |
| SohuJtagTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22802 |
| SohuLaneRepairTestCase | James Chou | Aidan Holm |  | https://github.com/etched-ai/sw/pull/22806 |
| SohuLlama8bFp8ForwardTestCase | Aidan Holm | James Chou |  |  |
| SohuLlama8bFp8PrefillTestCase | Aidan Holm | James Chou |  |  |
| SohuLlamaMttTestCase | James Chou | Aidan Holm |  | https://github.com/etched-ai/sw/pull/22827 |
| SohuLogReaderActivateTestCase | James Chou | Aidan Holm | In review | https://github.com/etched-ai/sw/pull/22804 |
| SohuMtcStressTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22899 |
| SohuPcieAerCheckTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22892 |
| SohuPcieCsramThroughputTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22890 |
| SohuPcieLaneMarginTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22889 |
| SohuPcieRateChangeTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22893 |
| SohuPdTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22898 |
| SohuPmbistTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22891 |
| SohuPowerTelemetryTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22897 |
| SohuPowerVirusTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22895 |
| SohuPowerVirusThermalTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22894 |
| SohuRdqsSweepTrainingTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22888 |
| SohuSaScreeningTestCase | Jack Chou | Sam Jiang |  | https://github.com/etched-ai/sw/pull/22896 |
| SohuSauPllPhaseAlignmentTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22803 |
| SohuSecureBootRecoveryUpdateTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22809 |
| SohuSramMemoryTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22828 |
| SohuThermalDiodeTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22830 |
| SohuUartTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22851 |
| SohuVfioPingTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22853 |
| SohuVmTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22854 |
| SohuVrmTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22855 |
| SohuWeightLoadTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22856 |
| VbbFirmwareUpdateTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22858 |
| VfioProxyVersionTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22860 |
| ServerNestedTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22859 |
| SltModuleNestedTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22863 |
| SohuChipBinTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22865 |
| SohuSnapTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22866 |
| PcieRescanTestCase | Ulysses Kao | Mykola Servetnyk |  | https://github.com/etched-ai/sw/pull/22868 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | DRI Members |  |  |  |
|  | Mykola Servetnyk |  |  |  |
|  | Aidan Holm |  |  |  |
|  | Sam Jiang |  |  |  |
|  | James Chou |  |  |  |
|  | Jack Chou |  |  |  |
|  | Ulysses Kao |  |  |  |

|  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
| http://pega3:3000/suite\_run/mlt\_2026.209.0-git3fe4de25\_run\_764cdc97?slot\_number=1 |  |  |  |  |  |
|  |  |  |  |  |  |
| Test ID | Test Name | Status | Duration | Completed | Actions |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup | ServerNestedTestCase | Passed | 431s | Aug 1, 2026, 10:53:31 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_vbb\_dependent\_tests | ServerNestedTestCase | Failed | 170s | Aug 1, 2026, 10:56:31 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1 | SltModuleNestedTestCase | Passed | 674s | Aug 1, 2026, 11:07:49 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_cleanup | ServerNestedTestCase | Passed | 57s | Aug 1, 2026, 11:12:06 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_vfio\_proxy\_version | VfioProxyVersionTestCase | Passed | 0s | Aug 1, 2026, 10:47:30 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_power\_on\_eval\_board | EvalBoardPowerTestCase | Passed | 0s | Aug 1, 2026, 10:47:30 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_pcie\_teardown | PcieTeardownTestCase | Passed | 15s | Aug 1, 2026, 10:47:42 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_reload\_kernel\_module | ReloadKernelModuleTestCase | Passed | 4s | Aug 1, 2026, 10:47:48 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_set\_skip\_flr\_on\_open\_close | SetSkipFlrOnOpenCloseTestCase | Passed | 0s | Aug 1, 2026, 10:47:48 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_vbb\_firmware\_update | VbbFirmwareUpdateTestCase | Passed | 11s | Aug 1, 2026, 10:47:59 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_retimer\_firmware\_update | RetimerFirmwareUpdateTestCase | Passed | 25s | Aug 1, 2026, 10:48:25 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_log\_reader\_deactivate | SohuLogReaderActivateTestCase | Passed | 0s | Aug 1, 2026, 10:48:27 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_program\_secure\_bootloader | ProgramSecureBootloaderTestCase | Passed | 121s | Aug 1, 2026, 10:50:26 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_bootloader\_result\_chip1 | BootloaderResultTestCase | Passed | 0s | Aug 1, 2026, 10:50:26 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_secure\_boot\_recovery\_chip1 | SohuSecureBootRecoveryUpdateTestCase | Passed | 25s | Aug 1, 2026, 10:50:53 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_log\_reader\_activate | SohuLogReaderActivateTestCase | Passed | 0s | Aug 1, 2026, 10:51:46 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_thermal\_diode\_chip1 | SohuThermalDiodeTestCase | Passed | 0s | Aug 1, 2026, 10:51:46 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_vrm\_chip1 | SohuVrmTestCase | Passed | 0s | Aug 1, 2026, 10:51:46 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_mezzanine\_i2c\_alerts\_chip1 | MezzanineI2cAlertsTestCase | Passed | 1s | Aug 1, 2026, 10:51:46 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_pcie\_setup | PcieSetupTestCase | Passed | 76s | Aug 1, 2026, 10:53:06 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_setup\_check\_pex\_firmware\_version | CheckPexFirmwareVersionTestCase | Passed | 24s | Aug 1, 2026, 10:53:29 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_vbb\_dependent\_tests\_i2c\_chip1 | SohuI2cTestCase | Passed | 7s | Aug 1, 2026, 10:54:35 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_vbb\_dependent\_tests\_vm\_chip1 | SohuVmTestCase | Passed | 9s | Aug 1, 2026, 10:54:52 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_hot\_reload\_firmware\_update | SohuHotReloadFirmwareUpdateTestCase | Passed | 13s | Aug 1, 2026, 10:57:42 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_vfio\_ping\_boot | SohuVfioPingTestCase | Passed | 0s | Aug 1, 2026, 10:57:42 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_chip\_id | SohuChipIdTestCase | Passed | 0s | Aug 1, 2026, 10:57:42 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_flr | SohuFlrTestCase | Passed | 1s | Aug 1, 2026, 10:57:46 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_check\_for\_application\_firmware\_after\_flr | CheckFirmwareVersionTestCase | Passed | 1s | Aug 1, 2026, 10:57:48 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_vfio\_ping\_application | SohuVfioPingTestCase | Passed | 1s | Aug 1, 2026, 10:57:48 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_detect\_board\_dvfs\_profile | DetectBoardDvfsProfileTestCase | Passed | 0s | Aug 1, 2026, 10:57:51 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_efuse\_test | SohuEfuseTestCase | Passed | 0s | Aug 1, 2026, 10:57:53 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_pd | SohuPdTestCase | Passed | 1s | Aug 1, 2026, 10:57:55 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_dts | SohuDtsTestCase | Passed | 0s | Aug 1, 2026, 10:57:57 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_sram\_memory | SohuSramMemoryTestCase | Passed | 2s | Aug 1, 2026, 10:57:59 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_gpio\_test | SohuGpioTestCase | Passed | 0s | Aug 1, 2026, 10:58:02 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_pcie\_lane\_margin | SohuPcieLaneMarginTestCase | Passed | 69s | Aug 1, 2026, 10:59:10 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_mac\_loopback\_linkup | C2cLinkupTestCase | Passed | 3s | Aug 1, 2026, 10:59:15 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_integrity\_mac\_loopback | C2cIntegrityTestCase | Passed | 8s | Aug 1, 2026, 10:59:25 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_linkup | C2cLinkupTestCase | Passed | 5s | Aug 1, 2026, 10:59:30 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_prbs | C2cPrbsLoopbackTestCase | Passed | 2s | Aug 1, 2026, 10:59:34 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_linkup\_2 | C2cLinkupTestCase | Passed | 5s | Aug 1, 2026, 10:59:40 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_integrity | C2cIntegrityTestCase | Passed | 8s | Aug 1, 2026, 10:59:51 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_socket\_dl\_loopback\_linkup | C2cLinkupTestCase | Skipped | 0s | — |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_integrity\_datalink\_loopback | C2cIntegrityTestCase | Skipped | 0s | — |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_linkup\_before\_throughput | C2cLinkupTestCase | Passed | 5s | Aug 1, 2026, 10:59:55 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_c2c\_throughput | C2cThroughputTestCase | Passed | 20s | Aug 1, 2026, 11:00:18 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_hbm\_device\_id | SohuHbmDeviceIdTestCase | Passed | 0s | Aug 1, 2026, 11:00:20 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_lane\_repair | SohuLaneRepairTestCase | Passed | 9s | Aug 1, 2026, 11:00:28 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_pmbist\_xmc\_4bk | SohuPmbistTestCase | Passed | 5s | Aug 1, 2026, 11:00:34 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_pmbist\_ymc\_32\_2bk | SohuPmbistTestCase | Passed | 9s | Aug 1, 2026, 11:00:45 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_pmbist\_ymc\_44\_2bk | SohuPmbistTestCase | Passed | 8s | Aug 1, 2026, 11:00:55 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_pmbist\_interleave\_16bk | SohuPmbistTestCase | Passed | 3s | Aug 1, 2026, 11:01:00 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_mtc\_stress | SohuMtcStressTestCase | Passed | 60s | Aug 1, 2026, 11:02:01 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_dma | SohuDmaTestCase | Passed | 23s | Aug 1, 2026, 11:02:25 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_sau\_pll\_phase\_alignment | SohuSauPllPhaseAlignmentTestCase | Passed | 1s | Aug 1, 2026, 11:02:27 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_run\_all\_attn\_hbm\_bypass\_tests | RunAllAttnHbmBypassTestsSingleChipTestCase | Passed | 21s | Aug 1, 2026, 11:02:48 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_run\_kv\_flush\_tests | RunKvFlushTestsSingleChipTestCase | Passed | 13s | Aug 1, 2026, 11:03:02 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_run\_all\_attn\_tests | RunAllAttnTestsSingleChipTestCase | Passed | 29s | Aug 1, 2026, 11:03:31 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_kv\_flush\_and\_attention | KvFlushAndAttentionSingleChipTestCase | Passed | 6s | Aug 1, 2026, 11:03:37 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_kv\_flush\_and\_attention\_interleaved | KvFlushAndAttentionInterleavedSingleChipTestCase | Passed | 6s | Aug 1, 2026, 11:03:44 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_sa\_sort\_rampup\_hbm | SaSortRampupHbmSingleChipTestCase | Passed | 15s | Aug 1, 2026, 11:03:58 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_sa\_column\_screen | SohuSaScreeningTestCase | Passed | 3s | Aug 1, 2026, 11:04:05 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_weight\_load | SohuWeightLoadTestCase | Passed | 8s | Aug 1, 2026, 11:04:13 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_llama8b\_fp8\_prefill | SohuLlama8bFp8PrefillTestCase | Passed | 3s | Aug 1, 2026, 11:04:17 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_llama8b\_fp8\_forward | SohuLlama8bFp8ForwardTestCase | Passed | 3s | Aug 1, 2026, 11:04:23 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_llama\_mtt\_soldered | SohuLlamaMttTestCase | Passed | 5s | Aug 1, 2026, 11:04:30 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_llama\_mtt\_socket | SohuLlamaMttTestCase | Skipped | 0s | — |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_power\_virus\_numeric\_sau | SohuPowerVirusTestCase | Passed | 6s | Aug 1, 2026, 11:04:38 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_power\_virus\_numeric\_sa | SohuPowerVirusTestCase | Passed | 7s | Aug 1, 2026, 11:04:44 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_power\_virus\_numeric\_c2c | SohuPowerVirusTestCase | Passed | 9s | Aug 1, 2026, 11:04:55 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_power\_virus\_csram\_numeric | SohuPowerVirusTestCase | Passed | 5s | Aug 1, 2026, 11:05:02 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_power\_virus\_thermal | SohuPowerVirusThermalTestCase | Passed | 162s | Aug 1, 2026, 11:07:45 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_chip\_bin | SohuChipBinTestCase | Skipped | 0s | — |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_chip1\_snap | SohuSnapTestCase | Passed | 0s | Aug 1, 2026, 11:07:47 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_cleanup\_cpld\_diagnostics | CpldDiagnosticsTestCase | Passed | 0s | Aug 1, 2026, 11:12:03 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_cleanup\_power\_off\_eval\_board\_test\_0 | EvalBoardPowerTestCase | Passed | 0s | Aug 1, 2026, 11:12:03 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_cleanup\_log\_reader\_capture | LogReaderCaptureTestCase | Passed | 0s | Aug 1, 2026, 11:12:06 PM UTC |  |
| mlt\_2026.209.0-git3fe4de25\_run\_764cdc97\_server\_cleanup\_pcie\_rescan\_server\_cleanup | PcieRescanTestCase | Passed | 0s | Aug 1, 2026, 11:12:06 PM UTC |  |