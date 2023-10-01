# ComponentName2.py
#
# EfiPy2.MdePkg.Protocol.ComponentName2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiComponentName2ProtocolGuid          = \
  EFI_GUID (0x6a7a5cff, 0xe8d9, 0x4f70, ( 0xba, 0xda, 0x75, 0xab, 0x30, 0x25, 0xce, 0x14 ))

class EFI_COMPONENT_NAME2_PROTOCOL (Structure):
  pass

EFI_COMPONENT_NAME2_GET_DRIVER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME2_PROTOCOL),  # IN *This
  PCHAR8,                                 # IN *Language
  POINTER (PCHAR16)                       # IN **DriverName
  )

EFI_COMPONENT_NAME2_GET_CONTROLLER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME2_PROTOCOL),  # IN *This
  EFI_HANDLE,                             # IN  ControllerHandle,
  EFI_HANDLE,                             # IN  ChildHandle        OPTIONAL,
  PCHAR8,                                 # IN *Language
  POINTER (PCHAR16)                       # IN **ControllerName
  )

EFI_COMPONENT_NAME2_PROTOCOL._fields_ = [
    ("GetDriverName",       EFI_COMPONENT_NAME2_GET_DRIVER_NAME),
    ("GetControllerName",   EFI_COMPONENT_NAME2_GET_CONTROLLER_NAME),
    ("SupportedLanguages",  PCHAR8)
  ]

