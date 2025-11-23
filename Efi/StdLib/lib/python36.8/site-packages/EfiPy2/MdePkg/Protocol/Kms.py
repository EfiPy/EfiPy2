# Kms.py
#
# EfiPy2.MdePkg.Protocol.Kms
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiKmsProtocolGuid = \
  EFI_GUID (0xEC3A978D, 0x7C4E, 0x48FA, (0x9A, 0xBE, 0x6A, 0xD9, 0x1C, 0xC8, 0xF8, 0x11 ))

class EFI_KMS_PROTOCOL (Structure):
  pass

EFI_KMS_DATA_TYPE_NONE      = 0
EFI_KMS_DATA_TYPE_BINARY    = 1
EFI_KMS_DATA_TYPE_ASCII     = 2
EFI_KMS_DATA_TYPE_UNICODE   = 4
EFI_KMS_DATA_TYPE_UTF8      = 8

gEfiKmsFormatGeneric128Guid     = \
  EFI_GUID (0xec8a3d69, 0x6ddf, 0x4108, (0x94, 0x76, 0x73, 0x37, 0xfc, 0x52, 0x21, 0x36 ))
gEfiKmsFormatGeneric160Guid     = \
  EFI_GUID (0xa3b3e6f8, 0xefca, 0x4bc1, (0x88, 0xfb, 0xcb, 0x87, 0x33, 0x9b, 0x25, 0x79 ))
gEfiKmsFormatGeneric256Guid     = \
  EFI_GUID (0x70f64793, 0xc323, 0x4261, (0xac, 0x2c, 0xd8, 0x76, 0xf2, 0x7c, 0x53, 0x45 ))
gEfiKmsFormatGeneric512Guid     = \
  EFI_GUID (0x978fe043, 0xd7af, 0x422e, (0x8a, 0x92, 0x2b, 0x48, 0xe4, 0x63, 0xbd, 0xe6 ))
gEfiKmsFormatGeneric1024Guid    = \
  EFI_GUID (0x43be0b44, 0x874b, 0x4ead, (0xb0, 0x9c, 0x24, 0x1a, 0x4f, 0xbd, 0x7e, 0xb3 ))
gEfiKmsFormatGeneric2048Guid    = \
  EFI_GUID (0x40093f23, 0x630c, 0x4626, (0x9c, 0x48, 0x40, 0x37, 0x3b, 0x19, 0xcb, 0xbe ))
gEfiKmsFormatGeneric3072Guid    = \
  EFI_GUID (0xb9237513, 0x6c44, 0x4411, (0xa9, 0x90, 0x21, 0xe5, 0x56, 0xe0, 0x5a, 0xde ))
EFI_KMS_FORMAT_GENERIC_DYNAMIC_GUID    = \
  EFI_GUID (0x2156e996, 0x66de, 0x4b27, (0x9c, 0xc9, 0xb0, 0x9f, 0xac, 0x4d, 0x2, 0xbe ))

gEfiKmsFormatMd2128Guid         = \
  EFI_GUID (0x78be11c4, 0xee44, 0x4a22, (0x9f, 0x05, 0x03, 0x85, 0x2e, 0xc5, 0xc9, 0x78 ))
gEfiKmsFormatMdc2128Guid        = \
  EFI_GUID (0xf7ad60f8, 0xefa8, 0x44a3, (0x91, 0x13, 0x23, 0x1f, 0x39, 0x9e, 0xb4, 0xc7 ))
gEfiKmsFormatMd4128Guid         = \
  EFI_GUID (0xd1c17aa1, 0xcac5, 0x400f, (0xbe, 0x17, 0xe2, 0xa2, 0xae, 0x06, 0x67, 0x7c ))
gEfiKmsFormatMdc4128Guid        = \
  EFI_GUID (0x3fa4f847, 0xd8eb, 0x4df4, (0xbd, 0x49, 0x10, 0x3a, 0x0a, 0x84, 0x7b, 0xbc ))
gEfiKmsFormatMd5128Guid         = \
  EFI_GUID (0xdcbc3662, 0x9cda, 0x4b52, (0xa0, 0x4c, 0x82, 0xeb, 0x1d, 0x23, 0x48, 0xc7 ))
gEfiKmsFormatMd5sha128Guid      = \
  EFI_GUID (0x1c178237, 0x6897, 0x459e, (0x9d, 0x36, 0x67, 0xce, 0x8e, 0xf9, 0x4f, 0x76 ))
gEfiKmsFormatSha1160Guid        = \
  EFI_GUID (0x453c5e5a, 0x482d, 0x43f0, (0x87, 0xc9, 0x59, 0x41, 0xf3, 0xa3, 0x8a, 0xc2 ))
gEfiKmsFormatSha256256Guid      = \
  EFI_GUID (0x6bb4f5cd, 0x8022, 0x448d, (0xbc, 0x6d, 0x77, 0x1b, 0xae, 0x93, 0x5f, 0xc6 ))
gEfiKmsFormatSha512512Guid      = \
  EFI_GUID (0x2f240e12, 0xe14d, 0x475c, (0x83, 0xb0, 0xef, 0xff, 0x22, 0xd7, 0x7b, 0xe7 ))

gEfiKmsFormatAesxts128Guid      = \
  EFI_GUID (0x4776e33f, 0xdb47, 0x479a, (0xa2, 0x5f, 0xa1, 0xcd, 0x0a, 0xfa, 0xb3, 0x8b ))
gEfiKmsFormatAesxts256Guid      = \
  EFI_GUID (0xdc7e8613, 0xc4bb, 0x4db0, (0x84, 0x62, 0x13, 0x51, 0x13, 0x57, 0xab, 0xe2 ))
gEfiKmsFormatAescbc128Guid      = \
  EFI_GUID (0xa0e8ee6a, 0x0e92, 0x44d4, (0x86, 0x1b, 0x0e, 0xaa, 0x4a, 0xca, 0x44, 0xa2 ))
gEfiKmsFormatAescbc256Guid      = \
  EFI_GUID (0xd7e69789, 0x1f68, 0x45e8, (0x96, 0xef, 0x3b, 0x64, 0x07, 0xa5, 0xb2, 0xdc ))
gEfiKmsFormatRsasha11024Guid    = \
  EFI_GUID (0x56417bed, 0x6bbe, 0x4882, (0x86, 0xa0, 0x3a, 0xe8, 0xbb, 0x17, 0xf8, 0xf9 ))
gEfiKmsFormatRsasha12048Guid    = \
  EFI_GUID (0xf66447d4, 0x75a6, 0x463e, (0xa8, 0x19, 0x07, 0x7f, 0x2d, 0xda, 0x05, 0xe9 ))
gEfiKmsFormatRsasha2562048Guid  = \
  EFI_GUID (0xa477af13, 0x877d, 0x4060, (0xba, 0xa1, 0x25, 0xd1, 0xbe, 0xa0, 0x8a, 0xd3 ))
gEfiKmsFormatRsasha2563072Guid  = \
  EFI_GUID (0x4e1356c2,  0xeed, 0x463f, (0x81, 0x47, 0x99, 0x33, 0xab, 0xdb, 0xc7, 0xd5 ))

EFI_KMS_ATTRIBUTE_TYPE_NONE             = 0x00
EFI_KMS_ATTRIBUTE_TYPE_INTEGER          = 0x01
EFI_KMS_ATTRIBUTE_TYPE_LONG_INTEGER     = 0x02
EFI_KMS_ATTRIBUTE_TYPE_BIG_INTEGER      = 0x03
EFI_KMS_ATTRIBUTE_TYPE_ENUMERATION      = 0x04
EFI_KMS_ATTRIBUTE_TYPE_BOOLEAN          = 0x05
EFI_KMS_ATTRIBUTE_TYPE_BYTE_STRING      = 0x06
EFI_KMS_ATTRIBUTE_TYPE_TEXT_STRING      = 0x07
EFI_KMS_ATTRIBUTE_TYPE_DATE_TIME        = 0x08
EFI_KMS_ATTRIBUTE_TYPE_INTERVAL         = 0x09
EFI_KMS_ATTRIBUTE_TYPE_STRUCTURE        = 0x0A
EFI_KMS_ATTRIBUTE_TYPE_DYNAMIC          = 0x0B

class EFI_KMS_FORMAT_GENERIC_DYNAMIC (Structure):
  _fields_ = [
    ("KeySize",     UINT32),
    ("KeyData",     UINT8 * 1)
  ]

class EFI_KMS_CLIENT_INFO (Structure):
  _fields_ = [
    ("ClientIdSize",    UINT16),
    ("ClientId",        PVOID),
    ("ClientNameType",  UINT8),
    ("ClientNameCount", UINT8),
    ("ClientName",      PVOID)
  ]

class EFI_KMS_KEY_DESCRIPTOR (Structure):
  _fields_ = [
    ("KeyIdentifierSize", UINT8),
    ("KeyIdentifier",     PVOID),
    ("KeyFormat",         EFI_GUID),
    ("KeyValue",          PVOID),
    ("KeyStatus",         EFI_STATUS)
  ]

class EFI_KMS_DYNAMIC_FIELD (Structure):
  _fields_ = [
    ("Tag",               UINT16),
    ("Type",              UINT16),
    ("Length",            UINT32),
    ("KeyAttributeData",  UINT8 * 1)
  ]

class EFI_KMS_DYNAMIC_ATTRIBUTE (Structure):
  _fields_ = [
    ("FieldCount",  UINT32),
    ("Field",       EFI_KMS_DYNAMIC_FIELD * 1)
  ]

class EFI_KMS_KEY_ATTRIBUTE (Structure):
  _fields_ = [
    ("KeyAttributeIdentifierType",  UINT8),
    ("KeyAttributeIdentifierCount", UINT8),
    ("KeyAttributeIdentifier",      PVOID),
    ("KeyAttributeInstance",        UINT16),
    ("KeyAttributeType",            UINT16),
    ("KeyAttributeValueSize",       UINT16),
    ("KeyAttributeValue",           PVOID),
    ("KeyAttributeStatus",          EFI_STATUS)
  ]

EFI_KMS_GET_SERVICE_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL)        # IN *This
  )

EFI_KMS_REGISTER_CLIENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),       # IN     *This
  POINTER(EFI_KMS_CLIENT_INFO),    # IN     *Client,
  POINTER(UINTN),                  # IN OUT *ClientDataSize OPTIONAL,
  POINTER(PVOID)                   # IN OUT **ClientData OPTIONAL
  )

EFI_KMS_CREATE_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN     *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN     *Client,
  POINTER(UINT16),                # IN OUT *KeyDescriptorCount,
  POINTER(EFI_KMS_KEY_DESCRIPTOR),# IN OUT *KeyDescriptors,
  POINTER(UINTN),                 # IN OUT *ClientDataSize OPTIONAL,
  POINTER(PVOID)                  # IN OUT **ClientData OPTIONAL
  )

EFI_KMS_GET_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN     *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN     *Client,
  POINTER(UINT16),                # IN OUT *KeyDescriptorCount,
  POINTER(EFI_KMS_KEY_DESCRIPTOR),# IN OUT *KeyDescriptors,
  POINTER(UINTN),                 # IN OUT *ClientDataSize OPTIONAL,
  POINTER(PVOID)                  # IN OUT **ClientData OPTIONAL
  )

EFI_KMS_ADD_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN     *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN     *Client,
  POINTER(UINT16),                # IN OUT *KeyDescriptorCount,
  POINTER(EFI_KMS_KEY_DESCRIPTOR),# IN OUT *KeyDescriptors,
  POINTER(UINTN),                 # IN OUT *ClientDataSize OPTIONAL,
  POINTER(PVOID)                  # IN OUT **ClientData OPTIONAL
  )

EFI_KMS_DELETE_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN     *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN     *Client,
  POINTER(UINT16),                # IN OUT *KeyDescriptorCount,
  POINTER(EFI_KMS_KEY_DESCRIPTOR),# IN OUT *KeyDescriptors,
  POINTER(UINTN),                 # IN OUT *ClientDataSize OPTIONAL,
  POINTER(PVOID)                  # IN OUT **ClientData OPTIONAL
  )

EFI_KMS_GET_KEY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN        *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN        *Client,
  POINTER(UINT8),                 # IN        *KeyIdentifierSize,
  PVOID,                          # IN CONST  *KeyIdentifier,
  POINTER(UINT16),                # IN OUT    *KeyAttributesCount,
  POINTER(EFI_KMS_KEY_ATTRIBUTE), # IN OUT    *KeyAttributes,
  POINTER(UINTN),                 # IN OUT    *ClientDataSize OPTIONAL,
  POINTER(PVOID),                 # IN OUT    **ClientData OPTIONAL
  )

EFI_KMS_ADD_KEY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN        *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN        *Client,
  POINTER(UINT8),                 # IN        *KeyIdentifierSize,
  PVOID,                          # IN CONST  *KeyIdentifier,
  POINTER(UINT16),                # IN OUT    *KeyAttributesCount,
  POINTER(EFI_KMS_KEY_ATTRIBUTE), # IN OUT    *KeyAttributes,
  POINTER(UINTN),                 # IN OUT    *ClientDataSize OPTIONAL,
  POINTER(PVOID),                 # IN OUT    **ClientData OPTIONAL
  )

EFI_KMS_DELETE_KEY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),      # IN        *This
  POINTER(EFI_KMS_CLIENT_INFO),   # IN        *Client,
  POINTER(UINT8),                 # IN        *KeyIdentifierSize,
  PVOID,                          # IN CONST  *KeyIdentifier,
  POINTER(UINT16),                # IN OUT    *KeyAttributesCount,
  POINTER(EFI_KMS_KEY_ATTRIBUTE), # IN OUT    *KeyAttributes,
  POINTER(UINTN),                 # IN OUT    *ClientDataSize OPTIONAL,
  POINTER(PVOID),                 # IN OUT    **ClientData OPTIONAL
  )

EFI_KMS_GET_KEY_BY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KMS_PROTOCOL),        # IN     *This
  POINTER(EFI_KMS_CLIENT_INFO),     # IN     *Client,
  POINTER(UINTN),                   # IN OUT *KeyAttributeCount,
  POINTER(EFI_KMS_KEY_ATTRIBUTE),   # IN OUT *KeyAttributes,
  POINTER(UINTN),                   # IN OUT *KeyDescriptorCount,
  POINTER(EFI_KMS_KEY_DESCRIPTOR),  # IN OUT *KeyDescriptors,
  POINTER(UINTN),                   # IN OUT *ClientDataSize OPTIONAL,
  POINTER(PVOID)                    # IN OUT **ClientData OPTIONAL
  )

EFI_KMS_PROTOCOL._fields_ = [
    ("GetServiceStatus",          EFI_KMS_GET_SERVICE_STATUS),
    ("RegisterClient",            EFI_KMS_REGISTER_CLIENT),
    ("CreateKey",                 EFI_KMS_CREATE_KEY),
    ("GetKey",                    EFI_KMS_GET_KEY),
    ("AddKey",                    EFI_KMS_ADD_KEY),
    ("DeleteKey",                 EFI_KMS_DELETE_KEY),
    ("GetKeyAttributes",          EFI_KMS_GET_KEY_ATTRIBUTES),
    ("AddKeyAttributes",          EFI_KMS_ADD_KEY_ATTRIBUTES),
    ("DeleteKeyAttributes",       EFI_KMS_DELETE_KEY_ATTRIBUTES),
    ("GetKeyByAttributes",        EFI_KMS_GET_KEY_BY_ATTRIBUTES),
    ("ProtocolVersion",           UINT32),
    ("ServiceId",                 EFI_GUID),
    ("ServiceName",               PCHAR16),
    ("ServiceVersion",            UINT32),
    ("ServiceAvailable",          BOOLEAN),
    ("ClientIdSupported",         BOOLEAN),
    ("ClientIdRequired",          BOOLEAN),
    ("ClientIdMaxSize",           UINT16),
    ("ClientNameStringTypes",     UINT8),
    ("ClientNameRequired",        BOOLEAN),
    ("ClientNameMaxCount",        UINT16),
    ("ClientDataSupported",       BOOLEAN),
    ("ClientDataMaxSize",         UINTN),
    ("KeyIdVariableLenSupported", BOOLEAN),
    ("KeyIdMaxSize",              UINTN),
    ("KeyFormatsCount",           UINTN),
    ("KeyFormats",                POINTER(EFI_GUID)),
    ("KeyAttributesSupported",    BOOLEAN),
    ("KeyAttributeIdStringTypes", UINT8),
    ("KeyAttributeIdMaxCount",    UINT16),
    ("KeyAttributesCount",        UINTN),
    ("KeyAttributes",             POINTER(EFI_KMS_KEY_ATTRIBUTE))
  ]

