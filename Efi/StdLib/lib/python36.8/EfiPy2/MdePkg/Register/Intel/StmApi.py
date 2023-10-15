# StmApi.py
#
# EfiPy2.MdePkg.Register.Intel.StmApi
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr      import MSEG_HEADER
from EfiPy2.MdePkg.Register.Intel.StmResourceDescriptor import STM_RSC

class STM_FEAT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Intel64ModeSupported",    UINT32, 1),
    ("EptSupported",            UINT32, 1),
    ("Reserved",                UINT32, 30)
  ]

STM_SPEC_VERSION_MAJOR  = 1
STM_SPEC_VERSION_MINOR  = 0

class SOFTWARE_STM_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("StmSpecVerMajor",             UINT8),
    ("StmSpecVerMinor",             UINT8),
    ("Reserved",                    UINT16),
    ("StaticImageSize",             UINT32),
    ("PerProcDynamicMemorySize",    UINT32),
    ("AdditionalDynamicMemorySize", UINT32),
    ("StmFeatures",                 STM_FEAT),
    ("NumberOfRevIDs",              UINT32),
    ("StmSmmRevID",                 UINT32 * 1)
  ]

class STM_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HwStmHdr",    MSEG_HEADER),
    ("SwStmHdr",    SOFTWARE_STM_HEADER)
  ]

class STM_MAP_ADDRESS_RANGE_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("PhysicalAddress", UINT64),
    ("VirtualAddress",  UINT64),
    ("PageCount",       UINT32),
    ("PatCacheType",    UINT32)
  ]

STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_ST_UC        = 0x00
STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_WC           = 0x01
STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_WT           = 0x04
STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_WP           = 0x05
STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_WB           = 0x06
STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_UC           = 0x07
STM_MAP_ADDRESS_RANGE_PAT_CACHE_TYPE_FOLLOW_MTRR  = 0xFFFFFFFF

STM_API_UNMAP_ADDRESS_RANGE  = 0x00000002

class STM_UNMAP_ADDRESS_RANGE_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("VirtualAddress",  UINT64),
    ("Length",          UINT32)
  ]

class STM_ADDRESS_LOOKUP_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("InterruptedGuestVirtualAddress",  UINT64),
    ("Length",                          UINT32),
    ("InterruptedCr3",                  UINT64),
    ("InterruptedEptp",                 UINT64),
    ("MapToSmmGuest",                   UINT32, 2),
    ("InterruptedCr4Pae",               UINT32, 1),
    ("InterruptedCr4Pse",               UINT32, 1),
    ("InterruptedIa32eMode",            UINT32, 1),
    ("Reserved1",                       UINT32, 27),
    ("Reserved2",                       UINT32),
    ("PhysicalAddress",                 UINT64),
    ("SmmGuestVirtualAddress",          UINT64)
  ]

STM_ADDRESS_LOOKUP_DESCRIPTOR_DO_NOT_MAP                 = 0
STM_ADDRESS_LOOKUP_DESCRIPTOR_ONE_TO_ONE                 = 1
STM_ADDRESS_LOOKUP_DESCRIPTOR_VIRTUAL_ADDRESS_SPECIFIED  = 3

STM_API_RETURN_FROM_PROTECTION_EXCEPTION  = 0x00000004

STM_API_START = BIT16 | 1

STM_CONFIG_SMI_UNBLOCKING_BY_VMX_OFF  = BIT0

STM_API_STOP  = BIT16 | 2

STM_API_PROTECT_RESOURCE  = BIT16 | 3

STM_API_UNPROTECT_RESOURCE  = BIT16 | 4

STM_API_GET_BIOS_RESOURCES  = BIT16 | 5

STM_API_MANAGE_VMCS_DATABASE  = BIT16 | 6

class STM_VMCS_DATABASE_REQUEST (Structure):
  _pack_   = 1
  _fields_ = [
    ("VmcsPhysPointer",     UINT64),
    ("DomainType",          UINT32, 4),
    ("XStatePolicy",        UINT32, 2),
    ("DegradationPolicy",   UINT32, 4),
    ("Reserved1",           UINT32, 22),
    ("AddOrRemove",         UINT32)
  ]

DOMAIN_UNPROTECTED            = 0
DOMAIN_DISALLOWED_IO_OUT      = BIT0
DOMAIN_DISALLOWED_IO_IN       = BIT1
DOMAIN_INTEGRITY              = BIT2
DOMAIN_CONFIDENTIALITY        = BIT3
DOMAIN_INTEGRITY_PROT_OUT_IN  = DOMAIN_INTEGRITY
DOMAIN_FULLY_PROT_OUT_IN      = DOMAIN_CONFIDENTIALITY | DOMAIN_INTEGRITY
DOMAIN_FULLY_PROT             = DOMAIN_FULLY_PROT_OUT_IN | DOMAIN_DISALLOWED_IO_IN | DOMAIN_DISALLOWED_IO_OUT

XSTATE_READWRITE  = 0x00
XSTATE_READONLY   = 0x01
XSTATE_SCRUB      = 0x03

STM_VMCS_DATABASE_REQUEST_ADD     = 1
STM_VMCS_DATABASE_REQUEST_REMOVE  = 0

STM_API_INITIALIZE_PROTECTION  = BIT16 | 7

STM_RSC_BGI  = BIT1
STM_RSC_BGM  = BIT2
STM_RSC_MSR  = BIT3

STM_API_MANAGE_EVENT_LOG  = BIT16 | 8

class STM_EVENT_LOG_MANAGEMENT_REQUEST_Data_LogBuffer (Structure):
  _pack_   = 1
  _fields_ = [
    ("PageCount",   UINT32),
    ("Pages",       UINT64 * 1)
  ]

class STM_EVENT_LOG_MANAGEMENT_REQUEST_Data (Union):
  _pack_   = 1
  _fields_ = [
    ("LogBuffer",           STM_EVENT_LOG_MANAGEMENT_REQUEST_Data_LogBuffer),
    ("EventEnableBitmap",   UINT32)
  ]

class STM_EVENT_LOG_MANAGEMENT_REQUEST (Structure):
  _pack_   = 1
  _fields_ = [
    ("Data",    STM_EVENT_LOG_MANAGEMENT_REQUEST_Data)
  ]

STM_EVENT_LOG_MANAGEMENT_REQUEST_NEW_LOG        = 1
STM_EVENT_LOG_MANAGEMENT_REQUEST_CONFIGURE_LOG  = 2
STM_EVENT_LOG_MANAGEMENT_REQUEST_START_LOG      = 3
STM_EVENT_LOG_MANAGEMENT_REQUEST_STOP_LOG       = 4
STM_EVENT_LOG_MANAGEMENT_REQUEST_CLEAR_LOG      = 5
STM_EVENT_LOG_MANAGEMENT_REQUEST_DELETE_LOG     = 6

class LOG_ENTRY_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventSerialNumber",   UINT32),
    ("Type",                UINT16),
    ("Lock",                UINT16, 1),
    ("Valid",               UINT16, 1),
    ("ReadByMle",           UINT16, 1),
    ("Wrapped",             UINT16, 1),
    ("Reserved",            UINT16, 12)
  ]

EvtLogStarted                       = 0 
EvtLogStopped                       = 1 
EvtLogInvalidParameterDetected      = 2 
EvtHandledProtectionException       = 3 
EvtBiosAccessToUnclaimedResource    = 4 
EvtMleResourceProtectionGranted     = 5 
EvtMleResourceProtectionDenied      = 6 
EvtMleResourceUnprotect             = 7 
EvtMleResourceUnprotectError        = 8 
EvtMleDomainTypeDegraded            = 9 
EvtMleMax                           = 10
EvtInvalid                          = 0xFFFFFFFF
EVENT_TYPE                          = ENUM

class ENTRY_EVT_LOG_STARTED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32)
  ]

class ENTRY_EVT_LOG_STOPPED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32)
  ]

class ENTRY_EVT_LOG_INVALID_PARAM (Structure):
  _pack_   = 1
  _fields_ = [
    ("ReserVmcallApiNumberved", UINT32)
  ]

class ENTRY_EVT_LOG_HANDLED_PROTECTION_EXCEPTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resource",    STM_RSC)
  ]

class ENTRY_EVT_BIOS_ACCESS_UNCLAIMED_RSC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resource",    STM_RSC)
  ]

class ENTRY_EVT_MLE_RSC_PROT_GRANTED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resource",    STM_RSC)
  ]

class ENTRY_EVT_MLE_RSC_PROT_DENIED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resource",    STM_RSC)
  ]

class ENTRY_EVT_MLE_RSC_UNPROT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resource",    STM_RSC)
  ]

class ENTRY_EVT_MLE_RSC_UNPROT_ERROR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resource",    STM_RSC)
  ]

class ENTRY_EVT_MLE_DOMAIN_TYPE_DEGRADED (Structure):
  _pack_   = 1
  _fields_ = [
    ("VmcsPhysPointer",     UINT64),
    ("ExpectedDomainType",  UINT8),
    ("DegradedDomainType",  UINT8)
  ]

class LOG_ENTRY_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("Started",                     ENTRY_EVT_LOG_STARTED),
    ("Stopped",                     ENTRY_EVT_LOG_STOPPED),
    ("InvalidParam",                ENTRY_EVT_LOG_INVALID_PARAM),
    ("HandledProtectionException",  ENTRY_EVT_LOG_HANDLED_PROTECTION_EXCEPTION),
    ("BiosUnclaimedRsc",            ENTRY_EVT_BIOS_ACCESS_UNCLAIMED_RSC),
    ("MleRscProtGranted",           ENTRY_EVT_MLE_RSC_PROT_GRANTED),
    ("MleRscProtDenied",            ENTRY_EVT_MLE_RSC_PROT_DENIED),
    ("MleRscUnprot",                ENTRY_EVT_MLE_RSC_UNPROT),
    ("MleRscUnprotError",           ENTRY_EVT_MLE_RSC_UNPROT_ERROR),
    ("MleDomainTypeDegraded",       ENTRY_EVT_MLE_DOMAIN_TYPE_DEGRADED)
  ]

class STM_LOG_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",     LOG_ENTRY_HEADER),
    ("Data",    LOG_ENTRY_DATA)
  ]

STM_LOG_ENTRY_SIZE  = 256

class STM_PROTECTION_EXCEPTION_STACK_FRAME_IA32 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Rdi",                         UINT32),
    ("Rsi",                         UINT32),
    ("Rbp",                         UINT32),
    ("Rdx",                         UINT32),
    ("Rcx",                         UINT32),
    ("Rbx",                         UINT32),
    ("Rax",                         UINT32),
    ("Cr3",                         UINT32),
    ("Cr2",                         UINT32),
    ("Cr0",                         UINT32),
    ("VmcsExitInstructionInfo",     UINT32),
    ("VmcsExitInstructionLength",   UINT32),
    ("VmcsExitQualification",       UINT64),
    ("ErrorCode",                   UINT32),
    ("Rip",                         UINT32),
    ("Cs",                          UINT32),
    ("Rflags",                      UINT32),
    ("Rsp",                         UINT32),
    ("Ss",                          UINT32)
  ]

class STM_PROTECTION_EXCEPTION_STACK_FRAME_X64 (Structure):
  _pack_   = 1
  _fields_ = [
    ("R15",                         UINT64),
    ("R14",                         UINT64),
    ("R13",                         UINT64),
    ("R12",                         UINT64),
    ("R11",                         UINT64),
    ("R10",                         UINT64),
    ("R9",                          UINT64),
    ("R8",                          UINT64),
    ("Rdi",                         UINT64),
    ("Rsi",                         UINT64),
    ("Rbp",                         UINT64),
    ("Rdx",                         UINT64),
    ("Rcx",                         UINT64),
    ("Rbx",                         UINT64),
    ("Rax",                         UINT64),
    ("Cr8",                         UINT64),
    ("Cr3",                         UINT64),
    ("Cr2",                         UINT64),
    ("Cr0",                         UINT64),
    ("VmcsExitInstructionInfo",     UINT64),
    ("VmcsExitInstructionLength",   UINT64),
    ("VmcsExitQualification",       UINT64),
    ("ErrorCode",                   UINT64),
    ("Rip",                         UINT64),
    ("Cs",                          UINT64),
    ("Rflags",                      UINT64),
    ("Rsp",                         UINT64),
    ("Ss",                          UINT64)
  ]

class STM_PROTECTION_EXCEPTION_STACK_FRAME (Union):
  _pack_   = 1
  _fields_ = [
    ("Ia32StackFrame",  POINTER(STM_PROTECTION_EXCEPTION_STACK_FRAME_IA32)),
    ("X64StackFrame",   POINTER(STM_PROTECTION_EXCEPTION_STACK_FRAME_X64))
  ]

TxtSmmPageViolation                 = 1
TxtSmmMsrViolation                  = 2
TxtSmmRegisterViolation             = 3
TxtSmmIoViolation                   = 4
TxtSmmPciViolation                  = 5
TXT_SMM_PROTECTION_EXCEPTION_TYPE   = ENUM

class STM_PROTECTION_EXCEPTION_HANDLER (Structure):
  _pack_   = 1
  _fields_ = [
    ("SpeRip",                      UINT64),
    ("SpeRsp",                      UINT64),
    ("SpeSs",                       UINT16),
    ("PageViolationException",      UINT16, 1),
    ("MsrViolationException",       UINT16, 1),
    ("RegisterViolationException",  UINT16, 1),
    ("IoViolationException",        UINT16, 1),
    ("PciViolationException",       UINT16, 1),
    ("Reserved1",                   UINT16, 11),
    ("Reserved2",                   UINT32)
  ]

class STM_SMM_ENTRY_STATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExecutionDisableOutsideSmrr", UINT8, 1),
    ("Intel64Mode",                 UINT8, 1),
    ("Cr4Pae",                      UINT8, 1),
    ("Cr4Pse",                      UINT8, 1),
    ("Reserved1",                   UINT8, 4),
  ]

class STM_SMM_RESUME_STATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("SmramToVmcsRestoreRequired",  UINT8, 1),
    ("ReinitializeVmcsRequired",    UINT8, 1),
    ("Reserved2",                   UINT8, 6)
  ]

class STM_SMM_STATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("DomainType",      UINT8, 4),
    ("XStatePolicy",    UINT8, 2),
    ("EptEnabled",      UINT8, 1),
    ("Reserved3",       UINT8, 1)
  ]

TXT_SMM_PSD_OFFSET                          = 0xfb00
TXT_PROCESSOR_SMM_DESCRIPTOR_SIGNATURE      = SIGNATURE_64('T', 'X', 'T', 'P', 'S', 'S', 'I', 'G')
TXT_PROCESSOR_SMM_DESCRIPTOR_VERSION_MAJOR  = 1
TXT_PROCESSOR_SMM_DESCRIPTOR_VERSION_MINOR  = 0

class TXT_PROCESSOR_SMM_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Signature",                       UINT64),
    ("Size",                            UINT16),
    ("SmmDescriptorVerMajor",           UINT8),
    ("SmmDescriptorVerMinor",           UINT8),
    ("LocalApicId",                     UINT32),
    ("SmmEntryState",                   STM_SMM_ENTRY_STATE),
    ("SmmResumeState",                  STM_SMM_RESUME_STATE),
    ("StmSmmState",                     STM_SMM_STATE),
    ("Reserved4",                       UINT8),
    ("SmmCs",                           UINT16),
    ("SmmDs",                           UINT16),
    ("SmmSs",                           UINT16),
    ("SmmOtherSegment",                 UINT16),
    ("SmmTr",                           UINT16),
    ("Reserved5",                       UINT16),
    ("SmmCr3",                          UINT64),
    ("SmmStmSetupRip",                  UINT64),
    ("SmmStmTeardownRip",               UINT64),
    ("SmmSmiHandlerRip",                UINT64),
    ("SmmSmiHandlerRsp",                UINT64),
    ("SmmGdtPtr",                       UINT64),
    ("SmmGdtSize",                      UINT32),
    ("RequiredStmSmmRevId",             UINT32),
    ("StmProtectionExceptionHandler",   STM_PROTECTION_EXCEPTION_HANDLER),
    ("Reserved6",                       UINT64),
    ("BiosHwResourceRequirementsPtr",   UINT64),
    ("AcpiRsdp",                        UINT64),
    ("PhysicalAddressBits",             UINT8)
  ]

