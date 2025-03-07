# Tdx.py
#
# EfiPy2.MdePkg.IndustryStandard.Tdx
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

EXIT_REASON_EXTERNAL_INTERRUPT  = 1
EXIT_REASON_TRIPLE_FAULT        = 2

EXIT_REASON_PENDING_INTERRUPT    = 7
EXIT_REASON_NMI_WINDOW           = 8
EXIT_REASON_TASK_SWITCH          = 9
EXIT_REASON_CPUID                = 10
EXIT_REASON_HLT                  = 12
EXIT_REASON_INVD                 = 13
EXIT_REASON_INVLPG               = 14
EXIT_REASON_RDPMC                = 15
EXIT_REASON_RDTSC                = 16
EXIT_REASON_VMCALL               = 18
EXIT_REASON_VMCLEAR              = 19
EXIT_REASON_VMLAUNCH             = 20
EXIT_REASON_VMPTRLD              = 21
EXIT_REASON_VMPTRST              = 22
EXIT_REASON_VMREAD               = 23
EXIT_REASON_VMRESUME             = 24
EXIT_REASON_VMWRITE              = 25
EXIT_REASON_VMOFF                = 26
EXIT_REASON_VMON                 = 27
EXIT_REASON_CR_ACCESS            = 28
EXIT_REASON_DR_ACCESS            = 29
EXIT_REASON_IO_INSTRUCTION       = 30
EXIT_REASON_MSR_READ             = 31
EXIT_REASON_MSR_WRITE            = 32
EXIT_REASON_INVALID_STATE        = 33
EXIT_REASON_MSR_LOAD_FAIL        = 34
EXIT_REASON_MWAIT_INSTRUCTION    = 36
EXIT_REASON_MONITOR_TRAP_FLAG    = 37
EXIT_REASON_MONITOR_INSTRUCTION  = 39
EXIT_REASON_PAUSE_INSTRUCTION    = 40
EXIT_REASON_MCE_DURING_VMENTRY   = 41
EXIT_REASON_TPR_BELOW_THRESHOLD  = 43
EXIT_REASON_APIC_ACCESS          = 44
EXIT_REASON_EOI_INDUCED          = 45
EXIT_REASON_GDTR_IDTR            = 46
EXIT_REASON_LDTR_TR              = 47
EXIT_REASON_EPT_VIOLATION        = 48
EXIT_REASON_EPT_MISCONFIG        = 49
EXIT_REASON_INVEPT               = 50
EXIT_REASON_RDTSCP               = 51
EXIT_REASON_PREEMPTION_TIMER     = 52
EXIT_REASON_INVVPID              = 53
EXIT_REASON_WBINVD               = 54
EXIT_REASON_XSETBV               = 55
EXIT_REASON_APIC_WRITE           = 56
EXIT_REASON_RDRAND               = 57
EXIT_REASON_INVPCID              = 58
EXIT_REASON_VMFUNC               = 59
EXIT_REASON_ENCLS                = 60
EXIT_REASON_RDSEED               = 61
EXIT_REASON_PML_FULL             = 62
EXIT_REASON_XSAVES               = 63
EXIT_REASON_XRSTORS              = 64
EXIT_REASON_PENDING_INTERRUPT    = 7
EXIT_REASON_NMI_WINDOW           = 8
EXIT_REASON_TASK_SWITCH          = 9
EXIT_REASON_CPUID                = 10
EXIT_REASON_HLT                  = 12
EXIT_REASON_INVD                 = 13
EXIT_REASON_INVLPG               = 14
EXIT_REASON_RDPMC                = 15
EXIT_REASON_RDTSC                = 16
EXIT_REASON_VMCALL               = 18
EXIT_REASON_VMCLEAR              = 19
EXIT_REASON_VMLAUNCH             = 20
EXIT_REASON_VMPTRLD              = 21
EXIT_REASON_VMPTRST              = 22
EXIT_REASON_VMREAD               = 23
EXIT_REASON_VMRESUME             = 24
EXIT_REASON_VMWRITE              = 25
EXIT_REASON_VMOFF                = 26
EXIT_REASON_VMON                 = 27
EXIT_REASON_CR_ACCESS            = 28
EXIT_REASON_DR_ACCESS            = 29
EXIT_REASON_IO_INSTRUCTION       = 30
EXIT_REASON_MSR_READ             = 31
EXIT_REASON_MSR_WRITE            = 32
EXIT_REASON_INVALID_STATE        = 33
EXIT_REASON_MSR_LOAD_FAIL        = 34
EXIT_REASON_MWAIT_INSTRUCTION    = 36
EXIT_REASON_MONITOR_TRAP_FLAG    = 37
EXIT_REASON_MONITOR_INSTRUCTION  = 39
EXIT_REASON_PAUSE_INSTRUCTION    = 40
EXIT_REASON_MCE_DURING_VMENTRY   = 41
EXIT_REASON_TPR_BELOW_THRESHOLD  = 43
EXIT_REASON_APIC_ACCESS          = 44
EXIT_REASON_EOI_INDUCED          = 45
EXIT_REASON_GDTR_IDTR            = 46
EXIT_REASON_LDTR_TR              = 47
EXIT_REASON_EPT_VIOLATION        = 48
EXIT_REASON_EPT_MISCONFIG        = 49
EXIT_REASON_INVEPT               = 50
EXIT_REASON_RDTSCP               = 51
EXIT_REASON_PREEMPTION_TIMER     = 52
EXIT_REASON_INVVPID              = 53
EXIT_REASON_WBINVD               = 54
EXIT_REASON_XSETBV               = 55
EXIT_REASON_APIC_WRITE           = 56
EXIT_REASON_RDRAND               = 57
EXIT_REASON_INVPCID              = 58
EXIT_REASON_VMFUNC               = 59
EXIT_REASON_ENCLS                = 60
EXIT_REASON_RDSEED               = 61
EXIT_REASON_PML_FULL             = 62
EXIT_REASON_XSAVES               = 63
EXIT_REASON_XRSTORS              = 64

TDX_EXIT_REASON_SUCCESS                = 0x0000000000000000
TDX_EXIT_REASON_PAGE_ALREADY_ACCEPTED  = 0x00000B0A00000000
TDX_EXIT_REASON_PAGE_SIZE_MISMATCH     = 0xC0000B0B00000000
TDX_EXIT_REASON_OPERAND_INVALID        = 0xC000010000000000
TDX_EXIT_REASON_OPERAND_BUSY           = 0x8000020000000000

TDCALL_ACCEPT_PAGE_SIZE_4K  = 0
TDCALL_ACCEPT_PAGE_SIZE_2M  = 1
TDCALL_ACCEPT_PAGE_SIZE_1G  = 2

TDCALL_TDVMCALL      = 0
TDCALL_TDINFO        = 1
TDCALL_TDEXTENDRTMR  = 2
TDCALL_TDGETVEINFO   = 3
TDCALL_TDREPORT      = 4
TDCALL_TDSETCPUIDVE  = 5
TDCALL_TDACCEPTPAGE  = 6

TDVMCALL_CPUID    = 0x0000a
TDVMCALL_HALT     = 0x0000c
TDVMCALL_IO       = 0x0001e
TDVMCALL_RDMSR    = 0x0001f
TDVMCALL_WRMSR    = 0x00020
TDVMCALL_MMIO     = 0x00030
TDVMCALL_PCONFIG  = 0x00041

TDVMCALL_GET_TDVMCALL_INFO   = 0x10000
TDVMCALL_MAPGPA              = 0x10001
TDVMCALL_GET_QUOTE           = 0x10002
TDVMCALL_REPORT_FATAL_ERR    = 0x10003
TDVMCALL_SETUP_EVENT_NOTIFY  = 0x10004

TDVMCALL_STATUS_RETRY  = 0x1

class TDCALL_GENERIC_RETURN_DATA (Structure):
  _fields_ = [
    ("Data",    UINT64 * 6)
    ]

class TDCALL_INFO_RETURN_DATA (Structure):
  _fields_ = [
    ("Gpaw",        UINT64),
    ("Attributes",  UINT64),
    ("NumVcpus",    UINT32),
    ("MaxVcpus",    UINT32),
    ("Resv",        UINT64 * 3)
    ]

class VMX_EXIT_QUALIFICATION_Io (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Size",        UINT32, 3),
    ("Direction",   UINT32, 1),
    ("String",      UINT32, 1),
    ("Rep",         UINT32, 1),
    ("Encoding",    UINT32, 1),
    ("Resv",        UINT32, 9),
    ("Port",        UINT32, 16),
    ("Resv2",       UINT32)
    ]

class VMX_EXIT_QUALIFICATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Val",     UINT64),
    ("Bits",    VMX_EXIT_QUALIFICATION_Io),
    ]

class TDCALL_VEINFO_RETURN_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExitReason",              UINT32                ),
    ("Resv",                    UINT32                ),
    ("ExitQualification",       VMX_EXIT_QUALIFICATION),
    ("GuestLA",                 UINT64                ),
    ("GuestPA",                 UINT64                ),
    ("ExitInstructionLength",   UINT32                ),
    ("ExitInstructionInfo",     UINT32                ),
    ("Resv1",                   UINT32                )
    ]

class TD_RETURN_DATA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Generic", TDCALL_GENERIC_RETURN_DATA),
    ("TdInfo",  TDCALL_INFO_RETURN_DATA),
    ("VeInfo",  TDCALL_VEINFO_RETURN_DATA)
    ]

class TD_REPORT_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8),
    ("Subtype", UINT8),
    ("Version", UINT8),
    ("Rsvd",    UINT8)
    ]

class REPORTMACSTRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReportType",      TD_REPORT_TYPE),
    ("Rsvd1",           UINT8 * 12),
    ("CpuSvn",          UINT8 * 16),
    ("TeeTcbInfoHash",  UINT8 * 48),
    ("TeeInfoHash",     UINT8 * 48),
    ("ReportData",      UINT8 * 64),
    ("Rsvd2",           UINT8 * 32),
    ("Mac",             UINT8 * 32)
    ]

class TEE_TCB_SVN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Seam",    UINT8 * 2),
    ("Rsvd",    UINT8 * 14)
    ]

class TEE_TCB_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Valid",           UINT8       * 8),
    ("TeeTcbSvn",       TEE_TCB_SVN),
    ("Mrseam",          UINT8       * 48),
    ("Mrsignerseam",    UINT8       * 48),
    ("Attributes",      UINT8       * 8),
    ("Rsvd",            UINT8       * 111)
    ]

class TDINFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Attributes",      UINT8 * 8),
    ("Xfam",            UINT8 * 8),
    ("Mrtd",            UINT8 * 48),
    ("Mrconfigid",      UINT8 * 48),
    ("Mrowner",         UINT8 * 48),
    ("Mrownerconfig",   UINT8 * 48),
    ("Rtmrs",          (UINT8 * 48) * 4),
    ("Rsvd",            UINT8 * 112)
    ]

class TDREPORT_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReportMacStruct", REPORTMACSTRUCT),
    ("TeeTcbInfo",      TEE_TCB_INFO),
    ("Rsvd",            UINT8 * 17),
    ("Tdinfo",          TDINFO)
    ]

