# WinCertificate.py
#
# EfiPy2.MdePkg.Guid.WinCertificate
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.Uefi.UefiBaseType   import *
from EfiPy2.MdePkg.Uefi.UefiSpec       import *

WIN_CERT_TYPE_PKCS_SIGNED_DATA = 0x0002
WIN_CERT_TYPE_EFI_PKCS115      = 0x0EF0
WIN_CERT_TYPE_EFI_GUID         = 0x0EF1

class WIN_CERTIFICATE (Structure):
  _fields_ = [
    ("dwLength",          UINT32),
    ("wRevision",         UINT16),
    ("wCertificateType",  UINT16)
    # ("bCertificate",      UINT8 * ANYSIZE_ARRAY)
  ]

gEfiCertTypeRsa2048Sha256Guid = \
  EFI_GUID (0xa7717414, 0xc616, 0x4977, (0x94, 0x20, 0x84, 0x47, 0x12, 0xa7, 0x35, 0xbf ))

class EFI_CERT_BLOCK_RSA_2048_SHA256 (Structure):
  _fields_ = [
    ("HashType",  EFI_GUID),
    ("PublicKey", UINT8 * 256),
    ("Signature", UINT8 * 256)
  ]

class WIN_CERTIFICATE_UEFI_GUID (Structure):
  _fields_ = [
    ("Hdr",       WIN_CERTIFICATE),
    ("CertType",  EFI_GUID),
    ("CertData",  UINT8 * 1)
  ]

class WIN_CERTIFICATE_EFI_PKCS1_15 (Structure):
  _fields_ = [
    ("Hdr",           WIN_CERTIFICATE),
    ("HashAlgorithm", EFI_GUID),
    # ("Signature",     UINT8 * N)
  ]

