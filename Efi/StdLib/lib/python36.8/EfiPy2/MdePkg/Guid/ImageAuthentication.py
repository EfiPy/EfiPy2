# ImageAuthentication.py
#
# EfiPy2.MdePkg.Guid.ImageAuthentication
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Guid     import GlobalVariable
from EfiPy2.MdePkg.Protocol import Hash

gEfiImageSecurityDatabaseGuid  = \
  EFI_GUID (0xd719b2cb, 0x3d3a, 0x4596, ( 0xa3, 0xbc, 0xda, 0xd0, 0xe, 0x67, 0x65, 0x6f ))

EFI_IMAGE_SECURITY_DATABASE  = "db"

EFI_IMAGE_SECURITY_DATABASE1  = "dbx"

EFI_IMAGE_SECURITY_DATABASE2  = "dbt"

SECURE_BOOT_MODE_ENABLE   = 1
SECURE_BOOT_MODE_DISABLE  = 0

SETUP_MODE  = 1
USER_MODE   = 0

class EFI_SIGNATURE_DATA (Structure):
  _pack_   = 1
  _fields_ = [
      ("SignatureOwner",  EFI_GUID),
      ("SignatureData",   UINT8 * 1)
    ]

class EFI_SIGNATURE_LIST (Structure):
  _pack_   = 1
  _fields_ = [
      ("SignatureType",       EFI_GUID),
      ("SignatureListSize",   UINT32),
      ("SignatureHeaderSize", UINT32),
      ("SignatureSize",       UINT32),
      # ("Signatures",         (EFI_SIGNATURE_DATA  * SignatureSize) * N)
    ]

class EFI_CERT_X509_SHA256 (Structure):
  _pack_   = 1
  _fields_ = [
      ("ToBeSignedHash",    Hash.EFI_SHA256_HASH),
      ("TimeOfRevocation",  EFI_TIME)
    ]

class EFI_CERT_X509_SHA384 (Structure):
  _pack_   = 1
  _fields_ = [
      ("ToBeSignedHash",    Hash.EFI_SHA384_HASH),
      ("TimeOfRevocation",  EFI_TIME)
    ]

class EFI_CERT_X509_SHA512 (Structure):
  _pack_   = 1
  _fields_ = [
      ("ToBeSignedHash",    Hash.EFI_SHA512_HASH),
      ("TimeOfRevocation",  EFI_TIME)
    ]

gEfiCertSha256Guid            = \
  EFI_GUID(0xc1c41626, 0x504c, 0x4092, (0xac, 0xa9, 0x41, 0xf9, 0x36, 0x93, 0x43, 0x28))

gEfiCertRsa2048Guid           = \
  EFI_GUID(0x3c5766e8, 0x269c, 0x4e34, (0xaa, 0x14, 0xed, 0x77, 0x6e, 0x85, 0xb3, 0xb6))

gEfiCertRsa2048Sha256Guid     = \
  EFI_GUID(0xe2b36190, 0x879b, 0x4a3d, (0xad, 0x8d, 0xf2, 0xe7, 0xbb, 0xa3, 0x27, 0x84))

gEfiCertSha1Guid              = \
  EFI_GUID(0x826ca512, 0xcf10, 0x4ac9, (0xb1, 0x87, 0xbe, 0x1, 0x49, 0x66, 0x31, 0xbd))

gEfiCertRsa2048Sha1Guid       = \
  EFI_GUID(0x67f8444f, 0x8743, 0x48f1, (0xa3, 0x28, 0x1e, 0xaa, 0xb8, 0x73, 0x60, 0x80))

gEfiCertX509Guid              = \
  EFI_GUID(0xa5c059a1, 0x94e4, 0x4aa7, (0x87, 0xb5, 0xab, 0x15, 0x5c, 0x2b, 0xf0, 0x72))

gEfiCertSha224Guid            = \
  EFI_GUID(0xb6e5233, 0xa65c, 0x44c9, (0x94, 0x7, 0xd9, 0xab, 0x83, 0xbf, 0xc8, 0xbd))

gEfiCertSha384Guid            = \
  EFI_GUID(0xff3e5307, 0x9fd0, 0x48c9, (0x85, 0xf1, 0x8a, 0xd5, 0x6c, 0x70, 0x1e, 0x1))

gEfiCertSha512Guid            = \
  EFI_GUID(0x93e0fae, 0xa6c4, 0x4f50, (0x9f, 0x1b, 0xd4, 0x1e, 0x2b, 0x89, 0xc1, 0x9a))

gEfiCertX509Sha256Guid        = \
  EFI_GUID(0x3bd2a492, 0x96c0, 0x4079, (0xb4, 0x20, 0xfc, 0xf9, 0x8e, 0xf1, 0x03, 0xed ))

gEfiCertX509Sha384Guid        = \
  EFI_GUID(0x7076876e, 0x80c2, 0x4ee6, (0xaa, 0xd2, 0x28, 0xb3, 0x49, 0xa6, 0x86, 0x5b ))

gEfiCertX509Sha512Guid        = \
  EFI_GUID(0x446dbf63, 0x2502, 0x4cda, (0xbc, 0xfa, 0x24, 0x65, 0xd2, 0xb0, 0xfe, 0x9d ))

gEfiCertPkcs7Guid             = \
  EFI_GUID(0x4aafd29d, 0x68df, 0x49ee, (0x8a, 0xa9, 0x34, 0x7d, 0x37, 0x56, 0x65, 0xa7))

EFI_IMAGE_EXECUTION_ACTION              = UINT32

EFI_IMAGE_EXECUTION_AUTHENTICATION      = 0x00000007
EFI_IMAGE_EXECUTION_AUTH_UNTESTED       = 0x00000000
EFI_IMAGE_EXECUTION_AUTH_SIG_FAILED     = 0x00000001
EFI_IMAGE_EXECUTION_AUTH_SIG_PASSED     = 0x00000002
EFI_IMAGE_EXECUTION_AUTH_SIG_NOT_FOUND  = 0x00000003
EFI_IMAGE_EXECUTION_AUTH_SIG_FOUND      = 0x00000004
EFI_IMAGE_EXECUTION_POLICY_FAILED       = 0x00000005
EFI_IMAGE_EXECUTION_INITIALIZED         = 0x00000008

class EFI_IMAGE_EXECUTION_INFO (Structure):
  _fields_ = [
    ("Action",      EFI_IMAGE_EXECUTION_ACTION),
    ("InfoSize",    UINT32)
    # ("Name",        CHAR16 * N),
    # ("DevicePath",  EFI_DEVICE_PATH_PROTOCOL),
    # ("Signature",   EFI_SIGNATURE_LIST)
  ]

class EFI_IMAGE_EXECUTION_INFO_TABLE (Structure):
  _fields_ = [
    ("NumberOfImages",    UINTN)
    # ("InformationInfo", EFI_IMAGE_EXECUTION_INFO * N)
  ]

