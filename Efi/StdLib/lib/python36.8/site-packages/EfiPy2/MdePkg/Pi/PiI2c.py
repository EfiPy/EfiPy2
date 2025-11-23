# PiI2c.py
#
# EfiPy2.MdePkg.Pi.PiI2c
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

I2C_ADDRESSING_10_BIT     = 0x80000000

class EFI_I2C_CONTROLLER_CAPABILITIES (Structure):
  _fields_ = [
    ("StructureSizeInBytes",  UINT32),
    ("MaximumReceiveBytes",   UINT32),
    ("MaximumTransmitBytes",  UINT32),
    ("MaximumTotalBytes",     UINT32)
  ]

class EFI_I2C_DEVICE (Structure):
  _fields_ = [
    ("DeviceGuid",          POINTER(EFI_GUID)),
    ("DeviceIndex",         UINT32),
    ("HardwareRevision",    UINT32),
    ("I2cBusConfiguration", UINT32),
    ("SlaveAddressCount",   UINT32),
    ("SlaveAddressArray",   POINTER(UINT32))
  ]

I2C_FLAG_READ               = 0x00000001

I2C_FLAG_SMBUS_OPERATION  = 0x00010000

I2C_FLAG_SMBUS_BLOCK  = 0x00020000

I2C_FLAG_SMBUS_PROCESS_CALL  = 0x00040000

I2C_FLAG_SMBUS_PEC  = 0x00080000

class EFI_I2C_OPERATION (Structure):
  _fields_ = [
    ("Flags",         UINT32),
    ("LengthInBytes", UINT32),
    ("Buffer",        POINTER(UINT8))
  ]

class EFI_I2C_REQUEST_PACKET (Structure):
  _fields_ = [
    ("OperationCount",  UINTN),
    ("Operation",       EFI_I2C_OPERATION * 1)
  ]

