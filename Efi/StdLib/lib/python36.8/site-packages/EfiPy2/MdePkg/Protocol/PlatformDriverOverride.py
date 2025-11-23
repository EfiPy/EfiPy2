# PlatformDriverOverride.py
#
# EfiPy2.MdePkg.Protocol.PlatformDriverOverride
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPlatformDriverOverrideProtocolGuid  = \
  EFI_GUID (0x6b30c738, 0xa391, 0x11d4, (0x9a, 0x3b, 0x00, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL), # IN *This
  EFI_HANDLE,                                     # IN ControllerHandle
  POINTER(EFI_HANDLE)                             # IN OUT
  )

EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL), # IN *This
  EFI_HANDLE,                                     # IN ControllerHandle
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))      # IN OUT **DriverImagePath
  )

EFI_PLATFORM_DRIVER_OVERRIDE_DRIVER_LOADED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL), # IN *This
  EFI_HANDLE,                                     # IN ControllerHandle
  POINTER(EFI_DEVICE_PATH_PROTOCOL),              # IN *DriverImagePath,
  EFI_HANDLE                                      # IN DriverImagePath
  )

EFI_PLATFORM_DRIVER_OVERRIDE_PROTOCOL._fields_ = [
    ("GetDriver",     EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER),
    ("GetDriverPath", EFI_PLATFORM_DRIVER_OVERRIDE_GET_DRIVER_PATH),
    ("DriverLoaded",  EFI_PLATFORM_DRIVER_OVERRIDE_DRIVER_LOADED)
  ]

