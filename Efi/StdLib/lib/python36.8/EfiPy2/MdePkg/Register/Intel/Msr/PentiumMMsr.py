# PentiumMMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.PentiumMMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_PENTIUM_M_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x0D
           )

MSR_PENTIUM_M_P5_MC_ADDR  = 0x00000000

MSR_PENTIUM_M_P5_MC_TYPE  = 0x00000001

MSR_PENTIUM_M_EBL_CR_POWERON  = 0x0000002A

class MSR_PENTIUM_M_EBL_CR_POWERON_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                   UINT32, 1),
    ("DataErrorCheckingEnable",     UINT32, 1),
    ("ResponseErrorCheckingEnable", UINT32, 1),
    ("MCERR_DriveEnable",           UINT32, 1),
    ("AddressParityEnable",         UINT32, 1),
    ("Reserved2",                   UINT32, 2),
    ("BINIT_DriverEnable",          UINT32, 1),
    ("OutputTriStateEnable",        UINT32, 1),
    ("ExecuteBIST",                 UINT32, 1),
    ("MCERR_ObservationEnabled",    UINT32, 1),
    ("Reserved3",                   UINT32, 1),
    ("BINIT_ObservationEnabled",    UINT32, 1),
    ("Reserved4",                   UINT32, 1),
    ("ResetVector",                 UINT32, 1),
    ("Reserved5",                   UINT32, 1),
    ("APICClusterID",               UINT32, 2),
    ("SystemBusFrequency",          UINT32, 1),
    ("Reserved6",                   UINT32, 1),
    ("SymmetricArbitrationID",      UINT32, 2),
    ("ClockFrequencyRatio",         UINT32, 5),
    ("Reserved7",                   UINT32, 5),
    ("Reserved8",                   UINT32, 32)
  ]

class MSR_PENTIUM_M_EBL_CR_POWERON_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_PENTIUM_M_EBL_CR_POWERON_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_PENTIUM_M_LASTBRANCH_0  = 0x00000040
MSR_PENTIUM_M_LASTBRANCH_1  = 0x00000041
MSR_PENTIUM_M_LASTBRANCH_2  = 0x00000042
MSR_PENTIUM_M_LASTBRANCH_3  = 0x00000043
MSR_PENTIUM_M_LASTBRANCH_4  = 0x00000044
MSR_PENTIUM_M_LASTBRANCH_5  = 0x00000045
MSR_PENTIUM_M_LASTBRANCH_6  = 0x00000046
MSR_PENTIUM_M_LASTBRANCH_7  = 0x00000047

MSR_PENTIUM_M_BBL_CR_CTL   = 0x00000119
MSR_PENTIUM_M_BBL_CR_CTL3  = 0x0000011E

class MSR_PENTIUM_M_BBL_CR_CTL3_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2HardwareEnabled",   UINT32, 1),
    ("Reserved1",           UINT32, 4),
    ("ECCCheckEnable",      UINT32, 1),
    ("Reserved2",           UINT32, 2),
    ("L2Enabled",           UINT32, 1),
    ("Reserved3",           UINT32, 14),
    ("L2NotPresent",        UINT32, 1),
    ("Reserved4",           UINT32, 8),
    ("Reserved5",           UINT32, 32)
  ]

class MSR_PENTIUM_M_BBL_CR_CTL3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_PENTIUM_M_BBL_CR_CTL3_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_PENTIUM_M_THERM2_CTL  = 0x0000019D

class MSR_PENTIUM_M_THERM2_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1", UINT32, 16),
    ("TM_SELECT", UINT32, 1),
    ("Reserved2", UINT32, 15),
    ("Reserved3", UINT32, 32)
  ]

class MSR_PENTIUM_M_THERM2_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_PENTIUM_M_THERM2_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_PENTIUM_M_IA32_MISC_ENABLE  = 0x000001A0

class MSR_PENTIUM_M_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                       UINT32, 3),
    ("AutomaticThermalControlCircuit",  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("PerformanceMonitoring",           UINT32, 1),
    ("Reserved3",                       UINT32, 2),
    ("FERR",                            UINT32, 1),
    ("BTS",                             UINT32, 1),
    ("PEBS",                            UINT32, 1),
    ("Reserved5",                       UINT32, 3),
    ("EIST",                            UINT32, 1),
    ("Reserved6",                       UINT32, 6),
    ("xTPR_Message_Disable",            UINT32, 1),
    ("Reserved7",                       UINT32, 8),
    ("Reserved8",                       UINT32, 32)
  ]

class MSR_PENTIUM_M_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_PENTIUM_M_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_PENTIUM_M_LASTBRANCH_TOS  = 0x000001C9
MSR_PENTIUM_M_DEBUGCTLB       = 0x000001D9
MSR_PENTIUM_M_LER_TO_LIP      = 0x000001DD
MSR_PENTIUM_M_LER_FROM_LIP    = 0x000001DE
MSR_PENTIUM_M_MC4_CTL         = 0x0000040C
MSR_PENTIUM_M_MC4_STATUS      = 0x0000040D
MSR_PENTIUM_M_MC4_ADDR        = 0x0000040E
MSR_PENTIUM_M_MC3_CTL         = 0x00000410
MSR_PENTIUM_M_MC3_STATUS      = 0x00000411
MSR_PENTIUM_M_MC3_ADDR        = 0x00000412
