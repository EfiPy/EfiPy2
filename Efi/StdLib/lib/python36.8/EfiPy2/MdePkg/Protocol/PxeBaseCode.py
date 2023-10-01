# PxeBaseCode.py
#
# EfiPy2.MdePkg.Protocol.PxeBaseCode
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPxeBaseCodeProtocolGuid = \
  EFI_GUID (0x03c4e603, 0xac28, 0x11d3, (0x9a, 0x2d, 0x00, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_PXE_BASE_CODE_PROTOCOL (Structure):
  pass

EFI_PXE_BASE_CODE = EFI_PXE_BASE_CODE_PROTOCOL

DEFAULT_TTL = 16
DEFAULT_ToS = 0

class EFI_PXE_BASE_CODE_ICMP_ERROR_Echo (Structure):
  _fields_ = [
    ("Identifier",  UINT16),
    ("Sequence",    UINT16)
  ]

class EFI_PXE_BASE_CODE_ICMP_ERROR_u (Union):
  _fields_ = [
    ("reserved",  UINT32),
    ("Mtu",       UINT32),
    ("Pointer",   UINT32),
    ("Echo",      EFI_PXE_BASE_CODE_ICMP_ERROR_Echo)
  ]

class EFI_PXE_BASE_CODE_ICMP_ERROR (Structure):
  _fields_ = [
    ("Type",      UINT8),
    ("Code",      UINT8),
    ("Checksum",  UINT16),
    ("u",         EFI_PXE_BASE_CODE_ICMP_ERROR_u),
    ("Data",      UINT8 * 494)
  ]

class EFI_PXE_BASE_CODE_TFTP_ERROR (Structure):
  _fields_ = [
    ("ErrorCode",   UINT8),
    ("ErrorString", CHAR8 * 127)
  ]

EFI_PXE_BASE_CODE_MAX_IPCNT = 8

class EFI_PXE_BASE_CODE_IP_FILTER (Structure):
  _fields_ = [
    ("Filters",   UINT8),
    ("IpCnt",     UINT8),
    ("reserved",  UINT16),
    ("IpList",    EFI_IP_ADDRESS * EFI_PXE_BASE_CODE_MAX_IPCNT)
  ]

EFI_PXE_BASE_CODE_IP_FILTER_STATION_IP            = 0x0001
EFI_PXE_BASE_CODE_IP_FILTER_BROADCAST             = 0x0002
EFI_PXE_BASE_CODE_IP_FILTER_PROMISCUOUS           = 0x0004
EFI_PXE_BASE_CODE_IP_FILTER_PROMISCUOUS_MULTICAST = 0x0008

class EFI_PXE_BASE_CODE_ARP_ENTRY (Structure):
  _fields_ = [
    ("IpAddr",  EFI_IP_ADDRESS),
    ("MacAddr", EFI_MAC_ADDRESS)
  ]

class EFI_PXE_BASE_CODE_ROUTE_ENTRY (Structure):
  _fields_ = [
    ("IpAddr",      EFI_IP_ADDRESS),
    ("SubnetMask",  EFI_IP_ADDRESS),
    ("SubnetMask",  EFI_IP_ADDRESS)
  ]

EFI_PXE_BASE_CODE_UDP_PORT  = UINT16

EFI_PXE_BASE_CODE_UDP_OPFLAGS_ANY_SRC_IP    = 0x0001
EFI_PXE_BASE_CODE_UDP_OPFLAGS_ANY_SRC_PORT  = 0x0002
EFI_PXE_BASE_CODE_UDP_OPFLAGS_ANY_DEST_IP   = 0x0004
EFI_PXE_BASE_CODE_UDP_OPFLAGS_ANY_DEST_PORT = 0x0008
EFI_PXE_BASE_CODE_UDP_OPFLAGS_USE_FILTER    = 0x0010
EFI_PXE_BASE_CODE_UDP_OPFLAGS_MAY_FRAGMENT  = 0x0020

EFI_PXE_BASE_CODE_BOOT_TYPE_BOOTSTRAP         = 0
EFI_PXE_BASE_CODE_BOOT_TYPE_MS_WINNT_RIS      = 1
EFI_PXE_BASE_CODE_BOOT_TYPE_INTEL_LCM         = 2
EFI_PXE_BASE_CODE_BOOT_TYPE_DOSUNDI           = 3
EFI_PXE_BASE_CODE_BOOT_TYPE_NEC_ESMPRO        = 4
EFI_PXE_BASE_CODE_BOOT_TYPE_IBM_WSoD          = 5
EFI_PXE_BASE_CODE_BOOT_TYPE_IBM_LCCM          = 6
EFI_PXE_BASE_CODE_BOOT_TYPE_CA_UNICENTER_TNG  = 7
EFI_PXE_BASE_CODE_BOOT_TYPE_HP_OPENVIEW       = 8
EFI_PXE_BASE_CODE_BOOT_TYPE_ALTIRIS_9         = 9
EFI_PXE_BASE_CODE_BOOT_TYPE_ALTIRIS_10        = 10
EFI_PXE_BASE_CODE_BOOT_TYPE_ALTIRIS_11        = 11
EFI_PXE_BASE_CODE_BOOT_TYPE_NOT_USED_12       = 12
EFI_PXE_BASE_CODE_BOOT_TYPE_REDHAT_INSTALL    = 13
EFI_PXE_BASE_CODE_BOOT_TYPE_REDHAT_BOOT       = 14
EFI_PXE_BASE_CODE_BOOT_TYPE_REMBO             = 15
EFI_PXE_BASE_CODE_BOOT_TYPE_BEOBOOT           = 16

EFI_PXE_BASE_CODE_BOOT_TYPE_PXETEST   = 65535

EFI_PXE_BASE_CODE_BOOT_LAYER_MASK     = 0x7FFF
EFI_PXE_BASE_CODE_BOOT_LAYER_INITIAL  = 0x0000

if EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_IA32:
  EFI_PXE_CLIENT_SYSTEM_ARCHITECTURE    = 0x0006
elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_X64:
  EFI_PXE_CLIENT_SYSTEM_ARCHITECTURE    = 0x0007
elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_ARM:
  EFI_PXE_CLIENT_SYSTEM_ARCHITECTURE    = 0x000A
elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_AARCH64:
  EFI_PXE_CLIENT_SYSTEM_ARCHITECTURE    = 0x000B
elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_RISCV64:
  EFI_PXE_CLIENT_SYSTEM_ARCHITECTURE    = 0x001B
elif EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_LOONGARCH64:
  EFI_PXE_CLIENT_SYSTEM_ARCHITECTURE    = 0x0027

class EFI_PXE_BASE_CODE_SRVLIST (Structure):
  _fields_ = [
    ("Type",              UINT16),
    ("AcceptAnyResponse", BOOLEAN),
    ("Reserved",          UINT8),
    ("IpAddr",            EFI_IP_ADDRESS)
  ]

class EFI_PXE_BASE_CODE_DISCOVER_INFO (Structure):
  _fields_ = [
    ("UseMCast",      BOOLEAN),
    ("UseBCast",      BOOLEAN),
    ("UseUCast",      BOOLEAN),
    ("MustUseList",   BOOLEAN),
    ("ServerMCastIp", EFI_IP_ADDRESS),
    ("IpCnt",         UINT16),
    ("SrvList",       EFI_PXE_BASE_CODE_SRVLIST * 1)
  ]

EFI_PXE_BASE_CODE_TFTP_FIRST            = 0
EFI_PXE_BASE_CODE_TFTP_GET_FILE_SIZE    = 1
EFI_PXE_BASE_CODE_TFTP_READ_FILE        = 2
EFI_PXE_BASE_CODE_TFTP_WRITE_FILE       = 3
EFI_PXE_BASE_CODE_TFTP_READ_DIRECTORY   = 4
EFI_PXE_BASE_CODE_MTFTP_GET_FILE_SIZE   = 5
EFI_PXE_BASE_CODE_MTFTP_READ_FILE       = 6
EFI_PXE_BASE_CODE_MTFTP_READ_DIRECTORY  = 7
EFI_PXE_BASE_CODE_MTFTP_LAST            = 8
EFI_PXE_BASE_CODE_TFTP_OPCODE           = ENUM

class EFI_PXE_BASE_CODE_MTFTP_INFO (Structure):
  _fields_ = [
    ("MCastIp",         EFI_IP_ADDRESS),
    ("CPort",           EFI_PXE_BASE_CODE_UDP_PORT),
    ("SPort",           EFI_PXE_BASE_CODE_UDP_PORT),
    ("ListenTimeout",   UINT16),
    ("TransmitTimeout", UINT16)
  ]

class EFI_PXE_BASE_CODE_DHCPV4_PACKET (Structure):
  _fields_ = [
    ("BootpOpcode",     UINT8),
    ("BootpHwType",     UINT8),
    ("BootpHwAddrLen",  UINT8),
    ("BootpGateHops",   UINT8),
    ("BootpIdent",      UINT32),
    ("BootpSeconds",    UINT16),
    ("BootpFlags",      UINT16),
    ("BootpCiAddr",     UINT8 * 4),
    ("BootpYiAddr",     UINT8 * 4),
    ("BootpSiAddr",     UINT8 * 4),
    ("BootpGiAddr",     UINT8 * 4),
    ("BootpHwAddr",     UINT8 * 16),
    ("BootpSrvName",    UINT8 * 64),
    ("BootpBootFile",   UINT8 * 128),
    ("DhcpMagik",       UINT32),
    ("DhcpOptions",     UINT8 * 56)
  ]

class EFI_PXE_BASE_CODE_DHCPV6_PACKET (Structure):
  _fields_ = [
    ("MessageType",   UINT32, 8),
    ("TransactionId", UINT32, 24),
    ("DhcpOptions",   UINT8 * 1024)
  ]

class EFI_PXE_BASE_CODE_PACKET (Union):
  _fields_ = [
    ("Raw",     UINT8 * 1472),
    ("Dhcpv4",  EFI_PXE_BASE_CODE_DHCPV4_PACKET),
    ("Dhcpv6",  EFI_PXE_BASE_CODE_DHCPV6_PACKET)
  ]

EFI_PXE_BASE_CODE_MAX_ARP_ENTRIES   = 8
EFI_PXE_BASE_CODE_MAX_ROUTE_ENTRIES = 8

class EFI_PXE_BASE_CODE_MODE (Structure):
  _fields_ = [
    ("Started",             BOOLEAN),
    ("Ipv6Available",       BOOLEAN),
    ("Ipv6Supported",       BOOLEAN),
    ("UsingIpv6",           BOOLEAN),
    ("BisSupported",        BOOLEAN),
    ("BisDetected",         BOOLEAN),
    ("AutoArp",             BOOLEAN),
    ("SendGUID",            BOOLEAN),
    ("DhcpDiscoverValid",   BOOLEAN),
    ("DhcpAckReceived",     BOOLEAN),
    ("ProxyOfferReceived",  BOOLEAN),
    ("PxeDiscoverValid",    BOOLEAN),
    ("PxeReplyReceived",    BOOLEAN),
    ("PxeBisReplyReceived", BOOLEAN),
    ("IcmpErrorReceived",   BOOLEAN),
    ("TftpErrorReceived",   BOOLEAN),
    ("MakeCallbacks",       BOOLEAN),
    ("TTL",                 UINT8),
    ("ToS",                 UINT8),
    ("StationIp",           EFI_IP_ADDRESS),
    ("SubnetMask",          EFI_IP_ADDRESS),
    ("DhcpDiscover",        EFI_PXE_BASE_CODE_PACKET),
    ("DhcpAck",             EFI_PXE_BASE_CODE_PACKET),
    ("ProxyOffer",          EFI_PXE_BASE_CODE_PACKET),
    ("PxeDiscover",         EFI_PXE_BASE_CODE_PACKET),
    ("PxeReply",            EFI_PXE_BASE_CODE_PACKET),
    ("PxeBisReply",         EFI_PXE_BASE_CODE_PACKET),
    ("IpFilter",            EFI_PXE_BASE_CODE_IP_FILTER),
    ("ArpCacheEntries",     UINT32),
    ("ArpCache",            EFI_PXE_BASE_CODE_ARP_ENTRY * EFI_PXE_BASE_CODE_MAX_ARP_ENTRIES),
    ("RouteTableEntries",   UINT32),
    ("RouteTable",          EFI_PXE_BASE_CODE_ROUTE_ENTRY * EFI_PXE_BASE_CODE_MAX_ROUTE_ENTRIES),
    ("IcmpError",           EFI_PXE_BASE_CODE_ICMP_ERROR),
    ("TftpError",           EFI_PXE_BASE_CODE_TFTP_ERROR)
  ]

EFI_PXE_BASE_CODE_START = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN *This
  BOOLEAN                               # IN UseIpv6
  )

EFI_PXE_BASE_CODE_STOP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL)   # IN *This
  )

EFI_PXE_BASE_CODE_DHCP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN *This
  BOOLEAN                               # IN SortOffers
  )

EFI_PXE_BASE_CODE_DISCOVER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),      # IN *This
  UINT16,                                   # IN Type,
  POINTER(UINT16),                          # IN *Layer,
  BOOLEAN,                                  # IN UseBis,
  POINTER(EFI_PXE_BASE_CODE_DISCOVER_INFO)  # IN *Info   OPTIONAL
  )

EFI_PXE_BASE_CODE_MTFTP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),    # IN      *This
  EFI_PXE_BASE_CODE_TFTP_OPCODE,          # IN      Operation,
  PVOID,                                  # IN OUT  *BufferPtr OPTIONAL,
  BOOLEAN,                                # IN      Overwrite,
  POINTER(UINT64),                        # IN OUT  *BufferSize,
  POINTER(UINTN),                         # IN      *BlockSize OPTIONAL,
  POINTER(EFI_IP_ADDRESS),                # IN      *ServerIp,
  POINTER(UINT8),                         # IN      *Filename  OPTIONAL,
  POINTER(EFI_PXE_BASE_CODE_MTFTP_INFO),  # IN      *Info      OPTIONAL,
  BOOLEAN                                 # IN      DontUseBuffer
  )

EFI_PXE_BASE_CODE_UDP_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN      *This
  UINT16,                               # IN      OpFlags,
  POINTER(EFI_IP_ADDRESS),              # IN      *DestIp,
  POINTER(EFI_PXE_BASE_CODE_UDP_PORT),  # IN      *DestPort,
  POINTER(EFI_IP_ADDRESS),              # IN      *GatewayIp,  OPTIONAL
  POINTER(EFI_IP_ADDRESS),              # IN      *SrcIp,      OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_UDP_PORT),  # IN OUT  *SrcPort,    OPTIONAL
  POINTER(UINTN),                       # IN      *HeaderSize, OPTIONAL
  PVOID,                                # IN      *HeaderPtr,  OPTIONAL
  POINTER(UINTN),                       # IN      *BufferSize,
  PVOID                                 # IN      *BufferPtr
  )

EFI_PXE_BASE_CODE_UDP_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN     *This
  UINT16,                               # IN     OpFlags,
  POINTER(EFI_IP_ADDRESS),              # IN OUT *DestIp,     OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_UDP_PORT),  # IN OUT *DestPort,   OPTIONAL
  POINTER(EFI_IP_ADDRESS),              # IN OUT *SrcIp,      OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_UDP_PORT),  # IN OUT *SrcPort,    OPTIONAL
  POINTER(UINTN),                       # IN     *HeaderSize, OPTIONAL
  PVOID,                                # IN     *HeaderPtr,  OPTIONAL
  POINTER(UINTN),                       # IN OUT *BufferSize,
  PVOID                                 # IN     *BufferPtr
  )

EFI_PXE_BASE_CODE_SET_IP_FILTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN *This
  POINTER(EFI_PXE_BASE_CODE_IP_FILTER)  # IN *NewFilter
  )

EFI_PXE_BASE_CODE_ARP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN *This
  POINTER(EFI_IP_ADDRESS),              # IN *IpAddr
  POINTER(EFI_MAC_ADDRESS)              # IN *MacAddr OPTIONAL
  )

EFI_PXE_BASE_CODE_SET_PARAMETERS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN *This
  POINTER(BOOLEAN),                     # IN *NewAutoArp,     OPTIONAL
  POINTER(BOOLEAN),                     # IN *NewSendGUID,    OPTIONAL
  POINTER(UINT8),                       # IN *NewTTL,         OPTIONAL
  POINTER(UINT8),                       # IN *NewToS,         OPTIONAL
  POINTER(BOOLEAN)                      # IN *NewMakeCallback OPTIONAL
  )

EFI_PXE_BASE_CODE_SET_STATION_IP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),  # IN *This
  POINTER(EFI_IP_ADDRESS),              # IN *NewStationIp,   OPTIONAL
  POINTER(EFI_IP_ADDRESS)               # IN *NewSubnetMask   OPTIONAL
  )

EFI_PXE_BASE_CODE_SET_PACKETS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PXE_BASE_CODE_PROTOCOL),          # IN *This
  POINTER(BOOLEAN),                             #    *NewDhcpDiscoverValid,   OPTIONAL
  POINTER(BOOLEAN),                             #    *NewDhcpAckReceived,     OPTIONAL
  POINTER(BOOLEAN),                             #    *NewProxyOfferReceived,  OPTIONAL
  POINTER(BOOLEAN),                             #    *NewPxeDiscoverValid,    OPTIONAL
  POINTER(BOOLEAN),                             #    *NewPxeReplyReceived,    OPTIONAL
  POINTER(BOOLEAN),                             #    *NewPxeBisReplyReceived, OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_PACKET),            # IN *NewDhcpDiscover,        OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_PACKET),            # IN *NewDhcpAck,             OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_PACKET),            # IN *NewProxyOffer,          OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_PACKET),            # IN *NewPxeDiscover,         OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_PACKET),            # IN *NewPxeReply,            OPTIONAL
  POINTER(EFI_PXE_BASE_CODE_PACKET)             # IN *NewPxeBisReply          OPTIONAL
  )

EFI_PXE_BASE_CODE_PROTOCOL_REVISION   = 0x00010000

EFI_PXE_BASE_CODE_INTERFACE_REVISION  = EFI_PXE_BASE_CODE_PROTOCOL_REVISION

EFI_PXE_BASE_CODE_PROTOCOL._fields_ = [
    ("Revision",      UINT64),
    ("Start",         EFI_PXE_BASE_CODE_START),
    ("Stop",          EFI_PXE_BASE_CODE_STOP),
    ("Dhcp",          EFI_PXE_BASE_CODE_DHCP),
    ("Discover",      EFI_PXE_BASE_CODE_DISCOVER),
    ("Mtftp",         EFI_PXE_BASE_CODE_MTFTP),
    ("UdpWrite",      EFI_PXE_BASE_CODE_UDP_WRITE),
    ("UdpRead",       EFI_PXE_BASE_CODE_UDP_READ ),
    ("SetIpFilter",   EFI_PXE_BASE_CODE_SET_IP_FILTER),
    ("Arp",           EFI_PXE_BASE_CODE_ARP),
    ("SetParameters", EFI_PXE_BASE_CODE_SET_PARAMETERS),
    ("SetStationIp",  EFI_PXE_BASE_CODE_SET_STATION_IP),
    ("SetPackets",    EFI_PXE_BASE_CODE_SET_PACKETS),
    ("Mode",          POINTER(EFI_PXE_BASE_CODE_MODE))
  ]

