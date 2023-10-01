# Dhcp.py
#
# EfiPy2.MdePkg.IndustryStandard.Dhcp
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

DHCP4_TAG_PAD              = 0      # Pad Option
DHCP4_TAG_EOP              = 255    # End Option
DHCP4_TAG_NETMASK          = 1      # Subnet Mask
DHCP4_TAG_TIME_OFFSET      = 2      # Time Offset from UTC
DHCP4_TAG_ROUTER           = 3      # Router option,
DHCP4_TAG_TIME_SERVER      = 4      # Time Server
DHCP4_TAG_NAME_SERVER      = 5      # Name Server
DHCP4_TAG_DNS_SERVER       = 6      # Domain Name Server
DHCP4_TAG_LOG_SERVER       = 7      # Log Server
DHCP4_TAG_COOKIE_SERVER    = 8      # Cookie Server
DHCP4_TAG_LPR_SERVER       = 9      # LPR Print Server
DHCP4_TAG_IMPRESS_SERVER   = 10     # Impress Server
DHCP4_TAG_RL_SERVER        = 11     # Resource Location Server
DHCP4_TAG_HOSTNAME         = 12     # Host Name
DHCP4_TAG_BOOTFILE_LEN     = 13     # Boot File Size
DHCP4_TAG_DUMP             = 14     # Merit Dump File
DHCP4_TAG_DOMAINNAME       = 15     # Domain Name
DHCP4_TAG_SWAP_SERVER      = 16     # Swap Server
DHCP4_TAG_ROOTPATH         = 17     # Root path
DHCP4_TAG_EXTEND_PATH      = 18     # Extensions Path
DHCP4_TAG_IPFORWARD        = 19     # IP Forwarding Enable/Disable
DHCP4_TAG_NONLOCAL_SRR     = 20     # on-Local Source Routing Enable/Disable
DHCP4_TAG_POLICY_SRR       = 21     # Policy Filter
DHCP4_TAG_EMTU             = 22     # Maximum Datagram Reassembly Size
DHCP4_TAG_TTL              = 23     # Default IP Time-to-live
DHCP4_TAG_PATHMTU_AGE      = 24     # Path MTU Aging Timeout
DHCP4_TAG_PATHMTU_PLATEAU  = 25     # Path MTU Plateau Table
DHCP4_TAG_IFMTU            = 26     # Interface MTU
DHCP4_TAG_SUBNET_LOCAL     = 27     # All Subnets are Local
DHCP4_TAG_BROADCAST        = 28     # Broadcast Address
DHCP4_TAG_DISCOVER_MASK    = 29     # Perform Mask Discovery
DHCP4_TAG_SUPPLY_MASK      = 30     # Mask Supplier
DHCP4_TAG_DISCOVER_ROUTE   = 31     # Perform Router Discovery
DHCP4_TAG_ROUTER_SOLICIT   = 32     # Router Solicitation Address
DHCP4_TAG_STATIC_ROUTE     = 33     # Static Route
DHCP4_TAG_TRAILER          = 34     # Trailer Encapsulation
DHCP4_TAG_ARPAGE           = 35     # ARP Cache Timeout
DHCP4_TAG_ETHER_ENCAP      = 36     # Ethernet Encapsulation
DHCP4_TAG_TCP_TTL          = 37     # TCP Default TTL
DHCP4_TAG_KEEP_INTERVAL    = 38     # TCP Keepalive Interval
DHCP4_TAG_KEEP_GARBAGE     = 39     # TCP Keepalive Garbage
DHCP4_TAG_NIS_DOMAIN       = 40     # Network Information Service Domain
DHCP4_TAG_NIS_SERVER       = 41     # Network Information Servers
DHCP4_TAG_NTP_SERVER       = 42     # Network Time Protocol Servers
DHCP4_TAG_VENDOR           = 43     # Vendor Specific Information
DHCP4_TAG_NBNS             = 44     # NetBIOS over TCP/IP Name Server
DHCP4_TAG_NBDD             = 45     # NetBIOS Datagram Distribution Server
DHCP4_TAG_NBTYPE           = 46     # NetBIOS over TCP/IP Node Type
DHCP4_TAG_NBSCOPE          = 47     # NetBIOS over TCP/IP Scope
DHCP4_TAG_XFONT            = 48     # X Window System Font Server
DHCP4_TAG_XDM              = 49     # X Window System Display Manager
DHCP4_TAG_REQUEST_IP       = 50     # Requested IP Address
DHCP4_TAG_LEASE            = 51     # IP Address Lease Time
DHCP4_TAG_OVERLOAD         = 52     # Option Overload
DHCP4_TAG_MSG_TYPE         = 53     # DHCP Message Type
DHCP4_TAG_SERVER_ID        = 54     # Server Identifier
DHCP4_TAG_PARA_LIST        = 55     # Parameter Request List
DHCP4_TAG_MESSAGE          = 56     # Message
DHCP4_TAG_MAXMSG           = 57     # Maximum DHCP Message Size
DHCP4_TAG_T1               = 58     # Renewal (T1) Time Value
DHCP4_TAG_T2               = 59     # Rebinding (T2) Time Value
DHCP4_TAG_VENDOR_CLASS_ID  = 60     # Vendor class identifier
DHCP4_TAG_CLIENT_ID        = 61     # Client-identifier
DHCP4_TAG_NISPLUS          = 64     # Network Information Service+ Domain
DHCP4_TAG_NISPLUS_SERVER   = 65     # Network Information Service+ Servers
DHCP4_TAG_TFTP             = 66     # TFTP server name
DHCP4_TAG_BOOTFILE         = 67     # Bootfile name
DHCP4_TAG_MOBILEIP         = 68     # Mobile IP Home Agent
DHCP4_TAG_SMTP             = 69     # Simple Mail Transport Protocol Server
DHCP4_TAG_POP3             = 70     # Post Office Protocol (POP3) Server
DHCP4_TAG_NNTP             = 71     # Network News Transport Protocol Server
DHCP4_TAG_WWW              = 72     # Default World Wide Web (WWW) Server
DHCP4_TAG_FINGER           = 73     # Default Finger Server
DHCP4_TAG_IRC              = 74     # Default Internet Relay Chat (IRC) Server
DHCP4_TAG_STTALK           = 75     # StreetTalk Server
DHCP4_TAG_STDA             = 76     # StreetTalk Directory Assistance Server
DHCP4_TAG_USER_CLASS_ID    = 77     # User class identifier
DHCP4_TAG_ARCH             = 93     # Client System Architecture Type, RFC 4578
DHCP4_TAG_UNDI             = 94     # Client Network Interface Identifier, RFC 4578
DHCP4_TAG_UUID             = 97     # Client Machine Identifier, RFC 4578
DHCP4_TAG_CLASSLESS_ROUTE  = 121    # Classless Route

Dhcp6MsgSolicit     = 1
Dhcp6MsgAdvertise   = 2
Dhcp6MsgRequest     = 3
Dhcp6MsgConfirm     = 4
Dhcp6MsgRenew       = 5
Dhcp6MsgRebind      = 6
Dhcp6MsgReply       = 7
Dhcp6MsgRelease     = 8
Dhcp6MsgDecline     = 9
Dhcp6MsgReconfigure = 10
Dhcp6MsgInfoRequest = 11
DHCP6_MSG_TYPE = ENUM

Dhcp6OptClientId          = 1
Dhcp6OptServerId          = 2
Dhcp6OptIana              = 3
Dhcp6OptIata              = 4
Dhcp6OptIaAddr            = 5
Dhcp6OptRequestOption     = 6
Dhcp6OptPreference        = 7
Dhcp6OptElapsedTime       = 8
Dhcp6OptReplayMessage     = 9
Dhcp6OptAuthentication    = 11
Dhcp6OptServerUnicast     = 12
Dhcp6OptStatusCode        = 13
Dhcp6OptRapidCommit       = 14
Dhcp6OptUserClass         = 15
Dhcp6OptVendorClass       = 16
Dhcp6OptVendorInfo        = 17
Dhcp6OptInterfaceId       = 18
Dhcp6OptReconfigMessage   = 19
Dhcp6OptReconfigureAccept = 20
DHCP6_OPT_CODE = ENUM

Dhcp6StsSuccess      = 0
Dhcp6StsUnspecFail   = 1
Dhcp6StsNoAddrsAvail = 2
Dhcp6StsNoBinding    = 3
Dhcp6StsNotOnLink    = 4
Dhcp6StsUseMulticast = 5
DHCP6_STS_CODE = ENUM

Dhcp6DuidTypeLlt  = 1
Dhcp6DuidTypeEn   = 2
Dhcp6DuidTypeLl   = 3
Dhcp6DuidTypeUuid = 4
DHCP6_DUID_TYPE = ENUM

DHCP6_SOL_MAX_DELAY  = 1
DHCP6_SOL_IRT        = 1
DHCP6_SOL_MRC        = 0
DHCP6_SOL_MRT        = 120
DHCP6_SOL_MRD        = 0

DHCP6_REQ_IRT  = 1
DHCP6_REQ_MRC  = 10
DHCP6_REQ_MRT  = 30
DHCP6_REQ_MRD  = 0

DHCP6_CNF_MAX_DELAY  = 1
DHCP6_CNF_IRT        = 1
DHCP6_CNF_MRC        = 0
DHCP6_CNF_MRT        = 4
DHCP6_CNF_MRD        = 10

DHCP6_REN_IRT  = 10
DHCP6_REN_MRC  = 0
DHCP6_REN_MRT  = 600
DHCP6_REN_MRD  = 0

DHCP6_REB_IRT  = 10
DHCP6_REB_MRC  = 0
DHCP6_REB_MRT  = 600
DHCP6_REB_MRD  = 0

DHCP6_INF_MAX_DELAY  = 1
DHCP6_INF_IRT        = 1
DHCP6_INF_MRC        = 0
DHCP6_INF_MRT        = 120
DHCP6_INF_MRD        = 0

DHCP6_REL_IRT  = 1
DHCP6_REL_MRC  = 5
DHCP6_REL_MRT  = 0
DHCP6_REL_MRD  = 0

DHCP6_DEC_IRT  = 1
DHCP6_DEC_MRC  = 5
DHCP6_DEC_MRT  = 0
DHCP6_DEC_MRD  = 0

DHCP6_OPT_CLIENT_ID        = 1     # Client Identifier Option
DHCP6_OPT_SERVER_ID        = 2     # Server Identifier Option
DHCP6_OPT_IA_NA            = 3     # The Identity Association for Non-temporary Addresses option
DHCP6_OPT_IA_TA            = 4     # The Identity Association for the Temporary Addresses
DHCP6_OPT_IAADDR           = 5     # IA Address option
DHCP6_OPT_ORO              = 6     # Request option
DHCP6_OPT_PREFERENCE       = 7     # Preference option
DHCP6_OPT_ELAPSED_TIME     = 8     # Elapsed Time Option
DHCP6_OPT_REPLAY_MSG       = 9     # Relay Message option
DHCP6_OPT_AUTH             = 11    # Authentication option
DHCP6_OPT_UNICAST          = 12    # Server Unicast Option
DHCP6_OPT_STATUS_CODE      = 13    # Status Code Option
DHCP6_OPT_RAPID_COMMIT     = 14    # Rapid Commit option
DHCP6_OPT_USER_CLASS       = 15    # User Class option
DHCP6_OPT_VENDOR_CLASS     = 16    # Vendor Class Option
DHCP6_OPT_VENDOR_OPTS      = 17    # Vendor-specific Information Option
DHCP6_OPT_INTERFACE_ID     = 18    # Interface-Id Option
DHCP6_OPT_RECONFIG_MSG     = 19    # Reconfigure Message Option
DHCP6_OPT_RECONFIG_ACCEPT  = 20    # Reconfigure Accept Option
DHCP6_OPT_DNS_SERVERS      = 23    # DNS Configuration options, RFC 3646
DHCP6_OPT_BOOT_FILE_URL    = 59    # Assigned by IANA, RFC 5970
DHCP6_OPT_BOOT_FILE_PARAM  = 60    # Assigned by IANA, RFC 5970
DHCP6_OPT_ARCH             = 61    # Assigned by IANA, RFC 5970
DHCP6_OPT_UNDI             = 62    # Assigned by IANA, RFC 5970

# 
PXE_CLIENT_ARCH_X86_BIOS     = 0x0000          # x86 BIOS for PXE
PXE_CLIENT_ARCH_IPF          = 0x0002          # Itanium for PXE
PXE_CLIENT_ARCH_IA32         = 0x0006          # x86 uefi for PXE
PXE_CLIENT_ARCH_X64          = 0x0007          # x64 uefi for PXE
PXE_CLIENT_ARCH_EBC          = 0x0009          # EBC for PXE
PXE_CLIENT_ARCH_ARM          = 0x000A          # Arm uefi 32 for PXE
PXE_CLIENT_ARCH_AARCH64      = 0x000B          # Arm uefi 64 for PXE
PXE_CLIENT_ARCH_RISCV32      = 0x0019          # RISC-V uefi 32 for PXE
PXE_CLIENT_ARCH_RISCV64      = 0x001B          # RISC-V uefi 64 for PXE
PXE_CLIENT_ARCH_RISCV128     = 0x001D          # RISC-V uefi 128 for PXE
PXE_CLIENT_ARCH_LOONGARCH32  = 0x0025          # LoongArch uefi 32 for PXE
PXE_CLIENT_ARCH_LOONGARCH64  = 0x0027          # LoongArch uefi 64 for PXE

HTTP_CLIENT_ARCH_IA32         = 0x000F          # x86 uefi boot from http
HTTP_CLIENT_ARCH_X64          = 0x0010          # x64 uefi boot from http
HTTP_CLIENT_ARCH_EBC          = 0x0011          # EBC boot from http
HTTP_CLIENT_ARCH_ARM          = 0x0012          # Arm uefi 32 boot from http
HTTP_CLIENT_ARCH_AARCH64      = 0x0013          # Arm uefi 64 boot from http
HTTP_CLIENT_ARCH_RISCV32      = 0x001A          # RISC-V uefi 32 boot from http
HTTP_CLIENT_ARCH_RISCV64      = 0x001C          # RISC-V uefi 64 boot from http
HTTP_CLIENT_ARCH_RISCV128     = 0x001E          # RISC-V uefi 128 boot from http
HTTP_CLIENT_ARCH_LOONGARCH32  = 0x0026          # LoongArch uefi 32 boot from http
HTTP_CLIENT_ARCH_LOONGARCH64  = 0x0028          # LoongArch uefi 64 boot from http

