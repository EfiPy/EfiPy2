# SmBus.py
#
# EfiPy2.MdePkg.IndustryStandard.SmBus
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class EFI_SMBUS_UDID (Structure):
  _fields_ = [
    ("VendorSpecificId",    UINT32),
    ("SubsystemDeviceId",   UINT16),
    ("SubsystemVendorId",   UINT16),
    ("Interface",           UINT16),
    ("DeviceId",            UINT16),
    ("VendorId",            UINT16),
    ("VendorRevision",      UINT8),
    ("DeviceCapabilities",  UINT8),
  ]

class EFI_SMBUS_DEVICE_ADDRESS (Structure):
  _fields_ = [
    ("SmbusDeviceAddress",    UINTN, 7)
  ]

class EFI_SMBUS_DEVICE_MAP (Structure):
  _fields_ = [
    ("SmbusDeviceAddress",  EFI_SMBUS_DEVICE_ADDRESS),
    ("SmbusDeviceUdid",     EFI_SMBUS_UDID)
  ]

EfiSmbusQuickRead       =  0
EfiSmbusQuickWrite      =  1
EfiSmbusReceiveByte     =  2
EfiSmbusSendByte        =  3
EfiSmbusReadByte        =  4
EfiSmbusWriteByte       =  5
EfiSmbusReadWord        =  6
EfiSmbusWriteWord       =  7
EfiSmbusReadBlock       =  8
EfiSmbusWriteBlock      =  9
EfiSmbusProcessCall     = 10
EfiSmbusBWBRProcessCall = 11
EFI_SMBUS_OPERATION = ENUM

EFI_SMBUS_DEVICE_COMMAND = UINTN

EFI_SMBUS_DEVICE_COMMAND = UINTN
