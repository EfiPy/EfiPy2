# ArmPerformanceMonitoringUnitTable.py
#
# EfiPy2.MdePkg.IndustryStandard.ArmPerformanceMonitoringUnitTable
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE

class EFI_ACPI_ARM_PERFORMANCE_MONITORING_UNIT_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        Acpi.EFI_ACPI_DESCRIPTION_HEADER)
  ]

EFI_ACPI_ARM_PERFORMANCE_MONITORING_UNIT_TABLE_REVISION  = 0x00

EFI_ACPI_APMT_DUAL_PAGE_EXTENSION_SUPPORTED          = BIT0
EFI_ACPI_APMT_PROCESSOR_AFFINITY_TYPE_CONTAINER      = BIT1
EFI_ACPI_APMT_PROCESSOR_AFFINITY_TYPE_PROCESSOR      = 0 # BIT 1
EFI_ACPI_APMT_64BIT_SINGLE_COPY_ATOMICITY_SUPPORTED  = BIT2

EFI_ACPI_APMT_INTERRUPT_MODE_EDGE_TRIGGERED   = BIT0
EFI_ACPI_APMT_INTERRUPT_MODE_LEVEL_TRIGGERED  = 0 # BIT 0
EFI_ACPI_APMT_INTERRUPT_TYPE_WIRED            = 0 # BIT 1

EFI_ACPI_APMT_NODE_TYPE_MEMORY_CONTROLLER  = 0x00
EFI_ACPI_APMT_NODE_TYPE_SMMU               = 0x01
EFI_ACPI_APMT_NODE_TYPE_PCIE_ROOT_COMPLEX  = 0x02
EFI_ACPI_APMT_NODE_TYPE_ACPI_DEVICE        = 0x03
EFI_ACPI_APMT_NODE_TYPE_CPU_CACHE          = 0x04

class EFI_ACPI_ARM_PERFORMANCE_MONITORING_UNIT_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",                  UINT16),
    ("NodeFlags",               UINT8),
    ("NodeType",                UINT8),
    ("Identifier",              UINT32),
    ("NodeInstancePrimary",     UINT64),
    ("NodeInstanceSecondary",   UINT32),
    ("BaseAddress0",            UINT64),
    ("BaseAddress1",            UINT64),
    ("OverflowInterrupt",       UINT32),
    ("Reserved1",               UINT32),
    ("OverflowInterruptFlags",  UINT32),
    ("ProcessorAffinity",       UINT32),
    ("ImplementationId",        UINT32)
  ]

