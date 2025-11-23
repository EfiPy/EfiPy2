# SpiHc.py
#
# EfiPy2.MdePkg.Protocol.SpiHc
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.SpiConfiguration import EFI_SPI_PERIPHERAL

from EfiPy2.MdePkg.Protocol.SpiIo            import EFI_SPI_BUS_TRANSACTION

gEfiSpiHcProtocolGuid           = \
  EFI_GUID (0xc74e5db2, 0xfa96, 0x4ae2, ( 0xb3, 0x99, 0x15, 0x97, 0x7f, 0xe3, 0x0, 0x2d ))

class EFI_SPI_HC_PROTOCOL (Structure):
  pass

EFI_SPI_HC_PROTOCOL_CHIP_SELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_HC_PROTOCOL), #   IN       *This
  POINTER(EFI_SPI_PERIPHERAL),  #   IN CONST *SpiPeripheral,
  BOOLEAN                       #   IN       PinValue
  )

EFI_SPI_HC_PROTOCOL_CLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_HC_PROTOCOL),         #   IN CONST *This
  POINTER(EFI_SPI_PERIPHERAL),          #   IN CONST *SpiPeripheral,
  POINTER(UINT32)                       #   IN       *ClockHz
  )

EFI_SPI_HC_PROTOCOL_TRANSACTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_HC_PROTOCOL),         #   IN CONST *This,
  POINTER(EFI_SPI_BUS_TRANSACTION),     #   IN       *BusTransaction
  )

HC_SUPPORTS_WRITE_ONLY_OPERATIONS       = BIT0
HC_SUPPORTS_READ_ONLY_OPERATIONS        = BIT1
HC_SUPPORTS_WRITE_THEN_READ_OPERATIONS  = BIT2
HC_TX_FRAME_IN_MOST_SIGNIFICANT_BITS    = BIT3
HC_RX_FRAME_IN_MOST_SIGNIFICANT_BITS    = BIT4
HC_SUPPORTS_2_BIT_DATA_BUS_WIDTH        = BIT5
HC_SUPPORTS_4_BIT_DATA_BUS_WIDTH        = BIT6
HC_SUPPORTS_8_BIT_DATA_BUS_WIDTH        = BIT7
HC_TRANSFER_SIZE_INCLUDES_OPCODE        = BIT8
HC_TRANSFER_SIZE_INCLUDES_ADDRESS       = BIT9
EFI_SPI_HC_PROTOCOL._fields_ = [
    ("Attributes",              UINT32),
    ("FrameSizeSupportMask",    UINT32),
    ("MaximumTransferBytes",    UINT32),
    ("ChipSelect",              EFI_SPI_HC_PROTOCOL_CHIP_SELECT),
    ("Clock",                   EFI_SPI_HC_PROTOCOL_CLOCK),
    ("Transaction",             EFI_SPI_HC_PROTOCOL_TRANSACTION)
  ]

