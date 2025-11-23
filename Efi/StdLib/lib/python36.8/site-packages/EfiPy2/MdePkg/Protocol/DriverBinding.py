# DriverBinding.py
#
# EfiPy2.MdePkg.Protocol.DriverBinding
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDriverBindingProtocolGuid           = \
  EFI_GUID (0x18a031ab, 0xb443, 0x4d1a, (0xa5, 0xc0, 0xc, 0x9, 0x26, 0x1e, 0x9f, 0x71 ))

class EFI_DRIVER_BINDING_PROTOCOL (Structure):
  pass

EFI_DRIVER_BINDING_SUPPORTED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_BINDING_PROTOCOL), # IN  *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN  *RemainingDevicePath OPTIONAL
  )

EFI_DRIVER_BINDING_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_BINDING_PROTOCOL), # IN  *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     # IN  *RemainingDevicePath OPTIONAL
  )

EFI_DRIVER_BINDING_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_BINDING_PROTOCOL), # IN  *This
  EFI_HANDLE,                           # IN  ControllerHandle,
  UINTN,                                # IN  NumberOfChildren,
  POINTER(EFI_HANDLE)                   # IN  *ChildHandleBuffer OPTIONAL
  )

EFI_DRIVER_BINDING_PROTOCOL._fields_ = [
    ("Supported",           EFI_DRIVER_BINDING_SUPPORTED),
    ("Start",               EFI_DRIVER_BINDING_START),
    ("Stop",                EFI_DRIVER_BINDING_STOP),
    ("Version",             UINT32),
    ("ImageHandle",         EFI_HANDLE),
    ("DriverBindingHandle", EFI_HANDLE)
  ]

