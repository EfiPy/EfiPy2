# MmStandbyButtonDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmStandbyButtonDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmStandbyButtonDispatchProtocolGuid = \
  EFI_GUID (0x7300c4a1, 0x43f2, 0x4017, (0xa5, 0x1b, 0xc8, 0x1a, 0x7f, 0x40, 0x58, 0x5b ))

EfiStandbyButtonEntry       = 1
EfiStandbyButtonExit        = 2
EfiStandbyButtonMax         = 3
EFI_STANDBY_BUTTON_PHASE    = ENUM

class EFI_MM_STANDBY_BUTTON_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Phase",   EFI_STANDBY_BUTTON_PHASE)
  ]

class EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_STANDBY_BUTTON_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,                       #   IN       DispatchFunction,
  POINTER(EFI_MM_STANDBY_BUTTON_REGISTER_CONTEXT),  #   IN       *RegisterContext,
  POINTER(EFI_HANDLE)                               #   OUT      *DispatchHandle
  )

EFI_MM_STANDBY_BUTTON_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_HANDLE                                        #   IN       DispatchHandle
  )

EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL._fields_ = [
    ("Register",                EFI_MM_STANDBY_BUTTON_REGISTER),
    ("UnRegister",              EFI_MM_STANDBY_BUTTON_UNREGISTER)
  ]

