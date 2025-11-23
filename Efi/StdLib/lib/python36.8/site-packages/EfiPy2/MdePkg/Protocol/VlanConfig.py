# VlanConfig.py
#
# EfiPy2.MdePkg.Protocol.VlanConfig
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiVlanConfigProtocolGuid  = \
  EFI_GUID (0x9e23d768, 0xd2f3, 0x4366, (0x9f, 0xc3, 0x3a, 0x7a, 0xba, 0x86, 0x43, 0x74 ))

class EFI_VLAN_CONFIG_PROTOCOL (Structure):
  pass

class EFI_VLAN_FIND_DATA (Structure):
  _fields_ = [
    ("VlanId",    UINT16),
    ("Priority",  UINT8)
  ]

EFI_VLAN_CONFIG_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VLAN_CONFIG_PROTOCOL),  # IN  *This
  UINT16,                             # IN  VlanId
  UINT8                               # IN  Priority
  )

EFI_VLAN_CONFIG_FIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VLAN_CONFIG_PROTOCOL),  # IN    *This
  UINT16,                             # IN    VlanId  OPTIONAL,
  POINTER(UINT16),                    #   OUT *NumberOfVlan,
  POINTER(POINTER(EFI_VLAN_FIND_DATA))#   OUT **Entries
  )

EFI_VLAN_CONFIG_REMOVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_VLAN_CONFIG_PROTOCOL),  # IN    *This
  UINT16                              # IN    VlanId
  )

EFI_VLAN_CONFIG_PROTOCOL._fields_ = [
    ("Set",     EFI_VLAN_CONFIG_SET),
    ("Find",    EFI_VLAN_CONFIG_FIND),
    ("Remove",  EFI_VLAN_CONFIG_REMOVE)
  ]

