# LegacySpiFlash.py
#
# EfiPy2.MdePkg.Protocol.LegacySpiFlash
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.SpiNorFlash import EFI_SPI_NOR_FLASH_PROTOCOL

gEfiLegacySpiFlashProtocolGuid = \
  EFI_GUID (0xf01bed57, 0x04bc, 0x4f3f, (0x96, 0x60, 0xd6, 0xf2, 0xea, 0x22, 0x82, 0x59 ))

class EFI_LEGACY_SPI_FLASH_PROTOCOL (Structure):
  pass

EFI_LEGACY_SPI_FLASH_PROTOCOL_BIOS_BASE_ADDRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_FLASH_PROTOCOL),   # IN *This
  UINT32                                    # IN BiosBaseAddress
  )

EFI_LEGACY_SPI_FLASH_PROTOCOL_CLEAR_SPI_PROTECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_FLASH_PROTOCOL)    # IN *This
  )

EFI_LEGACY_SPI_FLASH_PROTOCOL_IS_RANGE_PROTECTED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_FLASH_PROTOCOL),   # IN *This
  UINT32,                                   # IN BiosAddress
  UINT32                                    # IN BlocksToProtect
  )

EFI_LEGACY_SPI_FLASH_PROTOCOL_PROTECT_NEXT_RANGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_FLASH_PROTOCOL),   # IN *This
  UINT32,                                   # IN BiosAddress
  UINT32                                    # IN BlocksToProtect
  )

EFI_LEGACY_SPI_FLASH_PROTOCOL_LOCK_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_FLASH_PROTOCOL)    # IN *This
  )

EFI_LEGACY_SPI_FLASH_PROTOCOL._fields_ = [
    ("FlashProtocol",       EFI_SPI_NOR_FLASH_PROTOCOL),
    ("BiosBaseAddress",     EFI_LEGACY_SPI_FLASH_PROTOCOL_BIOS_BASE_ADDRESS),
    ("ClearSpiProtect",     EFI_LEGACY_SPI_FLASH_PROTOCOL_CLEAR_SPI_PROTECT),
    ("IsRangeProtected",    EFI_LEGACY_SPI_FLASH_PROTOCOL_IS_RANGE_PROTECTED),
    ("ProtectNextRange",    EFI_LEGACY_SPI_FLASH_PROTOCOL_PROTECT_NEXT_RANGE),
    ("LockController",      EFI_LEGACY_SPI_FLASH_PROTOCOL_LOCK_CONTROLLER)
  ]

