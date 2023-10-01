# Tcp4.py
#
# EfiPy2.MdePkg.Protocol.Tcp4
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Ip4             import EFI_IP4_MODE_DATA
from EfiPy2.MdePkg.Protocol.ManagedNetwork  import EFI_MANAGED_NETWORK_CONFIG_DATA
from EfiPy2.MdePkg.Protocol.SimpleNetwork   import EFI_SIMPLE_NETWORK_MODE

gEfiTcp4ServiceBindingProtocolGuid  = \
  EFI_GUID (0x00720665, 0x67EB, 0x4a99, (0xBA, 0xF7, 0xD3, 0xC3, 0x3A, 0x1C, 0x7C, 0xC9 ))

gEfiTcp4ProtocolGuid                = \
  EFI_GUID (0x65530BC7, 0xA359, 0x410f, (0xB0, 0x10, 0x5A, 0xAD, 0xC7, 0xEC, 0x2B, 0x62 ))

class EFI_TCP4_PROTOCOL (Structure):
  pass

class EFI_TCP4_SERVICE_POINT (Structure):
  _fields_ = [
    ("InstanceHandle",  EFI_HANDLE),
    ("LocalAddress",    EFI_IPv4_ADDRESS),
    ("LocalPort",       UINT16),
    ("RemoteAddress",   EFI_IPv4_ADDRESS),
    ("RemotePort",      UINT16)        
  ]

class EFI_TCP4_VARIABLE_DATA (Structure):
  _fields_ = [
    ("DriverHandle",  EFI_HANDLE),
    ("ServiceCount",  UINT32),
    ("Services",      EFI_TCP4_SERVICE_POINT * 1)
  ]

class EFI_TCP4_ACCESS_POINT (Structure):
  _fields_ = [
    ("UseDefaultAddress", BOOLEAN),
    ("StationAddress",    EFI_IPv4_ADDRESS),
    ("SubnetMask",        EFI_IPv4_ADDRESS),
    ("StationPort",       UINT16),
    ("RemoteAddress",     EFI_IPv4_ADDRESS),
    ("RemotePort",        UINT16),
    ("ActiveFlag",        BOOLEAN)
  ]

class EFI_TCP4_OPTION (Structure):
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

class EFI_TCP4_CONFIG_DATA (Structure):
  _fields_ = [
    ("TypeOfService", UINT8),
    ("TimeToLive",    UINT8),
    ("AccessPoint",   EFI_TCP4_ACCESS_POINT),
    ("ControlOption", POINTER(EFI_TCP4_OPTION))
  ]

Tcp4StateClosed         = 0
Tcp4StateListen         = 1
Tcp4StateSynSent        = 2
Tcp4StateSynReceived    = 3
Tcp4StateEstablished    = 4
Tcp4StateFinWait1       = 5
Tcp4StateFinWait2       = 6
Tcp4StateClosing        = 7
Tcp4StateTimeWait       = 8
Tcp4StateCloseWait      = 9
Tcp4StateLastAck        = 10
EFI_TCP4_CONNECTION_STATE = ENUM

class EFI_TCP4_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS)
  ]

class EFI_TCP4_CONNECTION_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken",   EFI_TCP4_COMPLETION_TOKEN)
  ]

class EFI_TCP4_LISTEN_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken",   EFI_TCP4_COMPLETION_TOKEN),
    ("NewChildHandle",    EFI_HANDLE)
  ]

class EFI_TCP4_FRAGMENT_DATA (Structure):
  _fields_ = [
    ("FragmentLength",  UINT32),
    ("FragmentBuffer",  PVOID)
  ]

class EFI_TCP4_RECEIVE_DATA (Structure):
  _fields_ = [
    ("UrgentFlag",    BOOLEAN),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_TCP4_FRAGMENT_DATA *1)
  ]

class EFI_TCP4_TRANSMIT_DATA (Structure):
  _fields_ = [
    ("Push",          BOOLEAN),
    ("Urgent",        BOOLEAN),
    ("DataLength",    UINT32),
    ("FragmentCount", UINT32),
    ("FragmentTable", EFI_TCP4_FRAGMENT_DATA *1)
  ]

class EFI_TCP4_IO_TOKEN_Packet (Union):
  _fields_ = [
    ("RxData",  POINTER(EFI_TCP4_RECEIVE_DATA)),
    ("TxData",  POINTER(EFI_TCP4_TRANSMIT_DATA))
  ]

class EFI_TCP4_IO_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken", EFI_TCP4_COMPLETION_TOKEN),
    ("Packet",          EFI_TCP4_IO_TOKEN_Packet)
  ]

class EFI_TCP4_CLOSE_TOKEN (Structure):
  _fields_ = [
    ("CompletionToken", EFI_TCP4_COMPLETION_TOKEN),
    ("AbortOnClose",    BOOLEAN)
  ]

EFI_TCP4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),                               # IN   *This
  POINTER(EFI_TCP4_CONNECTION_STATE),                       # OUT  *Tcp4State      OPTIONAL,
  POINTER(EFI_TCP4_CONFIG_DATA),                            # OUT  *Tcp4ConfigData OPTIONAL,
  POINTER(EFI_IP4_MODE_DATA),                               # OUT  *Ip4ModeData    OPTIONAL,
  POINTER(EFI_MANAGED_NETWORK_CONFIG_DATA),                 # OUT  *MnpConfigData  OPTIONAL,
  POINTER(EFI_SIMPLE_NETWORK_MODE)                          # OUT  *SnpModeData    OPTIONAL
  )

EFI_TCP4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),   # IN   *This
  POINTER(EFI_TCP4_CONFIG_DATA) # IN   *TcpConfigData OPTIONAL
  )

EFI_TCP4_ROUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),   # IN   *This
  BOOLEAN,                      # IN   DeleteRoute
  POINTER(EFI_IPv4_ADDRESS),    # IN   *SubnetAddress
  POINTER(EFI_IPv4_ADDRESS),    # IN   *SubnetMask
  POINTER(EFI_IPv4_ADDRESS)     # IN   *GatewayAddress
  )

EFI_TCP4_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),         # IN   *This
  POINTER(EFI_TCP4_CONNECTION_TOKEN)  # IN   *ConnectionToken
  )

EFI_TCP4_ACCEPT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),     # IN   *This
  POINTER(EFI_TCP4_LISTEN_TOKEN)  # IN   *ListenToken
  )

EFI_TCP4_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL), # IN   *This
  POINTER(EFI_TCP4_IO_TOKEN)  # IN   *Token
  )

EFI_TCP4_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL), # IN   *This
  POINTER(EFI_TCP4_IO_TOKEN)  # IN   *Token
  )

EFI_TCP4_CLOSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),   # IN   *This
  POINTER(EFI_TCP4_CLOSE_TOKEN) # IN   *CloseToken
  )

EFI_TCP4_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL),         # IN   *This
  POINTER(EFI_TCP4_COMPLETION_TOKEN)  # IN   *oken OPTIONAL
  )

EFI_TCP4_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCP4_PROTOCOL)  # IN   *This
  )

EFI_TCP4_PROTOCOL._fields_ = [
    ("GetModeData", EFI_TCP4_GET_MODE_DATA),
    ("Configure",   EFI_TCP4_CONFIGURE),
    ("Routes",      EFI_TCP4_ROUTES),
    ("Connect",     EFI_TCP4_CONNECT),
    ("Accept",      EFI_TCP4_ACCEPT),
    ("Transmit",    EFI_TCP4_TRANSMIT),
    ("Receive",     EFI_TCP4_RECEIVE),
    ("Close",       EFI_TCP4_CLOSE),
    ("Cancel",      EFI_TCP4_CANCEL),
    ("Poll",        EFI_TCP4_POLL)
  ]

