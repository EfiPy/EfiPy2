# SmmSwDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmSwDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.MmSwDispatch import gEfiMmSwDispatchProtocolGuid

from EfiPy2.MdePkg.Pi.PiSmmCis  import EFI_SMM_HANDLER_ENTRY_POINT2

gEfiSmmSwDispatch2ProtocolGuid = gEfiMmSwDispatchProtocolGuid

class EFI_SMM_SW_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("SwSmiInputValue", UINTN)
  ]

class EFI_SMM_SW_CONTEXT (Structure):
  _fields_ = [
    ("SwSmiCpuIndex",   UINTN),
    ("CommandPort",     UINT8),
    ("DataPort",        UINT8)
  ]

class EFI_SMM_SW_DISPATCH2_PROTOCOL (Structure):
  pass

EFI_SMM_SW_REGISTER2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_SW_DISPATCH2_PROTOCOL), #   IN        *This
  EFI_SMM_HANDLER_ENTRY_POINT2,           #   IN        DispatchFunction,
  POINTER(EFI_SMM_SW_REGISTER_CONTEXT),   #   IN  OUT   *RegisterContext,
  POINTER(EFI_HANDLE)                     #   OUT       *DispatchHandle
  )

EFI_SMM_SW_UNREGISTER2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_SW_DISPATCH2_PROTOCOL), #   IN        *This
  EFI_HANDLE                              #   IN        DispatchHandle
  )

EFI_SMM_SW_DISPATCH2_PROTOCOL._fields_ = [
    ("Register",        EFI_SMM_SW_REGISTER2),
    ("UnRegister",      EFI_SMM_SW_UNREGISTER2),
    ("MaximumSwiValue", UINTN)
  ]

