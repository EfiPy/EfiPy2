# HighPrecisionEventTimerTable.py
#
# EfiPy2.MdePkg.IndustryStandard.HighPrecisionEventTimerTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Revision",        UINT32, 8),
    ("NumberOfTimers",  UINT32, 5),
    ("CounterSize",     UINT32, 1),
    ("Reserved",        UINT32, 1),
    ("LegacyRoute",     UINT32, 1),
    ("VendorId",        UINT32, 16)
  ]

class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID_Bits),
    ("Uint32",          UINT32)
  ]

class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                    Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("EventTimerBlockId",                         UINT32),
    ("BaseAddressLower32Bit",                     Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("HpetNumber",                                UINT8),
    ("MainCounterMinimumClockTickInPeriodicMode", UINT16),
    ("PageProtectionAndOemAttribute",             UINT8)
  ]

EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_REVISION  = 0x01

EFI_ACPI_NO_PAGE_PROTECTION    = 0
EFI_ACPI_4KB_PAGE_PROTECTION   = 1
EFI_ACPI_64KB_PAGE_PROTECTION  = 2

