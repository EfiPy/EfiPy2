# PiMmCis.py
#
# EfiPy2.MdePkg.Pi.PiMmCis
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi       import PiMultiPhase
from EfiPy2.MdePkg.Protocol import MmCpuIo

class EFI_MM_SYSTEM_TABLE (Structure):
  pass

MM_MMST_SIGNATURE  = SIGNATURE_32 ('S', 'M', 'S', 'T')

MM_SPECIFICATION_MAJOR_REVISION  = 1
MM_SPECIFICATION_MINOR_REVISION  = 60
EFI_MM_SYSTEM_TABLE_REVISION     = ((MM_SPECIFICATION_MAJOR_REVISION<<16) | (MM_SPECIFICATION_MINOR_REVISION))

EFI_MM_INSTALL_CONFIGURATION_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SYSTEM_TABLE), # IN CONST *SystemTable,
  POINTER(EFI_GUID),            # IN CONST *Guid,
  PVOID,                        # IN *Table,
  UINTN                         # IN TableSize
  )

EFI_MM_STARTUP_THIS_AP = CFUNCTYPE (
  EFI_STATUS,
  PiMultiPhase.EFI_AP_PROCEDURE,    # IN      Procedure,
  UINTN,                            # IN      CpuNumber,
  PVOID                             # IN OUT *ProcArguments OPTIONAL
  )

EFI_MM_NOTIFY_FN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Protocol,
  PVOID,              # IN *Interface,
  EFI_HANDLE          # IN Handle
  )

EFI_MM_REGISTER_PROTOCOL_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),    # IN  CONST *Protocol,
  EFI_MM_NOTIFY_FN,     # IN        Function,
  POINTER(PVOID)        # OUT       **Registration
  )

EFI_MM_INTERRUPT_MANAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),    # IN CONST *HandlerType,
  PVOID,                # IN CONST *Context         OPTIONAL,
  PVOID,                # IN OUT   *CommBuffer      OPTIONAL,
  POINTER(UINTN)        # IN OUT   *CommBufferSize  OPTIONAL
  )

EFI_MM_HANDLER_ENTRY_POINT = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,     # IN       DispatchHandle,
  PVOID,          # IN CONST *Context         OPTIONAL,
  PVOID,          # IN OUT   *CommBuffer      OPTIONAL,
  POINTER(UINTN)  # IN OUT   *CommBufferSize  OPTIONAL
  )

EFI_MM_INTERRUPT_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_MM_HANDLER_ENTRY_POINT, # IN          Handler,
  POINTER(EFI_GUID),          # IN  CONST   *HandlerType OPTIONAL,
  POINTER(EFI_HANDLE)         # OUT         *DispatchHandle
  )

EFI_MM_INTERRUPT_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE    # IN  DispatchHandle
  )

class EFI_MM_ENTRY_CONTEXT (Structure):
  _fields_ = [
    ("MmStartupThisAp",         EFI_MM_STARTUP_THIS_AP),
    ("CurrentlyExecutingCpu",   UINTN),
    ("NumberOfCpus",            UINTN),
    ("CpuSaveStateSize",        POINTER(UINTN)),
    ("CpuSaveState",            POINTER(PVOID))
  ]

EFI_MM_ENTRY_POINT = CFUNCTYPE (
  None,
  POINTER(EFI_MM_ENTRY_CONTEXT) # IN CONST MmEntryContext
  )

EFI_MM_SYSTEM_TABLE._fields_ = [
    ("Hdr",                          EFI_TABLE_HEADER),
    ("MmFirmwareVendor",             POINTER(CHAR16)),
    ("MmFirmwareRevision",           UINT32),
    ("MmInstallConfigurationTable",  EFI_MM_INSTALL_CONFIGURATION_TABLE),
    ("MmIo",                         MmCpuIo.EFI_MM_CPU_IO_PROTOCOL),
    ("MmAllocatePool",               EFI_ALLOCATE_POOL),
    ("MmFreePool",                   EFI_FREE_POOL),
    ("MmAllocatePages",              EFI_ALLOCATE_PAGES),
    ("MmFreePages",                  EFI_FREE_PAGES),
    ("MmStartupThisAp",              EFI_MM_STARTUP_THIS_AP),
    ("CurrentlyExecutingCpu",        UINTN),
    ("NumberOfCpus",                 UINTN),
    ("CpuSaveStateSize",             POINTER(UINTN)),
    ("CpuSaveState",                 POINTER(PVOID)),
    ("NumberOfTableEntries",         UINTN),
    ("MmConfigurationTable",         POINTER(EFI_CONFIGURATION_TABLE)),
    ("MmInstallProtocolInterface",   EFI_INSTALL_PROTOCOL_INTERFACE),
    ("MmUninstallProtocolInterface", EFI_UNINSTALL_PROTOCOL_INTERFACE),
    ("MmHandleProtocol",             EFI_HANDLE_PROTOCOL),
    ("MmRegisterProtocolNotify",     EFI_MM_REGISTER_PROTOCOL_NOTIFY),
    ("MmLocateHandle",               EFI_LOCATE_HANDLE),
    ("MmLocateProtocol",             EFI_LOCATE_PROTOCOL),
    ("MmiManage",                    EFI_MM_INTERRUPT_MANAGE),
    ("MmiHandlerRegister",           EFI_MM_INTERRUPT_REGISTER),
    ("MmiHandlerUnRegister",         EFI_MM_INTERRUPT_UNREGISTER)
  ]

