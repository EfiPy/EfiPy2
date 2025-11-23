# CpuIdIntel.py
#
# EfiPy2.Lib.CpuIdIntel
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.Register.Intel.Cpuid as CpuidRegs

class CPUID_GENERIC_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x00000000, Vendor-ID and Largest Standard Function
CPUID_SIGNATURE = CpuidRegs.CPUID_SIGNATURE
class CPUID_SIGNATURE_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT8 * 4),
    ('ECX',  EfiPy.UINT8 * 4),
    ('EDX',  EfiPy.UINT8 * 4)
  ]


# 0x00000001, 
CPUID_VERSION_INFO  = CpuidRegs.CPUID_VERSION_INFO
class CPUID_VERSION_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_VERSION_INFO_EAX),
    ('EBX',  CpuidRegs.CPUID_VERSION_INFO_EBX),
    ('ECX',  CpuidRegs.CPUID_VERSION_INFO_ECX),
    ('EDX',  CpuidRegs.CPUID_VERSION_INFO_EDX)
  ]

# 0x00000002, Cache Info
CPUID_CACHE_INFO            = CpuidRegs.CPUID_CACHE_INFO

class CPUID_CACHE_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_CACHE_INFO_CACHE_TLB),
    ('EBX',  CpuidRegs.CPUID_CACHE_INFO_CACHE_TLB),
    ('ECX',  CpuidRegs.CPUID_CACHE_INFO_CACHE_TLB),
    ('EDX',  CpuidRegs.CPUID_CACHE_INFO_CACHE_TLB)
  ]


# 0x00000003, Processor Serial Number

# 0x00000004, Deterministic Cache Parameter
CPUID_CACHE_PARAMS          = CpuidRegs.CPUID_CACHE_PARAMS

class CPUID_CACHE_PARAMS_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_CACHE_PARAMS_EAX),
    ('EBX',  CpuidRegs.CPUID_CACHE_PARAMS_EBX),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_CACHE_PARAMS_EDX)
  ]

# 0x0000005, MONITOR/MWAIT Parameters
CPUID_MONITOR_MWAIT  = CpuidRegs.CPUID_MONITOR_MWAIT
class CPUID_MONITOR_MWAIT_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_MONITOR_MWAIT_EAX),
    ('EBX',  CpuidRegs.CPUID_MONITOR_MWAIT_EBX),
    ('ECX',  CpuidRegs.CPUID_MONITOR_MWAIT_ECX),
    ('EDX',  CpuidRegs.CPUID_MONITOR_MWAIT_EDX)
  ]

# 0x00000006, Digital Thermal Sensor and Power Management Parameters
CPUID_THERMAL_POWER_MANAGEMENT  = CpuidRegs.CPUID_THERMAL_POWER_MANAGEMENT
class CPUID_THERMAL_POWER_MANAGEMENT_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_THERMAL_POWER_MANAGEMENT_EAX),
    ('EBX',  CpuidRegs.CPUID_THERMAL_POWER_MANAGEMENT_EBX),
    ('ECX',  CpuidRegs.CPUID_THERMAL_POWER_MANAGEMENT_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x00000007, Structured Extended Feature Flags Enumeraiton
CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS                 = CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS
CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_INFO   = CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_INFO
CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_1_INFO = CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_1_INFO
CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_2_INFO = CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_2_INFO

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EBX),
    ('ECX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_ECX),
    ('EDX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_EDX)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_1_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_1_INFO_EAX),
    ('EBX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_1_INFO_EBX),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_1_INFO_EDX)
  ]

class CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_2_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS_SUB_LEAF_2_INFO_EDX)
  ]

# 0x00000008, Reserved

# 0x00000009, Direct Cache Access (DCA) Parameters
CPUID_DIRECT_CACHE_ACCESS_INFO                  = CpuidRegs.CPUID_DIRECT_CACHE_ACCESS_INFO
class CPUID_DIRECT_CACHE_ACCESS_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x0000000A, Architecture Performance Monitor Features
CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING      = CpuidRegs.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING
class CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EAX),
    ('EBX',  CpuidRegs.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EBX),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING_EDX)
  ]

# 0x0000000B, x2APIC Features / PRocessor Topology
CPUID_EXTENDED_TOPOLOGY  = CpuidRegs.CPUID_EXTENDED_TOPOLOGY
class CPUID_EXTENDED_TOPOLOGY_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_EXTENDED_TOPOLOGY_EAX),
    ('EBX',  CpuidRegs.CPUID_EXTENDED_TOPOLOGY_EBX),
    ('ECX',  CpuidRegs.CPUID_EXTENDED_TOPOLOGY_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x0000000D, Processor Extended State Enumeration
CPUID_EXTENDED_STATE                = CpuidRegs.CPUID_EXTENDED_STATE
CPUID_EXTENDED_STATE_MAIN_LEAF      = CpuidRegs.CPUID_EXTENDED_STATE_MAIN_LEAF
CPUID_EXTENDED_STATE_SUB_LEAF       = CpuidRegs.CPUID_EXTENDED_STATE_SUB_LEAF
CPUID_EXTENDED_STATE_SIZE_OFFSET    = CpuidRegs.CPUID_EXTENDED_STATE_SIZE_OFFSET

class CPUID_EXTENDED_STATE_MAIN_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_EXTENDED_STATE_MAIN_LEAF_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

class CPUID_EXTENDED_STATE_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_EXTENDED_STATE_SUB_LEAF_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_EXTENDED_STATE_SUB_LEAF_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

class CPUID_EXTENDED_STATE_SIZE_OFFSET_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_EXTENDED_STATE_SIZE_OFFSET_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x0000000F, Intel Resource Director Technology (Intel RDT)
CPUID_INTEL_RDT_MONITORING                          = CpuidRegs.CPUID_INTEL_RDT_MONITORING
CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF     = CpuidRegs.CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF
CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF        = CpuidRegs.CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF

class CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_INTEL_RDT_MONITORING_ENUMERATION_SUB_LEAF_EDX)
  ]

class CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_INTEL_RDT_MONITORING_L3_CACHE_SUB_LEAF_EDX)
  ]

# 0x00000010

CPUID_INTEL_RDT_ALLOCATION                              = CpuidRegs.CPUID_INTEL_RDT_ALLOCATION
CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF         = CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF
CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF            = CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF
CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF            = CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF
CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF    = CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF

class CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_ENUMERATION_SUB_LEAF_EBX),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]


class CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_ECX),
    ('EDX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L3_CACHE_SUB_LEAF_EDX)
  ]

class CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_L2_CACHE_SUB_LEAF_EDX)
  ]

class CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_ECX),
    ('EDX',  CpuidRegs.CPUID_INTEL_RDT_ALLOCATION_MEMORY_BANDWIDTH_SUB_LEAF_EDX)
  ]

# 0x00000012
CPUID_INTEL_SGX                                 = CpuidRegs.CPUID_INTEL_SGX
CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF         = CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF
CPUID_INTEL_SGX_CAPABILITIES_1_SUB_LEAF         = CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_1_SUB_LEAF
CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF = CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF

class CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_0_SUB_LEAF_EDX)
  ]

CPUID_INTEL_SGX_CAPABILITIES_1_SUB_LEAF_REGISTERs = CPUID_GENERIC_REGISTERs

class CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EAX),
    ('EBX',  CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EBX),
    ('ECX',  CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_ECX),
    ('EDX',  CpuidRegs.CPUID_INTEL_SGX_CAPABILITIES_RESOURCES_SUB_LEAF_EDX)
  ]

CPUID_INTEL_PROCESSOR_TRACE                         = CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE
CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF               = CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF
CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF                = CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF

class CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_EBX),
    ('ECX',  CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_ECX),
    ('EDX',  EfiPy.UINT32)
  ]


class CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE_SUB_LEAF_EBX),
    ('ECX',  CpuidRegs.CPUID_INTEL_PROCESSOR_TRACE_MAIN_LEAF_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x00000015, Time Stamp Counter and Nominal Core Crystal Clock Information Leaf
CPUID_TIME_STAMP_COUNTER                            = CpuidRegs.CPUID_TIME_STAMP_COUNTER

CPUID_TIME_STAMP_COUNTER_REGISTERs = CPUID_GENERIC_REGISTERs

# 0x00000016, Processor Frequency Information Leaf
CPUID_PROCESSOR_FREQUENCY                           = CpuidRegs.CPUID_PROCESSOR_FREQUENCY

class CPUID_PROCESSOR_FREQUENCY_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_PROCESSOR_FREQUENCY_EAX),
    ('EBX',  CpuidRegs.CPUID_PROCESSOR_FREQUENCY_EBX),
    ('ECX',  CpuidRegs.CPUID_PROCESSOR_FREQUENCY_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x00000017, SOC Vendor
CPUID_SOC_VENDOR                        = CpuidRegs.CPUID_SOC_VENDOR
CPUID_SOC_VENDOR_MAIN_LEAF              = CpuidRegs.CPUID_SOC_VENDOR_MAIN_LEAF
CPUID_SOC_VENDOR_BRAND_STRING1          = CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING1
CPUID_SOC_VENDOR_BRAND_STRING2          = CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING2
CPUID_SOC_VENDOR_BRAND_STRING3          = CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING3

class CPUID_SOC_VENDOR_MAIN_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  CpuidRegs.CPUID_SOC_VENDOR_MAIN_LEAF_EBX),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

class CPUID_SOC_VENDOR_BRAND_STRING_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING_DATA),
    ('EBX',  CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING_DATA),
    ('ECX',  CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING_DATA),
    ('EDX',  CpuidRegs.CPUID_SOC_VENDOR_BRAND_STRING_DATA)
  ]

# 0x00000018, Deterministic Address Translation Parameters
CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS              = CpuidRegs.CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS
CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_MAIN_LEAF    = CpuidRegs.CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_MAIN_LEAF

class CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  CpuidRegs.CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EBX),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  CpuidRegs.CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS_EDX)
  ]

# 0x00000019, Key Lock Leaf
CPUID_KEY_LOCK                                                  = 0x19

class CPUID_KEY_LOCK_EAX_Bits (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ("CPL0_only_supported",     EfiPy.UINT32, 1),
    ("no_encrypt_supported_1",  EfiPy.UINT32, 1),
    ("no_encrypt_supported_2",  EfiPy.UINT32, 1),
    ("Reserved",                EfiPy.UINT32, 29)
  ]

class CPUID_KEY_LOCK_EAX (EfiPy.Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_KEY_LOCK_EAX_Bits),
    ("Uint32",          EfiPy.UINT32)
  ]

class CPUID_KEY_LOCK_EBX_Bits (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ("AESKLE",                              EfiPy.UINT32, 1),
    ("Reserved",                            EfiPy.UINT32, 1),
    ("AES_wide_Key_Locker_instructions",    EfiPy.UINT32, 1),
    ("Reserved_2",                          EfiPy.UINT32, 1),
    ("Key_Locker_MSRs",                     EfiPy.UINT32, 1),
    ("Reserved_3",                          EfiPy.UINT32, 27),
  ]

class CPUID_KEY_LOCK_EBX (EfiPy.Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_KEY_LOCK_EBX_Bits),
    ("Uint32",          EfiPy.UINT32)
  ]

class CPUID_KEY_LOCK_ECX_Bits (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ("LOADIWKEY",           EfiPy.UINT32, 1),
    ("KeySource_encoding",  EfiPy.UINT32, 1),
    ("Reserved",            EfiPy.UINT32, 30)
  ]

class CPUID_KEY_LOCK_ECX (EfiPy.Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",            CPUID_KEY_LOCK_ECX_Bits),
    ("Uint32",          EfiPy.UINT32)
  ]

class CPUID_KEY_LOCK_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CPUID_KEY_LOCK_EAX),
    ('EBX',  CPUID_KEY_LOCK_EBX),
    ('ECX',  CPUID_KEY_LOCK_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x0000001A
CPUID_HYBRID_INFORMATION                = CpuidRegs.CPUID_HYBRID_INFORMATION
CPUID_HYBRID_INFORMATION_MAIN_LEAF      = CpuidRegs.CPUID_HYBRID_INFORMATION_MAIN_LEAF

class CPUID_HYBRID_INFORMATION_MAIN_LEAF_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_NATIVE_MODEL_ID_AND_CORE_TYPE_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x0000001B (TBC)
# 0x0000001C (TBC)
# 0x0000001D (TBC)
# 0x0000001E (TBC)
# 0x0000001F (TBC)
# 0x00000020 (TBC)
# 0x00000021 (TBC)

# 0x80000000
CPUID_EXTENDED_FUNCTION             = CpuidRegs.CPUID_EXTENDED_FUNCTION
CPUID_EXTENDED_FUNCTION_REGISTERs   = CPUID_GENERIC_REGISTERs

# 0x80000001
CPUID_EXTENDED_CPU_SIG              = CpuidRegs.CPUID_EXTENDED_CPU_SIG

class CPUID_EXTENDED_CPU_SIG_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_EXTENDED_CPU_SIG_ECX),
    ('EDX',  CpuidRegs.CPUID_EXTENDED_CPU_SIG_EDX)
  ]

# 0x80000002, Processor Brand String
# 0x80000003, Processor Brand String
# 0x80000004, Processor Brand String
# 0x80000005, NULL
CPUID_BRAND_STRING1                 = CpuidRegs.CPUID_BRAND_STRING1
CPUID_BRAND_STRING2                 = CpuidRegs.CPUID_BRAND_STRING2
CPUID_BRAND_STRING3                 = CpuidRegs.CPUID_BRAND_STRING3

class CPUID_BRAND_STRING_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_BRAND_STRING_DATA),
    ('EBX',  CpuidRegs.CPUID_BRAND_STRING_DATA),
    ('ECX',  CpuidRegs.CPUID_BRAND_STRING_DATA),
    ('EDX',  CpuidRegs.CPUID_BRAND_STRING_DATA)
  ]

# 0x80000006
CPUID_EXTENDED_CACHE_INFO           = CpuidRegs.CPUID_EXTENDED_CACHE_INFO

class CPUID_EXTENDED_CACHE_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_EXTENDED_CACHE_INFO_ECX),
    ('EDX',  EfiPy.UINT32)
  ]

# 0x80000007, 
CPUID_EXTENDED_TIME_STAMP_COUNTER   = CpuidRegs.CPUID_EXTENDED_TIME_STAMP_COUNTER

class CPUID_EXTENDED_TIME_STAMP_COUNTER_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  CpuidRegs.CPUID_EXTENDED_CACHE_INFO_ECX),
    ('EDX',  CpuidRegs.CPUID_EXTENDED_TIME_STAMP_COUNTER_EDX)
  ]

# 0x80000008
CPUID_VIR_PHY_ADDRESS_SIZE          = CpuidRegs.CPUID_VIR_PHY_ADDRESS_SIZE

class CPUID_VIR_PHY_ADDRESS_SIZE_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_VIR_PHY_ADDRESS_SIZE_EAX),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]
