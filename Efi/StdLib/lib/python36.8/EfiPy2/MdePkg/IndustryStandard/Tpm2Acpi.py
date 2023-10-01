# Tpm2Acpi.py
#
# EfiPy2.MdePkg.IndustryStandard.Tpm2Acpi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

EFI_TPM2_ACPI_TABLE_REVISION_3  = 3
EFI_TPM2_ACPI_TABLE_REVISION_4  = 4
EFI_TPM2_ACPI_TABLE_REVISION  = EFI_TPM2_ACPI_TABLE_REVISION_4  

class EFI_TPM2_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",                      Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Flags",                       UINT32),
    ("AddressOfControlArea",        UINT64),
    ("StartMethod",                 UINT32)
    # ("PlatformSpecificParameters",  UINT8 * N),
    # ("Laml",                        UINT32),
    # ("Lasa",                        UINT64),
  ]

EFI_TPM2_ACPI_TABLE_START_METHOD_ACPI                                          = 2
EFI_TPM2_ACPI_TABLE_START_METHOD_TIS                                           = 6
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE             = 7
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_ACPI   = 8
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_SMC   = 11

class EFI_TPM2_ACPI_CONTROL_AREA (Structure):
  _fields_ = [
    ("Reserved",          UINT32),
    ("Error",             UINT32),
    ("Cancel",            UINT32),
    ("Start",             UINT32),
    ("InterruptControl",  UINT64),
    ("CommandSize",       UINT32),
    ("Command",           UINT64),
    ("ResponseSize",      UINT32),
    ("Response",          UINT64)
  ]

class EFI_TPM2_ACPI_START_METHOD_SPECIFIC_PARAMETERS_ARM_SMC (Structure):
  _fields_ = [
    ("Interrupt",       UINT32),
    ("Flags",           UINT8),
    ("OperationFlags",  UINT8),
    ("Reserved",        UINT8 * 2),
    ("SmcFunctionId",   UINT32)
  ]

