# Eap.py
#
# EfiPy2.MdePkg.Protocol.Eap
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiEapProtocolGuid   = \
  EFI_GUID (0x5d9f96db, 0xe731, 0x4caa, (0xa0, 0xd, 0x72, 0xe1, 0x87, 0xcd, 0x77, 0x62 ))

class EFI_EAP_PROTOCOL (Structure):
  pass

EFI_PORT_HANDLE = PVOID

EFI_EAP_TYPE_TLS = 13

EFI_EAP_TYPE_MD5                = 4
EFI_EAP_TYPE_OTP                = 5
EFI_EAP_TYPE_TOKEN_CARD         = 6

EFI_EAP_BUILD_RESPONSE_PACKET = CFUNCTYPE (
  EFI_STATUS,
  EFI_PORT_HANDLE,  # IN     PortNumber,
  POINTER(UINT8),   # IN     *RequestBuffer, 
  UINTN,            # IN     RequestSize, 
  POINTER(UINT8),   # IN     *Buffer, 
  POINTER(UINTN)    # IN OUT *BufferSize
  )

EFI_EAP_SET_DESIRED_AUTHENTICATION_METHOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_PROTOCOL),  # IN  *This, 
  UINT8                       # IN  EapAuthType 
  )

EFI_EAP_REGISTER_AUTHENTICATION_METHOD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_PROTOCOL),    # IN  *This, 
  UINT8,                        # IN  EapAuthType 
  EFI_EAP_BUILD_RESPONSE_PACKET # IN  Handler 
  )

EFI_EAP_PROTOCOL._fields_ = [
    ("SetDesiredAuthMethod",  EFI_EAP_SET_DESIRED_AUTHENTICATION_METHOD),
    ("RegisterAuthMethod",    EFI_EAP_REGISTER_AUTHENTICATION_METHOD)
  ]

