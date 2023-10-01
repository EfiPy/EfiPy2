# HttpUtilities.py
#
# EfiPy2.MdePkg.Protocol.HttpUtilities
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Http import EFI_HTTP_HEADER

gEfiHttpUtilitiesProtocolGuid  = \
  EFI_GUID (0x3e35c163, 0x4074, 0x45dd, (0x43, 0x1e, 0x23, 0x98, 0x9d, 0xd8, 0x6b, 0x32 ))

class EFI_HTTP_UTILITIES_PROTOCOL (Structure):
  pass

EFI_HTTP_UTILS_BUILD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_UTILITIES_PROTOCOL), #   IN  *This,
  UINTN,                                #   IN  SeedMessageSize,
  PVOID,                                #   IN  *SeedMessage    OPTIONAL,
  UINTN,                                #   IN  DeleteCount,
  PCHAR8 * 1,                           #   IN  *DeleteList[]   OPTIONAL,
  UINTN,                                #   IN  AppendCount,
  POINTER(EFI_HTTP_HEADER) * 1,         #   IN  *AppendList[]   OPTIONAL,
  POINTER(UINTN),                       #   OUT *NewMessageSize,
  POINTER(PVOID)                        #   OUT **NewMessage
  )

EFI_HTTP_UTILS_PARSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_UTILITIES_PROTOCOL), #   IN  *This,
  PCHAR8,                               #   IN  *HttpMessage,
  UINTN,                                #   IN  HttpMessageSize,
  POINTER(POINTER(EFI_HTTP_HEADER)),    #   OUT **HeaderFields,
  POINTER(UINTN)                        #   OUT *FieldCount
  )

EFI_HTTP_UTILITIES_PROTOCOL._fields_ = [
    ("Build",    EFI_HTTP_UTILS_BUILD),
    ("Parse",    EFI_HTTP_UTILS_PARSE)
  ]

