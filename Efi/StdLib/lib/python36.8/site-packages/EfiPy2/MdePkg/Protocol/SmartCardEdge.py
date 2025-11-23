# SmartCardEdge.py
#
# EfiPy2.MdePkg.Protocol.SmartCardEdge
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSmartCardEdgeProtocolGuid   = \
  EFI_GUID (0xd317f29b, 0xa325, 0x4712, (0x9b, 0xf1, 0xc6, 0x19, 0x54, 0xdc, 0x19, 0x8c))

class EFI_SMART_CARD_EDGE_PROTOCOL (Structure):
  pass

SCARD_AID_MAXSIZE                        = 0x0010
SCARD_CSN_SIZE                           = 0x0010
SMART_CARD_EDGE_PROTOCOL_VERSION_1       = 0x00000100

SMART_CARD_AID  = UINT8 * SCARD_AID_MAXSIZE
SMART_CARD_CSN  = UINT8 * SCARD_CSN_SIZE

SC_EDGE_TAG_HEADER              = 0x0000
SC_EDGE_TAG_CERT                = 0x0001
SC_EDGE_TAG_KEY_ID              = 0x0002
SC_EDGE_TAG_KEY_TYPE            = 0x0003
SC_EDGE_TAG_KEY_SIZE            = 0x0004

SC_EDGE_L_SIZE_HEADER           = 1
SC_EDGE_L_SIZE_CERT             = 2
SC_EDGE_L_SIZE_KEY_ID           = 1
SC_EDGE_L_SIZE_KEY_TYPE         = 1
SC_EDGE_L_SIZE_KEY_SIZE         = 2

SC_EDGE_L_VALUE_HEADER          = 1
SC_EDGE_L_VALUE_KEY_ID          = 1
SC_EDGE_L_VALUE_KEY_TYPE        = 1
SC_EDGE_L_VALUE_KEY_SIZE        = 2

SC_EDGE_RSA_EXCHANGE            = 0x01
SC_EDGE_RSA_SIGNATURE           = 0x02
SC_EDGE_ECDSA_256               = 0x03
SC_EDGE_ECDSA_384               = 0x04
SC_EDGE_ECDSA_521               = 0x05
SC_EDGE_ECDH_256                = 0x06
SC_EDGE_ECDH_384                = 0x07
SC_EDGE_ECDH_521                = 0x08

gEfiPaddingRsassaPkcs1V1P5Guid          = \
  EFI_GUID (0x9317ec24, 0x7cb0, 0x4d0e, (0x8b, 0x32, 0x2e, 0xd9, 0x20, 0x9c, 0xd8, 0xaf))

gEfiPaddingRsassaPssGuid          = \
  EFI_GUID (0x7b2349e0, 0x522d, 0x4f8e, (0xb9, 0x27, 0x69, 0xd9, 0x7c, 0x9e, 0x79, 0x5f))

gEfiPaddingNoneGuid          = \
  EFI_GUID (0x3629ddb1, 0x228c, 0x452e, (0xb6, 0x16, 0x09, 0xed, 0x31, 0x6a, 0x97, 0x00))

gEfiPaddingRsaesPkcs1V1P5Guid          = \
  EFI_GUID (0xe1c1d0a9, 0x40b1, 0x4632, (0xbd, 0xcc, 0xd9, 0xd6, 0xe5, 0x29, 0x56, 0x31))

gEfiPaddingRsaesOaepGuid          = \
  EFI_GUID (0xc1e63ac4, 0xd0cf, 0x4ce6, (0x83, 0x5b, 0xee, 0xd0, 0xe6, 0xa8, 0xa4, 0x5b))

EFI_SMART_CARD_EDGE_GET_CONTEXT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  POINTER(UINTN),                         #    OUT  *NumberAidSupported,
  POINTER(UINTN),                         # IN OUT  *AidTableSize OPTIONAL,
  POINTER(SMART_CARD_AID),                #    OUT  *AidTable OPTIONAL,
  POINTER(UINTN),                         #    OUT  *NumberSCPresent,
  POINTER(UINTN),                         # IN OUT  *CsnTableSize OPTIONAL,
  POINTER(SMART_CARD_CSN),                #    OUT  *CsnTable OPTIONAL,
  POINTER(UINT32)                         #    OUT  *VersionScEdgeProtocol OPTIONAL
  )

EFI_SMART_CARD_EDGE_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  POINTER(EFI_HANDLE),                    #    OUT  *SCardHandle,
  POINTER(UINT8),                         # IN      *ScardCsn OPTIONAL,
  POINTER(UINT8)                          #    OUT  *ScardAid OPTIONAL
  )

EFI_SMART_CARD_EDGE_DISCONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE                              # IN      SCardHandle
  )

EFI_SMART_CARD_EDGE_GET_CSN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  UINT8 * SCARD_CSN_SIZE                  #     OUT Csn[SCARD_CSN_SIZE]
  )

EFI_SMART_CARD_EDGE_GET_READER_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  POINTER(UINTN),                         # IN OUT  *ReaderNameLength,
  PCHAR16                                 #    OUT  *ReaderName OPTIONAL
  )

EFI_SMART_CARD_EDGE_VERIFY_PIN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  INT32,                                  # IN      PinSize,
  POINTER(UINT8),                         # IN      *PinCode,
  POINTER(BOOLEAN),                       #    OUT  *PinResult,
  POINTER(UINT32)                         #    OUT  *RemainingAttempts OPTIONAL
  )

EFI_SMART_CARD_EDGE_GET_PIN_REMAINING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  POINTER(UINT32)                         #    OUT  *RemainingAttempts
  )

EFI_SMART_CARD_EDGE_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  POINTER(EFI_GUID),                      # IN      *DataId,
  POINTER(UINTN),                         # IN OUT  *DataSize,
  PVOID                                   #    OUT  *Data OPTIONAL
  )

EFI_SMART_CARD_EDGE_GET_CREDENTIAL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  POINTER(UINTN),                         # IN OUT  *CredentialSize,
  POINTER(UINT8)                          #    OUT  *CredentialList OPTIONAL
  )

EFI_SMART_CARD_EDGE_SIGN_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  UINTN,                                  # IN      KeyId,
  UINTN,                                  # IN      KeyType,
  POINTER(EFI_GUID),                      # IN      *HashAlgorithm,
  POINTER(EFI_GUID),                      # IN      *PaddingMethod,
  POINTER(UINT8),                         # IN      *HashedData,
  POINTER(UINT8)                          #    OUT  *SignatureData
  )

EFI_SMART_CARD_EDGE_DECRYPT_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  UINTN,                                  # IN      KeyId,
  POINTER(EFI_GUID),                      # IN      *HashAlgorithm,
  POINTER(EFI_GUID),                      # IN      *PaddingMethod,
  UINTN,                                  # IN      EncryptedSize,
  POINTER(UINT8),                         # IN      *EncryptedData,
  POINTER(UINTN),                         # IN OUT  *PlaintextSize,
  POINTER(UINT8)                          #    OUT  *PlaintextData
  )

EFI_SMART_CARD_EDGE_BUILD_DH_AGREEMENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMART_CARD_EDGE_PROTOCOL),  # IN      *This
  EFI_HANDLE,                             # IN      SCardHandle,
  UINTN,                                  # IN      KeyId,
  POINTER(UINT8),                         # IN      *dataQx,
  POINTER(UINT8),                         # IN      *dataQy,
  POINTER(UINT8)                          #    OUT  *DHAgreement
  )

EFI_SMART_CARD_EDGE_PROTOCOL._fields_ = [
    ("GetContext",        EFI_SMART_CARD_EDGE_GET_CONTEXT),
    ("Connect",           EFI_SMART_CARD_EDGE_CONNECT),
    ("Disconnect",        EFI_SMART_CARD_EDGE_DISCONNECT),
    ("GetCsn",            EFI_SMART_CARD_EDGE_GET_CSN),
    ("GetReaderName",     EFI_SMART_CARD_EDGE_GET_READER_NAME),
    ("VerifyPin",         EFI_SMART_CARD_EDGE_VERIFY_PIN),
    ("GetPinRemaining",   EFI_SMART_CARD_EDGE_GET_PIN_REMAINING),
    ("GetData",           EFI_SMART_CARD_EDGE_GET_DATA),
    ("GetCredential",     EFI_SMART_CARD_EDGE_GET_CREDENTIAL),
    ("SignData",          EFI_SMART_CARD_EDGE_SIGN_DATA),
    ("DecryptData",       EFI_SMART_CARD_EDGE_DECRYPT_DATA),
    ("BuildDHAgreement",  EFI_SMART_CARD_EDGE_BUILD_DH_AGREEMENT)
  ]

