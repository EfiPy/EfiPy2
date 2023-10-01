# I2cHost.py
#
# EfiPy2.MdePkg.Protocol.I2cHost
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi import PiI2c

gEfiI2cHostProtocolGuid =   \
  EFI_GUID (0xa5aab9e3, 0xc727, 0x48cd, ( 0x8b, 0xbf, 0x42, 0x72, 0x33, 0x85, 0x49, 0x48 ))

class EFI_I2C_HOST_PROTOCOL (Structure):
  pass

EFI_I2C_HOST_PROTOCOL_QUEUE_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_HOST_PROTOCOL),         # IN CONST  *This
  UINTN,                                  # IN        I2cBusConfiguration,
  UINTN,                                  # IN        SlaveAddress,
  EFI_EVENT,                              # IN        Event      OPTIONAL,
  POINTER(PiI2c.EFI_I2C_REQUEST_PACKET),  # IN        *RequestPacket,
  POINTER(EFI_STATUS)                     # OUT       *I2cStatus OPTIONAL
  )

EFI_I2C_HOST_PROTOCOL._fields_ = [
    ("QueueRequest",              EFI_I2C_HOST_PROTOCOL_QUEUE_REQUEST),
    ("I2cControllerCapabilities", POINTER(PiI2c.EFI_I2C_CONTROLLER_CAPABILITIES))
  ]

