# LegacySpiController.py
#
# EfiPy2.MdePkg.Protocol.LegacySpiController
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiLegacySpiControllerProtocolGuid = \
  EFI_GUID (0x39136fc7, 0x1a11, 0x49de, (0xbf, 0x35, 0x0e, 0x78, 0xdd, 0xb5, 0x24, 0xfc ))

class EFI_LEGACY_SPI_CONTROLLER_PROTOCOL (Structure):
  pass

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_ERASE_BLOCK_OPCODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL),  # IN *This
  UINT8                                         # IN EraseBlockOpcode
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_WRITE_STATUS_PREFIX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL),  # IN *This
  UINT8                                         # IN WriteStatusPrefix
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_BIOS_BASE_ADDRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL),  # IN *This
  UINT32                                        # IN BiosBaseAddress
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_CLEAR_SPI_PROTECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL)   # IN *This
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_IS_RANGE_PROTECTED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL),  # IN *This
  UINT32,                                       # IN BiosAddress
  UINT32                                        # IN BlocksToProtect
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_PROTECT_NEXT_RANGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL),  # IN *This
  UINT32,                                       # IN BiosAddress
  UINT32                                        # IN BlocksToProtect
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_LOCK_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL)   # IN *This
  )

EFI_LEGACY_SPI_CONTROLLER_PROTOCOL._fields_ = [
    ("MaximumOffset",       UINT32),
    ("MaximumRangeBytes",   UINT32),
    ("RangeRegisterCount",  UINT32),
    ("EraseBlockOpcode",    EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_ERASE_BLOCK_OPCODE),
    ("WriteStatusPrefix",   EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_WRITE_STATUS_PREFIX),
    ("BiosBaseAddress",     EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_BIOS_BASE_ADDRESS),
    ("ClearSpiProtect",     EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_CLEAR_SPI_PROTECT),
    ("IsRangeProtected",    EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_IS_RANGE_PROTECTED),
    ("ProtectNextRange",    EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_PROTECT_NEXT_RANGE),
    ("LockController",      EFI_LEGACY_SPI_CONTROLLER_PROTOCOL_LOCK_CONTROLLER)
  ]

