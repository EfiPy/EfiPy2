# I2cIo.py
#
# EfiPy2.MdePkg.Protocol.I2cIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi import PiI2c

gEfiI2cIoProtocolGuid = \
  EFI_GUID (0xb60a3e6b, 0x18c4, 0x46e5, ( 0xa2, 0x9a, 0xc9, 0xa1, 0x06, 0x65, 0xa2, 0x8e ))

class EFI_I2C_IO_PROTOCOL (Structure):
  pass

EFI_I2C_IO_PROTOCOL_QUEUE_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_IO_PROTOCOL),           # IN CONST  *This
  UINTN,                                  # IN  SlaveAddressIndex,
  EFI_EVENT,                              # IN  Event      OPTIONAL,
  POINTER(PiI2c.EFI_I2C_REQUEST_PACKET),  # IN  *RequestPacket,
  POINTER(EFI_STATUS)                     # OUT *I2cStatus OPTIONAL
  )

EFI_I2C_IO_PROTOCOL._fields_ = [
    ("QueueRequest",              EFI_I2C_IO_PROTOCOL_QUEUE_REQUEST),
    ("DeviceGuid",                POINTER(EFI_GUID)),
    ("DeviceIndex",               UINT32),
    ("HardwareRevision",          UINT32),
    ("I2cControllerCapabilities", POINTER(PiI2c.EFI_I2C_CONTROLLER_CAPABILITIES))
  ]

