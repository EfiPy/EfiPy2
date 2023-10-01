# MmPeriodicTimerDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmPeriodicTimerDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmPeriodicTimerDispatchProtocolGuid = \
  EFI_GUID (0x4cec368e, 0x8e8e, 0x4d71, (0x8b, 0xe1, 0x95, 0x8c, 0x45, 0xfc, 0x8a, 0x53 ))

class EFI_MM_PERIODIC_TIMER_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Period",          UINT64),
    ("MmiTickInterval", UINT64)
  ]

class EFI_MM_PERIODIC_TIMER_CONTEXT (Structure):
  _fields_ = [
    ("ElapsedTime", UINT64)
  ]

class EFI_MM_PERIODIC_TIMER_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_PERIODIC_TIMER_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_PERIODIC_TIMER_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,                       #   IN       DispatchFunction,
  POINTER(EFI_MM_PERIODIC_TIMER_REGISTER_CONTEXT),  #   IN CONST *RegisterContext,
  POINTER(EFI_HANDLE)                               #   OUT      *DispatchHandle
  )

EFI_MM_PERIODIC_TIMER_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_PERIODIC_TIMER_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_HANDLE                                        #   IN       DispatchHandle
  )

EFI_MM_PERIODIC_TIMER_INTERVAL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_PERIODIC_TIMER_DISPATCH_PROTOCOL), #   IN CONST *This
  POINTER(POINTER(UINT64))                          #   IN OUT   **MmiTickInterval
  )

EFI_MM_PERIODIC_TIMER_DISPATCH_PROTOCOL._fields_ = [
    ("Register",                EFI_MM_PERIODIC_TIMER_REGISTER),
    ("UnRegister",              EFI_MM_PERIODIC_TIMER_UNREGISTER),
    ("GetNextShorterInterval",  EFI_MM_PERIODIC_TIMER_INTERVAL)
  ]

