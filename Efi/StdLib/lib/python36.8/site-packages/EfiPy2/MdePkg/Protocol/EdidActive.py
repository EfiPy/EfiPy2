# EdidActive.py
#
# EfiPy2.MdePkg.Protocol.EdidActive
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiEdidActiveProtocolGuid    = \
  EFI_GUID (0xbd8c1056, 0x9f36, 0x44ec, (0x92, 0xa8, 0xa6, 0x33, 0x7f, 0x81, 0x79, 0x86 ))

class EFI_EDID_ACTIVE_PROTOCOL (Structure):
  _fields_ = [
    ("SizeOfEdid",  UINT32),
    ("Edid",        POINTER(UINT8))
  ]

