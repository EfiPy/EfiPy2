# AtomMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.AtomMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_ATOM_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x1C or
           DisplayModel == 0x26 or
           DisplayModel == 0x27 or
           DisplayModel == 0x35 or
           DisplayModel == 0x36
           )

MSR_ATOM_PLATFORM_ID  = 0x00000017

class MSR_ATOM_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumQualifiedRatio",   UINT32, 5),
    ("Reserved2",               UINT32, 19),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_ATOM_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_PLATFORM_ID_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_EBL_CR_POWERON  = 0x0000002A

class MSR_ATOM_EBL_CR_POWERON_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                   UINT32, 1),
    ("DataErrorCheckingEnable",     UINT32, 1),
    ("ResponseErrorCheckingEnable", UINT32, 1),
    ("AERR_DriveEnable",            UINT32, 1),
    ("BERR_Enable",                 UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("Reserved3",                   UINT32, 1),
    ("BINIT_DriverEnable",          UINT32, 1),
    ("Reserved4",                   UINT32, 1),
    ("ExecuteBIST",                 UINT32, 1),
    ("AERR_ObservationEnabled",     UINT32, 1),
    ("Reserved5",                   UINT32, 1),
    ("BINIT_ObservationEnabled",    UINT32, 1),
    ("Reserved6",                   UINT32, 1),
    ("ResetVector",                 UINT32, 1),
    ("Reserved7",                   UINT32, 1),
    ("APICClusterID",               UINT32, 2),
    ("Reserved8",                   UINT32, 2),
    ("SymmetricArbitrationID",      UINT32, 2),
    ("IntegerBusFrequencyRatio",    UINT32, 5),
    ("Reserved9",                   UINT32, 5),
    ("Reserved10",                  UINT32, 32)
  ]

class MSR_ATOM_EBL_CR_POWERON_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_EBL_CR_POWERON_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_LASTBRANCH_0_FROM_IP  = 0x00000040
MSR_ATOM_LASTBRANCH_1_FROM_IP  = 0x00000041
MSR_ATOM_LASTBRANCH_2_FROM_IP  = 0x00000042
MSR_ATOM_LASTBRANCH_3_FROM_IP  = 0x00000043
MSR_ATOM_LASTBRANCH_4_FROM_IP  = 0x00000044
MSR_ATOM_LASTBRANCH_5_FROM_IP  = 0x00000045
MSR_ATOM_LASTBRANCH_6_FROM_IP  = 0x00000046
MSR_ATOM_LASTBRANCH_7_FROM_IP  = 0x00000047

MSR_ATOM_LASTBRANCH_0_TO_IP  = 0x00000060
MSR_ATOM_LASTBRANCH_1_TO_IP  = 0x00000061
MSR_ATOM_LASTBRANCH_2_TO_IP  = 0x00000062
MSR_ATOM_LASTBRANCH_3_TO_IP  = 0x00000063
MSR_ATOM_LASTBRANCH_4_TO_IP  = 0x00000064
MSR_ATOM_LASTBRANCH_5_TO_IP  = 0x00000065
MSR_ATOM_LASTBRANCH_6_TO_IP  = 0x00000066
MSR_ATOM_LASTBRANCH_7_TO_IP  = 0x00000067

MSR_ATOM_FSB_FREQ  = 0x000000CD

class MSR_ATOM_FSB_FREQ_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ScalableBusSpeed",    UINT32, 3),
    ("Reserved1",           UINT32, 29),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_ATOM_FSB_FREQ_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_FSB_FREQ_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_BBL_CR_CTL3  = 0x0000011E

class MSR_ATOM_BBL_CR_CTL3_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2HardwareEnabled ", UINT32, 1),
    ("Reserved1         ", UINT32, 7),
    ("L2Enabled         ", UINT32, 1),
    ("Reserved2         ", UINT32, 14),
    ("L2NotPresent      ", UINT32, 1),
    ("Reserved3         ", UINT32, 8),
    ("Reserved4         ", UINT32, 32)
  ]

class MSR_ATOM_BBL_CR_CTL3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_BBL_CR_CTL3_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_PERF_STATUS  = 0x00000198

class MSR_ATOM_PERF_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CurrentPerformanceStateValue",    UINT32, 16),
    ("Reserved1",                       UINT32, 16),
    ("Reserved2",                       UINT32, 8),
    ("MaximumBusRatio",                 UINT32, 5),
    ("Reserved3",                       UINT32, 19)
  ]

class MSR_ATOM_PERF_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_PERF_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_THERM2_CTL  = 0x0000019D

class MSR_ATOM_THERM2_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 16),
    ("TM_SELECT",   UINT32, 1),
    ("Reserved2",   UINT32, 15),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_ATOM_THERM2_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_THERM2_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_IA32_MISC_ENABLE  = 0x000001A0

class MSR_ATOM_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FastStrings",                     UINT32, 1),
    ("Reserved1",                       UINT32, 2),
    ("AutomaticThermalControlCircuit",  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("PerformanceMonitoring",           UINT32, 1),
    ("Reserved3",                       UINT32, 1),
    ("Reserved4",                       UINT32, 1),
    ("FERR",                            UINT32, 1),
    ("BTS",                             UINT32, 1),
    ("PEBS",                            UINT32, 1),
    ("TM2",                             UINT32, 1),
    ("Reserved5",                       UINT32, 2),
    ("EIST",                            UINT32, 1),
    ("Reserved6",                       UINT32, 1),
    ("MONITOR",                         UINT32, 1),
    ("Reserved7",                       UINT32, 1),
    ("EISTLock",                        UINT32, 1),
    ("Reserved8",                       UINT32, 1),
    ("LimitCpuidMaxval",                UINT32, 1),
    ("xTPR_Message_Disable",            UINT32, 1),
    ("Reserved9",                       UINT32, 8),
    ("Reserved10",                      UINT32, 2),
    ("XD",                              UINT32, 1),
    ("Reserved11",                      UINT32, 29)
  ]

class MSR_ATOM_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_LASTBRANCH_TOS  = 0x000001C9

MSR_ATOM_LER_FROM_LIP    = 0x000001DD

MSR_ATOM_LER_TO_LIP      = 0x000001DE

MSR_ATOM_PEBS_ENABLE     = 0x000003F1

class MSR_ATOM_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",      UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_ATOM_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_ATOM_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_ATOM_PKG_C2_RESIDENCY  = 0x000003F8

MSR_ATOM_PKG_C4_RESIDENCY  = 0x000003F9

MSR_ATOM_PKG_C6_RESIDENCY  = 0x000003FA

