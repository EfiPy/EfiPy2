# AcpiTableDb.py
#
# EfiPy2.Lib.AcpiTableDb
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.MdePkg.IndustryStandard.Acpi20      import EFI_ACPI_DESCRIPTION_HEADER
from EfiPy2.MdePkg.IndustryStandard.Tpm2Acpi    import EFI_TPM2_ACPI_TABLE
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE
from EfiPy2.MdePkg.IndustryStandard import MemoryMappedConfigurationSpaceAccessTable as McfgTable
from EfiPy2.MdePkg.IndustryStandard.HighPrecisionEventTimerTable import EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_HEADER
from EfiPy2.MdePkg.IndustryStandard.DmaRemappingReportingTable   import EFI_ACPI_DMAR_HEADER
from EfiPy2.MdePkg.IndustryStandard.AlertStandardFormatTable     import EFI_ACPI_ASF_DESCRIPTION_HEADER
from EfiPy2.MdePkg.IndustryStandard.WatchdogResourceTable        import EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE

#
# Due to this ACPI table (MCFG) is too import.
# That it hard to ignore, creat it for more friendly usage
#
class EFIPY_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    McfgTable.EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_BASE_ADDRESS_TABLE_HEADER),
    ("McfgDesc",  McfgTable.EFI_ACPI_MEMORY_MAPPED_ENHANCED_CONFIGURATION_SPACE_BASE_ADDRESS_ALLOCATION_STRUCTURE)
  ]

class EFI_TPM2_ACPI_TABLE_V4 (EfiPy.Structure):
    _pack_   = 1
    _fields_ = [
        ("Header",                      EFI_ACPI_DESCRIPTION_HEADER),
        ("Flags",                       EfiPy.UINT32),
        ("AddressOfControlArea",        EfiPy.UINT64),
        ("StartMethod",                 EfiPy.UINT32),
        ("PlatformSpecificParameters",  EfiPy.UINT8 * 12),
        ("Laml",                        EfiPy.UINT32),
        ("Lasa",                        EfiPy.UINT64)
]

#
# This is reference from http://msdn.microsoft.com/en-us/windows/hardware/gg487524.aspx
#
class EFIPY_WINDOWS_ACPI_EMULATED_DEVICES_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_ACPI_DESCRIPTION_HEADER),
    ("Flags",   EfiPy.UINT32)
  ]

#
# This is reference from http://go.microsoft.com/fwlink/p/?LinkId=234840
#
class EFIPY_WINDOWS_PLATFORM_BINARY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("HandoffMemorySize",       EfiPy.UINT32),
    ("HandoffMemoryLocation",   EfiPy.UINT64),
    ("ContentLayout",           EfiPy.UINT8),
    ("ContentType",             EfiPy.UINT8),
  ]

#
# This is reference from https://uefi.org/specs/UEFI/2.10/Apx_O_UEFI_ACPI_Data_Table.html#uefi-acpi-data-table
#
class EFIPY_UEFI_ACPI_DATA_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DESCRIPTION_HEADER),
    ("Identifier",          EfiPy.EFI_GUID),
    ("DataOffset",          EfiPy.UINT16),
    ("SwSmiNumber",         EfiPy.UINT32),
    ("BufferPtrAddress",    EfiPy.UINT64),
    ("InvocationRegister",  Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
  ]

AcpiMcfg = {
  1: EFIPY_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_DESCRIPTION_TABLE,
}

AcpiBgrt = {
  1: Acpi.EFI_ACPI_6_5_BOOT_GRAPHICS_RESOURCE_TABLE,
}

AcpiTpm2 = {
  3: EFI_TPM2_ACPI_TABLE,
  4: EFI_TPM2_ACPI_TABLE_V4,
}

AcpiWaet = {
  1: EFIPY_WINDOWS_ACPI_EMULATED_DEVICES_TABLE,
}

AcpiHpet = {
  1: EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_HEADER,
}

AcpiDmar = {
  1: EFI_ACPI_DMAR_HEADER,
}

AcpiAsf = {
  0x20: EFI_ACPI_ASF_DESCRIPTION_HEADER,
}

AcpiApic = {
  1: Acpi.EFI_ACPI_2_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER,
  2: Acpi.EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER,
  3: Acpi.EFI_ACPI_6_5_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER,
}

AcpiFacp = {
  1: Acpi.EFI_ACPI_1_0_FIXED_ACPI_DESCRIPTION_TABLE,
  3: Acpi.EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE,
  4: Acpi.EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE,
  5: Acpi.EFI_ACPI_5_1_FIXED_ACPI_DESCRIPTION_TABLE,
  6: Acpi.EFI_ACPI_6_5_FIXED_ACPI_DESCRIPTION_TABLE,
}

AcpiFacs = {
  1: Acpi.EFI_ACPI_3_0_FIRMWARE_ACPI_CONTROL_STRUCTURE,
  2: Acpi.EFI_ACPI_6_5_FIRMWARE_ACPI_CONTROL_STRUCTURE,
}

AcpiWdrt = {
  1: EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE,
}

AcpiUefi = {
  1: EFIPY_UEFI_ACPI_DATA_TABLE,
}

AcpiWpbt = {
  1: EFIPY_WINDOWS_PLATFORM_BINARY_TABLE,
}

AcpiDb = {
  b'MCFG': AcpiMcfg,
  b'FACP': AcpiFacp,
  b'FACS': AcpiFacs,
  b'TPM2': AcpiTpm2,
  b'APIC': AcpiApic,    # MADT
  b'BGRT': AcpiBgrt,
  b'WAET': AcpiWaet,
  b'HPET': AcpiHpet,
  b'DMAR': AcpiDmar,
  b'ASF!': AcpiAsf,
  b'WDRT': AcpiWdrt,
  b'UEFI': AcpiUefi,
  b'WPBT': AcpiWpbt,
}
