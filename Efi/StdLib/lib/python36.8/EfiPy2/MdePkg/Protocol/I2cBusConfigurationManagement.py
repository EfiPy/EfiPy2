# I2cBusConfigurationManagement.py
#
# EfiPy2.MdePkg.Protocol.I2cBusConfigurationManagement
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiI2cBusConfigurationManagementProtocolGuid = \
  EFI_GUID (0x55b71fb5, 0x17c6, 0x410e, ( 0xb5, 0xbd, 0x5f, 0xa2, 0xe3, 0xd4, 0x46, 0x6b ))

class EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL (Structure):
  pass

EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL_ENABLE_I2C_BUS_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL), # IN *This
  UINTN,                                                  # IN I2cBusConfiguration,
  EFI_EVENT,                                              # IN Event      OPTIONAL,
  POINTER(EFI_STATUS)                                     # IN *I2cStatus OPTIONAL
  )

EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL._fields_ = [
  ("EnableI2cBusConfiguration", EFI_I2C_BUS_CONFIGURATION_MANAGEMENT_PROTOCOL_ENABLE_I2C_BUS_CONFIGURATION)
  ]

