# XeonPhiMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.XeonPhiMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_XEON_PHI_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x57 or
           DisplayModel == 0x85
           )

MSR_XEON_PHI_SMI_COUNT  = 0x00000034

class MSR_XEON_PHI_SMI_COUNT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SMICount",    UINT32, 8),
    ("Reserved",    UINT32, 8)
  ]

class MSR_XEON_PHI_SMI_COUNT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_SMI_COUNT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_PPIN_CTL  = 0x0000004E

class MSR_XEON_PHI_PPIN_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LockOut",     UINT32, 1),
    ("Enable_PPIN", UINT32, 1),
    ("Reserved1",   UINT32, 30),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_XEON_PHI_PPIN_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_PPIN_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_PPIN  = 0x0000004F

MSR_XEON_PHI_PLATFORM_INFO  = 0x000000CE

class MSR_XEON_PHI_PLATFORM_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumNonTurboRatio",    UINT32, 8),
    ("Reserved2",               UINT32, 12),
    ("RatioLimit",              UINT32, 1),
    ("TDPLimit",                UINT32, 1),
    ("Reserved3",               UINT32, 2),
    ("Reserved4",               UINT32, 8),
    ("MaximumEfficiencyRatio",  UINT32, 8),
    ("Reserved5",               UINT32, 16)
  ]

class MSR_XEON_PHI_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_PLATFORM_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_XEON_PHI_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",                           UINT32, 3),
    ("Reserved1",                       UINT32, 7),
    ("IO_MWAIT",                        UINT32, 1),
    ("Reserved2",                       UINT32, 4),
    ("CFGLock",                         UINT32, 1),
    ("Reserved5",                       UINT32, 10),
    ("C1StateAutoDemotionEnable",       UINT32, 1),
    ("Reserved6",                       UINT32, 1),
    ("C1StateAutoUndemotionEnable",     UINT32, 1),
    ("PKGC_StateAutoDemotionEnable",    UINT32, 1),
    ("Reserved7",                       UINT32, 2),
    ("Reserved4",                       UINT32, 32)
  ]

class MSR_XEON_PHI_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_PMG_IO_CAPTURE_BASE  = 0x000000E4

class MSR_XEON_PHI_PMG_IO_CAPTURE_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lvl2Base",    UINT32, 16),
    ("CStateRange", UINT32, 7),
    ("Reserved3",   UINT32, 9),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_XEON_PHI_PMG_IO_CAPTURE_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_PMG_IO_CAPTURE_BASE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_FEATURE_CONFIG  = 0x0000013C

class MSR_XEON_PHI_FEATURE_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("AESConfiguration",    UINT32, 2),
    ("Reserved1",           UINT32, 30),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_XEON_PHI_FEATURE_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_FEATURE_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_MISC_FEATURE_ENABLES  = 0x00000140

class MSR_XEON_PHI_MISC_FEATURE_ENABLES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 1),
    ("UserModeMonitorAndMwait", UINT32, 1),
    ("Reserved2",               UINT32, 30),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_XEON_PHI_MISC_FEATURE_ENABLES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_MISC_FEATURE_ENABLES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_SMM_MCA_CAP  = 0x0000017D

class MSR_XEON_PHI_SMM_MCA_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("BankSupport",             UINT32, 32),
    ("Reserved4",               UINT32, 24),
    ("TargetedSMI",             UINT32, 1),
    ("SMM_CPU_SVRSTR",          UINT32, 1),
    ("SMM_Code_Access_Chk",     UINT32, 1),
    ("Long_Flow_Indication",    UINT32, 1),
    ("Reserved3",               UINT32, 4)
  ]

class MSR_XEON_PHI_SMM_MCA_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_SMM_MCA_CAP_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_IA32_MISC_ENABLE  = 0x000001A0

class MSR_XEON_PHI_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
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

class MSR_XEON_PHI_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_TEMPERATURE_TARGET  = 0x000001A2

class MSR_XEON_PHI_TEMPERATURE_TARGET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 16),
    ("TemperatureTarget",   UINT32, 8),
    ("TargetOffset",        UINT32, 6),
    ("Reserved2",           UINT32, 2),
    ("Reserved3",           UINT32, 32)
  ]

class MSR_XEON_PHI_TEMPERATURE_TARGET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_TEMPERATURE_TARGET_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_MISC_FEATURE_CONTROL  = 0x000001A4

class MSR_XEON_PHI_MISC_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("DCUHardwarePrefetcherDisable",    UINT32, 1),
    ("L2HardwarePrefetcherDisable",     UINT32, 1),
    ("Reserved1",                       UINT32, 30),
    ("Reserved2",                       UINT32, 32)
  ]

class MSR_XEON_PHI_MISC_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_MISC_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_OFFCORE_RSP_0  = 0x000001A6

MSR_XEON_PHI_OFFCORE_RSP_1  = 0x000001A7

MSR_XEON_PHI_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_XEON_PHI_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",                    UINT32, 1),
    ("MaxCoresGroup0",              UINT32, 7),
    ("MaxRatioLimitGroup0",         UINT32, 8),
    ("MaxIncrementalCoresGroup1",   UINT32, 5),
    ("DeltaRatioGroup1",            UINT32, 3),
    ("MaxIncrementalCoresGroup2",   UINT32, 5),
    ("DeltaRatioGroup2",            UINT32, 3),
    ("MaxIncrementalCoresGroup3",   UINT32, 5),
    ("DeltaRatioGroup3",            UINT32, 3),
    ("MaxIncrementalCoresGroup4",   UINT32, 5),
    ("DeltaRatioGroup4",            UINT32, 3),
    ("MaxIncrementalCoresGroup5",   UINT32, 5),
    ("DeltaRatioGroup5",            UINT32, 3),
    ("MaxIncrementalCoresGroup6",   UINT32, 5),
    ("DeltaRatioGroup6",            UINT32, 3)
  ]

class MSR_XEON_PHI_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_LBR_SELECT  = 0x000001C8

class MSR_XEON_PHI_LBR_SELECT_REGISTER_Bits (Structure):
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
    ("Reserved1",       UINT32, 23),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_XEON_PHI_LBR_SELECT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_LBR_SELECT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_LASTBRANCH_TOS         = 0x000001C9
MSR_XEON_PHI_LER_FROM_LIP           = 0x000001DD
MSR_XEON_PHI_LER_TO_LIP             = 0x000001DE
MSR_XEON_PHI_PEBS_ENABLE            = 0x000003F1
MSR_XEON_PHI_PKG_C3_RESIDENCY       = 0x000003F8
MSR_XEON_PHI_PKG_C6_RESIDENCY       = 0x000003F9
MSR_XEON_PHI_PKG_C7_RESIDENCY       = 0x000003FA
MSR_XEON_PHI_MC0_RESIDENCY          = 0x000003FC
MSR_XEON_PHI_MC6_RESIDENCY          = 0x000003FD
MSR_XEON_PHI_CORE_C6_RESIDENCY      = 0x000003FF
MSR_XEON_PHI_IA32_VMX_EPT_VPID_ENUM = 0x0000048C
MSR_XEON_PHI_IA32_VMX_FMFUNC        = 0x00000491
MSR_XEON_PHI_RAPL_POWER_UNIT        = 0x00000606

class MSR_XEON_PHI_RAPL_POWER_UNIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PowerUnits",          UINT32, 4),
    ("Reserved1",           UINT32, 4),
    ("EnergyStatusUnits",   UINT32, 5),
    ("Reserved2",           UINT32, 3),
    ("TimeUnits",           UINT32, 4),
    ("Reserved3",           UINT32, 12),
    ("Reserved4",           UINT32, 32)
  ]

class MSR_XEON_PHI_RAPL_POWER_UNIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_RAPL_POWER_UNIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_PKG_C2_RESIDENCY       = 0x0000060D
MSR_XEON_PHI_PKG_POWER_LIMIT        = 0x00000610
MSR_XEON_PHI_PKG_ENERGY_STATUS      = 0x00000611
MSR_XEON_PHI_PKG_PERF_STATUS        = 0x00000613
MSR_XEON_PHI_PKG_POWER_INFO         = 0x00000614
MSR_XEON_PHI_DRAM_POWER_LIMIT       = 0x00000618
MSR_XEON_PHI_DRAM_ENERGY_STATUS     = 0x00000619
MSR_XEON_PHI_DRAM_PERF_STATUS       = 0x0000061B
MSR_XEON_PHI_DRAM_POWER_INFO        = 0x0000061C
MSR_XEON_PHI_MSRUNCORE_RATIO_LIMIT  = 0x00000620

class MSR_XEON_PHI_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_RATIO", UINT32, 7),
    ("Reserved1", UINT32, 1),
    ("MIN_RATIO", UINT32, 7),
    ("Reserved2", UINT32, 17),
    ("Reserved3", UINT32, 32)
  ]

class MSR_XEON_PHI_MSRUNCORE_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_PHI_PP0_POWER_LIMIT          = 0x00000638
MSR_XEON_PHI_PP0_ENERGY_STATUS        = 0x00000639
MSR_XEON_PHI_CONFIG_TDP_NOMINAL       = 0x00000648
MSR_XEON_PHI_CONFIG_TDP_LEVEL1        = 0x00000649
MSR_XEON_PHI_CONFIG_TDP_LEVEL2        = 0x0000064A
MSR_XEON_PHI_CONFIG_TDP_CONTROL       = 0x0000064B
MSR_XEON_PHI_TURBO_ACTIVATION_RATIO   = 0x0000064C
MSR_XEON_PHI_CORE_PERF_LIMIT_REASONS  = 0x00000690

class MSR_XEON_PHI_CORE_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",              UINT32, 1),
    ("ThermalStatus",               UINT32, 1),
    ("Reserved1",                   UINT32, 4),
    ("VRThermAlertStatus",          UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("ElectricalDesignPointStatus", UINT32, 1),
    ("Reserved3",                   UINT32, 23),
    ("Reserved4",                   UINT32, 32)
  ]

class MSR_XEON_PHI_CORE_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_PHI_CORE_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]
