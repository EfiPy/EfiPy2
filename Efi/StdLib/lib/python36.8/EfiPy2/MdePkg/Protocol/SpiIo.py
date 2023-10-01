# SpiIo.py
#
# EfiPy2.MdePkg.Protocol.SpiIo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.LegacySpiController import EFI_LEGACY_SPI_CONTROLLER_PROTOCOL

from EfiPy2.MdePkg.Protocol.SpiConfiguration    import EFI_SPI_PERIPHERAL

class EFI_SPI_IO_PROTOCOL (Structure):
  pass

SPI_TRANSACTION_FULL_DUPLEX     = 1
SPI_TRANSACTION_WRITE_ONLY      = 2
SPI_TRANSACTION_READ_ONLY       = 3
SPI_TRANSACTION_WRITE_THEN_READ = 4
EFI_SPI_TRANSACTION_TYPE        = ENUM

EFI_SPI_IO_PROTOCOL_TRANSACTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_IO_PROTOCOL), #   IN  *This
  EFI_SPI_TRANSACTION_TYPE,     #   IN  TransactionType,
  BOOLEAN,                      #   IN  DebugTransaction,
  UINT32,                       #   IN  ClockHz OPTIONAL,
  UINT32,                       #   IN  BusWidth,
  UINT32,                       #   IN  FrameSize,
  UINT32,                       #   IN  WriteBytes,
  POINTER(UINT8),               #   IN  *WriteBuffer,
  UINT32,                       #   IN  ReadBytes,
  POINTER(UINT8)                #   OUT *ReadBuffer
  )

EFI_SPI_IO_PROTOCOL_UPDATE_SPI_PERIPHERAL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_IO_PROTOCOL), #   IN CONST *This
  POINTER(EFI_SPI_PERIPHERAL)   #   IN CONST *SpiPeripheral
  )

class EFI_SPI_BUS_TRANSACTION (Structure):
  _fields_ = [
    ("SpiPeripheral",       POINTER(EFI_SPI_PERIPHERAL)),
    ("TransactionType",     EFI_SPI_TRANSACTION_TYPE),
    ("DebugTransaction",    BOOLEAN),
    ("BusWidth",            UINT32),
    ("FrameSize",           UINT32),
    ("WriteBytes",          UINT32),
    ("WriteBuffer",         POINTER(UINT8)),
    ("ReadBytes",           UINT32),
    ("ReadBuffer",          POINTER(UINT8))
  ]

EFI_SPI_IO_PROTOCOL._fields_ = [
    ("SpiPeripheral",           POINTER(EFI_SPI_PERIPHERAL)),
    ("OriginalSpiPeripheral",   POINTER(EFI_SPI_PERIPHERAL)),
    ("FrameSizeSupportMask",    UINT32),
    ("MaximumTransferBytes",    UINT32),
    ("Attributes",              UINT32),
    ("LegacySpiProtocol",       POINTER(EFI_LEGACY_SPI_CONTROLLER_PROTOCOL)),
    ("Transaction",             EFI_SPI_IO_PROTOCOL_TRANSACTION),
    ("UpdateSpiPeripheral",     EFI_SPI_IO_PROTOCOL_UPDATE_SPI_PERIPHERAL)
  ]

