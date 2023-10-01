# SmartCardReader.py
#
# EfiPy2.MdePkg.Protocol.SmartCardReader
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSmartCardReaderProtocolGuid         = \
  EFI_GUID (0x2a4d1adf, 0x21dc, 0x4b81, (0xa4, 0x2f, 0x8b, 0x8e, 0xe2, 0x38, 0x00, 0x60))

class EFI_SMART_CARD_READER_PROTOCOL (Structure):
  pass

SCARD_AM_READER              = 0x0001
SCARD_AM_CARD                = 0x0002

SCARD_CA_NORESET             = 0x0000
SCARD_CA_COLDRESET           = 0x0001
SCARD_CA_WARMRESET           = 0x0002
SCARD_CA_UNPOWER             = 0x0003
SCARD_CA_EJECT               = 0x0004

SCARD_PROTOCOL_UNDEFINED     = 0x0000
SCARD_PROTOCOL_T0            = 0x0001
SCARD_PROTOCOL_T1            = 0x0002
SCARD_PROTOCOL_RAW           = 0x0004

SCARD_UNKNOWN                = 0x0000
SCARD_ABSENT                 = 0x0001
SCARD_INACTIVE               = 0x0002
SCARD_ACTIVE                 = 0x0003

def SCARD_CTL_CODE(code):
  return 0x42000000 + code

CM_IOCTL_GET_FEATURE_REQUEST = SCARD_CTL_CODE(3400)

EFI_SMART_CARD_READER_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_READER_PROTOCOL),  # IN      *This
  UINT32,                                   # IN      AccessMode,
  UINT32,                                   # IN      CardAction,
  UINT32,                                   # IN      PreferredProtocols,
  POINTER(UINT32)                           #    OUT  *ActiveProtocol
  )

EFI_SMART_CARD_READER_DISCONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_READER_PROTOCOL),  # IN      *This,
  UINT32                                    # IN      CardAction
  )

EFI_SMART_CARD_READER_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_READER_PROTOCOL),  # IN      *This
  PCHAR16,                                  #    OUT  *ReaderName OPTIONAL,
  POINTER(UINTN),                           # IN OUT  *ReaderNameLength OPTIONAL,
  POINTER(UINT32),                          #    OUT  *State OPTIONAL,
  POINTER(UINT32),                          #    OUT  *CardProtocol OPTIONAL,
  POINTER(UINT8),                           #    OUT  *Atr OPTIONAL,
  POINTER(UINTN)                            # IN OUT  *AtrLength OPTIONAL
  )

EFI_SMART_CARD_READER_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_READER_PROTOCOL),  # IN      *This
  POINTER(UINT8),                           # IN      *CAPDU,
  UINTN,                                    # IN      CAPDULength,
  POINTER(UINT8),                           #    OUT  *RAPDU,
  POINTER(UINTN)                            # IN OUT  *RAPDULength
  )

EFI_SMART_CARD_READER_CONTROL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_READER_PROTOCOL),  # IN      *This
  UINT32,                                   # IN      ControlCode,
  POINTER(UINT8),                           # IN      *InBuffer OPTIONAL,
  UINTN,                                    # IN      InBufferLength OPTIONAL,
  POINTER(UINT8),                           #    OUT  *OutBuffer OPTIONAL,
  POINTER(UINTN)                            # IN OUT  *OutBufferLength OPTIONAL
  )

EFI_SMART_CARD_READER_GET_ATTRIB = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_READER_PROTOCOL),  # IN      *This
  UINT32,                                   # IN      Attrib,
  POINTER(UINT8),                           #    OUT  *OutBuffer,
  POINTER(UINTN)                            # IN OUT  *OutBufferLength
  )

EFI_SMART_CARD_READER_PROTOCOL._fields_ = [
    ("SCardConnect",    EFI_SMART_CARD_READER_CONNECT),
    ("SCardDisconnect", EFI_SMART_CARD_READER_DISCONNECT),
    ("SCardStatus",     EFI_SMART_CARD_READER_STATUS),
    ("SCardTransmit",   EFI_SMART_CARD_READER_TRANSMIT),
    ("SCardControl",    EFI_SMART_CARD_READER_CONTROL),
    ("SCardGetAttrib",  EFI_SMART_CARD_READER_GET_ATTRIB)
  ]

