# HttpBootCallback.py
#
# EfiPy2.MdePkg.Protocol.HttpBootCallback
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiHttpBootCallbackProtocolGuid  = \
  EFI_GUID (0xba23b311, 0x343d, 0x11e6, (0x91, 0x85, 0x58, 0x20, 0xb1, 0xd6, 0x52, 0x99 ))

class EFI_HTTP_BOOT_CALLBACK_PROTOCOL (Structure):
  pass

HttpBootDhcp4                       = 1
HttpBootDhcp6                       = 2
HttpBootHttpRequest                 = 3
HttpBootHttpResponse                = 4
HttpBootHttpEntityBody              = 5
HttpBootHttpAuthInfo                = 6
HttpBootTypeMax                     = 7
EFI_HTTP_BOOT_CALLBACK_DATA_TYPE    = ENUM

EFI_HTTP_BOOT_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_BOOT_CALLBACK_PROTOCOL), #   IN  *This,
  EFI_HTTP_BOOT_CALLBACK_DATA_TYPE,         #   IN DataType,
  BOOLEAN,                                  #   IN Received,
  UINT32,                                   #   IN DataLength,
  PVOID                                     #   IN *Data   OPTIONAL
  )

EFI_HTTP_BOOT_CALLBACK_PROTOCOL._fields_ = [
    ("Callback",    EFI_HTTP_BOOT_CALLBACK)
  ]

