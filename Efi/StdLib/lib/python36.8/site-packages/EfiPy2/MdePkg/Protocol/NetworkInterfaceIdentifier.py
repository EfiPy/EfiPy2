# NetworkInterfaceIdentifier.py
#
# EfiPy2.MdePkg.Protocol.NetworkInterfaceIdentifier
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiNetworkInterfaceIdentifierProtocolGuid    = \
  EFI_GUID (0xE18541CD, 0xF755, 0x4f73, (0x92, 0x8D, 0x64, 0x3C, 0x8A, 0x79, 0xB2, 0x29 ))

gEfiNetworkInterfaceIdentifierProtocolGuid_31 = \
  EFI_GUID (0x1ACED566, 0x76ED, 0x4218, (0xBC, 0x81, 0x76, 0x7F, 0x1F, 0x97, 0x7A, 0x89 ))

EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL_REVISION    = 0x00020000

EFI_NETWORK_INTERFACE_IDENTIFIER_INTERFACE_REVISION   = EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL_REVISION

class EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL (Structure):
  pass

EFI_NETWORK_INTERFACE_IDENTIFIER_PROTOCOL._fields_ = [
    ("Revision",      UINT64),
    ("Id",            UINT64),
    ("ImageAddr",     UINT64),
    ("ImageSize",     UINT32),
    ("StringId",      CHAR8 * 4),
    ("Type",          UINT8),
    ("MajorVer",      UINT8),
    ("MinorVer",      UINT8),
    ("Ipv6Supported", BOOLEAN),
    ("IfNum",         UINT16)
  ]

EfiNetworkInterfaceUndi = 1
EFI_NETWORK_INTERFACE_TYPE  = ENUM

class undiconfig_table (Structure):
  pass

UNDI_CONFIG_TABLE = undiconfig_table

class undiconfig_table_NII_entry (Structure):
  _fields_ = [
    ("NII_InterfacePointer",  PVOID),
    ("DevicePathPointer",     PVOID)
  ]

undiconfig_table._fields_ = [
    ("NumberOfInterfaces",  UINT32),
    ("reserved",            UINT32),
    ("nextlink",            POINTER(UNDI_CONFIG_TABLE)),
    ("NII_entry",           undiconfig_table_NII_entry * 1)
  ]

