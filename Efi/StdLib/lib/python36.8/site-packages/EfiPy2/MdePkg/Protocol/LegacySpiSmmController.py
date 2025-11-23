# LegacySpiSmmController.py
#
# EfiPy2.MdePkg.Protocol.LegacySpiSmmController
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.LegacySpiController import EFI_LEGACY_SPI_CONTROLLER_PROTOCOL

gEfiLegacySpiSmmControllerProtocolGuid = \
  EFI_GUID (0x62331b78, 0xd8d0, 0x4c8c, (0x8c, 0xcb, 0xd2, 0x7d, 0xfe, 0x32, 0xdb, 0x9b ))

EFI_LEGACY_SPI_SMM_CONTROLLER_PROTOCOL = EFI_LEGACY_SPI_CONTROLLER_PROTOCOL
