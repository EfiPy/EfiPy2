# Acpi40.py
#
# EfiPy2.MdePkg.IndustryStandard.Acpi40
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.Acpi30 import *

EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE = EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE

EFI_ACPI_4_0_SYSTEM_MEMORY              = 0
EFI_ACPI_4_0_SYSTEM_IO                  = 1
EFI_ACPI_4_0_PCI_CONFIGURATION_SPACE    = 2
EFI_ACPI_4_0_EMBEDDED_CONTROLLER        = 3
EFI_ACPI_4_0_SMBUS                      = 4
EFI_ACPI_4_0_FUNCTIONAL_FIXED_HARDWARE  = 0x7F

EFI_ACPI_4_0_UNDEFINED  = 0
EFI_ACPI_4_0_BYTE       = 1
EFI_ACPI_4_0_WORD       = 2
EFI_ACPI_4_0_DWORD      = 3
EFI_ACPI_4_0_QWORD      = 4

EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER = EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER

EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION = 0x02

EFI_ACPI_4_0_COMMON_HEADER = EFI_ACPI_3_0_COMMON_HEADER

EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_4_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE = EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE

EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x04

EFI_ACPI_4_0_PM_PROFILE_UNSPECIFIED         = 0
EFI_ACPI_4_0_PM_PROFILE_DESKTOP             = 1
EFI_ACPI_4_0_PM_PROFILE_MOBILE              = 2
EFI_ACPI_4_0_PM_PROFILE_WORKSTATION         = 3
EFI_ACPI_4_0_PM_PROFILE_ENTERPRISE_SERVER   = 4
EFI_ACPI_4_0_PM_PROFILE_SOHO_SERVER         = 5
EFI_ACPI_4_0_PM_PROFILE_APPLIANCE_PC        = 6
EFI_ACPI_4_0_PM_PROFILE_PERFORMANCE_SERVER  = 7

EFI_ACPI_4_0_LEGACY_DEVICES              = BIT0
EFI_ACPI_4_0_8042                        = BIT1
EFI_ACPI_4_0_VGA_NOT_PRESENT             = BIT2
EFI_ACPI_4_0_MSI_NOT_SUPPORTED           = BIT3
EFI_ACPI_4_0_PCIE_ASPM_CONTROLS          = BIT4

EFI_ACPI_4_0_WBINVD                                 = BIT0
EFI_ACPI_4_0_WBINVD_FLUSH                           = BIT1
EFI_ACPI_4_0_PROC_C1                                = BIT2
EFI_ACPI_4_0_P_LVL2_UP                              = BIT3
EFI_ACPI_4_0_PWR_BUTTON                             = BIT4
EFI_ACPI_4_0_SLP_BUTTON                             = BIT5
EFI_ACPI_4_0_FIX_RTC                                = BIT6
EFI_ACPI_4_0_RTC_S4                                 = BIT7
EFI_ACPI_4_0_TMR_VAL_EXT                            = BIT8
EFI_ACPI_4_0_DCK_CAP                                = BIT9
EFI_ACPI_4_0_RESET_REG_SUP                          = BIT10
EFI_ACPI_4_0_SEALED_CASE                            = BIT11
EFI_ACPI_4_0_HEADLESS                               = BIT12
EFI_ACPI_4_0_CPU_SW_SLP                             = BIT13
EFI_ACPI_4_0_PCI_EXP_WAK                            = BIT14
EFI_ACPI_4_0_USE_PLATFORM_CLOCK                     = BIT15
EFI_ACPI_4_0_S4_RTC_STS_VALID                       = BIT16
EFI_ACPI_4_0_REMOTE_POWER_ON_CAPABLE                = BIT17
EFI_ACPI_4_0_FORCE_APIC_CLUSTER_MODEL               = BIT18
EFI_ACPI_4_0_FORCE_APIC_PHYSICAL_DESTINATION_MODE   = BIT19

class EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",             UINT32),
    ("Length",                UINT32),
    ("HardwareSignature",     UINT32),
    ("FirmwareWakingVector",  UINT32),
    ("GlobalLock",            UINT32),
    ("Flags",                 UINT32),
    ("XFirmwareWakingVector", UINT64),
    ("Version",               UINT8),
    ("Reserved0",             UINT8 * 3),
    ("OspmFlags",             UINT32),
    ("Reserved1",             UINT8 * 24),
  ]

EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  = 0x02

EFI_ACPI_4_0_S4BIOS_F                     = BIT0
EFI_ACPI_4_0_64BIT_WAKE_SUPPORTED_F       = BIT1

EFI_ACPI_4_0_OSPM_64BIT_WAKE__F           = BIT0

EFI_ACPI_4_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_REVISION   = 0x02
EFI_ACPI_4_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_REVISION        = 0x02

EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER = EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER

EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x03

EFI_ACPI_4_0_PCAT_COMPAT         = BIT0

EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC           = 0x00
EFI_ACPI_4_0_IO_APIC                        = 0x01
EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE      = 0x02
EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
EFI_ACPI_4_0_LOCAL_APIC_NMI                 = 0x04
EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE    = 0x05
EFI_ACPI_4_0_IO_SAPIC                       = 0x06
EFI_ACPI_4_0_LOCAL_SAPIC                    = 0x07
EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES     = 0x08
EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC         = 0x09
EFI_ACPI_4_0_LOCAL_X2APIC_NMI               = 0x0A

EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_STRUCTURE = EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC_STRUCTURE

EFI_ACPI_4_0_LOCAL_APIC_ENABLED        = BIT0

EFI_ACPI_4_0_IO_APIC_STRUCTURE = EFI_ACPI_3_0_IO_APIC_STRUCTURE

EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE = EFI_ACPI_3_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE

EFI_ACPI_4_0_PLATFORM_INTERRUPT_APIC_STRUCTURE = EFI_ACPI_3_0_PLATFORM_INTERRUPT_APIC_STRUCTURE

EFI_ACPI_4_0_POLARITY      = (3 << 0)
EFI_ACPI_4_0_TRIGGER_MODE  = (3 << 2)

EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE = EFI_ACPI_3_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE

EFI_ACPI_4_0_LOCAL_APIC_NMI_STRUCTURE = EFI_ACPI_3_0_LOCAL_APIC_NMI_STRUCTURE

EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE = EFI_ACPI_3_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE

EFI_ACPI_4_0_IO_SAPIC_STRUCTURE = EFI_ACPI_3_0_IO_SAPIC_STRUCTURE

EFI_ACPI_4_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE = EFI_ACPI_3_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE

EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE = EFI_ACPI_3_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE

EFI_ACPI_4_0_CPEI_PROCESSOR_OVERRIDE          = BIT0

class EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("Reserved",          UINT8 * 2),
    ("X2ApicId",          UINT32),
    ("Flags",             UINT32),
    ("AcpiProcessorUid",  UINT32)
  ]

class EFI_ACPI_4_0_LOCAL_X2APIC_NMI_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("Flags",             UINT16),
    ("AcpiProcessorUid",  UINT32),
    ("LocalX2ApicLint",   UINT8),
    ("Reserved",          UINT8 * 3)
  ]

EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE = EFI_ACPI_3_0_SMART_BATTERY_DESCRIPTION_TABLE

EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE_REVISION = 0x01

EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE = EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE

EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  = EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION

EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER = EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER

EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_REVISION  = 0x03

EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY  = 0x00
EFI_ACPI_4_0_MEMORY_AFFINITY                      = 0x01
EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY      = 0x02

class EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Length",                UINT8),
    ("ProximityDomain7To0",   UINT8),
    ("ApicId",                UINT8),
    ("Flags",                 UINT32),
    ("LocalSapicEid",         UINT8),
    ("ProximityDomain31To8",  UINT8 * 3),
    ("ClockDomain",           UINT32)
  ]

EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_ENABLED = (1 << 0)

EFI_ACPI_4_0_MEMORY_AFFINITY_STRUCTURE = EFI_ACPI_3_0_MEMORY_AFFINITY_STRUCTURE

EFI_ACPI_4_0_MEMORY_ENABLED       = (1 << 0)
EFI_ACPI_4_0_MEMORY_HOT_PLUGGABLE = (1 << 1)
EFI_ACPI_4_0_MEMORY_NONVOLATILE   = (1 << 2)

class EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Reserved1",       UINT8 * 2),
    ("ProximityDomain", UINT32),
    ("X2ApicId",        UINT32),
    ("Flags",           UINT32),
    ("ClockDomain",     UINT32),
    ("Reserved2",       UINT8 * 4)
  ]

EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER = EFI_ACPI_3_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER

EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_REVISION  = 0x01

class EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",  UINT8 * 8)
  ]

EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_REVISION = 0x01

EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC  = 0x00

class EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("ProcessorId",     UINT8),
    ("ProcessorEid",    UINT8),
    ("PollingInterval", UINT32)
  ]

class EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          EFI_ACPI_DESCRIPTION_HEADER),
    ("OffsetProxDomInfo",               UINT32),
    ("MaximumNumberOfProximityDomains", UINT32),
    ("MaximumNumberOfClockDomains",     UINT32),
    ("MaximumPhysicalAddress",          UINT64)
  ]

EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_REVISION = 0x01

class EFI_ACPI_4_0_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Revision",                  UINT8),
    ("Length",                    UINT8),
    ("ProximityDomainRangeLow",   UINT32),
    ("ProximityDomainRangeHigh",  UINT32),
    ("MaximumProcessorCapacity",  UINT32),
    ("MaximumMemoryCapacity",     UINT64)
  ]

class EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("BootErrorRegionLength",   UINT32),
    ("BootErrorRegion",         UINT64)
  ]

EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_REVISION = 0x01

class EFI_ACPI_4_0_ERROR_BLOCK_STATUS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UncorrectableErrorValid",     UINT32, 1),
    ("CorrectableErrorValid",       UINT32, 1),
    ("MultipleUncorrectableErrors", UINT32, 1),
    ("MultipleCorrectableErrors",   UINT32, 1),
    ("ErrorDataEntryCount",         UINT32, 10),
    ("Reserved",                    UINT32, 18)
  ]

class EFI_ACPI_4_0_BOOT_ERROR_REGION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlockStatus",   EFI_ACPI_4_0_ERROR_BLOCK_STATUS),
    ("RawDataOffset", UINT32),
    ("RawDataLength", UINT32),
    ("DataLength",    UINT32),
    ("ErrorSeverity", UINT32)
  ]

EFI_ACPI_4_0_ERROR_SEVERITY_CORRECTABLE  = 0x00
EFI_ACPI_4_0_ERROR_SEVERITY_FATAL        = 0x01
EFI_ACPI_4_0_ERROR_SEVERITY_CORRECTED    = 0x02
EFI_ACPI_4_0_ERROR_SEVERITY_NONE         = 0x03

class EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionType",     UINT8 * 16),
    ("ErrorSeverity",   UINT32),
    ("Revision",        UINT16),
    ("ValidationBits",  UINT8),
    ("Flags",           UINT8),
    ("ErrorDataLength", UINT32),
    ("FruId",           UINT8 * 16),
    ("FruText",         UINT8 * 20)
  ]

EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_REVISION  = 0x0201

class EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_ACPI_DESCRIPTION_HEADER),
    ("ErrorSourceCount",  UINT32)
  ]

EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_REVISION = 0x01

EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION  = 0x00
EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK  = 0x01
EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR                = 0x02
EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER                  = 0x06
EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER                     = 0x07
EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER                     = 0x08
EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR                     = 0x09

EFI_ACPI_4_0_ERROR_SOURCE_FLAG_FIRMWARE_FIRST       = (1 << 0)
EFI_ACPI_4_0_ERROR_SOURCE_FLAG_GLOBAL               = (1 << 1)

class EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("Reserved0",                     UINT8 * 2),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("GlobalCapabilityInitData",      UINT64),
    ("GlobalCapabilityInitData",      UINT64),
    ("NumberOfHardwareBanks",         UINT8),
    ("Reserved1",                     UINT8 * 7)
  ]

class EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BankNumber",                    UINT8),
    ("ClearStatusOnInitialization",   UINT8),
    ("StatusDataFormat",              UINT8),
    ("Reserved0",                     UINT8),
    ("ControlRegisterMsrAddress",     UINT32),
    ("ControlInitData",               UINT64),
    ("StatusRegisterMsrAddress",      UINT32),
    ("AddressRegisterMsrAddress",     UINT32),
    ("MiscRegisterMsrAddress",        UINT32)
  ]

EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_IA32      = 0x00
EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_INTEL64   = 0x01
EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_AMD64     = 0x02

EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_POLLED                = 0x00
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_EXTERNAL_INTERRUPT    = 0x01
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_LOCAL_INTERRUPT       = 0x02
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_SCI                   = 0x03
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_NMI                   = 0x04

class EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT16, 1),
    ("PollInterval",                    UINT16, 1),
    ("SwitchToPollingThresholdValue",   UINT16, 1),
    ("SwitchToPollingThresholdWindow",  UINT16, 1),
    ("ErrorThresholdValue",             UINT16, 1),
    ("ErrorThresholdWindow",            UINT16, 1),
    ("Reserved",                        UINT16, 10)
  ]

class EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT8),
    ("Length",                        UINT8),
    ("ConfigurationWriteEnable",      EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE),
    ("PollInterval",                  UINT32),
    ("Vector",                        UINT32),
    ("SwitchToPollingThresholdValue", UINT32),
    ("SwitchToPollingThresholdWindow",UINT32),
    ("ErrorThresholdValue",           UINT32),
    ("ErrorThresholdWindow",          UINT32)
  ]

class EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("Reserved0",                     UINT8 * 2),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("NotificationStructure",         EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("NumberOfHardwareBanks",         UINT8),
    ("Reserved1",                     UINT8 * 3)
  ]

class EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("Reserved0",                     UINT8 * 2),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("MaxRawDataLength",              UINT32)
  ]

class EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("SourceId",                            UINT16),
    ("Reserved0",                           UINT8 * 2),
    ("Flags",                               UINT8),
    ("Enabled",                             UINT8),
    ("NumberOfRecordsToPreAllocate",        UINT32),
    ("MaxSectionsPerRecord",                UINT32),
    ("Bus",                                 UINT32),
    ("Device",                              UINT16),
    ("Function",                            UINT16),
    ("DeviceControl",                       UINT16),
    ("Reserved1",                           UINT8 * 2),
    ("UncorrectableErrorMask",              UINT32),
    ("UncorrectableErrorSeverity",          UINT32),
    ("CorrectableErrorMask",                UINT32),
    ("AdvancedErrorCapabilitiesAndControl", UINT32),
    ("RootErrorCommand",                    UINT32)
  ]

class EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("SourceId",                            UINT16),
    ("Reserved0",                           UINT8 * 2),
    ("Flags",                               UINT8),
    ("Enabled",                             UINT8),
    ("NumberOfRecordsToPreAllocate",        UINT32),
    ("MaxSectionsPerRecord",                UINT32),
    ("Bus",                                 UINT32),
    ("Device",                              UINT16),
    ("Function",                            UINT16),
    ("DeviceControl",                       UINT16),
    ("Reserved1",                           UINT8 * 2),
    ("UncorrectableErrorMask",              UINT32),
    ("UncorrectableErrorSeverity",          UINT32),
    ("CorrectableErrorMask",                UINT32),
    ("AdvancedErrorCapabilitiesAndControl", UINT32)
  ]

class EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                          UINT16),
    ("SourceId",                                      UINT16),
    ("Reserved0",                                     UINT8 * 2),
    ("Flags",                                         UINT8),
    ("Enabled",                                       UINT8),
    ("NumberOfRecordsToPreAllocate",                  UINT32),
    ("MaxSectionsPerRecord",                          UINT32),
    ("Bus",                                           UINT32),
    ("Device",                                        UINT16),
    ("Function",                                      UINT16),
    ("DeviceControl",                                 UINT16),
    ("Reserved1",                                     UINT8 * 2),
    ("UncorrectableErrorMask",                        UINT32),
    ("UncorrectableErrorSeverity",                    UINT32),
    ("CorrectableErrorMask",                          UINT32),
    ("AdvancedErrorCapabilitiesAndControl",           UINT32),
    ("SecondaryUncorrectableErrorMask",               UINT32),
    ("SecondaryUncorrectableErrorSeverity",           UINT32),
    ("SecondaryAdvancedErrorCapabilitiesAndControl",  UINT32)
  ]

class EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR_SOURCE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("RelatedSourceId",               UINT16),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("MaxRawDataLength",              UINT32),
    ("ErrorStatusAddress",            EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE),
    ("NotificationStructure",         EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("ErrorStatusBlockLength",        UINT32)
  ]

class EFI_ACPI_4_0_GENERIC_ERROR_STATUS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlockStatus",     EFI_ACPI_4_0_ERROR_BLOCK_STATUS),
    ("RawDataOffset",   UINT32),
    ("RawDataLength",   UINT32),
    ("DataLength",      UINT32),
    ("ErrorSeverity",   UINT32)
  ]

class EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("SerializationHeaderSize", UINT32),
    ("Reserved0",               UINT8 * 4),
    ("InstructionEntryCount",   UINT32)
  ]

EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_REVISION = 0x01

EFI_ACPI_4_0_ERST_BEGIN_WRITE_OPERATION                    = 0x00
EFI_ACPI_4_0_ERST_BEGIN_READ_OPERATION                     = 0x01
EFI_ACPI_4_0_ERST_BEGIN_CLEAR_OPERATION                    = 0x02
EFI_ACPI_4_0_ERST_END_OPERATION                            = 0x03
EFI_ACPI_4_0_ERST_SET_RECORD_OFFSET                        = 0x04
EFI_ACPI_4_0_ERST_EXECUTE_OPERATION                        = 0x05
EFI_ACPI_4_0_ERST_CHECK_BUSY_STATUS                        = 0x06
EFI_ACPI_4_0_ERST_GET_COMMAND_STATUS                       = 0x07
EFI_ACPI_4_0_ERST_GET_RECORD_IDENTIFIER                    = 0x08
EFI_ACPI_4_0_ERST_SET_RECORD_IDENTIFIER                    = 0x09
EFI_ACPI_4_0_ERST_GET_RECORD_COUNT                         = 0x0A
EFI_ACPI_4_0_ERST_BEGIN_DUMMY_WRITE_OPERATION              = 0x0B
EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE              = 0x0D
EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_LENGTH       = 0x0E
EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_ATTRIBUTES   = 0x0F

EFI_ACPI_4_0_EINJ_STATUS_SUCCESS                           = 0x00
EFI_ACPI_4_0_EINJ_STATUS_NOT_ENOUGH_SPACE                  = 0x01
EFI_ACPI_4_0_EINJ_STATUS_HARDWARE_NOT_AVAILABLE            = 0x02
EFI_ACPI_4_0_EINJ_STATUS_FAILED                            = 0x03
EFI_ACPI_4_0_EINJ_STATUS_RECORD_STORE_EMPTY                = 0x04
EFI_ACPI_4_0_EINJ_STATUS_RECORD_NOT_FOUND                  = 0x05

EFI_ACPI_4_0_ERST_READ_REGISTER                            = 0x00
EFI_ACPI_4_0_ERST_READ_REGISTER_VALUE                      = 0x01
EFI_ACPI_4_0_ERST_WRITE_REGISTER                           = 0x02
EFI_ACPI_4_0_ERST_WRITE_REGISTER_VALUE                     = 0x03
EFI_ACPI_4_0_ERST_NOOP                                     = 0x04
EFI_ACPI_4_0_ERST_LOAD_VAR1                                = 0x05
EFI_ACPI_4_0_ERST_LOAD_VAR2                                = 0x06
EFI_ACPI_4_0_ERST_STORE_VAR1                               = 0x07
EFI_ACPI_4_0_ERST_ADD                                      = 0x08
EFI_ACPI_4_0_ERST_SUBTRACT                                 = 0x09
EFI_ACPI_4_0_ERST_ADD_VALUE                                = 0x0A
EFI_ACPI_4_0_ERST_SUBTRACT_VALUE                           = 0x0B
EFI_ACPI_4_0_ERST_STALL                                    = 0x0C
EFI_ACPI_4_0_ERST_STALL_WHILE_TRUE                         = 0x0D
EFI_ACPI_4_0_ERST_SKIP_NEXT_INSTRUCTION_IF_TRUE            = 0x0E
EFI_ACPI_4_0_ERST_GOTO                                     = 0x0F
EFI_ACPI_4_0_ERST_SET_SRC_ADDRESS_BASE                     = 0x10
EFI_ACPI_4_0_ERST_SET_DST_ADDRESS_BASE                     = 0x11
EFI_ACPI_4_0_ERST_MOVE_DATA                                = 0x12

EFI_ACPI_4_0_ERST_PRESERVE_REGISTER                        = 0x01

class EFI_ACPI_4_0_ERST_SERIALIZATION_INSTRUCTION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SerializationAction", UINT8),
    ("Instruction",         UINT8),
    ("Flags",               UINT8),
    ("Reserved0",           UINT8),
    ("RegisterRegion",      EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE),
    ("Value",               UINT64),
    ("Mask",                UINT64)
  ]

class EFI_ACPI_4_0_ERROR_INJECTION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DESCRIPTION_HEADER),
    ("InjectionHeaderSize", UINT32),
    ("InjectionFlags",      UINT8),
    ("Reserved0",           UINT8 * 3),
    ("InjectionEntryCount", UINT32)
  ]

EFI_ACPI_4_0_ERROR_INJECTION_TABLE_REVISION = 0x01

EFI_ACPI_4_0_EINJ_BEGIN_INJECTION_OPERATION                = 0x00
EFI_ACPI_4_0_EINJ_GET_TRIGGER_ERROR_ACTION_TABLE           = 0x01
EFI_ACPI_4_0_EINJ_SET_ERROR_TYPE                           = 0x02
EFI_ACPI_4_0_EINJ_GET_ERROR_TYPE                           = 0x03
EFI_ACPI_4_0_EINJ_END_OPERATION                            = 0x04
EFI_ACPI_4_0_EINJ_EXECUTE_OPERATION                        = 0x05
EFI_ACPI_4_0_EINJ_CHECK_BUSY_STATUS                        = 0x06
EFI_ACPI_4_0_EINJ_GET_COMMAND_STATUS                       = 0x07
EFI_ACPI_4_0_EINJ_TRIGGER_ERROR                            = 0xFF

EFI_ACPI_4_0_EINJ_STATUS_SUCCESS                           = 0x00
EFI_ACPI_4_0_EINJ_STATUS_UNKNOWN_FAILURE                   = 0x01
EFI_ACPI_4_0_EINJ_STATUS_INVALID_ACCESS                    = 0x02

EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_CORRECTABLE                 = (1 << 0)
EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_NONFATAL      = (1 << 1)
EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_FATAL         = (1 << 2)
EFI_ACPI_4_0_EINJ_ERROR_MEMORY_CORRECTABLE                    = (1 << 3)
EFI_ACPI_4_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_NONFATAL         = (1 << 4)
EFI_ACPI_4_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_FATAL            = (1 << 5)
EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_CORRECTABLE               = (1 << 6)
EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_NONFATAL    = (1 << 7)
EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_FATAL       = (1 << 8)
EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_CORRECTABLE                  = (1 << 9)
EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_NONFATAL       = (1 << 10)
EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_FATAL          = (1 << 11)

EFI_ACPI_4_0_EINJ_READ_REGISTER                            = 0x00
EFI_ACPI_4_0_EINJ_READ_REGISTER_VALUE                      = 0x01
EFI_ACPI_4_0_EINJ_WRITE_REGISTER                           = 0x02
EFI_ACPI_4_0_EINJ_WRITE_REGISTER_VALUE                     = 0x03
EFI_ACPI_4_0_EINJ_NOOP                                     = 0x04

EFI_ACPI_4_0_EINJ_PRESERVE_REGISTER                        = 0x01

class EFI_ACPI_4_0_EINJ_INJECTION_INSTRUCTION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InjectionAction", UINT8),
    ("Instruction",     UINT8),
    ("Flags",           UINT8),
    ("Reserved0",       UINT8),
    ("RegisterRegion",  EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE),
    ("Value",           UINT64),
    ("Mask",            UINT64)
  ]

class EFI_ACPI_4_0_EINJ_TRIGGER_ACTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeaderSize",  UINT32),
    ("Revision",    UINT32),
    ("TableSize",   UINT32),
    ("EntryCount",  UINT32)
  ]

EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE
EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_SIGNATURE  = SIGNATURE_32('B', 'E', 'R', 'T')
EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE  = EFI_ACPI_3_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE
EFI_ACPI_4_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  = EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE
EFI_ACPI_4_0_ERROR_INJECTION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'I', 'N', 'J')
EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'R', 'S', 'T')
EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = EFI_ACPI_3_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE
EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_SIGNATURE  = SIGNATURE_32('H', 'E', 'S', 'T')
EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_SIGNATURE  = SIGNATURE_32('M', 'S', 'C', 'T')
EFI_ACPI_4_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE
EFI_ACPI_4_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE
EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE  = EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE
EFI_ACPI_4_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  = EFI_ACPI_3_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE
EFI_ACPI_4_0_DEBUG_PORT_TABLE_SIGNATURE  = EFI_ACPI_3_0_DEBUG_PORT_TABLE_SIGNATURE
EFI_ACPI_4_0_DMA_REMAPPING_TABLE_SIGNATURE  = SIGNATURE_32('D', 'M', 'A', 'R')
EFI_ACPI_4_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE  = EFI_ACPI_3_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE
EFI_ACPI_4_0_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE  = SIGNATURE_32('i', 'B', 'F', 'T')
EFI_ACPI_4_0_IO_VIRTUALIZATION_REPORTING_STRUCTURE_SIGNATURE  = SIGNATURE_32('I', 'V', 'R', 'S')
EFI_ACPI_4_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE
EFI_ACPI_4_0_MANAGEMENT_CONTROLLER_HOST_INTERFACE_TABLE_SIGNATURE  = SIGNATURE_32('M', 'C', 'H', 'I')
EFI_ACPI_4_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE
EFI_ACPI_4_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE  = EFI_ACPI_3_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE
EFI_ACPI_4_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE  = EFI_ACPI_3_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE
EFI_ACPI_4_0_UEFI_ACPI_DATA_TABLE_SIGNATURE  = SIGNATURE_32('U', 'E', 'F', 'I')
EFI_ACPI_4_0_WINDOWS_ACPI_ENLIGHTENMENT_TABLE_SIGNATURE  = SIGNATURE_32('W', 'A', 'E', 'T')
EFI_ACPI_4_0_WATCHDOG_ACTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_WATCHDOG_ACTION_TABLE_SIGNATURE
EFI_ACPI_4_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE  = EFI_ACPI_3_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE
