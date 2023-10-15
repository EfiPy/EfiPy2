# Cpuid.py
#
# EfiPy2.MdePkg.Register.Intel.Cpuid
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

CPUID_SIGNATURE  = 0x00

CPUID_SIGNATURE_GENUINE_INTEL_EBX  = SIGNATURE_32 ('G', 'e', 'n', 'u')
CPUID_SIGNATURE_GENUINE_INTEL_EDX  = SIGNATURE_32 ('i', 'n', 'e', 'I')
CPUID_SIGNATURE_GENUINE_INTEL_ECX  = SIGNATURE_32 ('n', 't', 'e', 'l')

CPUID_VERSION_INFO  = 0x01

class CPUID_VERSION_INFO_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SteppingId",          UINT32, 4), # [Bits   3:0] Stepping ID
    ("Model",               UINT32, 4), # [Bits   7:4] Model
    ("FamilyId",            UINT32, 4), # [Bits  11:8] Family
    ("ProcessorType",       UINT32, 2), # [Bits 13:12] Processor Type
    ("Reserved1",           UINT32, 2), # [Bits 15:14] Reserved
    ("ExtendedModelId",     UINT32, 4), # [Bits 19:16] Extended Model ID
    ("ExtendedFamilyId",    UINT32, 8), # [Bits 27:20] Extended Family ID
    ("Reserved2",           UINT32, 4)  # Reserved
  ]

class CPUID_VERSION_INFO_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_VERSION_INFO_EAX_Bits),
    ("Uint32",  UINT32)
  ]

CPUID_VERSION_INFO_EAX_PROCESSOR_TYPE_ORIGINAL_OEM_PROCESSOR     = 0x00
CPUID_VERSION_INFO_EAX_PROCESSOR_TYPE_INTEL_OVERDRIVE_PROCESSOR  = 0x01
CPUID_VERSION_INFO_EAX_PROCESSOR_TYPE_DUAL_PROCESSOR             = 0x02

class CPUID_VERSION_INFO_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("BrandIndex",                                  UINT32, 8),
    ("CacheLineSize",                               UINT32, 8),
    ("MaximumAddressableIdsForLogicalProcessors",   UINT32, 8),
    ("InitialLocalApicId",                          UINT32, 8)
  ]

class CPUID_VERSION_INFO_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_VERSION_INFO_EBX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_VERSION_INFO_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SSE3",                UINT32, 1),
    ("PCLMULQDQ",           UINT32, 1),
    ("DTES64",              UINT32, 1),
    ("MONITOR",             UINT32, 1),
    ("DS_CPL",              UINT32, 1),
    ("VMX",                 UINT32, 1),
    ("SMX",                 UINT32, 1),
    ("EIST",                UINT32, 1),
    ("TM2",                 UINT32, 1),
    ("SSSE3",               UINT32, 1),
    ("CNXT_ID",             UINT32, 1),
    ("SDBG",                UINT32, 1),
    ("FMA",                 UINT32, 1),
    ("CMPXCHG16B",          UINT32, 1),
    ("xTPR_Update_Control", UINT32, 1),
    ("PDCM",                UINT32, 1),
    ("Reserved",            UINT32, 1),
    ("PCID",                UINT32, 1),
    ("DCA",                 UINT32, 1),
    ("SSE4_1",              UINT32, 1),
    ("SSE4_2",              UINT32, 1),
    ("x2APIC",              UINT32, 1),
    ("MOVBE",               UINT32, 1),
    ("POPCNT",              UINT32, 1),
    ("TSC_Deadline",        UINT32, 1),
    ("AESNI",               UINT32, 1),
    ("XSAVE",               UINT32, 1),
    ("OSXSAVE",             UINT32, 1),
    ("AVX",                 UINT32, 1),
    ("F16C",                UINT32, 1),
    ("RDRAND",              UINT32, 1),
    ("ParaVirtualized",     UINT32, 1)
  ]

class CPUID_VERSION_INFO_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_VERSION_INFO_ECX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_VERSION_INFO_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FPU",         UINT32, 1),
    ("VME",         UINT32, 1),
    ("DE",          UINT32, 1),
    ("PSE",         UINT32, 1),
    ("TSC",         UINT32, 1),
    ("MSR",         UINT32, 1),
    ("PAE",         UINT32, 1),
    ("MCE",         UINT32, 1),
    ("CX8",         UINT32, 1),
    ("APIC",        UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("SEP",         UINT32, 1),
    ("MTRR",        UINT32, 1),
    ("PGE",         UINT32, 1),
    ("MCA",         UINT32, 1),
    ("CMOV",        UINT32, 1),
    ("PAT",         UINT32, 1),
    ("PSE_36",      UINT32, 1),
    ("PSN",         UINT32, 1),
    ("CLFSH",       UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("DS",          UINT32, 1),
    ("ACPI",        UINT32, 1),
    ("MMX",         UINT32, 1),
    ("FXSR",        UINT32, 1),
    ("SSE",         UINT32, 1),
    ("SSE2",        UINT32, 1),
    ("SS",          UINT32, 1),
    ("HTT",         UINT32, 1),
    ("TM",          UINT32, 1),
    ("Reserved3",   UINT32, 1),
    ("PBE",         UINT32, 1)
  ]

class CPUID_VERSION_INFO_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_VERSION_INFO_EDX_Bits),
    ("Uint32",  UINT32)
  ]

CPUID_CACHE_INFO  = 0x02

class CPUID_CACHE_INFO_CACHE_TLB_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32, 31),
    ("NotValid",    UINT32, 1)
  ]

class CPUID_CACHE_INFO_CACHE_TLB (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_CACHE_INFO_CACHE_TLB_Bits),
    ("CacheDescriptor", UINT8 * 4),
    ("Uint32",          UINT32)
  ]

CPUID_SERIAL_NUMBER = 0x03

CPUID_CACHE_PARAMS  = 0x04

class CPUID_CACHE_PARAMS_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CacheType",                                   UINT32, 5),
    ("CacheLevel",                                  UINT32, 3),
    ("SelfInitializingCache",                       UINT32, 1),
    ("FullyAssociativeCache",                       UINT32, 1),
    ("Reserved",                                    UINT32, 4),
    ("MaximumAddressableIdsForLogicalProcessors",   UINT32, 12),
    ("MaximumAddressableIdsForProcessorCores",      UINT32, 6)
  ]

class CPUID_CACHE_PARAMS_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_CACHE_PARAMS_EAX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_CACHE_PARAMS_CACHE_TYPE_NULL         = 0x00
CPUID_CACHE_PARAMS_CACHE_TYPE_DATA         = 0x01
CPUID_CACHE_PARAMS_CACHE_TYPE_INSTRUCTION  = 0x02
CPUID_CACHE_PARAMS_CACHE_TYPE_UNIFIED      = 0x03

class CPUID_CACHE_PARAMS_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LineSize",        UINT32, 12),
    ("LinePartitions",  UINT32, 10),
    ("Ways",            UINT32, 10)
  ]

class CPUID_CACHE_PARAMS_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_CACHE_PARAMS_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_CACHE_PARAMS_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Invalidate",              UINT32, 1),
    ("CacheInclusiveness",      UINT32, 1),
    ("ComplexCacheIndexing",    UINT32, 1),
    ("Reserved",                UINT32, 29)
  ]

class CPUID_CACHE_PARAMS_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_CACHE_PARAMS_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_MONITOR_MWAIT  = 0x05

class CPUID_MONITOR_MWAIT_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SmallestMonitorLineSize", UINT32, 16),
    ("Reserved",                UINT32, 16)
  ]

class CPUID_MONITOR_MWAIT_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_MONITOR_MWAIT_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_MONITOR_MWAIT_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LargestMonitorLineSize",  UINT32, 16),
    ("Reserved",                UINT32, 16)
  ]

class CPUID_MONITOR_MWAIT_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_MONITOR_MWAIT_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_MONITOR_MWAIT_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExtensionsSupported", UINT32, 1),
    ("InterruptAsBreak",    UINT32, 1),
    ("Reserved",            UINT32, 30)
  ]

class CPUID_MONITOR_MWAIT_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_MONITOR_MWAIT_ECX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_MONITOR_MWAIT_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("C0States", UINT32, 4),
    ("C1States", UINT32, 4),
    ("C2States", UINT32, 4),
    ("C3States", UINT32, 4),
    ("C4States", UINT32, 4),
    ("C5States", UINT32, 4),
    ("C6States", UINT32, 4),
    ("C7States", UINT32, 4)
  ]

class CPUID_MONITOR_MWAIT_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_MONITOR_MWAIT_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_THERMAL_POWER_MANAGEMENT  = 0x06

class CPUID_THERMAL_POWER_MANAGEMENT_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("DigitalTemperatureSensor",                UINT32, 1),
    ("TurboBoostTechnology",                    UINT32, 1),
    ("ARAT",                                    UINT32, 1),
    ("Reserved1",                               UINT32, 1),
    ("PLN",                                     UINT32, 1),
    ("ECMD",                                    UINT32, 1),
    ("PTM",                                     UINT32, 1),
    ("HWP",                                     UINT32, 1),
    ("HWP_Notification",                        UINT32, 1),
    ("HWP_Activity_Window",                     UINT32, 1),
    ("HWP_Energy_Performance_Preference",       UINT32, 1),
    ("HWP_Package_Level_Request",               UINT32, 1),
    ("Reserved2",                               UINT32, 1),
    ("HDC",                                     UINT32, 1),
    ("TurboBoostMaxTechnology30",               UINT32, 1),
    ("HWPCapabilities",                         UINT32, 1),
    ("HWPPECIOverride",                         UINT32, 1),
    ("FlexibleHWP",                             UINT32, 1),
    ("FastAccessMode",                          UINT32, 1),
    ("Reserved4",                               UINT32, 1),
    ("IgnoringIdleLogicalProcessorHWPRequest",  UINT32, 1),
    ("Reserved5",                               UINT32, 11)
  ]

class CPUID_THERMAL_POWER_MANAGEMENT_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_THERMAL_POWER_MANAGEMENT_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_THERMAL_POWER_MANAGEMENT_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptThresholds", UINT32, 4),
    ("Reserved",            UINT32, 28)
  ]

class CPUID_THERMAL_POWER_MANAGEMENT_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_THERMAL_POWER_MANAGEMENT_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_THERMAL_POWER_MANAGEMENT_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HardwareCoordinationFeedback",    UINT32, 1),
    ("Reserved1",                       UINT32, 2),
    ("PerformanceEnergyBias",           UINT32, 1),
    ("Reserved2",                       UINT32, 28)
  ]

class CPUID_THERMAL_POWER_MANAGEMENT_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_THERMAL_POWER_MANAGEMENT_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS                 = 0x07

CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_INFO   = 0x00

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FSGSBASE",                UINT32, 1),
    ("IA32_TSC_ADJUST",         UINT32, 1),
    ("SGX",                     UINT32, 1),
    ("BMI1",                    UINT32, 1),
    ("HLE",                     UINT32, 1),
    ("AVX2",                    UINT32, 1),
    ("FDP_EXCPTN_ONLY",         UINT32, 1),
    ("SMEP",                    UINT32, 1),
    ("BMI2",                    UINT32, 1),
    ("EnhancedRepMovsbStosb",   UINT32, 1),
    ("INVPCID",                 UINT32, 1),
    ("RTM",                     UINT32, 1),
    ("RDT_M",                   UINT32, 1),
    ("DeprecateFpuCsDs",        UINT32, 1),
    ("MPX",                     UINT32, 1),
    ("RDT_A",                   UINT32, 1),
    ("AVX512F",                 UINT32, 1),
    ("AVX512DQ",                UINT32, 1),
    ("RDSEED",                  UINT32, 1),
    ("ADX",                     UINT32, 1),
    ("SMAP",                    UINT32, 1),
    ("AVX512_IFMA",             UINT32, 1),
    ("Reserved6",               UINT32, 1),
    ("CLFLUSHOPT",              UINT32, 1),
    ("CLWB",                    UINT32, 1),
    ("IntelProcessorTrace",     UINT32, 1),
    ("AVX512PF",                UINT32, 1),
    ("AVX512ER",                UINT32, 1),
    ("AVX512CD",                UINT32, 1),
    ("SHA",                     UINT32, 1),
    ("AVX512BW",                UINT32, 1),
    ("AVX512VL",                UINT32, 1)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PREFETCHWT1",         UINT32, 1),
    ("AVX512_VBMI",         UINT32, 1),
    ("UMIP",                UINT32, 1),
    ("PKU",                 UINT32, 1),
    ("OSPKE",               UINT32, 1),
    ("Reserved8",           UINT32, 8),
    ("TME_EN",              UINT32, 1),
    ("AVX512_VPOPCNTDQ",    UINT32, 1),
    ("Reserved7",           UINT32, 1),
    ("FiveLevelPage",       UINT32, 1),
    ("MAWAU",               UINT32, 5),
    ("RDPID",               UINT32, 1),
    ("Reserved3",           UINT32, 7),
    ("SGX_LC",              UINT32, 1),
    ("Reserved4",           UINT32, 1)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_ECX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                               UINT32, 2),
    ("AVX512_4VNNIW",                           UINT32, 1),
    ("AVX512_4FMAPS",                           UINT32, 1),
    ("Reserved4",                               UINT32, 11),
    ("Hybrid",                                  UINT32, 1),
    ("Reserved5",                               UINT32, 10),
    ("EnumeratesSupportForIBRSAndIBPB",         UINT32, 1),
    ("EnumeratesSupportForSTIBP",               UINT32, 1),
    ("EnumeratesSupportForL1D_FLUSH",           UINT32, 1),
    ("EnumeratesSupportForCapability",          UINT32, 1),
    ("EnumeratesSupportForCoreCapabilitiesMsr", UINT32, 1),
    ("EnumeratesSupportForSSBD",                UINT32, 1)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_DIRECT_CACHE_ACCESS_INFO              = 0x09

CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING  = 0x0A

class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ArchPerfMonVerID",                UINT32, 8),
    ("PerformanceMonitorCounters",      UINT32, 8),
    ("PerformanceMonitorCounterWidth",  UINT32, 8),
    ("EbxBitVectorLength",              UINT32, 8)
  ]

class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("UnhaltedCoreCycles",          UINT32, 1),
    ("InstructionsRetired",         UINT32, 1),
    ("UnhaltedReferenceCycles",     UINT32, 1),
    ("LastLevelCacheReferences",    UINT32, 1),
    ("LastLevelCacheMisses",        UINT32, 1),
    ("BranchInstructionsRetired",   UINT32, 1),
    ("AllBranchMispredictRetired",  UINT32, 1),
    ("Reserved",                    UINT32, 25)
  ]

class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FixedFunctionPerformanceCounters",        UINT32, 5),
    ("FixedFunctionPerformanceCounterWidth",    UINT32, 8),
    ("Reserved1",                               UINT32, 2),
    ("AnyThreadDeprecation",                    UINT32, 1),
    ("Reserved2",                               UINT32, 16)
  ]

class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_EXTENDED_TOPOLOGY  = 0x0B

class CPUID_EXTENDED_TOPOLOGY_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ApicIdShift", UINT32, 5),
    ("Reserved",    UINT32, 27)
  ]

class CPUID_EXTENDED_TOPOLOGY_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_TOPOLOGY_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_EXTENDED_TOPOLOGY_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LogicalProcessors",   UINT32, 16),
    ("Reserved",            UINT32, 16)
  ]

class CPUID_EXTENDED_TOPOLOGY_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_TOPOLOGY_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_EXTENDED_TOPOLOGY_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LevelNumber", UINT32, 8),
    ("LevelType",   UINT32, 8),
    ("Reserved",    UINT32, 16)
  ]

class CPUID_EXTENDED_TOPOLOGY_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_TOPOLOGY_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_EXTENDED_TOPOLOGY_LEVEL_TYPE_INVALID  = 0x00
CPUID_EXTENDED_TOPOLOGY_LEVEL_TYPE_SMT      = 0x01
CPUID_EXTENDED_TOPOLOGY_LEVEL_TYPE_CORE     = 0x02

CPUID_EXTENDED_STATE  = 0x0D

CPUID_EXTENDED_STATE_MAIN_LEAF  = 0x00

class CPUID_EXTENDED_STATE_MAIN_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("x87",         UINT32, 1),
    ("SSE",         UINT32, 1),
    ("AVX",         UINT32, 1),
    ("MPX",         UINT32, 2),
    ("AVX_512",     UINT32, 3),
    ("IA32_XSS",    UINT32, 1),
    ("PKRU",        UINT32, 1),
    ("Reserved1",   UINT32, 3),
    ("IA32_XSS_2",  UINT32, 1),
    ("Reserved2",   UINT32, 18)
  ]

class CPUID_EXTENDED_STATE_MAIN_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_STATE_MAIN_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_EXTENDED_STATE_SUB_LEAF  = 0x01

class CPUID_EXTENDED_STATE_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("XSAVEOPT",    UINT32, 1),
    ("XSAVEC",      UINT32, 1),
    ("XGETBV",      UINT32, 1),
    ("XSAVES",      UINT32, 1),
    ("Reserved",    UINT32, 28)
  ]

class CPUID_EXTENDED_STATE_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_STATE_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_EXTENDED_STATE_SUB_LEAF_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("XCR0",        UINT32, 1),
    ("PT",          UINT32, 1),
    ("XCR0_1",      UINT32, 1),
    ("Reserved1",   UINT32, 3),
    ("HWPState",    UINT32, 1),
    ("Reserved8",   UINT32, 18)
  ]

class CPUID_EXTENDED_STATE_SUB_LEAF_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_STATE_SUB_LEAF_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_EXTENDED_STATE_SIZE_OFFSET  = 0x02

class CPUID_EXTENDED_STATE_SIZE_OFFSET_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("XSS",         UINT32, 1),
    ("Compacted",   UINT32, 1),
    ("Reserved",    UINT32, 30)
  ]

class CPUID_EXTENDED_STATE_SIZE_OFFSET_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_STATE_SIZE_OFFSET_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_RDT_MONITORING                      = 0x0F

CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF = 0x00

class CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",       UINT32, 1),
    ("L3CacheRDT_M",    UINT32, 1),
    ("Reserved2",       UINT32, 30)
  ]

class CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF  = 0x01

class CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("L3CacheOccupancyMonitoring",      UINT32, 1),
    ("L3CacheTotalBandwidthMonitoring", UINT32, 1),
    ("L3CacheLocalBandwidthMonitoring", UINT32, 1),
    ("Reserved",                        UINT32, 29)
  ]

class CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_RDT_ALLOCATION  = 0x10

CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF  = 0x00

class CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",           UINT32, 1),
    ("L3CacheAllocation",   UINT32, 1),
    ("L2CacheAllocation",   UINT32, 1),
    ("MemoryBandwidth",     UINT32, 1),
    ("Reserved3",           UINT32, 28)
  ]

class CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF_EBX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF  = 0x01

class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CapacityLength",  UINT32, 5),
    ("Reserved",        UINT32, 27)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved3",               UINT32, 2),
    ("CodeDataPrioritization",  UINT32, 1),
    ("Reserved2",               UINT32, 29)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_ECX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighestCosNumber",    UINT32, 16),
    ("Reserved",            UINT32, 16)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF  = 0x02

class CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CapacityLength",  UINT32, 5),
    ("Reserved",        UINT32, 27)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighestCosNumber",    UINT32, 16),
    ("Reserved",            UINT32, 16)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF  = 0x03

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MaximumMBAThrottling",    UINT32, 12),
    ("Reserved",                UINT32, 20)
  ]

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 2),
    ("Liner",       UINT32, 1),
    ("Reserved2",   UINT32, 29)
  ]

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_ECX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighestCosNumber",    UINT32, 16),
    ("Reserved",            UINT32, 16)
  ]

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_SGX                         = 0x12

CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF = 0x00

class CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SGX1",        UINT32, 1),
    ("SGX2",        UINT32, 1),
    ("Reserved1",   UINT32, 3),
    ("ENCLV",       UINT32, 1),
    ("ENCLS",       UINT32, 1),
    ("Reserved2",   UINT32, 25)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MaxEnclaveSize_Not64",    UINT32, 8),
    ("MaxEnclaveSize_64",       UINT32, 8),
    ("Reserved",                UINT32, 16)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_SGX_CAPABILITIES_1_SUB_LEAF         = 0x01

CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF = 0x02

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SubLeafType",             UINT32, 4),
    ("Reserved",                UINT32, 8),
    ("LowAddressOfEpcSection",  UINT32, 20)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighAddressOfEpcSection", UINT32, 20),
    ("Reserved",                UINT32, 12)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EpcSection",          UINT32, 4),
    ("Reserved",            UINT32, 8),
    ("LowSizeOfEpcSection", UINT32, 20)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_ECX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighSizeOfEpcSection",    UINT32, 20),
    ("Reserved",                UINT32, 12)
  ]

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF  = 0x00

class CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Cr3Filter",              UINT32, 1),
    ("ConfigurablePsb",        UINT32, 1),
    ("IpTraceStopFiltering",   UINT32, 1),
    ("Mtc",                    UINT32, 1),
    ("PTWrite",                UINT32, 1),
    ("PowerEventTrace",        UINT32, 1),
    ("Reserved",               UINT32, 26)
  ]

class CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("RTIT",                    UINT32, 1),
    ("ToPA",                    UINT32, 1),
    ("SingleRangeOutput",       UINT32, 1),
    ("TraceTransportSubsystem", UINT32, 1),
    ("Reserved",                UINT32, 27),
    ("LIP",                     UINT32, 1)
  ]

class CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF  = 0x01

class CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ConfigurableAddressRanges",   UINT32, 3),
    ("Reserved",                    UINT32, 13),
    ("MtcPeriodEncodings",          UINT32, 16)
  ]

class CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CycleThresholdEncodings", UINT32, 16),
    ("PsbFrequencyEncodings",   UINT32, 16)
  ]

class CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EBX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_TIME_STAMP_COUNTER    = 0x15

CPUID_PROCESSOR_FREQUENCY   = 0x16

class CPUID_PROCESSOR_FREQUENCY_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ProcessorBaseFrequency",  UINT32, 16),
    ("Reserved",                UINT32, 16)
  ]

class CPUID_PROCESSOR_FREQUENCY_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_PROCESSOR_FREQUENCY_EAX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_PROCESSOR_FREQUENCY_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MaximumFrequency",    UINT32, 16),
    ("Reserved",            UINT32, 16)
  ]

class CPUID_PROCESSOR_FREQUENCY_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_PROCESSOR_FREQUENCY_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_PROCESSOR_FREQUENCY_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("BusFrequency",    UINT32, 16),
    ("Reserved",        UINT32, 16)
  ]

class CPUID_PROCESSOR_FREQUENCY_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_PROCESSOR_FREQUENCY_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_SOC_VENDOR            = 0x17

CPUID_SOC_VENDOR_MAIN_LEAF  = 0x00

class CPUID_SOC_VENDOR_MAIN_LEAF_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SocVendorId",     UINT32, 16),
    ("IsVendorScheme",  UINT32, 1),
    ("Reserved",        UINT32, 15)
  ]

class CPUID_SOC_VENDOR_MAIN_LEAF_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_SOC_VENDOR_MAIN_LEAF_EBX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_SOC_VENDOR_BRAND_STRING1  = 0x01

class CPUID_SOC_VENDOR_BRAND_STRING_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("BrandString", CHAR8 * 4),
    ("Uint32",      UINT32)
  ]

CPUID_SOC_VENDOR_BRAND_STRING2  = 0x02

CPUID_SOC_VENDOR_BRAND_STRING3  = 0x03

CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS              = 0x18

CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_MAIN_LEAF    = 0x00

class CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Page4K",          UINT32, 1),
    ("Page2M",          UINT32, 1),
    ("Page4M",          UINT32, 1),
    ("Page1G",          UINT32, 1),
    ("Reserved1",       UINT32, 4),
    ("Partitioning",    UINT32, 3),
    ("Reserved2",       UINT32, 5),
    ("Way",             UINT32, 16)
  ]

class CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EBX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TranslationCacheType",    UINT32, 5),
    ("TranslationCacheLevel",   UINT32, 3),
    ("FullyAssociative",        UINT32, 1),
    ("Reserved1",               UINT32, 5),
    ("MaximumNum",              UINT32, 12),
    ("Reserved2",               UINT32, 6)
  ]

class CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_TRANSLATION_CACHE_TYPE_INVALID          = 0x00
CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_TRANSLATION_CACHE_TYPE_DATA_TLB         = 0x01
CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_TRANSLATION_CACHE_TYPE_INSTRUCTION_TLB  = 0x02
CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_TRANSLATION_CACHE_TYPE_UNIFIED_TLB      = 0x03

CPUID_HYBRID_INFORMATION  = 0x1A

CPUID_HYBRID_INFORMATION_MAIN_LEAF  = 0x00

class CPUID_NATIVE_MODEL_ID_AND_CORE_TYPE_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("NativeModelId",   UINT32, 24),
    ("CoreType",        UINT32, 8)
  ]

class CPUID_NATIVE_MODEL_ID_AND_CORE_TYPE_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_NATIVE_MODEL_ID_AND_CORE_TYPE_EAX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_CORE_TYPE_INTEL_ATOM  = 0x20
CPUID_CORE_TYPE_INTEL_CORE  = 0x40

CPUID_V2_EXTENDED_TOPOLOGY  = 0x1F

CPUID_V2_EXTENDED_TOPOLOGY_LEVEL_TYPE_MODULE  = 0x03
CPUID_V2_EXTENDED_TOPOLOGY_LEVEL_TYPE_TILE    = 0x04
CPUID_V2_EXTENDED_TOPOLOGY_LEVEL_TYPE_DIE     = 0x05

CPUID_GUESTTD_RUNTIME_ENVIRONMENT  = 0x21

CPUID_GUESTTD_SIGNATURE_GENUINE_INTEL_EBX  = SIGNATURE_32 ('I', 'n', 't', 'e')
CPUID_GUESTTD_SIGNATURE_GENUINE_INTEL_ECX  = SIGNATURE_32 (' ', ' ', ' ', ' ')
CPUID_GUESTTD_SIGNATURE_GENUINE_INTEL_EDX  = SIGNATURE_32 ('l', 'T', 'D', 'X')

CPUID_EXTENDED_FUNCTION     = 0x80000000

CPUID_EXTENDED_CPU_SIG      = 0x80000001

class CPUID_EXTENDED_CPU_SIG_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LAHF_SAHF",   UINT32, 1),
    ("Reserved1",   UINT32, 4),
    ("LZCNT",       UINT32, 1),
    ("Reserved2",   UINT32, 2),
    ("PREFETCHW",   UINT32, 1),
    ("Reserved3",   UINT32, 23)
  ]

class CPUID_EXTENDED_CPU_SIG_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_CPU_SIG_ECX_Bits),
    ("Uint32",          UINT32)
  ]

class CPUID_EXTENDED_CPU_SIG_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",       UINT32, 11),
    ("SYSCALL_SYSRET",  UINT32, 1),
    ("Reserved2",       UINT32, 8),
    ("NX",              UINT32, 1),
    ("Reserved3",       UINT32, 5),
    ("Page1GB",         UINT32, 1),
    ("RDTSCP",          UINT32, 1),
    ("Reserved4",       UINT32, 1),
    ("LM",              UINT32, 1),
    ("Reserved5",       UINT32, 2)
  ]

class CPUID_EXTENDED_CPU_SIG_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_CPU_SIG_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_BRAND_STRING1  = 0x80000002

class CPUID_BRAND_STRING_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("BrandString",     CHAR8 * 4),
    ("Uint32",          UINT32)
  ]

CPUID_BRAND_STRING2  = 0x80000003

CPUID_EXTENDED_CACHE_INFO  = 0x80000006

class CPUID_EXTENDED_CACHE_INFO_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CacheLineSize",       UINT32, 8),
    ("Reserved",            UINT32, 4),
    ("L2Associativity",     UINT32, 4),
    ("CacheSize",           UINT32, 16)
  ]

class CPUID_EXTENDED_CACHE_INFO_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_CACHE_INFO_ECX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_DISABLED       = 0x00
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_DIRECT_MAPPED  = 0x01
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_2_WAY          = 0x02
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_4_WAY          = 0x04
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_8_WAY          = 0x06
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_16_WAY         = 0x08
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_32_WAY         = 0x0A
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_48_WAY         = 0x0B
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_64_WAY         = 0x0C
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_96_WAY         = 0x0D
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_128_WAY        = 0x0E
CPUID_EXTENDED_CACHE_INFO_ECX_L2_ASSOCIATIVITY_FULL           = 0x0F

CPUID_EXTENDED_TIME_STAMP_COUNTER  = 0x80000007

class CPUID_EXTENDED_TIME_STAMP_COUNTER_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",       UINT32, 8),
    ("InvariantTsc",    UINT32, 1),
    ("Reserved2",       UINT32, 23)
  ]

class CPUID_EXTENDED_TIME_STAMP_COUNTER_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_EXTENDED_TIME_STAMP_COUNTER_EDX_Bits),
    ("Uint32",          UINT32)
  ]

CPUID_VIR_PHY_ADDRESS_SIZE  = 0x80000008

class CPUID_VIR_PHY_ADDRESS_SIZE_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PhysicalAddressBits", UINT32, 8),
    ("LinearAddressBits",   UINT32, 8),
    ("Reserved",            UINT32, 16)
  ]

class CPUID_VIR_PHY_ADDRESS_SIZE_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_VIR_PHY_ADDRESS_SIZE_EAX_Bits),
    ("Uint32",          UINT32)
  ]

