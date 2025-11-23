# Mtftp6.py
#
# EfiPy2.MdePkg.Protocol.Mtftp6
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMtftp6ServiceBindingProtocolGuid    = \
  EFI_GUID (0xd9760ff3, 0x3cca, 0x4267, (0x80, 0xf9, 0x75, 0x27, 0xfa, 0xfa, 0x42, 0x23 ))

gEfiMtftp6ProtocolGuid                  = \
  EFI_GUID (0xbf0a78ba, 0xec29, 0x49cf, (0xa1, 0xc9, 0x7a, 0xe5, 0x4e, 0xab, 0x6a, 0x51 ))

class EFI_MTFTP6_PROTOCOL (Structure):
  pass

class EFI_MTFTP6_TOKEN (Structure):
  pass

EFI_MTFTP6_OPCODE_RRQ                     = 1
EFI_MTFTP6_OPCODE_WRQ                     = 2
EFI_MTFTP6_OPCODE_DATA                    = 3
EFI_MTFTP6_OPCODE_ACK                     = 4
EFI_MTFTP6_OPCODE_ERROR                   = 5
EFI_MTFTP6_OPCODE_OACK                    = 6
EFI_MTFTP6_OPCODE_DIR                     = 7
EFI_MTFTP6_OPCODE_DATA8                   = 8
EFI_MTFTP6_OPCODE_ACK8                    = 9

EFI_MTFTP6_ERRORCODE_NOT_DEFINED          = 0
EFI_MTFTP6_ERRORCODE_FILE_NOT_FOUND       = 1
EFI_MTFTP6_ERRORCODE_ACCESS_VIOLATION     = 2
EFI_MTFTP6_ERRORCODE_DISK_FULL            = 3
EFI_MTFTP6_ERRORCODE_ILLEGAL_OPERATION    = 4
EFI_MTFTP6_ERRORCODE_UNKNOWN_TRANSFER_ID  = 5
EFI_MTFTP6_ERRORCODE_FILE_ALREADY_EXISTS  = 6
EFI_MTFTP6_ERRORCODE_NO_SUCH_USER         = 7
EFI_MTFTP6_ERRORCODE_REQUEST_DENIED       = 8

class EFI_MTFTP6_REQ_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",    UINT16),
    ("Filename",  UINT8 * 1)
  ]

class EFI_MTFTP6_OACK_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_MTFTP6_DATA_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_MTFTP6_ACK_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT16 * 1)
  ]

class EFI_MTFTP6_DATA8_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT64),
    ("Data",    UINT8 * 1)
  ]

class EFI_MTFTP6_ACK8_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("Block",   UINT64 * 1)
  ]

class EFI_MTFTP6_ERROR_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",        UINT16),
    ("ErrorCode",     UINT16),
    ("ErrorMessage",  UINT8 * 1)
  ]

class EFI_MTFTP6_PACKET (Union):
  _pack_   = 1
  _fields_ = [
    ("OpCode", UINT16),
    ("Rrq",   EFI_MTFTP6_REQ_HEADER),
    ("Wrq",   EFI_MTFTP6_REQ_HEADER),
    ("Oack",  EFI_MTFTP6_OACK_HEADER),
    ("Data",  EFI_MTFTP6_DATA_HEADER),
    ("Ack",   EFI_MTFTP6_ACK_HEADER),
    ("Data8", EFI_MTFTP6_DATA8_HEADER),
    ("Ack8",  EFI_MTFTP6_ACK8_HEADER),
    ("Error", EFI_MTFTP6_ERROR_HEADER)
  ]

class EFI_MTFTP6_CONFIG_DATA (Structure):
  _fields_ = [
    ("StationIp",         EFI_IPv6_ADDRESS),
    ("LocalPort",         UINT16),
    ("ServerIp",          EFI_IPv6_ADDRESS),
    ("InitialServerPort", UINT16),
    ("TryCount",          UINT16),
    ("TimeoutValue",      UINT16)
  ]

class EFI_MTFTP6_MODE_DATA (Structure):
  _fields_ = [
    ("ConfigData",            EFI_MTFTP6_CONFIG_DATA),
    ("SupportedOptionCount",  UINT8),
    ("SupportedOptions",      POINTER(POINTER(UINT8)))
  ]

class EFI_MTFTP6_OVERRIDE_DATA (Structure):
  _fields_ = [
    ("ServerIp",      EFI_IPv6_ADDRESS),
    ("ServerPort",    UINT16),
    ("TryCount",      UINT16),
    ("TimeoutValue",  UINT16)
  ]

class EFI_MTFTP6_OPTION (Structure):
  _fields_ = [
    ("OptionStr", POINTER(UINT8)),
    ("ValueStr",  POINTER(UINT8))
  ]

EFI_MTFTP6_CHECK_PACKET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN *This,
  POINTER(EFI_MTFTP6_TOKEN),            # IN *Token,
  UINT16,                               # IN PacketLen,
  POINTER(EFI_MTFTP6_PACKET)            # IN *Paket
  )

EFI_MTFTP6_TIMEOUT_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN *This,
  POINTER(EFI_MTFTP6_TOKEN)             # IN *Token
  )

EFI_MTFTP6_PACKET_NEEDED = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN      *This,
  POINTER(EFI_MTFTP6_TOKEN),            # IN      *Token,
  POINTER(UINT16),                      # IN  OUT *Length,
  POINTER(PVOID)                        # OUT     **Buffer
  )

class EFI_MTFTP6_TOKEN (Structure):
  _fields_ = [
    ("Status",          EFI_STATUS),
    ("Event",           EFI_EVENT),
    ("OverrideData",    POINTER(EFI_MTFTP6_OVERRIDE_DATA)),
    ("Filename",        POINTER(UINT8)),
    ("ModeStr",         POINTER(UINT8)),
    ("OptionCount",     UINT32),
    ("OptionList",      POINTER(EFI_MTFTP6_OPTION)),
    ("BufferSize",      UINT64),
    ("Buffer",          PVOID),
    ("Context",         PVOID),
    ("CheckPacket",     EFI_MTFTP6_CHECK_PACKET),
    ("TimeoutCallback", EFI_MTFTP6_TIMEOUT_CALLBACK),
    ("PacketNeeded",    EFI_MTFTP6_PACKET_NEEDED)
  ]

EFI_MTFTP6_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN      *This,
  POINTER(EFI_MTFTP6_MODE_DATA)         #     OUT *ModeData
  )

EFI_MTFTP6_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP6_CONFIG_DATA)       # IN  *MtftpConfigData OPTIONAL
  )

EFI_MTFTP6_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP6_OVERRIDE_DATA),    # IN  *OverrideData   OPTIONAL,
  POINTER(UINT8),                       # IN  *Filename,
  POINTER(UINT8),                       # IN  *ModeStr        OPTIONAL,
  UINT8,                                # IN  OptionCount,
  POINTER(EFI_MTFTP6_OPTION),           # IN  *OptionList OPTIONAL,
  POINTER(UINT32),                      # OUT *PacketLength,
  POINTER(POINTER(EFI_MTFTP6_PACKET))   # OUT **Packet        OPTIONAL
  )

EFI_MTFTP6_PARSE_OPTIONS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN  *This,
  UINT32,                               # IN  PacketLen,
  POINTER(EFI_MTFTP6_PACKET),           # IN  *Packet,
  POINTER(UINT32),                      # OUT *OptionCount,
  POINTER(POINTER(EFI_MTFTP6_OPTION))   # OUT **OptionList OPTIONAL
  )

EFI_MTFTP6_READ_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP6_TOKEN)             # IN  *Token
  )

EFI_MTFTP6_WRITE_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP6_TOKEN)             # IN  *Token
  )

EFI_MTFTP6_READ_DIRECTORY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL),         # IN  *This,
  POINTER(EFI_MTFTP6_TOKEN)             # IN  *Token
  )

EFI_MTFTP6_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MTFTP6_PROTOCOL)          # IN  *This,
  )

EFI_MTFTP6_PROTOCOL._fields_ = [
    ("GetModeData",   EFI_MTFTP6_GET_MODE_DATA),
    ("Configure",     EFI_MTFTP6_CONFIGURE),
    ("GetInfo",       EFI_MTFTP6_GET_INFO),
    ("ParseOptions",  EFI_MTFTP6_PARSE_OPTIONS),
    ("ReadFile",      EFI_MTFTP6_READ_FILE),
    ("WriteFile",     EFI_MTFTP6_WRITE_FILE),
    ("ReadDirectory", EFI_MTFTP6_READ_DIRECTORY),
    ("Poll",          EFI_MTFTP6_POLL)
  ]

