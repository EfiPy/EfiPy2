# LowPowerIdleTable.py
#
# EfiPy2.MdePkg.IndustryStandard.LowPowerIdleTable
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

ACPI_LPI_STRUCTURE_TYPE_NATIVE_CSTATE  = 0x00

class ACPI_LPI_STATE_FLAGS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Disabled",            UINT32, 1),
    ("CounterUnavailable",  UINT32, 1),
    ("Reserved",            UINT32, 30)
    ]

class ACPI_LPI_STATE_FLAGS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    ACPI_LPI_STATE_FLAGS_Bits),
    ("Data32",  UINT32)
    ]

class ACPI_LPI_NATIVE_CSTATE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                        UINT32                                     ),
    ("Length",                      UINT32                                     ),
    ("UniqueId",                    UINT16                                     ),
    ("Reserved",                    UINT8 * 2                                  ),
    ("Flags",                       ACPI_LPI_STATE_FLAGS                       ),
    ("EntryTrigger",                Acpi.EFI_ACPI_6_1_GENERIC_ADDRESS_STRUCTURE),
    ("Residency",                   UINT32                                     ),
    ("Latency",                     UINT32                                     ),
    ("ResidencyCounter",            Acpi.EFI_ACPI_6_1_GENERIC_ADDRESS_STRUCTURE),
    ("ResidencyCounterFrequency",   UINT64                                     )
  ]

