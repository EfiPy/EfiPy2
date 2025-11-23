# Pkcs7Verify.py
#
# EfiPy2.MdePkg.Protocol.Pkcs7Verify
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Guid.ImageAuthentication import EFI_SIGNATURE_LIST

gEfiPkcs7VerifyProtocolGuid = \
  EFI_GUID (0x47889fb2, 0xd671, 0x4fab, (0xa0, 0xca, 0xdf, 0x0e, 0x44, 0xdf, 0x70, 0xd6 ))

class EFI_PKCS7_VERIFY_PROTOCOL (Structure):
  pass

EFI_PKCS7_VERIFY_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PKCS7_VERIFY_PROTOCOL),                       # IN      *This
  PVOID,                                                    # IN      *SignedData,
  UINTN,                                                    # IN      SignedDataSize,
  PVOID,                                                    # IN      *InData          OPTIONAL,
  UINTN,                                                    # IN      InDataSize,
  POINTER(POINTER(EFI_SIGNATURE_LIST)), # IN      **AllowedDb,
  POINTER(POINTER(EFI_SIGNATURE_LIST)), # IN      **RevokedDb      OPTIONAL,
  POINTER(POINTER(EFI_SIGNATURE_LIST)), # IN      **TimeStampDb    OPTIONAL,
  PVOID,                                                    # OUT     *Content         OPTIONAL,
  POINTER(UINTN)                                            # IN OUT  *ContentSize
  )

EFI_PKCS7_VERIFY_SIGNATURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PKCS7_VERIFY_PROTOCOL),                       # IN *This
  PVOID,                                                    # IN *Signature,
  UINTN,                                                    # IN SignatureSize,
  PVOID,                                                    # IN *InHash,
  UINTN,                                                    # IN InHashSize,
  POINTER(POINTER(EFI_SIGNATURE_LIST)), # IN **AllowedDb,
  POINTER(POINTER(EFI_SIGNATURE_LIST)), # IN **RevokedDb       OPTIONAL,
  POINTER(POINTER(EFI_SIGNATURE_LIST))  # IN **TimeStampDb     OPTIONAL
  )

EFI_PKCS7_VERIFY_PROTOCOL._fields_ = [
  ("VerifyBuffer",    EFI_PKCS7_VERIFY_BUFFER),
  ("VerifySignature", EFI_PKCS7_VERIFY_SIGNATURE)
  ]

