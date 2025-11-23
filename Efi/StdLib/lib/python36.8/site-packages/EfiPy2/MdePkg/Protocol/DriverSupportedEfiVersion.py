# DriverSupportedEfiVersion.py
#
# EfiPy2.MdePkg.Protocol.DriverSupportedEfiVersion
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDriverSupportedEfiVersionProtocolGuid = \
  EFI_GUID (0x5c198761, 0x16a8, 0x4e69, ( 0x97, 0x2c, 0x89, 0xd6, 0x79, 0x54, 0xf8, 0x1d ))

class EFI_DRIVER_SUPPORTED_EFI_VERSION_PROTOCOL (Structure):
  _fields_ = [
    ("Length",          UINT32),
    ("FirmwareVersion", UINT32)
  ]

