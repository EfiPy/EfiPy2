# ReportStatusCodeHandler.py
#
# EfiPy2.MdePkg.Protocol.ReportStatusCodeHandler
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiStatusCode  import \
             EFI_STATUS_CODE_TYPE,         \
             EFI_STATUS_CODE_VALUE,        \
             EFI_STATUS_CODE_DATA

gEfiRscHandlerProtocolGuid  = \
  EFI_GUID (0x86212936, 0xe76, 0x41c8, (0xa0, 0x3a, 0x2a, 0xf2, 0xfc, 0x1c, 0x39, 0xe2))

EFI_RSC_HANDLER_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  EFI_STATUS_CODE_TYPE,                 # IN CodeType,
  EFI_STATUS_CODE_VALUE,                # IN Value,
  UINT32,                               # IN Instance,
  POINTER(EFI_GUID),                    # IN *CallerId,
  POINTER(EFI_STATUS_CODE_DATA)         # IN *Data
  )

EFI_RSC_HANDLER_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_RSC_HANDLER_CALLBACK, # IN Callback
  EFI_TPL                   # IN Tpl
  )

EFI_RSC_HANDLER_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_RSC_HANDLER_CALLBACK  # IN Callback
  )

class EFI_RSC_HANDLER_PROTOCOL (Structure):
  _fields_ = [
    ("Register",    EFI_RSC_HANDLER_REGISTER),
    ("Unregister",  EFI_RSC_HANDLER_UNREGISTER)
  ]

