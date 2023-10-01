# MmBase.py
#
# EfiPy2.MdePkg.Protocol.MmBase
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis import EFI_MM_SYSTEM_TABLE

gEfiMmBaseProtocolGuid = \
  EFI_GUID (0xf4ccbfb7, 0xf6e0, 0x47fd, (0x9d, 0xd4, 0x10, 0xa8, 0xf1, 0x50, 0xc1, 0x91 ))

class EFI_MM_BASE_PROTOCOL (Structure):
  pass

EFI_MM_INSIDE_OUT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_BASE_PROTOCOL),    # IN    *This,
  POINTER(BOOLEAN)                  # OUT   *InMmram
  )

EFI_MM_GET_MMST_LOCATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_BASE_PROTOCOL),    # IN     *This,
  POINTER(EFI_MM_SYSTEM_TABLE)      # IN OUT *Mmst
  )

EFI_MM_BASE_PROTOCOL._fields_ = [
    ("InMm",            EFI_MM_INSIDE_OUT),
    ("GetMmstLocation", EFI_MM_GET_MMST_LOCATION)
  ]

