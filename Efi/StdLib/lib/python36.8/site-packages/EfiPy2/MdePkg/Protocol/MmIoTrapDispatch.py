# MmIoTrapDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmIoTrapDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmIoTrapDispatchProtocolGuid = \
  EFI_GUID (0x58dc368d, 0x7bfa, 0x4e77, (0xab, 0xbc, 0xe, 0x29, 0x41, 0x8d, 0xf9, 0x30 ))

WriteTrap                       = 1
ReadTrap                        = 2
ReadWriteTrap                   = 3
IoTrapTypeMaximum               = 4
EFI_MM_IO_TRAP_DISPATCH_TYPE    = ENUM

class EFI_MM_IO_TRAP_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Address", UINT16),
    ("Length",  UINT16),
    ("Type",    EFI_MM_IO_TRAP_DISPATCH_TYPE)
  ]

class EFI_MM_IO_TRAP_CONTEXT (Structure):
  _fields_ = [
    ("WriteData",   UINT32)
  ]

class EFI_MM_IO_TRAP_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_IO_TRAP_DISPATCH_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_IO_TRAP_DISPATCH_PROTOCOL),    #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,                   #   IN       DispatchFunction,
  POINTER(EFI_MM_IO_TRAP_REGISTER_CONTEXT),     #   IN OUT   *RegisterContext,
  POINTER(EFI_HANDLE)                           #   OUT      *DispatchHandle
  )

EFI_MM_IO_TRAP_DISPATCH_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_IO_TRAP_DISPATCH_PROTOCOL),    #   IN CONST *This
  EFI_HANDLE                                    #   IN       DispatchHandle
  )

EFI_MM_IO_TRAP_DISPATCH_PROTOCOL._fields_ = [
    ("Register",            EFI_MM_IO_TRAP_DISPATCH_REGISTER),
    ("UnRegister",          EFI_MM_IO_TRAP_DISPATCH_UNREGISTER)
  ]

