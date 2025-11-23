# Hash2.py
#
# EfiPy2.MdePkg.Protocol.Hash2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiHash2ServiceBindingProtocolGuid = \
  EFI_GUID (0xda836f8d, 0x217f, 0x4ca0, ( 0x99, 0xc2, 0x1c, 0xa4, 0xe1, 0x60, 0x77, 0xea ))

gEfiHash2ProtocolGuid               = \
  EFI_GUID (0x55b1d734, 0xc5e1, 0x49db, ( 0x96, 0x47, 0xb1, 0x6a, 0xfb, 0xe, 0x30, 0x5b ))

from EfiPy2.MdePkg.Protocol import Hash

class EFI_HASH2_PROTOCOL (Structure):
  pass

EFI_MD5_HASH2     = UINT8 * 16
EFI_SHA1_HASH2    = UINT8 * 20
EFI_SHA224_HASH2  = UINT8 * 28
EFI_SHA256_HASH2  = UINT8 * 32
EFI_SHA384_HASH2  = UINT8 * 48
EFI_SHA512_HASH2  = UINT8 * 64

class EFI_HASH2_OUTPUT (Union):
  _fields_ = [
    ("Md5Hash",     POINTER(EFI_MD5_HASH2)),
    ("Sha1Hash",    POINTER(EFI_SHA1_HASH2)),
    ("Sha224Hash",  POINTER(EFI_SHA224_HASH2)),
    ("Sha256Hash",  POINTER(EFI_SHA256_HASH2)),
    ("Sha384Hash",  POINTER(EFI_SHA384_HASH2)),
    ("Sha512Hash",  POINTER(EFI_SHA512_HASH2)),
  ]

EFI_HASH2_GET_HASH_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH2_PROTOCOL),  # IN  *This
  POINTER(EFI_GUID),            # IN  *HashAlgorithm
  POINTER(UINTN)                # OUT *HashSize
  )

EFI_HASH2_HASH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH2_PROTOCOL),  # IN       *This
  POINTER(EFI_GUID),            # IN CONST *HashAlgorithm,
  POINTER(UINT8),               # IN CONST *Message,
  UINTN,                        # IN       MessageSize,
  POINTER(EFI_HASH2_OUTPUT)     # IN OUT   *Hash
  )

EFI_HASH2_HASH_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH2_PROTOCOL),  # IN CONST *This
  POINTER(EFI_GUID)             # IN CONST *HashAlgorithm,
  )

EFI_HASH2_HASH_UPDATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH2_PROTOCOL),  # IN CONST *This
  POINTER(UINT8),               # IN CONST *Message,
  UINTN                         # IN        MessageSize
  )

EFI_HASH2_HASH_FINAL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH2_PROTOCOL),  # IN CONST *This
  POINTER(EFI_HASH2_OUTPUT)     # IN OUT   *Hash
  )

EFI_HASH2_PROTOCOL._fields_ = [
  ("GetHashSize", EFI_HASH2_GET_HASH_SIZE),
  ("Hash",        EFI_HASH2_HASH),
  ("HashInit",    EFI_HASH2_HASH_INIT),
  ("HashUpdate",  EFI_HASH2_HASH_UPDATE),
  ("HashFinal",   EFI_HASH2_HASH_FINAL)
  ]

