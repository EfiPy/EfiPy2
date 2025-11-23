# DriverFamilyOverride.py
#
# EfiPy2.MdePkg.Protocol.DriverFamilyOverride
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDriverFamilyOverrideProtocolGuid    = \
  EFI_GUID (0xb1ee129e, 0xda36, 0x4181, ( 0x91, 0xf8, 0x4, 0xa4, 0x92, 0x37, 0x66, 0xa7 ))

class EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_DRIVER_FAMILY_OVERRIDE_GET_VERSION = CFUNCTYPE (
  UINT32,
  POINTER(EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL)  # IN  *This
  )

EFI_DRIVER_FAMILY_OVERRIDE_PROTOCOL._fields_ = [
    ("GetVersion",  EFI_DRIVER_FAMILY_OVERRIDE_GET_VERSION)
  ]

