# Dhcp6.py
#
# EfiPy2.MdePkg.Protocol.Dhcp6
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDhcp6ProtocolGuid                   = \
  EFI_GUID (0x87c8bad7, 0x595, 0x4053, (0x82, 0x97, 0xde, 0xde, 0x39, 0x5f, 0x5d, 0x5b ))

gEfiDhcp6ServiceBindingProtocolGuid     = \
  EFI_GUID (0x9fb9a8a1, 0x2f4a, 0x43a6, (0x88, 0x9c, 0xd0, 0xf7, 0xb6, 0xc4, 0x7a, 0xd5 ))

class EFI_DHCP6_PROTOCOL (Structure):
  pass

Dhcp6Init                    = 0x0
Dhcp6Selecting               = 0x1
Dhcp6Requesting              = 0x2
Dhcp6Declining               = 0x3
Dhcp6Confirming              = 0x4
Dhcp6Releasing               = 0x5
Dhcp6Bound                   = 0x6
Dhcp6Renewing                = 0x7
Dhcp6Rebinding               = 0x8
EFI_DHCP6_STATE              = ENUM

Dhcp6SendSolicit             = 0x0
Dhcp6RcvdAdvertise           = 0x1
Dhcp6SelectAdvertise         = 0x2
Dhcp6SendRequest             = 0x3
Dhcp6RcvdReply               = 0x4
Dhcp6RcvdReconfigure         = 0x5
Dhcp6SendDecline             = 0x6
Dhcp6SendConfirm             = 0x7
Dhcp6SendRelease             = 0x8
Dhcp6EnterRenewing           = 0x9
Dhcp6EnterRebinding          = 0xa
EFI_DHCP6_EVENT              = ENUM

EFI_DHCP6_IA_TYPE_NA   = 3
EFI_DHCP6_IA_TYPE_TA   = 4

class EFI_DHCP6_PACKET_OPTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT16),
    ("OpLen",   UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_DHCP6_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("MessageType",     UINT32, 8),
    ("TransactionId",   UINT32, 24)
  ]

class EFI_DHCP6_PACKET_Dhcp6 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_DHCP6_HEADER),
    ("Option",  UINT8 * 1)
  ]

class EFI_DHCP6_PACKET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Size",    UINT32),
    ("Length",  UINT32),
    ("Dhcp6", EFI_DHCP6_PACKET_Dhcp6)
  ]

class EFI_DHCP6_DUID (Structure):
  _fields_ = [
    ("Length",  UINT16),
    ("Duid",    UINT8 * 1)
  ]

class EFI_DHCP6_RETRANSMISSION (Structure):
  _fields_ = [
    ("Irt", UINT32),
    ("Mrc", UINT32),
    ("Mrt", UINT32),
    ("Mrd", UINT32)
  ]

class EFI_DHCP6_IA_ADDRESS (Structure):
  _fields_ = [
    ("IpAddress",         EFI_IPv6_ADDRESS),
    ("PreferredLifetime", UINT32),
    ("ValidLifetime",     UINT32)
  ]

class EFI_DHCP6_IA_DESCRIPTOR (Structure):
  _fields_ = [
    ("Type",  UINT16),
    ("IaId",  UINT32)
  ]

class EFI_DHCP6_IA (Structure):
  _fields_ = [
    ("Descriptor",      EFI_DHCP6_IA_DESCRIPTOR),
    ("State",           EFI_DHCP6_STATE),
    ("ReplyPacket",     POINTER(EFI_DHCP6_PACKET)),
    ("IaAddressCount",  UINT32),
    ("IaAddress",       EFI_DHCP6_IA_ADDRESS * 1)
  ]

class EFI_DHCP6_MODE_DATA (Structure):
  _fields_ = [
    ("ClientId",  POINTER (EFI_DHCP6_DUID)),
    ("Ia",        POINTER (EFI_DHCP6_IA))
  ]

EFI_DHCP6_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),        # IN     *This
  PVOID,                              # IN  *Context,
  EFI_DHCP6_STATE,                    # IN  CurrentState,
  EFI_DHCP6_EVENT,                    # IN  Dhcp4Event,
  POINTER(EFI_DHCP6_PACKET),          # IN  *Packet     OPTIONAL,
  POINTER(POINTER(EFI_DHCP6_PACKET))  # OUT **NewPacket OPTIONAL 
  )

class EFI_DHCP6_CONFIG_DATA (Structure):
  _fields_ = [
    ("Dhcp6Callback",         EFI_DHCP6_CALLBACK),
    ("CallbackContext",       PVOID),
    ("OptionCount",           UINT32),
    ("OptionList",            POINTER(POINTER(EFI_DHCP6_PACKET_OPTION))),
    ("IaDescriptor",          EFI_DHCP6_IA_DESCRIPTOR),
    ("IaInfoEvent",           EFI_EVENT),
    ("ReconfigureAccept",     BOOLEAN),
    ("RapidCommit",           BOOLEAN),
    ("SolicitRetransmission", POINTER(EFI_DHCP6_RETRANSMISSION))
  ]

EFI_DHCP6_INFO_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),  # IN *This
  PVOID,                        # IN *Context,
  EFI_DHCP6_PACKET              # IN *Packet
  )

EFI_DHCP6_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),    # IN      *This
  POINTER(EFI_DHCP6_MODE_DATA),   #    OUT  *Dhcp6ModeData
  POINTER(EFI_DHCP6_CONFIG_DATA)  #    OUT  *Dhcp6ConfigData
  )

EFI_DHCP6_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),    # IN *This
  POINTER(EFI_DHCP6_CONFIG_DATA)  # IN *Dhcp6CfgData  OPTIONAL
  )

EFI_DHCP6_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL)   # IN *This
  )

EFI_DHCP6_INFO_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),            # IN *This
  BOOLEAN,                                # IN SendClientId
  POINTER(EFI_DHCP6_PACKET_OPTION),       # IN *OptionRequest,
  UINT32,                                 # IN OptionCount,
  POINTER(EFI_DHCP6_PACKET_OPTION) * 1,   # IN *OptionList[] OPTIONAL,
  POINTER(EFI_DHCP6_RETRANSMISSION),      # IN *Retransmission, 
  EFI_EVENT,                              # IN TimeoutEvent OPTIONAL,
  EFI_DHCP6_INFO_CALLBACK,                # IN ReplyCallback,
  PVOID                                   # IN *CallbackContext OPTIONAL
  )

EFI_DHCP6_RENEW_REBIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),  # IN *This
  BOOLEAN                       # IN RebindRequest
  )

EFI_DHCP6_DECLINE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),  # IN *This
  UINT32,                       # IN AddressCount
  POINTER(EFI_IPv6_ADDRESS)     # IN *Addresses
  )

EFI_DHCP6_RELEASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),  # IN *This
  UINT32,                       # IN AddressCount
  POINTER(EFI_IPv6_ADDRESS)     # IN *Addresses
  )

EFI_DHCP6_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL)   # IN *This
  )

EFI_DHCP6_PARSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DHCP6_PROTOCOL),          # IN      *This
  POINTER(EFI_DHCP6_PACKET),            # IN      *Packet,
  POINTER(UINT32),                      # IN OUT  *OptionCount,
  POINTER(EFI_DHCP6_PACKET_OPTION) * 1  #    OUT  *PacketOptionList[] OPTIONAL
  )                             
                                
EFI_DHCP6_PROTOCOL._fields_ = [
    ("GetModeData", EFI_DHCP6_GET_MODE_DATA),
    ("Configure",   EFI_DHCP6_CONFIGURE),
    ("Start",       EFI_DHCP6_START),
    ("InfoRequest", EFI_DHCP6_INFO_REQUEST),
    ("RenewRebind", EFI_DHCP6_RENEW_REBIND),
    ("Decline",     EFI_DHCP6_DECLINE),
    ("Release",     EFI_DHCP6_RELEASE),
    ("Stop",        EFI_DHCP6_STOP),
    ("Parse",       EFI_DHCP6_PARSE)
  ]

