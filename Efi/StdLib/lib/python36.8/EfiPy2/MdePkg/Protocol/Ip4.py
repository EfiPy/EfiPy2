# Ip4.py
#
# EfiPy2.MdePkg.Protocol.Ip4
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import ManagedNetwork
from EfiPy2.MdePkg.Protocol import SimpleNetwork

gEfiIp4ServiceBindingProtocolGuid = \
  EFI_GUID (0xc51711e7, 0xb4bf, 0x404a, (0xbf, 0xb8, 0x0a, 0x04, 0x8e, 0xf1, 0xff, 0xe4 ))

gEfiIp4ProtocolGuid               = \
  EFI_GUID (0x41d94cd2, 0x35b6, 0x455a, (0x82, 0x58, 0xd4, 0xe5, 0x13, 0x34, 0xaa, 0xdd ))

class EFI_IP4_PROTOCOL (Structure):
  pass

class EFI_IP4_ADDRESS_PAIR (Structure):
  _fields_ = [
    ("InstanceHandle",  EFI_HANDLE),
    ("Ip4Address",      EFI_IPv4_ADDRESS),
    ("SubnetMask",      EFI_IPv4_ADDRESS)
  ]

class EFI_IP4_VARIABLE_DATA (Structure):
  _fields_ = [
    ("DriverHandle",  EFI_HANDLE),
    ("AddressCount",  UINT32),
    ("AddressPairs",  EFI_IP4_ADDRESS_PAIR * 1)
  ]

class EFI_IP4_CONFIG_DATA (Structure):
  _fields_ = [
    ("DefaultProtocol",   UINT8),
    ("AcceptAnyProtocol", BOOLEAN),
    ("AcceptIcmpErrors",  BOOLEAN),
    ("AcceptBroadcast",   BOOLEAN),
    ("AcceptPromiscuous", BOOLEAN),
    ("UseDefaultAddress", BOOLEAN),
    ("StationAddress",    EFI_IPv4_ADDRESS),
    ("SubnetMask",        EFI_IPv4_ADDRESS),
    ("TypeOfService",     UINT8),
    ("TimeToLive",        UINT8),
    ("DoNotFragment",     BOOLEAN),
    ("RawData",           BOOLEAN),
    ("ReceiveTimeout",    UINT32),
    ("TransmitTimeout",   UINT32)
  ]

class EFI_IP4_ROUTE_TABLE (Structure):
  _fields_ = [
    ("SubnetAddress",   EFI_IPv4_ADDRESS),
    ("SubnetMask",      EFI_IPv4_ADDRESS),
    ("GatewayAddress",  EFI_IPv4_ADDRESS)
  ]

class EFI_IP4_ICMP_TYPE (Structure):
  _fields_ = [
    ("Type",  UINT8),
    ("Code",  UINT8)
  ]

class EFI_IP4_MODE_DATA (Structure):
  _fields_ = [
    ("IsStarted",     BOOLEAN),
    ("MaxPacketSize", UINT32),
    ("ConfigData",    EFI_IP4_CONFIG_DATA),
    ("IsConfigured",  BOOLEAN),
    ("GroupCount",    UINT32),
    ("GroupTable",    POINTER(EFI_IPv4_ADDRESS)),
    ("RouteCount",    UINT32),
    ("RouteTable",    POINTER(EFI_IP4_ROUTE_TABLE)),
    ("IcmpTypeCount", UINT32),
    ("IcmpTypeList",  POINTER(EFI_IP4_ICMP_TYPE))
  ]

class EFI_IP4_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HeaderLength",        UINT8, 4),
    ("Version",             UINT8, 4),
    ("TypeOfService",       UINT8),
    ("TotalLength",         UINT16),
    ("Identification",      UINT16),
    ("Fragmentation",       UINT16),
    ("TimeToLive",          UINT8),
    ("Protocol",            UINT8),
    ("Checksum",            UINT16),
    ("SourceAddress",       EFI_IPv4_ADDRESS),
    ("DestinationAddress",  EFI_IPv4_ADDRESS)
  ]

class EFI_IP4_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_IP4_RECEIVE_DATA (Structure):
  _fields_ = [
    ("TimeStamp",     EFI_TIME),
    ("RecycleSignal", EFI_EVENT),
    ("HeaderLength",  UINT32),
    ("Header",        POINTER(EFI_IP4_HEADER)),
    ("OptionsLength", UINT32),
    ("Options",       PVOID),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_IP4_FRAGMENT_DATA * 1)
  ]

class EFI_IP4_OVERRIDE_DATA (Structure):
  _fields_ = [
    ("SourceAddress",   EFI_IPv4_ADDRESS),
    ("GatewayAddress",  EFI_IPv4_ADDRESS),
    ("Protocol",        UINT8),
    ("TypeOfService",   UINT8),
    ("TimeToLive",      UINT8),
    ("DoNotFragment",   BOOLEAN)
  ]

class EFI_IP4_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("DestinationAddress",  EFI_IPv4_ADDRESS),
    ("OverrideData",        POINTER(EFI_IP4_OVERRIDE_DATA)),
    ("OptionsLength",       UINT32),
    ("OptionsBuffer",       PVOID),
    ("TotalDataLength",     UINT32),
    ("FragmentCount",       UINT32),
    ("FragmentTable",       EFI_IP4_FRAGMENT_DATA * 1)
  ]

class EFI_IP4_COMPLETION_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData",  POINTER(EFI_IP4_RECEIVE_DATA)),
    ("TxData",  POINTER(EFI_IP4_TRANSMIT_DATA))
  ]

class EFI_IP4_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",  EFI_EVENT),
    ("Status", EFI_STATUS),
    ("Packet", EFI_IP4_COMPLETION_TOKEN_Packet)
  ]

EFI_IP4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),                                # IN  *This
  POINTER(EFI_IP4_MODE_DATA),                               # OUT *Ip4ModeData     OPTIONAL,
  POINTER(ManagedNetwork.EFI_MANAGED_NETWORK_CONFIG_DATA),  # OUT *MnpConfigData   OPTIONAL,
  POINTER(SimpleNetwork.EFI_SIMPLE_NETWORK_MODE)            # OUT *SnpModeData     OPTIONAL
  )

EFI_IP4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),    # IN  *This
  POINTER(EFI_IP4_CONFIG_DATA)  # IN  *IpConfigData     OPTIONAL,
  )

EFI_IP4_GROUPS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),    # IN  *This
  BOOLEAN,                      # IN  JoinFlag,
  POINTER(EFI_IPv4_ADDRESS)     # IN  *GroupAddress OPTIONAL
  )

EFI_IP4_ROUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),    # IN  *This
  BOOLEAN,                      # IN DeleteRoute,
  POINTER(EFI_IPv4_ADDRESS),    # IN *SubnetAddress,
  POINTER(EFI_IPv4_ADDRESS),    # IN *SubnetMask,
  POINTER(EFI_IPv4_ADDRESS)     # IN *GatewayAddress  
  )

EFI_IP4_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),        # IN  *This
  POINTER(EFI_IP4_COMPLETION_TOKEN) # IN *Token,
  )

EFI_IP4_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),        # IN  *This
  POINTER(EFI_IP4_COMPLETION_TOKEN) # IN  *Token
  )

EFI_IP4_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL),        # IN  *This
  POINTER(EFI_IP4_COMPLETION_TOKEN) # IN  *Token OPTIONAL
  )

EFI_IP4_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP4_PROTOCOL) # IN  *This
  )

EFI_IP4_PROTOCOL._fields_ = [
    ("GetModeData", EFI_IP4_GET_MODE_DATA),
    ("Configure",   EFI_IP4_CONFIGURE),
    ("Groups",      EFI_IP4_GROUPS),
    ("Routes",      EFI_IP4_ROUTES),
    ("Transmit",    EFI_IP4_TRANSMIT),
    ("Receive",     EFI_IP4_RECEIVE),
    ("Cancel",      EFI_IP4_CANCEL),
    ("Poll",        EFI_IP4_POLL)
  ]

