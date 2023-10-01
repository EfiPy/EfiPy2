# PcdInfo.py
#
# EfiPy2.MdePkg.Protocol.PcdInfo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMultiPhase import EFI_PCD_INFO

gGetPcdInfoProtocolGuid = \
  EFI_GUID (0x5be40f57, 0xfa68, 0x4610, ( 0xbb, 0xbf, 0xe9, 0xc5, 0xfc, 0xda, 0xd3, 0x65 ))

class GET_PCD_INFO_PROTOCOL (Structure):
  pass

GET_PCD_INFO_PROTOCOL_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                # IN  TokenNumber,
  POINTER(EFI_PCD_INFO) # OUT *PcdInfo
  )

GET_PCD_INFO_PROTOCOL_GET_INFO_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),    # IN CONST  *Guid,
  UINTN,                # IN  TokenNumber,
  POINTER(EFI_PCD_INFO) # OUT *PcdInfo
  )

GET_PCD_INFO_PROTOCOL_GET_SKU = CFUNCTYPE (
  UINTN
  )

GET_PCD_INFO_PROTOCOL._fields_ = [
    ("GetInfo",   GET_PCD_INFO_PROTOCOL_GET_INFO),
    ("GetInfoEx", GET_PCD_INFO_PROTOCOL_GET_INFO_EX),
    ("GetSku",    GET_PCD_INFO_PROTOCOL_GET_SKU)
  ]
