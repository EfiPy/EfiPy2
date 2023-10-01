# Supplicant.py
#
# EfiPy2.MdePkg.Protocol.Supplicant
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.WiFi2 import EFI_80211_MAC_ADDRESS, EFI_80211_SUITE_SELECTOR

gEfiSupplicantServiceBindingProtocolGuid    = \
  EFI_GUID (0x45bcd98e, 0x59ad, 0x4174, ( 0x95, 0x46, 0x34, 0x4a, 0x7, 0x48, 0x58, 0x98 ))

gEfiSupplicantProtocolGuid    = \
  EFI_GUID (0x54fcc43e, 0xaa89, 0x4333, ( 0x9a, 0x85, 0xcd, 0xea, 0x24, 0x5, 0x1e, 0x9e ))

class EFI_SUPPLICANT_PROTOCOL (Structure):
  pass
EfiSupplicantEncrypt        = 1
EfiSupplicantDecrypt        = 2
EFI_SUPPLICANT_CRYPT_MODE   = ENUM

EfiSupplicant80211AKMSuite                      = 1 
EfiSupplicant80211GroupDataCipherSuite          = 2 
EfiSupplicant80211PairwiseCipherSuite           = 3 
EfiSupplicant80211PskPassword                   = 4 
EfiSupplicant80211TargetSSIDName                = 5 
EfiSupplicant80211StationMac                    = 6 
EfiSupplicant80211TargetSSIDMac                 = 7 
EfiSupplicant80211PTK                           = 8 
EfiSupplicant80211GTK                           = 9 
EfiSupplicantState                              = 10
EfiSupplicant80211LinkState                     = 11
EfiSupplicantKeyRefresh                         = 12
EfiSupplicant80211SupportedAKMSuites            = 13
EfiSupplicant80211SupportedSoftwareCipherSuites = 14
EfiSupplicant80211SupportedHardwareCipherSuites = 15
EfiSupplicant80211IGTK                          = 16
EfiSupplicant80211PMK                           = 17
EfiSupplicantDataTypeMaximum                    = 18
EFI_SUPPLICANT_DATA_TYPE                        = ENUM

Ieee80211UnauthenticatedUnassociated    = 1
Ieee80211AuthenticatedUnassociated      = 2
Ieee80211PendingRSNAuthentication       = 3
Ieee80211AuthenticatedAssociated        = 4
EFI_80211_LINK_STATE                    = ENUM

Group                   = 1
Pairwise                = 2
PeerKey                 = 3
IGTK                    = 4
EFI_SUPPLICANT_KEY_TYPE = ENUM

Receive                         = 1
Transmit                        = 2
Both                            = 3
EFI_SUPPLICANT_KEY_DIRECTION    = ENUM

class EFI_SUPPLICANT_KEY_REFRESH (Structure):
  _fields_ = [
    ("GTKRefresh", BOOLEAN)
  ]

EFI_MAX_KEY_LEN  = 64

class EFI_SUPPLICANT_KEY (Structure):
  _fields_ = [
    ("Key",             UINT8 * EFI_MAX_KEY_LEN),
    ("KeyLen",          UINT8),
    ("KeyId",           UINT8),
    ("KeyType",         EFI_SUPPLICANT_KEY_TYPE),
    ("Addr",            EFI_80211_MAC_ADDRESS),
    ("Rsc",             UINT8 * 8),
    ("RscLen",          UINT8),
    ("IsAuthenticator", BOOLEAN),
    ("CipherSuite",     EFI_80211_SUITE_SELECTOR),
    ("Direction",       EFI_SUPPLICANT_KEY_DIRECTION)
  ]

class EFI_SUPPLICANT_KEY (Structure):
  _fields_ = [
    ("GTKCount",    UINT8),
    ("GTKList",     EFI_SUPPLICANT_KEY * 1)
  ]

class EFI_SUPPLICANT_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

EFI_SUPPLICANT_BUILD_RESPONSE_PACKET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SUPPLICANT_PROTOCOL), #   IN      *This
  POINTER(UINT8),                   #   IN      *RequestBuffer      OPTIONAL,
  UINTN,                            #   IN      RequestBufferSize   OPTIONAL,
  POINTER(UINT8),                   #   OUT     *Buffer,
  POINTER(UINTN)                    #   IN OUT  *BufferSize
  )

EFI_SUPPLICANT_PROCESS_PACKET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SUPPLICANT_PROTOCOL),                 #   IN     *This
  POINTER(POINTER(EFI_SUPPLICANT_FRAGMENT_DATA)),   #   IN OUT **FragmentTable,
  POINTER(UINT32),                                  #   IN     *FragmentCount,
  EFI_SUPPLICANT_CRYPT_MODE                         #   IN     CryptMode
  )

EFI_SUPPLICANT_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SUPPLICANT_PROTOCOL), #   IN      *This
  EFI_SUPPLICANT_DATA_TYPE,         #   IN      DataType,
  PVOID,                            #   IN      *Data,
  UINTN                             #   IN      DataSize
  )

EFI_SUPPLICANT_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SUPPLICANT_PROTOCOL), #   IN      *This
  EFI_SUPPLICANT_DATA_TYPE,         #   IN      DataType,
  POINTER(UINT8),                   #   OUT     *Data      OPTIONAL,
  POINTER(UINTN)                    #   IN      *DataSize
  )

EFI_SUPPLICANT_PROTOCOL._fields_ = [
    ("BuildResponsePacket", EFI_SUPPLICANT_BUILD_RESPONSE_PACKET),
    ("ProcessPacket",       EFI_SUPPLICANT_PROCESS_PACKET),
    ("SetData",             EFI_SUPPLICANT_SET_DATA),
    ("GetData",             EFI_SUPPLICANT_GET_DATA)
  ]

