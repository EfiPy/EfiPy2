# WatchdogTimer.py
#
# EfiPy2.MdePkg.Protocol.WatchdogTimer
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiWatchdogTimerArchProtocolGuid = \
  EFI_GUID (0x665E3FF5, 0x46CC, 0x11d4, (0x9A, 0x38, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_WATCHDOG_TIMER_ARCH_PROTOCOL (Structure):
  pass

EFI_WATCHDOG_TIMER_NOTIFY = CFUNCTYPE (
  VOID,
  UINT64  # IN  Time
  )

EFI_WATCHDOG_TIMER_REGISTER_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WATCHDOG_TIMER_ARCH_PROTOCOL),  # IN  *This
  EFI_WATCHDOG_TIMER_NOTIFY                   # IN  NotifyFunction
  )

EFI_WATCHDOG_TIMER_SET_TIMER_PERIOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WATCHDOG_TIMER_ARCH_PROTOCOL),  # IN  *This
  UINT64                                      # IN  TimerPeriod
  )

EFI_WATCHDOG_TIMER_GET_TIMER_PERIOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WATCHDOG_TIMER_ARCH_PROTOCOL),  # IN  *This,
  POINTER(UINT64)                             # OUT 8TimerPeriod
  )

EFI_WATCHDOG_TIMER_ARCH_PROTOCOL._fields_ = [
    ("RegisterHandler", EFI_WATCHDOG_TIMER_REGISTER_HANDLER),
    ("SetTimerPeriod",  EFI_WATCHDOG_TIMER_SET_TIMER_PERIOD),
    ("GetTimerPeriod",  EFI_WATCHDOG_TIMER_GET_TIMER_PERIOD)
  ]

