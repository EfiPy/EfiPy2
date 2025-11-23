# DebugPortTable.py
#
# EfiPy2.MdePkg.IndustryStandard.DebugPortTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

class EFI_ACPI_DEBUG_PORT_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("InterfaceType",     UINT8),
    ("Reserved_37",       UINT8 * 3),
    ("BaseAddress",       Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE)
  ]

EFI_ACPI_DEBUG_PORT_TABLE_REVISION      = 0x01

EFI_ACPI_DBGP_INTERFACE_TYPE_FULL_16550                                 = 0
EFI_ACPI_DBGP_INTERFACE_TYPE_16550_SUBSET_COMPATIBLE_WITH_MS_DBGP_SPEC  = 1

