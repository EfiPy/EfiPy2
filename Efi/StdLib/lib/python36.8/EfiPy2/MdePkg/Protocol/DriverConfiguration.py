# DriverConfiguration.py
#
# EfiPy2.MdePkg.Protocol.DriverConfiguration
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import DriverConfiguration2

gEfiDriverConfigurationProtocolGuid     = \
  EFI_GUID (0x107a772b, 0xd5e1, 0x11d4, (0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_DRIVER_CONFIGURATION_PROTOCOL (Structure):
  pass

EFI_DRIVER_CONFIGURATION_SET_OPTIONS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION_PROTOCOL),       # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE,                                       # IN  ChildHandle  OPTIONAL,
  PCHAR8,                                           # IN  *Language,
  POINTER(DriverConfiguration2.EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED) # OUT *ActionRequired
  )

EFI_DRIVER_CONFIGURATION_OPTIONS_VALID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION_PROTOCOL),       # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE                                        # IN  ChildHandle  OPTIONAL,
  )

EFI_DRIVER_CONFIGURATION_FORCE_DEFAULTS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION_PROTOCOL),       # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE,                                       # IN  ChildHandle  OPTIONAL,
  UINT32,                                           # IN  DefaultType,
  POINTER(DriverConfiguration2.EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED) # OUT *ActionRequired
  )

EFI_DRIVER_CONFIGURATION_PROTOCOL._fields_ = [
    ("SetOptions",          EFI_DRIVER_CONFIGURATION_SET_OPTIONS),
    ("OptionsValid",        EFI_DRIVER_CONFIGURATION_OPTIONS_VALID),
    ("ForceDefaults",       EFI_DRIVER_CONFIGURATION_FORCE_DEFAULTS),
    ("SupportedLanguages",  PCHAR8)
  ]

