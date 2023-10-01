# MmSxDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmSxDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmSxDispatchProtocolGuid = \
  EFI_GUID (0x456d2859, 0xa84b, 0x4e47, (0xa2, 0xee, 0x32, 0x76, 0xd8, 0x86, 0x99, 0x7d ))

SxS0                = 1
SxS1                = 2
SxS2                = 3
SxS3                = 4
SxS4                = 5
SxS5                = 6
EfiMaximumSleepType = 7
EFI_SLEEP_TYPE      = ENUM

SxEntry         = 1
SxExit          = 2
EfiMaximumPhase = 3
EFI_SLEEP_PHASE = ENUM

class EFI_MM_SX_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Type",    EFI_SLEEP_TYPE),
    ("Phase",   EFI_SLEEP_PHASE)
  ]

class EFI_MM_SX_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_SX_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SX_DISPATCH_PROTOCOL),     #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,               #   IN        DispatchFunction,
  POINTER(EFI_MM_SX_REGISTER_CONTEXT),      #   IN  CONST *RegisterContext,
  POINTER(EFI_HANDLE)                       #   OUT       *DispatchHandle
  )

EFI_MM_SX_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SX_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_HANDLE                            #   IN       DispatchHandle
  )

EFI_MM_SX_DISPATCH_PROTOCOL._fields_ = [
    ("Register",    EFI_MM_SX_REGISTER),
    ("UnRegister",  EFI_MM_SX_UNREGISTER)
  ]

