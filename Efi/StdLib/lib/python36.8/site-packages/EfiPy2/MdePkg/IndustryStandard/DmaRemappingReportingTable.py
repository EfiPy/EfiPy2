# DmaRemappingReportingTable.py
#
# EfiPy2.MdePkg.IndustryStandard.DmaRemappingReportingTable
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

EFI_ACPI_DMAR_REVISION  = 0x01

EFI_ACPI_DMAR_FLAGS_INTR_REMAP                     = BIT0
EFI_ACPI_DMAR_FLAGS_X2APIC_OPT_OUT                 = BIT1
EFI_ACPI_DMAR_FLAGS_DMA_CTRL_PLATFORM_OPT_IN_FLAG  = BIT2

EFI_ACPI_DMAR_TYPE_DRHD  = 0x00
EFI_ACPI_DMAR_TYPE_RMRR  = 0x01
EFI_ACPI_DMAR_TYPE_ATSR  = 0x02
EFI_ACPI_DMAR_TYPE_RHSA  = 0x03
EFI_ACPI_DMAR_TYPE_ANDD  = 0x04
EFI_ACPI_DMAR_TYPE_SATC  = 0x05
EFI_ACPI_DMAR_TYPE_SIDP  = 0x06

EFI_ACPI_DEVICE_SCOPE_ENTRY_TYPE_PCI_ENDPOINT           = 0x01
EFI_ACPI_DEVICE_SCOPE_ENTRY_TYPE_PCI_BRIDGE             = 0x02
EFI_ACPI_DEVICE_SCOPE_ENTRY_TYPE_IOAPIC                 = 0x03
EFI_ACPI_DEVICE_SCOPE_ENTRY_TYPE_MSI_CAPABLE_HPET       = 0x04
EFI_ACPI_DEVICE_SCOPE_ENTRY_TYPE_ACPI_NAMESPACE_DEVICE  = 0x05

EFI_ACPI_DEVICE_SCOPE_REQ_WO_PASID_NESTED_NOTALLOWED  = BIT0
EFI_ACPI_DEVICE_SCOPE_REQ_WO_PASID_PWSNP_NOTALLOWED   = BIT1
EFI_ACPI_DEVICE_SCOPE_REQ_WO_PASID_PGSNP_NOTALLOWED   = BIT2
EFI_ACPI_DEVICE_SCOPE_REQ_WO_PASID_ATC_HARDENED       = BIT3
EFI_ACPI_DEVICE_SCOPE_REQ_WO_PASID_ATC_REQUIRED       = BIT4

EFI_ACPI_DMAR_ATSR_FLAGS_ALL_PORTS  = BIT0

class EFI_ACPI_DMAR_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT16),
    ("Length",  UINT16)
  ]

class EFI_ACPI_DMAR_PCI_PATH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Device",      UINT8),
    ("Function",    UINT8)
  ]

class EFI_ACPI_DMAR_DEVICE_SCOPE_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Flags",           UINT8),
    ("Reserved",        UINT8),
    ("EnumerationId",   UINT8),
    ("StartBusNumber",  UINT8)
  ]

class EFI_ACPI_DMAR_DRHD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Flags",               UINT8),
    ("Size",                UINT8),
    ("SegmentNumber",       UINT16),
    ("RegisterBaseAddress", UINT64)
  ]

class EFI_ACPI_DMAR_RMRR_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Reserved",                        UINT8 * 2),
    ("SegmentNumber",                   UINT16),
    ("ReservedMemoryRegionBaseAddress", UINT64),
    ("ReservedMemoryRegionLimitAddress",UINT64)
  ]

class EFI_ACPI_DMAR_ATSR_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Flags",           UINT8),
    ("Reserved",        UINT8),
    ("SegmentNumber",   UINT16)
  ]

class EFI_ACPI_DMAR_RHSA_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Reserved",            UINT8 * 4),
    ("RegisterBaseAddress", UINT64),
    ("ProximityDomain",     UINT32)
  ]

class EFI_ACPI_DMAR_ANDD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Reserved",            UINT8 * 3),
    ("AcpiDeviceNumber",    UINT8)
  ]

class EFI_ACPI_DMAR_SATC_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Flags",           UINT8),
    ("Reserved",        UINT8),
    ("SegmentNumber",   UINT16)
  ]

class EFI_ACPI_DMAR_SIDP_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_ACPI_DMAR_STRUCTURE_HEADER),
    ("Reserved",        UINT16),
    ("SegmentNumber",   UINT16)
  ]

class EFI_ACPI_DMAR_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("HostAddressWidth",    UINT8),
    ("Flags",               UINT8),
    ("Reserved",            UINT8 * 10),
  ]

