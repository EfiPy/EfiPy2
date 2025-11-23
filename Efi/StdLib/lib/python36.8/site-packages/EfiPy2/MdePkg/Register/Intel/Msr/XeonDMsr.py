# XeonDMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.XeonDMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_XEON_D_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x4F or
           DisplayModel == 0x56
           )

MSR_XEON_D_PPIN_CTL  = 0x0000004E

class MSR_XEON_D_PPIN_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LockOut",     UINT32, 1),
    ("Enable_PPIN", UINT32, 1),
    ("Reserved1",   UINT32, 30),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_XEON_D_PPIN_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_PPIN_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_PPIN  = 0x0000004F

MSR_XEON_D_PLATFORM_INFO  = 0x000000CE

class MSR_XEON_D_PLATFORM_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumNonTurboRatio",    UINT32, 8),
    ("Reserved2",               UINT32, 7),
    ("PPIN_CAP",                UINT32, 1),
    ("Reserved3",               UINT32, 4),
    ("RatioLimit",              UINT32, 1),
    ("TDPLimit",                UINT32, 1),
    ("TJOFFSET",                UINT32, 1),
    ("Reserved4",               UINT32, 1),
    ("Reserved5",               UINT32, 8),
    ("MaximumEfficiencyRatio",  UINT32, 8),
    ("Reserved6",               UINT32, 16)
  ]

class MSR_XEON_D_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_PLATFORM_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_XEON_D_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",               UINT32, 3),
    ("Reserved1",           UINT32, 7),
    ("IO_MWAIT",            UINT32, 1),
    ("Reserved2",           UINT32, 4),
    ("CFGLock",             UINT32, 1),
    ("CStateConversion",    UINT32, 1),
    ("Reserved3",           UINT32, 8),
    ("C3AutoDemotion",      UINT32, 1),
    ("C1AutoDemotion",      UINT32, 1),
    ("C3Undemotion",        UINT32, 1),
    ("C1Undemotion",        UINT32, 1),
    ("CStateDemotion",      UINT32, 1),
    ("CStateUndemotion",    UINT32, 1),
    ("Reserved4",           UINT32, 1),
    ("Reserved5",           UINT32, 32)
  ]

class MSR_XEON_D_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_IA32_MCG_CAP  = 0x00000179

class MSR_XEON_D_IA32_MCG_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Count",       UINT32, 8),
    ("MCG_CTL_P",   UINT32, 1),
    ("MCG_EXT_P",   UINT32, 1),
    ("MCP_CMCI_P",  UINT32, 1),
    ("MCG_TES_P",   UINT32, 1),
    ("Reserved1",   UINT32, 4),
    ("MCG_EXT_CNT", UINT32, 8),
    ("MCG_SER_P",   UINT32, 1),
    ("MCG_EM_P",    UINT32, 1),
    ("MCG_ELOG_P",  UINT32, 1),
    ("Reserved2",   UINT32, 5),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_XEON_D_IA32_MCG_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_IA32_MCG_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_SMM_MCA_CAP  = 0x0000017D

class MSR_XEON_D_SMM_MCA_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 32),
    ("Reserved2",               UINT32, 26),
    ("SMM_Code_Access_Chk",     UINT32, 1),
    ("Long_Flow_Indication",    UINT32, 1),
    ("Reserved3",               UINT32, 4)
  ]

class MSR_XEON_D_SMM_MCA_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_SMM_MCA_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_TEMPERATURE_TARGET  = 0x000001A2

class MSR_XEON_D_TEMPERATURE_TARGET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 16),
    ("TemperatureTarget",   UINT32, 8),
    ("TCCActivationOffset", UINT32, 4),
    ("Reserved2",           UINT32, 4),
    ("Reserved3",           UINT32, 32)
  ]

class MSR_XEON_D_TEMPERATURE_TARGET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_TEMPERATURE_TARGET_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_XEON_D_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Maximum1C", UINT32, 8),
    ("Maximum2C", UINT32, 8),
    ("Maximum3C", UINT32, 8),
    ("Maximum4C", UINT32, 8),
    ("Maximum5C", UINT32, 8),
    ("Maximum6C", UINT32, 8),
    ("Maximum7C", UINT32, 8),
    ("Maximum8C", UINT32, 8)
  ]

class MSR_XEON_D_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_TURBO_RATIO_LIMIT1  = 0x000001AE

class MSR_XEON_D_TURBO_RATIO_LIMIT1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Maximum9C",  UINT32, 8),
    ("Maximum10C", UINT32, 8),
    ("Maximum11C", UINT32, 8),
    ("Maximum12C", UINT32, 8),
    ("Maximum13C", UINT32, 8),
    ("Maximum14C", UINT32, 8),
    ("Maximum15C", UINT32, 8),
    ("Maximum16C", UINT32, 8)
  ]

class MSR_XEON_D_TURBO_RATIO_LIMIT1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_TURBO_RATIO_LIMIT1_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_RAPL_POWER_UNIT  = 0x00000606

class MSR_XEON_D_RAPL_POWER_UNIT_REGISTER_Bits (Structure):
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

class MSR_XEON_D_RAPL_POWER_UNIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_RAPL_POWER_UNIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_DRAM_POWER_LIMIT  = 0x00000618

MSR_XEON_D_DRAM_ENERGY_STATUS  = 0x00000619

class MSR_XEON_D_DRAM_ENERGY_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Energy",      UINT32, 32),
    ("Reserved",    UINT32, 32)
  ]

class MSR_XEON_D_DRAM_ENERGY_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_DRAM_ENERGY_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_DRAM_PERF_STATUS  = 0x0000061B

MSR_XEON_D_DRAM_POWER_INFO  = 0x0000061C

MSR_XEON_D_MSRUNCORE_RATIO_LIMIT  = 0x00000620

class MSR_XEON_D_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_RATIO",    UINT32, 7),
    ("Reserved1",    UINT32, 1),
    ("MIN_RATIO",    UINT32, 7),
    ("Reserved2",    UINT32, 17),
    ("Reserved3",    UINT32, 32)
  ]

class MSR_XEON_D_MSRUNCORE_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_PP0_ENERGY_STATUS  = 0x00000639

MSR_XEON_D_CORE_PERF_LIMIT_REASONS  = 0x00000690

class MSR_XEON_D_CORE_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                                      UINT32, 1),
    ("ThermalStatus",                                       UINT32, 1),
    ("PowerBudgetManagementStatus",                         UINT32, 1),
    ("PlatformConfigurationServicesStatus",                 UINT32, 1),
    ("Reserved1",                                           UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlStatus",    UINT32, 1),
    ("VRThermAlertStatus",                                  UINT32, 1),
    ("Reserved2",                                           UINT32, 1),
    ("ElectricalDesignPointStatus",                         UINT32, 1),
    ("Reserved3",                                           UINT32, 1),
    ("MultiCoreTurboStatus",                                UINT32, 1),
    ("Reserved4",                                           UINT32, 2),
    ("FrequencyP1Status",                                   UINT32, 1),
    ("TurboFrequencyLimitingStatus",                        UINT32, 1),
    ("FrequencyLimitingStatus",                             UINT32, 1),
    ("PROCHOT_Log",                                         UINT32, 1),
    ("ThermalLog",                                          UINT32, 1),
    ("PowerBudgetManagementLog",                            UINT32, 1),
    ("PlatformConfigurationServicesLog",                    UINT32, 1),
    ("Reserved5",                                           UINT32, 1),
    ("AutonomousUtilizationBasedFrequencyControlLog",       UINT32, 1),
    ("VRThermAlertLog",                                     UINT32, 1),
    ("Reserved6",                                           UINT32, 1),
    ("ElectricalDesignPointLog",                            UINT32, 1),
    ("Reserved7",                                           UINT32, 1),
    ("MultiCoreTurboLog",                                   UINT32, 1),
    ("Reserved8",                                           UINT32, 2),
    ("CoreFrequencyP1Log",                                  UINT32, 1),
    ("TurboFrequencyLimitingLog",                           UINT32, 1),
    ("CoreFrequencyLimitingLog",                            UINT32, 1),
    ("Reserved9",                                           UINT32, 32)
  ]

class MSR_XEON_D_CORE_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_CORE_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_IA32_QM_EVTSEL  = 0x00000C8D

class MSR_XEON_D_IA32_QM_EVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventID",     UINT32, 8),
    ("Reserved1",   UINT32, 24),
    ("RMID",        UINT32, 10),
    ("Reserved2",   UINT32, 22)
  ]

class MSR_XEON_D_IA32_QM_EVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_IA32_QM_EVTSEL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_IA32_PQR_ASSOC  = 0x00000C8F

class MSR_XEON_D_IA32_PQR_ASSOC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("RMID",        UINT32, 10),
    ("Reserved1",   UINT32, 22),
    ("COS",         UINT32, 20),
    ("Reserved2",   UINT32, 12)
  ]

class MSR_XEON_D_IA32_PQR_ASSOC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_IA32_PQR_ASSOC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_IA32_L3_QOS_MASK_0   = 0x00000C90
MSR_XEON_D_IA32_L3_QOS_MASK_1   = 0x00000C91
MSR_XEON_D_IA32_L3_QOS_MASK_2   = 0x00000C92
MSR_XEON_D_IA32_L3_QOS_MASK_3   = 0x00000C93
MSR_XEON_D_IA32_L3_QOS_MASK_4   = 0x00000C94
MSR_XEON_D_IA32_L3_QOS_MASK_5   = 0x00000C95
MSR_XEON_D_IA32_L3_QOS_MASK_6   = 0x00000C96
MSR_XEON_D_IA32_L3_QOS_MASK_7   = 0x00000C97
MSR_XEON_D_IA32_L3_QOS_MASK_8   = 0x00000C98
MSR_XEON_D_IA32_L3_QOS_MASK_9   = 0x00000C99
MSR_XEON_D_IA32_L3_QOS_MASK_10  = 0x00000C9A
MSR_XEON_D_IA32_L3_QOS_MASK_11  = 0x00000C9B
MSR_XEON_D_IA32_L3_QOS_MASK_12  = 0x00000C9C
MSR_XEON_D_IA32_L3_QOS_MASK_13  = 0x00000C9D
MSR_XEON_D_IA32_L3_QOS_MASK_14  = 0x00000C9E
MSR_XEON_D_IA32_L3_QOS_MASK_15  = 0x00000C9F

class MSR_XEON_D_IA32_L3_QOS_MASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CBM",         UINT32, 20),
    ("Reserved2",   UINT32, 12),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_XEON_D_IA32_L3_QOS_MASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_IA32_L3_QOS_MASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_TURBO_RATIO_LIMIT3  = 0x000001AC

class MSR_XEON_D_TURBO_RATIO_LIMIT3_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                               UINT32, 32),
    ("Reserved2",                               UINT32, 31),
    ("TurboRatioLimitConfigurationSemaphore",   UINT32, 1)
  ]

class MSR_XEON_D_TURBO_RATIO_LIMIT3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_TURBO_RATIO_LIMIT3_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_D_IA32_L3_QOS_CFG  = 0x00000C81

class MSR_XEON_D_IA32_L3_QOS_CFG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CAT",         UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_XEON_D_IA32_L3_QOS_CFG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_D_IA32_L3_QOS_CFG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]
# 
# #endif
# 