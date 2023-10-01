# Mtftp4.py
#
# EfiPy2.MdePkg.Protocol.Mtftp4
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMtftp4ServiceBindingProtocolGuid  = \
  EFI_GUID (0x2FE800BE, 0x8F01, 0x4aa6, (0x94, 0x6B, 0xD7, 0x13, 0x88, 0xE1, 0x83, 0x3F ))

gEfiMtftp4ProtocolGuid                = \
  EFI_GUID (0x78247c57, 0x63db, 0x4708, (0x99, 0xc2, 0xa8, 0xb4, 0xa9, 0xa6, 0x1f, 0x6b ))

class EFI_MTFTP4_PROTOCOL (Structure):
  pass

class EFI_MTFTP4_TOKEN (Structure):
  pass

EFI_MTFTP4_OPCODE_RRQ                     = 1
EFI_MTFTP4_OPCODE_WRQ                     = 2
EFI_MTFTP4_OPCODE_DATA                    = 3
EFI_MTFTP4_OPCODE_ACK                     = 4
EFI_MTFTP4_OPCODE_ERROR                   = 5
EFI_MTFTP4_OPCODE_OACK                    = 6
EFI_MTFTP4_OPCODE_DIR                     = 7
EFI_MTFTP4_OPCODE_DATA8                   = 8
EFI_MTFTP4_OPCODE_ACK8                    = 9

EFI_MTFTP4_ERRORCODE_NOT_DEFINED          = 0
EFI_MTFTP4_ERRORCODE_FILE_NOT_FOUND       = 1
EFI_MTFTP4_ERRORCODE_ACCESS_VIOLATION     = 2
EFI_MTFTP4_ERRORCODE_DISK_FULL            = 3
EFI_MTFTP4_ERRORCODE_ILLEGAL_OPERATION    = 4
EFI_MTFTP4_ERRORCODE_UNKNOWN_TRANSFER_ID  = 5
EFI_MTFTP4_ERRORCODE_FILE_ALREADY_EXISTS  = 6
EFI_MTFTP4_ERRORCODE_NO_SUCH_USER         = 7
EFI_MTFTP4_ERRORCODE_REQUEST_DENIED       = 8

class EFI_MTFTP4_REQ_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",    UINT16),
    ("Filename",  UINT8 * 1)
  ]

class EFI_MTFTP4_OACK_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_MTFTP4_DATA_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_MTFTP4_ACK_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT16 * 1)
  ]

class EFI_MTFTP4_DATA8_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT64),
    ("Data",    UINT8 * 1)
  ]

class EFI_MTFTP4_ACK8_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT64 * 1)
  ]

class EFI_MTFTP4_ERROR_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",        UINT16),
    ("ErrorCode",     UINT16),
    ("ErrorMessage",  UINT8 * 1)
  ]

class EFI_MTFTP4_PACKET (Union):
  _pack_   = 1
  _fields_ = [
    ("OpCode; ", UINT16),
    ("Rrq;    ", EFI_MTFTP4_REQ_HEADER),
    ("Wrq;    ", EFI_MTFTP4_REQ_HEADER),
    ("Oack;   ", EFI_MTFTP4_OACK_HEADER),
    ("Data;   ", EFI_MTFTP4_DATA_HEADER),
    ("Ack;    ", EFI_MTFTP4_ACK_HEADER),
    ("Data8;  ", EFI_MTFTP4_DATA8_HEADER),
    ("Ack8;   ", EFI_MTFTP4_ACK8_HEADER),
    ("Error;  ", EFI_MTFTP4_ERROR_HEADER)
  ]

class EFI_MTFTP4_OPTION (Structure):
  _fields_ = [
    ("OptionStr", POINTER(UINT8)),
    ("ValueStr",  POINTER(UINT8))
  ]

class EFI_MTFTP4_CONFIG_DATA (Structure):
  _fields_ = [
    ("UseDefaultSetting", BOOLEAN),
    ("StationIp",         EFI_IPv4_ADDRESS),
    ("SubnetMask",        EFI_IPv4_ADDRESS),
    ("LocalPort",         UINT16),
    ("GatewayIp",         EFI_IPv4_ADDRESS),
    ("ServerIp",          EFI_IPv4_ADDRESS),
    ("InitialServerPort", UINT16),
    ("TryCount",          UINT16),
    ("TimeoutValue",      UINT16)
  ]

class EFI_MTFTP4_MODE_DATA (Structure):
  _fields_ = [
    ("ConfigData",              EFI_MTFTP4_CONFIG_DATA),
    ("SupportedOptionCount",    UINT8),
    ("SupportedOptoins",        POINTER(POINTER(UINT8))),
    ("UnsupportedOptionCount",  UINT8),
    ("UnsupportedOptoins",      POINTER(POINTER(UINT8)))
  ]

class EFI_MTFTP4_OVERRIDE_DATA (Structure):
  _fields_ = [
    ("GatewayIp",     EFI_IPv4_ADDRESS),
    ("ServerIp",      EFI_IPv4_ADDRESS),
    ("ServerPort",    UINT16),
    ("TryCount",      UINT16),
    ("TimeoutValue",  UINT16)
  ]

EFI_MTFTP4_CHECK_PACKET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN *This,
  POINTER(EFI_MTFTP4_TOKEN),            # IN *Token,
  UINT16,                               # IN PacketLen,
  POINTER(EFI_MTFTP4_PACKET)            # IN *Paket
  )

EFI_MTFTP4_TIMEOUT_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN *This,
  POINTER(EFI_MTFTP4_TOKEN)             # IN *Token
  )

EFI_MTFTP4_PACKET_NEEDED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN      *This,
  POINTER(EFI_MTFTP4_TOKEN),            # IN      *Token,
  POINTER(UINT16),                      # IN  OUT *Length,
  POINTER(PVOID)                        # OUT     **Buffer
  )

EFI_MTFTP4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN      *This,
  POINTER(EFI_MTFTP4_MODE_DATA)         #     OUT *ModeData
  )

EFI_MTFTP4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP4_CONFIG_DATA)       # IN  *MtftpConfigData OPTIONAL
  )

EFI_MTFTP4_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP4_OVERRIDE_DATA),    # IN  *OverrideData   OPTIONAL,
  POINTER(UINT8),                       # IN  *Filename,
  POINTER(UINT8),                       # IN  *ModeStr        OPTIONAL,
  UINT8,                                # IN  OptionCount,
  POINTER(EFI_MTFTP4_OPTION),           # IN  *OptionList,
  POINTER(UINT32),                      # OUT *PacketLength,
  POINTER(POINTER(EFI_MTFTP4_PACKET))   # OUT **Packet        OPTIONAL
  )

EFI_MTFTP4_PARSE_OPTIONS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN  *This,
  UINT32,                               # IN  PacketLen,
  POINTER(EFI_MTFTP4_PACKET),           # IN  *Packet,
  POINTER(UINT32),                      # OUT *OptionCount,
  POINTER(POINTER(EFI_MTFTP4_OPTION))   # OUT **OptionList OPTIONAL
  )

EFI_MTFTP4_READ_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP4_TOKEN)             # IN  *Token
  )

EFI_MTFTP4_WRITE_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP4_TOKEN)             # IN  *Token
  )

EFI_MTFTP4_READ_DIRECTORY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP4_TOKEN)             # IN  *Token
  )

EFI_MTFTP4_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP4_PROTOCOL)          # IN  *This,
  )

EFI_MTFTP4_PROTOCOL._fields_ = [
    ("GetModeData",   EFI_MTFTP4_GET_MODE_DATA),
    ("Configure",     EFI_MTFTP4_CONFIGURE),
    ("GetInfo",       EFI_MTFTP4_GET_INFO),
    ("ParseOptions",  EFI_MTFTP4_PARSE_OPTIONS),
    ("ReadFile",      EFI_MTFTP4_READ_FILE),
    ("WriteFile",     EFI_MTFTP4_WRITE_FILE),
    ("ReadDirectory", EFI_MTFTP4_READ_DIRECTORY),
    ("Poll",          EFI_MTFTP4_POLL)
  ]

EFI_MTFTP4_TOKEN._fields_ = [
    ("Status",          EFI_STATUS),
    ("Event",           EFI_EVENT),
    ("OverrideData",    POINTER(EFI_MTFTP4_OVERRIDE_DATA)),
    ("Filename",        POINTER(UINT8)),
    ("ModeStr",         POINTER(UINT8)),
    ("OptionCount",     UINT32),
    ("OptionList",      POINTER(EFI_MTFTP4_OPTION)),
    ("BufferSize",      UINT64),
    ("Buffer",          PVOID),
    ("Context",         PVOID),
    ("CheckPacket",     EFI_MTFTP4_CHECK_PACKET),
    ("TimeoutCallback", EFI_MTFTP4_TIMEOUT_CALLBACK),
    ("PacketNeeded",    EFI_MTFTP4_PACKET_NEEDED)
  ]

