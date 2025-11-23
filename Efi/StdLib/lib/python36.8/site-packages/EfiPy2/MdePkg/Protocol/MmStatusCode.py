# MmStatusCode.py
#
# EfiPy2.MdePkg.Protocol.MmStatusCode
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Pi.PiStatusCode  import EFI_STATUS_CODE_TYPE, EFI_STATUS_CODE_VALUE, EFI_STATUS_CODE_DATA

gEfiMmStatusCodeProtocolGuid = \
  EFI_GUID (0x6afd2b77, 0x98c1, 0x4acd, (0xa6, 0xf9, 0x8a, 0x94, 0x39, 0xde, 0xf, 0xb1 ))

class EFI_MM_STATUS_CODE_PROTOCOL (Structure):
  pass

EFI_MM_REPORT_STATUS_CODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_STATUS_CODE_PROTOCOL),     #   IN CONST *This
  EFI_STATUS_CODE_TYPE,                     #   IN       CodeType,
  EFI_STATUS_CODE_VALUE,                    #   IN       Value,
  UINT32,                                   #   IN       Instance,
  POINTER(EFI_GUID),                        #   IN CONST *CallerId,
  POINTER(EFI_STATUS_CODE_DATA)             #   IN       *Data OPTIONAL
  )

EFI_MM_STATUS_CODE_PROTOCOL._fields_ = [
    ("ReportStatusCode",    EFI_MM_REPORT_STATUS_CODE)
  ]

