# Dns4.py
#
# EfiPy2.MdePkg.Protocol.Dns4
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDns4ServiceBindingProtocolGuid  = \
  EFI_GUID (0xb625b186, 0xe063, 0x44f7, (0x89, 0x5, 0x6a, 0x74, 0xdc, 0x6f, 0x52, 0xb4 ))

gEfiDns4ProtocolGuid                = \
  EFI_GUID (0xae3d28cc, 0xe05b, 0x4fa1, (0xa0, 0x11, 0x7e, 0xb5, 0x5a, 0x3f, 0x14, 0x1 ))

class EFI_DNS4_PROTOCOL (Structure):
  pass

class EFI_DNS4_CONFIG_DATA (Structure):
  _fields_ = [
    ("DnsServerListCount",  UINTN),
    ("DnsServerList",       POINTER(EFI_IPv4_ADDRESS)),
    ("UseDefaultSetting",   BOOLEAN),
    ("EnableDnsCache",      BOOLEAN),
    ("Protocol",            UINT8),
    ("StationIp",           EFI_IPv4_ADDRESS),
    ("SubnetMask",          EFI_IPv4_ADDRESS),
    ("LocalPort",           UINT16),
    ("RetryCount",          UINT32),
    ("RetryInterval",       UINT32)
  ]

class EFI_DNS4_CACHE_ENTRY (Structure):
  _fields_ = [
    ("HostName",  PCHAR16),
    ("IpAddress", POINTER(EFI_IPv4_ADDRESS)),
    ("Timeout",   UINT32)
  ]

class EFI_DNS4_MODE_DATA (Structure):
  _fields_ = [
    ("DnsConfigData",   EFI_DNS4_CONFIG_DATA),
    ("DnsServerCount",  UINT32),
    ("DnsServerList",   POINTER(EFI_IPv4_ADDRESS)),
    ("DnsCacheCount",   UINT32),
    ("DnsCacheList",    POINTER(EFI_DNS4_CACHE_ENTRY))
  ]

class DNS_HOST_TO_ADDR_DATA (Structure):
  _fields_ = [
    ("IpCount", UINT32),
    ("IpList",  POINTER(EFI_IPv4_ADDRESS))
  ]

class DNS_ADDR_TO_HOST_DATA (Structure):
  _fields_ = [
    ("HostName",  PCHAR16)
  ]

class DNS_RESOURCE_RECORD (Structure):
  _fields_ = [
    ("QName",       PCHAR8),
    ("QType",       UINT16),
    ("QClass",      UINT16),
    ("TTL",         UINT32),
    ("DataLength",  UINT16),
    ("RData",       PCHAR8)
  ]

class DNS_GENERAL_LOOKUP_DATA (Structure):
  _fields_ = [
    ("RRCount", UINTN),
    ("RRList",  POINTER(DNS_RESOURCE_RECORD))
  ]

class EFI_DNS4_COMPLETION_TOKEN_RspData (Union):
  _fields_ = [
    ("H2AData",     POINTER(DNS_HOST_TO_ADDR_DATA)),
    ("A2HData",     POINTER(DNS_ADDR_TO_HOST_DATA)),
    ("GLookupData", POINTER(DNS_GENERAL_LOOKUP_DATA))
  ]

class EFI_DNS4_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",         EFI_EVENT),
    ("Status",        EFI_STATUS),
    ("RetryCount",    UINT32),
    ("RetryInterval", UINT32),
    ("RspData",       EFI_DNS4_COMPLETION_TOKEN_RspData)
  ]

EFI_DNS4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL), # IN     *This
  POINTER(EFI_DNS4_MODE_DATA) #    OUT *DnsModeData
  )

EFI_DNS4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL),   # IN  *This
  POINTER(EFI_DNS4_CONFIG_DATA) # IN  *DnsConfigData
  )

EFI_DNS4_HOST_NAME_TO_IP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL),         # IN  *This
  PCHAR16,                            # IN  *HostName
  POINTER(EFI_DNS4_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_DNS4_IP_TO_HOST_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL),         # IN  *This
  EFI_IPv4_ADDRESS,                   # IN  IpAddress
  POINTER(EFI_DNS4_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_DNS4_GENERAL_LOOKUP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL),         # IN *This
  PCHAR8,                             # IN *QName,
  UINT16,                             # IN QType,
  UINT16,                             # IN QClass,
  POINTER(EFI_DNS4_COMPLETION_TOKEN)  # IN *Token
  )

EFI_DNS4_UPDATE_DNS_CACHE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL), # IN *This
  BOOLEAN,                    # IN DeleteFlag,
  BOOLEAN,                    # IN Override,
  EFI_DNS4_CACHE_ENTRY        # IN DnsCacheEntry
  )

EFI_DNS4_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL)  # IN *This
  )

EFI_DNS4_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS4_PROTOCOL),         # IN *This
  POINTER(EFI_DNS4_COMPLETION_TOKEN)  # IN *Token
  )

EFI_DNS4_PROTOCOL._fields_ = [
    ("GetModeData",     EFI_DNS4_GET_MODE_DATA),
    ("Configure",       EFI_DNS4_CONFIGURE),
    ("HostNameToIp",    EFI_DNS4_HOST_NAME_TO_IP),
    ("IpToHostName",    EFI_DNS4_IP_TO_HOST_NAME),
    ("GeneralLookUp",   EFI_DNS4_GENERAL_LOOKUP),
    ("UpdateDnsCache",  EFI_DNS4_UPDATE_DNS_CACHE),
    ("Poll",            EFI_DNS4_POLL),
    ("Cancel",          EFI_DNS4_CANCEL)
  ]

