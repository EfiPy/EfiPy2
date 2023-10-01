# TcpaAcpi.py
#
# EfiPy2.MdePkg.IndustryStandard.TcpaAcpi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class EFI_TCG_CLIENT_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",        Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformClass", UINT16),
    ("Laml",          UINT32),
    ("Lasa",          UINT64)
  ]

class EFI_TCG_SERVER_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",          Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformClass",   UINT16),
    ("Reserved0",       UINT16),
    ("Laml",            UINT64),
    ("Lasa",            UINT64),
    ("SpecRev",         UINT16),
    ("DeviceFlags",     UINT8),
    ("InterruptFlags",  UINT8),
    ("Gpe",             UINT8),
    ("Reserved1",       UINT8 * 3),
    ("GlobalSysInt",    UINT32),
    ("BaseAddress",     Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("Reserved2",       UINT32),
    ("ConfigAddress",   Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("PciSegNum",       UINT8),
    ("PciBusNum",       UINT8),
    ("PciDevNum",       UINT8),
    ("PciFuncNum",      UINT8)
  ]

TCG_PLATFORM_TYPE_CLIENT   = 0
TCG_PLATFORM_TYPE_SERVER   = 1

