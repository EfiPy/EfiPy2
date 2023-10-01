# Tcp6.py
#
# EfiPy2.MdePkg.Protocol.Tcp6
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Ip6             import EFI_IP6_MODE_DATA
from EfiPy2.MdePkg.Protocol.ManagedNetwork  import EFI_MANAGED_NETWORK_CONFIG_DATA
from EfiPy2.MdePkg.Protocol.SimpleNetwork   import EFI_SIMPLE_NETWORK_MODE

gEfiTcp6ServiceBindingProtocolGuid = \
  EFI_GUID (0xec20eb79, 0x6c1a, 0x4664, (0x9a, 0x0d, 0xd2, 0xe4, 0xcc, 0x16, 0xd6, 0x64 ))

gEfiTcp6ProtocolGuid               = \
  EFI_GUID (0x46e44855, 0xbd60, 0x4ab7, (0xab, 0x0d, 0xa6, 0x79, 0xb9, 0x44, 0x7d, 0x77 ))

class EFI_TCP6_PROTOCOL (Structure):
  pass

class EFI_TCP6_SERVICE_POINT (Structure):
  _fields_ = [
    ("InstanceHandle",  EFI_HANDLE),
    ("LocalAddress",    EFI_IPv6_ADDRESS),
    ("LocalPort",       UINT16),
    ("RemoteAddress",   EFI_IPv6_ADDRESS),
    ("RemotePort",      UINT16)        
  ]

class EFI_TCP6_VARIABLE_DATA (Structure):
  _fields_ = [
    ("DriverHandle",  EFI_HANDLE),
    ("ServiceCount",  UINT32),
    ("Services",      EFI_TCP6_SERVICE_POINT * 1)
  ]

class EFI_TCP6_ACCESS_POINT (Structure):
  _fields_ = [
    ("StationAddress",    EFI_IPv6_ADDRESS),
    ("StationPort",       UINT16),
    ("RemoteAddress",     EFI_IPv6_ADDRESS),
    ("RemotePort",        UINT16),
    ("ActiveFlag",        BOOLEAN)
  ]

class EFI_TCP6_OPTION (Structure):
  _fields_ = [
    ("ReceiveBufferSize",       UINT32),
    ("SendBufferSize",          UINT32),
    ("MaxSynBackLog",           UINT32),
    ("ConnectionTimeout",       UINT32),
    ("DataRetries",             UINT32),
    ("FinTimeout",              UINT32),
    ("TimeWaitTimeout",         UINT32),
    ("KeepAliveProbes",         UINT32),
    ("KeepAliveTime",           UINT32),
    ("KeepAliveInterval",       UINT32),
    ("EnableNagle",             BOOLEAN),
    ("EnableTimeStamp",         BOOLEAN),
    ("EnableWindowScaling",     BOOLEAN),
    ("EnableSelectiveAck",      BOOLEAN),
    ("EnablePathMtuDiscovery",  BOOLEAN)
  ]

class EFI_TCP6_CONFIG_DATA (Structure):
  _fields_ = [
    ("TrafficClass",  UINT8),
    ("HopLimit",      UINT8),
    ("AccessPoint",   EFI_TCP6_ACCESS_POINT),
    ("ControlOption", POINTER(EFI_TCP6_OPTION))
  ]

Tcp6StateClosed         = 0
Tcp6StateListen         = 1
Tcp6StateSynSent        = 2
Tcp6StateSynReceived    = 3
Tcp6StateEstablished    = 4
Tcp6StateFinWait1       = 5
Tcp6StateFinWait2       = 6
Tcp6StateClosing        = 7
Tcp6StateTimeWait       = 8
Tcp6StateCloseWait      = 9
Tcp6StateLastAck        = 10
EFI_TCP6_CONNECTION_STATE = ENUM

class EFI_TCP6_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS)
  ]

class EFI_TCP6_CONNECTION_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken",   EFI_TCP6_COMPLETION_TOKEN)
  ]

class EFI_TCP6_LISTEN_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken",   EFI_TCP6_COMPLETION_TOKEN),
    ("NewChildHandle",    EFI_HANDLE)
  ]

class EFI_TCP6_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_TCP6_RECEIVE_DATA (Structure):
  _fields_ = [
    ("UrgentFlag",    BOOLEAN),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_TCP6_FRAGMENT_DATA *1)
  ]

class EFI_TCP6_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("Push",          BOOLEAN),
    ("Urgent",        BOOLEAN),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_TCP6_FRAGMENT_DATA *1)
  ]

class EFI_TCP6_IO_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData",  POINTER(EFI_TCP6_RECEIVE_DATA)),
    ("TxData",  POINTER(EFI_TCP6_TRANSMIT_DATA))
  ]

class EFI_TCP6_IO_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken", EFI_TCP6_COMPLETION_TOKEN),
    ("Packet",          EFI_TCP6_IO_TOKEN_Packet)
  ]

class EFI_TCP6_CLOSE_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken", EFI_TCP6_COMPLETION_TOKEN),
    ("AbortOnClose",    BOOLEAN)
  ]

EFI_TCP6_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL),                               # IN   *This
  POINTER(EFI_TCP6_CONNECTION_STATE),                       # OUT  *Tcp6State      OPTIONAL,
  POINTER(EFI_TCP6_CONFIG_DATA),                            # OUT  *Tcp6ConfigData OPTIONAL,
  POINTER(EFI_IP6_MODE_DATA),                               # OUT  *Ip6ModeData    OPTIONAL,
  POINTER(EFI_MANAGED_NETWORK_CONFIG_DATA),                 # OUT  *MnpConfigData  OPTIONAL,
  POINTER(EFI_SIMPLE_NETWORK_MODE)                          # OUT  *SnpModeData    OPTIONAL
  )

EFI_TCP6_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL),   # IN   *This
  POINTER(EFI_TCP6_CONFIG_DATA) # IN   *Tcp6ConfigData OPTIONAL
  )

EFI_TCP6_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL),         # IN   *This
  POINTER(EFI_TCP6_CONNECTION_TOKEN)  # IN   *ConnectionToken
  )

EFI_TCP6_ACCEPT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL),     # IN   *This
  POINTER(EFI_TCP6_LISTEN_TOKEN)  # IN   *ListenToken
  )

EFI_TCP6_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL), # IN   *This
  POINTER(EFI_TCP6_IO_TOKEN)  # IN   *Token
  )

EFI_TCP6_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL), # IN   *This
  POINTER(EFI_TCP6_IO_TOKEN)  # IN   *Token
  )

EFI_TCP6_CLOSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL),   # IN   *This
  POINTER(EFI_TCP6_CLOSE_TOKEN) # IN   *CloseToken
  )

EFI_TCP6_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL),         # IN   *This
  POINTER(EFI_TCP6_COMPLETION_TOKEN)  # IN   *oken OPTIONAL
  )

EFI_TCP6_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP6_PROTOCOL)  # IN   *This
  )

EFI_TCP6_PROTOCOL._fields_ = [
    ("GetModeData", EFI_TCP6_GET_MODE_DATA),
    ("Configure",   EFI_TCP6_CONFIGURE),
    ("Connect",     EFI_TCP6_CONNECT),
    ("Accept",      EFI_TCP6_ACCEPT),
    ("Transmit",    EFI_TCP6_TRANSMIT),
    ("Receive",     EFI_TCP6_RECEIVE),
    ("Close",       EFI_TCP6_CLOSE),
    ("Cancel",      EFI_TCP6_CANCEL),
    ("Poll",        EFI_TCP6_POLL)
  ]

