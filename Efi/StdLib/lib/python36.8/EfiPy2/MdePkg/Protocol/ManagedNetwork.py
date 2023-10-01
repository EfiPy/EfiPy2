# ManagedNetwork.py
#
# EfiPy2.MdePkg.Protocol.ManagedNetwork
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import SimpleNetwork

gEfiManagedNetworkServiceBindingProtocolGuid  = \
  EFI_GUID (0xf36ff770, 0xa7e1, 0x42cf, (0x9e, 0xd2, 0x56, 0xf0, 0xf2, 0x71, 0xf4, 0x4c ))

gEfiManagedNetworkProtocolGuid                = \
  EFI_GUID (0x7ab33a91, 0xace5, 0x4326, ( 0xb5, 0x72, 0xe7, 0xee, 0x33, 0xd3, 0x9f, 0x16 ))

class EFI_MANAGED_NETWORK_PROTOCOL (Structure):
  pass

class EFI_MANAGED_NETWORK_CONFIG_DATA (Structure):
  _fields_ = [
    ("ReceivedQueueTimeoutValue", UINT32),
    ("TransmitQueueTimeoutValue", UINT32),
    ("ProtocolTypeFilter",        UINT16),
    ("EnableUnicastReceive",      BOOLEAN),
    ("EnableMulticastReceive",    BOOLEAN),
    ("EnableBroadcastReceive",    BOOLEAN),
    ("EnablePromiscuousReceive",  BOOLEAN),
    ("FlushQueuesOnReset",        BOOLEAN),
    ("EnableReceiveTimestamps",   BOOLEAN),
    ("DisableBackgroundPolling",  BOOLEAN)
  ]

class EFI_MANAGED_NETWORK_RECEIVE_DATA (Structure):
  _fields_ = [
    ("Timestamp",           EFI_TIME ),
    ("RecycleEvent",        EFI_EVENT),
    ("PacketLength",        UINT32),
    ("HeaderLength",        UINT32),
    ("AddressLength",       UINT32),
    ("DataLength",          UINT32),
    ("BroadcastFlag",       BOOLEAN),
    ("MulticastFlag",       BOOLEAN),
    ("PromiscuousFlag",     BOOLEAN),
    ("ProtocolType",        UINT16),
    ("DestinationAddress",  PVOID),
    ("SourceAddress",       PVOID),
    ("MediaHeader",         PVOID),
    ("PacketData",          PVOID)
  ]

class EFI_MANAGED_NETWORK_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_MANAGED_NETWORK_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("DestinationAddress",  POINTER(EFI_MAC_ADDRESS)),
    ("SourceAddress",       POINTER(EFI_MAC_ADDRESS)),
    ("ProtocolType",        UINT16),
    ("DataLength",          UINT32),
    ("HeaderLength",        UINT16),
    ("FragmentCount",       UINT16),
    ("FragmentTable",       EFI_MANAGED_NETWORK_FRAGMENT_DATA * 1)
  ]

class EFI_MANAGED_NETWORK_COMPLETION_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData",  POINTER(EFI_MANAGED_NETWORK_RECEIVE_DATA)),
    ("TxData",  POINTER(EFI_MANAGED_NETWORK_TRANSMIT_DATA))
  ]

class EFI_MANAGED_NETWORK_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS),
    ("Packet",  EFI_MANAGED_NETWORK_COMPLETION_TOKEN_Packet)
  ]

EFI_MANAGED_NETWORK_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),          # IN  *This
  POINTER(EFI_MANAGED_NETWORK_CONFIG_DATA),       # OUT *MnpConfigData  OPTIONAL,
  POINTER(SimpleNetwork.EFI_SIMPLE_NETWORK_MODE)  # OUT *SnpModeData    OPTIONAL
  )

EFI_MANAGED_NETWORK_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),    # IN  *This
  POINTER(EFI_MANAGED_NETWORK_CONFIG_DATA)  # IN  *MnpConfigData  OPTIONAL,
  )

EFI_MANAGED_NETWORK_MCAST_IP_TO_MAC = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),  # IN  *This
  BOOLEAN,                                # IN  Ipv6Flag,
  POINTER(EFI_IP_ADDRESS),                # IN  *IpAddress,
  POINTER(EFI_MAC_ADDRESS)                # OUT *MacAddress
  )

EFI_MANAGED_NETWORK_GROUPS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),  # IN  *This
  BOOLEAN,                                # IN  JoinFlag,
  POINTER(EFI_MAC_ADDRESS)                # OUT *MacAddress
  )

EFI_MANAGED_NETWORK_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),        # IN  *This
  POINTER(EFI_MANAGED_NETWORK_COMPLETION_TOKEN) # IN  *Token
  )

EFI_MANAGED_NETWORK_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),        # IN  *This
  POINTER(EFI_MANAGED_NETWORK_COMPLETION_TOKEN) # IN  *Token
  )

EFI_MANAGED_NETWORK_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL),        # IN  *This
  POINTER(EFI_MANAGED_NETWORK_COMPLETION_TOKEN) # IN  *Token  OPTIONAL
  )

EFI_MANAGED_NETWORK_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MANAGED_NETWORK_PROTOCOL) # IN  *This
  )

EFI_MANAGED_NETWORK_PROTOCOL._fields_ = [
    ("GetModeData",   EFI_MANAGED_NETWORK_GET_MODE_DATA),
    ("Configure",     EFI_MANAGED_NETWORK_CONFIGURE),
    ("McastIpToMac",  EFI_MANAGED_NETWORK_MCAST_IP_TO_MAC),
    ("Groups",        EFI_MANAGED_NETWORK_GROUPS),
    ("Transmit",      EFI_MANAGED_NETWORK_TRANSMIT),
    ("Receive",       EFI_MANAGED_NETWORK_RECEIVE),
    ("Cancel",        EFI_MANAGED_NETWORK_CANCEL),
    ("Poll",          EFI_MANAGED_NETWORK_POLL)
  ]

