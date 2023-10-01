# Timestamp.py
#
# EfiPy2.MdePkg.Protocol.Timestamp
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiTimestampProtocolGuid = \
  EFI_GUID (0xafbfde41, 0x2e6e, 0x4262, (0xba, 0x65, 0x62, 0xb9, 0x23, 0x6e, 0x54, 0x95 ))

class EFI_TIMESTAMP_PROTOCOL (Structure):
  pass

class EFI_TIMESTAMP_PROPERTIES (Structure):
  _fields_ = [
    ("Frequency", UINT64),
    ("EndValue",  UINT64)
  ]

TIMESTAMP_GET = CFUNCTYPE (
  UINT64
  )

TIMESTAMP_GET_PROPERTIES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIMESTAMP_PROPERTIES)     # OUT *Properties
  )

EFI_TIMESTAMP_PROTOCOL._fields_ = [
    ("GetTimestamp",  TIMESTAMP_GET),
    ("GetProperties", TIMESTAMP_GET_PROPERTIES)
  ]

