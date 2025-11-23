# IpmiSerial.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiSerial
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
# 
from EfiPy2.MdePkg.IndustryStandard import *

BASIC_MODE_START                   = 0xA0
BASIC_MODE_STOP                    = 0xA5
BASIC_MODE_HANDSHAKE               = 0xA6
BASIC_MODE_ESCAPE                  = 0xAA
BASIC_MODE_ESC_CHAR                = 0x1B
BASIC_MODE_START_ENCODED_BYTE      = 0xB0
BASIC_MODE_STOP_ENCODED_BYTE       = 0xB5
BASIC_MODE_HANDSHAKE_ENCODED_BYTE  = 0xB6
BASIC_MODE_ESCAPE_ENCODED_BYTE     = 0xBA
BASIC_MODE_ESC_CHAR_ENCODED_BYTE   = 0x3B

MSG_IDLE         = 0
MSG_IN_PROGRESS  = 1

IPMI_MAX_LUN                              = 0x3
IPMI_MAX_NETFUNCTION                      = 0x3F
IPMI_SERIAL_CONNECTION_HEADER_LENGTH      = 3
IPMI_SERIAL_REQUEST_DATA_HEADER_LENGTH    = 3
IPMI_SERIAL_MAXIMUM_PACKET_SIZE_IN_BYTES  = 256
IPMI_SERIAL_MIN_REQUEST_LENGTH            = 7

class IPMI_SERIAL_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponderAddress",  UINT8),
    ("ResponderNetFnLun", UINT8),
    ("CheckSum",          UINT8),
    ("RequesterAddress",  UINT8),
    ("RequesterSeqLun",   UINT8),
    ("Command",           UINT8)
    # ("Data", UINT8 * N)
  ]

