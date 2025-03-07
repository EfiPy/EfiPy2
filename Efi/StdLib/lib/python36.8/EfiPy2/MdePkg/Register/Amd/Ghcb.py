# Ghcb.py
#
# EfiPy2.MdePkg.Register.Amd.Ghcb
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

UD_EXCEPTION  = 6
GP_EXCEPTION  = 13
VC_EXCEPTION  = 29

GHCB_VERSION_MIN  = 1
GHCB_VERSION_MAX  = 2

GHCB_STANDARD_USAGE  = 0

SVM_EXIT_DR7_READ   = 0x27
SVM_EXIT_DR7_WRITE  = 0x37
SVM_EXIT_RDTSC      = 0x6E
SVM_EXIT_RDPMC      = 0x6F
SVM_EXIT_CPUID      = 0x72
SVM_EXIT_INVD       = 0x76
SVM_EXIT_IOIO_PROT  = 0x7B
SVM_EXIT_MSR        = 0x7C
SVM_EXIT_VMMCALL    = 0x81
SVM_EXIT_RDTSCP     = 0x87
SVM_EXIT_WBINVD     = 0x89
SVM_EXIT_MONITOR    = 0x8A
SVM_EXIT_MWAIT      = 0x8B
SVM_EXIT_NPF        = 0x400

SVM_EXIT_MMIO_READ              = 0x80000001
SVM_EXIT_MMIO_WRITE             = 0x80000002
SVM_EXIT_NMI_COMPLETE           = 0x80000003
SVM_EXIT_AP_RESET_HOLD          = 0x80000004
SVM_EXIT_AP_JUMP_TABLE          = 0x80000005
SVM_EXIT_SNP_PAGE_STATE_CHANGE  = 0x80000010
SVM_EXIT_SNP_AP_CREATION        = 0x80000013
SVM_EXIT_GET_APIC_IDS           = 0x80000017
SVM_EXIT_HYPERVISOR_FEATURES    = 0x8000FFFD
SVM_EXIT_UNSUPPORTED            = 0x8000FFFF

IOIO_TYPE_STR   = BIT2
IOIO_TYPE_IN    = 1
IOIO_TYPE_INS   = (IOIO_TYPE_IN | IOIO_TYPE_STR)
IOIO_TYPE_OUT   = 0
IOIO_TYPE_OUTS  = (IOIO_TYPE_OUT | IOIO_TYPE_STR)

IOIO_REP  = BIT3

IOIO_ADDR_64  = BIT9
IOIO_ADDR_32  = BIT8
IOIO_ADDR_16  = BIT7

IOIO_DATA_32      = BIT6
IOIO_DATA_16      = BIT5
IOIO_DATA_8       = BIT4
IOIO_DATA_MASK    = (BIT6 | BIT5 | BIT4)
IOIO_DATA_OFFSET  = 4
def IOIO_DATA_BYTES(x):
  return ((x) & IOIO_DATA_MASK) >> IOIO_DATA_OFFSET

IOIO_SEG_ES  = 0
IOIO_SEG_DS  = (BIT11 | BIT10)

SVM_VMGEXIT_SNP_AP_CREATE_ON_INIT  = 0
SVM_VMGEXIT_SNP_AP_CREATE          = 1
SVM_VMGEXIT_SNP_AP_DESTROY         = 2

class GHCB_SAVE_AREA (Structure):
  _fields_ = [
    ("Reserved1",   UINT8 * 203),
    ("Cpl",         UINT8),
    ("Reserved8",   UINT8 * 300),
    ("Rax",         UINT64),
    ("Reserved4",   UINT8 * 264),
    ("Rcx",         UINT64),
    ("Rdx",         UINT64),
    ("Rbx",         UINT64),
    ("Reserved5",   UINT8 * 112),
    ("SwExitCode",  UINT64),
    ("SwExitInfo1", UINT64),
    ("SwExitInfo2", UINT64),
    ("SwScratch",   UINT64),
    ("Reserved6",   UINT8 * 56),
    ("XCr0",        UINT64),
    ("ValidBitmap", UINT8 * 16),
    ("X87StateGpa", UINT64),
    ("Reserved7",   UINT8 * 1016)
  ]

class GHCB (Structure):
  _fields_ = [
    ("SaveArea",        GHCB_SAVE_AREA),
    ("SharedBuffer",    UINT8 * 2032),
    ("Reserved1",       UINT8 * 10),
    ("ProtocolVersion", UINT16),
    ("GhcbUsage",       UINT32)
  ]

def GHCB_SAVE_AREA_QWORD_OFFSET(RegisterField):
  return OFFSET_OF (GHCB, SaveArea.RegisterField) // sizeof (UINT64)

class GHCB_EXIT_INFO_Elements (Structure):
  _fields_ = [
    ("Lower32Bits", UINT32),
    ("Upper32Bits", UINT32)
  ]

class GHCB_EXIT_INFO (Union):
  _fields_ = [
    ("Elements",    GHCB_EXIT_INFO_Elements),
    ("Uint64",      UINT64)
  ]

class GHCB_EVENT_INJECTION_Elements (Structure):
  _fields_ = [
    ("Vector",          UINT32, 8),
    ("Type",            UINT32, 3),
    ("ErrorCodeValid",  UINT32, 1),
    ("Rsvd",            UINT32, 19),
    ("Valid",           UINT32, 1),
    ("ErrorCode",       UINT32)
  ]

class GHCB_EVENT_INJECTION (Union):
  _fields_ = [
    ("Elements",    GHCB_EVENT_INJECTION_Elements),
    ("Uint64",      UINT64)
  ]

GHCB_EVENT_INJECTION_TYPE_INT        = 0
GHCB_EVENT_INJECTION_TYPE_NMI        = 2
GHCB_EVENT_INJECTION_TYPE_EXCEPTION  = 3
GHCB_EVENT_INJECTION_TYPE_SOFT_INT   = 4

GHCB_HV_FEATURES_SNP                             = BIT0
GHCB_HV_FEATURES_SNP_AP_CREATE                   = (GHCB_HV_FEATURES_SNP | BIT1)
GHCB_HV_FEATURES_SNP_RESTRICTED_INJECTION        = (GHCB_HV_FEATURES_SNP_AP_CREATE | BIT2)
GHCB_HV_FEATURES_SNP_RESTRICTED_INJECTION_TIMER  = (GHCB_HV_FEATURES_SNP_RESTRICTED_INJECTION | BIT3)

SNP_PAGE_STATE_PRIVATE  = 1
SNP_PAGE_STATE_SHARED   = 2
SNP_PAGE_STATE_PSMASH   = 3
SNP_PAGE_STATE_UNSMASH  = 4

class SNP_PAGE_STATE_ENTRY (Structure):
  _fields_ = [
    ("CurrentPage",     UINT64, 12),
    ("GuestFrameNumber",UINT64, 40),
    ("Operation",       UINT64, 4),
    ("PageSize",        UINT64, 1),
    ("Reserved",        UINT64, 7)
  ]

class SNP_PAGE_STATE_HEADER (Structure):
  _fields_ = [
    ("CurrentEntry",    UINT16),
    ("EndEntry",        UINT16),
    ("Reserved",        UINT32)
  ]

class SNP_PAGE_STATE_CHANGE_INFO (Structure):
  _fields_ = [
    ("Header",  SNP_PAGE_STATE_HEADER)
    # ("Entry",   SNP_PAGE_STATE_ENTRY * SNP_PAGE_STATE_MAX_ENTRY)
  ]

SNP_PAGE_STATE_MAX_ENTRY  = \
   (((GHCB.SharedBuffer.offset) - sizeof (SNP_PAGE_STATE_HEADER)) / sizeof (SNP_PAGE_STATE_ENTRY))
class GHCB_APIC_IDS (Structure):
  _fields_ = [
    ("NumEntries",  UINT32)
    # ("ApicIds",   UINT32 * N)
  ]

SEV_ES_RESET_CODE_SEGMENT_TYPE  = 0xA
SEV_ES_RESET_DATA_SEGMENT_TYPE  = 0x2

SEV_ES_RESET_LDT_TYPE  = 0x2
SEV_ES_RESET_TSS_TYPE  = 0x3

class SEV_ES_SEGMENT_REGISTER_ATTRIBUTES_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT16, 4),
    ("Sbit",        UINT16, 1),
    ("Dpl",         UINT16, 2),
    ("Present",     UINT16, 1),
    ("Avl",         UINT16, 1),
    ("Reserved1",   UINT16, 1),
    ("Db",          UINT16, 1),
    ("Granularity", UINT16, 1)
  ]

class SEV_ES_SEGMENT_REGISTER_ATTRIBUTES (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    SEV_ES_SEGMENT_REGISTER_ATTRIBUTES_Bits),
    ("Uint16",      UINT16)
  ]

class SEV_ES_SEGMENT_REGISTER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Selector",    UINT16),
    ("Attributes",  SEV_ES_SEGMENT_REGISTER_ATTRIBUTES),
    ("Limit",       UINT32),
    ("Base",        UINT64)
  ]

class SEV_ES_SAVE_AREA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Es",          SEV_ES_SEGMENT_REGISTER),
    ("Cs",          SEV_ES_SEGMENT_REGISTER),
    ("Ss",          SEV_ES_SEGMENT_REGISTER),
    ("Ds",          SEV_ES_SEGMENT_REGISTER),
    ("Fs",          SEV_ES_SEGMENT_REGISTER),
    ("Gs",          SEV_ES_SEGMENT_REGISTER),
    ("Gdtr",        SEV_ES_SEGMENT_REGISTER),
    ("Ldtr",        SEV_ES_SEGMENT_REGISTER),
    ("Idtr",        SEV_ES_SEGMENT_REGISTER),
    ("Tr",          SEV_ES_SEGMENT_REGISTER),
    ("Reserved1",   UINT8 * 42),
    ("Vmpl",        UINT8),
    ("Reserved2",   UINT8 * 5),
    ("Efer",        UINT64),
    ("Reserved3",   UINT8 * 112),
    ("Cr4",         UINT64),
    ("Reserved4",   UINT8 * 8),
    ("Cr0",         UINT64),
    ("Dr7",         UINT64),
    ("Dr6",         UINT64),
    ("Rflags",      UINT64),
    ("Rip",         UINT64),
    ("Reserved5",   UINT8 * 232),
    ("GPat",        UINT64),
    ("Reserved6",   UINT8 * 230),
    ("SevFeatures", UINT64),
    ("Reserved7",   UINT8 * 48),
    ("XCr0",        UINT64),
    ("Reserved8",   UINT8 * 24),
    ("Mxcsr",       UINT32),
    ("X87Ftw",      UINT16),
    ("Reserved9",   UINT8 * 2),
    ("X87Fcw",      UINT16)
  ]

