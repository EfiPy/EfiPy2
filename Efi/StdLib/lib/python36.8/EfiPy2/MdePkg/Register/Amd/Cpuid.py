# Cpuid.py
#
# EfiPy2.MdePkg.Register.Amd.Cpuid
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

CPUID_SIGNATURE_AUTHENTIC_AMD_EBX  = SIGNATURE_32 ('A', 'u', 't', 'h')
CPUID_SIGNATURE_AUTHENTIC_AMD_EDX  = SIGNATURE_32 ('e', 'n', 't', 'i')
CPUID_SIGNATURE_AUTHENTIC_AMD_ECX  = SIGNATURE_32 ('c', 'A', 'M', 'D')

AMD_CPUID_EXTENDED_TOPOLOGY  = 0x80000026

class CPUID_AMD_EXTENDED_CPU_SIG_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Stepping",    UINT32, 4),
    ("BaseModel",   UINT32, 4),
    ("BaseFamily",  UINT32, 4),
    ("Reserved1",   UINT32, 4),
    ("ExtModel",    UINT32, 4),
    ("ExtFamily",   UINT32, 8),
    ("Reserved2",   UINT32, 4)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_EXTENDED_CPU_SIG_EAX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32, 28),
    ("PkgType",     UINT32, 4)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_EXTENDED_CPU_SIG_EBX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LAHF_SAHF",               UINT32, 1),
    ("CmpLegacy",               UINT32, 1),
    ("SVM",                     UINT32, 1),
    ("ExtApicSpace",            UINT32, 1),
    ("AltMovCr8",               UINT32, 1),
    ("LZCNT",                   UINT32, 1),
    ("SSE4A",                   UINT32, 1),
    ("MisAlignSse",             UINT32, 1),
    ("PREFETCHW",               UINT32, 1),
    ("OSVW",                    UINT32, 1),
    ("IBS",                     UINT32, 1),
    ("XOP",                     UINT32, 1),
    ("SKINIT",                  UINT32, 1),
    ("WDT",                     UINT32, 1),
    ("Reserved1",               UINT32, 1),
    ("LWP",                     UINT32, 1),
    ("FMA4",                    UINT32, 1),
    ("TCE",                     UINT32, 1),
    ("Reserved2",               UINT32, 4),
    ("TopologyExtensions",      UINT32, 1),
    ("PerfCtrExtCore",          UINT32, 1),
    ("Reserved3",               UINT32, 2),
    ("DataBreakpointExtension", UINT32, 1),
    ("PerfTsc",                 UINT32, 1),
    ("PerfCtrExtL3",            UINT32, 1),
    ("MwaitExtended",           UINT32, 1),
    ("Reserved4",               UINT32, 2)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_EXTENDED_CPU_SIG_ECX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FPU",             UINT32, 1),
    ("VME",             UINT32, 1),
    ("DE",              UINT32, 1),
    ("PSE",             UINT32, 1),
    ("TSC",             UINT32, 1),
    ("MSR",             UINT32, 1),
    ("PAE",             UINT32, 1),
    ("MCE",             UINT32, 1),
    ("CMPXCHG8B",       UINT32, 1),
    ("APIC",            UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("SYSCALL_SYSRET",  UINT32, 1),
    ("MTRR",            UINT32, 1),
    ("PGE",             UINT32, 1),
    ("MCA",             UINT32, 1),
    ("CMOV",            UINT32, 1),
    ("PAT",             UINT32, 1),
    ("PSE36",           UINT32, 1),
    ("Reserved2",       UINT32, 2),
    ("NX",              UINT32, 1),
    ("Reserved3",       UINT32, 1),
    ("MmxExt",          UINT32, 1),
    ("MMX",             UINT32, 1),
    ("FFSR",            UINT32, 1),
    ("FFXSR",           UINT32, 1),
    ("Page1GB",         UINT32, 1),
    ("RDTSCP",          UINT32, 1),
    ("Reserved4",       UINT32, 1),
    ("LM",              UINT32, 1),
    ("ThreeDNow",       UINT32, 1),
    ("ThreeDNowExt",    UINT32, 1)
  ]

class CPUID_AMD_EXTENDED_CPU_SIG_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_EXTENDED_CPU_SIG_EDX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_VIR_PHY_ADDRESS_SIZE_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PhysicalAddressBits", UINT32, 8),
    ("LinearAddressBits",   UINT32, 8),
    ("GuestPhysAddrSize",   UINT32, 8),
    ("Reserved",            UINT32, 8)
  ]

class CPUID_AMD_VIR_PHY_ADDRESS_SIZE_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_VIR_PHY_ADDRESS_SIZE_EAX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_VIR_PHY_ADDRESS_SIZE_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CLZERO",      UINT32, 1),
    ("IRPerf",      UINT32, 1),
    ("XSaveErPtr",  UINT32, 1),
    ("Reserved",    UINT32, 29)
  ]

class CPUID_AMD_VIR_PHY_ADDRESS_SIZE_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_VIR_PHY_ADDRESS_SIZE_EBX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_VIR_PHY_ADDRESS_SIZE_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("NC",                  UINT32, 8),
    ("Reserved1",           UINT32, 4),
    ("ApicIdCoreIdSize",    UINT32, 4),
    ("PerfTscSize",         UINT32, 2),
    ("Reserved2",           UINT32, 14)
  ]

class CPUID_AMD_VIR_PHY_ADDRESS_SIZE_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_VIR_PHY_ADDRESS_SIZE_ECX_Bits),
    ("Uint32",  UINT32)
  ]

CPUID_AMD_PROCESSOR_TOPOLOGY  = 0x8000001E

class CPUID_AMD_PROCESSOR_TOPOLOGY_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExtendedApicId",      UINT32, 32)
  ]

class CPUID_AMD_PROCESSOR_TOPOLOGY_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_PROCESSOR_TOPOLOGY_EAX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_PROCESSOR_TOPOLOGY_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CoreId",          UINT32, 8),
    ("ThreadsPerCore",  UINT32, 8),
    ("Reserved",        UINT32, 16)
  ]

class CPUID_AMD_PROCESSOR_TOPOLOGY_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_PROCESSOR_TOPOLOGY_EBX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_AMD_PROCESSOR_TOPOLOGY_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("NodeId",              UINT32, 8),
    ("NodesPerProcessor",   UINT32, 3),
    ("Reserved",            UINT32, 21)
  ]

class CPUID_AMD_PROCESSOR_TOPOLOGY_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_AMD_PROCESSOR_TOPOLOGY_ECX_Bits),
    ("Uint32",  UINT32)
  ]

CPUID_MEMORY_ENCRYPTION_INFO  = 0x8000001F

class CPUID_MEMORY_ENCRYPTION_INFO_EAX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SmeBit",          UINT32, 1),
    ("SevBit",          UINT32, 1),
    ("PageFlushMsrBit", UINT32, 1),
    ("SevEsBit",        UINT32, 1),
    ("ReservedBits",    UINT32, 28)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_EAX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_MEMORY_ENCRYPTION_INFO_EAX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_EBX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PtePosBits",      UINT32, 6),
    ("ReducedPhysBits", UINT32, 5),
    ("ReservedBits",    UINT32, 21)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_EBX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_MEMORY_ENCRYPTION_INFO_EBX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_ECX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("NumGuests",       UINT32, 32)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_ECX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_MEMORY_ENCRYPTION_INFO_ECX_Bits),
    ("Uint32",  UINT32)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_EDX_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinAsid",         UINT32, 32)
  ]

class CPUID_MEMORY_ENCRYPTION_INFO_EDX (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPUID_MEMORY_ENCRYPTION_INFO_EDX_Bits),
    ("Uint32",  UINT32)
  ]

