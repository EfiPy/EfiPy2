# SimpleNetwork.py
#
# EfiPy2.MdePkg.Protocol.SimpleNetwork
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSimpleNetworkProtocolGuid = \
  EFI_GUID (0xA19832B9, 0xAC25, 0x11D3, (0x9A, 0x2D, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_SIMPLE_NETWORK_PROTOCOL (Structure):
  pass

class EFI_NETWORK_STATISTICS (Structure):
  _fields_ = [
    ("RxTotalFrames",       UINT64),
    ("RxGoodFrames",        UINT64),
    ("RxUndersizeFrames",   UINT64),
    ("RxOversizeFrames",    UINT64),
    ("RxDroppedFrames",     UINT64),
    ("RxUnicastFrames",     UINT64),
    ("RxBroadcastFrames",   UINT64),
    ("RxMulticastFrames",   UINT64),
    ("RxCrcErrorFrames",    UINT64),
    ("RxTotalBytes",        UINT64),
    ("TxTotalFrames",       UINT64),
    ("TxGoodFrames",        UINT64),
    ("TxUndersizeFrames",   UINT64),
    ("TxOversizeFrames",    UINT64),
    ("TxDroppedFrames",     UINT64),
    ("TxUnicastFrames",     UINT64),
    ("TxBroadcastFrames",   UINT64),
    ("TxMulticastFrames",   UINT64),
    ("TxCrcErrorFrames",    UINT64),
    ("TxTotalBytes",        UINT64),
    ("Collisions",          UINT64),
    ("UnsupportedProtocol", UINT64),
    ("RxDuplicatedFrames",  UINT64),
    ("RxDecryptErrorFrames",UINT64),
    ("TxErrorFrames",       UINT64),
    ("TxRetryFrames",       UINT64)
  ]

EfiSimpleNetworkStopped      = 0
EfiSimpleNetworkStarted      = 1
EfiSimpleNetworkInitialized  = 2
EfiSimpleNetworkMaxState     = 3
EFI_SIMPLE_NETWORK_STATE     = ENUM

EFI_SIMPLE_NETWORK_RECEIVE_UNICAST                = 0x01
EFI_SIMPLE_NETWORK_RECEIVE_MULTICAST              = 0x02
EFI_SIMPLE_NETWORK_RECEIVE_BROADCAST              = 0x04
EFI_SIMPLE_NETWORK_RECEIVE_PROMISCUOUS            = 0x08
EFI_SIMPLE_NETWORK_RECEIVE_PROMISCUOUS_MULTICAST  = 0x10

EFI_SIMPLE_NETWORK_RECEIVE_INTERRUPT              = 0x01
EFI_SIMPLE_NETWORK_TRANSMIT_INTERRUPT             = 0x02
EFI_SIMPLE_NETWORK_COMMAND_INTERRUPT              = 0x04
EFI_SIMPLE_NETWORK_SOFTWARE_INTERRUPT             = 0x08

MAX_MCAST_FILTER_CNT                              = 16

class EFI_SIMPLE_NETWORK_MODE (Structure):
  _fields_ = [
    ("State",                 UINT32),
    ("HwAddressSize",         UINT32),
    ("MediaHeaderSize",       UINT32),
    ("MaxPacketSize",         UINT32),
    ("NvRamSize",             UINT32),
    ("NvRamAccessSize",       UINT32),
    ("ReceiveFilterMask",     UINT32),
    ("ReceiveFilterSetting",  UINT32),
    ("MaxMCastFilterCount",   UINT32),
    ("MCastFilterCount",      UINT32),
    ("MCastFilter",           EFI_MAC_ADDRESS * MAX_MCAST_FILTER_CNT),
    ("CurrentAddress",        EFI_MAC_ADDRESS),
    ("BroadcastAddress",      EFI_MAC_ADDRESS),
    ("PermanentAddress",      EFI_MAC_ADDRESS),
    ("IfType",                UINT8),
    ("MacAddressChangeable",  BOOLEAN),
    ("MultipleTxSupported",   BOOLEAN),
    ("MediaPresentSupported", BOOLEAN),
    ("MediaPresent",          BOOLEAN)
  ]

EFI_SIMPLE_NETWORK_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL)  # IN  *This
  )

EFI_SIMPLE_NETWORK_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL)  # IN  *This
  )

EFI_SIMPLE_NETWORK_INITIALIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN  *This
  UINTN,                                # IN ExtraRxBufferSize  OPTIONAL,
  UINTN                                 # IN ExtraTxBufferSize  OPTIONAL
  )

EFI_SIMPLE_NETWORK_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN  *This
  BOOLEAN                               # IN ExtendedVerification
  )

EFI_SIMPLE_NETWORK_SHUTDOWN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL)  # IN  *This
  )

EFI_SIMPLE_NETWORK_RECEIVE_FILTERS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN *This
  UINT32,                               # IN Enable,
  UINT32,                               # IN Disable,
  BOOLEAN,                              # IN ResetMCastFilter,
  UINTN,                                # IN MCastFilterCnt     OPTIONAL,
  POINTER(EFI_MAC_ADDRESS)              # IN *MCastFilter OPTIONAL
  )

EFI_SIMPLE_NETWORK_STATION_ADDRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN *This
  BOOLEAN,                              # IN ResetMCastFilter,
  POINTER(EFI_MAC_ADDRESS)              # IN *New OPTIONAL
  )

EFI_SIMPLE_NETWORK_STATISTICS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN      *This
  BOOLEAN,                              # IN      Reset,
  POINTER(UINTN),                       # IN  OUT *StatisticsSize   OPTIONAL,
  POINTER(EFI_NETWORK_STATISTICS)       #     OUT *StatisticsTable  OPTIONAL
  )

EFI_SIMPLE_NETWORK_MCAST_IP_TO_MAC = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN      *This
  BOOLEAN,                              # IN      IPv6,
  POINTER(EFI_IP_ADDRESS),              # IN      *IP,
  POINTER(EFI_MAC_ADDRESS)              #     OUT *MAX
  )

EFI_SIMPLE_NETWORK_NVDATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN      *This
  BOOLEAN,                              # IN      ReadWrite,
  UINTN,                                # IN      Offset,
  UINTN,                                # IN      BufferSize,
  PVOID                                 # IN OUT  *Buffer
  )

EFI_SIMPLE_NETWORK_GET_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN      *This
  POINTER(UINT32),                      #    OUT  *InterruptStatus OPTIONAL,
  POINTER(PVOID)                        # IN OUT  **TxBuf OPTIONAL
  )

EFI_SIMPLE_NETWORK_TRANSMIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN *This
  UINTN,                                # IN HeaderSize,
  UINTN,                                # IN BufferSize,
  PVOID,                                # IN *Buffer,
  POINTER(EFI_MAC_ADDRESS),             # IN *SrcAddr  OPTIONAL,
  POINTER(EFI_MAC_ADDRESS),             # IN *DestAddr OPTIONAL,
  POINTER(UINT16)                       # IN *Protocol OPTIONAL
  )

EFI_SIMPLE_NETWORK_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_NETWORK_PROTOCOL), # IN      *This
  POINTER(UINTN),                       # OUT     *HeaderSize OPTIONAL,
  POINTER(UINTN),                       # IN OUT  *BufferSize,
  PVOID,                                # OUT     *Buffer,
  POINTER(EFI_MAC_ADDRESS),             # OUT     *SrcAddr    OPTIONAL,
  POINTER(EFI_MAC_ADDRESS),             # OUT     *DestAddr   OPTIONAL,
  POINTER(UINT16)                       # OUT     *Protocol   OPTIONAL
  )

EFI_SIMPLE_NETWORK_PROTOCOL_REVISION  = 0x00010000

EFI_SIMPLE_NETWORK_INTERFACE_REVISION  = EFI_SIMPLE_NETWORK_PROTOCOL_REVISION

EFI_SIMPLE_NETWORK_PROTOCOL._fields_ = [
    ("Revision",        UINT64),
    ("Start",           EFI_SIMPLE_NETWORK_START),
    ("Stop",            EFI_SIMPLE_NETWORK_STOP),
    ("Initialize",      EFI_SIMPLE_NETWORK_INITIALIZE),
    ("Reset",           EFI_SIMPLE_NETWORK_RESET),
    ("Shutdown",        EFI_SIMPLE_NETWORK_SHUTDOWN),
    ("ReceiveFilters",  EFI_SIMPLE_NETWORK_RECEIVE_FILTERS),
    ("StationAddress",  EFI_SIMPLE_NETWORK_STATION_ADDRESS),
    ("Statistics",      EFI_SIMPLE_NETWORK_STATISTICS),
    ("MCastIpToMac",    EFI_SIMPLE_NETWORK_MCAST_IP_TO_MAC),
    ("NvData",          EFI_SIMPLE_NETWORK_NVDATA),
    ("GetStatus",       EFI_SIMPLE_NETWORK_GET_STATUS),
    ("Transmit",        EFI_SIMPLE_NETWORK_TRANSMIT),
    ("Receive",         EFI_SIMPLE_NETWORK_RECEIVE),
    ("WaitForPacket",   EFI_EVENT),
    ("Mode",            POINTER(EFI_SIMPLE_NETWORK_MODE))
  ]

