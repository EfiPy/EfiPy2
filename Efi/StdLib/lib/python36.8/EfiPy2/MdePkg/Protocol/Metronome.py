# Metronome.py
#
# EfiPy2.MdePkg.Protocol.Metronome
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMetronomeArchProtocolGuid = \
  EFI_GUID (0x26baccb2, 0x6f42, 0x11d4, (0xbc, 0xe7, 0x0, 0x80, 0xc7, 0x3c, 0x88, 0x81 ))

class EFI_METRONOME_ARCH_PROTOCOL (Structure):
  pass

EFI_METRONOME_WAIT_FOR_TICK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_METRONOME_ARCH_PROTOCOL), # IN *This
  UINT32                                # IN TickNumber
  )

EFI_METRONOME_ARCH_PROTOCOL._fields_ = [
  ("WaitForTick", EFI_METRONOME_WAIT_FOR_TICK),
  ("TickPeriod",  UINT32)
  ]

