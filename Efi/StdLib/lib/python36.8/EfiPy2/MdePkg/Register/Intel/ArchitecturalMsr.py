# ArchitecturalMsr.py
#
# EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

MSR_IA32_P5_MC_ADDR             = 0x00000000

MSR_IA32_P5_MC_TYPE             = 0x00000001

MSR_IA32_MONITOR_FILTER_SIZE    = 0x00000006

MSR_IA32_TIME_STAMP_COUNTER     = 0x00000010

MSR_IA32_PLATFORM_ID            = 0x00000017

class MSR_IA32_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 32),
    ("Reserved2",   UINT32, 18),
    ("PlatformId",  UINT32, 3),
    ("Reserved3",   UINT32, 11)
  ]

class MSR_IA32_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PLATFORM_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_APIC_BASE              = 0x0000001B

class MSR_IA32_APIC_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 8),
    ("BSP",         UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("EXTD",        UINT32, 1),
    ("EN",          UINT32, 1),
    ("ApicBase",    UINT32, 20),
    ("ApicBaseHi",  UINT32, 32)
  ]

class MSR_IA32_APIC_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_APIC_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_FEATURE_CONTROL        = 0x0000003A

class MSR_IA32_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",                        UINT32, 1),
    ("EnableVmxInsideSmx",          UINT32, 1),
    ("EnableVmxOutsideSmx",         UINT32, 1),
    ("Reserved1",                   UINT32, 5),
    ("SenterLocalFunctionEnables",  UINT32, 7),
    ("SenterGlobalEnable",          UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("SgxLaunchControlEnable",      UINT32, 1),
    ("SgxEnable",                   UINT32, 1),
    ("Reserved3",                   UINT32, 1),
    ("LmceOn",                      UINT32, 1),
    ("Reserved4",                   UINT32, 11),
    ("Reserved5",                   UINT32, 32)
  ]

class MSR_IA32_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_TSC_ADJUST             = 0x0000003B

MSR_IA32_BIOS_UPDT_TRIG         = 0x00000079

MSR_IA32_BIOS_SIGN_ID           = 0x0000008B

class MSR_IA32_BIOS_SIGN_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",                    UINT32, 32),
    ("MicrocodeUpdateSignature",    UINT32, 32)
  ]

class MSR_IA32_BIOS_SIGN_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_BIOS_SIGN_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_SGXLEPUBKEYHASH0       = 0x0000008C
MSR_IA32_SGXLEPUBKEYHASH1       = 0x0000008D
MSR_IA32_SGXLEPUBKEYHASH2       = 0x0000008E
MSR_IA32_SGXLEPUBKEYHASH3       = 0x0000008F

MSR_IA32_SMM_MONITOR_CTL        = 0x0000009B

class MSR_IA32_SMM_MONITOR_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Valid",       UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("BlockSmi",    UINT32, 1),
    ("Reserved2",   UINT32, 9),
    ("MsegBase",    UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_IA32_SMM_MONITOR_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SMM_MONITOR_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

class MSEG_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("MsegHeaderRevision",  UINT32),
    ("MonitorFeatures",     UINT32),
    ("GdtrLimit",           UINT32),
    ("GdtrBaseOffset",      UINT32),
    ("CsSelector",          UINT32),
    ("EipOffset",           UINT32),
    ("EspOffset",           UINT32),
    ("Cr3Offset",           UINT32),
    ("Reserved",            UINT8 * (SIZE_2KB - 8 * sizeof (UINT32)))
  ]

STM_FEATURES_IA32E  = 0x1

MSR_IA32_SMBASE                 = 0x0000009E

MSR_IA32_PMC0  = 0x000000C1
MSR_IA32_PMC1  = 0x000000C2
MSR_IA32_PMC2  = 0x000000C3
MSR_IA32_PMC3  = 0x000000C4
MSR_IA32_PMC4  = 0x000000C5
MSR_IA32_PMC5  = 0x000000C6
MSR_IA32_PMC6  = 0x000000C7
MSR_IA32_PMC7  = 0x000000C8

MSR_IA32_MPERF                  = 0x000000E7

MSR_IA32_APERF                  = 0x000000E8

MSR_IA32_MTRRCAP                = 0x000000FE

class MSR_IA32_MTRRCAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VCNT",        UINT32, 8),
    ("FIX",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("WC",          UINT32, 1),
    ("SMRR",        UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_IA32_MTRRCAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRRCAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_SYSENTER_CS            = 0x00000174

class MSR_IA32_SYSENTER_CS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CS",          UINT32, 16),
    ("Reserved1",   UINT32, 16),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_SYSENTER_CS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SYSENTER_CS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_SYSENTER_ESP           = 0x00000175

MSR_IA32_SYSENTER_EIP           = 0x00000176

MSR_IA32_MCG_CAP                = 0x00000179

class MSR_IA32_MCG_CAP_REGISTER_Bits (Structure):
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
    ("Reserved2",   UINT32, 1),
    ("MCG_ELOG_P",  UINT32, 1),
    ("MCG_LMCE_P",  UINT32, 1),
    ("Reserved3",   UINT32, 4),
    ("Reserved4",   UINT32, 32)
  ]

class MSR_IA32_MCG_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MCG_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MCG_STATUS             = 0x0000017A

class MSR_IA32_MCG_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("RIPV",        UINT32, 1),
    ("EIPV",        UINT32, 1),
    ("MCIP",        UINT32, 1),
    ("LMCE_S",      UINT32, 1),
    ("Reserved1",   UINT32, 28),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_MCG_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MCG_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MCG_CTL                = 0x0000017B

MSR_IA32_PERFEVTSEL0  = 0x00000186
MSR_IA32_PERFEVTSEL1  = 0x00000187
MSR_IA32_PERFEVTSEL2  = 0x00000188
MSR_IA32_PERFEVTSEL3  = 0x00000189

class MSR_IA32_PERFEVTSEL_REGISTER_Bits (Structure):
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
    ("Reserved",    UINT32, 32)
  ]

class MSR_IA32_PERFEVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERFEVTSEL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_STATUS  = 0x00000198

class MSR_IA32_PERF_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("State",       UINT32, 16),
    ("Reserved1",   UINT32, 16),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_PERF_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_CTL               = 0x00000199

class MSR_IA32_PERF_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TargetState", UINT32, 16),
    ("Reserved1",   UINT32, 16),
    ("IDA",         UINT32, 1),
    ("Reserved2",   UINT32, 31)
  ]

class MSR_IA32_PERF_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_CTL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_CLOCK_MODULATION       = 0x0000019A

class MSR_IA32_CLOCK_MODULATION_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExtendedOnDemandClockModulationDutyCycle",    UINT32, 1),
    ("OnDemandClockModulationDutyCycle",            UINT32, 3),
    ("OnDemandClockModulationEnable",               UINT32, 1),
    ("Reserved1",                                   UINT32, 27),
    ("Reserved2",                                   UINT32, 32)
  ]

class MSR_IA32_CLOCK_MODULATION_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_CLOCK_MODULATION_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_THERM_INTERRUPT        = 0x0000019B

class MSR_IA32_THERM_INTERRUPT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighTempEnable",                  UINT32, 1),
    ("LowTempEnable",                   UINT32, 1),
    ("PROCHOT_Enable",                  UINT32, 1),
    ("FORCEPR_Enable",                  UINT32, 1),
    ("CriticalTempEnable",              UINT32, 1),
    ("Reserved1",                       UINT32, 3),
    ("Threshold1",                      UINT32, 7),
    ("Threshold1Enable",                UINT32, 1),
    ("Threshold2",                      UINT32, 7),
    ("Threshold2Enable",                UINT32, 1),
    ("PowerLimitNotificationEnable",    UINT32, 1),
    ("Reserved2",                       UINT32, 7),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_THERM_INTERRUPT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_THERM_INTERRUPT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_THERM_STATUS           = 0x0000019C

class MSR_IA32_THERM_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ThermalStatus",               UINT32, 1),
    ("ThermalStatusLog",            UINT32, 1),
    ("PROCHOT_FORCEPR_Event",       UINT32, 1),
    ("PROCHOT_FORCEPR_Log",         UINT32, 1),
    ("CriticalTempStatus",          UINT32, 1),
    ("CriticalTempStatusLog",       UINT32, 1),
    ("ThermalThreshold1Status",     UINT32, 1),
    ("ThermalThreshold1Log",        UINT32, 1),
    ("ThermalThreshold2Status",     UINT32, 1),
    ("ThermalThreshold2Log",        UINT32, 1),
    ("PowerLimitStatus",            UINT32, 1),
    ("PowerLimitLog",               UINT32, 1),
    ("CurrentLimitStatus",          UINT32, 1),
    ("CurrentLimitLog",             UINT32, 1),
    ("CrossDomainLimitStatus",      UINT32, 1),
    ("CrossDomainLimitLog",         UINT32, 1),
    ("DigitalReadout",              UINT32, 7),
    ("Reserved1",                   UINT32, 4),
    ("ResolutionInDegreesCelsius",  UINT32, 4),
    ("ReadingValid",                UINT32, 1),
    ("Reserved2",                   UINT32, 32)
  ]

class MSR_IA32_THERM_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_THERM_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MISC_ENABLE            = 0x000001A0

class MSR_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
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
    ("Reserved9",                       UINT32, 29)
  ]

class MSR_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_ENERGY_PERF_BIAS       = 0x000001B0

class MSR_IA32_ENERGY_PERF_BIAS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PowerPolicyPreference",   UINT32, 4),
    ("Reserved1",               UINT32, 28),
    ("Reserved2",               UINT32, 32)
  ]

class MSR_IA32_ENERGY_PERF_BIAS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_ENERGY_PERF_BIAS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PACKAGE_THERM_STATUS  = 0x000001B1

class MSR_IA32_PACKAGE_THERM_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ThermalStatus",           UINT32, 1),
    ("ThermalStatusLog",        UINT32, 1),
    ("PROCHOT_Event",           UINT32, 1),
    ("PROCHOT_Log",             UINT32, 1),
    ("CriticalTempStatus",      UINT32, 1),
    ("CriticalTempStatusLog",   UINT32, 1),
    ("ThermalThreshold1Status", UINT32, 1),
    ("ThermalThreshold1Log",    UINT32, 1),
    ("ThermalThreshold2Status", UINT32, 1),
    ("ThermalThreshold2Log",    UINT32, 1),
    ("PowerLimitStatus",        UINT32, 1),
    ("PowerLimitLog",           UINT32, 1),
    ("Reserved1",               UINT32, 4),
    ("DigitalReadout",          UINT32, 7),
    ("Reserved2",               UINT32, 9),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_IA32_PACKAGE_THERM_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PACKAGE_THERM_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PACKAGE_THERM_INTERRUPT  = 0x000001B2

class MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighTempEnable",                  UINT32, 1),
    ("LowTempEnable",                   UINT32, 1),
    ("PROCHOT_Enable",                  UINT32, 1),
    ("Reserved1",                       UINT32, 1),
    ("OverheatEnable",                  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("Threshold1",                      UINT32, 7),
    ("Threshold1Enable",                UINT32, 1),
    ("Threshold2",                      UINT32, 7),
    ("Threshold2Enable",                UINT32, 1),
    ("PowerLimitNotificationEnable",    UINT32, 1),
    ("Reserved3",                       UINT32, 7),
    ("Reserved4",                       UINT32, 32)
  ]

class MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_DEBUGCTL               = 0x000001D9

class MSR_IA32_DEBUGCTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LBR",                     UINT32, 1),
    ("BTF",                     UINT32, 1),
    ("Reserved1",               UINT32, 4),
    ("TR",                      UINT32, 1),
    ("BTS",                     UINT32, 1),
    ("BTINT",                   UINT32, 1),
    ("BTS_OFF_OS",              UINT32, 1),
    ("BTS_OFF_USR",             UINT32, 1),
    ("FREEZE_LBRS_ON_PMI",      UINT32, 1),
    ("FREEZE_PERFMON_ON_PMI",   UINT32, 1),
    ("ENABLE_UNCORE_PMI",       UINT32, 1),
    ("FREEZE_WHILE_SMM",        UINT32, 1),
    ("RTM_DEBUG",               UINT32, 1),
    ("Reserved2",               UINT32, 16),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_IA32_DEBUGCTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_DEBUGCTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_SMRR_PHYSBASE          = 0x000001F2

class MSR_IA32_SMRR_PHYSBASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 8),
    ("Reserved1",   UINT32, 4),
    ("PhysBase",    UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_SMRR_PHYSBASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SMRR_PHYSBASE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_SMRR_PHYSMASK          = 0x000001F3

class MSR_IA32_SMRR_PHYSMASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 11),
    ("Valid",       UINT32, 1),
    ("PhysMask",    UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_SMRR_PHYSMASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SMRR_PHYSMASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PLATFORM_DCA_CAP       = 0x000001F8

MSR_IA32_CPU_DCA_CAP            = 0x000001F9

MSR_IA32_DCA_0_CAP              = 0x000001FA

class MSR_IA32_DCA_0_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("DCA_ACTIVE",      UINT32, 1),
    ("TRANSACTION",     UINT32, 2),
    ("DCA_TYPE",        UINT32, 4),
    ("DCA_QUEUE_SIZE",  UINT32, 4),
    ("Reserved1",       UINT32, 2),
    ("DCA_DELAY",       UINT32, 4),
    ("Reserved2",       UINT32, 7),
    ("SW_BLOCK",        UINT32, 1),
    ("Reserved3",       UINT32, 1),
    ("HW_BLOCK",        UINT32, 1),
    ("Reserved4",       UINT32, 5),
    ("Reserved5",       UINT32, 32)
  ]

class MSR_IA32_DCA_0_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_DCA_0_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MTRR_PHYSBASE0  = 0x00000200
MSR_IA32_MTRR_PHYSBASE1  = 0x00000202
MSR_IA32_MTRR_PHYSBASE2  = 0x00000204
MSR_IA32_MTRR_PHYSBASE3  = 0x00000206
MSR_IA32_MTRR_PHYSBASE4  = 0x00000208
MSR_IA32_MTRR_PHYSBASE5  = 0x0000020A
MSR_IA32_MTRR_PHYSBASE6  = 0x0000020C
MSR_IA32_MTRR_PHYSBASE7  = 0x0000020E
MSR_IA32_MTRR_PHYSBASE8  = 0x00000210
MSR_IA32_MTRR_PHYSBASE9  = 0x00000212

MSR_IA32_MTRR_CACHE_UNCACHEABLE      = 0
MSR_IA32_MTRR_CACHE_WRITE_COMBINING  = 1
MSR_IA32_MTRR_CACHE_WRITE_THROUGH    = 4
MSR_IA32_MTRR_CACHE_WRITE_PROTECTED  = 5
MSR_IA32_MTRR_CACHE_WRITE_BACK       = 6
MSR_IA32_MTRR_CACHE_INVALID_TYPE     = 7

class MSR_IA32_MTRR_PHYSBASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 8),
    ("Reserved1",   UINT32, 4),
    ("PhysBase",    UINT32, 20),
    ("PhysBaseHi",  UINT32, 32)
  ]

class MSR_IA32_MTRR_PHYSBASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRR_PHYSBASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MTRR_PHYSMASK0  = 0x00000201
MSR_IA32_MTRR_PHYSMASK1  = 0x00000203
MSR_IA32_MTRR_PHYSMASK2  = 0x00000205
MSR_IA32_MTRR_PHYSMASK3  = 0x00000207
MSR_IA32_MTRR_PHYSMASK4  = 0x00000209
MSR_IA32_MTRR_PHYSMASK5  = 0x0000020B
MSR_IA32_MTRR_PHYSMASK6  = 0x0000020D
MSR_IA32_MTRR_PHYSMASK7  = 0x0000020F
MSR_IA32_MTRR_PHYSMASK8  = 0x00000211
MSR_IA32_MTRR_PHYSMASK9  = 0x00000213

class MSR_IA32_MTRR_PHYSMASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 11),
    ("V",           UINT32, 1),
    ("PhysMask",    UINT32, 20),
    ("PhysMaskHi",  UINT32, 32)
  ]

class MSR_IA32_MTRR_PHYSMASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRR_PHYSMASK_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MTRR_FIX64K_00000  = 0x00000250

MSR_IA32_MTRR_FIX16K_80000  = 0x00000258

MSR_IA32_MTRR_FIX16K_A0000  = 0x00000259

MSR_IA32_MTRR_FIX4K_C0000   = 0x00000268

MSR_IA32_MTRR_FIX4K_C8000   = 0x00000269

MSR_IA32_MTRR_FIX4K_D0000   = 0x0000026A

MSR_IA32_MTRR_FIX4K_D8000   = 0x0000026B

MSR_IA32_MTRR_FIX4K_E0000   = 0x0000026C

MSR_IA32_MTRR_FIX4K_E8000   = 0x0000026D

MSR_IA32_MTRR_FIX4K_F0000   = 0x0000026E

MSR_IA32_MTRR_FIX4K_F8000   = 0x0000026F

MSR_IA32_PAT                    = 0x00000277

class MSR_IA32_PAT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PA0",         UINT32, 3),
    ("Reserved1",   UINT32, 5),
    ("PA1",         UINT32, 3),
    ("Reserved2",   UINT32, 5),
    ("PA2",         UINT32, 3),
    ("Reserved3",   UINT32, 5),
    ("PA3",         UINT32, 3),
    ("Reserved4",   UINT32, 5),
    ("PA4",         UINT32, 3),
    ("Reserved5",   UINT32, 5),
    ("PA5",         UINT32, 3),
    ("Reserved6",   UINT32, 5),
    ("PA6",         UINT32, 3),
    ("Reserved7",   UINT32, 5),
    ("PA7",         UINT32, 3),
    ("Reserved8",   UINT32, 5)
  ]

class MSR_IA32_PAT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PAT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MC0_CTL2   = 0x00000280
MSR_IA32_MC1_CTL2   = 0x00000281
MSR_IA32_MC2_CTL2   = 0x00000282
MSR_IA32_MC3_CTL2   = 0x00000283
MSR_IA32_MC4_CTL2   = 0x00000284
MSR_IA32_MC5_CTL2   = 0x00000285
MSR_IA32_MC6_CTL2   = 0x00000286
MSR_IA32_MC7_CTL2   = 0x00000287
MSR_IA32_MC8_CTL2   = 0x00000288
MSR_IA32_MC9_CTL2   = 0x00000289
MSR_IA32_MC10_CTL2  = 0x0000028A
MSR_IA32_MC11_CTL2  = 0x0000028B
MSR_IA32_MC12_CTL2  = 0x0000028C
MSR_IA32_MC13_CTL2  = 0x0000028D
MSR_IA32_MC14_CTL2  = 0x0000028E
MSR_IA32_MC15_CTL2  = 0x0000028F
MSR_IA32_MC16_CTL2  = 0x00000290
MSR_IA32_MC17_CTL2  = 0x00000291
MSR_IA32_MC18_CTL2  = 0x00000292
MSR_IA32_MC19_CTL2  = 0x00000293
MSR_IA32_MC20_CTL2  = 0x00000294
MSR_IA32_MC21_CTL2  = 0x00000295
MSR_IA32_MC22_CTL2  = 0x00000296
MSR_IA32_MC23_CTL2  = 0x00000297
MSR_IA32_MC24_CTL2  = 0x00000298
MSR_IA32_MC25_CTL2  = 0x00000299
MSR_IA32_MC26_CTL2  = 0x0000029A
MSR_IA32_MC27_CTL2  = 0x0000029B
MSR_IA32_MC28_CTL2  = 0x0000029C
MSR_IA32_MC29_CTL2  = 0x0000029D
MSR_IA32_MC30_CTL2  = 0x0000029E
MSR_IA32_MC31_CTL2  = 0x0000029F

class MSR_IA32_MC_CTL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CorrectedErrorCountThreshold",    UINT32, 15),
    ("Reserved1",                       UINT32, 15),
    ("CMCI_EN",                         UINT32, 1),
    ("Reserved2",                       UINT32, 1),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_MC_CTL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MC_CTL2_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MTRR_DEF_TYPE          = 0x000002FF

class MSR_IA32_MTRR_DEF_TYPE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 3),
    ("Reserved1",   UINT32, 7),
    ("FE",          UINT32, 1),
    ("E",           UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_IA32_MTRR_DEF_TYPE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRR_DEF_TYPE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_FIXED_CTR0             = 0x00000309

MSR_IA32_FIXED_CTR1             = 0x0000030A

MSR_IA32_FIXED_CTR2             = 0x0000030B
MSR_IA32_FIXED_CTR3             = 0x0000030C
MSR_IA32_FIXED_CTR4             = 0x0000030D
MSR_IA32_FIXED_CTR5             = 0x0000030E
MSR_IA32_FIXED_CTR6             = 0x0000030F

MSR_IA32_PERF_CAPABILITIES      = 0x00000345

class MSR_IA32_PERF_CAPABILITIES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LBR_FMT",         UINT32, 6),
    ("PEBS_TRAP",       UINT32, 1),
    ("PEBS_ARCH_REG",   UINT32, 1),
    ("PEBS_REC_FMT",    UINT32, 4),
    ("SMM_FREEZE",      UINT32, 1),
    ("FW_WRITE",        UINT32, 1),
    ("Reserved1",       UINT32, 18),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_PERF_CAPABILITIES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_CAPABILITIES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_FIXED_CTR_CTRL         = 0x0000038D

class MSR_IA32_FIXED_CTR_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN0_OS",      UINT32, 1),
    ("EN0_Usr",     UINT32, 1),
    ("AnyThread0",  UINT32, 1),
    ("EN0_PMI",     UINT32, 1),
    ("EN1_OS",      UINT32, 1),
    ("EN1_Usr",     UINT32, 1),
    ("AnyThread1",  UINT32, 1),
    ("EN1_PMI",     UINT32, 1),
    ("EN2_OS",      UINT32, 1),
    ("EN2_Usr",     UINT32, 1),
    ("AnyThread2",  UINT32, 1),
    ("EN2_PMI",     UINT32, 1),
    ("Reserved1",   UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_FIXED_CTR_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_FIXED_CTR_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_GLOBAL_STATUS     = 0x0000038E

class MSR_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0",        UINT32, 1),
    ("Ovf_PMC1",        UINT32, 1),
    ("Ovf_PMC2",        UINT32, 1),
    ("Ovf_PMC3",        UINT32, 1),
    ("Reserved1",       UINT32, 28),
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
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_GLOBAL_CTRL       = 0x0000038F

class MSR_IA32_PERF_GLOBAL_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN_PMCn",         UINT32, 32),
    ("EN_FIXED_CTRn",   UINT32, 32)
  ]

class MSR_IA32_PERF_GLOBAL_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_CTRL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_GLOBAL_OVF_CTRL   = 0x00000390

class MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMCn",        UINT32, 32),
    ("Ovf_FIXED_CTRn",  UINT32, 23),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved2",       UINT32, 5),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_GLOBAL_STATUS_RESET  = 0x00000390

class MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMCn",        UINT32, 32),
    ("Ovf_FIXED_CTRn",  UINT32, 23),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved2",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_GLOBAL_STATUS_SET  = 0x00000391

class MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMCn",        UINT32, 32),
    ("Ovf_FIXED_CTRn",  UINT32, 23),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved2",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("Reserved3",       UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PERF_GLOBAL_INUSE  = 0x00000392

class MSR_IA32_PERF_GLOBAL_INUSE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("IA32_PERFEVTSELn",    UINT32, 32),
    ("IA32_FIXED_CTRn",     UINT32, 31),
    ("PMI",                 UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_INUSE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_INUSE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PEBS_ENABLE            = 0x000003F1

class MSR_IA32_PEBS_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",      UINT32, 1),
    ("Reserved1",   UINT32, 3),
    ("Reserved2",   UINT32, 28),
    ("Reserved3",   UINT32, 4),
    ("Reserved4",   UINT32, 28)
  ]

class MSR_IA32_PEBS_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PEBS_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_MC0_CTL   = 0x00000400
MSR_IA32_MC1_CTL   = 0x00000404
MSR_IA32_MC2_CTL   = 0x00000408
MSR_IA32_MC3_CTL   = 0x0000040C
MSR_IA32_MC4_CTL   = 0x00000410
MSR_IA32_MC5_CTL   = 0x00000414
MSR_IA32_MC6_CTL   = 0x00000418
MSR_IA32_MC7_CTL   = 0x0000041C
MSR_IA32_MC8_CTL   = 0x00000420
MSR_IA32_MC9_CTL   = 0x00000424
MSR_IA32_MC10_CTL  = 0x00000428
MSR_IA32_MC11_CTL  = 0x0000042C
MSR_IA32_MC12_CTL  = 0x00000430
MSR_IA32_MC13_CTL  = 0x00000434
MSR_IA32_MC14_CTL  = 0x00000438
MSR_IA32_MC15_CTL  = 0x0000043C
MSR_IA32_MC16_CTL  = 0x00000440
MSR_IA32_MC17_CTL  = 0x00000444
MSR_IA32_MC18_CTL  = 0x00000448
MSR_IA32_MC19_CTL  = 0x0000044C
MSR_IA32_MC20_CTL  = 0x00000450
MSR_IA32_MC21_CTL  = 0x00000454
MSR_IA32_MC22_CTL  = 0x00000458
MSR_IA32_MC23_CTL  = 0x0000045C
MSR_IA32_MC24_CTL  = 0x00000460
MSR_IA32_MC25_CTL  = 0x00000464
MSR_IA32_MC26_CTL  = 0x00000468
MSR_IA32_MC27_CTL  = 0x0000046C
MSR_IA32_MC28_CTL  = 0x00000470

MSR_IA32_MC0_STATUS   = 0x00000401
MSR_IA32_MC1_STATUS   = 0x00000405
MSR_IA32_MC2_STATUS   = 0x00000409
MSR_IA32_MC3_STATUS   = 0x0000040D
MSR_IA32_MC4_STATUS   = 0x00000411
MSR_IA32_MC5_STATUS   = 0x00000415
MSR_IA32_MC6_STATUS   = 0x00000419
MSR_IA32_MC7_STATUS   = 0x0000041D
MSR_IA32_MC8_STATUS   = 0x00000421
MSR_IA32_MC9_STATUS   = 0x00000425
MSR_IA32_MC10_STATUS  = 0x00000429
MSR_IA32_MC11_STATUS  = 0x0000042D
MSR_IA32_MC12_STATUS  = 0x00000431
MSR_IA32_MC13_STATUS  = 0x00000435
MSR_IA32_MC14_STATUS  = 0x00000439
MSR_IA32_MC15_STATUS  = 0x0000043D
MSR_IA32_MC16_STATUS  = 0x00000441
MSR_IA32_MC17_STATUS  = 0x00000445
MSR_IA32_MC18_STATUS  = 0x00000449
MSR_IA32_MC19_STATUS  = 0x0000044D
MSR_IA32_MC20_STATUS  = 0x00000451
MSR_IA32_MC21_STATUS  = 0x00000455
MSR_IA32_MC22_STATUS  = 0x00000459
MSR_IA32_MC23_STATUS  = 0x0000045D
MSR_IA32_MC24_STATUS  = 0x00000461
MSR_IA32_MC25_STATUS  = 0x00000465
MSR_IA32_MC26_STATUS  = 0x00000469
MSR_IA32_MC27_STATUS  = 0x0000046D
MSR_IA32_MC28_STATUS  = 0x00000471

MSR_IA32_MC0_ADDR   = 0x00000402
MSR_IA32_MC1_ADDR   = 0x00000406
MSR_IA32_MC2_ADDR   = 0x0000040A
MSR_IA32_MC3_ADDR   = 0x0000040E
MSR_IA32_MC4_ADDR   = 0x00000412
MSR_IA32_MC5_ADDR   = 0x00000416
MSR_IA32_MC6_ADDR   = 0x0000041A
MSR_IA32_MC7_ADDR   = 0x0000041E
MSR_IA32_MC8_ADDR   = 0x00000422
MSR_IA32_MC9_ADDR   = 0x00000426
MSR_IA32_MC10_ADDR  = 0x0000042A
MSR_IA32_MC11_ADDR  = 0x0000042E
MSR_IA32_MC12_ADDR  = 0x00000432
MSR_IA32_MC13_ADDR  = 0x00000436
MSR_IA32_MC14_ADDR  = 0x0000043A
MSR_IA32_MC15_ADDR  = 0x0000043E
MSR_IA32_MC16_ADDR  = 0x00000442
MSR_IA32_MC17_ADDR  = 0x00000446
MSR_IA32_MC18_ADDR  = 0x0000044A
MSR_IA32_MC19_ADDR  = 0x0000044E
MSR_IA32_MC20_ADDR  = 0x00000452
MSR_IA32_MC21_ADDR  = 0x00000456
MSR_IA32_MC22_ADDR  = 0x0000045A
MSR_IA32_MC23_ADDR  = 0x0000045E
MSR_IA32_MC24_ADDR  = 0x00000462
MSR_IA32_MC25_ADDR  = 0x00000466
MSR_IA32_MC26_ADDR  = 0x0000046A
MSR_IA32_MC27_ADDR  = 0x0000046E
MSR_IA32_MC28_ADDR  = 0x00000472

MSR_IA32_MC0_MISC   = 0x00000403
MSR_IA32_MC1_MISC   = 0x00000407
MSR_IA32_MC2_MISC   = 0x0000040B
MSR_IA32_MC3_MISC   = 0x0000040F
MSR_IA32_MC4_MISC   = 0x00000413
MSR_IA32_MC5_MISC   = 0x00000417
MSR_IA32_MC6_MISC   = 0x0000041B
MSR_IA32_MC7_MISC   = 0x0000041F
MSR_IA32_MC8_MISC   = 0x00000423
MSR_IA32_MC9_MISC   = 0x00000427
MSR_IA32_MC10_MISC  = 0x0000042B
MSR_IA32_MC11_MISC  = 0x0000042F
MSR_IA32_MC12_MISC  = 0x00000433
MSR_IA32_MC13_MISC  = 0x00000437
MSR_IA32_MC14_MISC  = 0x0000043B
MSR_IA32_MC15_MISC  = 0x0000043F
MSR_IA32_MC16_MISC  = 0x00000443
MSR_IA32_MC17_MISC  = 0x00000447
MSR_IA32_MC18_MISC  = 0x0000044B
MSR_IA32_MC19_MISC  = 0x0000044F
MSR_IA32_MC20_MISC  = 0x00000453
MSR_IA32_MC21_MISC  = 0x00000457
MSR_IA32_MC22_MISC  = 0x0000045B
MSR_IA32_MC23_MISC  = 0x0000045F
MSR_IA32_MC24_MISC  = 0x00000463
MSR_IA32_MC25_MISC  = 0x00000467
MSR_IA32_MC26_MISC  = 0x0000046B
MSR_IA32_MC27_MISC  = 0x0000046F
MSR_IA32_MC28_MISC  = 0x00000473

MSR_IA32_VMX_BASIC  = 0x00000480

class MSR_IA32_VMX_BASIC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VmcsRevisonId",       UINT32, 31),
    ("MustBeZero",          UINT32, 1),
    ("VmcsSize",            UINT32, 13),
    ("Reserved1",           UINT32, 3),
    ("VmcsAddressWidth",    UINT32, 1),
    ("DualMonitor",         UINT32, 1),
    ("MemoryType",          UINT32, 4),
    ("InsOutsReporting",    UINT32, 1),
    ("VmxControls",         UINT32, 1),
    ("Reserved2",           UINT32, 8)
  ]

class MSR_IA32_VMX_BASIC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_VMX_BASIC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_VMX_PINBASED_CTLS      = 0x00000481

MSR_IA32_VMX_PROCBASED_CTLS     = 0x00000482

MSR_IA32_VMX_EXIT_CTLS          = 0x00000483

MSR_IA32_VMX_ENTRY_CTLS         = 0x00000484

MSR_IA32_VMX_MISC               = 0x00000485

class IA32_VMX_MISC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VmxTimerRatio",                       UINT32, 5),
    ("VmExitEferLma",                       UINT32, 1),
    ("HltActivityStateSupported",           UINT32, 1),
    ("ShutdownActivityStateSupported",      UINT32, 1),
    ("WaitForSipiActivityStateSupported",   UINT32, 1),
    ("Reserved1",                           UINT32, 5),
    ("ProcessorTraceSupported",             UINT32, 1),
    ("SmBaseMsrSupported",                  UINT32, 1),
    ("NumberOfCr3TargetValues",             UINT32, 9),
    ("MsrStoreListMaximum",                 UINT32, 3),
    ("BlockSmiSupported",                   UINT32, 1),
    ("VmWriteSupported",                    UINT32, 1),
    ("VmInjectSupported",                   UINT32, 1),
    ("Reserved2",                           UINT32, 1),
    ("MsegRevisionIdentifier",              UINT32, 32)
  ]

class IA32_VMX_MISC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    IA32_VMX_MISC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_VMX_CR0_FIXED0             = 0x00000486

MSR_IA32_VMX_CR4_FIXED0             = 0x00000488

MSR_IA32_VMX_CR4_FIXED1             = 0x00000489

MSR_IA32_VMX_VMCS_ENUM              = 0x0000048A

MSR_IA32_VMX_PROCBASED_CTLS2        = 0x0000048B

MSR_IA32_VMX_EPT_VPID_CAP           = 0x0000048C

MSR_IA32_VMX_TRUE_PINBASED_CTLS     = 0x0000048D

MSR_IA32_VMX_TRUE_PROCBASED_CTLS    = 0x0000048E

MSR_IA32_VMX_TRUE_EXIT_CTLS         = 0x0000048F

MSR_IA32_VMX_TRUE_ENTRY_CTLS        = 0x00000490

MSR_IA32_VMX_VMFUNC                 = 0x00000491

MSR_IA32_A_PMC0  = 0x000004C1
MSR_IA32_A_PMC1  = 0x000004C2
MSR_IA32_A_PMC2  = 0x000004C3
MSR_IA32_A_PMC3  = 0x000004C4
MSR_IA32_A_PMC4  = 0x000004C5
MSR_IA32_A_PMC5  = 0x000004C6
MSR_IA32_A_PMC6  = 0x000004C7
MSR_IA32_A_PMC7  = 0x000004C8

MSR_IA32_MCG_EXT_CTL            = 0x000004D0

class MSR_IA32_MCG_EXT_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LMCE_EN",     UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_MCG_EXT_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MCG_EXT_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_SGX_SVN_STATUS         = 0x00000500

class MSR_IA32_SGX_SVN_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",            UINT32, 1),
    ("Reserved1",       UINT32, 15),
    ("SGX_SVN_SINIT",   UINT32, 8),
    ("Reserved2",       UINT32, 8),
    ("Reserved3",       UINT32, 32)
  ]

class MSR_IA32_SGX_SVN_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SGX_SVN_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_RTIT_OUTPUT_BASE       = 0x00000560

class MSR_IA32_RTIT_OUTPUT_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32, 7),
    ("Base",        UINT32, 25),
    ("BaseHi",      UINT32, 32)
  ]

class MSR_IA32_RTIT_OUTPUT_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_OUTPUT_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_RTIT_OUTPUT_MASK_PTRS  = 0x00000561

class MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",            UINT32, 7),
    ("MaskOrTableOffset",   UINT32, 25),
    ("OutputOffset",        UINT32, 32)
  ]

class MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

class RTIT_TOPA_TABLE_ENTRY_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("END",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("INT",         UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("STOP",        UINT32, 1),
    ("Reserved3",   UINT32, 1),
    ("Size",        UINT32, 4),
    ("Reserved4",   UINT32, 2),
    ("Base",        UINT32, 20),
    ("BaseHi",      UINT32, 32)
  ]

class RTIT_TOPA_TABLE_ENTRY (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    RTIT_TOPA_TABLE_ENTRY_Bits),
    ("Uint64",  UINT64)
  ]

RtitTopaMemorySize4K    = 0
RtitTopaMemorySize8K    = 1 
RtitTopaMemorySize16K   = 2 
RtitTopaMemorySize32K   = 3 
RtitTopaMemorySize64K   = 4 
RtitTopaMemorySize128K  = 5 
RtitTopaMemorySize256K  = 6 
RtitTopaMemorySize512K  = 7 
RtitTopaMemorySize1M    = 8 
RtitTopaMemorySize2M    = 9 
RtitTopaMemorySize4M    = 10
RtitTopaMemorySize8M    = 11
RtitTopaMemorySize16M   = 12
RtitTopaMemorySize32M   = 13
RtitTopaMemorySize64M   = 14
RtitTopaMemorySize128M  = 15
RTIT_TOPA_MEMORY_SIZE   = ENUM

MSR_IA32_RTIT_CTL               = 0x00000570

class MSR_IA32_RTIT_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TraceEn",     UINT32, 1),
    ("CYCEn",       UINT32, 1),
    ("OS",          UINT32, 1),
    ("User",        UINT32, 1),
    ("PwrEvtEn",    UINT32, 1),
    ("FUPonPTW",    UINT32, 1),
    ("FabricEn",    UINT32, 1),
    ("CR3",         UINT32, 1),
    ("ToPA",        UINT32, 1),
    ("MTCEn",       UINT32, 1),
    ("TSCEn",       UINT32, 1),
    ("DisRETC",     UINT32, 1),
    ("PTWEn",       UINT32, 1),
    ("BranchEn",    UINT32, 1),
    ("MTCFreq",     UINT32, 4),
    ("Reserved3",   UINT32, 1),
    ("CYCThresh",   UINT32, 4),
    ("Reserved4",   UINT32, 1),
    ("PSBFreq",     UINT32, 4),
    ("Reserved5",   UINT32, 4),
    ("ADDR0_CFG",   UINT32, 4),
    ("ADDR1_CFG",   UINT32, 4),
    ("ADDR2_CFG",   UINT32, 4),
    ("ADDR3_CFG",   UINT32, 4),
    ("Reserved6",   UINT32, 16)
  ]

class MSR_IA32_RTIT_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_CTL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_RTIT_STATUS  = 0x00000571

class MSR_IA32_RTIT_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FilterEn",        UINT32, 1),
    ("ContexEn",        UINT32, 1),
    ("TriggerEn",       UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("Error",           UINT32, 1),
    ("Stopped",         UINT32, 1),
    ("Reserved2",       UINT32, 26),
    ("PacketByteCnt",   UINT32, 17),
    ("Reserved3",       UINT32, 15)
  ]

class MSR_IA32_RTIT_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_RTIT_CR3_MATCH         = 0x00000572

class MSR_IA32_RTIT_CR3_MATCH_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32, 5),
    ("Cr3",         UINT32, 27),
    ("Cr3Hi",       UINT32, 32)
  ]

class MSR_IA32_RTIT_CR3_MATCH_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_CR3_MATCH_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_RTIT_ADDR0_A  = 0x00000580
MSR_IA32_RTIT_ADDR1_A  = 0x00000582
MSR_IA32_RTIT_ADDR2_A  = 0x00000584
MSR_IA32_RTIT_ADDR3_A  = 0x00000586

MSR_IA32_RTIT_ADDR0_B  = 0x00000581
MSR_IA32_RTIT_ADDR1_B  = 0x00000583
MSR_IA32_RTIT_ADDR2_B  = 0x00000585
MSR_IA32_RTIT_ADDR3_B  = 0x00000587

class MSR_IA32_RTIT_ADDR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VirtualAddress",      UINT32, 32),
    ("VirtualAddressHi",    UINT32, 16),
    ("SignExt_VA",          UINT32, 16)
  ]

class MSR_IA32_RTIT_ADDR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_ADDR_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_DS_AREA                = 0x00000600

MSR_IA32_TSC_DEADLINE           = 0x000006E0

MSR_IA32_PM_ENABLE              = 0x00000770

class MSR_IA32_PM_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HWP_ENABLE",  UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_PM_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PM_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_HWP_CAPABILITIES       = 0x00000771

class MSR_IA32_HWP_CAPABILITIES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Highest_Performance",         UINT32, 8),
    ("Guaranteed_Performance",      UINT32, 8),
    ("Most_Efficient_Performance",  UINT32, 8),
    ("Lowest_Performance",          UINT32, 8),
    ("Reserved",                    UINT32, 32)
  ]

class MSR_IA32_HWP_CAPABILITIES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_CAPABILITIES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_HWP_REQUEST_PKG        = 0x00000772

class MSR_IA32_HWP_REQUEST_PKG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Minimum_Performance",             UINT32, 8),
    ("Maximum_Performance",             UINT32, 8),
    ("Desired_Performance",             UINT32, 8),
    ("Energy_Performance_Preference",   UINT32, 8),
    ("Activity_Window",                 UINT32, 10),
    ("Reserved",                        UINT32, 22)
  ]

class MSR_IA32_HWP_REQUEST_PKG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_REQUEST_PKG_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_HWP_INTERRUPT          = 0x00000773

class MSR_IA32_HWP_INTERRUPT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN_Guaranteed_Performance_Change",    UINT32, 1),
    ("EN_Excursion_Minimum",                UINT32, 1),
    ("Reserved1",                           UINT32, 30),
    ("Reserved2",                           UINT32, 32)
  ]

class MSR_IA32_HWP_INTERRUPT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_INTERRUPT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_HWP_REQUEST            = 0x00000774

class MSR_IA32_HWP_REQUEST_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Minimum_Performance",             UINT32, 8),
    ("Maximum_Performance",             UINT32, 8),
    ("Desired_Performance",             UINT32, 8),
    ("Energy_Performance_Preference",   UINT32, 8),
    ("Activity_Window",                 UINT32, 10),
    ("Package_Control",                 UINT32, 1),
    ("Reserved",                        UINT32, 21)
  ]

class MSR_IA32_HWP_REQUEST_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_REQUEST_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_HWP_STATUS             = 0x00000777

class MSR_IA32_HWP_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Guaranteed_Performance_Change",   UINT32, 1),
    ("Reserved1",                       UINT32, 1),
    ("Excursion_To_Minimum",            UINT32, 1),
    ("Reserved2",                       UINT32, 29),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_HWP_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_X2APIC_APICID      = 0x00000802

MSR_IA32_X2APIC_VERSION     = 0x00000803

MSR_IA32_X2APIC_TPR         = 0x00000808

MSR_IA32_X2APIC_PPR         = 0x0000080A

MSR_IA32_X2APIC_EOI         = 0x0000080B

MSR_IA32_X2APIC_LDR         = 0x0000080D

MSR_IA32_X2APIC_SIVR        = 0x0000080F

MSR_IA32_X2APIC_ISR0  = 0x00000810
MSR_IA32_X2APIC_ISR1  = 0x00000811
MSR_IA32_X2APIC_ISR2  = 0x00000812
MSR_IA32_X2APIC_ISR3  = 0x00000813
MSR_IA32_X2APIC_ISR4  = 0x00000814
MSR_IA32_X2APIC_ISR5  = 0x00000815
MSR_IA32_X2APIC_ISR6  = 0x00000816
MSR_IA32_X2APIC_ISR7  = 0x00000817

MSR_IA32_X2APIC_TMR0  = 0x00000818
MSR_IA32_X2APIC_TMR1  = 0x00000819
MSR_IA32_X2APIC_TMR2  = 0x0000081A
MSR_IA32_X2APIC_TMR3  = 0x0000081B
MSR_IA32_X2APIC_TMR4  = 0x0000081C
MSR_IA32_X2APIC_TMR5  = 0x0000081D
MSR_IA32_X2APIC_TMR6  = 0x0000081E
MSR_IA32_X2APIC_TMR7  = 0x0000081F

MSR_IA32_X2APIC_IRR0  = 0x00000820
MSR_IA32_X2APIC_IRR1  = 0x00000821
MSR_IA32_X2APIC_IRR2  = 0x00000822
MSR_IA32_X2APIC_IRR3  = 0x00000823
MSR_IA32_X2APIC_IRR4  = 0x00000824
MSR_IA32_X2APIC_IRR5  = 0x00000825
MSR_IA32_X2APIC_IRR6  = 0x00000826
MSR_IA32_X2APIC_IRR7  = 0x00000827

MSR_IA32_X2APIC_ESR             = 0x00000828

MSR_IA32_X2APIC_LVT_CMCI        = 0x0000082F

MSR_IA32_X2APIC_ICR             = 0x00000830

MSR_IA32_X2APIC_LVT_TIMER       = 0x00000832

MSR_IA32_X2APIC_LVT_THERMAL     = 0x00000833

MSR_IA32_X2APIC_LVT_PMI         = 0x00000834

MSR_IA32_X2APIC_LVT_LINT0       = 0x00000835

MSR_IA32_X2APIC_LVT_LINT1       = 0x00000836

MSR_IA32_X2APIC_LVT_ERROR       = 0x00000837

MSR_IA32_X2APIC_INIT_COUNT      = 0x00000838

MSR_IA32_X2APIC_CUR_COUNT       = 0x00000839

MSR_IA32_X2APIC_DIV_CONF        = 0x0000083E

MSR_IA32_X2APIC_SELF_IPI        = 0x0000083F

MSR_IA32_TME_ACTIVATE           = 0x00000982

class MSR_IA32_TME_ACTIVATE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",                UINT32, 1),
    ("TmeEnable",           UINT32, 1),
    ("KeySelect",           UINT32, 1),
    ("SaveKeyForStandby",   UINT32, 1),
    ("TmePolicy",           UINT32, 4),
    ("Reserved",            UINT32, 23),
    ("TmeBypassMode",       UINT32, 1),
    ("MkTmeKeyidBits",      UINT32, 4),
    ("Reserved2",           UINT32, 12),
    ("MkTmeCryptoAlgs",     UINT32, 16),
  ]

class MSR_IA32_TME_ACTIVATE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_TME_ACTIVATE_REGISTER_Bits),
    ("Uint32",  UINT32 * 2),
    ("Uint64",  UINT64)
  ]

MSR_IA32_DEBUG_INTERFACE        = 0x00000C80

class MSR_IA32_DEBUG_INTERFACE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",          UINT32, 1),
    ("Reserved1",       UINT32, 29),
    ("Lock",            UINT32, 1),
    ("DebugOccurred",   UINT32, 1),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_DEBUG_INTERFACE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_DEBUG_INTERFACE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_L3_QOS_CFG             = 0x00000C81

class MSR_IA32_L3_QOS_CFG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",          UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_L3_QOS_CFG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_L3_QOS_CFG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_L2_QOS_CFG             = 0x00000C82

class MSR_IA32_L2_QOS_CFG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",          UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_L2_QOS_CFG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_L2_QOS_CFG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_QM_EVTSEL              = 0x00000C8D

class MSR_IA32_QM_EVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventID",                 UINT32, 8),
    ("Reserved",                UINT32, 24),
    ("ResourceMonitoringID",    UINT32, 32)
  ]

class MSR_IA32_QM_EVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_QM_EVTSEL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_QM_CTR                 = 0x00000C8E

class MSR_IA32_QM_CTR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ResourceMonitoredData",   UINT32, 32),
    ("ResourceMonitoredDataHi", UINT32, 30),
    ("Unavailable",             UINT32, 1),
    ("Error",                   UINT32, 1)
  ]

class MSR_IA32_QM_CTR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_QM_CTR_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PQR_ASSOC              = 0x00000C8F

class MSR_IA32_PQR_ASSOC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ResourceMonitoringID",    UINT32, 32),
    ("COS",                     UINT32, 30)
  ]

class MSR_IA32_PQR_ASSOC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PQR_ASSOC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_BNDCFGS                = 0x00000D90

class MSR_IA32_BNDCFGS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN",          UINT32, 1),
    ("BNDPRESERVE", UINT32, 1),
    ("Reserved",    UINT32, 10),
    ("Base",        UINT32, 20),
    ("BaseHi",      UINT32, 32)
  ]

class MSR_IA32_BNDCFGS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_BNDCFGS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_IA32_XSS                    = 0x00000DA0

class MSR_IA32_XSS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                       UINT32, 8),
    ("TracePacketConfigurationState",   UINT32, 1),
    ("Reserved2",                       UINT32, 23),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_XSS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_XSS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PKG_HDC_CTL            = 0x00000DB0

class MSR_IA32_PKG_HDC_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HDC_Pkg_Enable",  UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_PKG_HDC_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PKG_HDC_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_PM_CTL1                = 0x00000DB1

class MSR_IA32_PM_CTL1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HDC_Allow_Block", UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_PM_CTL1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PM_CTL1_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_THREAD_STALL           = 0x00000DB2

MSR_IA32_EFER                   = 0xC0000080

class MSR_IA32_EFER_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SCE",         UINT32, 1),
    ("Reserved1",   UINT32, 7),
    ("LME",         UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("LMA",         UINT32, 1),
    ("NXE",         UINT32, 1),
    ("Reserved3",   UINT32, 20),
    ("Reserved4",   UINT32, 32)
  ]

class MSR_IA32_EFER_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_EFER_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_IA32_STAR                   = 0xC0000081

MSR_IA32_LSTAR                  = 0xC0000082

MSR_IA32_CSTAR                  = 0xC0000083

MSR_IA32_FMASK                  = 0xC0000084

MSR_IA32_FS_BASE                = 0xC0000100

MSR_IA32_GS_BASE                = 0xC0000101

MSR_IA32_KERNEL_GS_BASE         = 0xC0000102

MSR_IA32_TSC_AUX                = 0xC0000103

class MSR_IA32_TSC_AUX_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("AUX",         UINT32, 32),
    ("Reserved",    UINT32, 32)
  ]

class MSR_IA32_TSC_AUX_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_TSC_AUX_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

