# Dns6.py
#
# EfiPy2.MdePkg.Protocol.Dns6
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDns6ServiceBindingProtocolGuid  = \
  EFI_GUID(0x7f1647c8, 0xb76e, 0x44b2, (0xa5, 0x65, 0xf7, 0xf, 0xf1, 0x9c, 0xd1, 0x9e ))

gEfiDns6ProtocolGuid                = \
  EFI_GUID(0xca37bc1f, 0xa327, 0x4ae9, (0x82, 0x8a, 0x8c, 0x40, 0xd8, 0x50, 0x6a, 0x17 ))

class EFI_DNS6_PROTOCOL (Structure):
  pass

class EFI_DNS6_CONFIG_DATA (Structure):
  _fields_ = [
    ("EnableDnsCache",  BOOLEAN),
    ("Protocol",        UINT8),
    ("StationIp",       EFI_IPv6_ADDRESS),
    ("LocalPort",       UINT16),
    ("DnsServerCount",  UINT32),
    ("DnsServerList",   POINTER(EFI_IPv6_ADDRESS)),
    ("RetryCount",      UINT32),
    ("RetryInterval",   UINT32)
  ]

class EFI_DNS6_CACHE_ENTRY (Structure):
  _fields_ = [
    ("HostName",  PCHAR16),
    ("IpAddress", POINTER(EFI_IPv6_ADDRESS)),
    ("Timeout",   UINT32)
  ]

class EFI_DNS6_MODE_DATA (Structure):
  _fields_ = [
    ("DnsConfigData",   EFI_DNS6_CONFIG_DATA),
    ("DnsServerCount",  UINT32),
    ("DnsServerList",   POINTER(EFI_IPv6_ADDRESS)),
    ("DnsCacheCount",   UINT32),
    ("DnsCacheList",    POINTER(EFI_DNS6_CACHE_ENTRY))
  ]

class DNS6_HOST_TO_ADDR_DATA (Structure):
  _fields_ = [
    ("IpCount", UINT32),
    ("IpList",  POINTER(EFI_IPv6_ADDRESS))
  ]

class DNS6_ADDR_TO_HOST_DATA (Structure):
  _fields_ = [
    ("HostName",  PCHAR16)
  ]

class DNS6_RESOURCE_RECORD (Structure):
  _fields_ = [
    ("QName",       PCHAR8),
    ("QType",       UINT16),
    ("QClass",      UINT16),
    ("TTL",         UINT32),
    ("DataLength",  UINT16),
    ("RData",       PCHAR8)
  ]

class DNS6_GENERAL_LOOKUP_DATA (Structure):
  _fields_ = [
    ("RRCount", UINTN),
    ("RRList",  POINTER(DNS6_RESOURCE_RECORD))
  ]

class EFI_DNS6_COMPLETION_TOKEN_RspData (Union):
  _fields_ = [
    ("H2AData",     POINTER(DNS6_HOST_TO_ADDR_DATA)),
    ("A2HData",     POINTER(DNS6_ADDR_TO_HOST_DATA)),
    ("GLookupData", POINTER(DNS6_GENERAL_LOOKUP_DATA))
  ]

class EFI_DNS6_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",         EFI_EVENT),
    ("Status",        EFI_STATUS),
    ("RetryCount",    UINT32),
    ("RetryInterval", UINT32),
    ("RspData",       EFI_DNS6_COMPLETION_TOKEN_RspData)
  ]

EFI_DNS6_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL), # IN     *This
  POINTER(EFI_DNS6_MODE_DATA) #    OUT *DnsModeData
  )

EFI_DNS6_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL),   # IN  *This
  POINTER(EFI_DNS6_CONFIG_DATA) # IN  *DnsConfigData
  )

EFI_DNS6_HOST_NAME_TO_IP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL),         # IN  *This
  PCHAR16,                            # IN  *HostName
  POINTER(EFI_DNS6_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_DNS6_IP_TO_HOST_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL),         # IN  *This
  EFI_IPv6_ADDRESS,                   # IN  IpAddress
  POINTER(EFI_DNS6_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_DNS6_GENERAL_LOOKUP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL),         # IN *This
  PCHAR8,                             # IN *QName,
  UINT16,                             # IN QType,
  UINT16,                             # IN QClass,
  POINTER(EFI_DNS6_COMPLETION_TOKEN)  # IN *Token
  )

EFI_DNS6_UPDATE_DNS_CACHE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL), # IN *This
  BOOLEAN,                    # IN DeleteFlag,
  BOOLEAN,                    # IN Override,
  EFI_DNS6_CACHE_ENTRY        # IN DnsCacheEntry
  )

EFI_DNS6_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL)  # IN *This
  )

EFI_DNS6_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DNS6_PROTOCOL),         # IN *This
  POINTER(EFI_DNS6_COMPLETION_TOKEN)  # IN *Token
  )

EFI_DNS6_PROTOCOL._fields_ = [
    ("GetModeData",     EFI_DNS6_GET_MODE_DATA),
    ("Configure",       EFI_DNS6_CONFIGURE),
    ("HostNameToIp",    EFI_DNS6_HOST_NAME_TO_IP),
    ("IpToHostName",    EFI_DNS6_IP_TO_HOST_NAME),
    ("GeneralLookUp",   EFI_DNS6_GENERAL_LOOKUP),
    ("UpdateDnsCache",  EFI_DNS6_UPDATE_DNS_CACHE),
    ("Poll",            EFI_DNS6_POLL),
    ("Cancel",          EFI_DNS6_CANCEL)
  ]

