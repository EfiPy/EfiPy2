# Security.py
#
# EfiPy2.MdePkg.Protocol.Security
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSecurityArchProtocolGuid  = \
  EFI_GUID (0xA46423E3, 0x4617, 0x49f1, (0xB9, 0xFF, 0xD1, 0xBF, 0xA9, 0x11, 0x58, 0x39 ))

class EFI_SECURITY_ARCH_PROTOCOL (Structure):
  pass

EFI_SECURITY_FILE_AUTHENTICATION_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECURITY_ARCH_PROTOCOL),    # IN        *This
  UINT32,                                 # IN        AuthenticationStatus,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)       # IN  CONST *File
  )

EFI_SECURITY_ARCH_PROTOCOL._fields_ = [
    ("FileAuthenticationState", EFI_SECURITY_FILE_AUTHENTICATION_STATE),
  ]

