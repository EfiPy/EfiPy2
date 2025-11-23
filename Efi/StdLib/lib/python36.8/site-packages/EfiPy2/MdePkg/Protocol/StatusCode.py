# StatusCode.py
#
# EfiPy2.MdePkg.Protocol.StatusCode
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiStatusCode  import \
    EFI_STATUS_CODE_TYPE,   \
    EFI_STATUS_CODE_VALUE,  \
    EFI_STATUS_CODE_DATA

gEfiStatusCodeRuntimeProtocolGuid   = \
  EFI_GUID (0xd2b2b828, 0x826, 0x48a7,  ( 0xb3, 0xdf, 0x98, 0x3c, 0x0, 0x60, 0x24, 0xf0 ))

EFI_REPORT_STATUS_CODE = CFUNCTYPE (
  EFI_STATUS,
  EFI_STATUS_CODE_TYPE,         # IN Type,
  EFI_STATUS_CODE_VALUE,        # IN Value,
  UINT32,                       # IN Instance,
  POINTER(EFI_GUID),            # IN *CallerId  OPTIONAL,
  POINTER(EFI_STATUS_CODE_DATA) # IN *Data      OPTIONAL
  )

class EFI_STATUS_CODE_PROTOCOL (Structure):
  _fields_ = [
    ("ReportStatusCode",  EFI_REPORT_STATUS_CODE)
  ]

