# AdapterInformation.py
#
# EfiPy2.MdePkg.Protocol.AdapterInformation
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiAdapterInformationProtocolGuid      = \
  EFI_GUID (0xE5DD1403, 0xD622, 0xC24E, (0x84, 0x88, 0xC7, 0x1B, 0x17, 0xF5, 0xE8, 0x02 ))

gEfiAdapterInfoMediaStateGuid           = \
  EFI_GUID (0xD7C74207, 0xA831, 0x4A26, (0xB1, 0xF5, 0xD1, 0x93, 0x06, 0x5C, 0xE8, 0xB6 ))

gEfiAdapterInfoNetworkBootGuid          = \
  EFI_GUID (0x1FBD2960, 0x4130, 0x41E5, (0x94, 0xAC, 0xD2, 0xCF, 0x03, 0x7F, 0xB3, 0x7C ))

gEfiAdapterInfoSanMacAddressGuid        = \
  EFI_GUID (0x114da5ef, 0x2cf1, 0x4e12, (0x9b, 0xbb, 0xc4, 0x70, 0xb5, 0x52, 0x5, 0xd9 ))

gEfiAdapterInfoUndiIpv6SupportGuid      = \
  EFI_GUID (0x4bd56be3, 0x4975, 0x4d8a, (0xa0, 0xad, 0xc4, 0x91, 0x20, 0x4b, 0x5d, 0x4d))

EFI_ADAPTER_INFO_MEDIA_TYPE_GUID        = \
  EFI_GUID (0x8484472f, 0x71ec, 0x411a, ( 0xb3, 0x9c, 0x62, 0xcd, 0x94, 0xd9, 0x91, 0x6e))

class EFI_ADAPTER_INFORMATION_PROTOCOL (Structure):
  pass

class EFI_ADAPTER_INFO_MEDIA_STATE (Structure):
  _fields_ = [
    ("MediaState",  EFI_STATUS),
  ]

class EFI_ADAPTER_INFO_MEDIA_TYPE (Structure):
  _fields_ = [
    ("MediaType",   UINT8)
  ]

class EFI_ADAPTER_INFO_NETWORK_BOOT (Structure):
  _fields_ = [
    ("iScsiIpv4BootCapablity",  BOOLEAN),
    ("iScsiIpv6BootCapablity",  BOOLEAN),
    ("FCoeBootCapablity",       BOOLEAN),
    ("OffloadCapability",       BOOLEAN),
    ("iScsiMpioCapability",     BOOLEAN),
    ("iScsiIpv4Boot",           BOOLEAN),
    ("iScsiIpv6Boot",           BOOLEAN),
    ("FCoeBoot",                BOOLEAN)
  ]

class EFI_ADAPTER_INFO_SAN_MAC_ADDRESS (Structure):
  _fields_ = [
    ("SanMacAddress", EFI_MAC_ADDRESS)
  ]

class EFI_ADAPTER_INFO_UNDI_IPV6_SUPPORT (Structure):
  _fields_ = [
    ("Ipv6Support", BOOLEAN)
  ]

EFI_ADAPTER_INFO_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ADAPTER_INFORMATION_PROTOCOL), # IN  *This
  POINTER (EFI_GUID),                         # IN  *InformationType
  POINTER (PVOID),                            # OUT **InformationBlock
  POINTER (UINTN)                             # OUT *InformationBlockSize
  )

EFI_ADAPTER_INFO_SET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ADAPTER_INFORMATION_PROTOCOL), # IN  *This
  POINTER (EFI_GUID),                         # IN  *InformationType
  PVOID,                                      # IN  *InformationBlock
  UINTN                                       # IN  InformationBlockSize
  )

EFI_ADAPTER_INFO_GET_SUPPORTED_TYPES = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ADAPTER_INFORMATION_PROTOCOL), # IN  *This
  POINTER (POINTER (EFI_GUID)),               # OUT **InfoTypesBuffer
  POINTER (UINTN)                             # OUT *InfoTypesBufferCount
  )

EFI_ADAPTER_INFORMATION_PROTOCOL._fields_ = [
    ("GetInformation",    EFI_ADAPTER_INFO_GET_INFO),
    ("SetInformation",    EFI_ADAPTER_INFO_SET_INFO),
    ("GetSupportedTypes", EFI_ADAPTER_INFO_GET_SUPPORTED_TYPES)
  ]

