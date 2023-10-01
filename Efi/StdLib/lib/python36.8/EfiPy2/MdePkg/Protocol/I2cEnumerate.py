# I2cEnumerate.py
#
# EfiPy2.MdePkg.Protocol.I2cEnumerate
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiI2c import EFI_I2C_DEVICE

gEfiI2cEnumerateProtocolGuid  = \
  EFI_GUID (0xda8cd7c4, 0x1c00, 0x49e2, ( 0x80, 0x3e, 0x52, 0x14, 0xe7, 0x01, 0x89, 0x4c ))

class EFI_I2C_ENUMERATE_PROTOCOL (Structure):
  pass

EFI_I2C_ENUMERATE_PROTOCOL_ENUMERATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_ENUMERATE_PROTOCOL),  # IN CONST  *This
  POINTER(POINTER(EFI_I2C_DEVICE))      # IN OUT    **Device
  )

EFI_I2C_ENUMERATE_PROTOCOL_GET_BUS_FREQUENCY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_ENUMERATE_PROTOCOL),  # IN CONST  *This
  UINTN,                                # IN        I2cBusConfiguration
  POINTER(UINTN)                        #    OUT    *BusClockHertz
  )

EFI_I2C_ENUMERATE_PROTOCOL._fields_ = [
  ("Enumerate",       EFI_I2C_ENUMERATE_PROTOCOL_ENUMERATE),
  ("GetBusFrequency", EFI_I2C_ENUMERATE_PROTOCOL_GET_BUS_FREQUENCY)
  ]

