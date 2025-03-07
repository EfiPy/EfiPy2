# DevicePath.py
#
# EfiPy2.MdePkg.Protocol.DevicePath
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Guid.PcAnsi       import                    \
                                       EFI_PC_ANSI_GUID,       \
                                       EFI_VT_100_GUID,        \
                                       EFI_VT_100_PLUS_GUID,   \
                                       EFI_VT_UTF8_GUID,       \
                                       EFI_SAS_DEVICE_PATH_GUID

from EfiPy2.MdePkg.IndustryStandard.Bluetooth  import  BLUETOOTH_ADDRESS
from EfiPy2.MdePkg.IndustryStandard.Acpi       import  EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_DISK_REGION_VOLATILE,    \
                                                       EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_CD_REGION_VOLATILE,      \
                                                       EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_DISK_REGION_PERSISTENT,  \
                                                       EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_CD_REGION_PERSISTENT
                                                      

gEfiDevicePathProtocolGuid = EFI_GUID( 0x9576e91, 0x6d3f, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b))

class EFIPY_DEVICE_PATH_STRUCTURE (Structure):
  _pack_          = 1
  DisplayOnly     = False
  AllowShortcuts  = False

class EFIPY_DEVICE_PATH_UNION (Union):
  _pack_ = 1

class EFI_DEVICE_PATH_PROTOCOL (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8),
    ("SubType", UINT8),
    ("Length",  UINT16)
    ]

  def NextDevicePathNode (self):
    return EFI_DEVICE_PATH_PROTOCOL.from_address (addressof(self) + self.Length)

  def IsDevicePathEndType (self):
    return True

  def IsDevicePathEnd (self):
    return True

  def IsDevicePathEndInstance (self):
    return True

  def __str__ (self):
    return u""

EFI_DEVICE_PATH = EFI_DEVICE_PATH_PROTOCOL

HARDWARE_DEVICE_PATH      = 0x01

HW_PCI_DP                 = 0x01

class PCI_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_DEVICE_PATH_PROTOCOL),
    ("Function",  UINT8),
    ("Device",    UINT8)
    ]

HW_PCCARD_DP              = 0x02

class PCCARD_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("FunctionNumber",  UINT8)
    ]

HW_MEMMAP_DP              = 0x03

class MEMMAP_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("MemoryType",      UINT32),
    ("StartingAddress", EFI_PHYSICAL_ADDRESS),
    ("EndingAddress",   EFI_PHYSICAL_ADDRESS)
    ]

HW_VENDOR_DP              = 0x04

class VENDOR_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Guid",    EFI_GUID)
    ]

HW_CONTROLLER_DP          = 0x05

class CONTROLLER_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_DEVICE_PATH_PROTOCOL),
    ("ControllerNumber",  UINT32)
    ]

HW_BMC_DP                 = 0x06

class BMC_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_DEVICE_PATH_PROTOCOL),
    ("InterfaceType", UINT8),
    ("BaseAddress",   UINT8 * 8),
    ]

ACPI_DEVICE_PATH          = 0x02

ACPI_DP                   = 0x01

class ACPI_HID_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("HID",     UINT32),
    ("UID",     UINT32)
    ]

ACPI_EXTENDED_DP          = 0x02

class ACPI_EXTENDED_HID_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("HID",     UINT32),
    ("UID",     UINT32),
    ("CID",     UINT32)
    ]

PNP_EISA_ID_CONST         = 0x41d0

def EISA_ID(_Name, _Num):
  return ((_Name) | (_Num) << 16)

def EISA_PNP_ID(_PNPId):
  return EISA_ID(PNP_EISA_ID_CONST, (_PNPId))

def EFI_PNP_ID(_PNPId):
  return EISA_ID(PNP_EISA_ID_CONST, (_PNPId))

PNP_EISA_ID_MASK          = 0xffff

def EISA_ID_TO_NUM(_Id):
  return _Id >> 16

ACPI_ADR_DP               = 0x03

class ACPI_ADR_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("ADR",     UINT32)
    ]

ACPI_ADR_DISPLAY_TYPE_OTHER             = 0
ACPI_ADR_DISPLAY_TYPE_VGA               = 1
ACPI_ADR_DISPLAY_TYPE_TV                = 2
ACPI_ADR_DISPLAY_TYPE_EXTERNAL_DIGITAL  = 3
ACPI_ADR_DISPLAY_TYPE_INTERNAL_DIGITAL  = 4

def ACPI_DISPLAY_ADR(_DeviceIdScheme, _HeadId, _NonVgaOutput, _BiosCanDetect, _VendorInfo, _Type, _Port, _Index):

  return (((_DeviceIdScheme) & 0x1) << 31) |  \
         (((_HeadId)         & 0x7) << 18) |  \
         (((_NonVgaOutput)   & 0x1) << 17) |  \
         (((_BiosCanDetect)  & 0x1) << 16) |  \
         (((_VendorInfo)     & 0xf) << 12) |  \
         (((_Type)           & 0xf) << 8)  |  \
         (((_Port)           & 0xf) << 4)  |  \
          ((_Index)          & 0xf)

MESSAGING_DEVICE_PATH     = 0x03

MSG_ATAPI_DP              = 0x01

class ATAPI_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_DEVICE_PATH_PROTOCOL),
    ("PrimarySecondary",  UINT8),
    ("SlaveMaster",       UINT8),
    ("Lun",               UINT16)
    ]

MSG_SCSI_DP               = 0x02

class SCSI_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Pun",     UINT16),
    ("Lun",     UINT16)
    ]

MSG_FIBRECHANNEL_DP       = 0x03

class FIBRECHANNEL_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_DEVICE_PATH_PROTOCOL),
    ("Reserved",  UINT32),
    ("WWN",       UINT64),
    ("Lun",       UINT64)
    ]

MSG_FIBRECHANNELEX_DP     = 0x15

class FIBRECHANNELEX_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_DEVICE_PATH_PROTOCOL),
    ("Reserved",  UINT32),
    ("WWN",       UINT8 * 8),
    ("Lun",       UINT8 * 8)
    ]

MSG_1394_DP               = 0x04

class F1394_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_DEVICE_PATH_PROTOCOL),
    ("Reserved",  UINT32),
    ("Guid",      UINT64)
    ]

MSG_USB_DP                = 0x05

class USB_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_DEVICE_PATH_PROTOCOL),
    ("ParentPortNumber",  UINT8),
    ("InterfaceNumber",   UINT8)
    ]

MSG_USB_CLASS_DP          = 0x0f

class USB_CLASS_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("VendorId",        UINT16),
    ("ProductId",       UINT16),
    ("DeviceClass",     UINT8),
    ("DeviceSubClass",  UINT8),
    ("DeviceProtocol",  UINT8)
    ]

MSG_USB_WWID_DP           = 0x10

class USB_WWID_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("InterfaceNumber", UINT16),
    ("VendorId",        UINT16),
    ("ProductId",       UINT16)
    ]

MSG_DEVICE_LOGICAL_UNIT_DP  = 0x11

class DEVICE_LOGICAL_UNIT_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Lun",     UINT8)
    ]

MSG_SATA_DP               = 0x12

class SATA_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",                    EFI_DEVICE_PATH_PROTOCOL),
    ("HBAPortNumber",             UINT16),
    ("PortMultiplierPortNumber",  UINT16),
    ("Lun",                       UINT16)
    ]

SATA_HBA_DIRECT_CONNECT_FLAG = 0x8000

MSG_I2O_DP                = 0x06

class I2O_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Tid",     UINT32)
    ]

MSG_MAC_ADDR_DP           = 0x0b

class MAC_ADDR_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",      EFI_DEVICE_PATH_PROTOCOL),
    ("MacAddress",  EFI_MAC_ADDRESS),
    ("IfType",      UINT8)
    ]

MSG_IPv4_DP               = 0x0c

def CatIPv6Address (Address):

  return u"%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x" % (
    Address.Addr[ 0],   Address.Addr[ 1],
    Address.Addr[ 2],   Address.Addr[ 3],
    Address.Addr[ 4],   Address.Addr[ 5],
    Address.Addr[ 6],   Address.Addr[ 7],
    Address.Addr[ 8],   Address.Addr[ 9],
    Address.Addr[10],   Address.Addr[11],
    Address.Addr[12],   Address.Addr[13],
    Address.Addr[14],   Address.Addr[15]
    )

def CatIPv4Address (Address):

  return u"%d.%d.%d.%d" % (Address.Addr[0], Address.Addr[1], Address.Addr[2], Address.Addr[3])

def CatNetworkProtocol (Protocol):

  from EfiPy.MdePkg.Library.UefiDevicePathLib import RFC_1700_TCP_PROTOCOL, RFC_1700_UDP_PROTOCOL

  if    Protocol == RFC_1700_TCP_PROTOCOL:
    return u"TCP"

  elif  Protocol == RFC_1700_UDP_PROTOCOL:
    return u"UDP"

  else:
    return u"0x%x" % Protocol

class IPv4_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_DEVICE_PATH_PROTOCOL),
    ("LocalIpAddress",    EFI_IPv4_ADDRESS),
    ("RemoteIpAddress",   EFI_IPv4_ADDRESS),
    ("LocalPort",         UINT16),
    ("RemotePort",        UINT16),
    ("Protocol",          UINT16),
    ("StaticIpAddress",   BOOLEAN),
    ("GatewayIpAddress",  EFI_IPv4_ADDRESS),
    ("SubnetMask",        EFI_IPv4_ADDRESS)
    ]

MSG_IPv6_DP               = 0x0d

class IPv6_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_DEVICE_PATH_PROTOCOL),
    ("LocalIpAddress",    EFI_IPv6_ADDRESS),
    ("RemoteIpAddress",   EFI_IPv6_ADDRESS),
    ("LocalPort",         UINT16),
    ("RemotePort",        UINT16),
    ("Protocol",          UINT16),
    ("IpAddressOrigin",   UINT8),
    ("PrefixLength",      UINT8),
    ("GatewayIpAddress",  EFI_IPv6_ADDRESS)
    ]

MSG_INFINIBAND_DP         = 0x09

class INFINIBAND_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_DEVICE_PATH_PROTOCOL),
    ("ResourceFlags", UINT32),
    ("PortGid",       UINT8 * 16),
    ("ServiceId",     UINT64),
    ("TargetPortId",  UINT64),
    ("DeviceId",      UINT64)
    ]

INFINIBAND_RESOURCE_FLAG_IOC_SERVICE                = 0x01
INFINIBAND_RESOURCE_FLAG_EXTENDED_BOOT_ENVIRONMENT  = 0x02
INFINIBAND_RESOURCE_FLAG_CONSOLE_PROTOCOL           = 0x04
INFINIBAND_RESOURCE_FLAG_STORAGE_PROTOCOL           = 0x08
INFINIBAND_RESOURCE_FLAG_NETWORK_PROTOCOL           = 0x10

MSG_UART_DP               = 0x0e

class UART_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_DEVICE_PATH_PROTOCOL),
    ("Reserved",      UINT32),
    ("BaudRate",      UINT64),
    ("DataBits",      UINT8),
    ("Parity",        UINT8),
    ("StopBits",      UINT8)
    ]

MSG_VENDOR_DP             = 0x0a
VENDOR_DEFINED_DEVICE_PATH        = VENDOR_DEVICE_PATH

DEVICE_PATH_MESSAGING_PC_ANSI     = EFI_PC_ANSI_GUID
DEVICE_PATH_MESSAGING_VT_100      = EFI_VT_100_GUID
DEVICE_PATH_MESSAGING_VT_100_PLUS = EFI_VT_100_PLUS_GUID
DEVICE_PATH_MESSAGING_VT_UTF8     = EFI_VT_UTF8_GUID

class UART_FLOW_CONTROL_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("Guid",            EFI_GUID),
    ("FlowControlMap",  UINT32)
    ]

UART_FLOW_CONTROL_HARDWARE         = 0x00000001
UART_FLOW_CONTROL_XON_XOFF         = 0x00000010

DEVICE_PATH_MESSAGING_SAS          = EFI_SAS_DEVICE_PATH_GUID

class SAS_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_DEVICE_PATH_PROTOCOL),
    ("Guid",                EFI_GUID),
    ("Reserved",            UINT32),
    ("SasAddress",          UINT64),
    ("Lun",                 UINT64),
    ("DeviceTopology",      UINT16),
    ("RelativeTargetPort",  UINT16)
    ]

MSG_SASEX_DP              = 0x16

class SASEX_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_DEVICE_PATH_PROTOCOL),
    ("SasAddress",          UINT8 * 8),
    ("Lun",                 UINT8 * 8),
    ("DeviceTopology",      UINT16),
    ("RelativeTargetPort",  UINT16)
    ]

MSG_NVME_NAMESPACE_DP     = 0x17

class NVME_NAMESPACE_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_DEVICE_PATH_PROTOCOL),
    ("NamespaceId",   UINT32),
    ("NamespaceUuid", UINT64)
    ]

MSG_NVME_OF_NAMESPACE_DP  = 0x22
class NVME_OF_NAMESPACE_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("NamespaceIdType", UINT8),
    ("NamespaceId",     UINT8 * 16),
    # ("SubsystemNqn",    CHAR8 * N)
    ]

MSG_URI_DP                = 0x18

class URI_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Uri",     CHAR8)
    ]

MSG_UFS_DP                = 0x19

class UFS_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Pun",     UINT8),
    ("Lun",     UINT8),
    ]

MSG_SD_DP                 = 0x1A

class SD_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",      EFI_DEVICE_PATH_PROTOCOL),
    ("SlotNumber",  UINT8)
    ]

MSG_ISCSI_DP              = 0x13

class ISCSI_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",                EFI_DEVICE_PATH_PROTOCOL),
    ("NetworkProtocol",       UINT16),
    ("LoginOption",           UINT16),
    ("Lun",                   UINT64),
    ("TargetPortalGroupTag",  UINT16)
    ]

ISCSI_LOGIN_OPTION_NO_HEADER_DIGEST             = 0x0000
ISCSI_LOGIN_OPTION_HEADER_DIGEST_USING_CRC32C   = 0x0002
ISCSI_LOGIN_OPTION_NO_DATA_DIGEST               = 0x0000
ISCSI_LOGIN_OPTION_DATA_DIGEST_USING_CRC32C     = 0x0008
ISCSI_LOGIN_OPTION_AUTHMETHOD_CHAP              = 0x0000
ISCSI_LOGIN_OPTION_AUTHMETHOD_NON               = 0x1000
ISCSI_LOGIN_OPTION_CHAP_BI                      = 0x0000
ISCSI_LOGIN_OPTION_CHAP_UNI                     = 0x2000

MSG_VLAN_DP               = 0x14

class VLAN_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("VlanId",  UINT16)
    ]

MSG_BLUETOOTH_DP     = 0x1b

class BLUETOOTH_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("BD_ADDR", BLUETOOTH_ADDRESS)
    ]

MSG_WIFI_DP               = 0x1C

class WIFI_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("SSId",    UINT8 * 32)
    ]

MEDIA_DEVICE_PATH         = 0x04

MEDIA_HARDDRIVE_DP        = 0x01

class HARDDRIVE_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("PartitionNumber", UINT32),
    ("PartitionStart",  UINT64),
    ("PartitionSize",   UINT64),
    ("Signature",       UINT8 * 16),
    ("MBRType",         UINT8),
    ("SignatureType",   UINT8)
    ]

MBR_TYPE_PCAT             = 0x01
MBR_TYPE_EFI_PARTITION_TABLE_HEADER = 0x02

NO_DISK_SIGNATURE         = 0x00
SIGNATURE_TYPE_MBR        = 0x01
SIGNATURE_TYPE_GUID       = 0x02

MEDIA_CDROM_DP            = 0x02

class CDROM_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_DEVICE_PATH_PROTOCOL),
    ("BootEntry",     UINT32),
    ("PartitionStart",UINT64),
    ("PartitionSize", UINT64)
    ]

MEDIA_VENDOR_DP           = 0x03

MEDIA_FILEPATH_DP         = 0x04

class FILEPATH_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_DEVICE_PATH_PROTOCOL),
    ("PathName",  CHAR16 * 1)
    ]

MEDIA_PROTOCOL_DP         = 0x05

class MEDIA_PROTOCOL_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_DEVICE_PATH_PROTOCOL),
    ("Protocol",  EFI_GUID)
    ]

MEDIA_PIWG_FW_FILE_DP     = 0x06

class MEDIA_FW_VOL_FILEPATH_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",      EFI_DEVICE_PATH_PROTOCOL),
    ("FvFileName",  EFI_GUID)
    ]

MEDIA_PIWG_FW_VOL_DP         = 0x07

class MEDIA_FW_VOL_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("FvName",  EFI_GUID)
    ]

MEDIA_RELATIVE_OFFSET_RANGE_DP = 0x08

class MEDIA_RELATIVE_OFFSET_RANGE_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_DEVICE_PATH_PROTOCOL),
    ("Reserved",        UINT32),
    ("StartingOffset",  UINT64),
    ("EndingOffset",    UINT64)
    ]

EFI_VIRTUAL_DISK_GUID               = EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_DISK_REGION_VOLATILE

gEfiVirtualDiskGuid           = EFI_VIRTUAL_DISK_GUID
EFI_VIRTUAL_CD_GUID                 = EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_CD_REGION_VOLATILE

gEfiVirtualCdGuid             = EFI_VIRTUAL_CD_GUID
EFI_PERSISTENT_VIRTUAL_DISK_GUID    = EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_DISK_REGION_PERSISTENT

gEfiPersistentVirtualDiskGuid = EFI_PERSISTENT_VIRTUAL_DISK_GUID
EFI_PERSISTENT_VIRTUAL_CD_GUID      = EFI_ACPI_6_0_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_CD_REGION_PERSISTENT
gEfiPersistentVirtualCdGuid   = EFI_PERSISTENT_VIRTUAL_CD_GUID

MEDIA_RAM_DISK_DP         = 0x09

class MEDIA_RAM_DISK_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_DEVICE_PATH_PROTOCOL),
    ("StartingAddr",  UINT32 * 2),
    ("EndingAddr",    UINT32 * 2),
    ("TypeGuid",      EFI_GUID),
    ("Instance",      UINT16)
    ]

BBS_DEVICE_PATH           = 0x05

BBS_BBS_DP                = 0x01

class BBS_BBS_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
  _fields_ = [
    ("Header",      EFI_DEVICE_PATH_PROTOCOL),
    ("DeviceType",  UINT16),
    ("StatusFlag",  UINT16),
    ("String",      CHAR8 * 1)
    ]

BBS_TYPE_FLOPPY           = 0x01
BBS_TYPE_HARDDRIVE        = 0x02
BBS_TYPE_CDROM            = 0x03
BBS_TYPE_PCMCIA           = 0x04
BBS_TYPE_USB              = 0x05
BBS_TYPE_EMBEDDED_NETWORK = 0x06
BBS_TYPE_BEV              = 0x80
BBS_TYPE_UNKNOWN          = 0xFF

class EFI_DEV_PATH (EFIPY_DEVICE_PATH_UNION):
  _fields_ = [
    ("DevPath",         EFI_DEVICE_PATH_PROTOCOL),
    ("Pci",             PCI_DEVICE_PATH),
    ("PcCard",          PCCARD_DEVICE_PATH),
    ("MemMap",          MEMMAP_DEVICE_PATH),
    ("Vendor",          VENDOR_DEVICE_PATH),
    ("Controller",      CONTROLLER_DEVICE_PATH),
    ("Bmc",             BMC_DEVICE_PATH),
    ("Acpi",            ACPI_HID_DEVICE_PATH),
    ("ExtendedAcpi",    ACPI_EXTENDED_HID_DEVICE_PATH),
    ("AcpiAdr",         ACPI_ADR_DEVICE_PATH),
    ("Atapi",           ATAPI_DEVICE_PATH),
    ("Scsi",            SCSI_DEVICE_PATH),
    ("Iscsi",           ISCSI_DEVICE_PATH),
    ("FibreChannel",    FIBRECHANNEL_DEVICE_PATH),
    ("FibreChannelEx",  FIBRECHANNELEX_DEVICE_PATH),
    ("F1394",           F1394_DEVICE_PATH),
    ("Usb",             USB_DEVICE_PATH),
    ("Sata",            SATA_DEVICE_PATH),
    ("UsbClass",        USB_CLASS_DEVICE_PATH),
    ("UsbWwid",         USB_WWID_DEVICE_PATH),
    ("LogicUnit",       DEVICE_LOGICAL_UNIT_DEVICE_PATH),
    ("I2O",             I2O_DEVICE_PATH),
    ("MacAddr",         MAC_ADDR_DEVICE_PATH),
    ("Ipv4",            IPv4_DEVICE_PATH),
    ("Ipv6",            IPv6_DEVICE_PATH),
    ("Vlan",            VLAN_DEVICE_PATH),
    ("InfiniBand",      INFINIBAND_DEVICE_PATH),
    ("Uart",            UART_DEVICE_PATH),
    ("UartFlowControl", UART_FLOW_CONTROL_DEVICE_PATH),
    ("Sas",             SAS_DEVICE_PATH),
    ("SasEx",           SASEX_DEVICE_PATH),
    ("NvmeNamespace",   NVME_NAMESPACE_DEVICE_PATH),
    ("Uri",             URI_DEVICE_PATH),
    ("Bluetooth",       BLUETOOTH_DEVICE_PATH),
    ("WiFi",            WIFI_DEVICE_PATH),
    ("Ufs",             UFS_DEVICE_PATH),
    ("Sd",              SD_DEVICE_PATH),
    ("HardDrive",       HARDDRIVE_DEVICE_PATH),
    ("CD",              CDROM_DEVICE_PATH),
    ("FilePath",        FILEPATH_DEVICE_PATH),
    ("MediaProtocol",   MEDIA_PROTOCOL_DEVICE_PATH),
    ("FirmwareVolume",  MEDIA_FW_VOL_DEVICE_PATH),
    ("FirmwareFile",    MEDIA_FW_VOL_FILEPATH_DEVICE_PATH),
    ("Offset",          MEDIA_RELATIVE_OFFSET_RANGE_DEVICE_PATH),
    ("RamDisk",         MEDIA_RAM_DISK_DEVICE_PATH),
    ("Bbs",             BBS_BBS_DEVICE_PATH)
    ]

class EFI_DEV_PATH_PTR (EFIPY_DEVICE_PATH_UNION):
  _fields_ = [
    ("DevPath",         POINTER (EFI_DEVICE_PATH_PROTOCOL)),
    ("Pci",             POINTER (PCI_DEVICE_PATH)),
    ("PcCard",          POINTER (PCCARD_DEVICE_PATH)),
    ("MemMap",          POINTER (MEMMAP_DEVICE_PATH)),
    ("Vendor",          POINTER (VENDOR_DEVICE_PATH)),
    ("Controller",      POINTER (CONTROLLER_DEVICE_PATH)),
    ("Bmc",             POINTER (BMC_DEVICE_PATH)),
    ("Acpi",            POINTER (ACPI_HID_DEVICE_PATH)),
    ("ExtendedAcpi",    POINTER (ACPI_EXTENDED_HID_DEVICE_PATH)),
    ("AcpiAdr",         POINTER (ACPI_ADR_DEVICE_PATH)),
    ("Atapi",           POINTER (ATAPI_DEVICE_PATH)),
    ("Scsi",            POINTER (SCSI_DEVICE_PATH)),
    ("Iscsi",           POINTER (ISCSI_DEVICE_PATH)),
    ("FibreChannel",    POINTER (FIBRECHANNEL_DEVICE_PATH)),
    ("FibreChannelEx",  POINTER (FIBRECHANNELEX_DEVICE_PATH)),
    ("F1394",           POINTER (F1394_DEVICE_PATH)),
    ("Usb",             POINTER (USB_DEVICE_PATH)),
    ("Sata",            POINTER (SATA_DEVICE_PATH)),
    ("UsbClass",        POINTER (USB_CLASS_DEVICE_PATH)),
    ("UsbWwid",         POINTER (USB_WWID_DEVICE_PATH)),
    ("LogicUnit",       POINTER (DEVICE_LOGICAL_UNIT_DEVICE_PATH)),
    ("I2O",             POINTER (I2O_DEVICE_PATH)),
    ("MacAddr",         POINTER (MAC_ADDR_DEVICE_PATH)),
    ("Ipv4",            POINTER (IPv4_DEVICE_PATH)),
    ("Ipv6",            POINTER (IPv6_DEVICE_PATH)),
    ("Vlan",            POINTER (VLAN_DEVICE_PATH)),
    ("InfiniBand",      POINTER (INFINIBAND_DEVICE_PATH)),
    ("Uart",            POINTER (UART_DEVICE_PATH)),
    ("UartFlowControl", POINTER (UART_FLOW_CONTROL_DEVICE_PATH)),
    ("Sas",             POINTER (SAS_DEVICE_PATH)),
    ("SasEx",           POINTER (SASEX_DEVICE_PATH)),
    ("NvmeNamespace",   POINTER (NVME_NAMESPACE_DEVICE_PATH)),
    ("Uri",             POINTER (URI_DEVICE_PATH)),
    ("Bluetooth",       POINTER (BLUETOOTH_DEVICE_PATH)),
    ("WiFi",            POINTER (WIFI_DEVICE_PATH)),
    ("Ufs",             POINTER (UFS_DEVICE_PATH)),
    ("Sd",              POINTER (SD_DEVICE_PATH)),
    ("HardDrive",       POINTER (HARDDRIVE_DEVICE_PATH)),
    ("CD",              POINTER (CDROM_DEVICE_PATH)),
    ("FilePath",        POINTER (FILEPATH_DEVICE_PATH)),
    ("MediaProtocol",   POINTER (MEDIA_PROTOCOL_DEVICE_PATH)),
    ("FirmwareVolume",  POINTER (MEDIA_FW_VOL_DEVICE_PATH)),
    ("FirmwareFile",    POINTER (MEDIA_FW_VOL_FILEPATH_DEVICE_PATH)),
    ("Offset",          POINTER (MEDIA_RELATIVE_OFFSET_RANGE_DEVICE_PATH)),
    ("RamDisk",         POINTER (MEDIA_RAM_DISK_DEVICE_PATH)),
    ("Bbs",             POINTER (BBS_BBS_DEVICE_PATH)),
    ("Raw",             POINTER (UINT8))
    ]

END_DEVICE_PATH_TYPE                 = 0x7f
END_ENTIRE_DEVICE_PATH_SUBTYPE       = 0xFF
END_INSTANCE_DEVICE_PATH_SUBTYPE     = 0x01


# class END_DEVICE_PATH (EFIPY_DEVICE_PATH_STRUCTURE):
#   _fields_ = [
#     ("Header",      EFI_DEVICE_PATH_PROTOCOL),
#     ("DeviceType",  UINT16),
#     ("StatusFlag",  UINT16),
#     ("String",      CHAR8 * 1)
#     ]
# 

DevNodeTable = {
  (HARDWARE_DEVICE_PATH  << 8) |    HW_PCI_DP                         : PCI_DEVICE_PATH,
  (HARDWARE_DEVICE_PATH  << 8) |    HW_PCCARD_DP                      : PCCARD_DEVICE_PATH,
  (HARDWARE_DEVICE_PATH  << 8) |    HW_MEMMAP_DP                      : MEMMAP_DEVICE_PATH,
  (HARDWARE_DEVICE_PATH  << 8) |    HW_VENDOR_DP                      : VENDOR_DEVICE_PATH,
  (HARDWARE_DEVICE_PATH  << 8) |    HW_CONTROLLER_DP                  : CONTROLLER_DEVICE_PATH,
  (ACPI_DEVICE_PATH      << 8) |    ACPI_DP                           : ACPI_HID_DEVICE_PATH,
  (ACPI_DEVICE_PATH      << 8) |    ACPI_EXTENDED_DP                  : ACPI_EXTENDED_HID_DEVICE_PATH,
  (ACPI_DEVICE_PATH      << 8) |    ACPI_ADR_DP                       : ACPI_ADR_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_ATAPI_DP                      : ATAPI_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_SCSI_DP                       : SCSI_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_FIBRECHANNEL_DP               : SCSI_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_FIBRECHANNELEX_DP             : FIBRECHANNELEX_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_SASEX_DP                      : SASEX_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_1394_DP                       : F1394_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_USB_DP                        : USB_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_USB_WWID_DP                   : USB_WWID_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_DEVICE_LOGICAL_UNIT_DP        : DEVICE_LOGICAL_UNIT_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_USB_CLASS_DP                  : USB_CLASS_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_SATA_DP                       : SATA_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_I2O_DP                        : I2O_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_MAC_ADDR_DP                   : MAC_ADDR_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_IPv4_DP                       : IPv4_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_IPv6_DP                       : IPv6_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_INFINIBAND_DP                 : INFINIBAND_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_UART_DP                       : UART_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_VENDOR_DP                     : VENDOR_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_ISCSI_DP                      : ISCSI_DEVICE_PATH,
  (MESSAGING_DEVICE_PATH << 8) |    MSG_VLAN_DP                       : VLAN_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_HARDDRIVE_DP                : HARDDRIVE_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_CDROM_DP                    : CDROM_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_VENDOR_DP                   : VENDOR_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_PROTOCOL_DP                 : MEDIA_PROTOCOL_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_FILEPATH_DP                 : FILEPATH_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_PIWG_FW_VOL_DP              : MEDIA_FW_VOL_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_PIWG_FW_FILE_DP             : MEDIA_FW_VOL_FILEPATH_DEVICE_PATH,
  (MEDIA_DEVICE_PATH     << 8) |    MEDIA_RELATIVE_OFFSET_RANGE_DP    : MEDIA_RELATIVE_OFFSET_RANGE_DEVICE_PATH,
  (BBS_DEVICE_PATH       << 8) |    BBS_BBS_DP                        : BBS_BBS_DEVICE_PATH,
  # (END_DEVICE_PATH_TYPE  << 8) |    END_ENTIRE_DEVICE_PATH_SUBTYPE    : END_DEVICE_PATH,
}

def _IsDevicePathEndType (self):
  if self.Type == END_DEVICE_PATH_TYPE:
    return True
  else:
    return False

def _IsDevicePathEnd (self):
  if self.IsDevicePathEndType () and (self.SubType == END_ENTIRE_DEVICE_PATH_SUBTYPE):
    return True
  else:
    return False

def _IsDevicePathEndInstance (self):
  if self.IsDevicePathEndType () and (self.SubType == END_INSTANCE_DEVICE_PATH_SUBTYPE):
    return True
  else:
    return False

EFI_DEVICE_PATH_PROTOCOL.IsDevicePathEndType      = _IsDevicePathEndType
EFI_DEVICE_PATH_PROTOCOL.IsDevicePathEnd          = _IsDevicePathEnd
EFI_DEVICE_PATH_PROTOCOL.IsDevicePathEndInstance  = _IsDevicePathEndInstance
