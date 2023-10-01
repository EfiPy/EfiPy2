# MmGpiDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmGpiDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmGpiDispatchProtocolGuid = \
  EFI_GUID (0x25566b03, 0xb577, 0x4cbf, (0x95, 0x8c, 0xed, 0x66, 0x3e, 0xa2, 0x43, 0x80 ))

class EFI_MM_GPI_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("GpiNum", UINT64)
  ]

class EFI_MM_GPI_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_GPI_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_GPI_DISPATCH_PROTOCOL),    #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,               #   IN       DispatchFunction,
  POINTER(EFI_MM_GPI_REGISTER_CONTEXT),     #   IN CONST *RegisterContext,
  POINTER(EFI_HANDLE)                       #   OUT      *DispatchHandle
  )

EFI_MM_GPI_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_GPI_DISPATCH_PROTOCOL),    #   IN CONST *This
  EFI_HANDLE                                #   IN       DispatchHandle
  )

EFI_MM_GPI_DISPATCH_PROTOCOL._fields_ = [
    ("Register",            EFI_MM_GPI_REGISTER),
    ("UnRegister",          EFI_MM_GPI_UNREGISTER),
    ("NumSupportedGpis",    UINTN)
  ]

