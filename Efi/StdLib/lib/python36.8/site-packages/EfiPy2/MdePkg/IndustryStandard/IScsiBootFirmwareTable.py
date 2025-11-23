# IScsiBootFirmwareTable.py
#
# EfiPy2.MdePkg.IndustryStandard.IScsiBootFirmwareTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_REVISION            = 0x01
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_STRUCTURE_ALIGNMENT = 8

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_RESERVED_STRUCTURE_ID         = 0
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_CONTROL_STRUCTURE_ID          = 1
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_INITIATOR_STRUCTURE_ID        = 2
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_NIC_STRUCTURE_ID              = 3
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_ID           = 4
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_EXTERNSIONS_STRUCTURE_ID      = 5

IpPrefixOriginOther                 = 0
IpPrefixOriginManual                = 1
IpPrefixOriginWellKnown             = 2
IpPrefixOriginDhcp                  = 3
IpPrefixOriginRouterAdvertisement   = 4
IpPrefixOriginUnchanged             = 16
IP_PREFIX_VALUE = ENUM

class EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",   UINT32),
    ("Length",      UINT32),
    ("Revision",    UINT8),
    ("Checksum",    UINT8),
    ("OemId",       UINT8 * 6),
    ("OemTableId",  UINT64),
    ("Reserved",    UINT8 * 24)
  ]

class EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("StructureId", UINT8),
    ("Version",     UINT8),
    ("Length",      UINT16),
    ("Index",       UINT8),
    ("Flags",       UINT8)
  ]

class EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_CONTROL_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_STRUCTURE_HEADER),
    ("Extensions",      UINT16),
    ("InitiatorOffset", UINT16),
    ("NIC0Offset",      UINT16),
    ("Target0Offset",   UINT16),
    ("NIC1Offset",      UINT16),
    ("Target1Offset",   UINT16)
  ]

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_CONTROL_STRUCTURE_VERSION              = 0x1

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_CONTROL_STRUCTURE_FLAG_BOOT_FAILOVER   = BIT0

class EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_INITIATOR_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_STRUCTURE_HEADER),
    ("ISnsServer",            EFI_IPv6_ADDRESS),
    ("SlpServer",             EFI_IPv6_ADDRESS),
    ("PrimaryRadiusServer",   EFI_IPv6_ADDRESS),
    ("SecondaryRadiusServer", EFI_IPv6_ADDRESS),
    ("IScsiNameLength",       UINT16),
    ("IScsiNameOffset",       UINT16)
  ]

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_INITIATOR_STRUCTURE_VERSION             = 0x1

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_INITIATOR_STRUCTURE_FLAG_BLOCK_VALID    = BIT0 
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_INITIATOR_STRUCTURE_FLAG_BOOT_SELECTED  = BIT1 

class EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_NIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_STRUCTURE_HEADER),
    ("Ip",                      EFI_IPv6_ADDRESS),
    ("SubnetMaskPrefixLength",  UINT8),
    ("Origin",                  UINT8),
    ("Gateway",                 EFI_IPv6_ADDRESS),
    ("PrimaryDns",              EFI_IPv6_ADDRESS),
    ("SecondaryDns",            EFI_IPv6_ADDRESS),
    ("DhcpServer",              EFI_IPv6_ADDRESS),
    ("VLanTag",                 UINT16),
    ("Mac",                     UINT8 * 6),
    ("PciLocation",             UINT16),
    ("HostNameLength",          UINT16),
    ("HostNameOffset",          UINT16),
  ]

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_NIC_STRUCTURE_VERSION                 = 0x1

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_NIC_STRUCTURE_FLAG_BLOCK_VALID        = BIT0
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_NIC_STRUCTURE_FLAG_BOOT_SELECTED      = BIT1
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_NIC_STRUCTURE_FLAG_GLOBAL             = BIT2

class EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_STRUCTURE_HEADER),
    ("Ip",                      EFI_IPv6_ADDRESS),
    ("Port",                    UINT16),
    ("BootLun",                 UINT8 * 8),
    ("CHAPType",                UINT8),
    ("NicIndex",                UINT8),
    ("IScsiNameLength",         UINT16),
    ("IScsiNameOffset",         UINT16),
    ("CHAPNameLength",          UINT16),
    ("CHAPNameOffset",          UINT16),
    ("CHAPSecretLength",        UINT16),
    ("CHAPSecretOffset",        UINT16),
    ("ReverseCHAPNameLength",   UINT16),
    ("ReverseCHAPNameOffset",   UINT16),
    ("ReverseCHAPSecretLength", UINT16),
    ("ReverseCHAPSecretOffset", UINT16)
  ]

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_VERSION               = 0x1

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_FLAG_BLOCK_VALID      = BIT0
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_FLAG_BOOT_SELECTED    = BIT1
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_FLAG_RADIUS_CHAP      = BIT2
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_FLAG_RADIUS_RCHAP     = BIT3

EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_CHAP_TYPE_NO_CHAP        = 0
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_CHAP_TYPE_CHAP           = 1
EFI_ACPI_ISCSI_BOOT_FIRMWARE_TABLE_TARGET_STRUCTURE_CHAP_TYPE_MUTUAL_CHAP    = 2
