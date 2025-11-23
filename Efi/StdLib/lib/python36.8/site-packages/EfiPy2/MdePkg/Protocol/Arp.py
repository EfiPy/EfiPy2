# Arp.py
#
# EfiPy2.MdePkg.Protocol.Arp
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiArpServiceBindingProtocolGuid       = \
  EFI_GUID (0xf44c00ee, 0x1f2c, 0x4a00, (0xaa, 0x9, 0x1c, 0x9f, 0x3e, 0x8, 0x0, 0xa3 ))

gEfiArpProtocolGuid                     = \
  EFI_GUID (0xf4b427bb, 0xba21, 0x4f16, (0xbc, 0x4e, 0x43, 0xe4, 0x16, 0xab, 0x61, 0x9c ))

class EFI_ARP_PROTOCOL (Structure):
  pass

class EFI_ARP_FIND_DATA (Structure):
  _fields_ = [
    ("Size",            UINT32),
    ("DenyFlag",        BOOLEAN),
    ("StaticFlag",      BOOLEAN),
    ("HwAddressType",   UINT16),
    ("SwAddressType",   UINT16),
    ("HwAddressLength", UINT8),
    ("SwAddressLength", UINT8)
  ]

class EFI_ARP_CONFIG_DATA (Structure):
  _fields_ = [
    ("SwAddressType",   UINT16),
    ("SwAddressLength", UINT8),
    ("StationAddress",  PVOID),
    ("EntryTimeOut",    UINT32),
    ("RetryCount",      UINT32),
    ("RetryTimeOut",    UINT32)
  ]

EFI_ARP_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL),   # IN  *This
  POINTER (EFI_ARP_CONFIG_DATA) # IN  *InformationType
  )

EFI_ARP_ADD = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL), # IN  *This
  BOOLEAN,                    # IN DenyFlag,
  PVOID,                      # IN *TargetSwAddress  OPTIONAL,
  PVOID,                      # IN *TargetHwAddress  OPTIONAL,
  UINT32,                     # IN TimeoutValue,
  BOOLEAN                     # IN Overwrite
  )

EFI_ARP_FIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL),             # IN  *This
  BOOLEAN,                                # IN  BySwAddress,
  PVOID,                                  # IN  *AddressBuffer    OPTIONAL,
  POINTER (UINT32),                       # OUT *EntryLength      OPTIONAL,
  POINTER (UINT32),                       # OUT *EntryCount       OPTIONAL,
  POINTER (POINTER (EFI_ARP_FIND_DATA)),  # OUT **Entries         OPTIONAL,
  BOOLEAN                                 # IN  Refresh
  )

EFI_ARP_DELETE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL), # IN  *This
  BOOLEAN,                    # IN  BySwAddress,
  PVOID                       # IN  *AddressBuffer    OPTIONAL,
  )

EFI_ARP_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL)  # IN  *This
  )

EFI_ARP_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL), # IN  *This
  PVOID    ,                  # IN  *TargetSwAddress  OPTIONAL,
  EFI_EVENT,                  # IN  ResolvedEvent     OPTIONAL,
  PVOID                       # OUT *TargetHwAddress  
  )

EFI_ARP_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ARP_PROTOCOL), # IN  *This
  PVOID    ,                  # IN  *TargetSwAddress  OPTIONAL,
  EFI_EVENT                   # IN  ResolvedEvent     OPTIONAL,
  )

EFI_ARP_PROTOCOL._fields_ = [
    ("Configure", EFI_ARP_CONFIGURE),
    ("Add",       EFI_ARP_ADD),
    ("Find",      EFI_ARP_FIND),
    ("Delete",    EFI_ARP_DELETE),
    ("Flush",     EFI_ARP_FLUSH),
    ("Request",   EFI_ARP_REQUEST),
    ("Cancel",    EFI_ARP_CANCEL)
  ]

