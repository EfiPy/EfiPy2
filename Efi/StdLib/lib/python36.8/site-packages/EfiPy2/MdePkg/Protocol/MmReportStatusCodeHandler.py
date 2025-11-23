# MmReportStatusCodeHandler.py
#
# EfiPy2.MdePkg.Protocol.MmReportStatusCodeHandler
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Pi.PiStatusCode  import EFI_STATUS_CODE_TYPE, EFI_STATUS_CODE_VALUE, EFI_STATUS_CODE_DATA

gEfiMmRscHandlerProtocolGuid = \
  EFI_GUID (0x2ff29fa7, 0x5e80, 0x4ed9, (0xb3, 0x80, 0x1, 0x7d, 0x3c, 0x55, 0x4f, 0xf4 ))

EFI_MM_RSC_HANDLER_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  EFI_STATUS_CODE_TYPE,         #   IN CodeType,
  EFI_STATUS_CODE_VALUE,        #   IN Value,
  UINT32,                       #   IN Instance,
  POINTER(EFI_GUID),            #   IN *CallerId,
  POINTER(EFI_STATUS_CODE_DATA) #   IN *Data
  )

EFI_MM_RSC_HANDLER_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_MM_RSC_HANDLER_CALLBACK   #   IN Callback
  )

EFI_MM_RSC_HANDLER_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  EFI_MM_RSC_HANDLER_CALLBACK   #   IN Callback
  )

class EFI_MM_RSC_HANDLER_PROTOCOL (Structure):
  _fields_ = [
    ("Register",                EFI_MM_RSC_HANDLER_REGISTER),
    ("UnRegister",              EFI_MM_RSC_HANDLER_UNREGISTER)
  ]

