# HaswellMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.HaswellMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_HASWELL_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x3C or
           DisplayModel == 0x45 or
           DisplayModel == 0x46
           )

MSR_HASWELL_PLATFORM_INFO  = 0x000000CE

class MSR_HASWELL_PLATFORM_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumNonTurboRatio",    UINT32, 8),
    ("Reserved2",               UINT32, 12),
    ("RatioLimit",              UINT32, 1),
    ("TDPLimit",                UINT32, 1),
    ("Reserved3",               UINT32, 2),
    ("LowPowerModeSupport",     UINT32, 1),
    ("ConfigTDPLevels",         UINT32, 2),
    ("Reserved4",               UINT32, 5),
    ("MaximumEfficiencyRatio",  UINT32, 8),
    ("MinimumOperatingRatio",   UINT32, 8),
    ("Reserved5",               UINT32, 8)
  ]

class MSR_HASWELL_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PLATFORM_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_IA32_PERFEVTSEL0  = 0x00000186
MSR_HASWELL_IA32_PERFEVTSEL1  = 0x00000187
MSR_HASWELL_IA32_PERFEVTSEL3  = 0x00000189

class MSR_HASWELL_IA32_PERFEVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventSelect", UINT32, 8),
    ("UMASK",       UINT32, 8),
    ("USR",         UINT32, 1),
    ("OS",          UINT32, 1),
    ("E",           UINT32, 1),
    ("PC",          UINT32, 1),
    ("INT",         UINT32, 1),
    ("ANY",         UINT32, 1),
    ("EN",          UINT32, 1),
    ("INV",         UINT32, 1),
    ("CMASK",       UINT32, 8),
    ("Reserved",    UINT32, 32),
    ("IN_TX",       UINT32, 1),
    ("Reserved2",   UINT32, 31)
  ]

class MSR_HASWELL_IA32_PERFEVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_IA32_PERFEVTSEL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_IA32_PERFEVTSEL2  = 0x00000188

class MSR_HASWELL_IA32_PERFEVTSEL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventSelect", UINT32, 8),
    ("UMASK",       UINT32, 8),
    ("USR",         UINT32, 1),
    ("OS",          UINT32, 1),
    ("E",           UINT32, 1),
    ("PC",          UINT32, 1),
    ("INT",         UINT32, 1),
    ("ANY",         UINT32, 1),
    ("EN",          UINT32, 1),
    ("INV",         UINT32, 1),
    ("CMASK",       UINT32, 8),
    ("Reserved",    UINT32, 32),
    ("IN_TX",       UINT32, 1),
    ("IN_TXCP",     UINT32, 1),
    ("Reserved2",   UINT32, 30)
  ]

class MSR_HASWELL_IA32_PERFEVTSEL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_IA32_PERFEVTSEL2_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_LBR_SELECT  = 0x000001C8

class MSR_HASWELL_LBR_SELECT_REGISTER_Bits (Structure):
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

class MSR_HASWELL_LBR_SELECT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_LBR_SELECT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PKGC_IRTL1  = 0x0000060B

class MSR_HASWELL_PKGC_IRTL1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptResponseTimeLimit",  UINT32, 10),
    ("TimeUnit",                    UINT32, 3),
    ("Reserved1",                   UINT32, 2),
    ("Valid",                       UINT32, 1),
    ("Reserved2",                   UINT32, 16),
    ("Reserved3",                   UINT32, 32)
  ]

class MSR_HASWELL_PKGC_IRTL1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PKGC_IRTL1_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PKGC_IRTL2  = 0x0000060C

class MSR_HASWELL_PKGC_IRTL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptResponseTimeLimit",  UINT32, 10),
    ("TimeUnit",                    UINT32, 3),
    ("Reserved1",                   UINT32, 2),
    ("Valid",                       UINT32, 1),
    ("Reserved2",                   UINT32, 16),
    ("Reserved3",                   UINT32, 32)
  ]

class MSR_HASWELL_PKGC_IRTL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PKGC_IRTL2_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PKG_PERF_STATUS     = 0x00000613

MSR_HASWELL_DRAM_ENERGY_STATUS  = 0x00000619

MSR_HASWELL_DRAM_PERF_STATUS    = 0x0000061B

MSR_HASWELL_CONFIG_TDP_NOMINAL  = 0x00000648

class MSR_HASWELL_CONFIG_TDP_NOMINAL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Config_TDP_Base", UINT32, 8),
    ("Reserved1",       UINT32, 24),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_HASWELL_CONFIG_TDP_NOMINAL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_CONFIG_TDP_NOMINAL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_CONFIG_TDP_LEVEL1  = 0x00000649

class MSR_HASWELL_CONFIG_TDP_LEVEL1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PKG_TDP_LVL1",            UINT32, 15),
    ("Reserved1",               UINT32, 1),
    ("Config_TDP_LVL1_Ratio",   UINT32, 8),
    ("Reserved2",               UINT32, 8),
    ("PKG_MAX_PWR_LVL1",        UINT32, 15),
    ("PKG_MIN_PWR_LVL1",        UINT32, 16),
    ("Reserved3",               UINT32, 1)
  ]

class MSR_HASWELL_CONFIG_TDP_LEVEL1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_CONFIG_TDP_LEVEL1_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_CONFIG_TDP_LEVEL2  = 0x0000064A

class MSR_HASWELL_CONFIG_TDP_LEVEL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PKG_TDP_LVL2",            UINT32, 15),
    ("Reserved1",               UINT32, 1),
    ("Config_TDP_LVL2_Ratio",   UINT32, 8),
    ("Reserved2",               UINT32, 8),
    ("PKG_MAX_PWR_LVL2",        UINT32, 15),
    ("PKG_MIN_PWR_LVL2",        UINT32, 16),
    ("Reserved3",               UINT32, 1)
  ]

class MSR_HASWELL_CONFIG_TDP_LEVEL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_CONFIG_TDP_LEVEL2_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_CONFIG_TDP_CONTROL  = 0x0000064B

class MSR_HASWELL_CONFIG_TDP_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TDP_LEVEL",       UINT32, 2),
    ("Reserved1",       UINT32, 29),
    ("Config_TDP_Lock", UINT32, 1),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_HASWELL_CONFIG_TDP_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_CONFIG_TDP_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_TURBO_ACTIVATION_RATIO  = 0x0000064C

class MSR_HASWELL_TURBO_ACTIVATION_RATIO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_NON_TURBO_RATIO",         UINT32, 8),
    ("Reserved1",                   UINT32, 23),
    ("TURBO_ACTIVATION_RATIO_Lock", UINT32, 1),
    ("Reserved2",                   UINT32, 32)
  ]

class MSR_HASWELL_TURBO_ACTIVATION_RATIO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_TURBO_ACTIVATION_RATIO_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_HASWELL_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",           UINT32, 4),
    ("Reserved1",       UINT32, 6),
    ("IO_MWAIT",        UINT32, 1),
    ("Reserved2",       UINT32, 4),
    ("CFGLock",         UINT32, 1),
    ("Reserved3",       UINT32, 9),
    ("C3AutoDemotion",  UINT32, 1),
    ("C1AutoDemotion",  UINT32, 1),
    ("C3Undemotion",    UINT32, 1),
    ("C1Undemotion",    UINT32, 1),
    ("Reserved4",       UINT32, 3),
    ("Reserved5",       UINT32, 32)
  ]

class MSR_HASWELL_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_SMM_MCA_CAP  = 0x0000017D

class MSR_HASWELL_SMM_MCA_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 32),
    ("Reserved2",               UINT32, 26),
    ("SMM_Code_Access_Chk",     UINT32, 1),
    ("Long_Flow_Indication",    UINT32, 1),
    ("Reserved3",               UINT32, 4)
  ]

class MSR_HASWELL_SMM_MCA_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_SMM_MCA_CAP_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_HASWELL_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Maximum1C", UINT32, 8),
    ("Maximum2C", UINT32, 8),
    ("Maximum3C", UINT32, 8),
    ("Maximum4C", UINT32, 8),
    ("Reserved",  UINT32, 32)
  ]

class MSR_HASWELL_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_PERF_GLOBAL_CTRL  = 0x00000391

class MSR_HASWELL_UNC_PERF_GLOBAL_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PMI_Sel_Core0",   UINT32, 1),
    ("PMI_Sel_Core1",   UINT32, 1),
    ("PMI_Sel_Core2",   UINT32, 1),
    ("PMI_Sel_Core3",   UINT32, 1),
    ("Reserved1",       UINT32, 15),
    ("Reserved2",       UINT32, 10),
    ("EN",              UINT32, 1),
    ("WakePMI",         UINT32, 1),
    ("FREEZE",          UINT32, 1),
    ("Reserved3",       UINT32, 32)
  ]

class MSR_HASWELL_UNC_PERF_GLOBAL_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_UNC_PERF_GLOBAL_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_PERF_GLOBAL_STATUS  = 0x00000392

class MSR_HASWELL_UNC_PERF_GLOBAL_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Fixed",       UINT32, 1),
    ("ARB",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("CBox",        UINT32, 1),
    ("Reserved2",   UINT32, 28),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_HASWELL_UNC_PERF_GLOBAL_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_UNC_PERF_GLOBAL_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_PERF_FIXED_CTRL  = 0x00000394

class MSR_HASWELL_UNC_PERF_FIXED_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",       UINT32, 20),
    ("EnableOverflow",  UINT32, 1),
    ("Reserved2",       UINT32, 1),
    ("EnableCounting",  UINT32, 1),
    ("Reserved3",       UINT32, 9),
    ("Reserved4",       UINT32, 32)
  ]

class MSR_HASWELL_UNC_PERF_FIXED_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_UNC_PERF_FIXED_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_PERF_FIXED_CTR  = 0x00000395

class MSR_HASWELL_UNC_PERF_FIXED_CTR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CurrentCount",    UINT32, 32),
    ("CurrentCountHi",  UINT32, 16),
    ("Reserved",        UINT32, 16)
  ]

class MSR_HASWELL_UNC_PERF_FIXED_CTR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_UNC_PERF_FIXED_CTR_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_CBO_CONFIG  = 0x00000396

class MSR_HASWELL_UNC_CBO_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CBox",        UINT32, 4),
    ("Reserved1",   UINT32, 28),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_HASWELL_UNC_CBO_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_UNC_CBO_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_ARB_PERFCTR0  = 0x000003B0

MSR_HASWELL_UNC_ARB_PERFCTR1  = 0x000003B1

MSR_HASWELL_UNC_ARB_PERFEVTSEL0  = 0x000003B2

MSR_HASWELL_UNC_ARB_PERFEVTSEL1  = 0x000003B3

MSR_HASWELL_SMM_FEATURE_CONTROL  = 0x000004E0

class MSR_HASWELL_SMM_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",            UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("SMM_Code_Chk_En", UINT32, 1),
    ("Reserved2",       UINT32, 29),
    ("Reserved3",       UINT32, 32)
  ]

class MSR_HASWELL_SMM_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_SMM_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_SMM_DELAYED     = 0x000004E2

MSR_HASWELL_SMM_BLOCKED     = 0x000004E3

MSR_HASWELL_RAPL_POWER_UNIT = 0x00000606

class MSR_HASWELL_RAPL_POWER_UNIT_REGISTER_Bits (Structure):
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

class MSR_HASWELL_RAPL_POWER_UNIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_RAPL_POWER_UNIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PP0_ENERGY_STATUS   = 0x00000639

MSR_HASWELL_PP1_POWER_LIMIT     = 0x00000640

MSR_HASWELL_PP1_ENERGY_STATUS   = 0x00000641

MSR_HASWELL_PP1_POLICY          = 0x00000642

MSR_HASWELL_CORE_PERF_LIMIT_REASONS = 0x00000690

class MSR_HASWELL_CORE_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                                  UINT32, 1),
    ("ThermalStatus",                                   UINT32, 1),
    ("Reserved1",                                       UINT32, 2),
    ("GraphicsDriverStatus",                            UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlStatus",UINT32, 1),
    ("VRThermAlertStatus",                              UINT32, 1),
    ("Reserved2",                                       UINT32, 1),
    ("ElectricalDesignPointStatus",                     UINT32, 1),
    ("PLStatus",                                        UINT32, 1),
    ("PL1Status",                                       UINT32, 1),
    ("PL2Status",                                       UINT32, 1),
    ("MaxTurboLimitStatus",                             UINT32, 1),
    ("TurboTransitionAttenuationStatus",                UINT32, 1),
    ("Reserved3",                                       UINT32, 2),
    ("PROCHOT_Log",                                     UINT32, 1),
    ("ThermalLog",                                      UINT32, 1),
    ("Reserved4",                                       UINT32, 2),
    ("GraphicsDriverLog",                               UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlLog",   UINT32, 1),
    ("VRThermAlertLog",                                 UINT32, 1),
    ("Reserved5",                                       UINT32, 1),
    ("ElectricalDesignPointLog",                        UINT32, 1),
    ("PLLog",                                           UINT32, 1),
    ("PL1Log",                                          UINT32, 1),
    ("PL2Log",                                          UINT32, 1),
    ("MaxTurboLimitLog",                                UINT32, 1),
    ("TurboTransitionAttenuationLog",                   UINT32, 1),
    ("Reserved6",                                       UINT32, 2),
    ("Reserved7",                                       UINT32, 32)
  ]

class MSR_HASWELL_CORE_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_CORE_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_GRAPHICS_PERF_LIMIT_REASONS  = 0x000006B0

class MSR_HASWELL_GRAPHICS_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                                      UINT32, 1),
    ("ThermalStatus",                                       UINT32, 1),
    ("Reserved1",                                           UINT32, 2),
    ("GraphicsDriverStatus",                                UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlStatus",    UINT32, 1),
    ("VRThermAlertStatus",                                  UINT32, 1),
    ("Reserved2",                                           UINT32, 1),
    ("ElectricalDesignPointStatus",                         UINT32, 1),
    ("GraphicsPowerLimitingStatus",                         UINT32, 1),
    ("PL1STatus",                                           UINT32, 1),
    ("PL2Status",                                           UINT32, 1),
    ("Reserved3",                                           UINT32, 4),
    ("PROCHOT_Log",                                         UINT32, 1),
    ("ThermalLog",                                          UINT32, 1),
    ("Reserved4",                                           UINT32, 2),
    ("GraphicsDriverLog",                                   UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlLog",       UINT32, 1),
    ("VRThermAlertLog",                                     UINT32, 1),
    ("Reserved5",                                           UINT32, 1),
    ("ElectricalDesignPointLog",                            UINT32, 1),
    ("CorePowerLimitingLog",                                UINT32, 1),
    ("PL1Log",                                              UINT32, 1),
    ("PL2Log",                                              UINT32, 1),
    ("MaxTurboLimitLog",                                    UINT32, 1),
    ("TurboTransitionAttenuationLog",                       UINT32, 1),
    ("Reserved6",                                           UINT32, 2),
    ("Reserved7",                                           UINT32, 32)
  ]

class MSR_HASWELL_GRAPHICS_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_GRAPHICS_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_RING_PERF_LIMIT_REASONS  = 0x000006B1

class MSR_HASWELL_RING_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                                  UINT32, 1),
    ("ThermalStatus",                                   UINT32, 1),
    ("Reserved1",                                       UINT32, 4),
    ("VRThermAlertStatus",                              UINT32, 1),
    ("Reserved2",                                       UINT32, 1),
    ("ElectricalDesignPointStatus",                     UINT32, 1),
    ("Reserved3",                                       UINT32, 1),
    ("PL1STatus",                                       UINT32, 1),
    ("PL2Status",                                       UINT32, 1),
    ("Reserved4",                                       UINT32, 4),
    ("PROCHOT_Log",                                     UINT32, 1),
    ("ThermalLog",                                      UINT32, 1),
    ("Reserved5",                                       UINT32, 2),
    ("GraphicsDriverLog",                               UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlLog",   UINT32, 1),
    ("VRThermAlertLog",                                 UINT32, 1),
    ("Reserved6",                                       UINT32, 1),
    ("ElectricalDesignPointLog",                        UINT32, 1),
    ("CorePowerLimitingLog",                            UINT32, 1),
    ("PL1Log",                                          UINT32, 1),
    ("PL2Log",                                          UINT32, 1),
    ("MaxTurboLimitLog",                                UINT32, 1),
    ("TurboTransitionAttenuationLog",                   UINT32, 1),
    ("Reserved7",                                       UINT32, 2),
    ("Reserved8",                                       UINT32, 32)
  ]

class MSR_HASWELL_RING_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_RING_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_UNC_CBO_0_PERFEVTSEL0   = 0x00000700
MSR_HASWELL_UNC_CBO_0_PERFEVTSEL1   = 0x00000701
MSR_HASWELL_UNC_CBO_0_PERFCTR0      = 0x00000706
MSR_HASWELL_UNC_CBO_0_PERFCTR1      = 0x00000707
MSR_HASWELL_UNC_CBO_1_PERFEVTSEL0   = 0x00000710
MSR_HASWELL_UNC_CBO_1_PERFEVTSEL1   = 0x00000711
MSR_HASWELL_UNC_CBO_1_PERFCTR0      = 0x00000716
MSR_HASWELL_UNC_CBO_1_PERFCTR1      = 0x00000717
MSR_HASWELL_UNC_CBO_2_PERFEVTSEL0   = 0x00000720
MSR_HASWELL_UNC_CBO_2_PERFEVTSEL1   = 0x00000721
MSR_HASWELL_UNC_CBO_2_PERFCTR0      = 0x00000726
MSR_HASWELL_UNC_CBO_2_PERFCTR1      = 0x00000727
MSR_HASWELL_UNC_CBO_3_PERFEVTSEL0   = 0x00000730
MSR_HASWELL_UNC_CBO_3_PERFEVTSEL1   = 0x00000731
MSR_HASWELL_UNC_CBO_3_PERFCTR0      = 0x00000736
MSR_HASWELL_UNC_CBO_3_PERFCTR1      = 0x00000737

MSR_HASWELL_PKG_C8_RESIDENCY  = 0x00000630

class MSR_HASWELL_PKG_C8_RESIDENCY_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("C8ResidencyCounter",      UINT32, 32),
    ("C8ResidencyCounterHi",    UINT32, 28),
    ("Reserved",                UINT32, 4)
  ]

class MSR_HASWELL_PKG_C8_RESIDENCY_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PKG_C8_RESIDENCY_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PKG_C9_RESIDENCY  = 0x00000631

class MSR_HASWELL_PKG_C9_RESIDENCY_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("C9ResidencyCounter",      UINT32, 32),
    ("C9ResidencyCounterHi",    UINT32, 28),
    ("Reserved",                UINT32, 4)
  ]

class MSR_HASWELL_PKG_C9_RESIDENCY_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PKG_C9_RESIDENCY_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_HASWELL_PKG_C10_RESIDENCY  = 0x00000632

class MSR_HASWELL_PKG_C10_RESIDENCY_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("C10ResidencyCounter",     UINT32, 32),
    ("C10ResidencyCounterHi",   UINT32, 28),
    ("Reserved",                UINT32, 4)
  ]

class MSR_HASWELL_PKG_C10_RESIDENCY_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_HASWELL_PKG_C10_RESIDENCY_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]
