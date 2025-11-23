# Ip6.py
#
# EfiPy2.MdePkg.Protocol.Ip6
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import ManagedNetwork
from EfiPy2.MdePkg.Protocol import SimpleNetwork

gEfiIp6ServiceBindingProtocolGuid = \
  EFI_GUID (0xec835dd3, 0xfe0f, 0x617b, (0xa6, 0x21, 0xb3, 0x50, 0xc3, 0xe1, 0x33, 0x88 ))

gEfiIp6ProtocolGuid               = \
  EFI_GUID (0x2c8759d5, 0x5c2d, 0x66ef, (0x92, 0x5f, 0xb6, 0x6c, 0x10, 0x19, 0x57, 0xe2 ))

class EFI_IP6_PROTOCOL (Structure):
  pass

class EFI_IP6_ADDRESS_PAIR (Structure):
  _fields_ = [
    ("InstanceHandle",  EFI_HANDLE),
    ("Ip6Address",      EFI_IPv6_ADDRESS),
    ("PrefixLength",    UINT8)
  ]

class EFI_IP6_VARIABLE_DATA (Structure):
  _fields_ = [
    ("DriverHandle",  EFI_HANDLE),
    ("AddressCount",  UINT32),
    ("AddressPairs",  EFI_IP6_ADDRESS_PAIR * 1)
  ]

ICMP_V6_DEST_UNREACHABLE                 = 0x1
ICMP_V6_PACKET_TOO_BIG                   = 0x2
ICMP_V6_TIME_EXCEEDED                    = 0x3
ICMP_V6_PARAMETER_PROBLEM                = 0x4

ICMP_V6_ECHO_REQUEST                     = 0x80
ICMP_V6_ECHO_REPLY                       = 0x81
ICMP_V6_LISTENER_QUERY                   = 0x82
ICMP_V6_LISTENER_REPORT                  = 0x83
ICMP_V6_LISTENER_DONE                    = 0x84
ICMP_V6_ROUTER_SOLICIT                   = 0x85
ICMP_V6_ROUTER_ADVERTISE                 = 0x86
ICMP_V6_NEIGHBOR_SOLICIT                 = 0x87
ICMP_V6_NEIGHBOR_ADVERTISE               = 0x88
ICMP_V6_REDIRECT                         = 0x89
ICMP_V6_LISTENER_REPORT_2                = 0x8F

ICMP_V6_NO_ROUTE_TO_DEST                 = 0x0
ICMP_V6_COMM_PROHIBITED                  = 0x1
ICMP_V6_BEYOND_SCOPE                     = 0x2
ICMP_V6_ADDR_UNREACHABLE                 = 0x3
ICMP_V6_PORT_UNREACHABLE                 = 0x4
ICMP_V6_SOURCE_ADDR_FAILED               = 0x5
ICMP_V6_ROUTE_REJECTED                   = 0x6

ICMP_V6_TIMEOUT_HOP_LIMIT                = 0x0
ICMP_V6_TIMEOUT_REASSEMBLE               = 0x1

ICMP_V6_ERRONEOUS_HEADER                 = 0x0
ICMP_V6_UNRECOGNIZE_NEXT_HDR             = 0x1
ICMP_V6_UNRECOGNIZE_OPTION               = 0x2

class EFI_IP6_CONFIG_DATA (Structure):
  _fields_ = [
    ("DefaultProtocol",     UINT8),
    ("AcceptAnyProtocol",   BOOLEAN),
    ("AcceptIcmpErrors",    BOOLEAN),
    ("AcceptPromiscuous",   BOOLEAN),
    ("DestinationAddress",  EFI_IPv6_ADDRESS),
    ("StationAddress",      EFI_IPv6_ADDRESS),
    ("TrafficClass",        UINT8),
    ("HopLimit",            UINT8),
    ("FlowLabel",           UINT32),
    ("ReceiveTimeout",      UINT32),
    ("TransmitTimeout",     UINT32)
  ]

class EFI_IP6_ADDRESS_INFO (Structure):
  _fields_ = [
    ("Address",       EFI_IPv6_ADDRESS),
    ("PrefixLength",  UINT8)
  ]

class EFI_IP6_ROUTE_TABLE (Structure):
  _fields_ = [
    ("Gateway",       EFI_IPv6_ADDRESS),
    ("Destination",   EFI_IPv6_ADDRESS),
    ("PrefixLength",  UINT8)
  ]

EfiNeighborInComplete   = 0
EfiNeighborReachable    = 1
EfiNeighborStale        = 2
EfiNeighborDelay        = 3
EfiNeighborProbe        = 4
EFI_IP6_NEIGHBOR_STATE  = ENUM

class EFI_IP6_NEIGHBOR_CACHE (Structure):
  _fields_ = [
    ("Neighbor",    EFI_IPv6_ADDRESS),
    ("LinkAddress", EFI_MAC_ADDRESS),
    ("State",       EFI_IP6_NEIGHBOR_STATE)
  ]

class EFI_IP6_ICMP_TYPE (Structure):
  _fields_ = [
    ("Type",  UINT8),
    ("Code",  UINT8)
  ]

class EFI_IP6_MODE_DATA (Structure):
  _fields_ = [
    ("IsStarted",     BOOLEAN),
    ("MaxPacketSize", UINT32),
    ("ConfigData",    EFI_IP6_CONFIG_DATA),
    ("IsConfigured",  BOOLEAN),
    ("AddressCount",  UINT32),
    ("AddressList",   POINTER(EFI_IP6_ADDRESS_INFO)),
    ("GroupCount",    UINT32),
    ("GroupTable",    POINTER(EFI_IPv6_ADDRESS)),
    ("RouteCount",    UINT32),
    ("RouteTable",    POINTER(EFI_IP6_ROUTE_TABLE)),
    ("NeighborCount", UINT32),
    ("NeighborCache", POINTER(EFI_IP6_NEIGHBOR_CACHE)),
    ("PrefixCount",   UINT32),
    ("PrefixTable",   POINTER(EFI_IP6_ADDRESS_INFO)),
    ("IcmpTypeCount", UINT32),
    ("IcmpTypeList",  POINTER(EFI_IP6_ICMP_TYPE))
  ]

class EFI_IP6_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("TrafficClassH",       UINT8, 4),
    ("Version",             UINT8, 4),
    ("FlowLabelH",          UINT8, 4),
    ("TrafficClassL",       UINT8, 4),
    ("FlowLabelL",          UINT16),
    ("PayloadLength",       UINT16),
    ("NextHeader",          UINT8),
    ("HopLimit",            UINT8),
    ("SourceAddress",       EFI_IPv6_ADDRESS),
    ("DestinationAddress",  EFI_IPv6_ADDRESS)
  ]

class EFI_IP6_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_IP6_RECEIVE_DATA (Structure):
  _fields_ = [
    ("TimeStamp",     EFI_TIME),
    ("RecycleSignal", EFI_EVENT),
    ("HeaderLength",  UINT32),
    ("Header",        POINTER(EFI_IP6_HEADER)),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_IP6_FRAGMENT_DATA * 1)
  ]

class EFI_IP6_OVERRIDE_DATA (Structure):
  _fields_ = [
    ("Protocol",  UINT8),
    ("HopLimit",  UINT8),
    ("FlowLabel", UINT32)
  ]

class EFI_IP6_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("DestinationAddress",  EFI_IPv6_ADDRESS),
    ("OverrideData",        POINTER(EFI_IP6_OVERRIDE_DATA)),
    ("ExtHdrsLength",       UINT32),
    ("ExtHdrs",             PVOID),
    ("NextHeader",          UINT8),
    ("DataLength",          UINT32),
    ("FragmentCount",       UINT32),
    ("FragmentTable",       EFI_IP6_FRAGMENT_DATA * 1)
  ]

class EFI_IP6_COMPLETION_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData",  POINTER(EFI_IP6_RECEIVE_DATA)),
    ("TxData",  POINTER(EFI_IP6_TRANSMIT_DATA))
  ]

class EFI_IP6_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS),
    ("Packet",  EFI_IP6_COMPLETION_TOKEN_Packet)
  ]

EFI_IP6_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),                                # IN  *This
  POINTER(EFI_IP6_MODE_DATA),                               # OUT *Ip6ModeData     OPTIONAL,
  POINTER(ManagedNetwork.EFI_MANAGED_NETWORK_CONFIG_DATA),  # OUT *MnpConfigData   OPTIONAL,
  POINTER(SimpleNetwork.EFI_SIMPLE_NETWORK_MODE)            # OUT *SnpModeData     OPTIONAL
  )

EFI_IP6_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),    # IN  *This
  POINTER(EFI_IP6_CONFIG_DATA)  # IN  *Ip6ConfigData    OPTIONAL,
  )

EFI_IP6_GROUPS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),    # IN  *This
  BOOLEAN,                      # IN  JoinFlag,
  POINTER(EFI_IPv6_ADDRESS)     # IN  *GroupAddress OPTIONAL
  )

EFI_IP6_ROUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),    # IN  *This
  BOOLEAN,                      # IN DeleteRoute,
  POINTER(EFI_IPv6_ADDRESS),    # IN *Destination OPTIONAL,
  UINT8,                        # IN PrefixLength,
  POINTER(EFI_IPv6_ADDRESS)     # IN *GatewayAddress  
  )

EFI_IP6_NEIGHBORS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),    # IN  *This
  BOOLEAN,                      # IN DeleteRoute,
  POINTER(EFI_IPv6_ADDRESS),    # IN *TargetIp6Address,
  POINTER(EFI_MAC_ADDRESS),     # IN *TargetLinkAddress,
  UINT32,                       # IN Timeout,
  BOOLEAN                       # IN Override
  )

EFI_IP6_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),        # IN  *This
  POINTER(EFI_IP6_COMPLETION_TOKEN) # IN *Token,
  )

EFI_IP6_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),        # IN  *This
  POINTER(EFI_IP6_COMPLETION_TOKEN) # IN  *Token
  )

EFI_IP6_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL),        # IN  *This
  POINTER(EFI_IP6_COMPLETION_TOKEN) # IN  *Token OPTIONAL
  )

EFI_IP6_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IP6_PROTOCOL) # IN  *This
  )

EFI_IP6_PROTOCOL._fields_ = [
    ("GetModeData", EFI_IP6_GET_MODE_DATA),
    ("Configure",   EFI_IP6_CONFIGURE),
    ("Groups",      EFI_IP6_GROUPS),
    ("Routes",      EFI_IP6_ROUTES),
    ("Neighbors",   EFI_IP6_NEIGHBORS),
    ("Transmit",    EFI_IP6_TRANSMIT),
    ("Receive",     EFI_IP6_RECEIVE),
    ("Cancel",      EFI_IP6_CANCEL),
    ("Poll",        EFI_IP6_POLL)
  ]

