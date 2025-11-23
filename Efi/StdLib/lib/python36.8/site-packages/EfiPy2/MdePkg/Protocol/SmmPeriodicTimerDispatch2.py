# SmmPeriodicTimerDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmPeriodicTimerDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiSmmCis  import EFI_SMM_HANDLER_ENTRY_POINT2
from EfiPy2.MdePkg.Protocol.MmPeriodicTimerDispatch import                      \
                                    gEfiMmPeriodicTimerDispatchProtocolGuid,    \
                                    EFI_MM_PERIODIC_TIMER_CONTEXT

gEfiSmmPeriodicTimerDispatch2ProtocolGuid = gEfiMmPeriodicTimerDispatchProtocolGuid

class EFI_SMM_PERIODIC_TIMER_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Period",          UINT64),
    ("SmiTickInterval", UINT64)
  ]

EFI_SMM_PERIODIC_TIMER_CONTEXT = EFI_MM_PERIODIC_TIMER_CONTEXT

class EFI_SMM_PERIODIC_TIMER_DISPATCH2_PROTOCOL (Structure):
  pass

EFI_SMM_PERIODIC_TIMER_REGISTER2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_PERIODIC_TIMER_DISPATCH2_PROTOCOL),   #   IN       *This
  EFI_SMM_HANDLER_ENTRY_POINT2,                         #   IN       DispatchFunction,
  POINTER(EFI_SMM_PERIODIC_TIMER_REGISTER_CONTEXT),     #   IN CONST *RegisterContext,
  POINTER(EFI_HANDLE)                                   #   OUT      *DispatchHandle
  )

EFI_SMM_PERIODIC_TIMER_UNREGISTER2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_PERIODIC_TIMER_DISPATCH2_PROTOCOL),   #   IN       *This
  EFI_HANDLE                                            #   IN       DispatchHandle
  )

EFI_SMM_PERIODIC_TIMER_INTERVAL2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_PERIODIC_TIMER_DISPATCH2_PROTOCOL),   #   IN       *This
  POINTER(POINTER(UINT64))                              #   IN OUT   **SmiTickInterval
  )

EFI_SMM_PERIODIC_TIMER_DISPATCH2_PROTOCOL._fields_ = [
    ("Register",                EFI_SMM_PERIODIC_TIMER_REGISTER2),
    ("UnRegister",              EFI_SMM_PERIODIC_TIMER_UNREGISTER2),
    ("GetNextShorterInterval",  EFI_SMM_PERIODIC_TIMER_INTERVAL2)
  ]

