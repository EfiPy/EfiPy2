# Tls.py
#
# EfiPy2.MdePkg.Protocol.Tls
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiTlsServiceBindingProtocolGuid = \
  EFI_GUID (0x952cb795, 0xff36, 0x48cf, (0xa2, 0x49, 0x4d, 0xf4, 0x86, 0xd6, 0xab, 0x8d ))

gEfiTlsProtocolGuid = \
  EFI_GUID (0xca959f, 0x6cfa, 0x4db1, (0x95, 0xbc, 0xe4, 0x6c, 0x47, 0x51, 0x43, 0x90 ))

class EFI_TLS_PROTOCOL (Structure):
  pass

EfiTlsVersion                   = 1 
EfiTlsConnectionEnd             = 2 
EfiTlsCipherList                = 3 
EfiTlsCompressionMethod         = 4 
EfiTlsExtensionData             = 5 
EfiTlsVerifyMethod              = 6 
EfiTlsSessionID                 = 7 
EfiTlsSessionState              = 8 
EfiTlsClientRandom              = 9 
EfiTlsServerRandom              = 10
EfiTlsKeyMaterial               = 11
EfiTlsVerifyHost                = 12
EfiTlsSessionDataTypeMaximum    = 13
EFI_TLS_SESSION_DATA_TYPE       = ENUM

class EFI_TLS_VERSION (Structure):
  _fields_ = [
    ("Major",   UINT8),
    ("Minor",   UINT8)
  ]

EfiTlsClient            = 1
EfiTlsServer            = 2
EFI_TLS_CONNECTION_END  = ENUM

class EFI_TLS_CIPHER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Data1",   UINT8),
    ("Data2",   UINT8)
  ]

EFI_TLS_COMPRESSION = UINT8

class EFI_TLS_EXTENSION (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExtensionType",   UINT16),
    ("Length",          UINT16),
    ("Data",            UINT8 * 1)
  ]

EFI_TLS_VERIFY = UINT32

EFI_TLS_VERIFY_NONE  = 0x0

EFI_TLS_VERIFY_PEER  = 0x1
EFI_TLS_VERIFY_FAIL_IF_NO_PEER_CERT  = 0x2

EFI_TLS_VERIFY_CLIENT_ONCE  = 0x4

EFI_TLS_VERIFY_HOST_FLAG = UINT32

EFI_TLS_VERIFY_FLAG_NONE  = 0x00

EFI_TLS_VERIFY_FLAG_ALWAYS_CHECK_SUBJECT  = 0x01

EFI_TLS_VERIFY_FLAG_NO_WILDCARDS  = 0x02

EFI_TLS_VERIFY_FLAG_NO_PARTIAL_WILDCARDS  = 0x04

EFI_TLS_VERIFY_FLAG_MULTI_LABEL_WILDCARDS  = 0x08

EFI_TLS_VERIFY_FLAG_SINGLE_LABEL_SUBDOMAINS  = 0x10

EFI_TLS_VERIFY_FLAG_NEVER_CHECK_SUBJECT  = 0x20

class EFI_TLS_VERIFY_HOST (Structure):
  _pack_   = 1
  _fields_ = [
    ("Flags",       EFI_TLS_VERIFY_HOST_FLAG),
    ("HostName",    POINTER(CHAR8))
  ]

class EFI_TLS_RANDOM (Structure):
  _pack_   = 1
  _fields_ = [
    ("GmtUnixTime", UINT32),
    ("RandomBytes", UINT8 * 28)
  ]

class EFI_TLS_MASTER_SECRET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Data",    UINT8 * 28)
  ]

MAX_TLS_SESSION_ID_LENGTH  = 32

class EFI_TLS_SESSION_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Length",  UINT16),
    ("Data",    UINT8 * MAX_TLS_SESSION_ID_LENGTH)
  ]

EfiTlsSessionNotStarted         = 1
EfiTlsSessionHandShaking        = 2
EfiTlsSessionDataTransferring   = 3
EfiTlsSessionClosing            = 4
EfiTlsSessionError              = 5
EfiTlsSessionStateMaximum       = 6
EFI_TLS_SESSION_STATE           = ENUM

class EFI_TLS_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

EfiTlsEncrypt       = 1
EfiTlsDecrypt       = 2
EFI_TLS_CRYPT_MODE  = ENUM

EFI_TLS_SET_SESSION_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TLS_PROTOCOL),      #   IN *This,
  EFI_TLS_SESSION_DATA_TYPE,      #   IN DataType,
  PVOID,                          #   IN *Data,
  UINTN                           #   IN DataSize
  )

EFI_TLS_GET_SESSION_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TLS_PROTOCOL),      #   IN     *This,
  EFI_TLS_SESSION_DATA_TYPE,      #   IN     DataType,
  PVOID,                          #   IN OUT *Data,
  POINTER(UINTN)                  #   IN OUT *DataSize
  )

EFI_TLS_BUILD_RESPONSE_PACKET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TLS_PROTOCOL),    #   IN     *This,
  POINTER(UINT8),               #   IN     *RequestBuffer  OPTIONAL,
  UINTN,                        #   IN     RequestSize  OPTIONAL,
  POINTER(UINT8),               #   OUT    *Buffer  OPTIONAL,
  POINTER(UINTN)                #   IN OUT *BufferSize
  )

EFI_TLS_PROCESS_PACKET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TLS_PROTOCOL),                #   IN     *This,
  POINTER(POINTER(EFI_TLS_FRAGMENT_DATA)),  #   IN OUT **FragmentTable,
  POINTER(UINT32),                          #   IN     *FragmentCount,
  EFI_TLS_CRYPT_MODE                        #   IN     CryptMode
  )

EFI_TLS_PROTOCOL._fields_ = [
    ("SetSessionData",      EFI_TLS_SET_SESSION_DATA),
    ("GetSessionData",      EFI_TLS_GET_SESSION_DATA),
    ("BuildResponsePacket", EFI_TLS_BUILD_RESPONSE_PACKET),
    ("ProcessPacket",       EFI_TLS_PROCESS_PACKET)
  ]

