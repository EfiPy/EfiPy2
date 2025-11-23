# ComponentName.py
#
# EfiPy2.MdePkg.Protocol.ComponentName
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiComponentNameProtocolGuid           = \
  EFI_GUID (0x107a772c, 0xd5e1, 0x11d4, (0x9a, 0x46, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_COMPONENT_NAME_PROTOCOL (Structure):
  pass

EFI_COMPONENT_NAME_GET_DRIVER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME_PROTOCOL), # IN *This
  PCHAR8,                               # IN *Language
  POINTER (PCHAR16)                     # IN **DriverName
  )

EFI_COMPONENT_NAME_GET_CONTROLLER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_COMPONENT_NAME_PROTOCOL), # IN *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  EFI_HANDLE,                           # IN  ChildHandle        OPTIONAL,
  PCHAR8,                               # IN *Language
  POINTER (PCHAR16)                     # IN **ControllerName
  )

EFI_COMPONENT_NAME_PROTOCOL._fields_ = [
    ("GetDriverName",       EFI_COMPONENT_NAME_GET_DRIVER_NAME),
    ("GetControllerName",   EFI_COMPONENT_NAME_GET_CONTROLLER_NAME),
    ("SupportedLanguages",  PCHAR8)
  ]

