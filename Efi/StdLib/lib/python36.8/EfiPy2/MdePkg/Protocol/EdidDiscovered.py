# EdidDiscovered.py
#
# EfiPy2.MdePkg.Protocol.EdidDiscovered
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiEdidDiscoveredProtocolGuid  = \
  EFI_GUID (0x1c0c34f6, 0xd380, 0x41fa, (0xa0, 0x49, 0x8a, 0xd0, 0x6c, 0x1a, 0x66, 0xaa ))

class EFI_EDID_DISCOVERED_PROTOCOL (Structure):
  _fields_ = [
    ("SizeOfEdid",  UINT32),
    ("Edid",        POINTER(UINT8))
  ]

