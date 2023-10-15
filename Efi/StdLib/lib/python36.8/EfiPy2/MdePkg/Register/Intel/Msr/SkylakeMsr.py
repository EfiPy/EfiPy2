# SkylakeMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.SkylakeMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_SKYLAKE_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x4E or
           DisplayModel == 0x5E or
           DisplayModel == 0x55 or
           DisplayModel == 0x8E or
           DisplayModel == 0x9E or
           DisplayModel == 0x66
           )

MSR_SKYLAKE_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_SKYLAKE_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Maximum1C",   UINT32, 8),
    ("Maximum2C",   UINT32, 8),
    ("Maximum3C",   UINT32, 8),
    ("Maximum4C",   UINT32, 8),
    ("Reserved",    UINT32, 32)
  ]

class MSR_SKYLAKE_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_LASTBRANCH_TOS  = 0x000001C9

MSR_SKYLAKE_POWER_CTL  = 0x000001FC

class MSR_SKYLAKE_POWER_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                           UINT32, 1),
    ("C1EEnable",                           UINT32, 1),
    ("Reserved2",                           UINT32, 17),
    ("Fix_Me_1",                            UINT32, 1),
    ("DisableEnergyEfficiencyOptimization", UINT32, 1),
    ("Reserved3",                           UINT32, 11),
    ("Reserved4",                           UINT32, 32)
  ]

class MSR_SKYLAKE_POWER_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_POWER_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_SGXOWNEREPOCH0  = 0x00000300

MSR_SKYLAKE_SGXOWNER0  = MSR_SKYLAKE_SGXOWNEREPOCH0

MSR_SKYLAKE_SGXOWNEREPOCH1  = 0x00000301

MSR_SKYLAKE_SGXOWNER1  = MSR_SKYLAKE_SGXOWNEREPOCH1

MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS  = 0x0000038E

class MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0",        UINT32, 1),
    ("Ovf_PMC1",        UINT32, 1),
    ("Ovf_PMC2",        UINT32, 1),
    ("Ovf_PMC3",        UINT32, 1),
    ("Ovf_PMC4",        UINT32, 1),
    ("Ovf_PMC5",        UINT32, 1),
    ("Ovf_PMC6",        UINT32, 1),
    ("Ovf_PMC7",        UINT32, 1),
    ("Reserved1",       UINT32, 24),
    ("Ovf_FixedCtr0",   UINT32, 1),
    ("Ovf_FixedCtr1",   UINT32, 1),
    ("Ovf_FixedCtr2",   UINT32, 1),
    ("Reserved2",       UINT32, 20),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved3",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("Ovf_BufDSSAVE",   UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_RESET  = 0x00000390

class MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0",        UINT32, 1),
    ("Ovf_PMC1",        UINT32, 1),
    ("Ovf_PMC2",        UINT32, 1),
    ("Ovf_PMC3",        UINT32, 1),
    ("Ovf_PMC4",        UINT32, 1),
    ("Ovf_PMC5",        UINT32, 1),
    ("Ovf_PMC6",        UINT32, 1),
    ("Ovf_PMC7",        UINT32, 1),
    ("Reserved1",       UINT32, 24),
    ("Ovf_FixedCtr0",   UINT32, 1),
    ("Ovf_FixedCtr1",   UINT32, 1),
    ("Ovf_FixedCtr2",   UINT32, 1),
    ("Reserved2",       UINT32, 20),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved3",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("Ovf_BufDSSAVE",   UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_SET  = 0x00000391

class MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0",        UINT32, 1),
    ("Ovf_PMC1",        UINT32, 1),
    ("Ovf_PMC2",        UINT32, 1),
    ("Ovf_PMC3",        UINT32, 1),
    ("Ovf_PMC4",        UINT32, 1),
    ("Ovf_PMC5",        UINT32, 1),
    ("Ovf_PMC6",        UINT32, 1),
    ("Ovf_PMC7",        UINT32, 1),
    ("Reserved1",       UINT32, 24),
    ("Ovf_FixedCtr0",   UINT32, 1),
    ("Ovf_FixedCtr1",   UINT32, 1),
    ("Ovf_FixedCtr2",   UINT32, 1),
    ("Reserved2",       UINT32, 20),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved3",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("Ovf_BufDSSAVE",   UINT32, 1),
    ("Reserved4",       UINT32, 1)
  ]

class MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_SET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PEBS_FRONTEND  = 0x000003F7

class MSR_SKYLAKE_PEBS_FRONTEND_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventCodeSelect",     UINT32, 3),
    ("Reserved1",           UINT32, 1),
    ("EventCodeSelectHigh", UINT32, 1),
    ("Reserved2",           UINT32, 3),
    ("IDQ_Bubble_Length",   UINT32, 12),
    ("IDQ_Bubble_Width",    UINT32, 3),
    ("Reserved3",           UINT32, 9),
    ("Reserved4",           UINT32, 32)
  ]

class MSR_SKYLAKE_PEBS_FRONTEND_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PEBS_FRONTEND_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PP0_ENERGY_STATUS  = 0x00000639

MSR_SKYLAKE_PLATFORM_ENERGY_COUNTER  = 0x0000064D

class MSR_SKYLAKE_PLATFORM_ENERGY_COUNTER_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TotalEnergy", UINT32, 32),
    ("Reserved",    UINT32, 32)
  ]

class MSR_SKYLAKE_PLATFORM_ENERGY_COUNTER_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PLATFORM_ENERGY_COUNTER_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PPERF  = 0x0000064E

MSR_SKYLAKE_CORE_PERF_LIMIT_REASONS  = 0x0000064F

class MSR_SKYLAKE_CORE_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                      UINT32, 1),
    ("ThermalStatus",                       UINT32, 1),
    ("Reserved1",                           UINT32, 2),
    ("ResidencyStateRegulationStatus",      UINT32, 1),
    ("RunningAverageThermalLimitStatus",    UINT32, 1),
    ("VRThermAlertStatus",                  UINT32, 1),
    ("VRThermDesignCurrentStatus",          UINT32, 1),
    ("OtherStatus",                         UINT32, 1),
    ("Reserved2",                           UINT32, 1),
    ("PL1Status",                           UINT32, 1),
    ("PL2Status",                           UINT32, 1),
    ("MaxTurboLimitStatus",                 UINT32, 1),
    ("TurboTransitionAttenuationStatus",    UINT32, 1),
    ("Reserved3",                           UINT32, 2),
    ("PROCHOT_Log",                         UINT32, 1),
    ("ThermalLog",                          UINT32, 1),
    ("Reserved4",                           UINT32, 2),
    ("ResidencyStateRegulationLog",         UINT32, 1),
    ("RunningAverageThermalLimitLog",       UINT32, 1),
    ("VRThermAlertLog",                     UINT32, 1),
    ("VRThermalDesignCurrentLog",           UINT32, 1),
    ("OtherLog",                            UINT32, 1),
    ("Reserved5",                           UINT32, 1),
    ("PL1Log",                              UINT32, 1),
    ("PL2Log",                              UINT32, 1),
    ("MaxTurboLimitLog",                    UINT32, 1),
    ("TurboTransitionAttenuationLog",       UINT32, 1),
    ("Reserved6",                           UINT32, 2),
    ("Reserved7",                           UINT32, 32)
  ]

class MSR_SKYLAKE_CORE_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_CORE_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PKG_HDC_CONFIG  = 0x00000652

class MSR_SKYLAKE_PKG_HDC_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PKG_Cx_Monitor",  UINT32, 3),
    ("Reserved1",       UINT32, 29),
    ("Reserved2",       UINT32, 32)
    ]

class MSR_SKYLAKE_PKG_HDC_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PKG_HDC_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_CORE_HDC_RESIDENCY          = 0x00000653
MSR_SKYLAKE_PKG_HDC_SHALLOW_RESIDENCY   = 0x00000655
MSR_SKYLAKE_PKG_HDC_DEEP_RESIDENCY      = 0x00000656
MSR_SKYLAKE_WEIGHTED_CORE_C0            = 0x00000658
MSR_SKYLAKE_ANY_CORE_C0                 = 0x00000659
MSR_SKYLAKE_ANY_GFXE_C0                 = 0x0000065A
MSR_SKYLAKE_CORE_GFXE_OVERLAP_C0        = 0x0000065B
MSR_SKYLAKE_PLATFORM_POWER_LIMIT        = 0x0000065C

class MSR_SKYLAKE_PLATFORM_POWER_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PlatformPowerLimit1",         UINT32, 15),
    ("EnablePlatformPowerLimit1",   UINT32, 1),
    ("PlatformClampingLimitation1", UINT32, 1),
    ("Time",                        UINT32, 7),
    ("Reserved1",                   UINT32, 8),
    ("PlatformPowerLimit2",         UINT32, 15),
    ("EnablePlatformPowerLimit2",   UINT32, 1),
    ("PlatformClampingLimitation2", UINT32, 1),
    ("Reserved2",                   UINT32, 14),
    ("Lock",                        UINT32, 1),
    ]

class MSR_SKYLAKE_PLATFORM_POWER_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PLATFORM_POWER_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_LASTBRANCH_16_FROM_IP  = 0x00000690
MSR_SKYLAKE_LASTBRANCH_17_FROM_IP  = 0x00000691
MSR_SKYLAKE_LASTBRANCH_18_FROM_IP  = 0x00000692
MSR_SKYLAKE_LASTBRANCH_19_FROM_IP  = 0x00000693
MSR_SKYLAKE_LASTBRANCH_20_FROM_IP  = 0x00000694
MSR_SKYLAKE_LASTBRANCH_21_FROM_IP  = 0x00000695
MSR_SKYLAKE_LASTBRANCH_22_FROM_IP  = 0x00000696
MSR_SKYLAKE_LASTBRANCH_23_FROM_IP  = 0x00000697
MSR_SKYLAKE_LASTBRANCH_24_FROM_IP  = 0x00000698
MSR_SKYLAKE_LASTBRANCH_25_FROM_IP  = 0x00000699
MSR_SKYLAKE_LASTBRANCH_26_FROM_IP  = 0x0000069A
MSR_SKYLAKE_LASTBRANCH_27_FROM_IP  = 0x0000069B
MSR_SKYLAKE_LASTBRANCH_28_FROM_IP  = 0x0000069C
MSR_SKYLAKE_LASTBRANCH_29_FROM_IP  = 0x0000069D
MSR_SKYLAKE_LASTBRANCH_30_FROM_IP  = 0x0000069E
MSR_SKYLAKE_LASTBRANCH_31_FROM_IP  = 0x0000069F

MSR_SKYLAKE_GRAPHICS_PERF_LIMIT_REASONS  = 0x000006B0

class MSR_SKYLAKE_GRAPHICS_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                      UINT32, 1),
    ("ThermalStatus",                       UINT32, 1),
    ("Reserved1",                           UINT32, 3),
    ("RunningAverageThermalLimitStatus",    UINT32, 1),
    ("VRThermAlertStatus",                  UINT32, 1),
    ("VRThermalDesignCurrentStatus",        UINT32, 1),
    ("OtherStatus",                         UINT32, 1),
    ("Reserved2",                           UINT32, 1),
    ("PL1Status",                           UINT32, 1),
    ("PL2Status",                           UINT32, 1),
    ("InefficientOperationStatus",          UINT32, 1),
    ("Reserved3",                           UINT32, 3),
    ("PROCHOT_Log",                         UINT32, 1),
    ("ThermalLog",                          UINT32, 1),
    ("Reserved4",                           UINT32, 3),
    ("RunningAverageThermalLimitLog",       UINT32, 1),
    ("VRThermAlertLog",                     UINT32, 1),
    ("VRThermalDesignCurrentLog",           UINT32, 1),
    ("OtherLog",                            UINT32, 1),
    ("Reserved5",                           UINT32, 1),
    ("PL1Log",                              UINT32, 1),
    ("PL2Log",                              UINT32, 1),
    ("InefficientOperationLog",             UINT32, 1),
    ("Reserved6",                           UINT32, 3),
    ("Reserved7",                           UINT32, 32)
    ]

class MSR_SKYLAKE_GRAPHICS_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_GRAPHICS_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_RING_PERF_LIMIT_REASONS  = 0x000006B1

class MSR_SKYLAKE_RING_PERF_LIMIT_REASONS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PROCHOT_Status",                      UINT32, 1),
    ("ThermalStatus",                       UINT32, 1),
    ("Reserved1",                           UINT32, 3),
    ("RunningAverageThermalLimitStatus",    UINT32, 1),
    ("VRThermAlertStatus",                  UINT32, 1),
    ("VRThermalDesignCurrentStatus",        UINT32, 1),
    ("OtherStatus",                         UINT32, 1),
    ("Reserved2",                           UINT32, 1),
    ("PL1Status",                           UINT32, 1),
    ("PL2Status",                           UINT32, 1),
    ("Reserved3",                           UINT32, 4),
    ("PROCHOT_Log",                         UINT32, 1),
    ("ThermalLog",                          UINT32, 1),
    ("Reserved4",                           UINT32, 3),
    ("RunningAverageThermalLimitLog",       UINT32, 1),
    ("VRThermAlertLog",                     UINT32, 1),
    ("VRThermalDesignCurrentLog",           UINT32, 1),
    ("OtherLog",                            UINT32, 1),
    ("Reserved5",                           UINT32, 1),
    ("PL1Log",                              UINT32, 1),
    ("PL2Log",                              UINT32, 1),
    ("Reserved6",                           UINT32, 4),
    ("Reserved7",                           UINT32, 32)
    ]

class MSR_SKYLAKE_RING_PERF_LIMIT_REASONS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_RING_PERF_LIMIT_REASONS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_LASTBRANCH_16_TO_IP  = 0x000006D0
MSR_SKYLAKE_LASTBRANCH_17_TO_IP  = 0x000006D1
MSR_SKYLAKE_LASTBRANCH_18_TO_IP  = 0x000006D2
MSR_SKYLAKE_LASTBRANCH_19_TO_IP  = 0x000006D3
MSR_SKYLAKE_LASTBRANCH_20_TO_IP  = 0x000006D4
MSR_SKYLAKE_LASTBRANCH_21_TO_IP  = 0x000006D5
MSR_SKYLAKE_LASTBRANCH_22_TO_IP  = 0x000006D6
MSR_SKYLAKE_LASTBRANCH_23_TO_IP  = 0x000006D7
MSR_SKYLAKE_LASTBRANCH_24_TO_IP  = 0x000006D8
MSR_SKYLAKE_LASTBRANCH_25_TO_IP  = 0x000006D9
MSR_SKYLAKE_LASTBRANCH_26_TO_IP  = 0x000006DA
MSR_SKYLAKE_LASTBRANCH_27_TO_IP  = 0x000006DB
MSR_SKYLAKE_LASTBRANCH_28_TO_IP  = 0x000006DC
MSR_SKYLAKE_LASTBRANCH_29_TO_IP  = 0x000006DD
MSR_SKYLAKE_LASTBRANCH_30_TO_IP  = 0x000006DE
MSR_SKYLAKE_LASTBRANCH_31_TO_IP  = 0x000006DF

MSR_SKYLAKE_LBR_INFO_0   = 0x00000DC0
MSR_SKYLAKE_LBR_INFO_1   = 0x00000DC1
MSR_SKYLAKE_LBR_INFO_2   = 0x00000DC2
MSR_SKYLAKE_LBR_INFO_3   = 0x00000DC3
MSR_SKYLAKE_LBR_INFO_4   = 0x00000DC4
MSR_SKYLAKE_LBR_INFO_5   = 0x00000DC5
MSR_SKYLAKE_LBR_INFO_6   = 0x00000DC6
MSR_SKYLAKE_LBR_INFO_7   = 0x00000DC7
MSR_SKYLAKE_LBR_INFO_8   = 0x00000DC8
MSR_SKYLAKE_LBR_INFO_9   = 0x00000DC9
MSR_SKYLAKE_LBR_INFO_10  = 0x00000DCA
MSR_SKYLAKE_LBR_INFO_11  = 0x00000DCB
MSR_SKYLAKE_LBR_INFO_12  = 0x00000DCC
MSR_SKYLAKE_LBR_INFO_13  = 0x00000DCD
MSR_SKYLAKE_LBR_INFO_14  = 0x00000DCE
MSR_SKYLAKE_LBR_INFO_15  = 0x00000DCF
MSR_SKYLAKE_LBR_INFO_16  = 0x00000DD0
MSR_SKYLAKE_LBR_INFO_17  = 0x00000DD1
MSR_SKYLAKE_LBR_INFO_18  = 0x00000DD2
MSR_SKYLAKE_LBR_INFO_19  = 0x00000DD3
MSR_SKYLAKE_LBR_INFO_20  = 0x00000DD4
MSR_SKYLAKE_LBR_INFO_21  = 0x00000DD5
MSR_SKYLAKE_LBR_INFO_22  = 0x00000DD6
MSR_SKYLAKE_LBR_INFO_23  = 0x00000DD7
MSR_SKYLAKE_LBR_INFO_24  = 0x00000DD8
MSR_SKYLAKE_LBR_INFO_25  = 0x00000DD9
MSR_SKYLAKE_LBR_INFO_26  = 0x00000DDA
MSR_SKYLAKE_LBR_INFO_27  = 0x00000DDB
MSR_SKYLAKE_LBR_INFO_28  = 0x00000DDC
MSR_SKYLAKE_LBR_INFO_29  = 0x00000DDD
MSR_SKYLAKE_LBR_INFO_30  = 0x00000DDE
MSR_SKYLAKE_LBR_INFO_31  = 0x00000DDF

MSR_SKYLAKE_UNC_PERF_FIXED_CTRL  = 0x00000394

class MSR_SKYLAKE_UNC_PERF_FIXED_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",       UINT32, 20),
    ("EnableOverflow",  UINT32, 1),
    ("Reserved2",       UINT32, 1),
    ("EnableCounting",  UINT32, 1),
    ("Reserved3",       UINT32, 9),
    ("Reserved4",       UINT32, 32)
    ]

class MSR_SKYLAKE_UNC_PERF_FIXED_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNC_PERF_FIXED_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_UNC_PERF_FIXED_CTR  = 0x00000395

class MSR_SKYLAKE_UNC_PERF_FIXED_CTR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CurrentCount",    UINT32, 32),
    ("CurrentCountHi",  UINT32, 12),
    ("Reserved",        UINT32, 20)
    ]

class MSR_SKYLAKE_UNC_PERF_FIXED_CTR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNC_PERF_FIXED_CTR_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_UNC_CBO_CONFIG  = 0x00000396

class MSR_SKYLAKE_UNC_CBO_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CBox",        UINT32, 4),
    ("Reserved1",   UINT32, 28),
    ("Reserved2",   UINT32, 32)
    ]

class MSR_SKYLAKE_UNC_CBO_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNC_CBO_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_UNC_ARB_PERFCTR0        = 0x000003B0
MSR_SKYLAKE_UNC_ARB_PERFCTR1        = 0x000003B1
MSR_SKYLAKE_UNC_ARB_PERFEVTSEL0     = 0x000003B2
MSR_SKYLAKE_UNC_ARB_PERFEVTSEL1     = 0x000003B3
MSR_SKYLAKE_UNC_CBO_0_PERFEVTSEL0   = 0x00000700
MSR_SKYLAKE_UNC_CBO_0_PERFEVTSEL1   = 0x00000701
MSR_SKYLAKE_UNC_CBO_0_PERFCTR0      = 0x00000706
MSR_SKYLAKE_UNC_CBO_0_PERFCTR1      = 0x00000707
MSR_SKYLAKE_UNC_CBO_1_PERFEVTSEL0   = 0x00000710
MSR_SKYLAKE_UNC_CBO_1_PERFEVTSEL1   = 0x00000711
MSR_SKYLAKE_UNC_CBO_1_PERFCTR0      = 0x00000716
MSR_SKYLAKE_UNC_CBO_1_PERFCTR1      = 0x00000717
MSR_SKYLAKE_UNC_CBO_2_PERFEVTSEL0   = 0x00000720
MSR_SKYLAKE_UNC_CBO_2_PERFEVTSEL1   = 0x00000721
MSR_SKYLAKE_UNC_CBO_2_PERFCTR0      = 0x00000726
MSR_SKYLAKE_UNC_CBO_2_PERFCTR1      = 0x00000727
MSR_SKYLAKE_UNC_CBO_3_PERFEVTSEL0   = 0x00000730
MSR_SKYLAKE_UNC_CBO_3_PERFEVTSEL1   = 0x00000731
MSR_SKYLAKE_UNC_CBO_3_PERFCTR0      = 0x00000736
MSR_SKYLAKE_UNC_CBO_3_PERFCTR1      = 0x00000737
MSR_SKYLAKE_UNC_PERF_GLOBAL_CTRL    = 0x00000E01

class MSR_SKYLAKE_UNC_PERF_GLOBAL_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PMI_Sel_Slice0",  UINT32, 1),
    ("PMI_Sel_Slice1",  UINT32, 1),
    ("PMI_Sel_Slice2",  UINT32, 1),
    ("PMI_Sel_Slice3",  UINT32, 1),
    ("PMI_Sel_Slice4",  UINT32, 1),
    ("Reserved1",       UINT32, 14),
    ("Reserved2",       UINT32, 10),
    ("EN",              UINT32, 1),
    ("WakePMI",         UINT32, 1),
    ("FREEZE",          UINT32, 1),
    ("Reserved3",       UINT32, 32)
    ]

class MSR_SKYLAKE_UNC_PERF_GLOBAL_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNC_PERF_GLOBAL_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_UNC_PERF_GLOBAL_STATUS  = 0x00000E02

class MSR_SKYLAKE_UNC_PERF_GLOBAL_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Fixed",       UINT32, 1),
    ("ARB",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("CBox",        UINT32, 1),
    ("Reserved2",   UINT32, 28),
    ("Reserved3",   UINT32, 32)
    ]

class MSR_SKYLAKE_UNC_PERF_GLOBAL_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNC_PERF_GLOBAL_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_TRACE_HUB_STH_ACPIBAR_BASE  = 0x00000080

class MSR_SKYLAKE_TRACE_HUB_STH_ACPIBAR_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Fix_Me_1",                UINT32, 1),
    ("Reserved",                UINT32, 17),
    ("ACPIBAR_BASE_ADDRESS",    UINT32, 14),
    ("Fix_Me_2",                UINT32, 32)
    ]

class MSR_SKYLAKE_TRACE_HUB_STH_ACPIBAR_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_TRACE_HUB_STH_ACPIBAR_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PRMRR_PHYS_BASE  = 0x000001F4

class MSR_SKYLAKE_PRMRR_PHYS_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MemTypePRMRRBASEMemType", UINT32, 3),
    ("Reserved1",               UINT32, 9),
    ("BasePRMRRBaseAddress",    UINT32, 20),
    ("Fix_Me_1",                UINT32, 14),
    ("Reserved2",               UINT32, 18)
    ]

class MSR_SKYLAKE_PRMRR_PHYS_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PRMRR_PHYS_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PRMRR_PHYS_MASK  = 0x000001F5

class MSR_SKYLAKE_PRMRR_PHYS_MASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 10),
    ("Fix_Me_1",    UINT32, 1),
    ("VLD",         UINT32, 1),
    ("Fix_Me_2",    UINT32, 20),
    ("Fix_Me_3",    UINT32, 14),
    ("Reserved2",   UINT32, 18)
    ]

class MSR_SKYLAKE_PRMRR_PHYS_MASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PRMRR_PHYS_MASK_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PRMRR_VALID_CONFIG  = 0x000001FB

class MSR_SKYLAKE_PRMRR_VALID_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Fix_Me_1",    UINT32, 1),
    ("Reserved1",   UINT32, 4),
    ("Fix_Me_2",    UINT32, 1),
    ("Fix_Me_3",    UINT32, 1),
    ("Fix_Me_4",    UINT32, 1),
    ("Reserved2",   UINT32, 24),
    ("Reserved3",   UINT32, 32)
    ]

class MSR_SKYLAKE_PRMRR_VALID_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PRMRR_VALID_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_UNCORE_PRMRR_PHYS_BASE  = 0x000002F4

class MSR_SKYLAKE_UNCORE_PRMRR_PHYS_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 12),
    ("Fix_Me_1",    UINT32, 20),
    ("Fix_Me_2",    UINT32, 7),
    ("Reserved2",   UINT32, 25)
    ]

class MSR_SKYLAKE_UNCORE_PRMRR_PHYS_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNCORE_PRMRR_PHYS_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_UNCORE_PRMRR_PHYS_MASK  = 0x000002F5

class MSR_SKYLAKE_UNCORE_PRMRR_PHYS_MASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 10),
    ("Fix_Me_1",    UINT32, 1),
    ("Fix_Me_2",    UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
    ]

class MSR_SKYLAKE_UNCORE_PRMRR_PHYS_MASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_UNCORE_PRMRR_PHYS_MASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_RING_RATIO_LIMIT  = 0x00000620

class MSR_SKYLAKE_RING_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Fix_Me_1",    UINT32, 7),
    ("Reserved1",   UINT32, 1),
    ("Fix_Me_2",    UINT32, 7),
    ("Reserved2",   UINT32, 17),
    ("Reserved3",   UINT32, 32)
    ]

class MSR_SKYLAKE_RING_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_RING_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_BR_DETECT_CTRL  = 0x00000350

class MSR_SKYLAKE_BR_DETECT_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EnMonitoring",    UINT32, 1),
    ("EnExcept",        UINT32, 1),
    ("EnLBRFrz",        UINT32, 1),
    ("DisableInGuest",  UINT32, 1),
    ("Reserved1",       UINT32, 4),
    ("WindowSize",      UINT32, 10),
    ("Reserved2",       UINT32, 6),
    ("WindowCntSel",    UINT32, 2),
    ("CntAndMode",      UINT32, 1),
    ("Reserved3",       UINT32, 5),
    ("Reserved4",       UINT32, 32)
    ]

class MSR_SKYLAKE_BR_DETECT_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_BR_DETECT_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_BR_DETECT_STATUS  = 0x00000351

class MSR_SKYLAKE_BR_DETECT_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("BranchMonitoringEventSignaled",   UINT32, 1),
    ("LBRsValid",                       UINT32, 1),
    ("Reserved1",                       UINT32, 6),
    ("CntrHit0",                        UINT32, 1),
    ("CntrHit1",                        UINT32, 1),
    ("Reserved2",                       UINT32, 6),
    ("CountWindow",                     UINT32, 10),
    ("Reserved3",                       UINT32, 6),
    ("Count0",                          UINT32, 8),
    ("Count1",                          UINT32, 8),
    ("Reserved4",                       UINT32, 16)
    ]

class MSR_SKYLAKE_BR_DETECT_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_BR_DETECT_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PKG_C3_RESIDENCY  = 0x000003F8

MSR_SKYLAKE_CORE_C1_RESIDENCY  = 0x00000660

MSR_SKYLAKE_CORE_C3_RESIDENCY  = 0x00000662

MSR_SKYLAKE_PPIN_CTL  = 0x0000004E

class MSR_SKYLAKE_PPIN_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LockOut",         UINT32, 1),
    ("Enable_PPIN",     UINT32, 1),
    ("Reserved1",       UINT32, 30),
    ("Reserved2",       UINT32, 32)
    ]

class MSR_SKYLAKE_PPIN_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PPIN_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PPIN  = 0x0000004F

MSR_SKYLAKE_PLATFORM_INFO  = 0x000000CE

class MSR_SKYLAKE_PLATFORM_INFO_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 8),
    ("MaximumNon_TurboRatio",   UINT32, 8),
    ("Reserved2",               UINT32, 7),
    ("PPIN_CAP",                UINT32, 1),
    ("Reserved3",               UINT32, 4),
    ("ProgrammableRatioLimit",  UINT32, 1),
    ("ProgrammableTDPLimit",    UINT32, 1),
    ("ProgrammableTJOFFSET",    UINT32, 1),
    ("Reserved4",               UINT32, 1),
    ("Reserved5",               UINT32, 8),
    ("MaximumEfficiencyRatio",  UINT32, 8),
    ("Reserved6",               UINT32, 16)
    ]

class MSR_SKYLAKE_PLATFORM_INFO_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PLATFORM_INFO_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_SKYLAKE_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("C_StateLimit",                        UINT32, 3),
    ("Reserved1",                           UINT32, 7),
    ("MWAITRedirectionEnable",              UINT32, 1),
    ("Reserved2",                           UINT32, 4),
    ("CFGLock",                             UINT32, 1),
    ("AutomaticC_StateConversionEnable",    UINT32, 1),
    ("Reserved3",                           UINT32, 8),
    ("C3StateAutoDemotionEnable",           UINT32, 1),
    ("C1StateAutoDemotionEnable",           UINT32, 1),
    ("EnableC3Undemotion",                  UINT32, 1),
    ("EnableC1Undemotion",                  UINT32, 1),
    ("CStateDemotionEnable",                UINT32, 1),
    ("CStateUnDemotionEnable",              UINT32, 1),
    ("Reserved4",                           UINT32, 1),
    ("Reserved5",                           UINT32, 32)
    ]

class MSR_SKYLAKE_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_IA32_MCG_CAP  = 0x00000179

class MSR_SKYLAKE_IA32_MCG_CAP_REGISTER_Bits (Structure):
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

class MSR_SKYLAKE_IA32_MCG_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_MCG_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_SMM_MCA_CAP  = 0x0000017D

class MSR_SKYLAKE_SMM_MCA_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",               UINT32, 32),
    ("Reserved2",               UINT32, 26),
    ("SMM_Code_Access_Chk",     UINT32, 1),
    ("Long_Flow_Indication",    UINT32, 1),
    ("Reserved3",               UINT32, 4)
    ]

class MSR_SKYLAKE_SMM_MCA_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_SMM_MCA_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_TEMPERATURE_TARGET  = 0x000001A2

class MSR_SKYLAKE_TEMPERATURE_TARGET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 16),
    ("TemperatureTarget",   UINT32, 8),
    ("TCCActivationOffset", UINT32, 4),
    ("Reserved2",           UINT32, 4),
    ("Reserved3",           UINT32, 32)
    ]

class MSR_SKYLAKE_TEMPERATURE_TARGET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_TEMPERATURE_TARGET_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_TURBO_RATIO_LIMIT_CORES  = 0x000001AE

class MSR_SKYLAKE_TURBO_RATIO_LIMIT_CORES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("NUMCORE_0", UINT32, 8),
    ("NUMCORE_1", UINT32, 8),
    ("NUMCORE_2", UINT32, 8),
    ("NUMCORE_3", UINT32, 8),
    ("NUMCORE_4", UINT32, 8),
    ("NUMCORE_5", UINT32, 8),
    ("NUMCORE_6", UINT32, 8),
    ("NUMCORE_7", UINT32, 8)
    ]

class MSR_SKYLAKE_TURBO_RATIO_LIMIT_CORES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_TURBO_RATIO_LIMIT_CORES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_RAPL_POWER_UNIT  = 0x00000606

class MSR_SKYLAKE_RAPL_POWER_UNIT_REGISTER_Bits (Structure):
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

class MSR_SKYLAKE_RAPL_POWER_UNIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_RAPL_POWER_UNIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_DRAM_POWER_LIMIT  = 0x00000618

MSR_SKYLAKE_DRAM_ENERGY_STATUS  = 0x00000619

class MSR_SKYLAKE_DRAM_ENERGY_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Energy",      UINT32, 32),
    ("Reserved",    UINT32, 32)
    ]

class MSR_SKYLAKE_DRAM_ENERGY_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_DRAM_ENERGY_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_DRAM_PERF_STATUS  = 0x0000061B

MSR_SKYLAKE_DRAM_POWER_INFO  = 0x0000061C

MSR_SKYLAKE_MSRUNCORE_RATIO_LIMIT  = 0x00000620

class MSR_SKYLAKE_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_RATIO", UINT32, 7),
    ("Reserved1", UINT32, 1),
    ("MIN_RATIO", UINT32, 7),
    ("Reserved2", UINT32, 17),
    ("Reserved3", UINT32, 32)
    ]

class MSR_SKYLAKE_MSRUNCORE_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_PP0_ENERGY_STATUS  = 0x00000639

MSR_SKYLAKE_IA32_QM_EVTSEL  = 0x00000C8D

class MSR_SKYLAKE_IA32_QM_EVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventID",     UINT32, 8),
    ("Reserved1",   UINT32, 24),
    ("RMID",        UINT32, 10),
    ("Reserved2",   UINT32, 22)
    ]

class MSR_SKYLAKE_IA32_QM_EVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_QM_EVTSEL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_IA32_PQR_ASSOC  = 0x00000C8F

class MSR_SKYLAKE_IA32_PQR_ASSOC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("RMID",        UINT32, 10),
    ("Reserved1",   UINT32, 22),
    ("COS",         UINT32, 20),
    ("Reserved2",   UINT32, 12)
    ]

class MSR_SKYLAKE_IA32_PQR_ASSOC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_PQR_ASSOC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_SKYLAKE_IA32_L3_QOS_MASK_0   = 0x00000C90
MSR_SKYLAKE_IA32_L3_QOS_MASK_1   = 0x00000C91
MSR_SKYLAKE_IA32_L3_QOS_MASK_2   = 0x00000C92
MSR_SKYLAKE_IA32_L3_QOS_MASK_3   = 0x00000C93
MSR_SKYLAKE_IA32_L3_QOS_MASK_4   = 0x00000C94
MSR_SKYLAKE_IA32_L3_QOS_MASK_5   = 0x00000C95
MSR_SKYLAKE_IA32_L3_QOS_MASK_6   = 0x00000C96
MSR_SKYLAKE_IA32_L3_QOS_MASK_7   = 0x00000C97
MSR_SKYLAKE_IA32_L3_QOS_MASK_8   = 0x00000C98
MSR_SKYLAKE_IA32_L3_QOS_MASK_9   = 0x00000C99
MSR_SKYLAKE_IA32_L3_QOS_MASK_10  = 0x00000C9A
MSR_SKYLAKE_IA32_L3_QOS_MASK_11  = 0x00000C9B
MSR_SKYLAKE_IA32_L3_QOS_MASK_12  = 0x00000C9C
MSR_SKYLAKE_IA32_L3_QOS_MASK_13  = 0x00000C9D
MSR_SKYLAKE_IA32_L3_QOS_MASK_14  = 0x00000C9E
MSR_SKYLAKE_IA32_L3_QOS_MASK_15  = 0x00000C9F

class MSR_SKYLAKE_IA32_L3_QOS_MASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CBM",         UINT32, 20),
    ("Reserved2",   UINT32, 12),
    ("Reserved3",   UINT32, 32)
    ]

class MSR_SKYLAKE_IA32_L3_QOS_MASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SKYLAKE_IA32_L3_QOS_MASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]
