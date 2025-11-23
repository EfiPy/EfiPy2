# IpSecConfig.py
#
# EfiPy2.MdePkg.Protocol.IpSecConfig
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiIpSecConfigProtocolGuid = \
  EFI_GUID (0xce5e5929, 0xc7a3, 0x4602, (0xad, 0x9e, 0xc9, 0xda, 0xf9, 0x4e, 0xbf, 0xcf ))

class EFI_IPSEC_CONFIG_PROTOCOL (Structure):
  pass

IPsecConfigDataTypeSpd      = 0
IPsecConfigDataTypeSad      = 1
IPsecConfigDataTypePad      = 2
IPsecConfigDataTypeMaximum  = 3
EFI_IPSEC_CONFIG_DATA_TYPE  = ENUM

class EFI_IP_ADDRESS_INFO (Structure):
  _fields_ = [
    ("Address",       EFI_IP_ADDRESS),
    ("PrefixLength",  UINT8)
  ]

class EFI_IPSEC_SPD_SELECTOR (Structure):
  _fields_ = [
    ("LocalAddressCount",   UINT32),
    ("LocalAddress",        POINTER(EFI_IP_ADDRESS_INFO)),
    ("RemoteAddressCount",  UINT32),
    ("RemoteAddress",       POINTER(EFI_IP_ADDRESS_INFO)),
    ("NextLayerProtocol",   UINT16),
    ("LocalPort",           UINT16),
    ("LocalPortRange",      UINT16),
    ("RemotePort",          UINT16),
    ("RemotePortRange",     UINT16)
  ]

EfiIPsecInBound       = 0
EfiIPsecOutBound      = 1
EFI_IPSEC_TRAFFIC_DIR = ENUM

EfiIPsecActionDiscard   = 0
EfiIPsecActionBypass    = 1
EfiIPsecActionProtect   = 2
EFI_IPSEC_ACTION        = ENUM

class EFI_IPSEC_SA_LIFETIME (Structure):
  _fields_ = [
    ("ByteCount",     UINT64),
    ("SoftLifetime",  UINT64),
    ("HardLifetime",  UINT64)
  ]

EfiIPsecTransport   = 0
EfiIPsecTunnel      = 1
EFI_IPSEC_MODE      = ENUM

EfiIPsecTunnelClearDf = 0
EfiIPsecTunnelSetDf   = 1
EfiIPsecTunnelCopyDf  = 2
EFI_IPSEC_TUNNEL_DF_OPTION  = ENUM

class EFI_IPSEC_TUNNEL_OPTION (Structure):
  _fields_ = [
    ("LocalTunnelAddress",  EFI_IP_ADDRESS),
    ("RemoteTunnelAddress", EFI_IP_ADDRESS),
    ("DF",                  EFI_IPSEC_TUNNEL_DF_OPTION)
  ]

EfiIPsecAH              = 0
EfiIPsecESP             = 1
EFI_IPSEC_PROTOCOL_TYPE = ENUM

class EFI_IPSEC_PROCESS_POLICY (Structure):
  _fields_ = [
    ("ExtSeqNum",     BOOLEAN),
    ("SeqOverflow",   BOOLEAN),
    ("FragCheck",     BOOLEAN),
    ("SaLifetime",    EFI_IPSEC_SA_LIFETIME),
    ("Mode",          EFI_IPSEC_MODE),
    ("TunnelOption",  POINTER(EFI_IPSEC_TUNNEL_OPTION)),
    ("Proto",         EFI_IPSEC_PROTOCOL_TYPE),
    ("AuthAlgoId",    UINT8),
    ("EncAlgoId",     UINT8)
  ]

class EFI_IPSEC_SA_ID (Structure):
  _fields_ = [
    ("Spi",         UINT32),
    ("Proto",       EFI_IPSEC_PROTOCOL_TYPE),
    ("DestAddress", EFI_IP_ADDRESS)
  ]

MAX_PEERID_LEN     = 128

class EFI_IPSEC_SPD_DATA (Structure):
  _fields_ = [
    ("Name",              UINT8 * MAX_PEERID_LEN),
    ("PackageFlag",       UINT32),
    ("TrafficDirection",  EFI_IPSEC_TRAFFIC_DIR),
    ("Action",            EFI_IPSEC_ACTION),
    ("ProcessingPolicy",  POINTER(EFI_IPSEC_PROCESS_POLICY)),
    ("SaIdCount",         UINTN),
    ("SaId",              EFI_IPSEC_SA_ID * 1)
  ]

class EFI_IPSEC_AH_ALGO_INFO (Structure):
  _fields_ = [
    ("AuthAlgoId",    UINT8),
    ("AuthKeyLength", UINTN),
    ("AuthKey",       PVOID)
  ]

class EFI_IPSEC_ESP_ALGO_INFO (Structure):
  _fields_ = [
    ("EncAlgoId",     UINT8),
    ("EncKeyLength",  UINTN),
    ("EncKey",        PVOID),
    ("AuthAlgoId",    UINT8),
    ("AuthKeyLength", UINTN),
    ("AuthKey",       PVOID)
  ]

class EFI_IPSEC_ALGO_INFO (Union):
  _fields_ = [
    ("AhAlgoInfo",  EFI_IPSEC_AH_ALGO_INFO),
    ("EspAlgoInfo", EFI_IPSEC_ESP_ALGO_INFO)
  ]

class EFI_IPSEC_SA_DATA (Structure):
  _fields_ = [
    ("Mode",              EFI_IPSEC_MODE),
    ("SNCount",           UINT64),
    ("AntiReplayWindows", UINT8),
    ("AlgoInfo",          EFI_IPSEC_ALGO_INFO),
    ("SaLifetime",        EFI_IPSEC_SA_LIFETIME),
    ("PathMTU",           UINT32),
    ("SpdSelector",       POINTER(EFI_IPSEC_SPD_SELECTOR)),
    ("ManualSet",         BOOLEAN),
  ]

class EFI_IPSEC_SA_DATA2 (Structure):
  _fields_ = [
    ("Mode",                      EFI_IPSEC_MODE),
    ("SNCount",                   UINT64),
    ("AntiReplayWindows",         UINT8),
    ("AlgoInfo",                  EFI_IPSEC_ALGO_INFO),
    ("SaLifetime",                EFI_IPSEC_SA_LIFETIME),
    ("PathMTU",                   UINT32),
    ("SpdSelector",               POINTER(EFI_IPSEC_SPD_SELECTOR)),
    ("ManualSet",                 BOOLEAN),
    ("TunnelSourceAddress",       EFI_IP_ADDRESS),
    ("TunnelDestinationAddress",  EFI_IP_ADDRESS)
  ]

class EFI_IPSEC_PAD_ID_Id (Union):
  _fields_ = [
    ("IpAddress", EFI_IP_ADDRESS_INFO),
    ("PeerId",    UINT8 * MAX_PEERID_LEN)
  ]

class EFI_IPSEC_PAD_ID (Structure):
  _fields_ = [
    ("PeerIdValid", BOOLEAN),
    ("Id",          EFI_IPSEC_PAD_ID_Id)
  ]

class EFI_IPSEC_CONFIG_SELECTOR (Union):
  _fields_ = [
    ("SpdSelector", EFI_IPSEC_SPD_SELECTOR),
    ("SaId",        EFI_IPSEC_SA_ID),
    ("PadId",       EFI_IPSEC_PAD_ID)
  ]

EfiIPsecAuthProtocolIKEv1     = 0
EfiIPsecAuthProtocolIKEv2     = 1
EfiIPsecAuthProtocolMaximum   = 2
EFI_IPSEC_AUTH_PROTOCOL_TYPE  = ENUM

EfiIPsecAuthMethodPreSharedSecret   = 0
EfiIPsecAuthMethodCertificates      = 1
EfiIPsecAuthMethodMaximum           = 2
EFI_IPSEC_AUTH_METHOD               = ENUM

class EFI_IPSEC_PAD_DATA (Structure):
  _fields_ = [
    ("AuthProtocol",        EFI_IPSEC_AUTH_PROTOCOL_TYPE),
    ("AuthMethod",          EFI_IPSEC_AUTH_METHOD),
    ("IkeIdFlag",           BOOLEAN),
    ("AuthDataSize",        UINTN),
    ("AuthData",            PVOID),
    ("RevocationDataSize",  UINTN),
    ("RevocationData",      PVOID)
  ]

EFI_IPSEC_CONFIG_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IPSEC_CONFIG_PROTOCOL), # IN *This
  EFI_IPSEC_CONFIG_DATA_TYPE,         # IN DataType,
  POINTER(EFI_IPSEC_CONFIG_SELECTOR), # IN *Selector,
  PVOID,                              # IN *Data,
  POINTER(EFI_IPSEC_CONFIG_SELECTOR)  # IN *InsertBefore   OPTIONAL
  )

EFI_IPSEC_CONFIG_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IPSEC_CONFIG_PROTOCOL), # IN      *This
  EFI_IPSEC_CONFIG_DATA_TYPE,         # IN      DataType,
  POINTER(EFI_IPSEC_CONFIG_SELECTOR), # IN      *Selector,
  POINTER(UINTN),                     # IN OUT  *DataSize
  PVOID                               #    OUT  *Data
  )

EFI_IPSEC_CONFIG_GET_NEXT_SELECTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IPSEC_CONFIG_PROTOCOL), # IN      *This
  EFI_IPSEC_CONFIG_DATA_TYPE,         # IN      DataType,
  POINTER(UINTN),                     # IN OUT  *SelectorSize,
  POINTER(EFI_IPSEC_CONFIG_SELECTOR)  # IN OUT  *Selector,
  )

EFI_IPSEC_CONFIG_REGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IPSEC_CONFIG_PROTOCOL), # IN *This
  EFI_IPSEC_CONFIG_DATA_TYPE,         # IN DataType,
  EFI_EVENT                           # IN Event
  )

EFI_IPSEC_CONFIG_UNREGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IPSEC_CONFIG_PROTOCOL), # IN *This
  EFI_IPSEC_CONFIG_DATA_TYPE,         # IN DataType,
  EFI_EVENT                           # IN Event
  )

EFI_IPSEC_CONFIG_PROTOCOL._fields_ = [
    ("SetData",               EFI_IPSEC_CONFIG_SET_DATA),
    ("GetData",               EFI_IPSEC_CONFIG_GET_DATA),
    ("GetNextSelector",       EFI_IPSEC_CONFIG_GET_NEXT_SELECTOR),
    ("RegisterDataNotify",    EFI_IPSEC_CONFIG_REGISTER_NOTIFY),
    ("UnregisterDataNotify",  EFI_IPSEC_CONFIG_UNREGISTER_NOTIFY)
  ]

