# Mpam.py
#
# EfiPy2.MdePkg.IndustryStandard.Mpam
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
# 
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

EFI_ACPI_MEMORY_SYSTEM_RESOURCE_PARTITIONING_AND_MONITORING_TABLE_REVISION  = (0x01)

EFI_ACPI_MPAM_INTERRUPT_LEVEL_TRIGGERED  = (0x0)
EFI_ACPI_MPAM_INTERRUPT_EDGE_TRIGGERED   = (0x1)

EFI_ACPI_MPAM_INTERRUPT_WIRED  = (0x0)

EFI_ACPI_MPAM_INTERRUPT_PROCESSOR_AFFINITY            = (0x0)
EFI_ACPI_MPAM_INTERRUPT_PROCESSOR_CONTAINER_AFFINITY  = (0x1)

EFI_ACPI_MPAM_INTERRUPT_AFFINITY_NOT_VALID  = (0x0)
EFI_ACPI_MPAM_INTERRUPT_AFFINITY_VALID      = (0x1)

EFI_ACPI_MPAM_INTERRUPT_MODE_SHIFT            = (0)
EFI_ACPI_MPAM_INTERRUPT_TYPE_SHIFT            = (1)
EFI_ACPI_MPAM_INTERRUPT_AFFINITY_TYPE_SHIFT   = (3)
EFI_ACPI_MPAM_INTERRUPT_AFFINITY_VALID_SHIFT  = (4)
EFI_ACPI_MPAM_INTERRUPT_RESERVED_SHIFT        = (5)

EFI_ACPI_MPAM_INTERRUPT_MODE_MASK            = (0x1)
EFI_ACPI_MPAM_INTERRUPT_TYPE_MASK            = (0x3)
EFI_ACPI_MPAM_INTERRUPT_AFFINITY_TYPE_MASK   = (0x8)
EFI_ACPI_MPAM_INTERRUPT_AFFINITY_VALID_MASK  = (0x10)
EFI_ACPI_MPAM_INTERRUPT_RESERVED_MASK        = (0xFFFFFFE0)

EFI_ACPI_MPAM_LOCATION_PROCESSOR_CACHE  = (0x0)
EFI_ACPI_MPAM_LOCATION_MEMORY           = (0x1)
EFI_ACPI_MPAM_LOCATION_SMMU             = (0x2)
EFI_ACPI_MPAM_LOCATION_MEMORY_CACHE     = (0x3)
EFI_ACPI_MPAM_LOCATION_ACPI_DEVICE      = (0x4)
EFI_ACPI_MPAM_LOCATION_INTERCONNECT     = (0x5)
EFI_ACPI_MPAM_LOCATION_UNKNOWN          = (0xFF)

EFI_ACPI_MPAM_INTERFACE_MMIO  = (0x00)
EFI_ACPI_MPAM_INTERFACE_PCC   = (0x0A)

EFI_ACPI_MPAM_LINK_TYPE_NUMA  = (0x00)
EFI_ACPI_MPAM_LINK_TYPE_PROC  = (0x01)

class EFI_ACPI_MPAM_GENERIC_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Descriptor1",  UINT64),
    ("Descriptor2",  UINT32)
  ]

class EFI_ACPI_MPAM_CACHE_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReference",  UINT64),
    ("Reserved",        UINT32)
  ]

class EFI_ACPI_MPAM_MEMORY_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ProximityDomain", UINT64),
    ("Reserved",        UINT32)
  ]

class EFI_ACPI_MPAM_SMMU_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SmmuInterface",   UINT64),
    ("Reserved",        UINT32)
  ]

class EFI_ACPI_MPAM_MEMORY_CACHE_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",  UINT8 * 7),
    ("Level",     UINT8),
    ("Reserved",  UINT32)
  ]

class EFI_ACPI_MPAM_ACPI_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AcpiHardwareId",  UINT64),
    ("AcpiUniqueId",    UINT32)
  ]

class EFI_ACPI_MPAM_INTERCONNECT_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InterconnectDescTblOff",  UINT64),
    ("Reserved",                UINT32)
  ]

class EFI_ACPI_MPAM_INTERCONNECT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SourceId",      UINT32),
    ("DestinationId", UINT32),
    ("LinkType",      UINT8),
    ("Reserved",      UINT8 * 3)
  ]

class EFI_ACPI_MPAM_INTERCONNECT_DESCRIPTOR_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT8 * 16),
    ("NumDescriptors",  UINT32)
  ]

class EFI_ACPI_MPAM_LOCATOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("CacheLocator",            EFI_ACPI_MPAM_CACHE_LOCATOR),
    ("MemoryLocator",           EFI_ACPI_MPAM_MEMORY_LOCATOR),
    ("SmmuLocator",             EFI_ACPI_MPAM_SMMU_LOCATOR),
    ("MemCacheLocator",         EFI_ACPI_MPAM_MEMORY_CACHE_LOCATOR),
    ("AcpiLocator",             EFI_ACPI_MPAM_ACPI_LOCATOR),
    ("InterconnectIfcLocator",  EFI_ACPI_MPAM_INTERCONNECT_LOCATOR),
    ("GenericLocator",          EFI_ACPI_MPAM_GENERIC_LOCATOR)
  ]

class EFI_ACPI_MPAM_MSC_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",                    UINT16),
    ("InterfaceType",             UINT8),
    ("Reserved",                  UINT8),
    ("Identifier",                UINT32),
    ("BaseAddress",               UINT64),
    ("MmioSize",                  UINT32),
    ("OverflowInterrupt",         UINT32),
    ("OverflowInterruptFlags",    UINT32),
    ("Reserved1",                 UINT32),
    ("OverflowInterruptAffinity", UINT32),
    ("ErrorInterrupt",            UINT32),
    ("ErrorInterruptFlags",       UINT32),
    ("Reserved2",                 UINT32),
    ("ErrorInterruptAffinity",    UINT32),
    ("MaxNrdyUsec",               UINT32),
    ("HardwareIdLinkedDevice",    UINT64),
    ("InstanceIdLinkedDevice",    UINT32),
    ("NumResources",              UINT32)
  ]

class EFI_ACPI_MPAM_MSC_RESOURCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Identifier",                  UINT32),
    ("RisIndex",                    UINT8),
    ("Reserved1",                   UINT16),
    ("LocatorType",                 UINT8),
    ("Locator",                     EFI_ACPI_MPAM_LOCATOR),
    ("NumFunctionalDependencies",   UINT32)
  ]

class EFI_ACPI_MPAM_FUNCTIONAL_DEPENDENCY_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Producer",  UINT32),
    ("Reserved",  UINT32)
  ]

