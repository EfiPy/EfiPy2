# Dhcp4.py
#
# EfiPy2.MdePkg.Protocol.Dhcp4
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDhcp4ProtocolGuid                   = \
  EFI_GUID (0x8a219718, 0x4ef5, 0x4761, (0x91, 0xc8, 0xc0, 0xf0, 0x4b, 0xda, 0x9e, 0x56 ))

gEfiDhcp4ServiceBindingProtocolGuid  = \
  EFI_GUID (0x9d9a39d8, 0xbd42, 0x4a73, (0xa4, 0xd5, 0x8e, 0xe9, 0x4b, 0xe1, 0x13, 0x80 ))

class EFI_DHCP4_PROTOCOL (Structure):
  pass

class EFI_DHCP4_PACKET_OPTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT8),
    ("Length",  UINT8),
    ("Data",    UINT8 * 1)
  ]

class EFI_DHCP4_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",            UINT8),
    ("HwType",            UINT8),
    ("HwAddrLen",         UINT8),
    ("Hops",              UINT8),
    ("Xid",               UINT32),
    ("Seconds",           UINT16),
    ("Reserved",          UINT16),
    ("ClientAddr",        EFI_IPv4_ADDRESS),
    ("YourAddr",          EFI_IPv4_ADDRESS),
    ("ServerAddr",        EFI_IPv4_ADDRESS),
    ("GatewayAddr",       EFI_IPv4_ADDRESS),
    ("ClientHwAddr",      UINT8 * 16),
    ("ServerName",        CHAR8 * 64),
    ("BootFileName",      CHAR8 * 128)
  ]

class EFI_DHCP4_PACKET_Dhcp4 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_DHCP4_HEADER),
    ("Magik",   UINT32),
    ("Option",  UINT8 * 1)
  ]

class EFI_DHCP4_PACKET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Size",    UINT32),
    ("Length",  UINT32),
    ("Dhcp4",   EFI_DHCP4_PACKET_Dhcp4)
  ]

Dhcp4Stopped        = 0x0
Dhcp4Init           = 0x1
Dhcp4Selecting      = 0x2
Dhcp4Requesting     = 0x3
Dhcp4Bound          = 0x4
Dhcp4Renewing       = 0x5
Dhcp4Rebinding      = 0x6
Dhcp4InitReboot     = 0x7
Dhcp4Rebooting      = 0x8
EFI_DHCP4_STATE     = ENUM

Dhcp4SendDiscover   = 0x01
Dhcp4RcvdOffer      = 0x02
Dhcp4SelectOffer    = 0x03
Dhcp4SendRequest    = 0x04
Dhcp4RcvdAck        = 0x05
Dhcp4RcvdNak        = 0x06
Dhcp4SendDecline    = 0x07
Dhcp4BoundCompleted = 0x08
Dhcp4EnterRenewing  = 0x09
Dhcp4EnterRebinding = 0x0a
Dhcp4AddressLost    = 0x0b
Dhcp4Fail           = 0x0c
EFI_DHCP4_EVENT     = ENUM

EFI_DHCP4_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),        # IN  *This
  PVOID,                              # IN  *Context,
  EFI_DHCP4_STATE,                    # IN  CurrentState,
  EFI_DHCP4_EVENT,                    # IN  Dhcp4Event,
  POINTER(EFI_DHCP4_PACKET),          # IN  *Packet     OPTIONAL,
  POINTER(POINTER(EFI_DHCP4_PACKET))  # OUT **NewPacket OPTIONAL 
  )

class EFI_DHCP4_CONFIG_DATA (Structure):
  _fields_ = [
    ("DiscoverTryCount",  UINT32),
    ("DiscoverTimeout",   POINTER(UINT32)),
    ("RequestTryCount",   UINT32),
    ("RequestTimeout",    POINTER(UINT32)),
    ("ClientAddress",     EFI_IPv4_ADDRESS),
    ("Dhcp4Callback",     EFI_DHCP4_CALLBACK),
    ("CallbackContext",   PVOID),
    ("OptionCount",       UINT32),
    ("OptionList",        POINTER(POINTER(EFI_DHCP4_PACKET_OPTION)))
  ]

class EFI_DHCP4_MODE_DATA (Structure):
  _fields_ = [
    ("State",             EFI_DHCP4_STATE),
    ("ConfigData",        EFI_DHCP4_CONFIG_DATA),
    ("ClientAddress",     EFI_IPv4_ADDRESS),
    ("ClientMacAddress",  EFI_MAC_ADDRESS),
    ("ServerAddress",     EFI_IPv4_ADDRESS),
    ("RouterAddress",     EFI_IPv4_ADDRESS),
    ("SubnetMask",        EFI_IPv4_ADDRESS),
    ("LeaseTime",         UINT32),
    ("ReplyPacket",       POINTER(EFI_DHCP4_PACKET))
  ]

class EFI_DHCP4_LISTEN_POINT (Structure):
  _fields_ = [
    ("ListenAddress", EFI_IPv4_ADDRESS),
    ("SubnetMask",    EFI_IPv4_ADDRESS),
    ("ListenPort",    UINT16)
  ]

class EFI_DHCP4_TRANSMIT_RECEIVE_TOKEN (Structure):
  _fields_ = [
    ("Status",            EFI_STATUS),
    ("CompletionEvent",   EFI_EVENT),
    ("RemoteAddress",     EFI_IPv4_ADDRESS),
    ("RemotePort",        UINT16),
    ("GatewayAddress",    EFI_IPv4_ADDRESS),
    ("ListenPointCount",  UINT32),
    ("ListenPoints",      POINTER(EFI_DHCP4_LISTEN_POINT)),
    ("TimeoutValue",      UINT32),
    ("Packet",            POINTER(EFI_DHCP4_PACKET)),
    ("ResponseCount",     UINT32),
    ("ResponseList",      POINTER(EFI_DHCP4_PACKET))
  ]

EFI_DHCP4_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),  # IN      *This
  POINTER(EFI_DHCP4_MODE_DATA)  #    OUT  *Dhcp4ModeData
  )

EFI_DHCP4_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),    # IN *This
  POINTER(EFI_DHCP4_CONFIG_DATA)  # IN *Dhcp4CfgData  OPTIONAL
  )

EFI_DHCP4_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),  # IN *This
  EFI_EVENT                     # IN CompletionEvent  OPTIONAL
  )

EFI_DHCP4_RENEW_REBIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),  # IN *This
  BOOLEAN,                      # IN RebindRequest
  EFI_EVENT                     # IN CompletionEvent  OPTIONAL
  )

EFI_DHCP4_RELEASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL)   # IN *This
  )

EFI_DHCP4_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL)   # IN *This
  )

EFI_DHCP4_BUILD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),          # IN      *This
  POINTER(EFI_DHCP4_PACKET),            # IN      *SeedPacket,
  UINT32,                               # IN      DeleteCount,
  POINTER(UINT8),                       # IN      *DeleteList   OPTIONAL,
  UINT32,                               # IN      AppendCount,  
  POINTER(EFI_DHCP4_PACKET_OPTION) * 1, # IN      *AppendList[] OPTIONAL,
  POINTER(POINTER(EFI_DHCP4_PACKET))    #    OUT  **NewPacket
  )

EFI_DHCP4_TRANSMIT_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),                # IN  *This
  POINTER(EFI_DHCP4_TRANSMIT_RECEIVE_TOKEN)   # IN  *Token,
  )

EFI_DHCP4_PARSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP4_PROTOCOL),                # IN     *This
  POINTER(EFI_DHCP4_PACKET),                  # IN     *Packet,
  POINTER(UINT32),                            # IN OUT *OptionCount,
  POINTER(EFI_DHCP4_PACKET_OPTION) * 1        #    OUT *PacketOptionList[] OPTIONAL,
  )

EFI_DHCP4_PROTOCOL._fields_ = [
    ("GetModeData",     EFI_DHCP4_GET_MODE_DATA),
    ("Configure",       EFI_DHCP4_CONFIGURE),
    ("Start",           EFI_DHCP4_START),
    ("RenewRebind",     EFI_DHCP4_RENEW_REBIND),
    ("Release",         EFI_DHCP4_RELEASE),
    ("Stop",            EFI_DHCP4_STOP),
    ("Build",           EFI_DHCP4_BUILD),
    ("TransmitReceive", EFI_DHCP4_TRANSMIT_RECEIVE),
    ("Parse",           EFI_DHCP4_PARSE)
  ]

