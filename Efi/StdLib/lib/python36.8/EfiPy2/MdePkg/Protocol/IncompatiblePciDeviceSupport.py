# IncompatiblePciDeviceSupport.py
#
# EfiPy2.MdePkg.Protocol.IncompatiblePciDeviceSupport
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiIncompatiblePciDeviceSupportProtocolGuid  = \
  EFI_GUID (0xeb23f55a, 0x7863, 0x4ac2, (0x8d, 0x3d, 0x95, 0x65, 0x35, 0xde, 0x03, 0x75))

class EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_PROTOCOL (Structure):
  pass

EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_CHECK_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_PROTOCOL),  # IN  *This
  UINTN,                                                  # IN  VendorId,
  UINTN,                                                  # IN  DeviceId,
  UINTN,                                                  # IN  RevisionId,
  UINTN,                                                  # IN  SubsystemVendorId,
  UINTN,                                                  # IN  SubsystemDeviceId,
  POINTER(PVOID)                                          # OUT **Configuration
  )

EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_PROTOCOL._fields_ = [
    ("CheckDevice", EFI_INCOMPATIBLE_PCI_DEVICE_SUPPORT_CHECK_DEVICE)
  ]

