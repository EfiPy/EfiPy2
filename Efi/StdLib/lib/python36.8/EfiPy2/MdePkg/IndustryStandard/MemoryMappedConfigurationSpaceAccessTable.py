# MemoryMappedConfigurationSpaceAccessTable.py
#
# EfiPy2.MdePkg.IndustryStandard.MemoryMappedConfigurationSpaceAccessTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

class EFI_ACPI_MEMORY_MAPPED_ENHANCED_CONFIGURATION_SPACE_BASE_ADDRESS_ALLOCATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BaseAddress",           UINT64),
    ("PciSegmentGroupNumber", UINT16),
    ("StartBusNumber",        UINT8),
    ("EndBusNumber",          UINT8),
    ("Reserved",              UINT32)
  ]

class EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_BASE_ADDRESS_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",  UINT64)
  ]

EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_TABLE_REVISION  = 0x01

