# IvyBridgeMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.IvyBridgeMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_IVY_BRIDGE_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x3A or
           DisplayModel == 0x3E
           )

MSR_IVY_BRIDGE_PLATFORM_INFO  = 0x000000CE

class MSR_IVY_BRIDGE_PLATFORM_INFO_REGISTER_Bits (Structure):
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

class MSR_IVY_BRIDGE_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_PLATFORM_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_IVY_BRIDGE_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",           UINT32, 3),
    ("Reserved1",       UINT32, 7),
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

class MSR_IVY_BRIDGE_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_PP0_ENERGY_STATUS  = 0x00000639

MSR_IVY_BRIDGE_CONFIG_TDP_NOMINAL  = 0x00000648

class MSR_IVY_BRIDGE_CONFIG_TDP_NOMINAL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Config_TDP_Base", UINT32, 8),
    ("Reserved1",       UINT32, 24),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IVY_BRIDGE_CONFIG_TDP_NOMINAL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_CONFIG_TDP_NOMINAL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL1  = 0x00000649

class MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PKG_TDP_LVL1",            UINT32, 15),
    ("Reserved1",               UINT32, 1),
    ("Config_TDP_LVL1_Ratio",   UINT32, 8),
    ("Reserved2",               UINT32, 8),
    ("PKG_MAX_PWR_LVL1",        UINT32, 15),
    ("Reserved3",               UINT32, 1),
    ("PKG_MIN_PWR_LVL1",        UINT32, 15),
    ("Reserved4",               UINT32, 1)
  ]

class MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL1_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL2  = 0x0000064A

class MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PKG_TDP_LVL2",            UINT32, 15),
    ("Reserved1",               UINT32, 1),
    ("Config_TDP_LVL2_Ratio",   UINT32, 8),
    ("Reserved2",               UINT32, 8),
    ("PKG_MAX_PWR_LVL2",        UINT32, 15),
    ("Reserved3",               UINT32, 1),
    ("PKG_MIN_PWR_LVL2",        UINT32, 15),
    ("Reserved4",               UINT32, 1)
  ]

class MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_CONFIG_TDP_LEVEL2_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_CONFIG_TDP_CONTROL  = 0x0000064B

class MSR_IVY_BRIDGE_CONFIG_TDP_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TDP_LEVEL",       UINT32, 2),
    ("Reserved1",       UINT32, 29),
    ("Config_TDP_Lock", UINT32, 1),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IVY_BRIDGE_CONFIG_TDP_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_CONFIG_TDP_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_TURBO_ACTIVATION_RATIO  = 0x0000064C

class MSR_IVY_BRIDGE_TURBO_ACTIVATION_RATIO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_NON_TURBO_RATIO",         UINT32, 8),
    ("Reserved1",                   UINT32, 23),
    ("TURBO_ACTIVATION_RATIO_Lock", UINT32, 1),
    ("Reserved2",                   UINT32, 32)
  ]

class MSR_IVY_BRIDGE_TURBO_ACTIVATION_RATIO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_TURBO_ACTIVATION_RATIO_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_PPIN_CTL  = 0x0000004E

class MSR_IVY_BRIDGE_PPIN_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LockOut     ", UINT32, 1),
    ("Enable_PPIN ", UINT32, 1),
    ("Reserved1   ", UINT32, 30),
    ("Reserved2   ", UINT32, 32)
  ]

class MSR_IVY_BRIDGE_PPIN_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_PPIN_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

class MSR_IVY_BRIDGE_PLATFORM_INFO_1_REGISTER_Bits (Structure):
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

class MSR_IVY_BRIDGE_PLATFORM_INFO_1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_PLATFORM_INFO_1_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_ERROR_CONTROL  = 0x0000017F

class MSR_IVY_BRIDGE_ERROR_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 1),
    ("MemErrorLogEnable",   UINT32, 1),
    ("Reserved2",           UINT32, 30),
    ("Reserved3",           UINT32, 32)
  ]

class MSR_IVY_BRIDGE_ERROR_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_ERROR_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_TEMPERATURE_TARGET  = 0x000001A2

class MSR_IVY_BRIDGE_TEMPERATURE_TARGET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 16),
    ("TemperatureTarget",   UINT32, 8),
    ("TCCActivationOffset", UINT32, 4),
    ("Reserved2",           UINT32, 4),
    ("Reserved3",           UINT32, 32)
  ]

class MSR_IVY_BRIDGE_TEMPERATURE_TARGET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_TEMPERATURE_TARGET_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_TURBO_RATIO_LIMIT1  = 0x000001AE

class MSR_IVY_BRIDGE_TURBO_RATIO_LIMIT1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Maximum9C",                               UINT32, 8),
    ("Maximum10C",                              UINT32, 8),
    ("Maximum11C",                              UINT32, 8),
    ("Maximum12C",                              UINT32, 8),
    ("Maximum13C",                              UINT32, 8),
    ("Maximum14C",                              UINT32, 8),
    ("Maximum15C",                              UINT32, 8),
    ("Reserved",                                UINT32, 7),
    ("TurboRatioLimitConfigurationSemaphore",   UINT32, 1)
  ]

class MSR_IVY_BRIDGE_TURBO_RATIO_LIMIT1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_TURBO_RATIO_LIMIT1_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_IA32_MC6_MISC  = 0x0000041B

class MSR_IVY_BRIDGE_IA32_MC6_MISC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("RecoverableAddressLSB",   UINT32, 6),
    ("AddressMode",             UINT32, 3),
    ("Reserved1",               UINT32, 7),
    ("PCIExpressRequestorID",   UINT32, 16),
    ("PCIExpressSegmentNumber", UINT32, 8),
    ("Reserved2",               UINT32, 24)
  ]

class MSR_IVY_BRIDGE_IA32_MC6_MISC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_IA32_MC6_MISC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_IA32_MC29_CTL  = 0x00000474
MSR_IVY_BRIDGE_IA32_MC30_CTL  = 0x00000478
MSR_IVY_BRIDGE_IA32_MC31_CTL  = 0x0000047C

MSR_IVY_BRIDGE_IA32_MC29_STATUS  = 0x00000475
MSR_IVY_BRIDGE_IA32_MC30_STATUS  = 0x00000479
MSR_IVY_BRIDGE_IA32_MC31_STATUS  = 0x0000047D

MSR_IVY_BRIDGE_IA32_MC29_ADDR  = 0x00000476
MSR_IVY_BRIDGE_IA32_MC30_ADDR  = 0x0000047A
MSR_IVY_BRIDGE_IA32_MC31_ADDR  = 0x0000047E

MSR_IVY_BRIDGE_IA32_MC29_MISC  = 0x00000477
MSR_IVY_BRIDGE_IA32_MC30_MISC  = 0x0000047B
MSR_IVY_BRIDGE_IA32_MC31_MISC  = 0x0000047F

MSR_IVY_BRIDGE_PKG_PERF_STATUS = 0x00000613

MSR_IVY_BRIDGE_DRAM_POWER_LIMIT     = 0x00000618
MSR_IVY_BRIDGE_DRAM_ENERGY_STATUS   = 0x00000619
MSR_IVY_BRIDGE_DRAM_PERF_STATUS     = 0x0000061B
MSR_IVY_BRIDGE_DRAM_POWER_INFO      = 0x0000061C

MSR_IVY_BRIDGE_PEBS_ENABLE  = 0x000003F1

class MSR_IVY_BRIDGE_PEBS_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PEBS_EN_PMC0",    UINT32, 1),
    ("PEBS_EN_PMC1",    UINT32, 1),
    ("PEBS_EN_PMC2",    UINT32, 1),
    ("PEBS_EN_PMC3",    UINT32, 1),
    ("Reserved1",       UINT32, 28),
    ("LL_EN_PMC0",      UINT32, 1),
    ("LL_EN_PMC1",      UINT32, 1),
    ("LL_EN_PMC2",      UINT32, 1),
    ("LL_EN_PMC3",      UINT32, 1),
    ("Reserved2",       UINT32, 28)
  ]

class MSR_IVY_BRIDGE_PEBS_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IVY_BRIDGE_PEBS_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IVY_BRIDGE_PMON_GLOBAL_CTL      = 0x00000C00
MSR_IVY_BRIDGE_PMON_GLOBAL_STATUS   = 0x00000C01
MSR_IVY_BRIDGE_PMON_GLOBAL_CONFIG   = 0x00000C06
MSR_IVY_BRIDGE_U_PMON_BOX_STATUS    = 0x00000C15
MSR_IVY_BRIDGE_PCU_PMON_BOX_STATUS  = 0x00000C35

MSR_IVY_BRIDGE_C0_PMON_BOX_FILTER1  = 0x00000D1A

MSR_IVY_BRIDGE_C1_PMON_BOX_FILTER1  = 0x00000D3A

MSR_IVY_BRIDGE_C2_PMON_BOX_FILTER1  = 0x00000D5A

MSR_IVY_BRIDGE_C3_PMON_BOX_FILTER1  = 0x00000D7A

MSR_IVY_BRIDGE_C4_PMON_BOX_FILTER1  = 0x00000D9A

MSR_IVY_BRIDGE_C5_PMON_BOX_FILTER1  = 0x00000DBA

MSR_IVY_BRIDGE_C6_PMON_BOX_FILTER1  = 0x00000DDA

MSR_IVY_BRIDGE_C7_PMON_BOX_FILTER1  = 0x00000DFA

MSR_IVY_BRIDGE_C8_PMON_BOX_CTL      = 0x00000E04
MSR_IVY_BRIDGE_C8_PMON_EVNTSEL0     = 0x00000E10
MSR_IVY_BRIDGE_C8_PMON_EVNTSEL1     = 0x00000E11
MSR_IVY_BRIDGE_C8_PMON_EVNTSEL2     = 0x00000E12
MSR_IVY_BRIDGE_C8_PMON_EVNTSEL3     = 0x00000E13
MSR_IVY_BRIDGE_C8_PMON_BOX_FILTER   = 0x00000E14
MSR_IVY_BRIDGE_C8_PMON_CTR0         = 0x00000E16
MSR_IVY_BRIDGE_C8_PMON_CTR1         = 0x00000E17
MSR_IVY_BRIDGE_C8_PMON_CTR2         = 0x00000E18
MSR_IVY_BRIDGE_C8_PMON_CTR3         = 0x00000E19
MSR_IVY_BRIDGE_C8_PMON_BOX_FILTER1  = 0x00000E1A

MSR_IVY_BRIDGE_C9_PMON_BOX_CTL      = 0x00000E24
MSR_IVY_BRIDGE_C9_PMON_EVNTSEL0     = 0x00000E30
MSR_IVY_BRIDGE_C9_PMON_EVNTSEL1     = 0x00000E31
MSR_IVY_BRIDGE_C9_PMON_EVNTSEL2     = 0x00000E32
MSR_IVY_BRIDGE_C9_PMON_EVNTSEL3     = 0x00000E33
MSR_IVY_BRIDGE_C9_PMON_BOX_FILTER   = 0x00000E34
MSR_IVY_BRIDGE_C9_PMON_CTR0         = 0x00000E36
MSR_IVY_BRIDGE_C9_PMON_CTR1         = 0x00000E37
MSR_IVY_BRIDGE_C9_PMON_CTR2         = 0x00000E38
MSR_IVY_BRIDGE_C9_PMON_CTR3         = 0x00000E39
MSR_IVY_BRIDGE_C9_PMON_BOX_FILTER1  = 0x00000E3A

MSR_IVY_BRIDGE_C10_PMON_BOX_CTL     = 0x00000E44
MSR_IVY_BRIDGE_C10_PMON_EVNTSEL0    = 0x00000E50
MSR_IVY_BRIDGE_C10_PMON_EVNTSEL1    = 0x00000E51
MSR_IVY_BRIDGE_C10_PMON_EVNTSEL2    = 0x00000E52
MSR_IVY_BRIDGE_C10_PMON_EVNTSEL3    = 0x00000E53
MSR_IVY_BRIDGE_C10_PMON_BOX_FILTER  = 0x00000E54
MSR_IVY_BRIDGE_C10_PMON_CTR0        = 0x00000E56
MSR_IVY_BRIDGE_C10_PMON_CTR1        = 0x00000E57
MSR_IVY_BRIDGE_C10_PMON_CTR2        = 0x00000E58
MSR_IVY_BRIDGE_C10_PMON_CTR3        = 0x00000E59
MSR_IVY_BRIDGE_C10_PMON_BOX_FILTER1 = 0x00000E5A

MSR_IVY_BRIDGE_C11_PMON_BOX_CTL     = 0x00000E64
MSR_IVY_BRIDGE_C11_PMON_EVNTSEL0    = 0x00000E70
MSR_IVY_BRIDGE_C11_PMON_EVNTSEL1    = 0x00000E71
MSR_IVY_BRIDGE_C11_PMON_EVNTSEL2    = 0x00000E72
MSR_IVY_BRIDGE_C11_PMON_EVNTSEL3    = 0x00000E73
MSR_IVY_BRIDGE_C11_PMON_BOX_FILTER  = 0x00000E74
MSR_IVY_BRIDGE_C11_PMON_CTR0        = 0x00000E76
MSR_IVY_BRIDGE_C11_PMON_CTR1        = 0x00000E77
MSR_IVY_BRIDGE_C11_PMON_CTR2        = 0x00000E78
MSR_IVY_BRIDGE_C11_PMON_CTR3        = 0x00000E79
MSR_IVY_BRIDGE_C11_PMON_BOX_FILTER1 = 0x00000E7A

MSR_IVY_BRIDGE_C12_PMON_BOX_CTL     = 0x00000E84
MSR_IVY_BRIDGE_C12_PMON_EVNTSEL0    = 0x00000E90
MSR_IVY_BRIDGE_C12_PMON_EVNTSEL1    = 0x00000E91
MSR_IVY_BRIDGE_C12_PMON_EVNTSEL2    = 0x00000E92
MSR_IVY_BRIDGE_C12_PMON_EVNTSEL3    = 0x00000E93
MSR_IVY_BRIDGE_C12_PMON_BOX_FILTER  = 0x00000E94
MSR_IVY_BRIDGE_C12_PMON_CTR0        = 0x00000E96
MSR_IVY_BRIDGE_C12_PMON_CTR1        = 0x00000E97
MSR_IVY_BRIDGE_C12_PMON_CTR2        = 0x00000E98
MSR_IVY_BRIDGE_C12_PMON_CTR3        = 0x00000E99
MSR_IVY_BRIDGE_C12_PMON_BOX_FILTER1 = 0x00000E9A

MSR_IVY_BRIDGE_C13_PMON_BOX_CTL     = 0x00000EA4
MSR_IVY_BRIDGE_C13_PMON_EVNTSEL0    = 0x00000EB0
MSR_IVY_BRIDGE_C13_PMON_EVNTSEL1    = 0x00000EB1
MSR_IVY_BRIDGE_C13_PMON_EVNTSEL2    = 0x00000EB2
MSR_IVY_BRIDGE_C13_PMON_EVNTSEL3    = 0x00000EB3
MSR_IVY_BRIDGE_C13_PMON_BOX_FILTER  = 0x00000EB4
MSR_IVY_BRIDGE_C13_PMON_CTR0        = 0x00000EB6
MSR_IVY_BRIDGE_C13_PMON_CTR1        = 0x00000EB7
MSR_IVY_BRIDGE_C13_PMON_CTR2        = 0x00000EB8
MSR_IVY_BRIDGE_C13_PMON_CTR3        = 0x00000EB9
MSR_IVY_BRIDGE_C13_PMON_BOX_FILTER1 = 0x00000EBA

MSR_IVY_BRIDGE_C14_PMON_BOX_CTL     = 0x00000EC4
MSR_IVY_BRIDGE_C14_PMON_EVNTSEL0    = 0x00000ED0
MSR_IVY_BRIDGE_C14_PMON_EVNTSEL1    = 0x00000ED1
MSR_IVY_BRIDGE_C14_PMON_EVNTSEL2    = 0x00000ED2
MSR_IVY_BRIDGE_C14_PMON_EVNTSEL3    = 0x00000ED3
MSR_IVY_BRIDGE_C14_PMON_BOX_FILTER  = 0x00000ED4
MSR_IVY_BRIDGE_C14_PMON_CTR0        = 0x00000ED6
MSR_IVY_BRIDGE_C14_PMON_CTR1        = 0x00000ED7
MSR_IVY_BRIDGE_C14_PMON_CTR2        = 0x00000ED8
MSR_IVY_BRIDGE_C14_PMON_CTR3        = 0x00000ED9
MSR_IVY_BRIDGE_C14_PMON_BOX_FILTER1 = 0x00000EDA
