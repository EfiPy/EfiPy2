# P6Msr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.P6Msr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_P6_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x03 or
           DisplayModel == 0x05 or
           DisplayModel == 0x07 or
           DisplayModel == 0x08 or
           DisplayModel == 0x0A or
           DisplayModel == 0x0B
           )

MSR_P6_P5_MC_ADDR  = 0x00000000

MSR_P6_P5_MC_TYPE  = 0x00000001

MSR_P6_TSC  = 0x00000010

MSR_P6_IA32_PLATFORM_ID  = 0x00000017

class MSR_P6_IA32_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 32),
    ("Reserved2",               UINT32, 18),
    ("PlatformId",              UINT32, 3),
    ("L2CacheLatencyRead",      UINT32, 4),
    ("Reserved3",               UINT32, 3),
    ("ClockFrequencyRatioRead", UINT32, 1),
    ("Reserved4",               UINT32, 3)
  ]

class MSR_P6_IA32_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_IA32_PLATFORM_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_P6_APIC_BASE  = 0x0000001B

class MSR_P6_IA32_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 8),
    ("BSP",         UINT32, 1),
    ("Reserved2",   UINT32, 2),
    ("EN",          UINT32, 1),
    ("ApicBase",    UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_P6_IA32_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_IA32_PLATFORM_ID_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_EBL_CR_POWERON  = 0x0000002A

class MSR_P6_EBL_CR_POWERON_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                   UINT32, 1),
    ("DataErrorCheckingEnable",     UINT32, 1),
    ("ResponseErrorCheckingEnable", UINT32, 1),
    ("AERR_DriveEnable",            UINT32, 1),
    ("BERR_Enable",                 UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("BERR_DriverEnable",           UINT32, 1),
    ("BINIT_DriverEnable",          UINT32, 1),
    ("OutputTriStateEnable",        UINT32, 1),
    ("ExecuteBIST",                 UINT32, 1),
    ("AERR_ObservationEnabled",     UINT32, 1),
    ("Reserved3",                   UINT32, 1),
    ("BINIT_ObservationEnabled",    UINT32, 1),
    ("InOrderQueueDepth",           UINT32, 1),
    ("ResetVector",                 UINT32, 1),
    ("FRCModeEnable",               UINT32, 1),
    ("APICClusterID",               UINT32, 2),
    ("SystemBusFrequency",          UINT32, 2),
    ("SymmetricArbitrationID",      UINT32, 2),
    ("ClockFrequencyRatio",         UINT32, 4),
    ("LowPowerModeEnable",          UINT32, 1),
    ("ClockFrequencyRatio1",        UINT32, 1),
    ("Reserved4",                   UINT32, 4),
    ("Reserved5",                   UINT32, 32)
  ]

class MSR_P6_EBL_CR_POWERON_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_EBL_CR_POWERON_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_TEST_CTL  = 0x00000033

class MSR_P6_TEST_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 30),
    ("StreamingBufferDisable",  UINT32, 1),
    ("Disable_LOCK",            UINT32, 1),
    ("Reserved2",               UINT32, 32)
  ]

class MSR_P6_TEST_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_TEST_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_BIOS_UPDT_TRIG  = 0x00000079

MSR_P6_BBL_CR_D0  = 0x00000088
MSR_P6_BBL_CR_D1  = 0x00000089
MSR_P6_BBL_CR_D2  = 0x0000008A

MSR_P6_BIOS_SIGN  = 0x0000008B

MSR_P6_PERFCTR0  = 0x000000C1
MSR_P6_PERFCTR1  = 0x000000C2

MSR_P6_MTRRCAP  = 0x000000FE

MSR_P6_BBL_CR_ADDR  = 0x00000116

class MSR_P6_BBL_CR_ADDR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 3),
    ("Address",     UINT32, 29),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_P6_BBL_CR_ADDR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_BBL_CR_ADDR_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_BBL_CR_DECC  = 0x00000118

MSR_P6_BBL_CR_CTL  = 0x00000119

class MSR_P6_BBL_CR_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2Command",       UINT32, 5),
    ("StateToL2",       UINT32, 2),
    ("Reserved",        UINT32, 1),
    ("WayToL2",         UINT32, 2),
    ("Way",             UINT32, 2),
    ("MESI",            UINT32, 2),
    ("StateFromL2",     UINT32, 2),
    ("Reserved2",       UINT32, 1),
    ("L2Hit",           UINT32, 1),
    ("Reserved3",       UINT32, 1),
    ("UserEcc",         UINT32, 2),
    ("ProcessorNumber", UINT32, 1),
    ("Reserved4",       UINT32, 10),
    ("Reserved5",       UINT32, 32)
  ]

class MSR_P6_BBL_CR_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_BBL_CR_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_BBL_CR_TRIG  = 0x0000011A

MSR_P6_BBL_CR_BUSY  = 0x0000011B

MSR_P6_BBL_CR_CTL3  = 0x0000011E

class MSR_P6_BBL_CR_CTL3_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L2Configured",                UINT32, 1),
    ("L2CacheLatency",              UINT32, 4),
    ("ECCCheckEnable",              UINT32, 1),
    ("AddressParityCheckEnable",    UINT32, 1),
    ("CRTNParityCheckEnable",       UINT32, 1),
    ("L2Enabled",                   UINT32, 1),
    ("L2Associativity",             UINT32, 2),
    ("L2Banks",                     UINT32, 2),
    ("CacheSizePerBank",            UINT32, 5),
    ("CacheStateErrorEnable",       UINT32, 1),
    ("Reserved1",                   UINT32, 1),
    ("L2AddressRange",              UINT32, 3),
    ("L2HardwareDisable",           UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("CacheBusFraction",            UINT32, 1),
    ("Reserved3",                   UINT32, 6),
    ("Reserved4",                   UINT32, 32)
  ]

class MSR_P6_BBL_CR_CTL3_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_BBL_CR_CTL3_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_SYSENTER_CS_MSR  = 0x00000174

MSR_P6_SYSENTER_ESP_MSR  = 0x00000175

MSR_P6_SYSENTER_EIP_MSR  = 0x00000176

MSR_P6_MCG_CAP  = 0x00000179

MSR_P6_MCG_STATUS  = 0x0000017A

MSR_P6_MCG_CTL  = 0x0000017B

MSR_P6_PERFEVTSEL0  = 0x00000186
MSR_P6_PERFEVTSEL1  = 0x00000187

class MSR_P6_PERFEVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventSelect", UINT32, 8),
    ("UMASK",       UINT32, 8),
    ("USR",         UINT32, 1),
    ("OS",          UINT32, 1),
    ("E",           UINT32, 1),
    ("PC",          UINT32, 1),
    ("INT",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("EN",          UINT32, 1),
    ("INV",         UINT32, 1),
    ("CMASK",       UINT32, 8),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_P6_PERFEVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_PERFEVTSEL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_DEBUGCTLMSR  = 0x000001D9

class MSR_P6_DEBUGCTLMSR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LBR",         UINT32, 1),
    ("BTF",         UINT32, 1),
    ("PB0",         UINT32, 1),
    ("PB1",         UINT32, 1),
    ("PB2",         UINT32, 1),
    ("PB3",         UINT32, 1),
    ("TR",          UINT32, 1),
    ("Reserved1",   UINT32, 25),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_P6_DEBUGCTLMSR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_DEBUGCTLMSR_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_LASTBRANCHFROMIP  = 0x000001DB

MSR_P6_LASTBRANCHTOIP  = 0x000001DC

MSR_P6_LASTINTFROMIP  = 0x000001DD

MSR_P6_LASTINTTOIP  = 0x000001DE

MSR_P6_MTRRPHYSBASE0  = 0x00000200
MSR_P6_MTRRPHYSBASE1  = 0x00000202
MSR_P6_MTRRPHYSBASE2  = 0x00000204
MSR_P6_MTRRPHYSBASE3  = 0x00000206
MSR_P6_MTRRPHYSBASE4  = 0x00000208
MSR_P6_MTRRPHYSBASE5  = 0x0000020A
MSR_P6_MTRRPHYSBASE6  = 0x0000020C
MSR_P6_MTRRPHYSBASE7  = 0x0000020E

MSR_P6_MTRRPHYSMASK0  = 0x00000201
MSR_P6_MTRRPHYSMASK1  = 0x00000203
MSR_P6_MTRRPHYSMASK2  = 0x00000205
MSR_P6_MTRRPHYSMASK3  = 0x00000207
MSR_P6_MTRRPHYSMASK4  = 0x00000209
MSR_P6_MTRRPHYSMASK5  = 0x0000020B
MSR_P6_MTRRPHYSMASK6  = 0x0000020D
MSR_P6_MTRRPHYSMASK7  = 0x0000020F

MSR_P6_MTRRFIX64K_00000  = 0x00000250

MSR_P6_MTRRFIX16K_80000  = 0x00000258

MSR_P6_MTRRFIX16K_A0000  = 0x00000259

MSR_P6_MTRRFIX4K_C0000  = 0x00000268

MSR_P6_MTRRFIX4K_C8000  = 0x00000269

MSR_P6_MTRRFIX4K_D0000  = 0x0000026A

MSR_P6_MTRRFIX4K_D8000  = 0x0000026B

MSR_P6_MTRRFIX4K_E0000  = 0x0000026C

MSR_P6_MTRRFIX4K_E8000  = 0x0000026D

MSR_P6_MTRRFIX4K_F0000  = 0x0000026E

MSR_P6_MTRRFIX4K_F8000  = 0x0000026F

MSR_P6_MTRRDEFTYPE  = 0x000002FF

class MSR_P6_MTRRDEFTYPE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 3),
    ("Reserved1",   UINT32, 7),
    ("FE",          UINT32, 1),
    ("E",           UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_P6_MTRRDEFTYPE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_MTRRDEFTYPE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_P6_MC0_CTL  = 0x00000400
MSR_P6_MC1_CTL  = 0x00000404
MSR_P6_MC2_CTL  = 0x00000408
MSR_P6_MC3_CTL  = 0x00000410
MSR_P6_MC4_CTL  = 0x0000040C

MSR_P6_MC0_STATUS  = 0x00000401
MSR_P6_MC1_STATUS  = 0x00000405
MSR_P6_MC2_STATUS  = 0x00000409
MSR_P6_MC3_STATUS  = 0x00000411
MSR_P6_MC4_STATUS  = 0x0000040D

class MSR_P6_MC_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MC_STATUS_MCACOD",    UINT32, 16),
    ("MC_STATUS_MSCOD",     UINT32, 16),
    ("Reserved",            UINT32, 25),
    ("MC_STATUS_DAM",       UINT32, 1),
    ("MC_STATUS_ADDRV",     UINT32, 1),
    ("MC_STATUS_MISCV",     UINT32, 1),
    ("MC_STATUS_EN",        UINT32, 1),
    ("MC_STATUS_UC",        UINT32, 1),
    ("MC_STATUS_O",         UINT32, 1),
    ("MC_STATUS_V",         UINT32, 1)
  ]

class MSR_P6_MC_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_P6_MC_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_P6_MC0_ADDR  = 0x00000402
MSR_P6_MC1_ADDR  = 0x00000406
MSR_P6_MC2_ADDR  = 0x0000040A
MSR_P6_MC3_ADDR  = 0x00000412
MSR_P6_MC4_ADDR  = 0x0000040E

MSR_P6_MC0_MISC  = 0x00000403
MSR_P6_MC1_MISC  = 0x00000407
MSR_P6_MC2_MISC  = 0x0000040B
MSR_P6_MC3_MISC  = 0x00000413
MSR_P6_MC4_MISC  = 0x0000040F
