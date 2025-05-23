# Acpi65.py
#
# EfiPy2.MdePkg.IndustryStandard.Acpi65
#   part of EfiPy2
#
# Copyright (C) 2023 -2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.Acpi64 import *

EFI_ACPI_6_5_AML_PSD_REVISION  = 0

EFI_ACPI_6_5_AML_CPC_REVISION  = 3

EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE = EFI_ACPI_6_4_GENERIC_ADDRESS_STRUCTURE

EFI_ACPI_6_5_SYSTEM_MEMORY                           = 0x00
EFI_ACPI_6_5_SYSTEM_IO                               = 0x01
EFI_ACPI_6_5_PCI_CONFIGURATION_SPACE                 = 0x02
EFI_ACPI_6_5_EMBEDDED_CONTROLLER                     = 0x03
EFI_ACPI_6_5_SMBUS                                   = 0x04
EFI_ACPI_6_5_SYSTEM_CMOS                             = 0x05
EFI_ACPI_6_5_PCI_BAR_TARGET                          = 0x06
EFI_ACPI_6_5_IPMI                                    = 0x07
EFI_ACPI_6_5_GENERAL_PURPOSE_IO                      = 0x08
EFI_ACPI_6_5_GENERIC_SERIAL_BUS                      = 0x09
EFI_ACPI_6_5_PLATFORM_COMMUNICATION_CHANNEL          = 0x0A
EFI_ACPI_6_5_PLATFORM_RUNTIME_MECHANISM              = 0x0B
EFI_ACPI_6_5_FUNCTIONAL_FIXED_HARDWARE               = 0x7F

EFI_ACPI_6_5_UNDEFINED  = 0
EFI_ACPI_6_5_BYTE       = 1
EFI_ACPI_6_5_WORD       = 2
EFI_ACPI_6_5_DWORD      = 3
EFI_ACPI_6_5_QWORD      = 4

EFI_ACPI_6_5_ROOT_SYSTEM_DESCRIPTION_POINTER = EFI_ACPI_6_4_ROOT_SYSTEM_DESCRIPTION_POINTER

EFI_ACPI_6_5_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION = 0x02

EFI_ACPI_6_5_COMMON_HEADER = EFI_ACPI_6_4_COMMON_HEADER

EFI_ACPI_6_5_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_6_5_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_6_5_FIXED_ACPI_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
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
    ("ResetReg",            EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("ResetValue",          UINT8),
    ("ArmBootArch",         UINT16),
    ("MinorVersion",        UINT8),
    ("XFirmwareCtrl",       UINT64),
    ("XDsdt",               UINT64),
    ("XPm1aEvtBlk",         EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bEvtBlk",         EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1aCntBlk",         EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XPm1bCntBlk",         EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XPm2CntBlk",          EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XPmTmrBlk",           EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe0Blk",            EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("XGpe1Blk",            EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("SleepControlReg",     EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("SleepStatusReg",      EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("HypervisorVendorIdentity",  UINT64)
  ]

EFI_ACPI_6_5_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x06
EFI_ACPI_6_5_FIXED_ACPI_DESCRIPTION_TABLE_MINOR_REVISION  = 0x00

EFI_ACPI_6_5_PM_PROFILE_UNSPECIFIED         = 0
EFI_ACPI_6_5_PM_PROFILE_DESKTOP             = 1
EFI_ACPI_6_5_PM_PROFILE_MOBILE              = 2
EFI_ACPI_6_5_PM_PROFILE_WORKSTATION         = 3
EFI_ACPI_6_5_PM_PROFILE_ENTERPRISE_SERVER   = 4
EFI_ACPI_6_5_PM_PROFILE_SOHO_SERVER         = 5
EFI_ACPI_6_5_PM_PROFILE_APPLIANCE_PC        = 6
EFI_ACPI_6_5_PM_PROFILE_PERFORMANCE_SERVER  = 7
EFI_ACPI_6_5_PM_PROFILE_TABLET              = 8

EFI_ACPI_6_5_LEGACY_DEVICES              = BIT0
EFI_ACPI_6_5_8042                        = BIT1
EFI_ACPI_6_5_VGA_NOT_PRESENT             = BIT2
EFI_ACPI_6_5_MSI_NOT_SUPPORTED           = BIT3
EFI_ACPI_6_5_PCIE_ASPM_CONTROLS          = BIT4
EFI_ACPI_6_5_CMOS_RTC_NOT_PRESENT        = BIT5

EFI_ACPI_6_5_ARM_PSCI_COMPLIANT              = BIT0
EFI_ACPI_6_5_ARM_PSCI_USE_HVC                = BIT1

EFI_ACPI_6_5_WBINVD                                 = BIT0
EFI_ACPI_6_5_WBINVD_FLUSH                           = BIT1
EFI_ACPI_6_5_PROC_C1                                = BIT2
EFI_ACPI_6_5_P_LVL2_UP                              = BIT3
EFI_ACPI_6_5_PWR_BUTTON                             = BIT4
EFI_ACPI_6_5_SLP_BUTTON                             = BIT5
EFI_ACPI_6_5_FIX_RTC                                = BIT6
EFI_ACPI_6_5_RTC_S4                                 = BIT7
EFI_ACPI_6_5_TMR_VAL_EXT                            = BIT8
EFI_ACPI_6_5_DCK_CAP                                = BIT9
EFI_ACPI_6_5_RESET_REG_SUP                          = BIT10
EFI_ACPI_6_5_SEALED_CASE                            = BIT11
EFI_ACPI_6_5_HEADLESS                               = BIT12
EFI_ACPI_6_5_CPU_SW_SLP                             = BIT13
EFI_ACPI_6_5_PCI_EXP_WAK                            = BIT14
EFI_ACPI_6_5_USE_PLATFORM_CLOCK                     = BIT15
EFI_ACPI_6_5_S4_RTC_STS_VALID                       = BIT16
EFI_ACPI_6_5_REMOTE_POWER_ON_CAPABLE                = BIT17
EFI_ACPI_6_5_FORCE_APIC_CLUSTER_MODEL               = BIT18
EFI_ACPI_6_5_FORCE_APIC_PHYSICAL_DESTINATION_MODE   = BIT19
EFI_ACPI_6_5_HW_REDUCED_ACPI                        = BIT20
EFI_ACPI_6_5_LOW_POWER_S0_IDLE_CAPABLE              = BIT21

EFI_ACPI_6_5_FIRMWARE_ACPI_CONTROL_STRUCTURE = EFI_ACPI_6_4_FIRMWARE_ACPI_CONTROL_STRUCTURE

EFI_ACPI_6_5_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  = 0x02

EFI_ACPI_6_5_S4BIOS_F                     = BIT0
EFI_ACPI_6_5_64BIT_WAKE_SUPPORTED_F       = BIT1

EFI_ACPI_6_5_OSPM_64BIT_WAKE_F            = BIT0

EFI_ACPI_6_5_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_REVISION   = 0x02
EFI_ACPI_6_5_SECONDARY_SYSTEM_DESCRIPTION_TABLE_REVISION        = 0x02

EFI_ACPI_6_5_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER = EFI_ACPI_6_4_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER

EFI_ACPI_6_5_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x06

EFI_ACPI_6_5_PCAT_COMPAT         = BIT0

EFI_ACPI_6_5_PROCESSOR_LOCAL_APIC           = 0x00
EFI_ACPI_6_5_IO_APIC                        = 0x01
EFI_ACPI_6_5_INTERRUPT_SOURCE_OVERRIDE      = 0x02
EFI_ACPI_6_5_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
EFI_ACPI_6_5_LOCAL_APIC_NMI                 = 0x04
EFI_ACPI_6_5_LOCAL_APIC_ADDRESS_OVERRIDE    = 0x05
EFI_ACPI_6_5_IO_SAPIC                       = 0x06
EFI_ACPI_6_5_LOCAL_SAPIC                    = 0x07
EFI_ACPI_6_5_PLATFORM_INTERRUPT_SOURCES     = 0x08
EFI_ACPI_6_5_PROCESSOR_LOCAL_X2APIC         = 0x09
EFI_ACPI_6_5_LOCAL_X2APIC_NMI               = 0x0A
EFI_ACPI_6_5_GIC                            = 0x0B
EFI_ACPI_6_5_GICD                           = 0x0C
EFI_ACPI_6_5_GIC_MSI_FRAME                  = 0x0D
EFI_ACPI_6_5_GICR                           = 0x0E
EFI_ACPI_6_5_GIC_ITS                        = 0x0F
EFI_ACPI_6_5_MULTIPROCESSOR_WAKEUP          = 0x10
EFI_ACPI_6_5_CORE_PIC                       = 0x11
EFI_ACPI_6_5_LIO_PIC                        = 0x12
EFI_ACPI_6_5_HT_PIC                         = 0x13
EFI_ACPI_6_5_EIO_PIC                        = 0x14
EFI_ACPI_6_5_MSI_PIC                        = 0x15
EFI_ACPI_6_5_BIO_PIC                        = 0x16
EFI_ACPI_6_5_LPC_PIC                        = 0x17

class EFI_ACPI_6_5_PROCESSOR_LOCAL_APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("AcpiProcessorUid",  UINT8),
    ("ApicId",            UINT8),
    ("Flags",             UINT32)
  ]

EFI_ACPI_6_5_LOCAL_APIC_ENABLED        = BIT0

EFI_ACPI_6_5_IO_APIC_STRUCTURE = EFI_ACPI_6_4_IO_APIC_STRUCTURE

EFI_ACPI_6_5_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE = EFI_ACPI_6_4_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE

EFI_ACPI_6_5_PLATFORM_INTERRUPT_APIC_STRUCTURE = EFI_ACPI_6_4_PLATFORM_INTERRUPT_APIC_STRUCTURE

EFI_ACPI_6_5_POLARITY      = (3 << 0)
EFI_ACPI_6_5_TRIGGER_MODE  = (3 << 2)

EFI_ACPI_6_5_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE = EFI_ACPI_6_4_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE

class EFI_ACPI_6_5_LOCAL_APIC_NMI_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("AcpiProcessorUid",  UINT8),
    ("Flags",             UINT16),
    ("LocalApicLint",     UINT8)
  ]

EFI_ACPI_6_5_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE = EFI_ACPI_6_4_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE

EFI_ACPI_6_5_IO_SAPIC_STRUCTURE = EFI_ACPI_6_4_IO_SAPIC_STRUCTURE

EFI_ACPI_6_5_PROCESSOR_LOCAL_SAPIC_STRUCTURE = EFI_ACPI_6_4_PROCESSOR_LOCAL_SAPIC_STRUCTURE

EFI_ACPI_6_5_PLATFORM_INTERRUPT_SOURCES_STRUCTURE = EFI_ACPI_6_4_PLATFORM_INTERRUPT_SOURCES_STRUCTURE

EFI_ACPI_6_5_CPEI_PROCESSOR_OVERRIDE          = BIT0

EFI_ACPI_6_5_PROCESSOR_LOCAL_X2APIC_STRUCTURE = EFI_ACPI_6_4_PROCESSOR_LOCAL_X2APIC_STRUCTURE

EFI_ACPI_6_5_LOCAL_X2APIC_NMI_STRUCTURE = EFI_ACPI_6_4_LOCAL_X2APIC_NMI_STRUCTURE

class EFI_ACPI_6_5_GIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT8),
    ("Length",                        UINT8),
    ("Reserved",                      UINT16),
    ("CPUInterfaceNumber",            UINT32),
    ("AcpiProcessorUid",              UINT32),
    ("Flags",                         UINT32),
    ("ParkingProtocolVersion",        UINT32),
    ("PerformanceInterruptGsiv",      UINT32),
    ("ParkedAddress",                 UINT64),
    ("PhysicalBaseAddress",           UINT64),
    ("GICV",                          UINT64),
    ("GICH",                          UINT64),
    ("VGICMaintenanceInterrupt",      UINT32),
    ("GICRBaseAddress",               UINT64),
    ("MPIDR",                         UINT64),
    ("ProcessorPowerEfficiencyClass", UINT8),
    ("Reserved2",                     UINT8),
    ("SpeOverflowInterrupt",          UINT16),
    ("TrbeInterrupt",                 UINT16)
  ]

EFI_ACPI_6_5_GIC_ENABLED                              = BIT0
EFI_ACPI_6_5_PERFORMANCE_INTERRUPT_MODEL              = BIT1
EFI_ACPI_6_5_VGIC_MAINTENANCE_INTERRUPT_MODE_FLAGS    = BIT2
EFI_ACPI_6_5_GIC_ONLINE_CAPABLE                       = BIT3

EFI_ACPI_6_5_GIC_DISTRIBUTOR_STRUCTURE = EFI_ACPI_6_4_GIC_DISTRIBUTOR_STRUCTURE

EFI_ACPI_6_5_GIC_V1  = 0x01
EFI_ACPI_6_5_GIC_V2  = 0x02
EFI_ACPI_6_5_GIC_V3  = 0x03
EFI_ACPI_6_5_GIC_V4  = 0x04

EFI_ACPI_6_5_GIC_MSI_FRAME_STRUCTURE = EFI_ACPI_6_4_GIC_MSI_FRAME_STRUCTURE

EFI_ACPI_6_5_SPI_COUNT_BASE_SELECT                    = BIT0

EFI_ACPI_6_5_GICR_STRUCTURE = EFI_ACPI_6_4_GICR_STRUCTURE

class EFI_ACPI_6_5_GIC_ITS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                UINT8),
    ("Length",              UINT8),
    ("Reserved",            UINT16),
    ("GicItsId",            UINT32),
    ("PhysicalBaseAddress", UINT64),
    ("Reserved2",           UINT32)
  ]

class EFI_ACPI_6_5_MULTIPROCESSOR_WAKEUP_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                UINT8),
    ("Length",              UINT8),
    ("MailBoxVersion",      UINT16),
    ("Reserved",            UINT32),
    ("MailBoxAddress",      UINT64)
  ]

class EFI_ACPI_6_5_MULTIPROCESSOR_WAKEUP_MAILBOX_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Command",                 UINT16),
    ("Reserved",                UINT16),
    ("AcpiId",                  UINT32),
    ("WakeupVector",            UINT64),
    ("ReservedForOs",           UINT8 * 2032),
    ("ReservedForFirmware",     UINT8 * 2048)
  ]

EFI_ACPI_6_5_MULTIPROCESSOR_WAKEUP_MAILBOX_COMMAND_NOOP    = 0x0000
EFI_ACPI_6_5_MULTIPROCESSOR_WAKEUP_MAILBOX_COMMAND_WAKEUP  = 0x0001

class EFI_ACPI_6_5_CORE_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("ProcessorId",     UINT32),
    ("CoreId",          UINT32),
    ("Flags",           UINT32)
  ]

class EFI_ACPI_6_5_LIO_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("Address",         UINT64),
    ("Size",            UINT16),
    ("Cascade",         UINT8 * 2),
    ("CascadeMap",      UINT32 * 2)
  ]

class EFI_ACPI_6_5_HT_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("Address",         UINT64),
    ("Size",            UINT16),
    ("Cascade",         UINT8 * 8)
  ]

class EFI_ACPI_6_5_EIO_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("Cascade",         UINT8),
    ("Node",            UINT8),
    ("NodeMap",         UINT64)
  ]

class EFI_ACPI_6_5_MSI_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("MsgAddress",      UINT64),
    ("Start",           UINT32),
    ("Count",           UINT32)
  ]

class EFI_ACPI_6_5_BIO_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("Address",         UINT64),
    ("Size",            UINT16),
    ("Id",              UINT16),
    ("GsiBase",         UINT16)
  ]

class EFI_ACPI_6_5_LPC_PIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Version",         UINT8),
    ("Address",         UINT64),
    ("Size",            UINT16),
    ("Cascade",         UINT8)
  ]

EFI_ACPI_6_5_SMART_BATTERY_DESCRIPTION_TABLE = EFI_ACPI_6_4_SMART_BATTERY_DESCRIPTION_TABLE

EFI_ACPI_6_5_SMART_BATTERY_DESCRIPTION_TABLE_REVISION = 0x01

class EFI_ACPI_6_5_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          EFI_ACPI_DESCRIPTION_HEADER),
    ("EcControl",       EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("EcData",          EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("Uid",             UINT32),
    ("GpeBit",          UINT8)
  ]

EFI_ACPI_6_5_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  = EFI_ACPI_6_4_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION

EFI_ACPI_6_5_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER = EFI_ACPI_6_4_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER

EFI_ACPI_6_5_SYSTEM_RESOURCE_AFFINITY_TABLE_REVISION  = 0x03

EFI_ACPI_6_5_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY  = 0x00
EFI_ACPI_6_5_MEMORY_AFFINITY                      = 0x01
EFI_ACPI_6_5_PROCESSOR_LOCAL_X2APIC_AFFINITY      = 0x02
EFI_ACPI_6_5_GICC_AFFINITY                        = 0x03
EFI_ACPI_6_5_GIC_ITS_AFFINITY                     = 0x04

EFI_ACPI_6_5_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE = EFI_ACPI_6_4_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE

EFI_ACPI_6_5_PROCESSOR_LOCAL_APIC_SAPIC_ENABLED = (1 << 0)

EFI_ACPI_6_5_MEMORY_AFFINITY_STRUCTURE = EFI_ACPI_6_4_MEMORY_AFFINITY_STRUCTURE

EFI_ACPI_6_5_MEMORY_ENABLED       = (1 << 0)
EFI_ACPI_6_5_MEMORY_HOT_PLUGGABLE = (1 << 1)
EFI_ACPI_6_5_MEMORY_NONVOLATILE   = (1 << 2)

EFI_ACPI_6_5_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE = EFI_ACPI_6_4_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE

EFI_ACPI_6_5_GICC_AFFINITY_STRUCTURE = EFI_ACPI_6_4_GICC_AFFINITY_STRUCTURE
EFI_ACPI_6_5_GICC_ENABLED = (1 << 0)

class EFI_ACPI_6_5_GIC_ITS_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                UINT8),
    ("Length",              UINT8),
    ("ProximityDomain",     UINT32),
    ("Reserved",            UINT8),
    ("ItsId",               UINT32),
  ]

EFI_ACPI_6_5_ACPI_DEVICE_HANDLE  = 0x00
EFI_ACPI_6_5_PCI_DEVICE_HANDLE   = 0x01

class EFI_ACPI_6_5_DEVICE_HANDLE_ACPI (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AcpiHid",     UINT64),
    ("AcpiUid",     UINT32),
    ("Reserved",    UINT8 * 4)
  ]

class EFI_ACPI_6_5_DEVICE_HANDLE_PCI (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PciSegment",      UINT16),
    ("PciBdfNumber",    UINT16),
    ("Reserved",        UINT8 * 12)
  ]

class EFI_ACPI_6_5_DEVICE_HANDLE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Acpi",    EFI_ACPI_6_5_DEVICE_HANDLE_ACPI),
    ("Pci",     EFI_ACPI_6_5_DEVICE_HANDLE_PCI)
  ]

class EFI_ACPI_6_5_GENERIC_INITIATOR_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                UINT8),
    ("Length",              UINT8),
    ("Reserved1",           UINT8),
    ("DeviceHandleType",    UINT8),
    ("ProximityDomain",     UINT32),
    ("DeviceHandle",        EFI_ACPI_6_5_DEVICE_HANDLE),
    ("Flags",               UINT32),
    ("Reserved2",           UINT8 * 4),
  ]

EFI_ACPI_6_5_GENERIC_INITIATOR_AFFINITY_STRUCTURE_ENABLED                     = BIT0
EFI_ACPI_6_5_GENERIC_INITIATOR_AFFINITY_STRUCTURE_ARCHITECTURAL_TRANSACTIONS  = BIT1

EFI_ACPI_6_5_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER = EFI_ACPI_6_4_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER

EFI_ACPI_6_5_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_REVISION  = 0x01

EFI_ACPI_6_5_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER = EFI_ACPI_6_4_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER

EFI_ACPI_6_5_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_REVISION = 0x01

EFI_ACPI_6_5_CPEP_PROCESSOR_APIC_SAPIC  = 0x00

EFI_ACPI_6_5_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE = EFI_ACPI_6_4_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE

EFI_ACPI_6_5_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER = EFI_ACPI_6_4_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER

EFI_ACPI_6_5_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_REVISION = 0x01

EFI_ACPI_6_5_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE = EFI_ACPI_6_4_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE

EFI_ACPI_6_5_RAS_FEATURE_TABLE = EFI_ACPI_6_4_RAS_FEATURE_TABLE

EFI_ACPI_6_5_RAS_FEATURE_TABLE_REVISION = 0x01

EFI_ACPI_6_5_RASF_PLATFORM_COMMUNICATION_CHANNEL_SHARED_MEMORY_REGION = EFI_ACPI_6_4_RASF_PLATFORM_COMMUNICATION_CHANNEL_SHARED_MEMORY_REGION

EFI_ACPI_6_5_RASF_PCC_COMMAND_CODE_EXECUTE_RASF_COMMAND  = 0x01

EFI_ACPI_6_5_RASF_PLATFORM_RAS_CAPABILITY_HARDWARE_BASED_PATROL_SCRUB_SUPPOTED                          = 0x01
EFI_ACPI_6_5_RASF_PLATFORM_RAS_CAPABILITY_HARDWARE_BASED_PATROL_SCRUB_SUPPOTED_AND_EXPOSED_TO_SOFTWARE  = 0x02
EFI_ACPI_6_5_RASF_PLATFORM_RAS_CAPABILITY_CPU_CACHE_FLUSH_TO_NVDIMM_DURABILITY_ON_POWER_LOSS            = BIT2
EFI_ACPI_6_5_RASF_PLATFORM_RAS_CAPABILITY_MEMORY_CONTROLLER_FLUSH_TO_NVDIMM_DURABILITY_ON_POWER_LOSS    = BIT3
EFI_ACPI_6_5_RASF_PLATFORM_RAS_CAPABILITY_BYTE_ADDRESSABLE_PERSISTENT_MEMORY_HARDWARE_MIRRORING         = BIT4

EFI_ACPI_6_5_RASF_PATROL_SCRUB_PLATFORM_BLOCK_STRUCTURE = EFI_ACPI_6_4_RASF_PATROL_SCRUB_PLATFORM_BLOCK_STRUCTURE

EFI_ACPI_6_5_RASF_PATROL_SCRUB_COMMAND_GET_PATROL_PARAMETERS   = 0x01
EFI_ACPI_6_5_RASF_PATROL_SCRUB_COMMAND_START_PATROL_SCRUBBER   = 0x02
EFI_ACPI_6_5_RASF_PATROL_SCRUB_COMMAND_STOP_PATROL_SCRUBBER    = 0x03

class EFI_ACPI_RAS2_PCC_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PccId",           UINT8),
    ("Reserved",        UINT8 * 2),
    ("RasFeatureType",  UINT8),
    ("Instance",        UINT32)
  ]

class EFI_ACPI_6_5_RAS2_FEATURE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",    UINT16),
    ("PccCount",    UINT16),
    # ("Descriptors", EFI_ACPI_RAS2_PCC_DESCRIPTOR * PccCount)
  ]

EFI_ACPI_6_5_MEMORY_POWER_STATUS_TABLE = EFI_ACPI_6_4_MEMORY_POWER_STATUS_TABLE

EFI_ACPI_6_5_MEMORY_POWER_STATE_TABLE_REVISION = 0x01

EFI_ACPI_6_5_MPST_PLATFORM_COMMUNICATION_CHANNEL_SHARED_MEMORY_REGION = EFI_ACPI_6_4_MPST_PLATFORM_COMMUNICATION_CHANNEL_SHARED_MEMORY_REGION

EFI_ACPI_6_5_MPST_PCC_COMMAND_CODE_EXECUTE_MPST_COMMAND  = 0x03

EFI_ACPI_6_5_MPST_MEMORY_POWER_COMMAND_GET_MEMORY_POWER_STATE       = 0x01
EFI_ACPI_6_5_MPST_MEMORY_POWER_COMMAND_SET_MEMORY_POWER_STATE       = 0x02
EFI_ACPI_6_5_MPST_MEMORY_POWER_COMMAND_GET_AVERAGE_POWER_CONSUMED   = 0x03
EFI_ACPI_6_5_MPST_MEMORY_POWER_COMMAND_GET_MEMORY_ENERGY_CONSUMED   = 0x04

EFI_ACPI_6_5_MPST_MEMORY_POWER_STATE = EFI_ACPI_6_4_MPST_MEMORY_POWER_STATE

EFI_ACPI_6_5_MPST_MEMORY_POWER_STRUCTURE = EFI_ACPI_6_4_MPST_MEMORY_POWER_STRUCTURE

EFI_ACPI_6_5_MPST_MEMORY_POWER_STRUCTURE_FLAG_ENABLE          = 0x01
EFI_ACPI_6_5_MPST_MEMORY_POWER_STRUCTURE_FLAG_POWER_MANAGED   = 0x02
EFI_ACPI_6_5_MPST_MEMORY_POWER_STRUCTURE_FLAG_HOT_PLUGGABLE   = 0x04

EFI_ACPI_6_5_MPST_MEMORY_POWER_NODE_TABLE = EFI_ACPI_6_4_MPST_MEMORY_POWER_NODE_TABLE

EFI_ACPI_6_5_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE = EFI_ACPI_6_4_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE

EFI_ACPI_6_5_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE_FLAG_MEMORY_CONTENT_PRESERVED              = 0x01
EFI_ACPI_6_5_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE_FLAG_AUTONOMOUS_MEMORY_POWER_STATE_ENTRY   = 0x02
EFI_ACPI_6_5_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_STRUCTURE_FLAG_AUTONOMOUS_MEMORY_POWER_STATE_EXIT    = 0x04

EFI_ACPI_6_5_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_TABLE = EFI_ACPI_6_4_MPST_MEMORY_POWER_STATE_CHARACTERISTICS_TABLE

class EFI_ACPI_6_5_PLATFORM_MEMORY_TOPOLOGY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("NumberOfMemoryDevices",   UINT32)
    # ("MemoryDeviceStructure",   EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE * NumberOfMemoryDevices)
  ]

EFI_ACPI_6_5_MEMORY_TOPOLOGY_TABLE_REVISION = 0x01

class EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                    UINT8),
    ("Reserved",                UINT8),
    ("Length",                  UINT16),
    ("Flags",                   UINT16),
    ("Reserved1",               UINT16),
    ("NumberOfMemoryDevices",   UINT32)
    # ("TypeSpecificData",          UINT8 * N)
    # ("MemoryDeviceStructure",     EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE * NumberOfMemoryDevices)
  ]

EFI_ACPI_6_5_PMTT_MEMORY_DEVICE_TYPE_SOCKET                = 0x0
EFI_ACPI_6_5_PMTT_MEMORY_DEVICE_TYPE_MEMORY_CONTROLLER     = 0x1
EFI_ACPI_6_5_PMTT_MEMORY_DEVICE_TYPE_DIMM                  = 0x2
EFI_ACPI_6_5_PMTT_MEMORY_DEVICE_TYPE_VENDOR_SPECIFIC_TYPE  = 0xFF

class EFI_ACPI_6_5_PMTT_SOCKET_TYPE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommonMemoryDeviceHeader",        EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE),
    ("SocketIdentifier",                UINT16),
    ("Reserved",                        UINT16),
    # ("MemoryDeviceStructure",     EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE * N)
  ]

class EFI_ACPI_6_5_PMTT_MEMORY_CONTROLLER_TYPE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommonMemoryDeviceHeader",        EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE),
    ("MemoryControllerIdentifier",      UINT16),
    ("Reserved",                        UINT16),
    # ("MemoryDeviceStructure",     EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE * N)
  ]

class EFI_ACPI_6_5_PMTT_DIMM_TYPE_SPECIFIC_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommonMemoryDeviceHeader",        EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE),
    ("SmbiosHandle",                    UINT32)
  ]

class EFI_ACPI_6_5_PMTT_VENDOR_SPECIFIC_TYPE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommonMemoryDeviceHeader",    EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE),
    ("TypeUuid",                    UINT8 * 16)
    # ("VendorSpecificData",          EFI_ACPI_6_5_PMTT_VENDOR_SPECIFIC_TYPE_DATA * N)
    # ("MemoryDeviceStructure",       EFI_ACPI_6_5_PMTT_COMMON_MEMORY_DEVICE * N)
  ]

EFI_ACPI_6_5_BOOT_GRAPHICS_RESOURCE_TABLE = EFI_ACPI_6_4_BOOT_GRAPHICS_RESOURCE_TABLE

EFI_ACPI_6_5_BOOT_GRAPHICS_RESOURCE_TABLE_REVISION = 1

EFI_ACPI_6_5_BGRT_VERSION         = 0x01

EFI_ACPI_6_5_BGRT_STATUS_NOT_DISPLAYED = 0x00
EFI_ACPI_6_5_BGRT_STATUS_DISPLAYED     = 0x01

EFI_ACPI_6_5_BGRT_IMAGE_TYPE_BMP  = 0x00

EFI_ACPI_6_5_FIRMWARE_PERFORMANCE_DATA_TABLE_REVISION = 0x01

EFI_ACPI_6_5_FPDT_RECORD_TYPE_FIRMWARE_BASIC_BOOT_POINTER      = 0x0000
EFI_ACPI_6_5_FPDT_RECORD_TYPE_S3_PERFORMANCE_TABLE_POINTER     = 0x0001

EFI_ACPI_6_5_FPDT_RECORD_REVISION_FIRMWARE_BASIC_BOOT_POINTER  = 0x01
EFI_ACPI_6_5_FPDT_RECORD_REVISION_S3_PERFORMANCE_TABLE_POINTER = 0x01

EFI_ACPI_6_5_FPDT_RUNTIME_RECORD_TYPE_S3_RESUME                = 0x0000
EFI_ACPI_6_5_FPDT_RUNTIME_RECORD_TYPE_S3_SUSPEND               = 0x0001
EFI_ACPI_6_5_FPDT_RUNTIME_RECORD_TYPE_FIRMWARE_BASIC_BOOT      = 0x0002

EFI_ACPI_6_5_FPDT_RUNTIME_RECORD_REVISION_S3_RESUME            = 0x01
EFI_ACPI_6_5_FPDT_RUNTIME_RECORD_REVISION_S3_SUSPEND           = 0x01
EFI_ACPI_6_5_FPDT_RUNTIME_RECORD_REVISION_FIRMWARE_BASIC_BOOT  = 0x02

EFI_ACPI_6_5_FPDT_PERFORMANCE_RECORD_HEADER = EFI_ACPI_6_4_FPDT_PERFORMANCE_RECORD_HEADER

EFI_ACPI_6_5_FPDT_PERFORMANCE_TABLE_HEADER = EFI_ACPI_6_4_FPDT_PERFORMANCE_TABLE_HEADER

EFI_ACPI_6_5_FPDT_BOOT_PERFORMANCE_TABLE_POINTER_RECORD = EFI_ACPI_6_4_FPDT_BOOT_PERFORMANCE_TABLE_POINTER_RECORD

EFI_ACPI_6_5_FPDT_S3_PERFORMANCE_TABLE_POINTER_RECORD = EFI_ACPI_6_4_FPDT_S3_PERFORMANCE_TABLE_POINTER_RECORD

EFI_ACPI_6_5_FPDT_FIRMWARE_BASIC_BOOT_RECORD = EFI_ACPI_6_4_FPDT_FIRMWARE_BASIC_BOOT_RECORD

EFI_ACPI_6_5_FPDT_BOOT_PERFORMANCE_TABLE_SIGNATURE  = SIGNATURE_32('F', 'B', 'P', 'T')
EFI_ACPI_6_5_FPDT_FIRMWARE_BASIC_BOOT_TABLE = EFI_ACPI_6_4_FPDT_FIRMWARE_BASIC_BOOT_TABLE

EFI_ACPI_6_5_FPDT_S3_PERFORMANCE_TABLE_SIGNATURE  = SIGNATURE_32('S', '3', 'P', 'T')
EFI_ACPI_6_5_FPDT_FIRMWARE_S3_BOOT_TABLE = EFI_ACPI_6_4_FPDT_FIRMWARE_S3_BOOT_TABLE

EFI_ACPI_6_5_FPDT_S3_RESUME_RECORD = EFI_ACPI_6_4_FPDT_S3_RESUME_RECORD

EFI_ACPI_6_5_FPDT_S3_SUSPEND_RECORD = EFI_ACPI_6_4_FPDT_S3_SUSPEND_RECORD

EFI_ACPI_6_5_FIRMWARE_PERFORMANCE_RECORD_TABLE = EFI_ACPI_6_4_FIRMWARE_PERFORMANCE_RECORD_TABLE

class EFI_ACPI_6_5_GENERIC_TIMER_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CntControlBasePhysicalAddress", UINT64),
    ("Reserved",                      UINT32),
    ("SecurePL1TimerGSIV",            UINT32),
    ("SecurePL1TimerFlags",           UINT32),
    ("NonSecurePL1TimerGSIV",         UINT32),
    ("NonSecurePL1TimerFlags",        UINT32),
    ("VirtualTimerGSIV",              UINT32),
    ("VirtualTimerFlags",             UINT32),
    ("NonSecurePL2TimerGSIV",         UINT32),
    ("NonSecurePL2TimerFlags",        UINT32),
    ("CntReadBasePhysicalAddress",    UINT64),
    ("PlatformTimerCount",            UINT32),
    ("PlatformTimerOffset",           UINT32),
    ("VirtualPL2TimerGSIV",           UINT32),
    ("VirtualPL2TimerFlags",          UINT32)
  ]

EFI_ACPI_6_5_GENERIC_TIMER_DESCRIPTION_TABLE_REVISION  = 0x02
EFI_ACPI_6_5_GTDT_TIMER_FLAG_TIMER_INTERRUPT_MODE          = BIT0
EFI_ACPI_6_5_GTDT_TIMER_FLAG_TIMER_INTERRUPT_POLARITY      = BIT1
EFI_ACPI_6_5_GTDT_TIMER_FLAG_ALWAYS_ON_CAPABILITY          = BIT2

EFI_ACPI_6_5_GTDT_GT_BLOCK                       = 0
EFI_ACPI_6_5_GTDT_ARM_GENERIC_WATCHDOG           = 1

EFI_ACPI_6_5_GTDT_GT_BLOCK_STRUCTURE = EFI_ACPI_6_4_GTDT_GT_BLOCK_STRUCTURE

EFI_ACPI_6_5_GTDT_GT_BLOCK_TIMER_STRUCTURE = EFI_ACPI_6_4_GTDT_GT_BLOCK_TIMER_STRUCTURE

EFI_ACPI_6_5_GTDT_GT_BLOCK_TIMER_FLAG_TIMER_INTERRUPT_MODE          = BIT0
EFI_ACPI_6_5_GTDT_GT_BLOCK_TIMER_FLAG_TIMER_INTERRUPT_POLARITY      = BIT1

EFI_ACPI_6_5_GTDT_GT_BLOCK_COMMON_FLAG_SECURE_TIMER              = BIT0
EFI_ACPI_6_5_GTDT_GT_BLOCK_COMMON_FLAG_ALWAYS_ON_CAPABILITY      = BIT1

EFI_ACPI_6_5_GTDT_SBSA_GENERIC_WATCHDOG_STRUCTURE = EFI_ACPI_6_4_GTDT_SBSA_GENERIC_WATCHDOG_STRUCTURE

EFI_ACPI_6_5_GTDT_SBSA_GENERIC_WATCHDOG_FLAG_TIMER_INTERRUPT_MODE          = BIT0
EFI_ACPI_6_5_GTDT_SBSA_GENERIC_WATCHDOG_FLAG_TIMER_INTERRUPT_POLARITY      = BIT1
EFI_ACPI_6_5_GTDT_SBSA_GENERIC_WATCHDOG_FLAG_SECURE_TIMER                  = BIT2

class EFI_ACPI_6_5_NVDIMM_FIRMWARE_INTERFACE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    UINT8),
    ("Reserved",  UINT8)
  ]

EFI_ACPI_6_5_NVDIMM_FIRMWARE_INTERFACE_TABLE_REVISION = 0x1

EFI_ACPI_6_5_NFIT_SYSTEM_PHYSICAL_ADDRESS_RANGE_STRUCTURE_TYPE              = 0
EFI_ACPI_6_5_NFIT_NVDIMM_REGION_MAPPING_STRUCTURE_TYPE                      = 1
EFI_ACPI_6_5_NFIT_INTERLEAVE_STRUCTURE_TYPE                                 = 2
EFI_ACPI_6_5_NFIT_SMBIOS_MANAGEMENT_INFORMATION_STRUCTURE_TYPE              = 3
EFI_ACPI_6_5_NFIT_NVDIMM_CONTROL_REGION_STRUCTURE_TYPE                      = 4
EFI_ACPI_6_5_NFIT_NVDIMM_BLOCK_DATA_WINDOW_REGION_STRUCTURE_TYPE            = 5
EFI_ACPI_6_5_NFIT_FLUSH_HINT_ADDRESS_STRUCTURE_TYPE                         = 6
EFI_ACPI_6_5_NFIT_PLATFORM_CAPABILITIES_STRUCTURE_TYPE                      = 7

class EFI_ACPI_6_5_NFIT_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT16),
    ("Length",  UINT16)
  ]

EFI_ACPI_6_5_NFIT_SYSTEM_PHYSICAL_ADDRESS_RANGE_FLAGS_CONTROL_REGION_FOR_MANAGEMENT      = BIT0
EFI_ACPI_6_5_NFIT_SYSTEM_PHYSICAL_ADDRESS_RANGE_FLAGS_PROXIMITY_DOMAIN_VALID             = BIT1

EFI_ACPI_6_5_NFIT_SYSTEM_PHYSICAL_ADDRESS_RANGE_FLAGS_SPA_LOCATION_COOKIE_VALID      = BIT2

EFI_ACPI_6_5_NFIT_GUID_VOLATILE_MEMORY_REGION                             = EFI_GUID (0x7305944F, 0xFDDA, 0x44E3, (0xB1, 0x6C, 0x3F, 0x22, 0xD2, 0x52, 0xE5, 0xD0))
EFI_ACPI_6_5_NFIT_GUID_BYTE_ADDRESSABLE_PERSISTENT_MEMORY_REGION          = EFI_GUID ( 0x66F0D379, 0xB4F3, 0x4074, (0xAC, 0x43, 0x0D, 0x33, 0x18, 0xB7, 0x8C, 0xDB ))
EFI_ACPI_6_5_NFIT_GUID_NVDIMM_CONTROL_REGION                              = EFI_GUID ( 0x92F701F6, 0x13B4, 0x405D, (0x91, 0x0B, 0x29, 0x93, 0x67, 0xE8, 0x23, 0x4C ))
EFI_ACPI_6_5_NFIT_GUID_NVDIMM_BLOCK_DATA_WINDOW_REGION                    = EFI_GUID ( 0x91AF0530, 0x5D86, 0x470E, (0xA6, 0xB0, 0x0A, 0x2D, 0xB9, 0x40, 0x82, 0x49 ))
EFI_ACPI_6_5_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_DISK_REGION_VOLATILE   = EFI_GUID ( 0x77AB535A, 0x45FC, 0x624B, (0x55, 0x60, 0xF7, 0xB2, 0x81, 0xD1, 0xF9, 0x6E ))
EFI_ACPI_6_5_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_CD_REGION_VOLATILE     = EFI_GUID ( 0x3D5ABD30, 0x4175, 0x87CE, (0x6D, 0x64, 0xD2, 0xAD, 0xE5, 0x23, 0xC4, 0xBB ))
EFI_ACPI_6_5_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_DISK_REGION_PERSISTENT = EFI_GUID ( 0x5CEA02C9, 0x4D07, 0x69D3, (0x26, 0x9F ,0x44, 0x96, 0xFB, 0xE0, 0x96, 0xF9 ))
EFI_ACPI_6_5_NFIT_GUID_RAM_DISK_SUPPORTING_VIRTUAL_CD_REGION_PERSISTENT   = EFI_GUID ( 0x08018188, 0x42CD, 0xBB48, (0x10, 0x0F, 0x53, 0x87, 0xD5, 0x3D, 0xED, 0x3D ))

class EFI_ACPI_6_5_NFIT_SYSTEM_PHYSICAL_ADDRESS_RANGE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("Length",                              UINT16),
    ("SPARangeStructureIndex",              UINT16),
    ("Flags",                               UINT16),
    ("Reserved_8",                          UINT32),
    ("ProximityDomain",                     UINT32),
    ("AddressRangeTypeGUID",                GUID),
    ("SystemPhysicalAddressRangeBase",      UINT64),
    ("SystemPhysicalAddressRangeLength",    UINT64),
    ("AddressRangeMemoryMappingAttribute",  UINT64),
    ("SPALocationCookie",                   UINT64)
  ]

class EFI_ACPI_6_5_NFIT_DEVICE_HANDLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DIMMNumber",          UINT32, 4),
    ("MemoryChannelNumber", UINT32, 4),
    ("MemoryControllerID",  UINT32, 4),
    ("SocketID",            UINT32, 4),
    ("NodeControllerID",    UINT32, 12),
    ("Reserved_28",         UINT32, 4)
  ]

EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_PREVIOUS_SAVE_FAIL                                      = BIT0
EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_LAST_RESTORE_FAIL                                       = BIT1
EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_PLATFORM_FLUSH_FAIL                                     = BIT2
EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_NOT_ARMED_PRIOR_TO_OSPM_HAND_OFF                        = BIT3
EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_SMART_HEALTH_EVENTS_PRIOR_OSPM_HAND_OFF                 = BIT4
EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_FIRMWARE_ENABLED_TO_NOTIFY_OSPM_ON_SMART_HEALTH_EVENTS  = BIT5
EFI_ACPI_6_5_NFIT_MEMORY_DEVICE_STATE_FLAGS_FIRMWARE_NOT_MAP_NVDIMM_TO_SPA                          = BIT6

class EFI_ACPI_6_5_NFIT_NVDIMM_REGION_MAPPING_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                    UINT16),
    ("Length",                                  UINT16),
    ("NFITDeviceHandle",                        EFI_ACPI_6_5_NFIT_DEVICE_HANDLE),
    ("NVDIMMPhysicalID",                        UINT16),
    ("NVDIMMRegionID",                          UINT16),
    ("SPARangeStructureIndex",                  UINT16),
    ("NVDIMMControlRegionStructureIndex",       UINT16),
    ("NVDIMMRegionSize",                        UINT64),
    ("RegionOffset",                            UINT64),
    ("NVDIMMPhysicalAddressRegionBase",         UINT64),
    ("InterleaveStructureIndex",                UINT16),
    ("InterleaveWays",                          UINT16),
    ("NVDIMMStateFlags",                        UINT16),
    ("Reserved_46",                             UINT16)
  ]

class EFI_ACPI_6_5_NFIT_INTERLEAVE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                      UINT16),
    ("Length",                    UINT16),
    ("InterleaveStructureIndex",  UINT16),
    ("Reserved_6",                UINT16),
    ("NumberOfLines",             UINT32),
    ("LineSize",                  UINT32),
    # ("LineOffset",              UINT32 * NumberOfLines)
  ]

class EFI_ACPI_6_5_NFIT_SMBIOS_MANAGEMENT_INFORMATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        UINT16),
    ("Length",      UINT16),
    ("Reserved_4",  UINT32),
    # ("Data",      UINT8 * N)
  ]

EFI_ACPI_6_5_NFIT_NVDIMM_CONTROL_REGION_VALID_FIELDS_MANUFACTURING          = BIT0
EFI_ACPI_6_5_NFIT_NVDIMM_CONTROL_REGION_FLAGS_BLOCK_DATA_WINDOWS_BUFFERED    = BIT0
class EFI_ACPI_6_5_NFIT_NVDIMM_CONTROL_REGION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                        UINT16),
    ("Length",                                      UINT16),
    ("NVDIMMControlRegionStructureIndex",           UINT16),
    ("VendorID",                                    UINT16),
    ("DeviceID",                                    UINT16),
    ("RevisionID",                                  UINT16),
    ("SubsystemVendorID",                           UINT16),
    ("SubsystemDeviceID",                           UINT16),
    ("SubsystemRevisionID",                         UINT16),
    ("ValidFields",                                 UINT8),
    ("ManufacturingLocation",                       UINT8),
    ("ManufacturingDate",                           UINT16),
    ("Reserved_22",                                 UINT8 * 2),
    ("SerialNumber",                                UINT32),
    ("RegionFormatInterfaceCode",                   UINT16),
    ("NumberOfBlockControlWindows",                 UINT16),
    ("SizeOfBlockControlWindow",                    UINT64),
    ("CommandRegisterOffsetInBlockControlWindow",   UINT64),
    ("SizeOfCommandRegisterInBlockControlWindows",  UINT64),
    ("StatusRegisterOffsetInBlockControlWindow",    UINT64),
    ("SizeOfStatusRegisterInBlockControlWindows",   UINT64),
    ("NVDIMMControlRegionFlag",                     UINT16),
    ("Reserved_74",                                 UINT8)
  ]

class EFI_ACPI_6_5_NFIT_NVDIMM_BLOCK_DATA_WINDOW_REGION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                                UINT16),
    ("Length",                                              UINT16),
    ("NVDIMMControlRegionStructureIndex",                   UINT16),
    ("NumberOfBlockDataWindows",                            UINT16),
    ("BlockDataWindowStartOffset",                          UINT64),
    ("SizeOfBlockDataWindow",                               UINT64),
    ("BlockAccessibleMemoryCapacity",                       UINT64),
    ("BeginningAddressOfFirstBlockInBlockAccessibleMemory", UINT64)
  ]

class EFI_ACPI_6_5_NFIT_FLUSH_HINT_ADDRESS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                        UINT16),
    ("Length",                      UINT16),
    ("NFITDeviceHandle",            EFI_ACPI_6_5_NFIT_DEVICE_HANDLE),
    ("NumberOfFlushHintAddresses",  UINT16),
    ("Reserved_10",                 UINT8 * 6),
    # ("FlushHintAddress",            UINT64 * NumberOfFlushHintAddresses)
  ]

class EFI_ACPI_6_5_NFIT_PLATFORM_CAPABILITIES_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                        UINT16),
    ("Length",                      UINT16),
    ("HighestValidCapability",      UINT8),
    ("Reserved_5",                  UINT8 * 3),
    ("Capabilities",                UINT32),
    ("Reserved_12",                 UINT8 * 4)
  ]

EFI_ACPI_6_5_NFIT_PLATFORM_CAPABILITY_CPU_CACHE_FLUSH_TO_NVDIMM_DURABILITY_ON_POWER_LOSS          = BIT0
EFI_ACPI_6_5_NFIT_PLATFORM_CAPABILITY_MEMORY_CONTROLLER_FLUSH_TO_NVDIMM_DURABILITY_ON_POWER_LOSS  = BIT1
EFI_ACPI_6_5_NFIT_PLATFORM_CAPABILITY_BYTE_ADDRESSABLE_PERSISTENT_MEMORY_HARDWARE_MIRRORING       = BIT2
class EFI_ACPI_6_5_SECURE_DEVICES_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  EFI_ACPI_DESCRIPTION_HEADER)
  ]

EFI_ACPI_6_5_SECURE_DEVICES_TABLE_REVISION  = 0x01

EFI_ACPI_6_5_SDEV_TYPE_ACPI_NAMESPACE_DEVICE   = 0x01
EFI_ACPI_6_5_SDEV_TYPE_PCIE_ENDPOINT_DEVICE    = 0x00

EFI_ACPI_6_5_SDEV_FLAG_ALLOW_HANDOFF                      = BIT0
EFI_ACPI_6_5_SDEV_FLAG_SECURE_ACCESS_COMPONENTS_PRESENT   = BIT1

class EFI_ACPI_6_5_SDEV_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8),
    ("Flags",   UINT8),
    ("Length",  UINT16)
  ]

class EFI_ACPI_6_5_SDEV_STRUCTURE_ACPI_NAMESPACE_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          EFI_ACPI_6_5_SDEV_STRUCTURE_HEADER),
    ("DeviceIdentifierOffset",          UINT16),
    ("DeviceIdentifierLength",          UINT16),
    ("VendorSpecificDataOffset",        UINT16),
    ("VendorSpecificDataLength",        UINT16),
    ("SecureAccessComponentsOffset",    UINT16),
    ("SecureAccessComponentsLength",    UINT16)
  ]

EFI_ACPI_6_5_SDEV_SECURE_ACCESS_COMPONENT_TYPE_IDENTIFICATION  = 0x00
EFI_ACPI_6_5_SDEV_SECURE_ACCESS_COMPONENT_TYPE_MEMORY          = 0x01

class EFI_ACPI_6_5_SDEV_SECURE_ACCESS_COMPONENT_IDENTIFICATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                              EFI_ACPI_6_5_SDEV_STRUCTURE_HEADER),
    ("HardwareIdentifierOffset",            UINT16),
    ("HardwareIdentifierLength",            UINT16),
    ("SubsystemIdentifierOffset",           UINT16),
    ("SubsystemIdentifierLength",           UINT16),
    ("HardwareRevision",                    UINT16),
    ("HardwareRevisionPresent",             UINT8),
    ("ClassCodePresent",                    UINT8),
    ("PciCompatibleBaseClass",              UINT8),
    ("PciCompatibleSubClass",               UINT8),
    ("PciCompatibleProgrammingInterface",   UINT8)
  ]

class EFI_ACPI_6_5_SDEV_SECURE_ACCESS_COMPONENT_MEMORY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_6_5_SDEV_STRUCTURE_HEADER),
    ("Reserved",            UINT16),
    ("MemoryAddressBase",   UINT64),
    ("MemoryLength",        UINT64)
  ]

class EFI_ACPI_6_5_SDEV_STRUCTURE_PCIE_ENDPOINT_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      EFI_ACPI_6_5_SDEV_STRUCTURE_HEADER),
    ("PciSegmentNumber",            UINT16),
    ("StartBusNumber",              UINT16),
    ("PciPathOffset",               UINT16),
    ("PciPathLength",               UINT16),
    ("VendorSpecificDataOffset",    UINT16),
    ("VendorSpecificDataLength",    UINT16)
  ]

class EFI_ACPI_6_5_BOOT_ERROR_RECORD_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      EFI_ACPI_DESCRIPTION_HEADER),
    ("BootErrorRegionLength",       UINT32),
    ("BootErrorRegion",             UINT64)
  ]

EFI_ACPI_6_5_BOOT_ERROR_RECORD_TABLE_REVISION = 0x01

EFI_ACPI_6_5_ERROR_BLOCK_STATUS = EFI_ACPI_6_4_ERROR_BLOCK_STATUS

EFI_ACPI_6_5_BOOT_ERROR_REGION_STRUCTURE = EFI_ACPI_6_4_BOOT_ERROR_REGION_STRUCTURE

EFI_ACPI_6_5_ERROR_SEVERITY_CORRECTABLE  = EFI_ACPI_6_4_ERROR_SEVERITY_CORRECTABLE
EFI_ACPI_6_5_ERROR_SEVERITY_FATAL        = EFI_ACPI_6_4_ERROR_SEVERITY_FATAL
EFI_ACPI_6_5_ERROR_SEVERITY_CORRECTED    = EFI_ACPI_6_4_ERROR_SEVERITY_CORRECTED
EFI_ACPI_6_5_ERROR_SEVERITY_NONE         = EFI_ACPI_6_4_ERROR_SEVERITY_NONE

EFI_ACPI_6_5_ERROR_SEVERITY_CORRECTABLE          = 0x00
class EFI_ACPI_6_5_GENERIC_ERROR_DATA_ENTRY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionType",     UINT8 * 16),
    ("ErrorSeverity",   UINT32),
    ("Revision",        UINT16),
    ("ValidationBits",  UINT8),
    ("Flags",           UINT8),
    ("ErrorDataLength", UINT32),
    ("FruId",           UINT8 * 16),
    ("FruText",         UINT8 * 20),
    ("Timestamp",       UINT8 * 8)
  ]

EFI_ACPI_6_5_GENERIC_ERROR_DATA_ENTRY_REVISION  = EFI_ACPI_6_4_GENERIC_ERROR_DATA_ENTRY_REVISION

EFI_ACPI_6_5_HARDWARE_ERROR_SOURCE_TABLE_HEADER = EFI_ACPI_6_4_HARDWARE_ERROR_SOURCE_TABLE_HEADER

EFI_ACPI_6_5_HARDWARE_ERROR_SOURCE_TABLE_REVISION = 0x02

EFI_ACPI_6_5_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION  = EFI_ACPI_6_4_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION
EFI_ACPI_6_5_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK  = EFI_ACPI_6_4_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK
EFI_ACPI_6_5_IA32_ARCHITECTURE_NMI_ERROR                = EFI_ACPI_6_4_IA32_ARCHITECTURE_NMI_ERROR
EFI_ACPI_6_5_PCI_EXPRESS_ROOT_PORT_AER                  = EFI_ACPI_6_4_PCI_EXPRESS_ROOT_PORT_AER
EFI_ACPI_6_5_PCI_EXPRESS_DEVICE_AER                     = EFI_ACPI_6_4_PCI_EXPRESS_DEVICE_AER
EFI_ACPI_6_5_PCI_EXPRESS_BRIDGE_AER                     = EFI_ACPI_6_4_PCI_EXPRESS_BRIDGE_AER
EFI_ACPI_6_5_GENERIC_HARDWARE_ERROR                     = EFI_ACPI_6_4_GENERIC_HARDWARE_ERROR
EFI_ACPI_6_5_GENERIC_HARDWARE_ERROR_VERSION_2           = 0x0A
EFI_ACPI_6_5_IA32_ARCHITECTURE_DEFERRED_MACHINE_CHECK   = 0x0B

EFI_ACPI_6_5_ERROR_SOURCE_FLAG_FIRMWARE_FIRST       = EFI_ACPI_6_4_ERROR_SOURCE_FLAG_FIRMWARE_FIRST
EFI_ACPI_6_5_ERROR_SOURCE_FLAG_GLOBAL               = EFI_ACPI_6_4_ERROR_SOURCE_FLAG_GLOBAL
EFI_ACPI_6_5_ERROR_SOURCE_FLAG_GHES_ASSIST          = (1 << 2)

EFI_ACPI_6_5_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE = EFI_ACPI_6_4_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE

EFI_ACPI_6_5_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE = EFI_ACPI_6_4_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE

EFI_ACPI_6_5_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_IA32      = EFI_ACPI_6_4_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_IA32
EFI_ACPI_6_5_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_INTEL64   = EFI_ACPI_6_4_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_INTEL64
EFI_ACPI_6_5_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_AMD64     = EFI_ACPI_6_4_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_AMD64

EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_POLLED                = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_POLLED
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_EXTERNAL_INTERRUPT    = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_EXTERNAL_INTERRUPT
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_LOCAL_INTERRUPT       = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_LOCAL_INTERRUPT
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_SCI                   = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_SCI
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_NMI                   = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_NMI
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_ARMV8_SEA             = 0x08
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_ARMV8_SEI             = 0x09
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_GSIV                  = 0x0A
EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_SOFTWARE_DELEGATED_EXCEPTION  = 0x0B

EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE

EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_STRUCTURE = EFI_ACPI_6_4_HARDWARE_ERROR_NOTIFICATION_STRUCTURE

EFI_ACPI_6_5_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE = EFI_ACPI_6_4_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE

EFI_ACPI_6_5_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE = EFI_ACPI_6_4_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE

EFI_ACPI_6_5_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE = EFI_ACPI_6_4_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE

EFI_ACPI_6_5_PCI_EXPRESS_DEVICE_AER_STRUCTURE = EFI_ACPI_6_4_PCI_EXPRESS_DEVICE_AER_STRUCTURE

EFI_ACPI_6_5_PCI_EXPRESS_BRIDGE_AER_STRUCTURE = EFI_ACPI_6_4_PCI_EXPRESS_BRIDGE_AER_STRUCTURE

class EFI_ACPI_6_5_GENERIC_HARDWARE_ERROR_SOURCE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("RelatedSourceId",               UINT16),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("MaxRawDataLength",              UINT32),
    ("ErrorStatusAddress",            EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("NotificationStructure",         EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("ErrorStatusBlockLength",        UINT32)
  ]

class EFI_ACPI_6_5_GENERIC_HARDWARE_ERROR_SOURCE_VERSION_2_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("RelatedSourceId",               UINT16),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("MaxRawDataLength",              UINT32),
    ("ErrorStatusAddress",            EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("NotificationStructure",         EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("ErrorStatusBlockLength",        UINT32),
    ("ReadAckRegister",               EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("ReadAckPreserve",               UINT64),
    ("ReadAckWrite",                  UINT64)
  ]

class EFI_ACPI_6_5_GENERIC_ERROR_STATUS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlockStatus",         EFI_ACPI_6_5_ERROR_BLOCK_STATUS),
    ("RawDataOffset",       UINT32),
    ("RawDataLength",       UINT32),
    ("DataLength",          UINT32),
    ("ErrorSeverity",       UINT32)
  ]

class EFI_ACPI_6_5_IA32_ARCHITECTURE_DEFERRED_MACHINE_CHECK_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT16),
    ("SourceId",                        UINT16),
    ("Reserved0",                       UINT8 * 2),
    ("Flags",                           UINT8),
    ("Enabled",                         UINT8),
    ("NumberOfRecordsToPreAllocate",    UINT32),
    ("MaxSectionsPerRecord",            UINT32),
    ("NotificationStructure",           EFI_ACPI_6_5_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("NumberOfHardwareBanks",           UINT8),
    ("Reserved1",                       UINT8 * 3)
  ]

class EFI_ACPI_6_5_HETEROGENEOUS_MEMORY_ATTRIBUTE_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",    UINT8 * 4)
  ]

EFI_ACPI_6_5_HETEROGENEOUS_MEMORY_ATTRIBUTE_TABLE_REVISION  = 0x01

EFI_ACPI_6_5_HMAT_TYPE_MEMORY_SUBSYSTEM_ADDRESS_RANGE              = 0x00
EFI_ACPI_6_5_HMAT_TYPE_SYSTEM_LOCALITY_LATENCY_AND_BANDWIDTH_INFO  = 0x01
EFI_ACPI_6_5_HMAT_TYPE_MEMORY_SIDE_CACHE_INFO                      = 0x02

class EFI_ACPI_6_5_HMAT_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        UINT16),
    ("Reserved",    UINT8 * 2),
    ("Length",      UINT32)
  ]

class EFI_ACPI_6_5_HMAT_STRUCTURE_MEMORY_PROXIMITY_DOMAIN_ATTRIBUTES_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InitiatorProximityDomainValid",   UINT16, 1),
    ("Reserved",                        UINT16, 15)
  ]

class EFI_ACPI_6_5_HMAT_STRUCTURE_MEMORY_PROXIMITY_DOMAIN_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("Reserved",                            UINT8 * 2),
    ("Length",                              UINT32),
    ("Flags",                               EFI_ACPI_6_5_HMAT_STRUCTURE_MEMORY_PROXIMITY_DOMAIN_ATTRIBUTES_FLAGS),
    ("Reserved1",                           UINT8 * 2),
    ("InitiatorProximityDomain",            UINT32),
    ("MemoryProximityDomain",               UINT32),
    ("Reserved2",                           UINT8 * 20)
  ]

class EFI_ACPI_6_5_HMAT_STRUCTURE_SYSTEM_LOCALITY_LATENCY_AND_BANDWIDTH_INFO_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryHierarchy",     UINT8, 4),
    ("AccessAttributes",    UINT8, 2),
    ("Reserved",            UINT8, 2)
  ]

class EFI_ACPI_6_5_HMAT_STRUCTURE_SYSTEM_LOCALITY_LATENCY_AND_BANDWIDTH_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("Reserved",                            UINT8 * 2),
    ("Length",                              UINT32),
    ("Flags",                               EFI_ACPI_6_5_HMAT_STRUCTURE_SYSTEM_LOCALITY_LATENCY_AND_BANDWIDTH_INFO_FLAGS),
    ("DataType",                            UINT8),
    ("MinTransferSize",                     UINT8),
    ("Reserved1",                           UINT8),
    ("NumberOfInitiatorProximityDomains",   UINT32),
    ("NumberOfTargetProximityDomains",      UINT32),
    ("Reserved2",                           UINT8 * 4),
    ("EntryBaseUnit",                       UINT64)
  ]

class EFI_ACPI_6_5_HMAT_STRUCTURE_MEMORY_SIDE_CACHE_INFO_CACHE_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TotalCacheLevels",        UINT32, 4),
    ("CacheLevel",              UINT32, 4),
    ("CacheAssociativity",      UINT32, 4),
    ("WritePolicy",             UINT32, 4),
    ("CacheLineSize",           UINT32, 16)
  ]

class EFI_ACPI_6_5_HMAT_STRUCTURE_MEMORY_SIDE_CACHE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("Reserved",                            UINT8 * 2),
    ("Length",                              UINT32),
    ("MemoryProximityDomain",               UINT32),
    ("Reserved1",                           UINT8 * 4),
    ("MemorySideCacheSize",                 UINT64),
    ("CacheAttributes",                     EFI_ACPI_6_5_HMAT_STRUCTURE_MEMORY_SIDE_CACHE_INFO_CACHE_ATTRIBUTES),
    ("Reserved2",                           UINT8 * 2),
    ("NumberOfSmbiosHandles",               UINT16)
  ]

EFI_ACPI_6_5_ERROR_RECORD_SERIALIZATION_TABLE_HEADER = EFI_ACPI_6_4_ERROR_RECORD_SERIALIZATION_TABLE_HEADER

EFI_ACPI_6_5_ERROR_RECORD_SERIALIZATION_TABLE_REVISION = 0x01

EFI_ACPI_6_5_ERST_BEGIN_WRITE_OPERATION                    = EFI_ACPI_6_4_ERST_BEGIN_WRITE_OPERATION
EFI_ACPI_6_5_ERST_BEGIN_READ_OPERATION                     = EFI_ACPI_6_4_ERST_BEGIN_READ_OPERATION
EFI_ACPI_6_5_ERST_BEGIN_CLEAR_OPERATION                    = EFI_ACPI_6_4_ERST_BEGIN_CLEAR_OPERATION
EFI_ACPI_6_5_ERST_END_OPERATION                            = EFI_ACPI_6_4_ERST_END_OPERATION
EFI_ACPI_6_5_ERST_SET_RECORD_OFFSET                        = EFI_ACPI_6_4_ERST_SET_RECORD_OFFSET
EFI_ACPI_6_5_ERST_EXECUTE_OPERATION                        = EFI_ACPI_6_4_ERST_EXECUTE_OPERATION
EFI_ACPI_6_5_ERST_CHECK_BUSY_STATUS                        = EFI_ACPI_6_4_ERST_CHECK_BUSY_STATUS
EFI_ACPI_6_5_ERST_GET_COMMAND_STATUS                       = EFI_ACPI_6_4_ERST_GET_COMMAND_STATUS
EFI_ACPI_6_5_ERST_GET_RECORD_IDENTIFIER                    = EFI_ACPI_6_4_ERST_GET_RECORD_IDENTIFIER
EFI_ACPI_6_5_ERST_SET_RECORD_IDENTIFIER                    = EFI_ACPI_6_4_ERST_SET_RECORD_IDENTIFIER
EFI_ACPI_6_5_ERST_GET_RECORD_COUNT                         = EFI_ACPI_6_4_ERST_GET_RECORD_COUNT
EFI_ACPI_6_5_ERST_BEGIN_DUMMY_WRITE_OPERATION              = EFI_ACPI_6_4_ERST_BEGIN_DUMMY_WRITE_OPERATION
EFI_ACPI_6_5_ERST_GET_ERROR_LOG_ADDRESS_RANGE              = EFI_ACPI_6_4_ERST_GET_ERROR_LOG_ADDRESS_RANGE
EFI_ACPI_6_5_ERST_GET_ERROR_LOG_ADDRESS_RANGE_LENGTH       = EFI_ACPI_6_4_ERST_GET_ERROR_LOG_ADDRESS_RANGE_LENGTH
EFI_ACPI_6_5_ERST_GET_ERROR_LOG_ADDRESS_RANGE_ATTRIBUTES   = EFI_ACPI_6_4_ERST_GET_ERROR_LOG_ADDRESS_RANGE_ATTRIBUTES
EFI_ACPI_6_5_ERST_GET_EXECUTE_OPERATION_TIMINGS            = 0x10

EFI_ACPI_6_5_ERST_STATUS_SUCCESS                           = EFI_ACPI_6_4_ERST_STATUS_SUCCESS
EFI_ACPI_6_5_ERST_STATUS_NOT_ENOUGH_SPACE                  = EFI_ACPI_6_4_ERST_STATUS_NOT_ENOUGH_SPACE
EFI_ACPI_6_5_ERST_STATUS_HARDWARE_NOT_AVAILABLE            = EFI_ACPI_6_4_ERST_STATUS_HARDWARE_NOT_AVAILABLE
EFI_ACPI_6_5_ERST_STATUS_FAILED                            = EFI_ACPI_6_4_ERST_STATUS_FAILED
EFI_ACPI_6_5_ERST_STATUS_RECORD_STORE_EMPTY                = EFI_ACPI_6_4_ERST_STATUS_RECORD_STORE_EMPTY
EFI_ACPI_6_5_ERST_STATUS_RECORD_NOT_FOUND                  = EFI_ACPI_6_4_ERST_STATUS_RECORD_NOT_FOUND

EFI_ACPI_6_5_ERST_READ_REGISTER                            = EFI_ACPI_6_4_ERST_READ_REGISTER
EFI_ACPI_6_5_ERST_READ_REGISTER_VALUE                      = EFI_ACPI_6_4_ERST_READ_REGISTER_VALUE
EFI_ACPI_6_5_ERST_WRITE_REGISTER                           = EFI_ACPI_6_4_ERST_WRITE_REGISTER
EFI_ACPI_6_5_ERST_WRITE_REGISTER_VALUE                     = EFI_ACPI_6_4_ERST_WRITE_REGISTER_VALUE
EFI_ACPI_6_5_ERST_NOOP                                     = EFI_ACPI_6_4_ERST_NOOP
EFI_ACPI_6_5_ERST_LOAD_VAR1                                = EFI_ACPI_6_4_ERST_LOAD_VAR1
EFI_ACPI_6_5_ERST_LOAD_VAR2                                = EFI_ACPI_6_4_ERST_LOAD_VAR2
EFI_ACPI_6_5_ERST_STORE_VAR1                               = EFI_ACPI_6_4_ERST_STORE_VAR1
EFI_ACPI_6_5_ERST_ADD                                      = EFI_ACPI_6_4_ERST_ADD
EFI_ACPI_6_5_ERST_SUBTRACT                                 = EFI_ACPI_6_4_ERST_SUBTRACT
EFI_ACPI_6_5_ERST_ADD_VALUE                                = EFI_ACPI_6_4_ERST_ADD_VALUE
EFI_ACPI_6_5_ERST_SUBTRACT_VALUE                           = EFI_ACPI_6_4_ERST_SUBTRACT_VALUE
EFI_ACPI_6_5_ERST_STALL                                    = EFI_ACPI_6_4_ERST_STALL
EFI_ACPI_6_5_ERST_STALL_WHILE_TRUE                         = EFI_ACPI_6_4_ERST_STALL_WHILE_TRUE
EFI_ACPI_6_5_ERST_SKIP_NEXT_INSTRUCTION_IF_TRUE            = EFI_ACPI_6_4_ERST_SKIP_NEXT_INSTRUCTION_IF_TRUE
EFI_ACPI_6_5_ERST_GOTO                                     = EFI_ACPI_6_4_ERST_GOTO
EFI_ACPI_6_5_ERST_SET_SRC_ADDRESS_BASE                     = EFI_ACPI_6_4_ERST_SET_SRC_ADDRESS_BASE
EFI_ACPI_6_5_ERST_SET_DST_ADDRESS_BASE                     = EFI_ACPI_6_4_ERST_SET_DST_ADDRESS_BASE
EFI_ACPI_6_5_ERST_MOVE_DATA                                = EFI_ACPI_6_4_ERST_MOVE_DATA

EFI_ACPI_6_5_ERST_PRESERVE_REGISTER                        = EFI_ACPI_6_4_ERST_PRESERVE_REGISTER

EFI_ACPI_6_5_ERST_SERIALIZATION_INSTRUCTION_ENTRY = EFI_ACPI_6_4_ERST_SERIALIZATION_INSTRUCTION_ENTRY

EFI_ACPI_6_5_ERROR_INJECTION_TABLE_HEADER = EFI_ACPI_6_4_ERROR_INJECTION_TABLE_HEADER

EFI_ACPI_6_5_ERROR_INJECTION_TABLE_REVISION = 0x01

EFI_ACPI_6_5_EINJ_BEGIN_INJECTION_OPERATION                = EFI_ACPI_6_4_EINJ_BEGIN_INJECTION_OPERATION
EFI_ACPI_6_5_EINJ_GET_TRIGGER_ERROR_ACTION_TABLE           = EFI_ACPI_6_4_EINJ_GET_TRIGGER_ERROR_ACTION_TABLE
EFI_ACPI_6_5_EINJ_SET_ERROR_TYPE                           = EFI_ACPI_6_4_EINJ_SET_ERROR_TYPE
EFI_ACPI_6_5_EINJ_GET_ERROR_TYPE                           = EFI_ACPI_6_4_EINJ_GET_ERROR_TYPE
EFI_ACPI_6_5_EINJ_END_OPERATION                            = EFI_ACPI_6_4_EINJ_END_OPERATION
EFI_ACPI_6_5_EINJ_EXECUTE_OPERATION                        = EFI_ACPI_6_4_EINJ_EXECUTE_OPERATION
EFI_ACPI_6_5_EINJ_CHECK_BUSY_STATUS                        = EFI_ACPI_6_4_EINJ_CHECK_BUSY_STATUS
EFI_ACPI_6_5_EINJ_GET_COMMAND_STATUS                       = EFI_ACPI_6_4_EINJ_GET_COMMAND_STATUS
EFI_ACPI_6_5_EINJ_SET_ERROR_TYPE_WITH_ADDRESS              = EFI_ACPI_6_4_EINJ_SET_ERROR_TYPE_WITH_ADDRESS
EFI_ACPI_6_5_EINJ_GET_EXECUTE_OPERATION_TIMINGS            = EFI_ACPI_6_4_EINJ_GET_EXECUTE_OPERATION_TIMINGS
EFI_ACPI_6_5_EINJ_EINJV2_SET_ERROR_TYPE                    = 0x10
EFI_ACPI_6_5_EINJ_EINJV2_GET_ERROR_TYPE                    = 0x11
EFI_ACPI_6_5_EINJ_TRIGGER_ERROR                            = EFI_ACPI_6_4_EINJ_TRIGGER_ERROR

EFI_ACPI_6_5_EINJ_STATUS_SUCCESS                           = EFI_ACPI_6_4_EINJ_STATUS_SUCCESS
EFI_ACPI_6_5_EINJ_STATUS_UNKNOWN_FAILURE                   = EFI_ACPI_6_4_EINJ_STATUS_UNKNOWN_FAILURE
EFI_ACPI_6_5_EINJ_STATUS_INVALID_ACCESS                    = EFI_ACPI_6_4_EINJ_STATUS_INVALID_ACCESS

EFI_ACPI_6_5_EINJ_ERROR_PROCESSOR_CORRECTABLE                 = EFI_ACPI_6_4_EINJ_ERROR_PROCESSOR_CORRECTABLE
EFI_ACPI_6_5_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_NONFATAL      = EFI_ACPI_6_4_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_NONFATAL
EFI_ACPI_6_5_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_FATAL         = EFI_ACPI_6_4_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_FATAL
EFI_ACPI_6_5_EINJ_ERROR_MEMORY_CORRECTABLE                    = EFI_ACPI_6_4_EINJ_ERROR_MEMORY_CORRECTABLE
EFI_ACPI_6_5_EINJ_ERROR_MEMORY_UNCORRECTABLE_NONFATAL         = EFI_ACPI_6_4_EINJ_ERROR_MEMORY_UNCORRECTABLE_NONFATAL
EFI_ACPI_6_5_EINJ_ERROR_MEMORY_UNCORRECTABLE_FATAL            = EFI_ACPI_6_4_EINJ_ERROR_MEMORY_UNCORRECTABLE_FATAL
EFI_ACPI_6_5_EINJ_ERROR_PCI_EXPRESS_CORRECTABLE               = EFI_ACPI_6_4_EINJ_ERROR_PCI_EXPRESS_CORRECTABLE
EFI_ACPI_6_5_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_NONFATAL    = EFI_ACPI_6_4_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_NONFATAL
EFI_ACPI_6_5_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_FATAL       = EFI_ACPI_6_4_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_FATAL
EFI_ACPI_6_5_EINJ_ERROR_PLATFORM_CORRECTABLE                  = EFI_ACPI_6_4_EINJ_ERROR_PLATFORM_CORRECTABLE
EFI_ACPI_6_5_EINJ_ERROR_PLATFORM_UNCORRECTABLE_NONFATAL       = EFI_ACPI_6_4_EINJ_ERROR_PLATFORM_UNCORRECTABLE_NONFATAL
EFI_ACPI_6_5_EINJ_ERROR_PLATFORM_UNCORRECTABLE_FATAL          = EFI_ACPI_6_4_EINJ_ERROR_PLATFORM_UNCORRECTABLE_FATAL

EFI_ACPI_6_5_EINJ_READ_REGISTER                            = EFI_ACPI_6_4_EINJ_READ_REGISTER
EFI_ACPI_6_5_EINJ_READ_REGISTER_VALUE                      = EFI_ACPI_6_4_EINJ_READ_REGISTER_VALUE
EFI_ACPI_6_5_EINJ_WRITE_REGISTER                           = EFI_ACPI_6_4_EINJ_WRITE_REGISTER
EFI_ACPI_6_5_EINJ_WRITE_REGISTER_VALUE                     = EFI_ACPI_6_4_EINJ_WRITE_REGISTER_VALUE
EFI_ACPI_6_5_EINJ_NOOP                                     = EFI_ACPI_6_4_EINJ_NOOP

EFI_ACPI_6_5_EINJ_PRESERVE_REGISTER                        = EFI_ACPI_6_4_EINJ_PRESERVE_REGISTER

EFI_ACPI_6_5_EINJ_INJECTION_INSTRUCTION_ENTRY = EFI_ACPI_6_4_EINJ_INJECTION_INSTRUCTION_ENTRY

EFI_ACPI_6_5_EINJ_TRIGGER_ACTION_TABLE = EFI_ACPI_6_4_EINJ_TRIGGER_ACTION_TABLE

EFI_ACPI_6_5_PLATFORM_COMMUNICATION_CHANNEL_TABLE_HEADER = EFI_ACPI_6_4_PLATFORM_COMMUNICATION_CHANNEL_TABLE_HEADER

EFI_ACPI_6_5_PLATFORM_COMMUNICATION_CHANNEL_TABLE_REVISION = EFI_ACPI_6_4_PLATFORM_COMMUNICATION_CHANNEL_TABLE_REVISION

EFI_ACPI_6_5_PCCT_FLAGS_PLATFORM_INTERRUPT  = BIT0

EFI_ACPI_6_5_PCCT_SUBSPACE_TYPE_GENERIC                        = 0x00
EFI_ACPI_6_5_PCCT_SUBSPACE_TYPE_1_HW_REDUCED_COMMUNICATIONS    = 0x01
EFI_ACPI_6_5_PCCT_SUBSPACE_TYPE_2_HW_REDUCED_COMMUNICATIONS    = 0x02
EFI_ACPI_6_5_PCCT_SUBSPACE_TYPE_3_EXTENDED_PCC                 = 0x03
EFI_ACPI_6_5_PCCT_SUBSPACE_TYPE_4_EXTENDED_PCC                 = 0x04
EFI_ACPI_6_5_PCCT_SUBSPACE_TYPE_5_HW_REGISTERS_COMMUNICATIONS  = 0x05

EFI_ACPI_6_5_PCCT_SUBSPACE_HEADER = EFI_ACPI_6_4_PCCT_SUBSPACE_HEADER

EFI_ACPI_6_5_PCCT_SUBSPACE_GENERIC = EFI_ACPI_6_4_PCCT_SUBSPACE_GENERIC

class EFI_ACPI_6_5_PCCT_GENERIC_SHARED_MEMORY_REGION_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Command",             UINT8),
    ("Reserved",            UINT8, 7),
    ("NotifyOnCompletion",  UINT8, 1)
  ]

class EFI_ACPI_6_5_PCCT_GENERIC_SHARED_MEMORY_REGION_STATUS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommandComplete",         UINT8, 1),
    ("PlatformInterrupt",       UINT8, 1),
    ("Error",                   UINT8, 1),
    ("PlatformNotification",    UINT8, 1),
    ("Reserved",                UINT8, 4),
    ("Reserved1",               UINT8),
  ]

EFI_ACPI_6_5_PCCT_GENERIC_SHARED_MEMORY_REGION_HEADER = EFI_ACPI_6_4_PCCT_GENERIC_SHARED_MEMORY_REGION_HEADER

EFI_ACPI_6_5_PCCT_SUBSPACE_DOORBELL_INTERRUPT_FLAGS_POLARITY          = BIT0
EFI_ACPI_6_5_PCCT_SUBSPACE_DOORBELL_INTERRUPT_FLAGS_MODE              = BIT1

class EFI_ACPI_6_5_PCCT_SUBSPACE_1_HW_REDUCED_COMMUNICATIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT8),
    ("Length",                          UINT8),
    ("PlatformInterrupt",               UINT32),
    ("PlatformInterruptFlags",          UINT8),
    ("Reserved",                        UINT8),
    ("BaseAddress",                     UINT64),
    ("AddressLength",                   UINT64),
    ("DoorbellRegister",                EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("DoorbellPreserve",                UINT64),
    ("DoorbellWrite",                   UINT64),
    ("NominalLatency",                  UINT32),
    ("MaximumPeriodicAccessRate",       UINT32),
    ("MinimumRequestTurnaroundTime",    UINT16)
  ]

class EFI_ACPI_6_5_PCCT_SUBSPACE_2_HW_REDUCED_COMMUNICATIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT8),
    ("Length",                          UINT8),
    ("PlatformInterrupt",               UINT32),
    ("PlatformInterruptFlags",          UINT8),
    ("Reserved",                        UINT8),
    ("BaseAddress",                     UINT64),
    ("AddressLength",                   UINT64),
    ("DoorbellRegister",                EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("DoorbellPreserve",                UINT64),
    ("DoorbellWrite",                   UINT64),
    ("NominalLatency",                  UINT32),
    ("MaximumPeriodicAccessRate",       UINT32),
    ("MinimumRequestTurnaroundTime",    UINT16),
    ("PlatformInterruptAckRegister",    EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("PlatformInterruptAckPreserve",    UINT64),
    ("PlatformInterruptAckWrite",       UINT64)
  ]

class EFI_ACPI_6_5_PCCT_SUBSPACE_3_EXTENDED_PCC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT8),
    ("Length",                          UINT8),
    ("PlatformInterrupt",               UINT32),
    ("PlatformInterruptFlags",          UINT8),
    ("Reserved",                        UINT8),
    ("BaseAddress",                     UINT64),
    ("AddressLength",                   UINT32),
    ("DoorbellRegister",                EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("DoorbellPreserve",                UINT64),
    ("DoorbellWrite",                   UINT64),
    ("NominalLatency",                  UINT32),
    ("MaximumPeriodicAccessRate",       UINT32),
    ("MinimumRequestTurnaroundTime",    UINT32),
    ("PlatformInterruptAckRegister",    EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("PlatformInterruptAckPreserve",    UINT64),
    ("PlatformInterruptAckSet",         UINT64),
    ("Reserved1",                       UINT8),
    ("CommandCompleteCheckRegister",    EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("CommandCompleteCheckMask",        UINT64),
    ("CommandCompleteUpdateRegister",   EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("CommandCompleteUpdatePreserve",   UINT64),
    ("CommandCompleteUpdateSet",        UINT64),
    ("ErrorStatusRegister",             EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("ErrorStatusMask",                 UINT64)
  ]

EFI_ACPI_6_5_PCCT_SUBSPACE_4_EXTENDED_PCC = EFI_ACPI_6_5_PCCT_SUBSPACE_3_EXTENDED_PCC

EFI_ACPI_6_5_PCCT_MASTER_SLAVE_COMMUNICATIONS_CHANNEL_FLAGS_NOTIFY_ON_COMPLETION  = BIT0

class EFI_ACPI_6_5_PCCT_EXTENDED_PCC_SHARED_MEMORY_REGION_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",   UINT32),
    ("Flags",       UINT32),
    ("Length",      UINT32),
    ("Command",     UINT32)
  ]

class EFI_ACPI_6_5_PCCT_SUBSPACE_5_HW_REGISTERS_COMMUNICATIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT8),
    ("Length",                          UINT8),
    ("Version",                         UINT16),
    ("BaseAddress",                     UINT64),
    ("SharedMemoryRangeLength",         UINT64),
    ("DoorbellRegister",                EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("DoorbellPreserve",                UINT64),
    ("DoorbellWrite",                   UINT64),
    ("CommandCompleteCheckRegister",    EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("CommandCompleteCheckMask",        UINT64),
    ("ErrorStatusRegister",             EFI_ACPI_6_5_GENERIC_ADDRESS_STRUCTURE),
    ("ErrorStatusMask",                 UINT64),
    ("NominalLatency",                  UINT32),
    ("MinimumRequestTurnaroundTime",    UINT32)
  ]

class EFI_6_4_PCCT_REDUCED_PCC_SUBSPACE_SHARED_MEMORY_REGION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",                       UINT32)
    # ("CommunicationSubspace",           UINT8 * N)
  ]

class EFI_ACPI_6_5_PLATFORM_DEBUG_TRIGGER_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          EFI_ACPI_DESCRIPTION_HEADER),
    ("TriggerCount",                    UINT8),
    ("Reserved",                        UINT8 * 3),
    ("TriggerIdentifierArrayOffset",    UINT32),
  ]

EFI_ACPI_6_5_PLATFORM_DEBUG_TRIGGER_TABLE_REVISION  = 0x00

class EFI_ACPI_6_5_PDTT_PCC_IDENTIFIER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SubChannelIdentifer",     UINT16, 8),
    ("Runtime",                 UINT16, 1),
    ("WaitForCompletion",       UINT16, 1),
    ("TriggerOrder",            UINT16, 1),
    ("Reserved",                UINT16, 5)
  ]

EFI_ACPI_6_5_PDTT_PCC_COMMAND_DOORBELL_ONLY    = 0x00
EFI_ACPI_6_5_PDTT_PCC_COMMAND_VENDOR_SPECIFIC  = 0x01

EFI_ACPI_6_5_PDTT_PCC = EFI_ACPI_6_5_PCCT_GENERIC_SHARED_MEMORY_REGION_HEADER

class EFI_ACPI_6_5_PROCESSOR_PROPERTIES_TOPOLOGY_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",     EFI_ACPI_DESCRIPTION_HEADER)
  ]

EFI_ACPI_6_5_PROCESSOR_PROPERTIES_TOPOLOGY_TABLE_REVISION  = 0x01

EFI_ACPI_6_5_PPTT_TYPE_PROCESSOR  = 0x00
EFI_ACPI_6_5_PPTT_TYPE_CACHE      = 0x01
EFI_ACPI_6_5_PPTT_TYPE_ID         = 0x02

class EFI_ACPI_6_5_PPTT_STRUCTURE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        UINT8),
    ("Length",      UINT8),
    ("Reserved",    UINT8 * 2)
  ]

EFI_ACPI_6_5_PPTT_PACKAGE_NOT_PHYSICAL          = 0x0
EFI_ACPI_6_5_PPTT_PACKAGE_PHYSICAL              = 0x1
EFI_ACPI_6_5_PPTT_PROCESSOR_ID_INVALID          = 0x0
EFI_ACPI_6_5_PPTT_PROCESSOR_ID_VALID            = 0x1
EFI_ACPI_6_5_PPTT_PROCESSOR_IS_NOT_THREAD       = 0x0
EFI_ACPI_6_5_PPTT_PROCESSOR_IS_THREAD           = 0x1
EFI_ACPI_6_5_PPTT_NODE_IS_NOT_LEAF              = 0x0
EFI_ACPI_6_5_PPTT_NODE_IS_LEAF                  = 0x1
EFI_ACPI_6_5_PPTT_IMPLEMENTATION_NOT_IDENTICAL  = 0x0
EFI_ACPI_6_5_PPTT_IMPLEMENTATION_IDENTICAL      = 0x1

class EFI_ACPI_6_5_PPTT_STRUCTURE_PROCESSOR_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PhysicalPackage",         UINT32, 1),
    ("AcpiProcessorIdValid",    UINT32, 1),
    ("ProcessorIsAThread",      UINT32, 1),
    ("NodeIsALeaf",             UINT32, 1),
    ("IdenticalImplementation", UINT32, 1),
    ("Reserved",                UINT32, 27)
  ]

class EFI_ACPI_6_5_PPTT_STRUCTURE_PROCESSOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                        UINT8),
    ("Length",                      UINT8),
    ("Reserved",                    UINT8 * 2),
    ("Flags",                       EFI_ACPI_6_5_PPTT_STRUCTURE_PROCESSOR_FLAGS),
    ("Parent",                      UINT32),
    ("AcpiProcessorId",             UINT32),
    ("NumberOfPrivateResources",    UINT32)
  ]

EFI_ACPI_6_5_PPTT_CACHE_SIZE_INVALID       = 0x0
EFI_ACPI_6_5_PPTT_CACHE_SIZE_VALID         = 0x1
EFI_ACPI_6_5_PPTT_NUMBER_OF_SETS_INVALID   = 0x0
EFI_ACPI_6_5_PPTT_NUMBER_OF_SETS_VALID     = 0x1
EFI_ACPI_6_5_PPTT_ASSOCIATIVITY_INVALID    = 0x0
EFI_ACPI_6_5_PPTT_ASSOCIATIVITY_VALID      = 0x1
EFI_ACPI_6_5_PPTT_ALLOCATION_TYPE_INVALID  = 0x0
EFI_ACPI_6_5_PPTT_ALLOCATION_TYPE_VALID    = 0x1
EFI_ACPI_6_5_PPTT_CACHE_TYPE_INVALID       = 0x0
EFI_ACPI_6_5_PPTT_CACHE_TYPE_VALID         = 0x1
EFI_ACPI_6_5_PPTT_WRITE_POLICY_INVALID     = 0x0
EFI_ACPI_6_5_PPTT_WRITE_POLICY_VALID       = 0x1
EFI_ACPI_6_5_PPTT_LINE_SIZE_INVALID        = 0x0
EFI_ACPI_6_5_PPTT_LINE_SIZE_VALID          = 0x1
EFI_ACPI_6_5_PPTT_CACHE_ID_INVALID         = 0x0
EFI_ACPI_6_5_PPTT_CACHE_ID_VALID           = 0x1

class EFI_ACPI_6_5_PPTT_STRUCTURE_CACHE_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SizePropertyValid",       UINT32, 1),
    ("NumberOfSetsValid",       UINT32, 1),
    ("AssociativityValid",      UINT32, 1),
    ("AllocationTypeValid",     UINT32, 1),
    ("CacheTypeValid",          UINT32, 1),
    ("WritePolicyValid",        UINT32, 1),
    ("LineSizeValid",           UINT32, 1),
    ("CacheIdValid",            UINT32, 1),
    ("Reserved",                UINT32, 24)
  ]

EFI_ACPI_6_5_CACHE_ATTRIBUTES_ALLOCATION_READ             = 0x0
EFI_ACPI_6_5_CACHE_ATTRIBUTES_ALLOCATION_WRITE            = 0x1
EFI_ACPI_6_5_CACHE_ATTRIBUTES_ALLOCATION_READ_WRITE       = 0x2
EFI_ACPI_6_5_CACHE_ATTRIBUTES_CACHE_TYPE_DATA             = 0x0
EFI_ACPI_6_5_CACHE_ATTRIBUTES_CACHE_TYPE_INSTRUCTION      = 0x1
EFI_ACPI_6_5_CACHE_ATTRIBUTES_CACHE_TYPE_UNIFIED          = 0x2
EFI_ACPI_6_5_CACHE_ATTRIBUTES_WRITE_POLICY_WRITE_BACK     = 0x0
EFI_ACPI_6_5_CACHE_ATTRIBUTES_WRITE_POLICY_WRITE_THROUGH  = 0x1

class EFI_ACPI_6_5_PPTT_STRUCTURE_CACHE_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AllocationType",      UINT8, 2),
    ("CacheType",           UINT8, 2),
    ("WritePolicy",         UINT8, 1),
    ("Reserved",            UINT8, 3)
  ]

class EFI_ACPI_6_5_PPTT_STRUCTURE_CACHE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                UINT8),
    ("Length",              UINT8),
    ("Reserved",            UINT8 * 2),
    ("Flags",               EFI_ACPI_6_5_PPTT_STRUCTURE_CACHE_FLAGS),
    ("NextLevelOfCache",    UINT32),
    ("Size",                UINT32),
    ("NumberOfSets",        UINT32),
    ("Associativity",       UINT8),
    ("Attributes",          EFI_ACPI_6_5_PPTT_STRUCTURE_CACHE_ATTRIBUTES),
    ("LineSize",            UINT16)
  ]

class EFI_ACPI_6_5_PLATFORM_HEALTH_ASSESSMENT_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      EFI_ACPI_DESCRIPTION_HEADER)
    # ("PlatformTelemetryRecords",    UINT8 * N)
  ]

EFI_ACPI_6_5_PLATFORM_HEALTH_ASSESSMENT_TABLE_REVISION  = 0x01

class EFI_ACPI_6_5_PHAT_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PlatformHealthAssessmentRecordType",  UINT16),
    ("RecordLength",                        UINT16),
    ("Revision",                            UINT8)
    # ("Data",                                UINT8 * N)
  ]

EFI_ACPI_6_5_PHAT_RECORD_TYPE_FIRMWARE_VERSION_DATA_RECORD  = 0x0000
EFI_ACPI_6_5_PHAT_RECORD_TYPE_FIRMWARE_HEALTH_DATA_RECORD   = 0x0001

class EFI_ACPI_6_5_PHAT_VERSION_ELEMENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ComponentId",     GUID),
    ("VersionValue",    UINT64),
    ("ProducerId",      UINT32)
  ]

class EFI_ACPI_6_5_PHAT_FIRMWARE_VERISON_DATA_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PlatformRecordType",  UINT16),
    ("RecordLength",        UINT16),
    ("Revision",            UINT8),
    ("Reserved",            UINT8 * 3),
    ("RecordCount",         UINT32)
    # ("PhatVersionElement",  UINT8 * N)
  ]

EFI_ACPI_6_5_PHAT_FIRMWARE_VERSION_DATA_RECORD_REVISION  = 0x01

class EFI_ACPI_6_5_PHAT_FIRMWARE_HEALTH_DATA_RECORD_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PlatformRecordType",          UINT16),
    ("RecordLength",                UINT16),
    ("Revision",                    UINT8),
    ("Reserved",                    UINT16),
    ("AmHealthy",                   UINT8),
    ("DeviceSignature",             GUID),
    ("DeviceSpecificDataOffset",    UINT32)
    # ("DevicePath",                  UINT32 * N)
    # ("DeviceSpecificData",          UINT32 * N)
  ]

EFI_ACPI_6_5_PHAT_FIRMWARE_HEALTH_DATA_RECORD_REVISION  = 0x01

EFI_ACPI_6_5_PHAT_FIRMWARE_HEALTH_DATA_RECORD_ERRORS_FOUND     = 0x00
EFI_ACPI_6_5_PHAT_FIRMWARE_HEALTH_DATA_RECORD_NO_ERRORS_FOUND  = 0x01
EFI_ACPI_6_5_PHAT_FIRMWARE_HEALTH_DATA_RECORD_UNKNOWN          = 0x02
EFI_ACPI_6_5_PHAT_FIRMWARE_HEALTH_DATA_RECORD_ADVISORY         = 0x03

class EFI_ACPI_6_5_PHAT_RESET_REASON_HEALTH_RECORD_VENDOR_DATA_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VendorDataID",  GUID),
    ("Length",        UINT16),
    ("Revision",      UINT16),
    # ("Data",          UINTN * N)
  ]

class EFI_ACPI_6_5_PHAT_RESET_REASON_HEALTH_RECORD_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SupportedSources",  UINT8),
    ("Source",            UINT8),
    ("SubSource",         UINT8),
    ("Reason",            UINT8),
    ("VendorCount",       UINT16),
    # ("VendorSpecificResetReasonEntry", EFI_ACPI_6_5_PHAT_RESET_REASON_HEALTH_RECORD_VENDOR_DATA_ENTRY * N)
  ]

EFI_ACPI_6_5_PHAT_RESET_REASON_HEADER_GUID  = EFI_GUID ( 0x7a014ce2, 0xf263, 0x4b77, ( 0xb8, 0x8a, 0xe6, 0x33, 0x6b, 0x78, 0x2c, 0x14 ))

EFI_ACPI_6_5_PHAT_RESET_REASON_SUPPORTED_SOURCES_UNKNOWN     = BIT0
EFI_ACPI_6_5_PHAT_RESET_REASON_SUPPORTED_SOURCES_HARDWARE    = BIT1
EFI_ACPI_6_5_PHAT_RESET_REASON_SUPPORTED_SOURCES_FIRMWARE    = BIT2
EFI_ACPI_6_5_PHAT_RESET_REASON_SUPPORTED_SOURCES_SOFTWARE    = BIT3
EFI_ACPI_6_5_PHAT_RESET_REASON_SUPPORTED_SOURCES_SUPERVISOR  = BIT4

EFI_ACPI_6_5_PHAT_RESET_REASON_SOURCES_UNKNOWN     = BIT0
EFI_ACPI_6_5_PHAT_RESET_REASON_SOURCES_HARDWARE    = BIT1
EFI_ACPI_6_5_PHAT_RESET_REASON_SOURCES_FIRMWARE    = BIT2
EFI_ACPI_6_5_PHAT_RESET_REASON_SOURCES_SOFTWARE    = BIT3
EFI_ACPI_6_5_PHAT_RESET_REASON_SOURCES_SUPERVISOR  = BIT4

EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_UNKNOWN            = 0x00
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_COLD_BOOT          = 0x01
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_COLD_RESET         = 0x02
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_WARM_RESET         = 0x03
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_UPDATE             = 0x04
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_UNEXPECTED_RESET   = 0x20
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_FAULT              = 0x21
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_TIMEOUT            = 0x22
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_THERMAL            = 0x23
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_POWER_LOSS         = 0x24
EFI_ACPI_6_5_PHAT_RESET_REASON_REASON_POWER_BUTTON       = 0x25

EFI_ACPI_6_5_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = EFI_ACPI_6_4_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE
EFI_ACPI_6_5_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_ARM_PERFORMANCE_MONITORING_UNIT_TABLE_SIGNATURE  = SIGNATURE_32('A', 'P', 'M', 'T')
EFI_ACPI_6_5_BOOT_ERROR_RECORD_TABLE_SIGNATURE  = EFI_ACPI_6_4_BOOT_ERROR_RECORD_TABLE_SIGNATURE
EFI_ACPI_6_5_BOOT_GRAPHICS_RESOURCE_TABLE_SIGNATURE  = EFI_ACPI_6_4_BOOT_GRAPHICS_RESOURCE_TABLE_SIGNATURE
EFI_ACPI_6_5_COMPONENT_DISTANCE_INFORMATION_TABLE_SIGNATURE  = SIGNATURE_32('C', 'D', 'I', 'T')
EFI_ACPI_6_5_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE  = EFI_ACPI_6_4_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE
EFI_ACPI_6_5_COMPONENT_RESOURCE_ATTRIBUTE_TABLE_SIGNATURE  = SIGNATURE_32('C', 'R', 'A', 'T')
EFI_ACPI_6_5_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  = EFI_ACPI_6_4_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE
EFI_ACPI_6_5_ERROR_INJECTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_ERROR_INJECTION_TABLE_SIGNATURE
EFI_ACPI_6_5_ERROR_RECORD_SERIALIZATION_TABLE_SIGNATURE  = EFI_ACPI_6_4_ERROR_RECORD_SERIALIZATION_TABLE_SIGNATURE
EFI_ACPI_6_5_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = EFI_ACPI_6_4_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE
EFI_ACPI_6_5_FIRMWARE_PERFORMANCE_DATA_TABLE_SIGNATURE  = EFI_ACPI_6_4_FIRMWARE_PERFORMANCE_DATA_TABLE_SIGNATURE
EFI_ACPI_6_5_GENERIC_TIMER_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_GENERIC_TIMER_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_HARDWARE_ERROR_SOURCE_TABLE_SIGNATURE  = EFI_ACPI_6_4_HARDWARE_ERROR_SOURCE_TABLE_SIGNATURE
EFI_ACPI_6_5_HETEROGENEOUS_MEMORY_ATTRIBUTE_TABLE_SIGNATURE  = SIGNATURE_32('H', 'M', 'A', 'T')
EFI_ACPI_6_5_MEMORY_POWER_STATE_TABLE_SIGNATURE  = EFI_ACPI_6_4_MEMORY_POWER_STATE_TABLE_SIGNATURE
EFI_ACPI_6_5_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_SIGNATURE  = EFI_ACPI_6_4_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_SIGNATURE
EFI_ACPI_6_5_NVDIMM_FIRMWARE_INTERFACE_TABLE_STRUCTURE_SIGNATURE  = SIGNATURE_32('N', 'F', 'I', 'T')
EFI_ACPI_6_5_PLATFORM_DEBUG_TRIGGER_TABLE_STRUCTURE_SIGNATURE  = SIGNATURE_32('P', 'D', 'T', 'T')
EFI_ACPI_6_5_PLATFORM_MEMORY_TOPOLOGY_TABLE_SIGNATURE  = SIGNATURE_32('P', 'M', 'T', 'T')
EFI_ACPI_6_5_PROCESSOR_PROPERTIES_TOPOLOGY_TABLE_STRUCTURE_SIGNATURE  = SIGNATURE_32('P', 'P', 'T', 'T')
EFI_ACPI_6_5_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('P', 'S', 'D', 'T')
EFI_ACPI_6_5_ACPI_RAS2_FEATURE_TABLE_SIGNATURE  = SIGNATURE_32('R', 'A', 'S', '2')
EFI_ACPI_6_5_ACPI_RAS_FEATURE_TABLE_SIGNATURE  = SIGNATURE_32('R', 'A', 'S', 'F')
EFI_ACPI_6_5_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32('R', 'S', 'D', 'T')
EFI_ACPI_6_5_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'B', 'S', 'T')
EFI_ACPI_6_5_SECURE_DEVICES_TABLE_SIGNATURE  = SIGNATURE_32('S', 'D', 'E', 'V')
EFI_ACPI_6_5_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  = SIGNATURE_32('S', 'L', 'I', 'T')
EFI_ACPI_6_5_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE  = SIGNATURE_32('S', 'R', 'A', 'T')
EFI_ACPI_6_5_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  = EFI_ACPI_6_4_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE
EFI_ACPI_6_5_CORE_SYSTEM_RESOURCE_TABLE_SIGNATURE  = EFI_ACPI_6_4_CORE_SYSTEM_RESOURCE_TABLE_SIGNATURE
EFI_ACPI_6_5_DEBUG_PORT_2_TABLE_SIGNATURE  = EFI_ACPI_6_4_DEBUG_PORT_2_TABLE_SIGNATURE
EFI_ACPI_6_5_DEBUG_PORT_TABLE_SIGNATURE  = EFI_ACPI_6_4_DEBUG_PORT_TABLE_SIGNATURE
EFI_ACPI_6_5_DMA_REMAPPING_TABLE_SIGNATURE  = EFI_ACPI_6_4_DMA_REMAPPING_TABLE_SIGNATURE
EFI_ACPI_6_5_DYNAMIC_ROOT_OF_TRUST_FOR_MEASUREMENT_TABLE_SIGNATURE  = EFI_ACPI_6_4_DYNAMIC_ROOT_OF_TRUST_FOR_MEASUREMENT_TABLE_SIGNATURE
EFI_ACPI_6_5_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE  = EFI_ACPI_6_4_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE
EFI_ACPI_6_5_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE  = EFI_ACPI_6_4_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE
EFI_ACPI_6_5_INTERRUPT_SOURCE_OVERRIDE_SIGNATURE  = SIGNATURE_32('I', 'O', 'R', 'T')
EFI_ACPI_6_5_IO_VIRTUALIZATION_REPORTING_STRUCTURE_SIGNATURE  = EFI_ACPI_6_4_IO_VIRTUALIZATION_REPORTING_STRUCTURE_SIGNATURE
EFI_ACPI_6_5_LOW_POWER_IDLE_TABLE_STRUCTURE_SIGNATURE  = EFI_ACPI_6_4_LOW_POWER_IDLE_TABLE_STRUCTURE_SIGNATURE
EFI_ACPI_6_5_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_6_5_MANAGEMENT_CONTROLLER_HOST_INTERFACE_TABLE_SIGNATURE  = EFI_ACPI_6_4_MANAGEMENT_CONTROLLER_HOST_INTERFACE_TABLE_SIGNATURE
EFI_ACPI_6_5_DATA_MANAGEMENT_TABLE_SIGNATURE  = EFI_ACPI_6_4_DATA_MANAGEMENT_TABLE_SIGNATURE
EFI_ACPI_6_5_PLATFORM_COMMUNICATIONS_CHANNEL_TABLE_SIGNATURE  = SIGNATURE_32('P', 'C', 'C', 'T')
EFI_ACPI_6_5_PLATFORM_HEALTH_ASSESSMENT_TABLE_SIGNATURE  = SIGNATURE_32('P', 'H', 'A', 'T')

EFI_ACPI_6_5_SOFTWARE_DELEGATED_EXCEPTIONS_INTERFACE_TABLE_SIGNATURE  = SIGNATURE_32('S', 'D', 'E', 'I')
EFI_ACPI_6_5_SOFTWARE_LICENSING_TABLE_SIGNATURE  = EFI_ACPI_6_4_SOFTWARE_LICENSING_TABLE_SIGNATURE
EFI_ACPI_6_5_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE
EFI_ACPI_6_5_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE  = EFI_ACPI_6_4_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE
EFI_ACPI_6_5_STA_OVERRIDE_TABLE_SIGNATURE  = SIGNATURE_32('S', 'T', 'A', 'O')
EFI_ACPI_6_5_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE  = EFI_ACPI_6_4_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE
EFI_ACPI_6_5_TRUSTED_COMPUTING_PLATFORM_2_TABLE_SIGNATURE  = EFI_ACPI_6_4_TRUSTED_COMPUTING_PLATFORM_2_TABLE_SIGNATURE
EFI_ACPI_6_5_UEFI_ACPI_DATA_TABLE_SIGNATURE  = EFI_ACPI_6_4_UEFI_ACPI_DATA_TABLE_SIGNATURE
EFI_ACPI_6_5_WINDOWS_ACPI_EMULATED_DEVICES_TABLE_SIGNATURE  = EFI_ACPI_6_4_WINDOWS_ACPI_EMULATED_DEVICES_TABLE_SIGNATURE
EFI_ACPI_6_5_WATCHDOG_ACTION_TABLE_SIGNATURE  = EFI_ACPI_6_4_WATCHDOG_ACTION_TABLE_SIGNATURE
EFI_ACPI_6_5_WATCHDOG_RESOURCE_TABLE_SIGNATURE  = EFI_ACPI_6_4_WATCHDOG_RESOURCE_TABLE_SIGNATURE
EFI_ACPI_6_5_PLATFORM_BINARY_TABLE_SIGNATURE  = EFI_ACPI_6_4_PLATFORM_BINARY_TABLE_SIGNATURE
EFI_ACPI_6_5_WINDOWS_SMM_SECURITY_MITIGATION_TABLE_SIGNATURE  = SIGNATURE_32('W', 'S', 'M', 'T')
EFI_ACPI_6_5_XEN_PROJECT_TABLE_SIGNATURE  = SIGNATURE_32('X', 'E', 'N', 'V')
EFI_ACPI_MEMORY_SYSTEM_RESOURCE_PARTITIONING_AND_MONITORING_TABLE_SIGNATURE  = SIGNATURE_32('M', 'P', 'A', 'M')

