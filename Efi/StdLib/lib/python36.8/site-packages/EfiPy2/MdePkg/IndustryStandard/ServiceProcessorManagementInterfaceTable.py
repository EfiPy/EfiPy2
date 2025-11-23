# ServiceProcessorManagementInterfaceTable.py
#
# EfiPy2.MdePkg.IndustryStandard.ServiceProcessorManagementInterfaceTable
#   part of EfiPy2
#
# Copyright (C) 2023 -2025ир MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class EFI_ACPI_SERVICE_PROCESSOR_MANAGEMENT_INTERFACE_TABLE_DEVICE_ID_Pci (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SegmentGroup",    UINT8),
    ("Bus",             UINT8),
    ("Device",          UINT8),
    ("Function",        UINT8)
  ]

class EFI_ACPI_SERVICE_PROCESSOR_MANAGEMENT_INTERFACE_TABLE_DEVICE_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Pci", EFI_ACPI_SERVICE_PROCESSOR_MANAGEMENT_INTERFACE_TABLE_DEVICE_ID_Pci),
    ("Uid", UINT32)
  ]

class EFI_ACPI_SERVICE_PROCESSOR_MANAGEMENT_INTERFACE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  Acpi.EFI_ACPI_DESCRIPTION_HEADER                               ),
    ("InterfaceType",           UINT8                                                          ),
    ("Reserved1",               UINT8                                                          ),
    ("SpecificationRevision",   UINT16                                                         ),
    ("InterruptType",           UINT8                                                          ),
    ("Gpe",                     UINT8                                                          ),
    ("Reserved2",               UINT8                                                          ),
    ("PciDeviceFlag",           UINT8                                                          ),
    ("GlobalSystemInterrupt",   UINT32                                                         ),
    ("BaseAddress",             Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE                    ),
    ("DeviceId",                EFI_ACPI_SERVICE_PROCESSOR_MANAGEMENT_INTERFACE_TABLE_DEVICE_ID),
    ("Reserved3",               UINT8                                                          )
  ]

EFI_ACPI_SERVICE_PROCESSOR_MANAGEMENT_INTERFACE_5_TABLE_REVISION  = 0x05

EFI_ACPI_SPMI_INTERFACE_TYPE_KCS   = 0x01
EFI_ACPI_SPMI_INTERFACE_TYPE_SMIC  = 0x02
EFI_ACPI_SPMI_INTERFACE_TYPE_BT    = 0x03
EFI_ACPI_SPMI_INTERFACE_TYPE_SSIF  = 0x04
