# Bds.py
#
# EfiPy2.MdePkg.Protocol.Bds
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiBdsArchProtocolGuid                 = \
  EFI_GUID (0x665E3FF6, 0x46CC, 0x11d4, (0x9A, 0x38, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_BDS_ARCH_PROTOCOL (Structure):
  pass

EFI_BDS_ENTRY = CFUNCTYPE (
  VOID,
  POINTER (EFI_BDS_ARCH_PROTOCOL) # IN  *This
  )

EFI_BDS_ARCH_PROTOCOL._fields_ = [
    ("Entry", EFI_BDS_ENTRY)
  ]

