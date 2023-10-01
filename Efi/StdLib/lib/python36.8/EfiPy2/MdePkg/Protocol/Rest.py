# Rest.py
#
# EfiPy2.MdePkg.Protocol.Rest
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Http import EFI_HTTP_MESSAGE

gEfiRestProtocolGuid           = \
  EFI_GUID (0x0db48a36, 0x4e54, 0xea9c, (0x9b, 0x09, 0x1e, 0xa5, 0xbe, 0x3a, 0x66, 0x0b ))

class EFI_REST_PROTOCOL (Structure):
  pass

EFI_REST_SEND_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_PROTOCOL),        # IN  *This,
  POINTER(EFI_HTTP_MESSAGE),         # IN  *RequestMessage,
  POINTER(EFI_HTTP_MESSAGE)          # OUT *ResponseMessage
  )

EFI_REST_GET_TIME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_PROTOCOL),        # IN  *This,
  POINTER(EFI_TIME)                  # OUT *Time
  )

EFI_REST_PROTOCOL._fields_ = [
    ("SendReceive",         EFI_REST_SEND_RECEIVE),
    ("GetServiceTime",      EFI_REST_GET_TIME)
  ]

