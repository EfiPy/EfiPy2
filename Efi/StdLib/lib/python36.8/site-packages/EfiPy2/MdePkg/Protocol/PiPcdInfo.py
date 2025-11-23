# PiPcdInfo.py
#
# EfiPy2.MdePkg.Protocol.PiPcdInfo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMultiPhase import EFI_PCD_INFO

gEfiGetPcdInfoProtocolGuid  = \
  EFI_GUID (0xfd0f4478,  0xefd, 0x461d, ( 0xba, 0x2d, 0xe5, 0x8c, 0x45, 0xfd, 0x5f, 0x5e ))

class EFI_GET_PCD_INFO_PROTOCOL (Structure):
  pass

EFI_GET_PCD_INFO_PROTOCOL_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),                  # IN CONST  *Guid,
  UINTN,                              # IN        TokenNumber,
  POINTER(EFI_PCD_INFO)  # OUT       *PcdInfo
  )

EFI_GET_PCD_INFO_PROTOCOL_GET_SKU = CFUNCTYPE (
  UINTN
  )

EFI_GET_PCD_INFO_PROTOCOL._fields_ = [
    ("GetInfo", EFI_GET_PCD_INFO_PROTOCOL_GET_INFO),
    ("GetSku",  EFI_GET_PCD_INFO_PROTOCOL_GET_SKU)
  ]

