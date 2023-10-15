# SilvermontMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.SilvermontMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_SILVERMONT_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x37 or
           DisplayModel == 0x4A or
           DisplayModel == 0x4D or
           DisplayModel == 0x5A or
           DisplayModel == 0x5D
           )

MSR_SILVERMONT_PLATFORM_ID  = 0x00000017

class MSR_SILVERMONT_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumQualifiedRatio",   UINT32, 5),
    ("Reserved2",               UINT32, 19),
    ("Reserved3",               UINT32, 18),
    ("PlatformId",              UINT32, 3),
    ("Reserved4",               UINT32, 11)
  ]

class MSR_SILVERMONT_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PLATFORM_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_EBL_CR_POWERON  = 0x0000002A

class MSR_SILVERMONT_EBL_CR_POWERON_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 32),
    ("Reserved2",   UINT32, 32),
  ]

class MSR_SILVERMONT_EBL_CR_POWERON_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_EBL_CR_POWERON_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_SMI_COUNT  = 0x00000034

class MSR_SILVERMONT_SMI_COUNT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SMICount",    UINT32, 32),
    ("Reserved",    UINT32, 32),
  ]

class MSR_SILVERMONT_SMI_COUNT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_SMI_COUNT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_IA32_FEATURE_CONTROL  = 0x0000003A

class MSR_SILVERMONT_IA32_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",                UINT32, 1),
    ("Reserved1",           UINT32, 1),
    ("EnableVmxOutsideSmx", UINT32, 1),
    ("Reserved2",           UINT32, 29),
    ("Reserved3",           UINT32, 32),
  ]

class MSR_SILVERMONT_IA32_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_IA32_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_LASTBRANCH_0_FROM_IP  = 0x00000040
MSR_SILVERMONT_LASTBRANCH_1_FROM_IP  = 0x00000041
MSR_SILVERMONT_LASTBRANCH_2_FROM_IP  = 0x00000042
MSR_SILVERMONT_LASTBRANCH_3_FROM_IP  = 0x00000043
MSR_SILVERMONT_LASTBRANCH_4_FROM_IP  = 0x00000044
MSR_SILVERMONT_LASTBRANCH_5_FROM_IP  = 0x00000045
MSR_SILVERMONT_LASTBRANCH_6_FROM_IP  = 0x00000046
MSR_SILVERMONT_LASTBRANCH_7_FROM_IP  = 0x00000047

MSR_SILVERMONT_LASTBRANCH_0_TO_IP  = 0x00000060
MSR_SILVERMONT_LASTBRANCH_1_TO_IP  = 0x00000061
MSR_SILVERMONT_LASTBRANCH_2_TO_IP  = 0x00000062
MSR_SILVERMONT_LASTBRANCH_3_TO_IP  = 0x00000063
MSR_SILVERMONT_LASTBRANCH_4_TO_IP  = 0x00000064
MSR_SILVERMONT_LASTBRANCH_5_TO_IP  = 0x00000065
MSR_SILVERMONT_LASTBRANCH_6_TO_IP  = 0x00000066
MSR_SILVERMONT_LASTBRANCH_7_TO_IP  = 0x00000067

MSR_SILVERMONT_FSB_FREQ  = 0x000000CD

class MSR_SILVERMONT_FSB_FREQ_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ScalableBusSpeed",    UINT32, 4),
    ("Reserved1",           UINT32, 28),
    ("Reserved2",           UINT32, 32),
  ]

class MSR_SILVERMONT_FSB_FREQ_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_FSB_FREQ_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PLATFORM_INFO  = 0x000000CE

class MSR_SILVERMONT_PLATFORM_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumNon_TurboRatio",   UINT32, 8),
    ("Reserved2",               UINT32, 16),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_SILVERMONT_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PLATFORM_INFO_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_SILVERMONT_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",       UINT32, 3),
    ("Reserved1",   UINT32, 7),
    ("IO_MWAIT",    UINT32, 1),
    ("Reserved2",   UINT32, 4),
    ("CFGLock",     UINT32, 1),
    ("Reserved3",   UINT32, 16),
    ("Reserved4",   UINT32, 32)
  ]

class MSR_SILVERMONT_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PMG_IO_CAPTURE_BASE  = 0x000000E4

class MSR_SILVERMONT_PMG_IO_CAPTURE_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lvl2Base",    UINT32, 16),
    ("CStateRange", UINT32, 3),
    ("Reserved1",   UINT32, 13),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_SILVERMONT_PMG_IO_CAPTURE_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PMG_IO_CAPTURE_BASE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_BBL_CR_CTL3  = 0x0000011E

class MSR_SILVERMONT_BBL_CR_CTL3_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2HardwareEnabled",   UINT32, 1),
    ("Reserved1",           UINT32, 7),
    ("L2Enabled",           UINT32, 1),
    ("Reserved2",           UINT32, 14),
    ("L2NotPresent",        UINT32, 1),
    ("Reserved3",           UINT32, 8),
    ("Reserved4",           UINT32, 32)
  ]

class MSR_SILVERMONT_BBL_CR_CTL3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_BBL_CR_CTL3_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_FEATURE_CONFIG  = 0x0000013C

class MSR_SILVERMONT_FEATURE_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("AESConfiguration",    UINT32, 2),
    ("Reserved1",           UINT32, 30),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_SILVERMONT_FEATURE_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_FEATURE_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_IA32_MISC_ENABLE  = 0x000001A0

class MSR_SILVERMONT_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
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

class MSR_SILVERMONT_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_TEMPERATURE_TARGET  = 0x000001A2

class MSR_SILVERMONT_TEMPERATURE_TARGET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 16),
    ("TemperatureTarget",   UINT32, 8),
    ("TargetOffset",        UINT32, 6),
    ("Reserved2",           UINT32, 2),
    ("Reserved3",           UINT32, 32)
  ]

class MSR_SILVERMONT_TEMPERATURE_TARGET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_TEMPERATURE_TARGET_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_MISC_FEATURE_CONTROL  = 0x000001A4

class MSR_SILVERMONT_MISC_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2HardwarePrefetcherDisable",     UINT32, 1),
    ("Reserved1",                       UINT32, 1),
    ("DCUHardwarePrefetcherDisable",    UINT32, 1),
    ("Reserved2",                       UINT32, 29),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_SILVERMONT_MISC_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_MISC_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_OFFCORE_RSP_0  = 0x000001A6

MSR_SILVERMONT_OFFCORE_RSP_1  = 0x000001A7

MSR_SILVERMONT_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_SILVERMONT_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
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

class MSR_SILVERMONT_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_LBR_SELECT  = 0x000001C8

class MSR_SILVERMONT_LBR_SELECT_REGISTER_Bits (Structure):
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

class MSR_SILVERMONT_LBR_SELECT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_LBR_SELECT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_LASTBRANCH_TOS  = 0x000001C9

MSR_SILVERMONT_LER_FROM_LIP  = 0x000001DD

MSR_SILVERMONT_LER_TO_LIP  = 0x000001DE

MSR_SILVERMONT_PEBS_ENABLE  = 0x000003F1

class MSR_SILVERMONT_PEBS_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PEBS",        UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_SILVERMONT_PEBS_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PEBS_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PKG_C6_RESIDENCY  = 0x000003FA

MSR_SILVERMONT_CORE_C6_RESIDENCY  = 0x000003FD

MSR_SILVERMONT_IA32_VMX_EPT_VPID_ENUM  = 0x0000048C

MSR_SILVERMONT_IA32_VMX_FMFUNC  = 0x00000491

MSR_SILVERMONT_CORE_C1_RESIDENCY  = 0x00000660

MSR_SILVERMONT_RAPL_POWER_UNIT  = 0x00000606

class MSR_SILVERMONT_RAPL_POWER_UNIT_REGISTER_Bits (Structure):
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

class MSR_SILVERMONT_RAPL_POWER_UNIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_RAPL_POWER_UNIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PKG_POWER_LIMIT  = 0x00000610

class MSR_SILVERMONT_PKG_POWER_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",           UINT32, 15),
    ("Enable",          UINT32, 1),
    ("ClampingLimit",   UINT32, 1),
    ("Time",            UINT32, 7),
    ("Reserved1",       UINT32, 8),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_SILVERMONT_PKG_POWER_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PKG_POWER_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PKG_ENERGY_STATUS  = 0x00000611

MSR_SILVERMONT_PP0_ENERGY_STATUS  = 0x00000639

MSR_SILVERMONT_CC6_DEMOTION_POLICY_CONFIG  = 0x00000668

MSR_SILVERMONT_MC6_DEMOTION_POLICY_CONFIG  = 0x00000669

MSR_SILVERMONT_MC6_RESIDENCY_COUNTER  = 0x00000664

MSR_SILVERMONT_PKG_POWER_INFO  = 0x0000066E

class MSR_SILVERMONT_PKG_POWER_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ThermalSpecPower",    UINT32, 15),
    ("Reserved1",           UINT32, 17),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_SILVERMONT_PKG_POWER_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PKG_POWER_INFO_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SILVERMONT_PP0_POWER_LIMIT  = 0x00000638

class MSR_SILVERMONT_PP0_POWER_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",       UINT32, 15),
    ("Enable",      UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("Time",        UINT32, 7),
    ("Reserved2",   UINT32, 8),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_SILVERMONT_PP0_POWER_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SILVERMONT_PP0_POWER_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]
