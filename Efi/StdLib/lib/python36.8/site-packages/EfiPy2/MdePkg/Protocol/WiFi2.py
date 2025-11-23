# WiFi2.py
#
# EfiPy2.MdePkg.Protocol.WiFi2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiWiFi2ProtocolGuid  = \
  EFI_GUID (0x1b0fb9bf, 0x699d, 0x4fdd, ( 0xa7, 0xc3, 0x25, 0x46, 0x68, 0x1b, 0xf6, 0x3b ))

class EFI_WIRELESS_MAC_CONNECTION_II_PROTOCOL (Structure):
  pass

IeeeInfrastructureBSS   = 1
IeeeIndependentBSS      = 2
IeeeMeshBSS             = 3
IeeeAnyBss              = 4
EFI_80211_BSS_TYPE      = ENUM

ConnectSuccess                          = 1
ConnectRefused                          = 2
ConnectFailed                           = 3
ConnectFailureTimeout                   = 4
ConnectFailedReasonUnspecified          = 5
EFI_80211_CONNECT_NETWORK_RESULT_CODE   = ENUM

class EFI_80211_MAC_ADDRESS (Structure):
  _fields_ = [
    ("Addr",    UINT8 * 6)
  ]

EFI_MAX_SSID_LEN  = 32

class EFI_80211_SSID (Structure):
  _fields_ = [
    ("SSIdLen", UINT8),
    ("SSId",    UINT8 * EFI_MAX_SSID_LEN)
  ]

class EFI_80211_GET_NETWORKS_DATA (Structure):
  _fields_ = [
    ("NumOfSSID",   UINT32),
    ("SSIDList",    EFI_80211_SSID * 1)
  ]

class EFI_80211_SUITE_SELECTOR (Structure):
  _fields_ = [
    ("Oui",         UINT8 * 3),
    ("SuiteType",   UINT8)
  ]

class EFI_80211_AKM_SUITE_SELECTOR (Structure):
  _fields_ = [
    ("AKMSuiteCount",   UINT16),
    ("AKMSuiteList",    EFI_80211_SUITE_SELECTOR * 1)
  ]

class EFI_80211_CIPHER_SUITE_SELECTOR (Structure):
  _fields_ = [
    ("CipherSuiteCount",   UINT16),
    ("CipherSuiteList",    EFI_80211_SUITE_SELECTOR * 1)
  ]

class EFI_80211_NETWORK (Structure):
  _fields_ = [
    ("BSSType",         EFI_80211_BSS_TYPE),
    ("SSId",            EFI_80211_SSID),
    ("*AKMSuite",       EFI_80211_AKM_SUITE_SELECTOR),
    ("*CipherSuite",    EFI_80211_CIPHER_SUITE_SELECTOR)
  ]

class EFI_80211_NETWORK_DESCRIPTION (Structure):
  _fields_ = [
    ("Network",         EFI_80211_NETWORK),
    ("NetworkQuality",  UINT8)
  ]

class EFI_80211_GET_NETWORKS_RESULT (Structure):
  _fields_ = [
    ("NumOfNetworkDesc",    UINT8),
    ("NetworkDesc",         EFI_80211_NETWORK_DESCRIPTION * 1)
  ]

class EFI_80211_GET_NETWORKS_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS),
    ("*Data",   EFI_80211_GET_NETWORKS_DATA),
    ("*Result", EFI_80211_GET_NETWORKS_RESULT)
  ]

class EFI_80211_CONNECT_NETWORK_DATA (Structure):
  _fields_ = [
    ("Network",         POINTER(EFI_80211_NETWORK)),
    ("FailureTimeout",  UINT32)
  ]

class EFI_80211_CONNECT_NETWORK_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS),
    ("*Data",       EFI_80211_CONNECT_NETWORK_DATA),
    ("ResultCode",  EFI_80211_CONNECT_NETWORK_RESULT_CODE)
  ]

class EFI_80211_DISCONNECT_NETWORK_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS)
  ]

EFI_WIRELESS_MAC_CONNECTION_II_GET_NETWORKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_II_PROTOCOL), # IN  *This
  POINTER(EFI_80211_GET_NETWORKS_TOKEN)             # IN  *Token
  )

EFI_WIRELESS_MAC_CONNECTION_II_CONNECT_NETWORK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_II_PROTOCOL), # IN  *This
  POINTER(EFI_80211_CONNECT_NETWORK_TOKEN)          # IN  *Token
  )

EFI_WIRELESS_MAC_CONNECTION_II_DISCONNECT_NETWORK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_II_PROTOCOL), # IN  *This
  POINTER(EFI_80211_DISCONNECT_NETWORK_TOKEN)       # IN  *Token
  )

EFI_WIRELESS_MAC_CONNECTION_II_PROTOCOL._fields_ = [
    ("GetNetworks",         EFI_WIRELESS_MAC_CONNECTION_II_GET_NETWORKS),
    ("ConnectNetwork",      EFI_WIRELESS_MAC_CONNECTION_II_CONNECT_NETWORK),
    ("DisconnectNetwork",   EFI_WIRELESS_MAC_CONNECTION_II_DISCONNECT_NETWORK)
  ]

