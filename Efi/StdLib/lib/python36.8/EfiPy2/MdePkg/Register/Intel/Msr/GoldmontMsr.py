# GoldmontMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.GoldmontMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_GOLDMONT_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x5C
           )

MSR_GOLDMONT_FEATURE_CONTROL  = 0x0000003A

class MSR_GOLDMONT_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",                        UINT32, 1),
    ("EnableVmxInsideSmx",          UINT32, 1),
    ("EnableVmxOutsideSmx",         UINT32, 1),
    ("Reserved1",                   UINT32, 5),
    ("SenterLocalFunctionEnables",  UINT32, 7),
    ("SenterGlobalEnable",          UINT32, 1),
    ("Reserved2",                   UINT32, 2),
    ("SgxEnable",                   UINT32, 1),
    ("Reserved3",                   UINT32, 13),
    ("Reserved4",                   UINT32, 32)
  ]

class MSR_GOLDMONT_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PLATFORM_INFO  = 0x000000CE

class MSR_GOLDMONT_PLATFORM_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumNonTurboRatio",    UINT32, 8),
    ("Reserved2",               UINT32, 12),
    ("RatioLimit",              UINT32, 1),
    ("TDPLimit",                UINT32, 1),
    ("TJOFFSET",                UINT32, 1),
    ("Reserved3",               UINT32, 1),
    ("Reserved4",               UINT32, 8),
    ("MaximumEfficiencyRatio",  UINT32, 8),
    ("Reserved5",               UINT32, 16)
  ]

class MSR_GOLDMONT_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PLATFORM_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_GOLDMONT_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",       UINT32, 4),
    ("Reserved1",   UINT32, 6),
    ("IO_MWAIT",    UINT32, 1),
    ("Reserved2",   UINT32, 4),
    ("CFGLock",     UINT32, 1),
    ("Reserved3",   UINT32, 16),
    ("Reserved4",   UINT32, 32)
  ]

class MSR_GOLDMONT_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_SMM_MCA_CAP  = 0x0000017D

class MSR_GOLDMONT_SMM_MCA_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 32),
    ("Reserved2",               UINT32, 26),
    ("SMM_Code_Access_Chk",     UINT32, 1),
    ("Long_Flow_Indication",    UINT32, 1),
    ("Reserved3",               UINT32, 4)
  ]

class MSR_GOLDMONT_SMM_MCA_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_SMM_MCA_CAP_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_IA32_MISC_ENABLE  = 0x000001A0

class MSR_GOLDMONT_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FastStrings",                     UINT32, 1),
    ("Reserved1",                       UINT32, 2),
    ("AutomaticThermalControlCircuit",  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("PerformanceMonitoring",           UINT32, 1),
    ("Reserved3",                       UINT32, 3),
    ("BTS",                             UINT32, 1),
    ("PEBS",                            UINT32, 1),
    ("Reserved4",                       UINT32, 3),
    ("EIST",                            UINT32, 1),
    ("Reserved5",                       UINT32, 1),
    ("MONITOR",                         UINT32, 1),
    ("Reserved6",                       UINT32, 3),
    ("LimitCpuidMaxval",                UINT32, 1),
    ("xTPR_Message_Disable",            UINT32, 1),
    ("Reserved7",                       UINT32, 8),
    ("Reserved8",                       UINT32, 2),
    ("XD",                              UINT32, 1),
    ("Reserved9",                       UINT32, 3),
    ("TurboModeDisable",                UINT32, 1),
    ("Reserved10",                      UINT32, 25)
  ]

class MSR_GOLDMONT_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_MISC_FEATURE_CONTROL  = 0x000001A4

class MSR_GOLDMONT_MISC_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2HardwarePrefetcherDisable",     UINT32, 1),
    ("Reserved1",                       UINT32, 1),
    ("DCUHardwarePrefetcherDisable",    UINT32, 1),
    ("Reserved2",                       UINT32, 29),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_GOLDMONT_MISC_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_MISC_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_MISC_PWR_MGMT  = 0x000001AA

class MSR_GOLDMONT_MISC_PWR_MGMT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EISTHardwareCoordinationDisable",     UINT32, 1),
    ("Reserved1",                           UINT32, 21),
    ("ThermalInterruptCoordinationEnable",  UINT32, 1),
    ("Reserved2",                           UINT32, 9),
    ("Reserved3",                           UINT32, 32)
  ]

class MSR_GOLDMONT_MISC_PWR_MGMT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_MISC_PWR_MGMT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_GOLDMONT_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MaxRatioLimitGroup0", UINT32, 8),
    ("MaxRatioLimitGroup1", UINT32, 8),
    ("MaxRatioLimitGroup2", UINT32, 8),
    ("MaxRatioLimitGroup3", UINT32, 8),
    ("MaxRatioLimitGroup4", UINT32, 8),
    ("MaxRatioLimitGroup5", UINT32, 8),
    ("MaxRatioLimitGroup6", UINT32, 8),
    ("MaxRatioLimitGroup7", UINT32, 8)
  ]

class MSR_GOLDMONT_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_TURBO_GROUP_CORECNT  = 0x000001AE

class MSR_GOLDMONT_TURBO_GROUP_CORECNT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CoreCountThresholdGroup0", UINT32, 8),
    ("CoreCountThresholdGroup1", UINT32, 8),
    ("CoreCountThresholdGroup2", UINT32, 8),
    ("CoreCountThresholdGroup3", UINT32, 8),
    ("CoreCountThresholdGroup4", UINT32, 8),
    ("CoreCountThresholdGroup5", UINT32, 8),
    ("CoreCountThresholdGroup6", UINT32, 8),
    ("CoreCountThresholdGroup7", UINT32, 8)
  ]

class MSR_GOLDMONT_TURBO_GROUP_CORECNT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_TURBO_GROUP_CORECNT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_LBR_SELECT  = 0x000001C8

class MSR_GOLDMONT_LBR_SELECT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CPL_EQ_0",        UINT32, 1),
    ("CPL_NEQ_0",       UINT32, 1),
    ("JCC",             UINT32, 1),
    ("NEAR_REL_CALL",   UINT32, 1),
    ("NEAR_IND_CALL",   UINT32, 1),
    ("NEAR_RET",        UINT32, 1),
    ("NEAR_IND_JMP",    UINT32, 1),
    ("NEAR_REL_JMP",    UINT32, 1),
    ("FAR_BRANCH",      UINT32, 1),
    ("EN_CALL_STACK",   UINT32, 1),
    ("Reserved1",       UINT32, 22),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_GOLDMONT_LBR_SELECT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_LBR_SELECT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_LASTBRANCH_TOS  = 0x000001C9

MSR_GOLDMONT_POWER_CTL  = 0x000001FC

class MSR_GOLDMONT_POWER_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1", UINT32, 1),
    ("C1EEnable", UINT32, 1),
    ("Reserved2", UINT32, 30),
    ("Reserved3", UINT32, 32)
  ]

class MSR_GOLDMONT_POWER_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_POWER_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_SGXOWNEREPOCH0  = 0x00000300

MSR_GOLDMONT_SGXOWNER0  = MSR_GOLDMONT_SGXOWNEREPOCH0

MSR_GOLDMONT_SGXOWNEREPOCH1  = 0x00000301

MSR_GOLDMONT_SGXOWNER1  = MSR_GOLDMONT_SGXOWNEREPOCH1

MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_RESET  = 0x00000390

class MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0", UINT32, 1),
    ("Ovf_PMC1", UINT32, 1),
    ("Ovf_PMC2", UINT32, 1),
    ("Ovf_PMC3", UINT32, 1),
    ("Reserved1", UINT32, 28),
    ("Ovf_FixedCtr0", UINT32, 1),
    ("Ovf_FixedCtr1", UINT32, 1),
    ("Ovf_FixedCtr2", UINT32, 1),
    ("Reserved2", UINT32, 20),
    ("Trace_ToPA_PMI", UINT32, 1),
    ("Reserved3", UINT32, 2),
    ("LBR_Frz", UINT32, 1),
    ("CTR_Frz", UINT32, 1),
    ("ASCI", UINT32, 1),
    ("Ovf_Uncore", UINT32, 1),
    ("Ovf_BufDSSAVE", UINT32, 1),
    ("CondChgd", UINT32, 1)
  ]

class MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_SET  = 0x00000391

class MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0", UINT32, 1),
    ("Ovf_PMC1", UINT32, 1),
    ("Ovf_PMC2", UINT32, 1),
    ("Ovf_PMC3", UINT32, 1),
    ("Reserved1", UINT32, 28),
    ("Ovf_FixedCtr0", UINT32, 1),
    ("Ovf_FixedCtr1", UINT32, 1),
    ("Ovf_FixedCtr2", UINT32, 1),
    ("Reserved2", UINT32, 20),
    ("Trace_ToPA_PMI", UINT32, 1),
    ("Reserved3", UINT32, 2),
    ("LBR_Frz", UINT32, 1),
    ("CTR_Frz", UINT32, 1),
    ("ASCI", UINT32, 1),
    ("Ovf_Uncore", UINT32, 1),
    ("Ovf_BufDSSAVE", UINT32, 1),
    ("CondChgd", UINT32, 1)
  ]

class MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_SET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PEBS_ENABLE  = 0x000003F1

class MSR_GOLDMONT_PEBS_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",      UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_GOLDMONT_PEBS_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PEBS_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PKG_C3_RESIDENCY  = 0x000003F8

MSR_GOLDMONT_PKG_C6_RESIDENCY  = 0x000003F9

MSR_GOLDMONT_CORE_C3_RESIDENCY  = 0x000003FC

MSR_GOLDMONT_SMM_FEATURE_CONTROL  = 0x000004E0

class MSR_GOLDMONT_SMM_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",            UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("SMM_Code_Chk_En", UINT32, 1),
    ("Reserved2",       UINT32, 29),
    ("Reserved3",       UINT32, 32)
  ]

class MSR_GOLDMONT_SMM_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_SMM_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_SMM_DELAYED  = 0x000004E2

MSR_GOLDMONT_SMM_BLOCKED  = 0x000004E3

MSR_IA32_RTIT_CTL  = 0x00000570

class MSR_GOLDMONT_IA32_RTIT_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TraceEn",     UINT32, 1),
    ("CYCEn",       UINT32, 1),
    ("OS",          UINT32, 1),
    ("User",        UINT32, 1),
    ("Reserved1",   UINT32, 3),
    ("CR3",         UINT32, 1),
    ("ToPA",        UINT32, 1),
    ("MTCEn",       UINT32, 1),
    ("TSCEn",       UINT32, 1),
    ("DisRETC",     UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("BranchEn",    UINT32, 1),
    ("MTCFreq",     UINT32, 4),
    ("Reserved3",   UINT32, 1),
    ("CYCThresh",   UINT32, 4),
    ("Reserved4",   UINT32, 1),
    ("PSBFreq",     UINT32, 4),
    ("Reserved5",   UINT32, 4),
    ("ADDR0_CFG",   UINT32, 4),
    ("ADDR1_CFG",   UINT32, 4),
    ("Reserved6",   UINT32, 24)
  ]

class MSR_GOLDMONT_IA32_RTIT_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_RTIT_CTL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_RAPL_POWER_UNIT  = 0x00000606

class MSR_GOLDMONT_RAPL_POWER_UNIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PowerUnits",          UINT32, 4),
    ("Reserved1",           UINT32, 4),
    ("EnergyStatusUnits",   UINT32, 5),
    ("Reserved2",           UINT32, 3),
    ("TimeUnit",            UINT32, 4),
    ("Reserved3",           UINT32, 12),
    ("Reserved4",           UINT32, 32)
  ]

class MSR_GOLDMONT_RAPL_POWER_UNIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_RAPL_POWER_UNIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PKGC3_IRTL  = 0x0000060A

class MSR_GOLDMONT_PKGC3_IRTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptResponseTimeLimit",  UINT32, 10),
    ("TimeUnit",                    UINT32, 3),
    ("Reserved1",                   UINT32, 2),
    ("Valid",                       UINT32, 1),
    ("Reserved2",                   UINT32, 16),
    ("Reserved3",                   UINT32, 32)
  ]

class MSR_GOLDMONT_PKGC3_IRTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PKGC3_IRTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PKGC_IRTL1  = 0x0000060B

class MSR_GOLDMONT_PKGC_IRTL1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptResponseTimeLimit",  UINT32, 10),
    ("TimeUnit",                    UINT32, 3),
    ("Reserved1",                   UINT32, 2),
    ("Valid",                       UINT32, 1),
    ("Reserved2",                   UINT32, 16),
    ("Reserved3",                   UINT32, 32)
  ]

class MSR_GOLDMONT_PKGC_IRTL1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PKGC_IRTL1_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PKGC_IRTL2  = 0x0000060C

class MSR_GOLDMONT_PKGC_IRTL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptResponseTimeLimit",  UINT32, 10),
    ("TimeUnit",                    UINT32, 3),
    ("Reserved1",                   UINT32, 2),
    ("Valid",                       UINT32, 1),
    ("Reserved2",                   UINT32, 16),
    ("Reserved3",                   UINT32, 32)
  ]

class MSR_GOLDMONT_PKGC_IRTL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PKGC_IRTL2_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_PKG_C2_RESIDENCY  = 0x0000060D

MSR_GOLDMONT_PKG_POWER_LIMIT  = 0x00000610

MSR_GOLDMONT_PKG_ENERGY_STATUS  = 0x00000611

MSR_GOLDMONT_PKG_PERF_STATUS  = 0x00000613

MSR_GOLDMONT_PKG_POWER_INFO  = 0x00000614

class MSR_GOLDMONT_PKG_POWER_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ThermalSpecPower",    UINT32, 15),
    ("Reserved1",           UINT32, 1),
    ("MinimumPower",        UINT32, 15),
    ("Reserved2",           UINT32, 1),
    ("MaximumPower",        UINT32, 15),
    ("Reserved3",           UINT32, 1),
    ("MaximumTimeWindow",   UINT32, 7),
    ("Reserved4",           UINT32, 9)
  ]

class MSR_GOLDMONT_PKG_POWER_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_PKG_POWER_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_DRAM_POWER_LIMIT  = 0x00000618

MSR_GOLDMONT_DRAM_ENERGY_STATUS  = 0x00000619

MSR_GOLDMONT_DRAM_PERF_STATUS  = 0x0000061B

MSR_GOLDMONT_DRAM_POWER_INFO  = 0x0000061C

MSR_GOLDMONT_PKG_C10_RESIDENCY  = 0x00000632

MSR_GOLDMONT_PP0_ENERGY_STATUS  = 0x00000639

MSR_GOLDMONT_PP1_ENERGY_STATUS  = 0x00000641

MSR_GOLDMONT_TURBO_ACTIVATION_RATIO  = 0x0000064C

class MSR_GOLDMONT_TURBO_ACTIVATION_RATIO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_NON_TURBO_RATIO",         UINT32, 8),
    ("Reserved1",                   UINT32, 23),
    ("TURBO_ACTIVATION_RATIO_Lock", UINT32, 1),
    ("Reserved2",                   UINT32, 32)
  ]

class MSR_GOLDMONT_TURBO_ACTIVATION_RATIO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_TURBO_ACTIVATION_RATIO_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_CORE_PERF_LIMIT_REASONS  = 0x0000064F

class MSR_GOLDMONT_CORE_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOTStatus",                       UINT32, 1),
    ("ThermalStatus",                       UINT32, 1),
    ("PL1Status",                           UINT32, 1),
    ("PL2Status",                           UINT32, 1),
    ("Reserved1",                           UINT32, 5),
    ("PowerLimitingStatus",                 UINT32, 1),
    ("VRThermAlertStatus",                  UINT32, 1),
    ("MaxTurboLimitStatus",                 UINT32, 1),
    ("ElectricalDesignPointStatus",         UINT32, 1),
    ("TurboTransitionAttenuationStatus",    UINT32, 1),
    ("MaximumEfficiencyFrequencyStatus",    UINT32, 1),
    ("Reserved2",                           UINT32, 1),
    ("PROCHOT",                             UINT32, 1),
    ("ThermalLog",                          UINT32, 1),
    ("PL1Log",                              UINT32, 1),
    ("PL2Log",                              UINT32, 1),
    ("Reserved3",                           UINT32, 5),
    ("CorePowerLimitingLog",                UINT32, 1),
    ("VRThermAlertLog",                     UINT32, 1),
    ("MaxTurboLimitLog",                    UINT32, 1),
    ("ElectricalDesignPointLog",            UINT32, 1),
    ("TurboTransitionAttenuationLog",       UINT32, 1),
    ("MaximumEfficiencyFrequencyLog",       UINT32, 1),
    ("Reserved4",                           UINT32, 1),
    ("Reserved5",                           UINT32, 32)
  ]

class MSR_GOLDMONT_CORE_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_CORE_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_LASTBRANCH_0_FROM_IP   = 0x00000680
MSR_GOLDMONT_LASTBRANCH_1_FROM_IP   = 0x00000681
MSR_GOLDMONT_LASTBRANCH_2_FROM_IP   = 0x00000682
MSR_GOLDMONT_LASTBRANCH_3_FROM_IP   = 0x00000683
MSR_GOLDMONT_LASTBRANCH_4_FROM_IP   = 0x00000684
MSR_GOLDMONT_LASTBRANCH_5_FROM_IP   = 0x00000685
MSR_GOLDMONT_LASTBRANCH_6_FROM_IP   = 0x00000686
MSR_GOLDMONT_LASTBRANCH_7_FROM_IP   = 0x00000687
MSR_GOLDMONT_LASTBRANCH_8_FROM_IP   = 0x00000688
MSR_GOLDMONT_LASTBRANCH_9_FROM_IP   = 0x00000689
MSR_GOLDMONT_LASTBRANCH_10_FROM_IP  = 0x0000068A
MSR_GOLDMONT_LASTBRANCH_11_FROM_IP  = 0x0000068B
MSR_GOLDMONT_LASTBRANCH_12_FROM_IP  = 0x0000068C
MSR_GOLDMONT_LASTBRANCH_13_FROM_IP  = 0x0000068D
MSR_GOLDMONT_LASTBRANCH_14_FROM_IP  = 0x0000068E
MSR_GOLDMONT_LASTBRANCH_15_FROM_IP  = 0x0000068F
MSR_GOLDMONT_LASTBRANCH_16_FROM_IP  = 0x00000690
MSR_GOLDMONT_LASTBRANCH_17_FROM_IP  = 0x00000691
MSR_GOLDMONT_LASTBRANCH_18_FROM_IP  = 0x00000692
MSR_GOLDMONT_LASTBRANCH_19_FROM_IP  = 0x00000693
MSR_GOLDMONT_LASTBRANCH_20_FROM_IP  = 0x00000694
MSR_GOLDMONT_LASTBRANCH_21_FROM_IP  = 0x00000695
MSR_GOLDMONT_LASTBRANCH_22_FROM_IP  = 0x00000696
MSR_GOLDMONT_LASTBRANCH_23_FROM_IP  = 0x00000697
MSR_GOLDMONT_LASTBRANCH_24_FROM_IP  = 0x00000698
MSR_GOLDMONT_LASTBRANCH_25_FROM_IP  = 0x00000699
MSR_GOLDMONT_LASTBRANCH_26_FROM_IP  = 0x0000069A
MSR_GOLDMONT_LASTBRANCH_27_FROM_IP  = 0x0000069B
MSR_GOLDMONT_LASTBRANCH_28_FROM_IP  = 0x0000069C
MSR_GOLDMONT_LASTBRANCH_29_FROM_IP  = 0x0000069D
MSR_GOLDMONT_LASTBRANCH_30_FROM_IP  = 0x0000069E
MSR_GOLDMONT_LASTBRANCH_31_FROM_IP  = 0x0000069F

class MSR_GOLDMONT_LASTBRANCH_FROM_IP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FromLinearAddress",   UINT32, 32),
    ("FromLinearAddressHi", UINT32, 16),
    ("SignedExtension",     UINT32, 15),
    ("Mispred",             UINT32, 1)
  ]

class MSR_GOLDMONT_LASTBRANCH_FROM_IP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_LASTBRANCH_FROM_IP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_LASTBRANCH_0_TO_IP   = 0x000006C0
MSR_GOLDMONT_LASTBRANCH_1_TO_IP   = 0x000006C1
MSR_GOLDMONT_LASTBRANCH_2_TO_IP   = 0x000006C2
MSR_GOLDMONT_LASTBRANCH_3_TO_IP   = 0x000006C3
MSR_GOLDMONT_LASTBRANCH_4_TO_IP   = 0x000006C4
MSR_GOLDMONT_LASTBRANCH_5_TO_IP   = 0x000006C5
MSR_GOLDMONT_LASTBRANCH_6_TO_IP   = 0x000006C6
MSR_GOLDMONT_LASTBRANCH_7_TO_IP   = 0x000006C7
MSR_GOLDMONT_LASTBRANCH_8_TO_IP   = 0x000006C8
MSR_GOLDMONT_LASTBRANCH_9_TO_IP   = 0x000006C9
MSR_GOLDMONT_LASTBRANCH_10_TO_IP  = 0x000006CA
MSR_GOLDMONT_LASTBRANCH_11_TO_IP  = 0x000006CB
MSR_GOLDMONT_LASTBRANCH_12_TO_IP  = 0x000006CC
MSR_GOLDMONT_LASTBRANCH_13_TO_IP  = 0x000006CD
MSR_GOLDMONT_LASTBRANCH_14_TO_IP  = 0x000006CE
MSR_GOLDMONT_LASTBRANCH_15_TO_IP  = 0x000006CF
MSR_GOLDMONT_LASTBRANCH_16_TO_IP  = 0x000006D0
MSR_GOLDMONT_LASTBRANCH_17_TO_IP  = 0x000006D1
MSR_GOLDMONT_LASTBRANCH_18_TO_IP  = 0x000006D2
MSR_GOLDMONT_LASTBRANCH_19_TO_IP  = 0x000006D3
MSR_GOLDMONT_LASTBRANCH_20_TO_IP  = 0x000006D4
MSR_GOLDMONT_LASTBRANCH_21_TO_IP  = 0x000006D5
MSR_GOLDMONT_LASTBRANCH_22_TO_IP  = 0x000006D6
MSR_GOLDMONT_LASTBRANCH_23_TO_IP  = 0x000006D7
MSR_GOLDMONT_LASTBRANCH_24_TO_IP  = 0x000006D8
MSR_GOLDMONT_LASTBRANCH_25_TO_IP  = 0x000006D9
MSR_GOLDMONT_LASTBRANCH_26_TO_IP  = 0x000006DA
MSR_GOLDMONT_LASTBRANCH_27_TO_IP  = 0x000006DB
MSR_GOLDMONT_LASTBRANCH_28_TO_IP  = 0x000006DC
MSR_GOLDMONT_LASTBRANCH_29_TO_IP  = 0x000006DD
MSR_GOLDMONT_LASTBRANCH_30_TO_IP  = 0x000006DE
MSR_GOLDMONT_LASTBRANCH_31_TO_IP  = 0x000006DF

class MSR_GOLDMONT_LASTBRANCH_TO_IP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TargetLinearAddress",     UINT32, 32),
    ("TargetLinearAddressHi",   UINT32, 16),
    ("ElapsedCycles",           UINT32, 15)
  ]

class MSR_GOLDMONT_LASTBRANCH_TO_IP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_LASTBRANCH_TO_IP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_IA32_PQR_ASSOC  = 0x00000C8F

class MSR_GOLDMONT_IA32_PQR_ASSOC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 32),
    ("COS",         UINT32, 2),
    ("Reserved2",   UINT32, 30)
  ]

class MSR_GOLDMONT_IA32_PQR_ASSOC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_PQR_ASSOC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_IA32_L2_QOS_MASK_0  = 0x00000D10
MSR_GOLDMONT_IA32_L2_QOS_MASK_1  = 0x00000D11
MSR_GOLDMONT_IA32_L2_QOS_MASK_2  = 0x00000D12

class MSR_GOLDMONT_IA32_L2_QOS_MASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CBM",         UINT32, 8),
    ("Reserved1",   UINT32, 24),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_GOLDMONT_IA32_L2_QOS_MASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_L2_QOS_MASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_GOLDMONT_IA32_L2_QOS_MASK_3  = 0x00000D13

class MSR_GOLDMONT_IA32_L2_QOS_MASK_3_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CBM",         UINT32, 20),
    ("Reserved1",   UINT32, 12),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_GOLDMONT_IA32_L2_QOS_MASK_3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GOLDMONT_IA32_L2_QOS_MASK_3_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

