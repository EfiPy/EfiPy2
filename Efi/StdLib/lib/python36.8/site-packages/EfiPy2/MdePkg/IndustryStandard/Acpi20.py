# Acpi20.py
#
# EfiPy2.MdePkg.IndustryStandard.Acpi20
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.Acpi10 import *

ACPI_LARGE_GENERIC_REGISTER_DESCRIPTOR_NAME          = 0x02

ACPI_GENERIC_REGISTER_DESCRIPTOR          = 0x82

class EFI_ACPI_GENERIC_REGISTER_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            ACPI_LARGE_RESOURCE_HEADER),
    ("AddressSpaceId",    UINT8),
    ("RegisterBitWidth",  UINT8),
    ("RegisterBitOffset", UINT8),
    ("AddressSize",       UINT8),
    ("RegisterAddress",   UINT64)
  ]

class EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressSpaceId",    UINT8),
    ("RegisterBitWidth",  UINT8),
    ("RegisterBitOffset", UINT8),
    ("Reserved",          UINT8),
    ("Address",           UINT64)
  ]

EFI_ACPI_2_0_SYSTEM_MEMORY              = 0
EFI_ACPI_2_0_SYSTEM_IO                  = 1
EFI_ACPI_2_0_PCI_CONFIGURATION_SPACE    = 2
EFI_ACPI_2_0_EMBEDDED_CONTROLLER        = 3
EFI_ACPI_2_0_SMBUS                      = 4
EFI_ACPI_2_0_FUNCTIONAL_FIXED_HARDWARE  = 0x7F

class EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",         UINT64),
    ("Checksum",          UINT8),
    ("OemId",             UINT8 * 6),
    ("Revision",          UINT8),
    ("RsdtAddress",       UINT32),
    ("Length",            UINT32),
    ("XsdtAddress",       UINT64),
    ("ExtendedChecksum",  UINT8),
    ("Reserved",          UINT8 * 3)
  ]

EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION = 0x02

EFI_ACPI_2_0_COMMON_HEADER = EFI_ACPI_COMMON_HEADER

EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_2_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DESCRIPTION_HEADER),
    ("FirmwareCtrl",        UINT32),
    ("Dsdt",                UINT32),
    ("Reserved0",           UINT8),
    ("PreferredPmProfile",  UINT8),
    ("SciInt",              UINT16),
    ("SmiCmd",              UINT32),
    ("AcpiEnable",          UINT8),
    ("AcpiDisable",         UINT8),
    ("S4BiosReq",           UINT8),
    ("PstateCnt",           UINT8),
    ("Pm1aEvtBlk",          UINT32),
    ("Pm1bEvtBlk",          UINT32),
    ("Pm1aCntBlk",          UINT32),
    ("Pm1bCntBlk",          UINT32),
    ("Pm2CntBlk",           UINT32),
    ("PmTmrBlk",            UINT32),
    ("Gpe0Blk",             UINT32),
    ("Gpe1Blk",             UINT32),
    ("Pm1EvtLen",           UINT8),
    ("Pm1CntLen",           UINT8),
    ("Pm2CntLen",           UINT8),
    ("PmTmrLen",            UINT8),
    ("Gpe0BlkLen",          UINT8),
    ("Gpe1BlkLen",          UINT8),
    ("Gpe1Base",            UINT8),
    ("CstCnt",              UINT8),
    ("PLvl2Lat",            UINT16),
    ("PLvl3Lat",            UINT16),
    ("FlushSize",           UINT16),
    ("FlushStride",         UINT16),
    ("DutyOffset",          UINT8),
    ("DutyWidth",           UINT8),
    ("DayAlrm",             UINT8),
    ("MonAlrm",             UINT8),
    ("Century",             UINT8),
    ("IaPcBootArch",        UINT16),
    ("Reserved1",           UINT8),
    ("Flags",               UINT32),
    ("ResetReg",            EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("ResetValue",          UINT8),
    ("Reserved2",           UINT8 * 3),
    ("XFirmwareCtrl",       UINT64),
    ("XDsdt",               UINT64),
    ("XPm1aEvtBlk",         EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bEvtBlk",         EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1aCntBlk",         EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bCntBlk",         EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPm2CntBlk",          EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XPmTmrBlk",           EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe0Blk",            EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe1Blk",            EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE)
  ]

EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x03

EFI_ACPI_2_0_PM_PROFILE_UNSPECIFIED         = 0
EFI_ACPI_2_0_PM_PROFILE_DESKTOP             = 1
EFI_ACPI_2_0_PM_PROFILE_MOBILE              = 2
EFI_ACPI_2_0_PM_PROFILE_WORKSTATION         = 3
EFI_ACPI_2_0_PM_PROFILE_ENTERPRISE_SERVER   = 4
EFI_ACPI_2_0_PM_PROFILE_SOHO_SERVER         = 5
EFI_ACPI_2_0_PM_PROFILE_APPLIANCE_PC        = 6

EFI_ACPI_2_0_LEGACY_DEVICES          = BIT0
EFI_ACPI_2_0_8042                    = BIT1

EFI_ACPI_2_0_WBINVD                  = BIT0
EFI_ACPI_2_0_WBINVD_FLUSH            = BIT1
EFI_ACPI_2_0_PROC_C1                 = BIT2
EFI_ACPI_2_0_P_LVL2_UP               = BIT3
EFI_ACPI_2_0_PWR_BUTTON              = BIT4
EFI_ACPI_2_0_SLP_BUTTON              = BIT5
EFI_ACPI_2_0_FIX_RTC                 = BIT6
EFI_ACPI_2_0_RTC_S4                  = BIT7
EFI_ACPI_2_0_TMR_VAL_EXT             = BIT8
EFI_ACPI_2_0_DCK_CAP                 = BIT9
EFI_ACPI_2_0_RESET_REG_SUP           = BIT10
EFI_ACPI_2_0_SEALED_CASE             = BIT11
EFI_ACPI_2_0_HEADLESS                = BIT12
EFI_ACPI_2_0_CPU_SW_SLP              = BIT13

class EFI_ACPI_2_0_FIRMWARE_ACPI_CONTROL_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",             UINT32),
    ("Length",                UINT32),
    ("HardwareSignature",     UINT32),
    ("FirmwareWakingVector",  UINT32),
    ("GlobalLock",            UINT32),
    ("Flags",                 UINT32),
    ("XFirmwareWakingVector", UINT64),
    ("Version",               UINT8),
    ("Reserved",              UINT8 * 31)
  ]

EFI_ACPI_2_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  = 0x01

EFI_ACPI_2_0_S4BIOS_F        = BIT0

EFI_ACPI_2_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER = EFI_ACPI_1_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER

EFI_ACPI_2_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_2_0_PCAT_COMPAT          = BIT0

EFI_ACPI_2_0_PROCESSOR_LOCAL_APIC           = 0x00
EFI_ACPI_2_0_IO_APIC                        = 0x01
EFI_ACPI_2_0_INTERRUPT_SOURCE_OVERRIDE      = 0x02
EFI_ACPI_2_0_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
EFI_ACPI_2_0_LOCAL_APIC_NMI                 = 0x04
EFI_ACPI_2_0_LOCAL_APIC_ADDRESS_OVERRIDE    = 0x05
EFI_ACPI_2_0_IO_SAPIC                       = 0x06
EFI_ACPI_2_0_PROCESSOR_LOCAL_SAPIC          = 0x07
EFI_ACPI_2_0_PLATFORM_INTERRUPT_SOURCES     = 0x08

EFI_ACPI_2_0_PROCESSOR_LOCAL_APIC_STRUCTURE = EFI_ACPI_1_0_PROCESSOR_LOCAL_APIC_STRUCTURE

EFI_ACPI_2_0_LOCAL_APIC_ENABLED         = BIT0

class EFI_ACPI_2_0_IO_APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                      UINT8),
    ("Length",                    UINT8),
    ("IoApicId",                  UINT8),
    ("Reserved",                  UINT8),
    ("IoApicAddress",             UINT32),
    ("GlobalSystemInterruptBase", UINT32)
  ]

class EFI_ACPI_2_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Length",                UINT8),
    ("Bus",                   UINT8),
    ("Source",                UINT8),
    ("GlobalSystemInterrupt", UINT32),
    ("Flags",                 UINT16)
  ]

class EFI_ACPI_2_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Length",                UINT8),
    ("Flags",                 UINT16),
    ("GlobalSystemInterrupt", UINT32)
  ]

EFI_ACPI_2_0_LOCAL_APIC_NMI_STRUCTURE = EFI_ACPI_1_0_LOCAL_APIC_NMI_STRUCTURE

class EFI_ACPI_2_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",          UINT8),
    ("Length",        UINT8),
    ("Reserved",      UINT16),
    ("LocalApicLint", UINT64)
  ]

class EFI_ACPI_2_0_IO_SAPIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                      UINT8),
    ("Length",                    UINT8),
    ("IoApicId",                  UINT8),
    ("Reserved",                  UINT8),
    ("GlobalSystemInterruptBase", UINT32),
    ("IoSapicAddress",            UINT64)
  ]

class EFI_ACPI_2_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("AcpiProcessorId",   UINT8),
    ("LocalSapicId",      UINT8),
    ("LocalSapicEid",     UINT8),
    ("Reserved",          UINT8 * 3),
    ("Flags",             UINT32)
  ]

class EFI_ACPI_2_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Length",                UINT8),
    ("Flags",                 UINT16),
    ("InterruptType",         UINT8),
    ("ProcessorId",           UINT8),
    ("ProcessorEid",          UINT8),
    ("IoSapicVector",         UINT8),
    ("GlobalSystemInterrupt", UINT32),
    ("Reserved",              UINT32)
  ]

EFI_ACPI_2_0_SMART_BATTERY_DESCRIPTION_TABLE = EFI_ACPI_1_0_SMART_BATTERY_DESCRIPTION_TABLE

EFI_ACPI_2_0_SMART_BATTERY_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_2_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("EcControl", EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("EcData",    EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("Uid",       UINT32),
    ("GpeBit",    UINT8)
  ]

EFI_ACPI_2_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  = 0x01

EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = EFI_ACPI_1_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE
EFI_ACPI_2_0_MULTIPLE_SAPIC_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_1_0_APIC_SIGNATURE
EFI_ACPI_2_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  = SIGNATURE_32('B', 'O', 'O', 'T')
EFI_ACPI_2_0_DEBUG_PORT_TABLE_SIGNATURE  = SIGNATURE_32('D', 'B', 'G', 'P')
EFI_ACPI_2_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_1_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_2_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  = SIGNATURE_32('E', 'C', 'D', 'T')
EFI_ACPI_2_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'T', 'D', 'T')
EFI_ACPI_2_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = EFI_ACPI_1_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE
EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_1_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_2_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('A', 'P', 'I', 'C')
EFI_ACPI_2_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_1_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_1_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_2_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = EFI_ACPI_1_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE
EFI_ACPI_2_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'L', 'I', 'T')
EFI_ACPI_2_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'P', 'C', 'R')
EFI_ACPI_2_0_STATIC_RESOURCE_AFFINITY_TABLE_SIGNATURE  = SIGNATURE_32('S', 'R', 'A', 'T')
EFI_ACPI_2_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_1_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_2_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_SIGNATURE  = SIGNATURE_32('S', 'P', 'M', 'I')
EFI_ACPI_2_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('X', 'S', 'D', 'T')
EFI_ACPI_2_0_MEMORY_MAPPED_CONFIGURATION_BASE_ADDRESS_TABLE_SIGNATURE  = SIGNATURE_32('M', 'C', 'F', 'G')
