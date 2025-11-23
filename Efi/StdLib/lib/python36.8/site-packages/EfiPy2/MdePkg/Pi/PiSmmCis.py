# PiSmmCis.py
#
# EfiPy2.MdePkg.Pi.PiSmmCis
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi       import PiMmCis
from EfiPy2.MdePkg.Protocol import SmmCpuIo2

class EFI_SMM_SYSTEM_TABLE2 (Structure):
  pass

SMM_SMST_SIGNATURE                = PiMmCis.MM_MMST_SIGNATURE
SMM_SPECIFICATION_MAJOR_REVISION  = PiMmCis.MM_SPECIFICATION_MAJOR_REVISION
SMM_SPECIFICATION_MINOR_REVISION  = PiMmCis.MM_SPECIFICATION_MINOR_REVISION
EFI_SMM_SYSTEM_TABLE2_REVISION    = PiMmCis.EFI_MM_SYSTEM_TABLE_REVISION

EFI_SMM_INSTALL_CONFIGURATION_TABLE2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_SYSTEM_TABLE2),  # IN CONST *SystemTable,
  POINTER(EFI_GUID),               # IN CONST *Guid,
  PVOID,                           # IN       *Table,
  UINTN                            # IN       TableSize
  )

EFI_SMM_STARTUP_THIS_AP             = PiMmCis.EFI_MM_STARTUP_THIS_AP
EFI_SMM_NOTIFY_FN                   = PiMmCis.EFI_MM_NOTIFY_FN
EFI_SMM_REGISTER_PROTOCOL_NOTIFY    = PiMmCis.EFI_MM_REGISTER_PROTOCOL_NOTIFY
EFI_SMM_INTERRUPT_MANAGE            = PiMmCis.EFI_MM_INTERRUPT_MANAGE
EFI_SMM_HANDLER_ENTRY_POINT2        = PiMmCis.EFI_MM_HANDLER_ENTRY_POINT
EFI_SMM_INTERRUPT_REGISTER          = PiMmCis.EFI_MM_INTERRUPT_REGISTER
EFI_SMM_INTERRUPT_UNREGISTER        = PiMmCis.EFI_MM_INTERRUPT_UNREGISTER

class EFI_SMM_ENTRY_CONTEXT (Structure):
  _fields_ = [
    ("SmmStartupThisAp",        EFI_SMM_STARTUP_THIS_AP),
    ("CurrentlyExecutingCpu",   UINTN),
    ("NumberOfCpus",            UINTN),
    ("CpuSaveStateSize",        POINTER(UINTN),),
    ("CpuSaveState",            POINTER(PVOID)),
  ]

EFI_SMM_ENTRY_POINT = CFUNCTYPE (
  None,
  POINTER(EFI_SMM_ENTRY_CONTEXT)    # IN CONST  *SmmEntryContext
  )

EFI_SMM_SYSTEM_TABLE2._fields_ = [
    ("Hdr",                             EFI_TABLE_HEADER),
    ("SmmFirmwareVendor",               POINTER(CHAR16)),
    ("SmmFirmwareRevision",             UINT32),
    ("SmmInstallConfigurationTable",    EFI_SMM_INSTALL_CONFIGURATION_TABLE2),
    ("SmmIo",                           SmmCpuIo2.EFI_SMM_CPU_IO2_PROTOCOL),
    ("SmmAllocatePool",                 EFI_ALLOCATE_POOL),
    ("SmmFreePool",                     EFI_FREE_POOL),
    ("SmmAllocatePages",                EFI_ALLOCATE_PAGES),
    ("SmmFreePages",                    EFI_FREE_PAGES),
    ("SmmStartupThisAp",                EFI_SMM_STARTUP_THIS_AP),
    ("CurrentlyExecutingCpu",           UINTN),
    ("NumberOfCpus",                    UINTN),
    ("CpuSaveStateSize",                POINTER(UINTN)),
    ("CpuSaveState",                    POINTER(PVOID)),
    ("NumberOfTableEntries",            UINTN),
    ("SmmConfigurationTable",           POINTER(EFI_CONFIGURATION_TABLE)),
    ("SmmInstallProtocolInterface",     EFI_INSTALL_PROTOCOL_INTERFACE),
    ("SmmUninstallProtocolInterface",   EFI_UNINSTALL_PROTOCOL_INTERFACE),
    ("SmmHandleProtocol",               EFI_HANDLE_PROTOCOL),
    ("SmmRegisterProtocolNotify",       EFI_SMM_REGISTER_PROTOCOL_NOTIFY),
    ("SmmLocateHandle",                 EFI_LOCATE_HANDLE),
    ("SmmLocateProtocol",               EFI_LOCATE_PROTOCOL),
    ("SmiManage",                       EFI_SMM_INTERRUPT_MANAGE),
    ("SmiHandlerRegister",              EFI_SMM_INTERRUPT_REGISTER),
    ("SmiHandlerUnRegister",            EFI_SMM_INTERRUPT_UNREGISTER)
  ]

