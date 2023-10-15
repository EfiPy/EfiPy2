# Core2Msr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.Core2Msr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_CORE2_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x0F or
           DisplayModel == 0x17
           )

MSR_CORE2_PLATFORM_ID  = 0x00000017

class MSR_CORE2_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumQualifiedRatio",   UINT32, 5),
    ("Reserved2",               UINT32, 19),
    ("Reserved3",               UINT32, 18),
    ("PlatformId",              UINT32, 3),
    ("Reserved4",               UINT32, 11)
  ]

class MSR_CORE2_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_PLATFORM_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_EBL_CR_POWERON  = 0x0000002A

# } MSR_CORE2_EBL_CR_POWERON_REGISTER;
class MSR_CORE2_EBL_CR_POWERON_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                   UINT32, 1),
    ("DataErrorCheckingEnable",     UINT32, 1),
    ("ResponseErrorCheckingEnable", UINT32, 1),
    ("MCERR_DriveEnable",           UINT32, 1),
    ("AddressParityEnable",         UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("Reserved3",                   UINT32, 1),
    ("BINIT_DriverEnable",          UINT32, 1),
    ("OutputTriStateEnable",        UINT32, 1),
    ("ExecuteBIST",                 UINT32, 1),
    ("MCERR_ObservationEnabled",    UINT32, 1),
    ("IntelTXTCapableChipset",      UINT32, 1),
    ("BINIT_ObservationEnabled",    UINT32, 1),
    ("Reserved4",                   UINT32, 1),
    ("ResetVector",                 UINT32, 1),
    ("Reserved5",                   UINT32, 1),
    ("APICClusterID",               UINT32, 2),
    ("NonIntegerBusRatio",          UINT32, 1),
    ("Reserved6",                   UINT32, 1),
    ("SymmetricArbitrationID",      UINT32, 2),
    ("IntegerBusFrequencyRatio",    UINT32, 5),
    ("Reserved7",                   UINT32, 5),
    ("Reserved8",                   UINT32, 32)
  ]

class MSR_CORE2_EBL_CR_POWERON_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_EBL_CR_POWERON_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_FEATURE_CONTROL  = 0x0000003A

class MSR_CORE2_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 3),
    ("SMRREnable",  UINT32, 1),
    ("Reserved2",   UINT32, 28),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_CORE2_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_LASTBRANCH_0_FROM_IP  = 0x00000040
MSR_CORE2_LASTBRANCH_1_FROM_IP  = 0x00000041
MSR_CORE2_LASTBRANCH_2_FROM_IP  = 0x00000042
MSR_CORE2_LASTBRANCH_3_FROM_IP  = 0x00000043

MSR_CORE2_LASTBRANCH_0_TO_IP  = 0x00000060
MSR_CORE2_LASTBRANCH_1_TO_IP  = 0x00000061
MSR_CORE2_LASTBRANCH_2_TO_IP  = 0x00000062
MSR_CORE2_LASTBRANCH_3_TO_IP  = 0x00000063

MSR_CORE2_SMRR_PHYSBASE  = 0x000000A0

class MSR_CORE2_SMRR_PHYSBASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 12),
    ("PhysBase",    UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_CORE2_SMRR_PHYSBASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_SMRR_PHYSBASE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_SMRR_PHYSMASK  = 0x000000A1

class MSR_CORE2_SMRR_PHYSMASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 11),
    ("Valid",       UINT32, 1),
    ("PhysMask",    UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_CORE2_SMRR_PHYSMASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_SMRR_PHYSMASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_FSB_FREQ  = 0x000000CD

class MSR_CORE2_FSB_FREQ_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ScalableBusSpeed",    UINT32, 3),
    ("Reserved1",           UINT32, 29),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_CORE2_FSB_FREQ_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_FSB_FREQ_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_PERF_STATUS  = 0x00000198

class MSR_CORE2_PERF_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CurrentPerformanceStateValue",    UINT32, 16),
    ("Reserved1",                       UINT32, 15),
    ("XEOperation",                     UINT32, 1),
    ("Reserved2",                       UINT32, 8),
    ("MaximumBusRatio",                 UINT32, 5),
    ("Reserved3",                       UINT32, 1),
    ("NonIntegerBusRatio",              UINT32, 1),
    ("Reserved4",                       UINT32, 17)
  ]

class MSR_CORE2_PERF_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_PERF_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_THERM2_CTL  = 0x0000019D

class MSR_CORE2_THERM2_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 16),
    ("TM_SELECT",   UINT32, 1),
    ("Reserved2",   UINT32, 15),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_CORE2_THERM2_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_THERM2_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_IA32_MISC_ENABLE  = 0x000001A0

class MSR_CORE2_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FastStrings",                         UINT32, 1),
    ("Reserved1",                           UINT32, 2),
    ("AutomaticThermalControlCircuit",      UINT32, 1),
    ("Reserved2",                           UINT32, 3),
    ("PerformanceMonitoring",               UINT32, 1),
    ("Reserved3",                           UINT32, 1),
    ("HardwarePrefetcherDisable",           UINT32, 1),
    ("FERR",                                UINT32, 1),
    ("BTS",                                 UINT32, 1),
    ("PEBS",                                UINT32, 1),
    ("TM2",                                 UINT32, 1),
    ("Reserved4",                           UINT32, 2),
    ("EIST",                                UINT32, 1),
    ("Reserved5",                           UINT32, 1),
    ("MONITOR",                             UINT32, 1),
    ("AdjacentCacheLinePrefetchDisable",    UINT32, 1),
    ("EISTLock",                            UINT32, 1),
    ("Reserved6",                           UINT32, 1),
    ("LimitCpuidMaxval",                    UINT32, 1),
    ("xTPR_Message_Disable",                UINT32, 1),
    ("Reserved7",                           UINT32, 8),
    ("Reserved8",                           UINT32, 2),
    ("XD",                                  UINT32, 1),
    ("Reserved9",                           UINT32, 2),
    ("DCUPrefetcherDisable",                UINT32, 1),
    ("IDADisable",                          UINT32, 1),
    ("IPPrefetcherDisable",                 UINT32, 1),
    ("Reserved10",                          UINT32, 24)
  ]

class MSR_CORE2_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_LASTBRANCH_TOS  = 0x000001C9

MSR_CORE2_LER_FROM_LIP  = 0x000001DD

MSR_CORE2_LER_TO_LIP  = 0x000001DE

MSR_CORE2_PERF_FIXED_CTR0  = 0x00000309
MSR_CORE2_PERF_FIXED_CTR1  = 0x0000030A
MSR_CORE2_PERF_FIXED_CTR2  = 0x0000030B

MSR_CORE2_PERF_CAPABILITIES  = 0x00000345

class MSR_CORE2_PERF_CAPABILITIES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LBR_FMT",         UINT32, 6),
    ("PEBS_FMT",        UINT32, 1),
    ("PEBS_ARCH_REG",   UINT32, 1),
    ("Reserved1",       UINT32, 24),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_CORE2_PERF_CAPABILITIES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_PERF_CAPABILITIES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_PERF_FIXED_CTR_CTRL  = 0x0000038D

MSR_CORE2_PERF_GLOBAL_STATUS  = 0x0000038E

MSR_CORE2_PERF_GLOBAL_CTRL  = 0x0000038F

MSR_CORE2_PERF_GLOBAL_OVF_CTRL  = 0x00000390

MSR_CORE2_PEBS_ENABLE  = 0x000003F1

class MSR_CORE2_PEBS_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",      UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_CORE2_PEBS_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE2_PEBS_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE2_EMON_L3_CTR_CTL0  = 0x000107CC
MSR_CORE2_EMON_L3_CTR_CTL1  = 0x000107CD
MSR_CORE2_EMON_L3_CTR_CTL2  = 0x000107CE
MSR_CORE2_EMON_L3_CTR_CTL3  = 0x000107CF
MSR_CORE2_EMON_L3_CTR_CTL4  = 0x000107D0
MSR_CORE2_EMON_L3_CTR_CTL5  = 0x000107D1
MSR_CORE2_EMON_L3_CTR_CTL6  = 0x000107D2
MSR_CORE2_EMON_L3_CTR_CTL7  = 0x000107D3

MSR_CORE2_EMON_L3_GL_CTL  = 0x000107D8

