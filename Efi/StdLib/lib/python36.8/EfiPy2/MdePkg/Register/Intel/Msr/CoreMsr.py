# CoreMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.CoreMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_CORE_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x0E
           )

MSR_CORE_P5_MC_ADDR  = 0x00000000

MSR_CORE_P5_MC_TYPE  = 0x00000001

MSR_CORE_EBL_CR_POWERON  = 0x0000002A

class MSR_CORE_EBL_CR_POWERON_REGISTER_Bits (Structure):
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

class MSR_CORE_EBL_CR_POWERON_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE_EBL_CR_POWERON_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# #define MSR_CORE_LASTBRANCH_7  0x00000047
MSR_CORE_LASTBRANCH_0  = 0x00000040
MSR_CORE_LASTBRANCH_1  = 0x00000041
MSR_CORE_LASTBRANCH_2  = 0x00000042
MSR_CORE_LASTBRANCH_3  = 0x00000043
MSR_CORE_LASTBRANCH_4  = 0x00000044
MSR_CORE_LASTBRANCH_5  = 0x00000045
MSR_CORE_LASTBRANCH_6  = 0x00000046
MSR_CORE_LASTBRANCH_7  = 0x00000047

MSR_CORE_FSB_FREQ  = 0x000000CD

class MSR_CORE_FSB_FREQ_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ScalableBusSpeed",    UINT32, 3),
    ("Reserved1",           UINT32, 29),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_CORE_FSB_FREQ_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE_FSB_FREQ_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE_BBL_CR_CTL3  = 0x0000011E

class MSR_CORE_BBL_CR_CTL3_REGISTER_Bits (Structure):
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

class MSR_CORE_BBL_CR_CTL3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE_BBL_CR_CTL3_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE_THERM2_CTL  = 0x0000019D

class MSR_CORE_THERM2_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1", UINT32, 16),
    ("TM_SELECT", UINT32, 1),
    ("Reserved2", UINT32, 15),
    ("Reserved3", UINT32, 32)
  ]

class MSR_CORE_THERM2_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE_THERM2_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_CORE_IA32_MISC_ENABLE  = 0x000001A0

class MSR_CORE_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                       UINT32, 3),
    ("AutomaticThermalControlCircuit",  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("PerformanceMonitoring",           UINT32, 1),
    ("Reserved3",                       UINT32, 2),
    ("FERR",                            UINT32, 1),
    ("BTS",                             UINT32, 1),
    ("Reserved4",                       UINT32, 1),
    ("TM2",                             UINT32, 1),
    ("Reserved5",                       UINT32, 2),
    ("EIST",                            UINT32, 1),
    ("Reserved6",                       UINT32, 1),
    ("MONITOR",                         UINT32, 1),
    ("Reserved7",                       UINT32, 1),
    ("Reserved8",                       UINT32, 2),
    ("LimitCpuidMaxval",                UINT32, 1),
    ("Reserved9",                       UINT32, 9),
    ("Reserved10",                      UINT32, 2),
    ("XD",                              UINT32, 1),
    ("Reserved11",                      UINT32, 29)
  ]

class MSR_CORE_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_CORE_LASTBRANCH_TOS  = 0x000001C9

MSR_CORE_LER_FROM_LIP  = 0x000001DD

MSR_CORE_LER_TO_LIP  = 0x000001DE

MSR_CORE_MTRRPHYSBASE0  = 0x00000200
MSR_CORE_MTRRPHYSBASE1  = 0x00000202
MSR_CORE_MTRRPHYSBASE2  = 0x00000204
MSR_CORE_MTRRPHYSBASE3  = 0x00000206
MSR_CORE_MTRRPHYSBASE4  = 0x00000208
MSR_CORE_MTRRPHYSBASE5  = 0x0000020A
MSR_CORE_MTRRPHYSMASK6  = 0x0000020D
MSR_CORE_MTRRPHYSMASK7  = 0x0000020F

MSR_CORE_MTRRPHYSMASK0  = 0x00000201
MSR_CORE_MTRRPHYSMASK1  = 0x00000203
MSR_CORE_MTRRPHYSMASK2  = 0x00000205
MSR_CORE_MTRRPHYSMASK3  = 0x00000207
MSR_CORE_MTRRPHYSMASK4  = 0x00000209
MSR_CORE_MTRRPHYSMASK5  = 0x0000020B
MSR_CORE_MTRRPHYSBASE6  = 0x0000020C
MSR_CORE_MTRRPHYSBASE7  = 0x0000020E

MSR_CORE_MTRRFIX64K_00000  = 0x00000250

MSR_CORE_MTRRFIX16K_80000  = 0x00000258

MSR_CORE_MTRRFIX16K_A0000  = 0x00000259

MSR_CORE_MTRRFIX4K_C0000  = 0x00000268

MSR_CORE_MTRRFIX4K_C8000  = 0x00000269

MSR_CORE_MTRRFIX4K_D0000  = 0x0000026A

MSR_CORE_MTRRFIX4K_D8000  = 0x0000026B

MSR_CORE_MTRRFIX4K_E0000  = 0x0000026C

MSR_CORE_MTRRFIX4K_E8000  = 0x0000026D

MSR_CORE_MTRRFIX4K_F0000  = 0x0000026E

MSR_CORE_MTRRFIX4K_F8000  = 0x0000026F

MSR_CORE_MC4_CTL  = 0x0000040C

MSR_CORE_MC4_STATUS  = 0x0000040D

MSR_CORE_MC4_ADDR  = 0x0000040E

MSR_CORE_MC3_ADDR  = 0x00000412

MSR_CORE_MC3_MISC  = 0x00000413

MSR_CORE_MC5_CTL  = 0x00000414

MSR_CORE_MC5_STATUS  = 0x00000415

MSR_CORE_MC5_ADDR  = 0x00000416

MSR_CORE_MC5_MISC  = 0x00000417

MSR_CORE_IA32_EFER  = 0xC0000080

class MSR_CORE_IA32_EFER_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 11),
    ("NXE",         UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_CORE_IA32_EFER_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_CORE_IA32_EFER_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

