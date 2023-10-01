# Acpi10.py
#
# EfiPy2.MdePkg.IndustryStandard.Acpi10
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.AcpiAml import *

class EFI_ACPI_COMMON_HEADER (Structure):
  _fields_ = [
    ("Signature", UINT32),
    ("Length",    UINT32)
  ]

class EFI_ACPI_DESCRIPTION_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("Length",          UINT32),
    ("Revision",        UINT8),
    ("Checksum",        UINT8),
    ("OemId",           UINT8 * 6),
    ("OemTableId",      UINT64),
    ("OemRevision",     UINT32),
    ("CreatorId",       UINT32),
    ("CreatorRevision", UINT32)
  ]

ACPI_SMALL_IRQ_DESCRIPTOR_NAME                       = 0x04
ACPI_SMALL_DMA_DESCRIPTOR_NAME                       = 0x05
ACPI_SMALL_START_DEPENDENT_DESCRIPTOR_NAME           = 0x06
ACPI_SMALL_END_DEPENDENT_DESCRIPTOR_NAME             = 0x07
ACPI_SMALL_IO_PORT_DESCRIPTOR_NAME                   = 0x08
ACPI_SMALL_FIXED_IO_PORT_DESCRIPTOR_NAME             = 0x09
ACPI_SMALL_VENDOR_DEFINED_DESCRIPTOR_NAME            = 0x0E
ACPI_SMALL_END_TAG_DESCRIPTOR_NAME                   = 0x0F

ACPI_LARGE_24_BIT_MEMORY_RANGE_DESCRIPTOR_NAME       = 0x01
ACPI_LARGE_VENDOR_DEFINED_DESCRIPTOR_NAME            = 0x04
ACPI_LARGE_32_BIT_MEMORY_RANGE_DESCRIPTOR_NAME       = 0x05
ACPI_LARGE_32_BIT_FIXED_MEMORY_RANGE_DESCRIPTOR_NAME = 0x06
ACPI_LARGE_DWORD_ADDRESS_SPACE_DESCRIPTOR_NAME       = 0x07
ACPI_LARGE_WORD_ADDRESS_SPACE_DESCRIPTOR_NAME        = 0x08
ACPI_LARGE_EXTENDED_IRQ_DESCRIPTOR_NAME              = 0x09
ACPI_LARGE_QWORD_ADDRESS_SPACE_DESCRIPTOR_NAME       = 0x0A

ACPI_IRQ_NOFLAG_DESCRIPTOR                = 0x22
ACPI_IRQ_DESCRIPTOR                       = 0x23
ACPI_DMA_DESCRIPTOR                       = 0x2A
ACPI_START_DEPENDENT_DESCRIPTOR           = 0x30
ACPI_START_DEPENDENT_EX_DESCRIPTOR        = 0x31
ACPI_END_DEPENDENT_DESCRIPTOR             = 0x38
ACPI_IO_PORT_DESCRIPTOR                   = 0x47
ACPI_FIXED_LOCATION_IO_PORT_DESCRIPTOR    = 0x4B
ACPI_END_TAG_DESCRIPTOR                   = 0x79

ACPI_24_BIT_MEMORY_RANGE_DESCRIPTOR       = 0x81
ACPI_32_BIT_MEMORY_RANGE_DESCRIPTOR       = 0x85
ACPI_32_BIT_FIXED_MEMORY_RANGE_DESCRIPTOR = 0x86
ACPI_DWORD_ADDRESS_SPACE_DESCRIPTOR       = 0x87
ACPI_WORD_ADDRESS_SPACE_DESCRIPTOR        = 0x88
ACPI_EXTENDED_INTERRUPT_DESCRIPTOR        = 0x89
ACPI_QWORD_ADDRESS_SPACE_DESCRIPTOR       = 0x8A
ACPI_ADDRESS_SPACE_DESCRIPTOR             = 0x8A

ACPI_ADDRESS_SPACE_TYPE_MEM   = 0x00
ACPI_ADDRESS_SPACE_TYPE_IO    = 0x01
ACPI_ADDRESS_SPACE_TYPE_BUS   = 0x02

ACPI_TIMER_FREQUENCY       = 3579545

class EFI_ACPI_ADDRESS_SPACE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Desc",                  UINT8),
    ("Len",                   UINT16),
    ("ResType",               UINT8),
    ("GenFlag",               UINT8),
    ("SpecificFlag",          UINT8),
    ("AddrSpaceGranularity",  UINT64),
    ("AddrRangeMin",          UINT64),
    ("AddrRangeMax",          UINT64),
    ("AddrTranslationOffset", UINT64),
    ("AddrLen",               UINT64)
    ]

class ACPI_SMALL_RESOURCE_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",  UINT8, 3),
    ("Name",    UINT8, 4),
    ("Type",    UINT8, 1)
  ]

class ACPI_SMALL_RESOURCE_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Byte",  UINT8),
    ("Bits",  ACPI_SMALL_RESOURCE_HEADER_Bits)
  ]

class ACPI_LARGE_RESOURCE_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Name",    UINT8, 7),
    ("Type",    UINT8, 1)
  ]

class ACPI_LARGE_RESOURCE_HEADER_Union (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Byte",    UINT8),
    ("Bits",    ACPI_LARGE_RESOURCE_HEADER_Bits)
  ]

class ACPI_LARGE_RESOURCE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  ACPI_LARGE_RESOURCE_HEADER_Union),
    ("Length",  UINT16)
  ]

class EFI_ACPI_IRQ_NOFLAG_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  ACPI_SMALL_RESOURCE_HEADER),
    ("Mask",    UINT16)
  ]

class EFI_ACPI_IRQ_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      ACPI_SMALL_RESOURCE_HEADER),
    ("Mask",        UINT16),
    ("Information", UINT8)
  ]

class EFI_ACPI_DMA_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      ACPI_SMALL_RESOURCE_HEADER),
    ("ChannelMask", UINT8),
    ("Information", UINT8)
  ]

class EFI_ACPI_IO_PORT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          ACPI_SMALL_RESOURCE_HEADER),
    ("Information",     UINT8),
    ("BaseAddressMin",  UINT16),
    ("BaseAddressMax",  UINT16),
    ("Alignment",       UINT8),
    ("Length",          UINT8)
  ]

class EFI_ACPI_FIXED_LOCATION_IO_PORT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      ACPI_SMALL_RESOURCE_HEADER),
    ("BaseAddress", UINT16),
    ("Length",      UINT8)
  ]

class EFI_ACPI_24_BIT_MEMORY_RANGE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          ACPI_LARGE_RESOURCE_HEADER),
    ("Information",     UINT8),
    ("BaseAddressMin",  UINT16),
    ("BaseAddressMax",  UINT16),
    ("Alignment",       UINT16),
    ("Length",          UINT16)
  ]

class EFI_ACPI_32_BIT_MEMORY_RANGE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          ACPI_LARGE_RESOURCE_HEADER),
    ("Information",     UINT8),
    ("BaseAddressMin",  UINT32),
    ("BaseAddressMax",  UINT32),
    ("Alignment",       UINT32),
    ("Length",          UINT32)
  ]

class EFI_ACPI_32_BIT_FIXED_MEMORY_RANGE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      ACPI_LARGE_RESOURCE_HEADER),
    ("Information", UINT8),
    ("BaseAddress", UINT32),
    ("Length",      UINT32)
  ]

class EFI_ACPI_QWORD_ADDRESS_SPACE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                ACPI_LARGE_RESOURCE_HEADER),
    ("ResType",               UINT8),
    ("GenFlag",               UINT8),
    ("SpecificFlag",          UINT8),
    ("AddrSpaceGranularity",  UINT64),
    ("AddrRangeMin",          UINT64),
    ("AddrRangeMax",          UINT64),
    ("AddrTranslationOffset", UINT64),
    ("AddrLen",               UINT64)
  ]

class EFI_ACPI_DWORD_ADDRESS_SPACE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                ACPI_LARGE_RESOURCE_HEADER),
    ("ResType",               UINT8),
    ("GenFlag",               UINT8),
    ("SpecificFlag",          UINT8),
    ("AddrSpaceGranularity",  UINT32),
    ("AddrRangeMin",          UINT32),
    ("AddrRangeMax",          UINT32),
    ("AddrTranslationOffset", UINT32),
    ("AddrLen",               UINT32)
  ]

class EFI_ACPI_WORD_ADDRESS_SPACE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                ACPI_LARGE_RESOURCE_HEADER),
    ("ResType",               UINT8),
    ("GenFlag",               UINT8),
    ("SpecificFlag",          UINT8),
    ("AddrSpaceGranularity",  UINT16),
    ("AddrRangeMin",          UINT16),
    ("AddrRangeMax",          UINT16),
    ("AddrTranslationOffset", UINT16),
    ("AddrLen",               UINT16)
  ]

class EFI_ACPI_EXTENDED_INTERRUPT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                ACPI_LARGE_RESOURCE_HEADER),
    ("InterruptVectorFlags",  UINT8),
    ("InterruptTableLength",  UINT8),
    ("InterruptNumber",       UINT32 * 1)
  ]

class EFI_ACPI_END_TAG_DESCRIPTOR (Structure):
  _fields_ = [
    ("Desc",      UINT8),
    ("Checksum",  UINT8)
  ]

EFI_ACPI_RESERVED_BYTE  = 0x00
EFI_ACPI_RESERVED_WORD  = 0x0000
EFI_ACPI_RESERVED_DWORD = 0x00000000
EFI_ACPI_RESERVED_QWORD = 0x0000000000000000

EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_READ_WRITE                = (1 << 0)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_READ_ONLY                 = (0 << 0)

EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_NON_CACHEABLE             = (0 << 1)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_CACHEABLE                 = (1 << 1)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_CACHEABLE_WRITE_COMBINING = (2 << 1)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_CACHEABLE_PREFETCHABLE    = (3 << 1)

EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_ADDRESS_RANGE_MEMORY      = (0 << 3)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_ADDRESS_RANGE_RESERVED    = (1 << 3)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_ADDRESS_RANGE_ACPI        = (2 << 3)
EFI_APCI_MEMORY_RESOURCE_SPECIFIC_FLAG_ADDRESS_RANGE_NVS         = (3 << 3)

EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_TYPE_TRANSLATION          = (1 << 5)
EFI_ACPI_MEMORY_RESOURCE_SPECIFIC_FLAG_TYPE_STATIC               = (0 << 5)

EFI_ACPI_IRQ_SHARABLE_MASK                      = 0x10
EFI_ACPI_IRQ_SHARABLE                           = 0x10

EFI_ACPI_IRQ_POLARITY_MASK                      = 0x08
EFI_ACPI_IRQ_HIGH_TRUE                          = 0x00
EFI_ACPI_IRQ_LOW_FALSE                          = 0x08

EFI_ACPI_IRQ_MODE                               = 0x01
EFI_ACPI_IRQ_LEVEL_TRIGGERED                    = 0x00
EFI_ACPI_IRQ_EDGE_TRIGGERED                     = 0x01

EFI_ACPI_DMA_SPEED_TYPE_MASK                    = 0x60
EFI_ACPI_DMA_SPEED_TYPE_COMPATIBILITY           = 0x00
EFI_ACPI_DMA_SPEED_TYPE_A                       = 0x20
EFI_ACPI_DMA_SPEED_TYPE_B                       = 0x40
EFI_ACPI_DMA_SPEED_TYPE_F                       = 0x60

EFI_ACPI_DMA_BUS_MASTER_MASK                    = 0x04
EFI_ACPI_DMA_BUS_MASTER                         = 0x04

EFI_ACPI_DMA_TRANSFER_TYPE_MASK                 = 0x03
EFI_ACPI_DMA_TRANSFER_TYPE_8_BIT                = 0x00
EFI_ACPI_DMA_TRANSFER_TYPE_8_BIT_AND_16_BIT     = 0x01
EFI_ACPI_DMA_TRANSFER_TYPE_16_BIT               = 0x10

EFI_ACPI_IO_DECODE_MASK                         = 0x01
EFI_ACPI_IO_DECODE_16_BIT                       = 0x01
EFI_ACPI_IO_DECODE_10_BIT                       = 0x00

EFI_ACPI_MEMORY_WRITE_STATUS_MASK               = 0x01
EFI_ACPI_MEMORY_WRITABLE                        = 0x01
EFI_ACPI_MEMORY_NON_WRITABLE                    = 0x00

class EFI_ACPI_1_0_ROOT_SYSTEM_DESCRIPTION_POINTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",   UINT64),
    ("Checksum",    UINT8),
    ("OemId",       UINT8 * 6),
    ("Reserved",    UINT8),
    ("RsdtAddress", UINT32)
  ]

EFI_ACPI_1_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_1_0_FIXED_ACPI_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        EFI_ACPI_DESCRIPTION_HEADER),
    ("FirmwareCtrl",  UINT32),
    ("Dsdt",          UINT32),
    ("IntModel",      UINT8),
    ("Reserved1",     UINT8),
    ("SciInt",        UINT16),
    ("SmiCmd",        UINT32),
    ("AcpiEnable",    UINT8),
    ("AcpiDisable",   UINT8),
    ("S4BiosReq",     UINT8),
    ("Reserved2",     UINT8),
    ("Pm1aEvtBlk",    UINT32),
    ("Pm1bEvtBlk",    UINT32),
    ("Pm1aCntBlk",    UINT32),
    ("Pm1bCntBlk",    UINT32),
    ("Pm2CntBlk",     UINT32),
    ("PmTmrBlk",      UINT32),
    ("Gpe0Blk",       UINT32),
    ("Gpe1Blk",       UINT32),
    ("Pm1EvtLen",     UINT8),
    ("Pm1CntLen",     UINT8),
    ("Pm2CntLen",     UINT8),
    ("PmTmLen",       UINT8),
    ("Gpe0BlkLen",    UINT8),
    ("Gpe1BlkLen",    UINT8),
    ("Gpe1Base",      UINT8),
    ("Reserved3",     UINT8),
    ("PLvl2Lat",      UINT16),
    ("PLvl3Lat",      UINT16),
    ("FlushSize",     UINT16),
    ("FlushStride",   UINT16),
    ("DutyOffset",    UINT8),
    ("DutyWidth",     UINT8),
    ("DayAlrm",       UINT8),
    ("MonAlrm",       UINT8),
    ("Century",       UINT8),
    ("Reserved4",     UINT8),
    ("Reserved5",     UINT8),
    ("Reserved6",     UINT8),
    ("Flags",         UINT32)
  ]

EFI_ACPI_1_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x01

EFI_ACPI_1_0_INT_MODE_DUAL_PIC         = 0
EFI_ACPI_1_0_INT_MODE_MULTIPLE_APIC    = 1

EFI_ACPI_1_0_WBINVD               = BIT0
EFI_ACPI_1_0_WBINVD_FLUSH         = BIT1
EFI_ACPI_1_0_PROC_C1              = BIT2
EFI_ACPI_1_0_P_LVL2_UP            = BIT3
EFI_ACPI_1_0_PWR_BUTTON           = BIT4
EFI_ACPI_1_0_SLP_BUTTON           = BIT5
EFI_ACPI_1_0_FIX_RTC              = BIT6
EFI_ACPI_1_0_RTC_S4               = BIT7
EFI_ACPI_1_0_TMR_VAL_EXT          = BIT8
EFI_ACPI_1_0_DCK_CAP              = BIT9

class EFI_ACPI_1_0_FIRMWARE_ACPI_CONTROL_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",             UINT32),
    ("Length",                UINT32),
    ("HardwareSignature",     UINT32),
    ("FirmwareWakingVector",  UINT32),
    ("GlobalLock",            UINT32),
    ("Flags",                 UINT32),
    ("Reserved",              UINT8 * 40)
  ]

EFI_ACPI_1_0_S4BIOS_F             = BIT0

class EFI_ACPI_1_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_ACPI_DESCRIPTION_HEADER),
    ("LocalApicAddress",  UINT32),
    ("Flags",             UINT32)
  ]

EFI_ACPI_1_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_1_0_PCAT_COMPAT           = BIT0

EFI_ACPI_1_0_PROCESSOR_LOCAL_APIC           = 0x00
EFI_ACPI_1_0_IO_APIC                        = 0x01
EFI_ACPI_1_0_INTERRUPT_SOURCE_OVERRIDE      = 0x02
EFI_ACPI_1_0_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
EFI_ACPI_1_0_LOCAL_APIC_NMI                 = 0x04

class EFI_ACPI_1_0_PROCESSOR_LOCAL_APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("AcpiProcessorId", UINT8),
    ("ApicId",          UINT8),
    ("Flags",           UINT32)
  ]

EFI_ACPI_1_0_LOCAL_APIC_ENABLED      = BIT0

class EFI_ACPI_1_0_IO_APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("IoApicId",          UINT8),
    ("Reserved",          UINT8),
    ("IoApicAddress",     UINT32),
    ("SystemVectorBase",  UINT32)
  ]

class EFI_ACPI_1_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                        UINT8),
    ("Length",                      UINT8),
    ("Bus",                         UINT8),
    ("Source",                      UINT8),
    ("GlobalSystemInterruptVector", UINT32),
    ("Flags",                       UINT16)
  ]

class EFI_ACPI_1_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                        UINT8),
    ("Length",                      UINT8),
    ("Flags",                       UINT16),
    ("GlobalSystemInterruptVector", UINT32)
  ]

class EFI_ACPI_1_0_LOCAL_APIC_NMI_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("AcpiProcessorId", UINT8),
    ("Flags",           UINT16),
    ("LocalApicInti",   UINT8)
  ]

class EFI_ACPI_1_0_SMART_BATTERY_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DESCRIPTION_HEADER),
    ("WarningEnergyLevel",  UINT32),
    ("LowEnergyLevel",      UINT32),
    ("CriticalEnergyLevel", UINT32)
  ]

EFI_ACPI_1_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = SIGNATURE_64('R', 'S', 'D', ' ', 'P', 'T', 'R', ' ')
EFI_ACPI_1_0_APIC_SIGNATURE  = SIGNATURE_32('A', 'P', 'I', 'C')
EFI_ACPI_1_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('D', 'S', 'D', 'T')
EFI_ACPI_1_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = SIGNATURE_32('F', 'A', 'C', 'S')
EFI_ACPI_1_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('F', 'A', 'C', 'P')
EFI_ACPI_1_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('P', 'S', 'D', 'T')
EFI_ACPI_1_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('R', 'S', 'D', 'T')
EFI_ACPI_1_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'B', 'S', 'T')
EFI_ACPI_1_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'S', 'D', 'T')
