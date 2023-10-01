# AcpiTable.py
#
# EfiPy2.MdePkg.Protocol.AcpiTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiAcpiTableProtocolGuid               = \
  EFI_GUID (0xffe06bdd, 0x6107, 0x46a6, ( 0x7b, 0xb2, 0x5a, 0x9c, 0x7e, 0xc5, 0x27, 0x5c ))

class EFI_ACPI_TABLE_PROTOCOL (Structure):
  pass

EFI_ACPI_TABLE_INSTALL_ACPI_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_TABLE_PROTOCOL), # IN  *This
  PVOID,                            # IN  *AcpiTableBuffer
  UINTN,                            # IN  AcpiTableBufferSize
  POINTER (UINTN)                   # OUT *TableKey
  )

EFI_ACPI_TABLE_UNINSTALL_ACPI_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_TABLE_PROTOCOL), # IN  *This
  UINTN                             # IN  TableKey
  )

EFI_ACPI_TABLE_PROTOCOL._fields_ = [
    ("InstallAcpiTable",    EFI_ACPI_TABLE_INSTALL_ACPI_TABLE),
    ("UninstallAcpiTable",  EFI_ACPI_TABLE_UNINSTALL_ACPI_TABLE)
  ]

