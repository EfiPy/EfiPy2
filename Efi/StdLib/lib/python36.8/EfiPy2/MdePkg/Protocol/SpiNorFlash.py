# SpiNorFlash.py
#
# EfiPy2.MdePkg.Protocol.SpiNorFlash
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.SpiConfiguration import EFI_SPI_PERIPHERAL

gEfiSpiNorFlashProtocolGuid = \
  EFI_GUID (0xb57ec3fe, 0xf833, 0x4ba6, (0x85, 0x78, 0x2a, 0x7d, 0x6a, 0x87, 0x44, 0x4b ))

class EFI_SPI_NOR_FLASH_PROTOCOL (Structure):
  pass

EFI_SPI_NOR_FLASH_PROTOCOL_GET_FLASH_ID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_NOR_FLASH_PROTOCOL),  #   IN  *This
  POINTER(UINT8)                        #   OUT *Buffer
  )

EFI_SPI_NOR_FLASH_PROTOCOL_READ_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_NOR_FLASH_PROTOCOL),  #   IN  *This
  UINT32,                               #   IN  FlashAddress,
  UINT32,                               #   IN  LengthInBytes,
  POINTER(UINT8)                        #   OUT *Buffer
  )

EFI_SPI_NOR_FLASH_PROTOCOL_READ_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_NOR_FLASH_PROTOCOL),  #   IN  *This
  UINT32,                               #   IN  LengthInBytes,
  POINTER(UINT8)                        #   OUT *FlashStatus
  )

EFI_SPI_NOR_FLASH_PROTOCOL_WRITE_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_NOR_FLASH_PROTOCOL),  #   IN  *This
  UINT32,                               #   IN  LengthInBytes,
  POINTER(UINT8)                        #   IN  *FlashStatus
  )

EFI_SPI_NOR_FLASH_PROTOCOL_WRITE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_NOR_FLASH_PROTOCOL),  #   IN  *This
  UINT32,                               #   IN  FlashAddress,
  UINT32,                               #   IN  LengthInBytes,
  POINTER(UINT8)                        #   IN  *Buffer
  )

EFI_SPI_NOR_FLASH_PROTOCOL_ERASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_NOR_FLASH_PROTOCOL),  #   IN  *This
  UINT32,                               #   IN  FlashAddress,
  UINT32                                #   IN  BlockCount
  )

EFI_SPI_NOR_FLASH_PROTOCOL._fields_ = [
    ("SpiPeripheral",   POINTER(EFI_SPI_PERIPHERAL)),
    ("FlashSize",       UINT32),
    ("Deviceid",        UINT8 * 3),
    ("EraseBlockBytes", UINT32),
    ("GetFlashid",      EFI_SPI_NOR_FLASH_PROTOCOL_GET_FLASH_ID),
    ("ReadData",        EFI_SPI_NOR_FLASH_PROTOCOL_READ_DATA),
    ("LfReadData",      EFI_SPI_NOR_FLASH_PROTOCOL_READ_DATA),
    ("ReadStatus",      EFI_SPI_NOR_FLASH_PROTOCOL_READ_STATUS),
    ("WriteStatus",     EFI_SPI_NOR_FLASH_PROTOCOL_WRITE_STATUS),
    ("WriteData",       EFI_SPI_NOR_FLASH_PROTOCOL_WRITE_DATA),
    ("Erase",           EFI_SPI_NOR_FLASH_PROTOCOL_ERASE)
  ]

