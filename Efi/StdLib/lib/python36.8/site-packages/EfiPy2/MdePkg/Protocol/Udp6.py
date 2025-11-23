# Udp6.py
#
# EfiPy2.MdePkg.Protocol.Udp6
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Ip6             import EFI_IP6_MODE_DATA
from EfiPy2.MdePkg.Protocol.ManagedNetwork  import EFI_MANAGED_NETWORK_CONFIG_DATA
from EfiPy2.MdePkg.Protocol.SimpleNetwork   import EFI_SIMPLE_NETWORK_MODE

gEfiUdp6ServiceBindingProtocolGuid  = \
  EFI_GUID (0x66ed4721, 0x3c98, 0x4d3e, (0x81, 0xe3, 0xd0, 0x3d, 0xd3, 0x9a, 0x72, 0x54 ))

gEfiUdp6ProtocolGuid                = \
  EFI_GUID (0x4f948815, 0xb4b9, 0x43cb, (0x8a, 0x33, 0x90, 0xe0, 0x60, 0xb3, 0x49, 0x55 ))

class EFI_UDP6_SERVICE_POINT (Structure):
  _fields_ = [
    ("InstanceHandle",EFI_HANDLE),
    ("LocalAddress",  EFI_IPv6_ADDRESS),
    ("LocalPort",     UINT16),
    ("RemoteAddress", EFI_IPv6_ADDRESS),
    ("RemotePort",    UINT16)
  ]

class EFI_UDP6_VARIABLE_DATA (Structure):
  _fields_ = [
    ("DriverHandle",  EFI_HANDLE),
    ("ServiceCount",  UINT32),
    ("Services",      EFI_UDP6_SERVICE_POINT * 1)
  ]

class EFI_UDP6_PROTOCOL (Structure):
  pass

class EFI_UDP6_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_UDP6_SESSION_DATA (Structure):
  _fields_ = [
    ("SourceAddress",       EFI_IPv6_ADDRESS),
    ("SourcePort",          UINT16),
    ("DestinationAddress",  EFI_IPv6_ADDRESS),
    ("DestinationPort",     UINT16)
  ]

class EFI_UDP6_CONFIG_DATA (Structure):
  _fields_ = [
    ("AcceptPromiscuous",   BOOLEAN),
    ("AcceptAnyPort",       BOOLEAN),
    ("AllowDuplicatePort",  BOOLEAN),
    ("TrafficClass",        UINT8),
    ("HopLimit",            UINT8),
    ("ReceiveTimeout",      UINT32),
    ("TransmitTimeout",     UINT32),
    ("StationAddress",      EFI_IPv6_ADDRESS),
    ("StationPort",         UINT16),
    ("RemoteAddress",       EFI_IPv6_ADDRESS),
    ("RemotePort",          UINT16)
  ]

class EFI_UDP6_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("UdpSessionData",  POINTER(EFI_UDP6_SESSION_DATA)),
    ("DataLength",      UINT32),
    ("FragmentCount",   UINT32),
    ("FragmentTable",   EFI_UDP6_FRAGMENT_DATA * 1)
  ]

class EFI_UDP6_RECEIVE_DATA (Structure):
  _fields_ = [
    ("TimeStamp",     EFI_TIME),
    ("RecycleSignal", EFI_EVENT),
    ("UdpSession",    EFI_UDP6_SESSION_DATA),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_UDP6_FRAGMENT_DATA * 1)
  ]

class EFI_UDP6_COMPLETION_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData", POINTER(EFI_UDP6_RECEIVE_DATA)),
    ("TxData", POINTER(EFI_UDP6_TRANSMIT_DATA))
  ]

class EFI_UDP6_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS),
    ("Packet",  EFI_UDP6_COMPLETION_TOKEN_Packet)
  ]

EFI_UDP6_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL),                               # IN  *This
  POINTER(EFI_UDP6_CONFIG_DATA),                            # OUT *Udp6ConfigData OPTIONAL,
  POINTER(EFI_IP6_MODE_DATA),                               # OUT *Ip6ModeData    OPTIONAL,
  POINTER(EFI_MANAGED_NETWORK_CONFIG_DATA),                 # OUT *MnpConfigData  OPTIONAL,
  POINTER(EFI_SIMPLE_NETWORK_MODE)                          # OUT *SnpModeData    OPTIONAL
  )

EFI_UDP6_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL),   # IN  *This
  POINTER(EFI_UDP6_CONFIG_DATA) # IN  *UdpConfigData  OPTIONAL
  )

EFI_UDP6_GROUPS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL),   # IN  *This
  BOOLEAN,                      # IN  JoinFlag
  POINTER(EFI_IPv6_ADDRESS)     # IN  *MulticastAddress  OPTIONAL
  )

EFI_UDP6_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL),         # IN  *This
  POINTER(EFI_UDP6_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_UDP6_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL),         # IN  *This
  POINTER(EFI_UDP6_COMPLETION_TOKEN)  # IN  *Token
  )

EFI_UDP6_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL),         # IN  *This
  POINTER(EFI_UDP6_COMPLETION_TOKEN)  # IN  *Token  OPTIONAL
  )

EFI_UDP6_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UDP6_PROTOCOL)    # IN  *This
  )

EFI_UDP6_PROTOCOL._fields_ = [
    ("GetModeData", EFI_UDP6_GET_MODE_DATA),
    ("Configure",   EFI_UDP6_CONFIGURE),
    ("Groups",      EFI_UDP6_GROUPS),
    ("Transmit",    EFI_UDP6_TRANSMIT),
    ("Receive",     EFI_UDP6_RECEIVE),
    ("Cancel",      EFI_UDP6_CANCEL),
    ("Poll",        EFI_UDP6_POLL)
  ]

