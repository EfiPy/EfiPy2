# UefiAcpiDataTable.py
#
# EfiPy2.MdePkg.Uefi.UefiAcpiDataTable
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
import EfiPy2 as EfiPy

from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE

class EFI_ACPI_DATA_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Identifier",          EfiPy.GUID),
    ("DataOffset",          EfiPy.UINT16),
  ]

