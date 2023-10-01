# MmPowerButtonDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmPowerButtonDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmPowerButtonDispatchProtocolGuid = \
  EFI_GUID (0x1b1183fa, 0x1823, 0x46a7, (0x88, 0x72, 0x9c, 0x57, 0x87, 0x55, 0x40, 0x9d ))

EfiPowerButtonEntry     = 1
EfiPowerButtonExit      = 2
EfiPowerButtonMax       = 3
EFI_POWER_BUTTON_PHASE  = ENUM

class EFI_MM_POWER_BUTTON_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Phase",   EFI_POWER_BUTTON_PHASE)
  ]

class EFI_MM_POWER_BUTTON_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_POWER_BUTTON_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_POWER_BUTTON_DISPATCH_PROTOCOL),   #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,                       #   IN       DispatchFunction,
  POINTER(EFI_MM_POWER_BUTTON_REGISTER_CONTEXT),    #   IN       *RegisterContext,
  POINTER(EFI_HANDLE)                               #   OUT      *DispatchHandle
  )

EFI_MM_POWER_BUTTON_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_POWER_BUTTON_DISPATCH_PROTOCOL),   #   IN CONST *This
  EFI_HANDLE                                        #   IN       DispatchHandle
  )

EFI_MM_POWER_BUTTON_DISPATCH_PROTOCOL._fields_ = [
    ("Register",                EFI_MM_POWER_BUTTON_REGISTER),
    ("UnRegister",              EFI_MM_POWER_BUTTON_UNREGISTER)
  ]

