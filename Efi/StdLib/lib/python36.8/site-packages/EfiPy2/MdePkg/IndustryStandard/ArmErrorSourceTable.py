# ArmErrorSourceTable.py
#
# EfiPy2.MdePkg.IndustryStandard.ArmErrorSourceTable
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION

EFI_ACPI_6_3_ARM_ERROR_SOURCE_TABLE_SIGNATURE  = SIGNATURE_32('A', 'E', 'S', 'T')

EFI_ACPI_ARM_ERROR_SOURCE_TABLE_REVISION  = 1

class EFI_ACPI_ARM_ERROR_SOURCE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        Acpi.EFI_ACPI_DESCRIPTION_HEADER)
  ]

class EFI_ACPI_AEST_NODE_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT8),
    ("Length",                          UINT16),
    ("Reserved",                        UINT8),
    ("DataOffset",                      UINT32),
    ("InterfaceOffset",                 UINT32),
    ("InterruptArrayOffset",            UINT32),
    ("InterruptArrayCount",             UINT32),
    ("TimestampRate",                   UINT64),
    ("Reserved1",                       UINT64),
    ("ErrorInjectionCountdownRate",     UINT64)
  ]

EFI_ACPI_AEST_NODE_TYPE_PROCESSOR       = 0x0
EFI_ACPI_AEST_NODE_TYPE_MEMORY          = 0x1
EFI_ACPI_AEST_NODE_TYPE_SMMU            = 0x2
EFI_ACPI_AEST_NODE_TYPE_VENDOR_DEFINED  = 0x3
EFI_ACPI_AEST_NODE_TYPE_GIC             = 0x4

class EFI_ACPI_AEST_INTERFACE_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                    UINT8),
    ("Reserved",                                UINT8 * 3),
    ("Flags",                                   UINT32),
    ("BaseAddress",                             UINT64),
    ("StartErrorRecordIndex",                   UINT32),
    ("NumberErrorRecords",                      UINT32),
    ("ErrorRecordImplemented",                  UINT64),
    ("ErrorRecordStatusReportingSupported",     UINT64),
    ("AddressingMode",                          UINT64)
  ]

EFI_ACPI_AEST_INTERFACE_TYPE_SR    = 0x0
EFI_ACPI_AEST_INTERFACE_TYPE_MMIO  = 0x1

EFI_ACPI_AEST_INTERFACE_FLAG_PRIVATE      = 0
EFI_ACPI_AEST_INTERFACE_FLAG_SHARED       = BIT0
EFI_ACPI_AEST_INTERFACE_FLAG_CLEAR_MISCX  = BIT1

class EFI_ACPI_AEST_INTERRUPT_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InterruptType",   UINT8),
    ("Reserved",        UINT8 * 2),
    ("InterruptFlags",  UINT8),
    ("InterruptGsiv",   UINT32),
    ("ItsGroupRefId",   UINT8),
    ("Reserved1",       UINT8 * 3)
  ]

EFI_ACPI_AEST_INTERRUPT_TYPE_FAULT_HANDLING  = 0x0
EFI_ACPI_AEST_INTERRUPT_TYPE_ERROR_RECOVERY  = 0x1

EFI_ACPI_AEST_INTERRUPT_FLAG_TRIGGER_TYPE_EDGE   = 0
EFI_ACPI_AEST_INTERRUPT_FLAG_TRIGGER_TYPE_LEVEL  = BIT0

class EFI_ACPI_AEST_PROCESSOR_CACHE_RESOURCE_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheRefId",      UINT32),
    ("Reserved",        UINT32)
  ]

class EFI_ACPI_AEST_PROCESSOR_TLB_RESOURCE_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TlbRefId",        UINT32),
    ("Reserved",        UINT32)
  ]

class EFI_ACPI_AEST_PROCESSOR_GENERIC_RESOURCE_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",        UINT32)
  ]

class EFI_ACPI_AEST_PROCESSOR_RESOURCE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Cache",       EFI_ACPI_AEST_PROCESSOR_CACHE_RESOURCE_STRUCT),
    ("Tlb",         EFI_ACPI_AEST_PROCESSOR_TLB_RESOURCE_STRUCT),
    ("Generic",     EFI_ACPI_AEST_PROCESSOR_GENERIC_RESOURCE_STRUCT)
  ]

class EFI_ACPI_AEST_PROCESSOR_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NodeHeader",                          EFI_ACPI_AEST_NODE_STRUCT),
    ("AcpiProcessorId",                     UINT32),
    ("ResourceType",                        UINT8),
    ("Reserved",                            UINT8),
    ("Flags",                               UINT8),
    ("Revision",                            UINT8),
    ("ProcessorAffinityLevelIndicator",     UINT64),
    ("Resource",                            EFI_ACPI_AEST_PROCESSOR_RESOURCE)

    # ("NodeInterface",                       EFI_ACPI_AEST_INTERFACE_STRUCT),
    # ("NodeInterruptArray",                  EFI_ACPI_AEST_INTERRUPT_STRUCT * n)
  ]

EFI_ACPI_AEST_PROCESSOR_RESOURCE_TYPE_CACHE    = 0x0
EFI_ACPI_AEST_PROCESSOR_RESOURCE_TYPE_TLB      = 0x1
EFI_ACPI_AEST_PROCESSOR_RESOURCE_TYPE_GENERIC  = 0x2

EFI_ACPI_AEST_PROCESSOR_FLAG_GLOBAL  = BIT0
EFI_ACPI_AEST_PROCESSOR_FLAG_SHARED  = BIT1

class EFI_ACPI_AEST_MEMORY_CONTROLLER_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NodeHeader",      EFI_ACPI_AEST_NODE_STRUCT),
    ("ProximityDomain", UINT32)

    # ("NodeInterface",       EFI_ACPI_AEST_INTERFACE_STRUCT),
    # ("NodeInterruptArray",  EFI_ACPI_AEST_INTERRUPT_STRUCT * n)
  ]

class EFI_ACPI_AEST_SMMU_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NodeHeader",          EFI_ACPI_AEST_NODE_STRUCT),
    ("SmmuRefId",           UINT32),
    ("SubComponentRefId",   UINT32)

    # ("NodeInterface",       EFI_ACPI_AEST_INTERFACE_STRUCT),
    # ("NodeInterruptArray"   EFI_ACPI_AEST_INTERRUPT_STRUCT * n)
  ]

class EFI_ACPI_AEST_VENDOR_DEFINED_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NodeHeader",      EFI_ACPI_AEST_NODE_STRUCT),
    ("HardwareId",      UINT32),
    ("UniqueId",        UINT32),
    ("VendorData",      UINT8 * 16)

    # ("NodeInterface",       EFI_ACPI_AEST_INTERFACE_STRUCT),
    # ("NodeInterruptArray",  EFI_ACPI_AEST_INTERRUPT_STRUCT * n)
  ]

class EFI_ACPI_AEST_GIC_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NodeHeader",          EFI_ACPI_AEST_NODE_STRUCT),
    ("InterfaceType",       UINT32),
    ("GicInterfaceRefId",   UINT32)

    # ("NodeInterface",       EFI_ACPI_AEST_INTERFACE_STRUCT),
    # ("NodeInterruptArray",  EFI_ACPI_AEST_INTERRUPT_STRUCT * n)
  ]

EFI_ACPI_AEST_GIC_INTERFACE_TYPE_GICC  = 0x0
EFI_ACPI_AEST_GIC_INTERFACE_TYPE_GICD  = 0x1
EFI_ACPI_AEST_GIC_INTERFACE_TYPE_GICR  = 0x2
EFI_ACPI_AEST_GIC_INTERFACE_TYPE_GITS  = 0x3

