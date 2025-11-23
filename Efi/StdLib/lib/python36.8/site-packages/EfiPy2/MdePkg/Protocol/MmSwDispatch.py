# MmSwDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmSwDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmSwDispatchProtocolGuid = \
  EFI_GUID (0x18a3c6dc, 0x5eea, 0x48c8, (0xa1, 0xc1, 0xb5, 0x33, 0x89, 0xf9, 0x89, 0x99 ))

class EFI_MM_SW_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("SwMmiInputValue", UINTN)
  ]

class EFI_MM_SW_CONTEXT (Structure):
  _fields_ = [
    ("SwMmiCpuIndex",   UINTN),
    ("CommandPort",     UINT8),
    ("DataPort",        UINT8)
  ]

class EFI_MM_SW_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_SW_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SW_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,           #   IN        DispatchFunction,
  POINTER(EFI_MM_SW_REGISTER_CONTEXT),  #   IN  OUT   *RegisterContext,
  POINTER(EFI_HANDLE)                   #   OUT       *DispatchHandle
  )

EFI_MM_SW_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SW_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_HANDLE                            #   IN        DispatchHandle
  )

EFI_MM_SW_DISPATCH_PROTOCOL._fields_ = [
    ("Register",        EFI_MM_SW_REGISTER),
    ("UnRegister",      EFI_MM_SW_UNREGISTER),
    ("MaximumSwiValue", UINTN)
  ]

