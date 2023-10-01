# WindowsSmmSecurityMitigationTable.py
#
# EfiPy2.MdePkg.IndustryStandard.WindowsSmmSecurityMitigationTable
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard  import *
from EfiPy2.MdePkg.IndustryStandard  import Acpi

EFI_ACPI_WINDOWS_SMM_SECURITY_MITIGATION_TABLE_SIGNATURE  = SIGNATURE_32('W', 'S', 'M', 'T')

EFI_WSMT_TABLE_REVISION  = 1

class EFI_ACPI_WSMT_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("ProtectionFlags", UINT32)
  ]

EFI_WSMT_PROTECTION_FLAGS_FIXED_COMM_BUFFERS                 = 0x1
EFI_WSMT_PROTECTION_FLAGS_COMM_BUFFER_NESTED_PTR_PROTECTION  = 0x2
EFI_WSMT_PROTECTION_FLAGS_SYSTEM_RESOURCE_PROTECTION         = 0x4

