# WatchdogResourceTable.py
#
# EfiPy2.MdePkg.IndustryStandard.WatchdogResourceTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

class EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("ControlRegisterAddress",  Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("CountRegisterAddress",    Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("PCIDeviceID",             UINT16),
    ("PCIVendorID",             UINT16),
    ("PCIBusNumber",            UINT8),
    ("PCIDeviceNumber",         UINT8),
    ("PCIFunctionNumber",       UINT8),
    ("PCISegment",              UINT8),
    ("MaxCount",                UINT16),
    ("Units",                   UINT8)
  ]

EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE_REVISION  = 0x01

EFI_ACPI_WDRT_1_0_COUNT_UNIT_1_SEC_PER_COUNT        = 1
EFI_ACPI_WDRT_1_0_COUNT_UNIT_100_MILLISEC_PER_COUNT = 2
EFI_ACPI_WDRT_1_0_COUNT_UNIT_10_MILLISEC_PER_COUNT  = 3

