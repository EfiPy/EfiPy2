# MmUsbDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmUsbDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

gEfiMmUsbDispatchProtocolGuid = \
  EFI_GUID (0xee9b8d90, 0xc5a6, 0x40a2, (0xbd, 0xe2, 0x52, 0x55, 0x8d, 0x33, 0xcc, 0xa1 ))

UsbLegacy           = 1
UsbWake             = 2
EFI_USB_MMI_TYPE    = ENUM

class EFI_MM_USB_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Type",    EFI_USB_MMI_TYPE),
    ("Device",  POINTER(EFI_DEVICE_PATH_PROTOCOL))
  ]

class EFI_MM_USB_DISPATCH_PROTOCOL (Structure):
  pass

EFI_MM_USB_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_USB_DISPATCH_PROTOCOL),    #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,               #   IN        DispatchFunction,
  POINTER(EFI_MM_USB_REGISTER_CONTEXT),     #   IN  CONST *RegisterContext,
  POINTER(EFI_HANDLE)                       #   OUT       *DispatchHandle
  )

EFI_MM_USB_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_USB_DISPATCH_PROTOCOL),    #   IN CONST *This
  EFI_HANDLE                                #   IN       DispatchHandle
  )

EFI_MM_USB_DISPATCH_PROTOCOL._fields_ = [
    ("Register",    EFI_MM_USB_REGISTER),
    ("UnRegister",  EFI_MM_USB_UNREGISTER)
  ]

