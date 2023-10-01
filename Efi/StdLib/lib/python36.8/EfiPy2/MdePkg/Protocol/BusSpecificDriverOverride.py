# BusSpecificDriverOverride.py
#
# EfiPy2.MdePkg.Protocol.BusSpecificDriverOverride
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiBusSpecificDriverOverrideProtocolGuid = \
  EFI_GUID (0x3bc1b285, 0x8a15, 0x4a82, (0xaa, 0xbf, 0x4d, 0x7d, 0x13, 0xfb, 0x32, 0x65 ))

class EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_GET_DRIVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL),   # IN     *This
  POINTER(EFI_HANDLE)                                   # IN OUT *DriverImageHandle
  )

EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_PROTOCOL._fields_ = [
    ("GetDriver", EFI_BUS_SPECIFIC_DRIVER_OVERRIDE_GET_DRIVER)
  ]

