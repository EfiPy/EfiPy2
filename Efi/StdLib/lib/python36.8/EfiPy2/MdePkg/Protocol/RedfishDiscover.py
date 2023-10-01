# RedfishDiscover.py
#
# EfiPy2.MdePkg.Protocol.RedfishDiscover
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiRedfishDiscoverProtocolGuid       = \
  EFI_GUID (0x5db12509, 0x4550, 0x4347, ( 0x96, 0xb3, 0x73, 0xc0, 0xff, 0x6e, 0x86, 0x9f ))

REDFISH_DISCOVER_TOKEN_SIGNATURE  = SIGNATURE_32 ('R', 'F', 'T', 'S')

EFI_REDFISH_DISCOVER_FLAG = UINT32

EFI_REDFISH_DISCOVER_HOST_INTERFACE  = 0x00000001 # Discover Redfish server reported in SMBIOS 42h.
EFI_REDFISH_DISCOVER_SSDP            = 0x00000002 # Discover Redfish server using UPnP Http search method.
EFI_REDFISH_DISCOVER_SSDP_UDP6       = 0x00000004 # Use UDP version 6.
EFI_REDFISH_DISCOVER_KEEP_ALIVE      = 0x00000008 # Keep to send UPnP Search in the duration indicated in

EFI_REDFISH_DISCOVER_RENEW  = 0x00000010

EFI_REDFISH_DISCOVER_VALIDATION     = 0x80000000
EFI_REDFISH_DISCOVER_DURATION_MASK  = 0x0f000000

class EFI_REDFISH_DISCOVER_PROTOCOL (Structure):
  pass

class EFI_REDFISH_DISCOVERED_INFORMATION (Structure):
  _fields_ = [
    ("RedfishRestExHandle",     EFI_HANDLE),
    ("IsUdp6",                  BOOLEAN),
    ("RedfishHostIpAddress",    EFI_IP_ADDRESS),
    ("RedfishVersion",          UINTN),
    ("Location",                POINTER(CHAR16)),
    ("Uuid",                    POINTER(CHAR16)),
    ("Os",                      POINTER(CHAR16)),
    ("OsVersion",               POINTER(CHAR16)),
    ("Product",                 POINTER(CHAR16)),
    ("ProductVer",              POINTER(CHAR16)),
    ("UseHttps",                BOOLEAN)
  ]

class EFI_REDFISH_DISCOVERED_INSTANCE (Structure):
  _fields_ = [
    ("Status",      EFI_STATUS),
    ("Information", EFI_REDFISH_DISCOVERED_INFORMATION)
  ]

class EFI_REDFISH_DISCOVERED_LIST (Structure):
  _fields_ = [
    ("NumberOfServiceFound",    EFI_REDFISH_DISCOVERED_INSTANCE),
    ("RedfishInstances",        POINTER(EFI_REDFISH_DISCOVERED_INSTANCE))
  ]

class EFI_REDFISH_DISCOVER_NETWORK_INTERFACE (Structure):
  _fields_ = [
    ("MacAddress",          EFI_MAC_ADDRESS),
    ("IsIpv6",              BOOLEAN),
    ("SubnetId",            EFI_IP_ADDRESS),
    ("SubnetPrefixLength",  UINT8),
    ("VlanId",              UINT16)
  ]

class EFI_REDFISH_DISCOVERED_TOKEN (Structure):
  _fields_ = [
    ("Signature",       UINT32),
    ("DiscoverList",    EFI_REDFISH_DISCOVERED_LIST),
    ("Event",           EFI_EVENT),
    ("Timeout",         UINTN)
  ]

EFI_REDFISH_DISCOVER_NETWORK_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REDFISH_DISCOVER_PROTOCOL),                   #   IN  *This
  EFI_HANDLE,                                               #   IN  ImageHandle,
  POINTER(UINTN),                                           #   OUT *NumberOfNetworkInterfaces,
  POINTER(POINTER(EFI_REDFISH_DISCOVER_NETWORK_INTERFACE))  #   OUT **NetworkInterfaces
  )

EFI_REDFISH_DISCOVER_ACQUIRE_SERVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REDFISH_DISCOVER_PROTOCOL),           #   IN  *This
  EFI_HANDLE,                                       #   IN  ImageHandle,
  POINTER(EFI_REDFISH_DISCOVER_NETWORK_INTERFACE),  #   IN  *TargetNetworkInterface OPTIONAL,
  EFI_REDFISH_DISCOVER_FLAG,                        #   IN  Flags,
  POINTER(EFI_REDFISH_DISCOVERED_TOKEN)             #   IN  *Token
  )

EFI_REDFISH_DISCOVER_ABORT_ACQUIRE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REDFISH_DISCOVER_PROTOCOL),           #   IN  *This
  POINTER(EFI_REDFISH_DISCOVER_NETWORK_INTERFACE)   #   IN  *TargetNetworkInterface OPTIONAL,
  )

EFI_REDFISH_DISCOVER_RELEASE_SERVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REDFISH_DISCOVER_PROTOCOL),   #   IN  *This
  POINTER(EFI_REDFISH_DISCOVERED_LIST)      #   IN  *List OPTIONAL,
  )

EFI_REDFISH_DISCOVER_PROTOCOL._fields_ = [
    ("GetNetworkInterfaceList",     EFI_REDFISH_DISCOVER_NETWORK_LIST),
    ("AcquireRedfishService",       EFI_REDFISH_DISCOVER_ACQUIRE_SERVICE),
    ("AbortAcquireRedfishService",  EFI_REDFISH_DISCOVER_ABORT_ACQUIRE),
    ("ReleaseRedfishService",       EFI_REDFISH_DISCOVER_RELEASE_SERVICE)
  ]

