# Rng.py
#
# EfiPy2.MdePkg.Protocol.Rng
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiRngProtocolGuid                 = \
  EFI_GUID (0x3152bca5, 0xeade, 0x433d, (0x86, 0x2e, 0xc0, 0x1c, 0xdc, 0x29, 0x1f, 0x44 ))

class EFI_RNG_PROTOCOL (Structure):
  pass

EFI_RNG_ALGORITHM = EFI_GUID

gEfiRngAlgorithmSp80090Hash256Guid  = \
  EFI_GUID (0xa7af67cb, 0x603b, 0x4d42, (0xba, 0x21, 0x70, 0xbf, 0xb6, 0x29, 0x3f, 0x96 ))

gEfiRngAlgorithmSp80090Hmac256Guid  = \
  EFI_GUID (0xc5149b43, 0xae85, 0x4f53, (0x99, 0x82, 0xb9, 0x43, 0x35, 0xd3, 0xa9, 0xe7 ))

gEfiRngAlgorithmSp80090Ctr256Guid   = \
  EFI_GUID (0x44f0de6e, 0x4d8c, 0x4045, (0xa8, 0xc7, 0x4d, 0xd1, 0x68, 0x85, 0x6b, 0x9e ))

gEfiRngAlgorithmX9313DesGuid        = \
  EFI_GUID (0x63c4785a, 0xca34, 0x4012, (0xa3, 0xc8, 0x0b, 0x6a, 0x32, 0x4f, 0x55, 0x46 ))

gEfiRngAlgorithmX931AesGuid         = \
  EFI_GUID (0xacd03321, 0x777e, 0x4d3d, (0xb1, 0xc8, 0x20, 0xcf, 0xd8, 0x88, 0x20, 0xc9 ))

gEfiRngAlgorithmRaw                 = \
  EFI_GUID (0xe43176d7, 0xb6e8, 0x4827, (0xb7, 0x84, 0x7f, 0xfd, 0xc4, 0xb6, 0x85, 0x61 ))

EFI_RNG_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_RNG_PROTOCOL),            # IN      *This
  POINTER(UINTN),                       # IN OUT  *RNGAlgorithmListSize,
  POINTER(EFI_RNG_ALGORITHM)            # OUT     *RNGAlgorithmList
  )

EFI_RNG_GET_RNG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_RNG_PROTOCOL),    # IN  *This
  POINTER(EFI_RNG_ALGORITHM),   # IN  *RNGAlgorithm, OPTIONAL
  UINTN,                        # IN  RNGValueLength,
  POINTER(UINT8)                # OUT *RNGValue
  )

EFI_RNG_PROTOCOL._fields_ = [
  ("GetInfo", EFI_RNG_GET_INFO),
  ("GetRNG",  EFI_RNG_GET_RNG)
  ]

