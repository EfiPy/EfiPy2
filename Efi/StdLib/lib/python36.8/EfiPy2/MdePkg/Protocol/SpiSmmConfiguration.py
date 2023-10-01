# SpiSmmConfiguration.py
#
# EfiPy2.MdePkg.Protocol.SpiSmmConfiguration
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.SpiConfiguration import EFI_SPI_CONFIGURATION_PROTOCOL

gEfiSpiSmmConfigurationProtocolGuid = \
  EFI_GUID (0x995c6eca, 0x171b, 0x45fd, (0xa3, 0xaa, 0xfd, 0x4c, 0x9c, 0x9d, 0xef, 0x59 ))

EFI_SPI_SMM_CONFIGURATION_PROTOCOL = EFI_SPI_CONFIGURATION_PROTOCOL

