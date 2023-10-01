# PciHotPlugRequest.py
#
# EfiPy2.MdePkg.Protocol.PciHotPlugRequest
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPciHotPlugRequestProtocolGuid   = \
  EFI_GUID (0x19cb87ab, 0x2cb9, 0x4665, (0x83, 0x60, 0xdd, 0xcf, 0x60, 0x54, 0xf7, 0x9d))

class EFI_PCI_HOTPLUG_REQUEST_PROTOCOL (Structure):
  pass

EfiPciHotPlugRequestAdd     = 0
EfiPciHotplugRequestRemove  = 1
EFI_PCI_HOTPLUG_OPERATION   = ENUM

EFI_PCI_HOTPLUG_REQUEST_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOTPLUG_REQUEST_PROTOCOL),  # IN  *This,
  EFI_PCI_HOTPLUG_OPERATION,                  # IN     Operation,
  EFI_HANDLE,                                 # IN     Controller,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),          # IN     *RemainingDevicePath  OPTIONAL,
  POINTER(UINT8),                             # IN OUT *NumberOfChildren,
  POINTER(EFI_HANDLE)                         # IN OUT *ChildHandleBuffer
  )

EFI_PCI_HOTPLUG_REQUEST_PROTOCOL._fields_ = [
    ("Notify",  EFI_PCI_HOTPLUG_REQUEST_NOTIFY)
  ]

