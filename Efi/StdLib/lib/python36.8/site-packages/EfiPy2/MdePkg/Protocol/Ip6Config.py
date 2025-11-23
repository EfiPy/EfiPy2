# Ip6Config.py
#
# EfiPy2.MdePkg.Protocol.Ip6Config
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import Ip6

gEfiIp6ConfigProtocolGuid = \
  EFI_GUID (0x937fe521, 0x95ae, 0x4d1a, (0x89, 0x29, 0x48, 0xbc, 0xd9, 0x0a, 0xd3, 0x1a ))

class EFI_IP6_CONFIG_PROTOCOL (Structure):
  pass

Ip6ConfigDataTypeInterfaceInfo           = 0
Ip6ConfigDataTypeAltInterfaceId          = 1
Ip6ConfigDataTypePolicy                  = 2
Ip6ConfigDataTypeDupAddrDetectTransmits  = 3
Ip6ConfigDataTypeManualAddress           = 4
Ip6ConfigDataTypeGateway                 = 5
Ip6ConfigDataTypeDnsServer               = 6
Ip6ConfigDataTypeMaximum                 = 7
EFI_IP6_CONFIG_DATA_TYPE                 = ENUM

class EFI_IP6_CONFIG_INTERFACE_INFO (Structure):
  _fields_ = [
    ("Name",              CHAR16 * 32),
    ("IfType",            UINT8),
    ("HwAddressSize",     UINT32),
    ("HwAddress",         EFI_MAC_ADDRESS),
    ("AddressInfoCount",  UINT32),
    ("AddressInfo",       POINTER(Ip6.EFI_IP6_ADDRESS_INFO)),
    ("RouteCount",        UINT32),
    ("RouteTable",        POINTER(Ip6.EFI_IP6_ROUTE_TABLE))
  ]

class EFI_IP6_CONFIG_INTERFACE_ID (Structure):
  _fields_ = [
    ("Id",  UINT8 * 8)
  ]

Ip6ConfigPolicyManual       = 0
Ip6ConfigPolicyAutomatic    = 1
EFI_IP6_CONFIG_POLICY       = ENUM

class EFI_IP6_CONFIG_DUP_ADDR_DETECT_TRANSMITS (Structure):
  _fields_ = [
    ("DupAddrDetectTransmits",  UINT32)
  ]

class EFI_IP6_CONFIG_MANUAL_ADDRESS (Structure):
  _fields_ = [
    ("Address",       EFI_IPv6_ADDRESS),
    ("IsAnycast",     BOOLEAN),
    ("PrefixLength",  UINT8)
  ]

EFI_IP6_CONFIG_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_CONFIG_PROTOCOL), # IN *This
  EFI_IP6_CONFIG_DATA_TYPE,         # IN DataType
  UINTN,                            # IN DataSize
  PVOID                             # IN *Data
  )

EFI_IP6_CONFIG_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_CONFIG_PROTOCOL), # IN      *This
  EFI_IP6_CONFIG_DATA_TYPE,         # IN      DataType
  POINTER(UINTN),                   # IN OUT  *DataSize,
  PVOID                             # IN      *Data   OPTIONAL
  )

EFI_IP6_CONFIG_REGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_CONFIG_PROTOCOL), # IN *This
  EFI_IP6_CONFIG_DATA_TYPE,         # IN DataType,
  EFI_EVENT                         # IN Event
  )

EFI_IP6_CONFIG_UNREGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_CONFIG_PROTOCOL), # IN *This
  EFI_IP6_CONFIG_DATA_TYPE,         # IN DataType,
  EFI_EVENT                         # IN Event
  )

EFI_IP6_CONFIG_PROTOCOL._fields_ = [
    ("SetData",               EFI_IP6_CONFIG_SET_DATA),
    ("GetData",               EFI_IP6_CONFIG_GET_DATA),
    ("RegisterDataNotify",    EFI_IP6_CONFIG_REGISTER_NOTIFY),
    ("UnregisterDataNotify",  EFI_IP6_CONFIG_UNREGISTER_NOTIFY)
  ]

