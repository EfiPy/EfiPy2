# LegacySpiSmmFlash.py
#
# EfiPy2.MdePkg.Protocol.LegacySpiSmmFlash
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.LegacySpiFlash import EFI_LEGACY_SPI_FLASH_PROTOCOL

gEfiLegacySpiSmmFlashProtocolGuid = \
  EFI_GUID (0x5e3848d4, 0x0db5, 0x4fc0, (0x97, 0x29, 0x3f, 0x35, 0x3d, 0x4f, 0x87, 0x9f ))

EFI_LEGACY_SPI_SMM_FLASH_PROTOCOL = EFI_LEGACY_SPI_FLASH_PROTOCOL

