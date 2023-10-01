# Hash.py
#
# EfiPy2.MdePkg.Protocol.Hash
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiHashServiceBindingProtocolGuid  = \
  EFI_GUID(0x42881c98, 0xa4f3, 0x44b0, (0xa3, 0x9d, 0xdf, 0xa1, 0x86, 0x67, 0xd8, 0xcd ))

gEfiHashProtocolGuid              = \
  EFI_GUID(0xc5184932, 0xdba5, 0x46db, (0xa5, 0xba, 0xcc, 0x0b, 0xda, 0x9c, 0x14, 0x35 ))

gEfiHashAlgorithmSha1Guid         = \
  EFI_GUID(0x2ae9d80f, 0x3fb2, 0x4095, (0xb7, 0xb1, 0xe9, 0x31, 0x57, 0xb9, 0x46, 0xb6 ))

gEfiHashAlgorithmSha224Guid       = \
  EFI_GUID(0x8df01a06, 0x9bd5, 0x4bf7, (0xb0, 0x21, 0xdb, 0x4f, 0xd9, 0xcc, 0xf4, 0x5b ))

gEfiHashAlgorithmSha256Guid       = \
  EFI_GUID(0x51aa59de, 0xfdf2, 0x4ea3, (0xbc, 0x63, 0x87, 0x5f, 0xb7, 0x84, 0x2e, 0xe9 ))

gEfiHashAlgorithmSha384Guid       = \
  EFI_GUID(0xefa96432, 0xde33, 0x4dd2, (0xae, 0xe6, 0x32, 0x8c, 0x33, 0xdf, 0x77, 0x7a ))

gEfiHashAlgorithmSha512Guid       = \
  EFI_GUID(0xcaa4381e, 0x750c, 0x4770, (0xb8, 0x70, 0x7a, 0x23, 0xb4, 0xe4, 0x21, 0x30 ))

gEfiHashAlgorithmMD5Guid          = \
  EFI_GUID(0xaf7c79c, 0x65b5, 0x4319, (0xb0, 0xae, 0x44, 0xec, 0x48, 0x4e, 0x4a, 0xd7 ))

gEfiHashAlgorithmSha1NoPadGuid    = \
  EFI_GUID(0x24c5dc2f, 0x53e2, 0x40ca, (0x9e, 0xd6, 0xa5, 0xd9, 0xa4, 0x9f, 0x46, 0x3b ))

gEfiHashAlgorithmSha256NoPadGuid  = \
  EFI_GUID(0x8628752a, 0x6cb7, 0x4814, (0x96, 0xfc, 0x24, 0xa8, 0x15, 0xac, 0x22, 0x26 ))

class EFI_HASH_PROTOCOL (Structure):
  pass

EFI_MD5_HASH    = UINT8 * 16
EFI_SHA1_HASH   = UINT8 * 20
EFI_SHA224_HASH = UINT8 * 28
EFI_SHA256_HASH = UINT8 * 32
EFI_SHA384_HASH = UINT8 * 48
EFI_SHA512_HASH = UINT8 * 64

class EFI_HASH_OUTPUT (Union):
  _fields_ = [
    ("Md5Hash",     POINTER(EFI_MD5_HASH)),
    ("Sha1Hash",    POINTER(EFI_SHA1_HASH)),
    ("Sha224Hash",  POINTER(EFI_SHA224_HASH)),
    ("Sha256Hash",  POINTER(EFI_SHA256_HASH)),
    ("Sha384Hash",  POINTER(EFI_SHA384_HASH)),
    ("Sha512Hash",  POINTER(EFI_SHA512_HASH))
  ]

EFI_HASH_GET_HASH_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH_PROTOCOL), # IN  *This
  POINTER(EFI_GUID),          # IN  *HashAlgorithm
  POINTER(UINTN)              # OUT *HashSize
  )

EFI_HASH_HASH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HASH_PROTOCOL), # IN       *This
  POINTER(EFI_GUID),          # IN CONST *HashAlgorithm,
  BOOLEAN,                    # IN       Extend,
  POINTER(UINT8),             # IN CONST *Message,
  UINT64,                     # IN       MessageSize,
  POINTER(EFI_HASH_OUTPUT)    # IN OUT   *Hash
  )

EFI_HASH_PROTOCOL._fields_ = [
  ("GetHashSize", EFI_HASH_GET_HASH_SIZE),
  ("Hash",        EFI_HASH_HASH)
  ]

