# I2cMaster.py
#
# EfiPy2.MdePkg.Protocol.I2cMaster
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi import PiI2c

gEfiI2cMasterProtocolGuid   = \
  EFI_GUID (0xcd72881f, 0x45b5, 0x4feb, ( 0x98, 0xc8, 0x31, 0x3d, 0xa8, 0x11, 0x74, 0x62 ))

class EFI_I2C_MASTER_PROTOCOL (Structure):
  pass

EFI_I2C_MASTER_PROTOCOL_SET_BUS_FREQUENCY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_MASTER_PROTOCOL), # IN CONST *This
  POINTER(UINTN)                    # IN OUT   *BusClockHertz
  )

EFI_I2C_MASTER_PROTOCOL_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_MASTER_PROTOCOL)  # IN CONST *This
  )

EFI_I2C_MASTER_PROTOCOL_START_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_MASTER_PROTOCOL),       # IN CONST  *This
  UINTN,                                  # IN        SlaveAddress,
  POINTER(PiI2c.EFI_I2C_REQUEST_PACKET),  # IN        *RequestPacket,
  EFI_EVENT,                              # IN        Event      OPTIONAL,
  POINTER(EFI_STATUS)                     # OUT       *I2cStatus OPTIONAL
  )

EFI_I2C_MASTER_PROTOCOL._fields_ = [
    ("SetBusFrequency",           EFI_I2C_MASTER_PROTOCOL_SET_BUS_FREQUENCY),
    ("Reset",                     EFI_I2C_MASTER_PROTOCOL_RESET),
    ("StartRequest",              EFI_I2C_MASTER_PROTOCOL_START_REQUEST),
    ("I2cControllerCapabilities", POINTER(PiI2c.EFI_I2C_CONTROLLER_CAPABILITIES))
  ]

