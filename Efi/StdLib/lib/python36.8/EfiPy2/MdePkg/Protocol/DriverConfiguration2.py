# DriverConfiguration2.py
#
# EfiPy2.MdePkg.Protocol.DriverConfiguration2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDriverConfiguration2ProtocolGuid     = \
  EFI_GUID (0xbfd7dc1d, 0x24f1, 0x40d9, (0x82, 0xe7, 0x2e, 0x09, 0xbb, 0x6b, 0x4e, 0xbe ))

class EFI_DRIVER_CONFIGURATION2_PROTOCOL (Structure):
  pass

EfiDriverConfigurationActionNone              = 0
EfiDriverConfigurationActionStopController    = 1
EfiDriverConfigurationActionRestartController = 2
EfiDriverConfigurationActionRestartPlatform   = 3
EfiDriverConfigurationActionMaximum           = 4
EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED      = ENUM

EFI_DRIVER_CONFIGURATION_SAFE_DEFAULTS          = 0x00000000
EFI_DRIVER_CONFIGURATION_MANUFACTURING_DEFAULTS = 0x00000001
EFI_DRIVER_CONFIGURATION_CUSTOM_DEFAULTS        = 0x00000002
EFI_DRIVER_CONFIGURATION_PERORMANCE_DEFAULTS    = 0x00000003

EFI_DRIVER_CONFIGURATION2_SET_OPTIONS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION2_PROTOCOL),      # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE,                                       # IN  ChildHandle  OPTIONAL,
  PCHAR8,                                           # IN  *Language,
  POINTER(EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED) # OUT *ActionRequired
  )

EFI_DRIVER_CONFIGURATION2_OPTIONS_VALID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION2_PROTOCOL),      # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE                                        # IN  ChildHandle  OPTIONAL,
  )

EFI_DRIVER_CONFIGURATION2_FORCE_DEFAULTS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_CONFIGURATION2_PROTOCOL),      # IN  *This
  EFI_HANDLE,                                       # IN  ControllerHandle,
  EFI_HANDLE,                                       # IN  ChildHandle  OPTIONAL,
  UINT32,                                           # IN  DefaultType,
  POINTER(EFI_DRIVER_CONFIGURATION_ACTION_REQUIRED) # OUT *ActionRequired
  )

EFI_DRIVER_CONFIGURATION2_PROTOCOL._fields_ = [
    ("SetOptions",          EFI_DRIVER_CONFIGURATION2_SET_OPTIONS),
    ("OptionsValid",        EFI_DRIVER_CONFIGURATION2_OPTIONS_VALID),
    ("ForceDefaults",       EFI_DRIVER_CONFIGURATION2_FORCE_DEFAULTS),
    ("SupportedLanguages",  PCHAR8)
  ]

