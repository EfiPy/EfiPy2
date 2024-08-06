# SmBios.py
#
# EfiPy2.MdePkg.IndustryStandard.SmBios
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

SMBIOS_HANDLE_RESERVED_BEGIN = 0xFF00

SMBIOS_HANDLE_PI_RESERVED = 0xFFFE

SMBIOS_STRING_MAX_LENGTH     = 64

SMBIOS_TABLE_MAX_LENGTH  = 0xFFFF

SMBIOS_3_0_TABLE_MAX_LENGTH  = 0xFFFFFFFF

SMBIOS_ANCHOR_STRING         = b"_SM_"
SMBIOS_ANCHOR_STRING_LENGTH  = 4

SMBIOS_3_0_ANCHOR_STRING         = b"_SM3_"
SMBIOS_3_0_ANCHOR_STRING_LENGTH  = 5

SMBIOS_TYPE_BIOS_INFORMATION                      = 0
SMBIOS_TYPE_SYSTEM_INFORMATION                    = 1
SMBIOS_TYPE_BASEBOARD_INFORMATION                 = 2
SMBIOS_TYPE_SYSTEM_ENCLOSURE                      = 3
SMBIOS_TYPE_PROCESSOR_INFORMATION                 = 4
SMBIOS_TYPE_MEMORY_CONTROLLER_INFORMATION         = 5
SMBIOS_TYPE_MEMORY_MODULE_INFORMATON              = 6
SMBIOS_TYPE_CACHE_INFORMATION                     = 7
SMBIOS_TYPE_PORT_CONNECTOR_INFORMATION            = 8
SMBIOS_TYPE_SYSTEM_SLOTS                          = 9
SMBIOS_TYPE_ONBOARD_DEVICE_INFORMATION            = 10
SMBIOS_TYPE_OEM_STRINGS                           = 11
SMBIOS_TYPE_SYSTEM_CONFIGURATION_OPTIONS          = 12
SMBIOS_TYPE_BIOS_LANGUAGE_INFORMATION             = 13
SMBIOS_TYPE_GROUP_ASSOCIATIONS                    = 14
SMBIOS_TYPE_SYSTEM_EVENT_LOG                      = 15
SMBIOS_TYPE_PHYSICAL_MEMORY_ARRAY                 = 16
SMBIOS_TYPE_MEMORY_DEVICE                         = 17
SMBIOS_TYPE_32BIT_MEMORY_ERROR_INFORMATION        = 18
SMBIOS_TYPE_MEMORY_ARRAY_MAPPED_ADDRESS           = 19
SMBIOS_TYPE_MEMORY_DEVICE_MAPPED_ADDRESS          = 20
SMBIOS_TYPE_BUILT_IN_POINTING_DEVICE              = 21
SMBIOS_TYPE_PORTABLE_BATTERY                      = 22
SMBIOS_TYPE_SYSTEM_RESET                          = 23
SMBIOS_TYPE_HARDWARE_SECURITY                     = 24
SMBIOS_TYPE_SYSTEM_POWER_CONTROLS                 = 25
SMBIOS_TYPE_VOLTAGE_PROBE                         = 26
SMBIOS_TYPE_COOLING_DEVICE                        = 27
SMBIOS_TYPE_TEMPERATURE_PROBE                     = 28
SMBIOS_TYPE_ELECTRICAL_CURRENT_PROBE              = 29
SMBIOS_TYPE_OUT_OF_BAND_REMOTE_ACCESS             = 30
SMBIOS_TYPE_BOOT_INTEGRITY_SERVICE                = 31
SMBIOS_TYPE_SYSTEM_BOOT_INFORMATION               = 32
SMBIOS_TYPE_64BIT_MEMORY_ERROR_INFORMATION        = 33
SMBIOS_TYPE_MANAGEMENT_DEVICE                     = 34
SMBIOS_TYPE_MANAGEMENT_DEVICE_COMPONENT           = 35
SMBIOS_TYPE_MANAGEMENT_DEVICE_THRESHOLD_DATA      = 36
SMBIOS_TYPE_MEMORY_CHANNEL                        = 37
SMBIOS_TYPE_IPMI_DEVICE_INFORMATION               = 38
SMBIOS_TYPE_SYSTEM_POWER_SUPPLY                   = 39
SMBIOS_TYPE_ADDITIONAL_INFORMATION                = 40
SMBIOS_TYPE_ONBOARD_DEVICES_EXTENDED_INFORMATION  = 41
SMBIOS_TYPE_MANAGEMENT_CONTROLLER_HOST_INTERFACE  = 42
SMBIOS_TYPE_TPM_DEVICE                            = 43
SMBIOS_TYPE_PROCESSOR_ADDITIONAL_INFORMATION      = 44
SMBIOS_TYPE_FIRMWARE_INVENTORY_INFORMATION        = 45
SMBIOS_TYPE_STRING_PROPERTY_INFORMATION           = 46

SMBIOS_TYPE_INACTIVE  = 0x007E

SMBIOS_TYPE_END_OF_TABLE  = 0x007F

SMBIOS_OEM_BEGIN  = 128
SMBIOS_OEM_END    = 255

SMBIOS_TYPE      = UINT8
SMBIOS_HANDLE    = UINT16

class SMBIOS_TABLE_ENTRY_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AnchorString",                UINT8 * SMBIOS_ANCHOR_STRING_LENGTH),
    ("EntryPointStructureChecksum", UINT8),
    ("EntryPointLength",            UINT8),
    ("MajorVersion",                UINT8),
    ("MinorVersion",                UINT8),
    ("MaxStructureSize",            UINT16),
    ("EntryPointRevision",          UINT8),
    ("FormattedArea",               UINT8 * 5),
    ("IntermediateAnchorString",    UINT8 * 5),
    ("IntermediateChecksum",        UINT8),
    ("TableLength",                 UINT16),
    ("TableAddress",                UINT32),
    ("NumberOfSmbiosStructures",    UINT16),
    ("SmbiosBcdRevision",           UINT8)
  ]

class SMBIOS_TABLE_3_0_ENTRY_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AnchorString",                UINT8 * SMBIOS_3_0_ANCHOR_STRING_LENGTH),
    ("EntryPointStructureChecksum", UINT8),
    ("EntryPointLength",            UINT8),
    ("MajorVersion",                UINT8),
    ("MinorVersion",                UINT8),
    ("DocRev",                      UINT8),
    ("EntryPointRevision",          UINT8),
    ("Reserved",                    UINT8),
    ("TableMaximumSize",            UINT32),
    ("TableAddress",                UINT64)
  ]

class SMBIOS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8),
    ("Length",  UINT8),
    ("Handle",  UINT16)
  ]

class SMBIOS_TABLE_STRING (UINT8):
  pass

class MISC_BIOS_CHARACTERISTICS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                        UINT32, 2),
    ("Unknown",                         UINT32, 1),
    ("BiosCharacteristicsNotSupported", UINT32, 1),
    ("IsaIsSupported",                  UINT32, 1),
    ("McaIsSupported",                  UINT32, 1),
    ("EisaIsSupported",                 UINT32, 1),
    ("PciIsSupported",                  UINT32, 1),
    ("PcmciaIsSupported",               UINT32, 1),
    ("PlugAndPlayIsSupported",          UINT32, 1),
    ("ApmIsSupported",                  UINT32, 1),
    ("BiosIsUpgradable",                UINT32, 1),
    ("BiosShadowingAllowed",            UINT32, 1),
    ("VlVesaIsSupported",               UINT32, 1),
    ("EscdSupportIsAvailable",          UINT32, 1),
    ("BootFromCdIsSupported",           UINT32, 1),
    ("SelectableBootIsSupported",       UINT32, 1),
    ("RomBiosIsSocketed",               UINT32, 1),
    ("BootFromPcmciaIsSupported",       UINT32, 1),
    ("EDDSpecificationIsSupported",     UINT32, 1),
    ("JapaneseNecFloppyIsSupported",    UINT32, 1),
    ("JapaneseToshibaFloppyIsSupported",UINT32, 1),
    ("Floppy525_360IsSupported",        UINT32, 1),
    ("Floppy525_12IsSupported",         UINT32, 1),
    ("Floppy35_720IsSupported",         UINT32, 1),
    ("Floppy35_288IsSupported",         UINT32, 1),
    ("PrintScreenIsSupported",          UINT32, 1),
    ("Keyboard8042IsSupported",         UINT32, 1),
    ("SerialIsSupported",               UINT32, 1),
    ("PrinterIsSupported",              UINT32, 1),
    ("CgaMonoIsSupported",              UINT32, 1),
    ("NecPc98",                         UINT32, 1),
    ("ReservedForVendor",               UINT32, 32)
  ]

class MBCE_BIOS_RESERVED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AcpiIsSupported",               UINT8, 1),
    ("UsbLegacyIsSupported",          UINT8, 1),
    ("AgpIsSupported",                UINT8, 1),
    ("I2OBootIsSupported",            UINT8, 1),
    ("Ls120BootIsSupported",          UINT8, 1),
    ("AtapiZipDriveBootIsSupported",  UINT8, 1),
    ("Boot1394IsSupported",           UINT8, 1),
    ("SmartBatteryIsSupported",       UINT8, 1)
  ]

class MBCE_SYSTEM_RESERVED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BiosBootSpecIsSupported",           UINT8, 1),
    ("FunctionKeyNetworkBootIsSupported", UINT8, 1),
    ("TargetContentDistributionEnabled",  UINT8, 1),
    ("UefiSpecificationSupported",        UINT8, 1),
    ("VirtualMachineSupported",           UINT8, 1),
    ("ManufacturingModeSupported",        UINT8, 1),
    ("ManufacturingModeEnabled",          UINT8, 1),
    ("ExtensionByte2Reserved",            UINT8, 1)
  ]

class MISC_BIOS_CHARACTERISTICS_EXTENSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BiosReserved",    MBCE_BIOS_RESERVED),
    ("SystemReserved",  MBCE_SYSTEM_RESERVED)
  ]

class EXTENDED_BIOS_ROM_SIZE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Size", UINT16, 14),
    ("Unit", UINT16, 2)
  ]

class SMBIOS_TABLE_TYPE0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                                     SMBIOS_STRUCTURE),
    ("Vendor",                                  SMBIOS_TABLE_STRING),
    ("BiosVersion",                             SMBIOS_TABLE_STRING),
    ("BiosSegment",                             UINT16),
    ("BiosReleaseDate",                         SMBIOS_TABLE_STRING),
    ("BiosSize",                                UINT8),
    ("BiosCharacteristics",                     MISC_BIOS_CHARACTERISTICS),
    ("BIOSCharacteristicsExtensionBytes",       UINT8 * 2),
    ("SystemBiosMajorRelease",                  UINT8),
    ("SystemBiosMinorRelease",                  UINT8),
    ("EmbeddedControllerFirmwareMajorRelease",  UINT8),
    ("EmbeddedControllerFirmwareMinorRelease",  UINT8)
  ]

SystemWakeupTypeReserved         = 0x00
SystemWakeupTypeOther            = 0x01
SystemWakeupTypeUnknown          = 0x02
SystemWakeupTypeApmTimer         = 0x03
SystemWakeupTypeModemRing        = 0x04
SystemWakeupTypeLanRemote        = 0x05
SystemWakeupTypePowerSwitch      = 0x06
SystemWakeupTypePciPme           = 0x07
SystemWakeupTypeAcPowerRestored  = 0x08
MISC_SYSTEM_WAKEUP_TYPE = ENUM

class SMBIOS_TABLE_TYPE1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",           SMBIOS_STRUCTURE),
    ("Manufacturer",  SMBIOS_TABLE_STRING),
    ("ProductName",   SMBIOS_TABLE_STRING),
    ("Version",       SMBIOS_TABLE_STRING),
    ("SerialNumber",  SMBIOS_TABLE_STRING),
    ("Uuid",          GUID),
    ("WakeUpType",    UINT8),
    ("SKUNumber",     SMBIOS_TABLE_STRING),
    ("Family",        SMBIOS_TABLE_STRING)
  ]

class BASE_BOARD_FEATURE_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Motherboard",           UINT8, 1),
    ("RequiresDaughterCard",  UINT8, 1),
    ("Removable",             UINT8, 1),
    ("Replaceable",           UINT8, 1),
    ("HotSwappable",          UINT8, 1),
    ("Reserved",              UINT8, 3)
  ]

BaseBoardTypeUnknown                  = 0x1
BaseBoardTypeOther                    = 0x2
BaseBoardTypeServerBlade              = 0x3
BaseBoardTypeConnectivitySwitch       = 0x4
BaseBoardTypeSystemManagementModule   = 0x5
BaseBoardTypeProcessorModule          = 0x6
BaseBoardTypeIOModule                 = 0x7
BaseBoardTypeMemoryModule             = 0x8
BaseBoardTypeDaughterBoard            = 0x9
BaseBoardTypeMotherBoard              = 0xA
BaseBoardTypeProcessorMemoryModule    = 0xB
BaseBoardTypeProcessorIOModule        = 0xC
BaseBoardTypeInterconnectBoard        = 0xD
BASE_BOARD_TYPE = ENUM

class SMBIOS_TABLE_TYPE2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                             SMBIOS_STRUCTURE),
    ("Manufacturer",                    SMBIOS_TABLE_STRING),
    ("ProductName",                     SMBIOS_TABLE_STRING),
    ("Version",                         SMBIOS_TABLE_STRING),
    ("SerialNumber",                    SMBIOS_TABLE_STRING),
    ("AssetTag",                        SMBIOS_TABLE_STRING),
    ("FeatureFlag",                     BASE_BOARD_FEATURE_FLAGS),
    ("LocationInChassis",               SMBIOS_TABLE_STRING),
    ("ChassisHandle",                   UINT16),
    ("BoardType",                       UINT8),
    ("NumberOfContainedObjectHandles",  UINT8),
    ("ContainedObjectHandles",          UINT16 * 1)
  ]

MiscChassisTypeOther               = 0x01
MiscChassisTypeUnknown             = 0x02
MiscChassisTypeDeskTop             = 0x03
MiscChassisTypeLowProfileDesktop   = 0x04
MiscChassisTypePizzaBox            = 0x05
MiscChassisTypeMiniTower           = 0x06
MiscChassisTypeTower               = 0x07
MiscChassisTypePortable            = 0x08
MiscChassisTypeLapTop              = 0x09
MiscChassisTypeNotebook            = 0x0A
MiscChassisTypeHandHeld            = 0x0B
MiscChassisTypeDockingStation      = 0x0C
MiscChassisTypeAllInOne            = 0x0D
MiscChassisTypeSubNotebook         = 0x0E
MiscChassisTypeSpaceSaving         = 0x0F
MiscChassisTypeLunchBox            = 0x10
MiscChassisTypeMainServerChassis   = 0x11
MiscChassisTypeExpansionChassis    = 0x12
MiscChassisTypeSubChassis          = 0x13
MiscChassisTypeBusExpansionChassis = 0x14
MiscChassisTypePeripheralChassis   = 0x15
MiscChassisTypeRaidChassis         = 0x16
MiscChassisTypeRackMountChassis    = 0x17
MiscChassisTypeSealedCasePc        = 0x18
MiscChassisMultiSystemChassis      = 0x19
MiscChassisCompactPCI              = 0x1A
MiscChassisAdvancedTCA             = 0x1B
MiscChassisBlade                   = 0x1C
MiscChassisBladeEnclosure          = 0x1D
MiscChassisTablet                  = 0x1E
MiscChassisConvertible             = 0x1F
MiscChassisDetachable              = 0x20
MiscChassisIoTGateway              = 0x21
MiscChassisEmbeddedPc              = 0x22
MiscChassisMiniPc                  = 0x23
MiscChassisStickPc                 = 0x24
MISC_CHASSIS_TYPE = ENUM

ChassisStateOther           = 0x01
ChassisStateUnknown         = 0x02
ChassisStateSafe            = 0x03
ChassisStateWarning         = 0x04
ChassisStateCritical        = 0x05
ChassisStateNonRecoverable  = 0x06
MISC_CHASSIS_STATE = ENUM

ChassisSecurityStatusOther                          = 0x01
ChassisSecurityStatusUnknown                        = 0x02
ChassisSecurityStatusNone                           = 0x03
ChassisSecurityStatusExternalInterfaceLockedOut     = 0x04
ChassisSecurityStatusExternalInterfaceLockedEnabled = 0x05
MISC_CHASSIS_SECURITY_STATE = ENUM

class CONTAINED_ELEMENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContainedElementType",    UINT8),
    ("ContainedElementMinimum", UINT8),
    ("ContainedElementMaximum", UINT8)
  ]

class SMBIOS_TABLE_TYPE3 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                           SMBIOS_STRUCTURE),
    ("Manufacturer",                  SMBIOS_TABLE_STRING),
    ("Type",                          UINT8),
    ("Version",                       SMBIOS_TABLE_STRING),
    ("SerialNumber",                  SMBIOS_TABLE_STRING),
    ("AssetTag",                      SMBIOS_TABLE_STRING),
    ("BootupState",                   UINT8),
    ("PowerSupplyState",              UINT8),
    ("ThermalState",                  UINT8),
    ("SecurityStatus",                UINT8),
    ("OemDefined",                    UINT8 * 4),
    ("Height",                        UINT8),
    ("NumberofPowerCords",            UINT8),
    ("ContainedElementCount",         UINT8),
    ("ContainedElementRecordLength",  UINT8),
    ("ContainedElements",             CONTAINED_ELEMENT * 1)
    # ("SKUNumber",                     SMBIOS_TABLE_STRING)
  ]

ProcessorOther   = 0x01
ProcessorUnknown = 0x02
CentralProcessor = 0x03
MathProcessor    = 0x04
DspProcessor     = 0x05
VideoProcessor   = 0x06
PROCESSOR_TYPE_DATA = ENUM

ProcessorFamilyOther                           = 0x01
ProcessorFamilyUnknown                         = 0x02
ProcessorFamily8086                            = 0x03
ProcessorFamily80286                           = 0x04
ProcessorFamilyIntel386                        = 0x05
ProcessorFamilyIntel486                        = 0x06
ProcessorFamily8087                            = 0x07
ProcessorFamily80287                           = 0x08
ProcessorFamily80387                           = 0x09
ProcessorFamily80487                           = 0x0A
ProcessorFamilyPentium                         = 0x0B
ProcessorFamilyPentiumPro                      = 0x0C
ProcessorFamilyPentiumII                       = 0x0D
ProcessorFamilyPentiumMMX                      = 0x0E
ProcessorFamilyCeleron                         = 0x0F
ProcessorFamilyPentiumIIXeon                   = 0x10
ProcessorFamilyPentiumIII                      = 0x11
ProcessorFamilyM1                              = 0x12
ProcessorFamilyM2                              = 0x13
ProcessorFamilyIntelCeleronM                   = 0x14
ProcessorFamilyIntelPentium4Ht                 = 0x15
ProcessorFamilyAmdDuron                        = 0x18
ProcessorFamilyK5                              = 0x19
ProcessorFamilyK6                              = 0x1A
ProcessorFamilyK6_2                            = 0x1B
ProcessorFamilyK6_3                            = 0x1C
ProcessorFamilyAmdAthlon                       = 0x1D
ProcessorFamilyAmd29000                        = 0x1E
ProcessorFamilyK6_2Plus                        = 0x1F
ProcessorFamilyPowerPC                         = 0x20
ProcessorFamilyPowerPC601                      = 0x21
ProcessorFamilyPowerPC603                      = 0x22
ProcessorFamilyPowerPC603Plus                  = 0x23
ProcessorFamilyPowerPC604                      = 0x24
ProcessorFamilyPowerPC620                      = 0x25
ProcessorFamilyPowerPCx704                     = 0x26
ProcessorFamilyPowerPC750                      = 0x27
ProcessorFamilyIntelCoreDuo                    = 0x28
ProcessorFamilyIntelCoreDuoMobile              = 0x29
ProcessorFamilyIntelCoreSoloMobile             = 0x2A
ProcessorFamilyIntelAtom                       = 0x2B
ProcessorFamilyIntelCoreM                      = 0x2C
ProcessorFamilyIntelCorem3                     = 0x2D
ProcessorFamilyIntelCorem5                     = 0x2E
ProcessorFamilyIntelCorem7                     = 0x2F
ProcessorFamilyAlpha                           = 0x30
ProcessorFamilyAlpha21064                      = 0x31
ProcessorFamilyAlpha21066                      = 0x32
ProcessorFamilyAlpha21164                      = 0x33
ProcessorFamilyAlpha21164PC                    = 0x34
ProcessorFamilyAlpha21164a                     = 0x35
ProcessorFamilyAlpha21264                      = 0x36
ProcessorFamilyAlpha21364                      = 0x37
ProcessorFamilyAmdTurionIIUltraDualCoreMobileM = 0x38
ProcessorFamilyAmdTurionIIDualCoreMobileM      = 0x39
ProcessorFamilyAmdAthlonIIDualCoreM            = 0x3A
ProcessorFamilyAmdOpteron6100Series            = 0x3B
ProcessorFamilyAmdOpteron4100Series            = 0x3C
ProcessorFamilyAmdOpteron6200Series            = 0x3D
ProcessorFamilyAmdOpteron4200Series            = 0x3E
ProcessorFamilyAmdFxSeries                     = 0x3F
ProcessorFamilyMips                            = 0x40
ProcessorFamilyMIPSR4000                       = 0x41
ProcessorFamilyMIPSR4200                       = 0x42
ProcessorFamilyMIPSR4400                       = 0x43
ProcessorFamilyMIPSR4600                       = 0x44
ProcessorFamilyMIPSR10000                      = 0x45
ProcessorFamilyAmdCSeries                      = 0x46
ProcessorFamilyAmdESeries                      = 0x47
ProcessorFamilyAmdASeries                      = 0x48 # SMBIOS spec 2.8.0 updated the name
ProcessorFamilyAmdGSeries                      = 0x49
ProcessorFamilyAmdZSeries                      = 0x4A
ProcessorFamilyAmdRSeries                      = 0x4B
ProcessorFamilyAmdOpteron4300                  = 0x4C
ProcessorFamilyAmdOpteron6300                  = 0x4D
ProcessorFamilyAmdOpteron3300                  = 0x4E
ProcessorFamilyAmdFireProSeries                = 0x4F
ProcessorFamilySparc                           = 0x50
ProcessorFamilySuperSparc                      = 0x51
ProcessorFamilymicroSparcII                    = 0x52
ProcessorFamilymicroSparcIIep                  = 0x53
ProcessorFamilyUltraSparc                      = 0x54
ProcessorFamilyUltraSparcII                    = 0x55
ProcessorFamilyUltraSparcIii                   = 0x56
ProcessorFamilyUltraSparcIII                   = 0x57
ProcessorFamilyUltraSparcIIIi                  = 0x58
ProcessorFamily68040                           = 0x60
ProcessorFamily68xxx                           = 0x61
ProcessorFamily68000                           = 0x62
ProcessorFamily68010                           = 0x63
ProcessorFamily68020                           = 0x64
ProcessorFamily68030                           = 0x65
ProcessorFamilyAmdAthlonX4QuadCore             = 0x66
ProcessorFamilyAmdOpteronX1000Series           = 0x67
ProcessorFamilyAmdOpteronX2000Series           = 0x68
ProcessorFamilyAmdOpteronASeries               = 0x69
ProcessorFamilyAmdOpteronX3000Series           = 0x6A
ProcessorFamilyAmdZen                          = 0x6B
ProcessorFamilyHobbit                          = 0x70
ProcessorFamilyCrusoeTM5000                    = 0x78
ProcessorFamilyCrusoeTM3000                    = 0x79
ProcessorFamilyEfficeonTM8000                  = 0x7A
ProcessorFamilyWeitek                          = 0x80
ProcessorFamilyItanium                         = 0x82
ProcessorFamilyAmdAthlon64                     = 0x83
ProcessorFamilyAmdOpteron                      = 0x84
ProcessorFamilyAmdSempron                      = 0x85
ProcessorFamilyAmdTurion64Mobile               = 0x86
ProcessorFamilyDualCoreAmdOpteron              = 0x87
ProcessorFamilyAmdAthlon64X2DualCore           = 0x88
ProcessorFamilyAmdTurion64X2Mobile             = 0x89
ProcessorFamilyQuadCoreAmdOpteron              = 0x8A
ProcessorFamilyThirdGenerationAmdOpteron       = 0x8B
ProcessorFamilyAmdPhenomFxQuadCore             = 0x8C
ProcessorFamilyAmdPhenomX4QuadCore             = 0x8D
ProcessorFamilyAmdPhenomX2DualCore             = 0x8E
ProcessorFamilyAmdAthlonX2DualCore             = 0x8F
ProcessorFamilyPARISC                          = 0x90
ProcessorFamilyPaRisc8500                      = 0x91
ProcessorFamilyPaRisc8000                      = 0x92
ProcessorFamilyPaRisc7300LC                    = 0x93
ProcessorFamilyPaRisc7200                      = 0x94
ProcessorFamilyPaRisc7100LC                    = 0x95
ProcessorFamilyPaRisc7100                      = 0x96
ProcessorFamilyV30                             = 0xA0
ProcessorFamilyQuadCoreIntelXeon3200Series     = 0xA1
ProcessorFamilyDualCoreIntelXeon3000Series     = 0xA2
ProcessorFamilyQuadCoreIntelXeon5300Series     = 0xA3
ProcessorFamilyDualCoreIntelXeon5100Series     = 0xA4
ProcessorFamilyDualCoreIntelXeon5000Series     = 0xA5
ProcessorFamilyDualCoreIntelXeonLV             = 0xA6
ProcessorFamilyDualCoreIntelXeonULV            = 0xA7
ProcessorFamilyDualCoreIntelXeon7100Series     = 0xA8
ProcessorFamilyQuadCoreIntelXeon5400Series     = 0xA9
ProcessorFamilyQuadCoreIntelXeon               = 0xAA
ProcessorFamilyDualCoreIntelXeon5200Series     = 0xAB
ProcessorFamilyDualCoreIntelXeon7200Series     = 0xAC
ProcessorFamilyQuadCoreIntelXeon7300Series     = 0xAD
ProcessorFamilyQuadCoreIntelXeon7400Series     = 0xAE
ProcessorFamilyMultiCoreIntelXeon7400Series    = 0xAF
ProcessorFamilyPentiumIIIXeon                  = 0xB0
ProcessorFamilyPentiumIIISpeedStep             = 0xB1
ProcessorFamilyPentium4                        = 0xB2
ProcessorFamilyIntelXeon                       = 0xB3
ProcessorFamilyAS400                           = 0xB4
ProcessorFamilyIntelXeonMP                     = 0xB5
ProcessorFamilyAMDAthlonXP                     = 0xB6
ProcessorFamilyAMDAthlonMP                     = 0xB7
ProcessorFamilyIntelItanium2                   = 0xB8
ProcessorFamilyIntelPentiumM                   = 0xB9
ProcessorFamilyIntelCeleronD                   = 0xBA
ProcessorFamilyIntelPentiumD                   = 0xBB
ProcessorFamilyIntelPentiumEx                  = 0xBC
ProcessorFamilyIntelCoreSolo                   = 0xBD # SMBIOS spec 2.6 updated this value
ProcessorFamilyReserved                        = 0xBE
ProcessorFamilyIntelCore2                      = 0xBF
ProcessorFamilyIntelCore2Solo                  = 0xC0
ProcessorFamilyIntelCore2Extreme               = 0xC1
ProcessorFamilyIntelCore2Quad                  = 0xC2
ProcessorFamilyIntelCore2ExtremeMobile         = 0xC3
ProcessorFamilyIntelCore2DuoMobile             = 0xC4
ProcessorFamilyIntelCore2SoloMobile            = 0xC5
ProcessorFamilyIntelCoreI7                     = 0xC6
ProcessorFamilyDualCoreIntelCeleron            = 0xC7
ProcessorFamilyIBM390                          = 0xC8
ProcessorFamilyG4                              = 0xC9
ProcessorFamilyG5                              = 0xCA
ProcessorFamilyG6                              = 0xCB
ProcessorFamilyzArchitecture                   = 0xCC
ProcessorFamilyIntelCoreI5                     = 0xCD
ProcessorFamilyIntelCoreI3                     = 0xCE
ProcessorFamilyIntelCoreI9                     = 0xCF
ProcessorFamilyViaC7M                          = 0xD2
ProcessorFamilyViaC7D                          = 0xD3
ProcessorFamilyViaC7                           = 0xD4
ProcessorFamilyViaEden                         = 0xD5
ProcessorFamilyMultiCoreIntelXeon              = 0xD6
ProcessorFamilyDualCoreIntelXeon3Series        = 0xD7
ProcessorFamilyQuadCoreIntelXeon3Series        = 0xD8
ProcessorFamilyViaNano                         = 0xD9
ProcessorFamilyDualCoreIntelXeon5Series        = 0xDA
ProcessorFamilyQuadCoreIntelXeon5Series        = 0xDB
ProcessorFamilyDualCoreIntelXeon7Series        = 0xDD
ProcessorFamilyQuadCoreIntelXeon7Series        = 0xDE
ProcessorFamilyMultiCoreIntelXeon7Series       = 0xDF
ProcessorFamilyMultiCoreIntelXeon3400Series    = 0xE0
ProcessorFamilyAmdOpteron3000Series            = 0xE4
ProcessorFamilyAmdSempronII                    = 0xE5
ProcessorFamilyEmbeddedAmdOpteronQuadCore      = 0xE6
ProcessorFamilyAmdPhenomTripleCore             = 0xE7
ProcessorFamilyAmdTurionUltraDualCoreMobile    = 0xE8
ProcessorFamilyAmdTurionDualCoreMobile         = 0xE9
ProcessorFamilyAmdAthlonDualCore               = 0xEA
ProcessorFamilyAmdSempronSI                    = 0xEB
ProcessorFamilyAmdPhenomII                     = 0xEC
ProcessorFamilyAmdAthlonII                     = 0xED
ProcessorFamilySixCoreAmdOpteron               = 0xEE
ProcessorFamilyAmdSempronM                     = 0xEF
ProcessorFamilyi860                            = 0xFA
ProcessorFamilyi960                            = 0xFB
ProcessorFamilyIndicatorFamily2                = 0xFE
ProcessorFamilyReserved1                       = 0xFF
PROCESSOR_FAMILY_DATA   = ENUM

ProcessorFamilyARMv7               = 0x0100
ProcessorFamilyARMv8               = 0x0101
ProcessorFamilyARMv9               = 0x0102
ProcessorFamilySH3                 = 0x0104
ProcessorFamilySH4                 = 0x0105
ProcessorFamilyARM                 = 0x0118
ProcessorFamilyStrongARM           = 0x0119
ProcessorFamily6x86                = 0x012C
ProcessorFamilyMediaGX             = 0x012D
ProcessorFamilyMII                 = 0x012E
ProcessorFamilyWinChip             = 0x0140
ProcessorFamilyDSP                 = 0x015E
ProcessorFamilyVideoProcessor      = 0x01F4
ProcessorFamilyRiscvRV32           = 0x0200
ProcessorFamilyRiscVRV64           = 0x0201
ProcessorFamilyRiscVRV128          = 0x0202
ProcessorFamilyLoongArch           = 0x0258
ProcessorFamilyLoongson1           = 0x0259
ProcessorFamilyLoongson2           = 0x025A
ProcessorFamilyLoongson3           = 0x025B
ProcessorFamilyLoongson2K          = 0x025C
ProcessorFamilyLoongson3A          = 0x025D
ProcessorFamilyLoongson3B          = 0x025E
ProcessorFamilyLoongson3C          = 0x025F
ProcessorFamilyLoongson3D          = 0x0260
ProcessorFamilyLoongson3E          = 0x0261
ProcessorFamilyDualCoreLoongson2K  = 0x0262
ProcessorFamilyQuadCoreLoongson3A  = 0x026C
ProcessorFamilyMultiCoreLoongson3A = 0x026D
ProcessorFamilyQuadCoreLoongson3B  = 0x026E
ProcessorFamilyMultiCoreLoongson3B = 0x026F
ProcessorFamilyMultiCoreLoongson3C = 0x0270
ProcessorFamilyMultiCoreLoongson3D = 0x0271
PROCESSOR_FAMILY2_DATA = ENUM

class PROCESSOR_VOLTAGE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ProcessorVoltageCapability5V",        UINT8, 1),
    ("ProcessorVoltageCapability3_3V",      UINT8, 1), 
    ("ProcessorVoltageCapability2_9V",      UINT8, 1), 
    ("ProcessorVoltageCapabilityReserved",  UINT8, 1),
    ("ProcessorVoltageReserved",            UINT8, 3),
    ("ProcessorVoltageIndicateLegacy",      UINT8, 1)
  ]

ProcessorUpgradeOther           = 0x01
ProcessorUpgradeUnknown         = 0x02
ProcessorUpgradeDaughterBoard   = 0x03
ProcessorUpgradeZIFSocket       = 0x04
ProcessorUpgradePiggyBack       = 0x05 # Replaceable.
ProcessorUpgradeNone            = 0x06
ProcessorUpgradeLIFSocket       = 0x07
ProcessorUpgradeSlot1           = 0x08
ProcessorUpgradeSlot2           = 0x09
ProcessorUpgrade370PinSocket    = 0x0A
ProcessorUpgradeSlotA           = 0x0B
ProcessorUpgradeSlotM           = 0x0C
ProcessorUpgradeSocket423       = 0x0D
ProcessorUpgradeSocketA         = 0x0E # Socket 462.
ProcessorUpgradeSocket478       = 0x0F
ProcessorUpgradeSocket754       = 0x10
ProcessorUpgradeSocket940       = 0x11
ProcessorUpgradeSocket939       = 0x12
ProcessorUpgradeSocketmPGA604   = 0x13
ProcessorUpgradeSocketLGA771    = 0x14
ProcessorUpgradeSocketLGA775    = 0x15
ProcessorUpgradeSocketS1        = 0x16
ProcessorUpgradeAM2             = 0x17
ProcessorUpgradeF1207           = 0x18
ProcessorSocketLGA1366          = 0x19
ProcessorUpgradeSocketG34       = 0x1A
ProcessorUpgradeSocketAM3       = 0x1B
ProcessorUpgradeSocketC32       = 0x1C
ProcessorUpgradeSocketLGA1156   = 0x1D
ProcessorUpgradeSocketLGA1567   = 0x1E
ProcessorUpgradeSocketPGA988A   = 0x1F
ProcessorUpgradeSocketBGA1288   = 0x20
ProcessorUpgradeSocketrPGA988B  = 0x21
ProcessorUpgradeSocketBGA1023   = 0x22
ProcessorUpgradeSocketBGA1224   = 0x23
ProcessorUpgradeSocketLGA1155   = 0x24 # SMBIOS spec 2.8.0 updated the name
ProcessorUpgradeSocketLGA1356   = 0x25
ProcessorUpgradeSocketLGA2011   = 0x26
ProcessorUpgradeSocketFS1       = 0x27
ProcessorUpgradeSocketFS2       = 0x28
ProcessorUpgradeSocketFM1       = 0x29
ProcessorUpgradeSocketFM2       = 0x2A
ProcessorUpgradeSocketLGA2011_3 = 0x2B
ProcessorUpgradeSocketLGA1356_3 = 0x2C
ProcessorUpgradeSocketLGA1150   = 0x2D
ProcessorUpgradeSocketBGA1168   = 0x2E
ProcessorUpgradeSocketBGA1234   = 0x2F
ProcessorUpgradeSocketBGA1364   = 0x30
ProcessorUpgradeSocketAM4       = 0x31
ProcessorUpgradeSocketLGA1151   = 0x32
ProcessorUpgradeSocketBGA1356   = 0x33
ProcessorUpgradeSocketBGA1440   = 0x34
ProcessorUpgradeSocketBGA1515   = 0x35
ProcessorUpgradeSocketLGA3647_1 = 0x36
ProcessorUpgradeSocketSP3       = 0x37
ProcessorUpgradeSocketSP3r2     = 0x38
ProcessorUpgradeSocketLGA2066   = 0x39
ProcessorUpgradeSocketBGA1392   = 0x3A
ProcessorUpgradeSocketBGA1510   = 0x3B
ProcessorUpgradeSocketBGA1528   = 0x3C
ProcessorUpgradeSocketLGA4189   = 0x3D
ProcessorUpgradeSocketLGA1200   = 0x3E
ProcessorUpgradeSocketLGA4677   = 0x3F
ProcessorUpgradeSocketLGA1700   = 0x40
ProcessorUpgradeSocketBGA1744   = 0x41
ProcessorUpgradeSocketBGA1781   = 0x42
ProcessorUpgradeSocketBGA1211   = 0x43
ProcessorUpgradeSocketBGA2422   = 0x44
ProcessorUpgradeSocketLGA1211   = 0x45
ProcessorUpgradeSocketLGA2422   = 0x46
ProcessorUpgradeSocketLGA5773   = 0x47
ProcessorUpgradeSocketBGA5773   = 0x48
PROCESSOR_UPGRADE = ENUM

class PROCESSOR_SIGNATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ProcessorSteppingId", UINT32, 4),
    ("ProcessorModel",      UINT32, 4),
    ("ProcessorFamily",     UINT32, 4),
    ("ProcessorType",       UINT32, 2),
    ("ProcessorReserved1",  UINT32, 2),
    ("ProcessorXModel",     UINT32, 4),
    ("ProcessorXFamily",    UINT32, 8),
    ("ProcessorReserved2",  UINT32, 4)
  ]

class PROCESSOR_FEATURE_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ProcessorFpu",        UINT32, 1),
    ("ProcessorVme",        UINT32, 1),
    ("ProcessorDe",         UINT32, 1),
    ("ProcessorPse",        UINT32, 1),
    ("ProcessorTsc",        UINT32, 1),
    ("ProcessorMsr",        UINT32, 1),
    ("ProcessorPae",        UINT32, 1),
    ("ProcessorMce",        UINT32, 1),
    ("ProcessorCx8",        UINT32, 1),
    ("ProcessorApic",       UINT32, 1),
    ("ProcessorReserved1",  UINT32, 1),
    ("ProcessorSep",        UINT32, 1),
    ("ProcessorMtrr",       UINT32, 1),
    ("ProcessorPge",        UINT32, 1),
    ("ProcessorMca",        UINT32, 1),
    ("ProcessorCmov",       UINT32, 1),
    ("ProcessorPat",        UINT32, 1),
    ("ProcessorPse36",      UINT32, 1),
    ("ProcessorPsn",        UINT32, 1),
    ("ProcessorClfsh",      UINT32, 1),
    ("ProcessorReserved2",  UINT32, 1),
    ("ProcessorDs",         UINT32, 1),
    ("ProcessorAcpi",       UINT32, 1),
    ("ProcessorMmx",        UINT32, 1),
    ("ProcessorFxsr",       UINT32, 1),
    ("ProcessorSse",        UINT32, 1),
    ("ProcessorSse2",       UINT32, 1),
    ("ProcessorSs",         UINT32, 1),
    ("ProcessorReserved3",  UINT32, 1),
    ("ProcessorTm",         UINT32, 1),
    ("ProcessorReserved4",  UINT32, 2)
  ]

class PROCESSOR_CHARACTERISTIC_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ProcessorReserved1",              UINT16, 1),
    ("ProcessorUnknown",                UINT16, 1),
    ("Processor64BitCapable",           UINT16, 1),
    ("ProcessorMultiCore",              UINT16, 1),
    ("ProcessorHardwareThread",         UINT16, 1),
    ("ProcessorExecuteProtection",      UINT16, 1),
    ("ProcessorEnhancedVirtualization", UINT16, 1),
    ("ProcessorPowerPerformanceCtrl",   UINT16, 1),
    ("Processor128BitCapable",          UINT16, 1),
    ("ProcessorArm64SocId",             UINT16, 1),
    ("ProcessorReserved2",              UINT16, 6)
  ]

class PROCESSOR_STATUS_DATA_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CpuStatus",       UINT8, 3),
    ("Reserved1",       UINT8, 3),
    ("SocketPopulated", UINT8, 1),
    ("Reserved2",       UINT8, 1)
    ]

class PROCESSOR_STATUS_DATA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PROCESSOR_STATUS_DATA_Bits),
    ("Data",    UINT8)
    ]

class PROCESSOR_ID_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",     PROCESSOR_SIGNATURE),
    ("FeatureFlags",  PROCESSOR_FEATURE_FLAGS)
  ]

class SMBIOS_TABLE_TYPE4 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                       SMBIOS_STRUCTURE),
    ("Socket",                    SMBIOS_TABLE_STRING),
    ("ProcessorType",             UINT8),
    ("ProcessorFamily",           UINT8),
    ("ProcessorManufacturer",     SMBIOS_TABLE_STRING),
    ("ProcessorId",               PROCESSOR_ID_DATA),
    ("ProcessorVersion",          SMBIOS_TABLE_STRING),
    ("Voltage",                   PROCESSOR_VOLTAGE),
    ("ExternalClock",             UINT16),
    ("MaxSpeed",                  UINT16),
    ("CurrentSpeed",              UINT16),
    ("Status",                    UINT8),
    ("ProcessorUpgrade",          UINT8),
    ("L1CacheHandle",             UINT16),
    ("L2CacheHandle",             UINT16),
    ("L3CacheHandle",             UINT16),
    ("SerialNumber",              SMBIOS_TABLE_STRING),
    ("AssetTag",                  SMBIOS_TABLE_STRING),
    ("PartNumber",                SMBIOS_TABLE_STRING),
    ("CoreCount",                 UINT8),
    ("EnabledCoreCount",          UINT8),
    ("ThreadCount",               UINT8),
    ("ProcessorCharacteristics",  UINT16),
    ("ProcessorFamily2",          UINT16),
    ("CoreCount2",                UINT16),
    ("EnabledCoreCount2",         UINT16),
    ("ThreadCount2",              UINT16),
    ("ThreadEnabled",             UINT16)
  ]

ErrorDetectingMethodOther   = 0x01
ErrorDetectingMethodUnknown = 0x02
ErrorDetectingMethodNone    = 0x03
ErrorDetectingMethodParity  = 0x04
ErrorDetectingMethod32Ecc   = 0x05
ErrorDetectingMethod64Ecc   = 0x06
ErrorDetectingMethod128Ecc  = 0x07
ErrorDetectingMethodCrc     = 0x08
MEMORY_ERROR_DETECT_METHOD = ENUM

class MEMORY_ERROR_CORRECT_CAPABILITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Other",                 UINT8, 1),
    ("Unknown",               UINT8, 1),
    ("None",                  UINT8, 1),
    ("SingleBitErrorCorrect", UINT8, 1),
    ("DoubleBitErrorCorrect", UINT8, 1),
    ("ErrorScrubbing",        UINT8, 1),
    ("Reserved",              UINT8, 2)
  ]

MemoryInterleaveOther      = 0x01
MemoryInterleaveUnknown    = 0x02
MemoryInterleaveOneWay     = 0x03
MemoryInterleaveTwoWay     = 0x04
MemoryInterleaveFourWay    = 0x05
MemoryInterleaveEightWay   = 0x06
MemoryInterleaveSixteenWay = 0x07
MEMORY_SUPPORT_INTERLEAVE_TYPE = ENUM

class MEMORY_SPEED_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Other",     UINT16, 1),
    ("Unknown",   UINT16, 1),
    ("SeventyNs", UINT16, 1),
    ("SixtyNs",   UINT16, 1),
    ("FiftyNs",   UINT16, 1),
    ("Reserved",  UINT16, 11)
  ]

class SMBIOS_TABLE_TYPE5 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                       SMBIOS_STRUCTURE),
    ("ErrDetectMethod",           UINT8),
    ("ErrCorrectCapability",      MEMORY_ERROR_CORRECT_CAPABILITY),
    ("SupportInterleave",         UINT8),
    ("CurrentInterleave",         UINT8),   
    ("MaxMemoryModuleSize",       UINT8),
    ("SupportSpeed",              MEMORY_SPEED_TYPE),
    ("SupportMemoryType",         UINT16),
    ("MemoryModuleVoltage",       UINT8),
    ("AssociatedMemorySlotNum",   UINT8),
    ("MemoryModuleConfigHandles", UINT16 * 1)
  ]

class MEMORY_CURRENT_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Other",         UINT16, 1),
    ("Unknown",       UINT16, 1),
    ("Standard",      UINT16, 1),
    ("FastPageMode",  UINT16, 1),
    ("Edo",           UINT16, 1),
    ("Parity",        UINT16, 1),
    ("Ecc",           UINT16, 1),
    ("Simm",          UINT16, 1),
    ("Dimm",          UINT16, 1),
    ("BurstEdo",      UINT16, 1),
    ("Sdram",         UINT16, 1),
    ("Reserved",      UINT16, 5)
  ]

class MEMORY_INSTALLED_ENABLED_SIZE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InstalledOrEnabledSize",  UINT8, 7),
    ("SingleOrDoubleBank",      UINT8, 1)
  ]

class SMBIOS_TABLE_TYPE6 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",               SMBIOS_STRUCTURE),
    ("SocketDesignation", SMBIOS_TABLE_STRING),
    ("BankConnections",   UINT8),
    ("CurrentSpeed",      UINT8),
    ("CurrentMemoryType", MEMORY_CURRENT_TYPE),
    ("InstalledSize",     MEMORY_INSTALLED_ENABLED_SIZE),
    ("EnabledSize",       MEMORY_INSTALLED_ENABLED_SIZE),
    ("ErrorStatus",       UINT8)
  ]

class CACHE_SRAM_TYPE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Other",         UINT16, 1),
    ("Unknown",       UINT16, 1),
    ("NonBurst",      UINT16, 1),
    ("Burst",         UINT16, 1),
    ("PipelineBurst", UINT16, 1),
    ("Synchronous",   UINT16, 1),
    ("Asynchronous",  UINT16, 1),
    ("Reserved",      UINT16, 9)
  ]

CacheErrorOther     = 0x01
CacheErrorUnknown   = 0x02
CacheErrorNone      = 0x03
CacheErrorParity    = 0x04
CacheErrorSingleBit = 0x05
CacheErrorMultiBit  = 0x06
CACHE_ERROR_TYPE_DATA = ENUM

CacheTypeOther       = 0x01
CacheTypeUnknown     = 0x02
CacheTypeInstruction = 0x03
CacheTypeData        = 0x04
CacheTypeUnified     = 0x05
CACHE_TYPE_DATA = ENUM

CacheAssociativityOther        = 0x01
CacheAssociativityUnknown      = 0x02
CacheAssociativityDirectMapped = 0x03
CacheAssociativity2Way         = 0x04
CacheAssociativity4Way         = 0x05
CacheAssociativityFully        = 0x06
CacheAssociativity8Way         = 0x07
CacheAssociativity16Way        = 0x08
CacheAssociativity12Way        = 0x09
CacheAssociativity24Way        = 0x0A
CacheAssociativity32Way        = 0x0B
CacheAssociativity48Way        = 0x0C
CacheAssociativity64Way        = 0x0D
CacheAssociativity20Way        = 0x0E
CACHE_ASSOCIATIVITY_DATA = ENUM

class SMBIOS_TABLE_TYPE7 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 SMBIOS_STRUCTURE),
    ("SocketDesignation",   SMBIOS_TABLE_STRING ),
    ("CacheConfiguration",  UINT16),
    ("MaximumCacheSize",    UINT16),
    ("InstalledSize",       UINT16),
    ("SupportedSRAMType",   CACHE_SRAM_TYPE_DATA),
    ("CurrentSRAMType",     CACHE_SRAM_TYPE_DATA),
    ("CacheSpeed",          UINT8),
    ("ErrorCorrectionType", UINT8),
    ("SystemCacheType",     UINT8),
    ("Associativity",       UINT8)
  ]

PortConnectorTypeNone                 = 0x00
PortConnectorTypeCentronics           = 0x01
PortConnectorTypeMiniCentronics       = 0x02
PortConnectorTypeProprietary          = 0x03
PortConnectorTypeDB25Male             = 0x04
PortConnectorTypeDB25Female           = 0x05
PortConnectorTypeDB15Male             = 0x06
PortConnectorTypeDB15Female           = 0x07
PortConnectorTypeDB9Male              = 0x08
PortConnectorTypeDB9Female            = 0x09
PortConnectorTypeRJ11                 = 0x0A
PortConnectorTypeRJ45                 = 0x0B
PortConnectorType50PinMiniScsi        = 0x0C
PortConnectorTypeMiniDin              = 0x0D
PortConnectorTypeMicroDin             = 0x0E
PortConnectorTypePS2                  = 0x0F
PortConnectorTypeInfrared             = 0x10
PortConnectorTypeHpHil                = 0x11
PortConnectorTypeUsb                  = 0x12
PortConnectorTypeSsaScsi              = 0x13
PortConnectorTypeCircularDin8Male     = 0x14
PortConnectorTypeCircularDin8Female   = 0x15
PortConnectorTypeOnboardIde           = 0x16
PortConnectorTypeOnboardFloppy        = 0x17
PortConnectorType9PinDualInline       = 0x18
PortConnectorType25PinDualInline      = 0x19
PortConnectorType50PinDualInline      = 0x1A
PortConnectorType68PinDualInline      = 0x1B
PortConnectorTypeOnboardSoundInput    = 0x1C
PortConnectorTypeMiniCentronicsType14 = 0x1D
PortConnectorTypeMiniCentronicsType26 = 0x1E
PortConnectorTypeHeadPhoneMiniJack    = 0x1F
PortConnectorTypeBNC                  = 0x20
PortConnectorType1394                 = 0x21
PortConnectorTypeSasSata              = 0x22
PortConnectorTypeUsbTypeC             = 0x23
PortConnectorTypePC98                 = 0xA0
PortConnectorTypePC98Hireso           = 0xA1
PortConnectorTypePCH98                = 0xA2
PortConnectorTypePC98Note             = 0xA3
PortConnectorTypePC98Full             = 0xA4
PortConnectorTypeOther                = 0xFF
MISC_PORT_CONNECTOR_TYPE = ENUM

PortTypeNone                   = 0x00
PortTypeParallelXtAtCompatible = 0x01
PortTypeParallelPortPs2        = 0x02
PortTypeParallelPortEcp        = 0x03
PortTypeParallelPortEpp        = 0x04
PortTypeParallelPortEcpEpp     = 0x05
PortTypeSerialXtAtCompatible   = 0x06
PortTypeSerial16450Compatible  = 0x07
PortTypeSerial16550Compatible  = 0x08
PortTypeSerial16550ACompatible = 0x09
PortTypeScsi                   = 0x0A
PortTypeMidi                   = 0x0B
PortTypeJoyStick               = 0x0C
PortTypeKeyboard               = 0x0D
PortTypeMouse                  = 0x0E
PortTypeSsaScsi                = 0x0F
PortTypeUsb                    = 0x10
PortTypeFireWire               = 0x11
PortTypePcmciaTypeI            = 0x12
PortTypePcmciaTypeII           = 0x13
PortTypePcmciaTypeIII          = 0x14
PortTypeCardBus                = 0x15
PortTypeAccessBusPort          = 0x16
PortTypeScsiII                 = 0x17
PortTypeScsiWide               = 0x18
PortTypePC98                   = 0x19
PortTypePC98Hireso             = 0x1A
PortTypePCH98                  = 0x1B
PortTypeVideoPort              = 0x1C
PortTypeAudioPort              = 0x1D
PortTypeModemPort              = 0x1E
PortTypeNetworkPort            = 0x1F
PortTypeSata                   = 0x20
PortTypeSas                    = 0x21
PortTypeMfdp                   = 0x22    # Multi-Function Display Port
PortTypeThunderbolt            = 0x23
PortType8251Compatible         = 0xA0
PortType8251FifoCompatible     = 0xA1
PortTypeOther                  = 0xFF
MISC_PORT_TYPE = ENUM

class SMBIOS_TABLE_TYPE8 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                         SMBIOS_STRUCTURE),
    ("InternalReferenceDesignator", SMBIOS_TABLE_STRING),
    ("InternalConnectorType",       UINT8),
    ("ExternalReferenceDesignator", SMBIOS_TABLE_STRING),
    ("ExternalConnectorType",       UINT8),
    ("PortType",                    UINT8)
  ]

SlotTypeOther                                     = 0x01
SlotTypeUnknown                                   = 0x02
SlotTypeIsa                                       = 0x03
SlotTypeMca                                       = 0x04
SlotTypeEisa                                      = 0x05
SlotTypePci                                       = 0x06
SlotTypePcmcia                                    = 0x07
SlotTypeVlVesa                                    = 0x08
SlotTypeProprietary                               = 0x09
SlotTypeProcessorCardSlot                         = 0x0A
SlotTypeProprietaryMemoryCardSlot                 = 0x0B
SlotTypeIORiserCardSlot                           = 0x0C
SlotTypeNuBus                                     = 0x0D
SlotTypePci66MhzCapable                           = 0x0E
SlotTypeAgp                                       = 0x0F
SlotTypeApg2X                                     = 0x10
SlotTypeAgp4X                                     = 0x11
SlotTypePciX                                      = 0x12
SlotTypeAgp8X                                     = 0x13
SlotTypeM2Socket1_DP                              = 0x14
SlotTypeM2Socket1_SD                              = 0x15
SlotTypeM2Socket2                                 = 0x16
SlotTypeM2Socket3                                 = 0x17
SlotTypeMxmTypeI                                  = 0x18
SlotTypeMxmTypeII                                 = 0x19
SlotTypeMxmTypeIIIStandard                        = 0x1A
SlotTypeMxmTypeIIIHe                              = 0x1B
SlotTypeMxmTypeIV                                 = 0x1C
SlotTypeMxm30TypeA                                = 0x1D
SlotTypeMxm30TypeB                                = 0x1E
SlotTypePciExpressGen2Sff_8639                    = 0x1F
SlotTypePciExpressGen3Sff_8639                    = 0x20
SlotTypePciExpressMini52pinWithBSKO               = 0x21    # PCI Express Mini 52-pin (CEM spec. 2.0) with bottom-side keep-outs.
SlotTypePciExpressMini52pinWithoutBSKO            = 0x22    # PCI Express Mini 52-pin (CEM spec. 2.0) without bottom-side keep-outs.
SlotTypePciExpressMini76pin                       = 0x23    # PCI Express Mini 76-pin (CEM spec. 2.0) Corresponds to Display-Mini card.
SlotTypePCIExpressGen4SFF_8639                    = 0x24    # U.2
SlotTypePCIExpressGen5SFF_8639                    = 0x25    # U.2
SlotTypeOCPNIC30SmallFormFactor                   = 0x26    # SFF
SlotTypeOCPNIC30LargeFormFactor                   = 0x27    # LFF
SlotTypeOCPNICPriorto30                           = 0x28
SlotTypeCXLFlexbus10                              = 0x30
SlotTypePC98C20                                   = 0xA0
SlotTypePC98C24                                   = 0xA1
SlotTypePC98E                                     = 0xA2
SlotTypePC98LocalBus                              = 0xA3
SlotTypePC98Card                                  = 0xA4
SlotTypePciExpress                                = 0xA5
SlotTypePciExpressX1                              = 0xA6
SlotTypePciExpressX2                              = 0xA7
SlotTypePciExpressX4                              = 0xA8
SlotTypePciExpressX8                              = 0xA9
SlotTypePciExpressX16                             = 0xAA
SlotTypePciExpressGen2                            = 0xAB
SlotTypePciExpressGen2X1                          = 0xAC
SlotTypePciExpressGen2X2                          = 0xAD
SlotTypePciExpressGen2X4                          = 0xAE
SlotTypePciExpressGen2X8                          = 0xAF
SlotTypePciExpressGen2X16                         = 0xB0
SlotTypePciExpressGen3                            = 0xB1
SlotTypePciExpressGen3X1                          = 0xB2
SlotTypePciExpressGen3X2                          = 0xB3
SlotTypePciExpressGen3X4                          = 0xB4
SlotTypePciExpressGen3X8                          = 0xB5
SlotTypePciExpressGen3X16                         = 0xB6
SlotTypePciExpressGen4                            = 0xB8
SlotTypePciExpressGen4X1                          = 0xB9
SlotTypePciExpressGen4X2                          = 0xBA
SlotTypePciExpressGen4X4                          = 0xBB
SlotTypePciExpressGen4X8                          = 0xBC
SlotTypePciExpressGen4X16                         = 0xBD
SlotTypePCIExpressGen5                            = 0xBE
SlotTypePCIExpressGen5X1                          = 0xBF
SlotTypePCIExpressGen5X2                          = 0xC0
SlotTypePCIExpressGen5X4                          = 0xC1
SlotTypePCIExpressGen5X8                          = 0xC2
SlotTypePCIExpressGen5X16                         = 0xC3
SlotTypePCIExpressGen6andBeyond                   = 0xC4
SlotTypeEnterpriseandDatacenter1UE1FormFactorSlot = 0xC5
SlotTypeEnterpriseandDatacenter3E3FormFactorSlot  = 0xC6
MISC_SLOT_TYPE = ENUM

SlotDataBusWidthOther   = 0x01
SlotDataBusWidthUnknown = 0x02
SlotDataBusWidth8Bit    = 0x03
SlotDataBusWidth16Bit   = 0x04
SlotDataBusWidth32Bit   = 0x05
SlotDataBusWidth64Bit   = 0x06
SlotDataBusWidth128Bit  = 0x07
SlotDataBusWidth1X      = 0x08    # Or X1
SlotDataBusWidth2X      = 0x09    # Or X2
SlotDataBusWidth4X      = 0x0A    # Or X4
SlotDataBusWidth8X      = 0x0B    # Or X8
SlotDataBusWidth12X     = 0x0C    # Or X12
SlotDataBusWidth16X     = 0x0D    # Or X16
SlotDataBusWidth32X     = 0x0E    # Or X32
MISC_SLOT_DATA_BUS_WIDTH = ENUM

SlotPhysicalWidthOther   = 0x01
SlotPhysicalWidthUnknown = 0x02
SlotPhysicalWidth8Bit    = 0x03
SlotPhysicalWidth16Bit   = 0x04
SlotPhysicalWidth32Bit   = 0x05
SlotPhysicalWidth64Bit   = 0x06
SlotPhysicalWidth128Bit  = 0x07
SlotPhysicalWidth1X      = 0x08    # Or X1
SlotPhysicalWidth2X      = 0x09    # Or X2
SlotPhysicalWidth4X      = 0x0A    # Or X4
SlotPhysicalWidth8X      = 0x0B    # Or X8
SlotPhysicalWidth12X     = 0x0C    # Or X12
SlotPhysicalWidth16X     = 0x0D    # Or X16
SlotPhysicalWidth32X     = 0x0E    # Or X32
MISC_SLOT_PHYSICAL_WIDTH    = ENUM

Others = 0x00
Gen1   = 0x01
Gen2   = 0x01
Gen3   = 0x03
Gen4   = 0x04
Gen5   = 0x05
Gen6   = 0x06
MISC_SLOT_INFORMATION = ENUM

SlotUsageOther       = 0x01
SlotUsageUnknown     = 0x02
SlotUsageAvailable   = 0x03
SlotUsageInUse       = 0x04
SlotUsageUnavailable = 0x05
MISC_SLOT_USAGE = ENUM

SlotLengthOther   = 0x01
SlotLengthUnknown = 0x02
SlotLengthShort   = 0x03
SlotLengthLong    = 0x04
MISC_SLOT_LENGTH = ENUM

class MISC_SLOT_CHARACTERISTICS1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CharacteristicsUnknown",    UINT8, 1),
    ("Provides50Volts",           UINT8, 1),
    ("Provides33Volts",           UINT8, 1),
    ("SharedSlot",                UINT8, 1),
    ("PcCard16Supported",         UINT8, 1),
    ("CardBusSupported",          UINT8, 1),
    ("ZoomVideoSupported",        UINT8, 1),
    ("ModemRingResumeSupported",  UINT8, 1)
  ]

class MISC_SLOT_CHARACTERISTICS2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PmeSignalSupported",      UINT8, 1),
    ("HotPlugDevicesSupported", UINT8, 1),
    ("SmbusSignalSupported",    UINT8, 1),
    ("BifurcationSupported",    UINT8, 1),
    ("AsyncSurpriseRemoval",    UINT8, 1),
    ("FlexbusSlotCxl10Capable", UINT8, 1),
    ("FlexbusSlotCxl20Capable", UINT8, 1),
    ("Reserved",                UINT8, 1)
  ]

SlotHeightNone       = 0x00
SlotHeightOther      = 0x01
SlotHeightUnknown    = 0x02
SlotHeightFullHeight = 0x03
SlotHeightLowProfile = 0x04
MISC_SLOT_HEIGHT = ENUM

class MISC_SLOT_PEER_GROUP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SegmentGroupNum", UINT16),
    ("BusNum",          UINT8),
    ("DevFuncNum",      UINT8),
    ("DataBusWidth",    UINT8)
  ]

class SMBIOS_TABLE_TYPE9 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                   SMBIOS_STRUCTURE),
    ("SlotDesignation",       SMBIOS_TABLE_STRING),
    ("SlotType",              UINT8),
    ("SlotDataBusWidth",      UINT8),
    ("CurrentUsage",          UINT8),
    ("SlotLength",            UINT8),
    ("SlotID",                UINT16),
    ("SlotCharacteristics1",  MISC_SLOT_CHARACTERISTICS1),
    ("SlotCharacteristics2",  MISC_SLOT_CHARACTERISTICS2),
    ("SegmentGroupNum",       UINT16),
    ("BusNum",                UINT8),
    ("DevFuncNum",            UINT8),
    ("DataBusWidth",          UINT8),
    ("PeerGroupingCount",     UINT8),
    ("PeerGroups",            MISC_SLOT_PEER_GROUP * 1),
  ]

class SMBIOS_TABLE_TYPE9_EXTENDED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SlotInformation",     UINT8),
    ("SlotPhysicalWidth",   UINT8),
    ("SlotPitch",           UINT16),
    ("SlotHeight",          UINT8),
  ]

OnBoardDeviceTypeOther          = 0x01
OnBoardDeviceTypeUnknown        = 0x02
OnBoardDeviceTypeVideo          = 0x03
OnBoardDeviceTypeScsiController = 0x04
OnBoardDeviceTypeEthernet       = 0x05
OnBoardDeviceTypeTokenRing      = 0x06
OnBoardDeviceTypeSound          = 0x07
OnBoardDeviceTypePATAController = 0x08
OnBoardDeviceTypeSATAController = 0x09
OnBoardDeviceTypeSASController  = 0x0A
MISC_ONBOARD_DEVICE_TYPE = ENUM

class DEVICE_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceType",        UINT8),
    ("DescriptionString", SMBIOS_TABLE_STRING)
  ]

class SMBIOS_TABLE_TYPE10 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",     SMBIOS_STRUCTURE),
    ("Device",  DEVICE_STRUCT * 1)
  ]

class SMBIOS_TABLE_TYPE11 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",         SMBIOS_STRUCTURE),
    ("StringCount", UINT8)
  ]

class SMBIOS_TABLE_TYPE12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",         SMBIOS_STRUCTURE),
    ("StringCount", UINT8)
  ]

class SMBIOS_TABLE_TYPE13 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                   SMBIOS_STRUCTURE),
    ("InstallableLanguages",  UINT8),
    ("Flags",                 UINT8),
    ("Reserved",              UINT8 * 15),
    ("CurrentLanguages",      SMBIOS_TABLE_STRING)
  ]

class GROUP_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ItemType",    UINT8),
    ("ItemHandle",  UINT16)
  ]

class SMBIOS_TABLE_TYPE14 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",       SMBIOS_STRUCTURE),
    ("GroupName", SMBIOS_TABLE_STRING),
    ("Group",     GROUP_STRUCT * 1)
  ]

EventLogTypeReserved         = 0x00
EventLogTypeSingleBitECC     = 0x01
EventLogTypeMultiBitECC      = 0x02
EventLogTypeParityMemErr     = 0x03
EventLogTypeBusTimeOut       = 0x04
EventLogTypeIOChannelCheck   = 0x05
EventLogTypeSoftwareNMI      = 0x06
EventLogTypePOSTMemResize    = 0x07
EventLogTypePOSTErr          = 0x08
EventLogTypePCIParityErr     = 0x09
EventLogTypePCISystemErr     = 0x0A
EventLogTypeCPUFailure       = 0x0B
EventLogTypeEISATimeOut      = 0x0C
EventLogTypeMemLogDisabled   = 0x0D
EventLogTypeLoggingDisabled  = 0x0E
EventLogTypeSysLimitExce     = 0x10
EventLogTypeAsyncHWTimer     = 0x11
EventLogTypeSysConfigInfo    = 0x12
EventLogTypeHDInfo           = 0x13
EventLogTypeSysReconfig      = 0x14
EventLogTypeUncorrectCPUErr  = 0x15
EventLogTypeAreaResetAndClr  = 0x16
EventLogTypeSystemBoot       = 0x17
EventLogTypeUnused           = 0x18
EventLogTypeAvailForSys      = 0x80
EventLogTypeEndOfLog         = 0xFF
EVENT_LOG_TYPE_DATA = ENUM

EventLogVariableNone                        = 0x00
EventLogVariableHandle                      = 0x01
EventLogVariableMutilEvent                  = 0x02
EventLogVariableMutilEventHandle            = 0x03
EventLogVariablePOSTResultBitmap            = 0x04
EventLogVariableSysManagementType           = 0x05
EventLogVariableMutliEventSysManagmentType  = 0x06,                              
EventLogVariableUnused                      = 0x07
EventLogVariableOEMAssigned                 = 0x80
EVENT_LOG_VARIABLE_DATA = ENUM

class EVENT_LOG_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogType",         UINT8),
    ("DataFormatType",  UINT8)
  ]

class SMBIOS_TABLE_TYPE15 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                                 SMBIOS_STRUCTURE),
    ("LogAreaLength",                       UINT16),
    ("LogHeaderStartOffset",                UINT16),
    ("LogDataStartOffset",                  UINT16),
    ("AccessMethod",                        UINT8),
    ("LogStatus",                           UINT8),
    ("LogChangeToken",                      UINT32),
    ("AccessMethodAddress",                 UINT32),
    ("LogHeaderFormat",                     UINT8),
    ("NumberOfSupportedLogTypeDescriptors", UINT8),
    ("LengthOfLogTypeDescriptor",           UINT8),
    ("EventLogTypeDescriptors",             EVENT_LOG_TYPE * 1)
  ]

MemoryArrayLocationOther                 = 0x01
MemoryArrayLocationUnknown               = 0x02
MemoryArrayLocationSystemBoard           = 0x03
MemoryArrayLocationIsaAddonCard          = 0x04
MemoryArrayLocationEisaAddonCard         = 0x05
MemoryArrayLocationPciAddonCard          = 0x06
MemoryArrayLocationMcaAddonCard          = 0x07
MemoryArrayLocationPcmciaAddonCard       = 0x08
MemoryArrayLocationProprietaryAddonCard  = 0x09
MemoryArrayLocationNuBus                 = 0x0A
MemoryArrayLocationPc98C20AddonCard      = 0xA0
MemoryArrayLocationPc98C24AddonCard      = 0xA1
MemoryArrayLocationPc98EAddonCard        = 0xA2
MemoryArrayLocationPc98LocalBusAddonCard = 0xA3
MemoryArrayLocationCXLAddonCard          = 0xA4
MEMORY_ARRAY_LOCATION = ENUM

MemoryArrayUseOther                      = 0x01
MemoryArrayUseUnknown                    = 0x02
MemoryArrayUseSystemMemory               = 0x03
MemoryArrayUseVideoMemory                = 0x04
MemoryArrayUseFlashMemory                = 0x05
MemoryArrayUseNonVolatileRam             = 0x06
MemoryArrayUseCacheMemory                = 0x07
MEMORY_ARRAY_USE = ENUM

MemoryErrorCorrectionOther               = 0x01
MemoryErrorCorrectionUnknown             = 0x02
MemoryErrorCorrectionNone                = 0x03
MemoryErrorCorrectionParity              = 0x04
MemoryErrorCorrectionSingleBitEcc        = 0x05
MemoryErrorCorrectionMultiBitEcc         = 0x06
MemoryErrorCorrectionCrc                 = 0x07
MEMORY_ERROR_CORRECTION = ENUM

class SMBIOS_TABLE_TYPE16 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                           SMBIOS_STRUCTURE),
    ("Location",                      UINT8),
    ("Use",                           UINT8),
    ("MemoryErrorCorrection",         UINT8),
    ("MaximumCapacity",               UINT32),
    ("MemoryErrorInformationHandle",  UINT16),
    ("NumberOfMemoryDevices",         UINT16),
    ("ExtendedMaximumCapacity",       UINT64)
  ]

MemoryFormFactorOther           = 0x01
MemoryFormFactorUnknown         = 0x02
MemoryFormFactorSimm            = 0x03
MemoryFormFactorSip             = 0x04
MemoryFormFactorChip            = 0x05
MemoryFormFactorDip             = 0x06
MemoryFormFactorZip             = 0x07
MemoryFormFactorProprietaryCard = 0x08
MemoryFormFactorDimm            = 0x09
MemoryFormFactorTsop            = 0x0A
MemoryFormFactorRowOfChips      = 0x0B
MemoryFormFactorRimm            = 0x0C
MemoryFormFactorSodimm          = 0x0D
MemoryFormFactorSrimm           = 0x0E
MemoryFormFactorFbDimm          = 0x0F
MemoryFormFactorDie             = 0x10
MEMORY_FORM_FACTOR = ENUM

MemoryTypeOther                    = 0x01
MemoryTypeUnknown                  = 0x02
MemoryTypeDram                     = 0x03
MemoryTypeEdram                    = 0x04
MemoryTypeVram                     = 0x05
MemoryTypeSram                     = 0x06
MemoryTypeRam                      = 0x07
MemoryTypeRom                      = 0x08
MemoryTypeFlash                    = 0x09
MemoryTypeEeprom                   = 0x0A
MemoryTypeFeprom                   = 0x0B
MemoryTypeEprom                    = 0x0C
MemoryTypeCdram                    = 0x0D
MemoryType3Dram                    = 0x0E
MemoryTypeSdram                    = 0x0F
MemoryTypeSgram                    = 0x10
MemoryTypeRdram                    = 0x11
MemoryTypeDdr                      = 0x12
MemoryTypeDdr2                     = 0x13
MemoryTypeDdr2FbDimm               = 0x14
MemoryTypeDdr3                     = 0x18
MemoryTypeFbd2                     = 0x19
MemoryTypeDdr4                     = 0x1A
MemoryTypeLpddr                    = 0x1B
MemoryTypeLpddr2                   = 0x1C
MemoryTypeLpddr3                   = 0x1D
MemoryTypeLpddr4                   = 0x1E
MemoryTypeLogicalNonVolatileDevice = 0x1F
MemoryTypeHBM                      = 0x20
MemoryTypeHBM2                     = 0x21
MemoryTypeDdr5                     = 0x22
MemoryTypeLpddr5                   = 0x23
MemoryTypeHBM3                     = 0x24
MEMORY_DEVICE_TYPE  = ENUM

class MEMORY_DEVICE_TYPE_DETAIL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",      UINT16, 1),
    ("Other",         UINT16, 1),
    ("Unknown",       UINT16, 1),
    ("FastPaged",     UINT16, 1),
    ("StaticColumn",  UINT16, 1),
    ("PseudoStatic",  UINT16, 1),
    ("Rambus",        UINT16, 1),
    ("Synchronous",   UINT16, 1),
    ("Cmos",          UINT16, 1),
    ("Edo",           UINT16, 1),
    ("WindowDram",    UINT16, 1),
    ("CacheDram",     UINT16, 1),
    ("Nonvolatile",   UINT16, 1),
    ("Registered",    UINT16, 1),
    ("Unbuffered",    UINT16, 1),
    ("LrDimm",        UINT16, 1)
  ]

MemoryTechnologyOther   = 0x01
MemoryTechnologyUnknown = 0x02
MemoryTechnologyDram    = 0x03
MemoryTechnologyNvdimmN = 0x04
MemoryTechnologyNvdimmF = 0x05
MemoryTechnologyNvdimmP = 0x06
MemoryTechnologyIntelOptanePersistentMemory = 0x07
MEMORY_DEVICE_TECHNOLOGY = ENUM

class MEMORY_DEVICE_OPERATING_MODE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                        UINT16, 1),
    ("Other",                           UINT16, 1),
    ("Unknown",                         UINT16, 1),
    ("VolatileMemory",                  UINT16, 1),
    ("ByteAccessiblePersistentMemory",  UINT16, 1),
    ("BlockAccessiblePersistentMemory", UINT16, 1),
    ("Reserved2",                       UINT16, 10),
    ]

class MEMORY_DEVICE_OPERATING_MODE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    MEMORY_DEVICE_OPERATING_MODE_CAPABILITY_Bits),
    ("Uint16",  UINT16)
    ]

class SMBIOS_TABLE_TYPE17 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                                     SMBIOS_STRUCTURE),
    ("MemoryArrayHandle",                       UINT16),
    ("MemoryErrorInformationHandle",            UINT16),
    ("TotalWidth",                              UINT16),
    ("DataWidth",                               UINT16),
    ("Size",                                    UINT16),
    ("FormFactor",                              UINT8),
    ("DeviceSet",                               UINT8),
    ("DeviceLocator",                           SMBIOS_TABLE_STRING),
    ("BankLocator",                             SMBIOS_TABLE_STRING),
    ("MemoryType",                              UINT8),
    ("TypeDetail",                              MEMORY_DEVICE_TYPE_DETAIL),
    ("Speed",                                   UINT16),
    ("Manufacturer",                            SMBIOS_TABLE_STRING),
    ("SerialNumber",                            SMBIOS_TABLE_STRING),
    ("AssetTag",                                SMBIOS_TABLE_STRING),
    ("PartNumber",                              SMBIOS_TABLE_STRING),
    ("Attributes",                              UINT8),
    ("ExtendedSize",                            UINT32),
    ("ConfiguredMemoryClockSpeed",              UINT16),
    ("MinimumVoltage",                          UINT16),
    ("MaximumVoltage",                          UINT16),
    ("ConfiguredVoltage",                       UINT16),
    ("MemoryTechnology",                        UINT8),
    ("MemoryOperatingModeCapability",           MEMORY_DEVICE_OPERATING_MODE_CAPABILITY),
    ("FirmwareVersion",                         SMBIOS_TABLE_STRING),
    ("ModuleManufacturerID",                    UINT16),
    ("ModuleProductID",                         UINT16),
    ("MemorySubsystemControllerManufacturerID", UINT16),
    ("MemorySubsystemControllerProductID",      UINT16),
    ("NonVolatileSize",                         UINT64),
    ("VolatileSize",                            UINT64),
    ("CacheSize",                               UINT64),
    ("LogicalSize",                             UINT64),
    ("ExtendedSpeed",                           UINT32),
    ("ExtendedConfiguredMemorySpeed",           UINT32)
  ]

MemoryErrorOther             = 0x01
MemoryErrorUnknown           = 0x02
MemoryErrorOk                = 0x03
MemoryErrorBadRead           = 0x04
MemoryErrorParity            = 0x05
MemoryErrorSigleBit          = 0x06
MemoryErrorDoubleBit         = 0x07
MemoryErrorMultiBit          = 0x08
MemoryErrorNibble            = 0x09
MemoryErrorChecksum          = 0x0A
MemoryErrorCrc               = 0x0B
MemoryErrorCorrectSingleBit  = 0x0C
MemoryErrorCorrected         = 0x0D
MemoryErrorUnCorrectable     = 0x0E
MEMORY_ERROR_TYPE = ENUM

MemoryGranularityOther               = 0x01
MemoryGranularityOtherUnknown        = 0x02
MemoryGranularityDeviceLevel         = 0x03
MemoryGranularityMemPartitionLevel   = 0x04
MEMORY_ERROR_GRANULARITY = ENUM

MemoryErrorOperationOther            = 0x01
MemoryErrorOperationUnknown          = 0x02
MemoryErrorOperationRead             = 0x03
MemoryErrorOperationWrite            = 0x04
MemoryErrorOperationPartialWrite     = 0x05
MEMORY_ERROR_OPERATION = ENUM

class SMBIOS_TABLE_TYPE18 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                     SMBIOS_STRUCTURE),
    ("ErrorType",               UINT8),
    ("ErrorGranularity",        UINT8),
    ("ErrorOperation",          UINT8),
    ("VendorSyndrome",          UINT32),
    ("MemoryArrayErrorAddress", UINT32),
    ("DeviceErrorAddress",      UINT32),
    ("ErrorResolution",         UINT32)
  ]

class SMBIOS_TABLE_TYPE19 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                     SMBIOS_STRUCTURE),
    ("StartingAddress",         UINT32),
    ("EndingAddress",           UINT32),
    ("MemoryArrayHandle",       UINT16),
    ("PartitionWidth",          UINT8),
    ("ExtendedStartingAddress", UINT64),
    ("ExtendedEndingAddress",   UINT64)
  ]

class SMBIOS_TABLE_TYPE20 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                             SMBIOS_STRUCTURE),
    ("StartingAddress",                 UINT32),
    ("EndingAddress",                   UINT32),
    ("MemoryDeviceHandle",              UINT16),
    ("MemoryArrayMappedAddressHandle",  UINT16),
    ("PartitionRowPosition",            UINT8),
    ("InterleavePosition",              UINT8),
    ("InterleavedDataDepth",            UINT8),
    ("ExtendedStartingAddress",         UINT64),
    ("ExtendedEndingAddress",           UINT64)
  ]

PointingDeviceTypeOther         = 0x01
PointingDeviceTypeUnknown       = 0x02
PointingDeviceTypeMouse         = 0x03
PointingDeviceTypeTrackBall     = 0x04
PointingDeviceTypeTrackPoint    = 0x05
PointingDeviceTypeGlidePoint    = 0x06
PointingDeviceTouchPad          = 0x07
PointingDeviceTouchScreen       = 0x08
PointingDeviceOpticalSensor     = 0x09
BUILTIN_POINTING_DEVICE_TYPE = ENUM

PointingDeviceInterfaceOther            = 0x01
PointingDeviceInterfaceUnknown          = 0x02
PointingDeviceInterfaceSerial           = 0x03
PointingDeviceInterfacePs2              = 0x04
PointingDeviceInterfaceInfrared         = 0x05
PointingDeviceInterfaceHpHil            = 0x06
PointingDeviceInterfaceBusMouse         = 0x07
PointingDeviceInterfaceADB              = 0x08
PointingDeviceInterfaceBusMouseDB9      = 0xA0
PointingDeviceInterfaceBusMouseMicroDin = 0xA1
PointingDeviceInterfaceUsb              = 0xA2
PointingDeviceInterfaceI2c              = 0xA3
PointingDeviceInterfaceSpi              = 0xA4
BUILTIN_POINTING_DEVICE_INTERFACE = ENUM

class SMBIOS_TABLE_TYPE21 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",             SMBIOS_STRUCTURE),
    ("Type",            UINT8),
    ("Interface",       UINT8),
    ("NumberOfButtons", UINT8),
  ]

PortableBatteryDeviceChemistryOther               = 0x01
PortableBatteryDeviceChemistryUnknown             = 0x02
PortableBatteryDeviceChemistryLeadAcid            = 0x03
PortableBatteryDeviceChemistryNickelCadmium       = 0x04
PortableBatteryDeviceChemistryNickelMetalHydride  = 0x05
PortableBatteryDeviceChemistryLithiumIon          = 0x06
PortableBatteryDeviceChemistryZincAir             = 0x07
PortableBatteryDeviceChemistryLithiumPolymer      = 0x08
PORTABLE_BATTERY_DEVICE_CHEMISTRY = ENUM

class SMBIOS_TABLE_TYPE22 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                       SMBIOS_STRUCTURE),
    ("Location",                  SMBIOS_TABLE_STRING),
    ("Manufacturer",              SMBIOS_TABLE_STRING),
    ("ManufactureDate",           SMBIOS_TABLE_STRING),
    ("SerialNumber",              SMBIOS_TABLE_STRING),
    ("DeviceName",                SMBIOS_TABLE_STRING),
    ("DeviceChemistry",           UINT8),
    ("DeviceCapacity",            UINT16),
    ("DesignVoltage",             UINT16),
    ("SBDSVersionNumber",         SMBIOS_TABLE_STRING),
    ("MaximumErrorInBatteryData", UINT8),
    ("SBDSSerialNumber",          UINT16),
    ("SBDSManufactureDate",       UINT16),
    ("SBDSDeviceChemistry",       SMBIOS_TABLE_STRING),
    ("DesignCapacityMultiplier",  UINT8),
    ("OEMSpecific",               UINT32)
  ]

class SMBIOS_TABLE_TYPE23 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",           SMBIOS_STRUCTURE),
    ("Capabilities",  UINT8),
    ("ResetCount",    UINT16),
    ("ResetLimit",    UINT16),
    ("TimerInterval", UINT16),
    ("Timeout",       UINT16)
  ]

class SMBIOS_TABLE_TYPE24 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                       SMBIOS_STRUCTURE),
    ("HardwareSecuritySettings",  UINT8)
  ]

class SMBIOS_TABLE_TYPE25 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                             SMBIOS_STRUCTURE),
    ("NextScheduledPowerOnMonth",       UINT8),
    ("NextScheduledPowerOnDayOfMonth",  UINT8),
    ("NextScheduledPowerOnHour",        UINT8),
    ("NextScheduledPowerOnMinute",      UINT8),
    ("NextScheduledPowerOnSecond",      UINT8)
  ]

class MISC_VOLTAGE_PROBE_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VoltageProbeSite",    UINT8, 5),
    ("VoltageProbeStatus",  UINT8, 3)
  ]

class SMBIOS_TABLE_TYPE26 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",               SMBIOS_STRUCTURE),
    ("Description",       SMBIOS_TABLE_STRING),
    ("LocationAndStatus", MISC_VOLTAGE_PROBE_LOCATION),
    ("MaximumValue",      UINT16),
    ("MinimumValue",      UINT16),
    ("Resolution",        UINT16),
    ("Tolerance",         UINT16),
    ("Accuracy",          UINT16),
    ("OEMDefined",        UINT32),
    ("NominalValue",      UINT16)
  ]

class MISC_COOLING_DEVICE_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CoolingDevice",       UINT8, 5),
    ("CoolingDeviceStatus", UINT8, 3)
  ]

class SMBIOS_TABLE_TYPE27 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                     SMBIOS_STRUCTURE),
    ("TemperatureProbeHandle",  UINT16),
    ("DeviceTypeAndStatus",     MISC_COOLING_DEVICE_TYPE),
    ("CoolingUnitGroup",        UINT8),
    ("OEMDefined",              UINT32),
    ("NominalSpeed",            UINT16),
    ("Description",             SMBIOS_TABLE_STRING)
  ]

class MISC_TEMPERATURE_PROBE_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TemperatureProbeSite",    UINT8, 5),
    ("TemperatureProbeStatus",  UINT8, 3),
  ]

class SMBIOS_TABLE_TYPE28 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",               SMBIOS_STRUCTURE),
    ("Description",       SMBIOS_TABLE_STRING),
    ("LocationAndStatus", MISC_TEMPERATURE_PROBE_LOCATION),
    ("MaximumValue",      UINT16),
    ("MinimumValue",      UINT16),
    ("Resolution",        UINT16),
    ("Tolerance",         UINT16),
    ("Accuracy",          UINT16),
    ("OEMDefined",        UINT32),
    ("NominalValue",      UINT16)
  ]

class MISC_ELECTRICAL_CURRENT_PROBE_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ElectricalCurrentProbeSite",    UINT8, 5),
    ("ElectricalCurrentProbeStatus",  UINT8, 3)
  ]

class SMBIOS_TABLE_TYPE29 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",               SMBIOS_STRUCTURE),
    ("Description",       SMBIOS_TABLE_STRING),
    ("LocationAndStatus", MISC_ELECTRICAL_CURRENT_PROBE_LOCATION),
    ("MaximumValue",      UINT16),
    ("MinimumValue",      UINT16),
    ("Resolution",        UINT16),
    ("Tolerance",         UINT16),
    ("Accuracy",          UINT16),
    ("OEMDefined",        UINT32),
    ("NominalValue",      UINT16)
  ]

class SMBIOS_TABLE_TYPE30 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",               SMBIOS_STRUCTURE),
    ("ManufacturerName",  SMBIOS_TABLE_STRING),
    ("Connections",       UINT8)
  ]

class SMBIOS_TABLE_TYPE31 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",         SMBIOS_STRUCTURE),
    ("Checksum",    UINT8),
    ("Reserved1",   UINT8),
    ("Reserved2",   UINT16),
    ("BisEntry16",  UINT32),
    ("BisEntry32",  UINT32),
    ("Reserved3",   UINT64),
    ("Reserved4",   UINT32)
  ]

BootInformationStatusNoError                  = 0x00
BootInformationStatusNoBootableMedia          = 0x01
BootInformationStatusNormalOSFailedLoading    = 0x02
BootInformationStatusFirmwareDetectedFailure  = 0x03
BootInformationStatusOSDetectedFailure        = 0x04
BootInformationStatusUserRequestedBoot        = 0x05
BootInformationStatusSystemSecurityViolation  = 0x06
BootInformationStatusPreviousRequestedImage   = 0x07
BootInformationStatusWatchdogTimerExpired     = 0x08
BootInformationStatusStartReserved            = 0x09
BootInformationStatusStartOemSpecific         = 0x80
BootInformationStatusStartProductSpecific     = 0xC0
MISC_BOOT_INFORMATION_STATUS_DATA_TYPE = ENUM

class SMBIOS_TABLE_TYPE32 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",         SMBIOS_STRUCTURE),
    ("Reserved",    UINT8 * 6),
    ("BootStatus",  UINT8)
  ]

class SMBIOS_TABLE_TYPE33 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                     SMBIOS_STRUCTURE),
    ("ErrorType",               UINT8),
    ("ErrorGranularity",        UINT8),
    ("ErrorOperation",          UINT8),
    ("VendorSyndrome",          UINT32),
    ("MemoryArrayErrorAddress", UINT64),
    ("DeviceErrorAddress",      UINT64),
    ("ErrorResolution",         UINT32)
  ]

ManagementDeviceTypeOther      = 0x01
ManagementDeviceTypeUnknown    = 0x02
ManagementDeviceTypeLm75       = 0x03
ManagementDeviceTypeLm78       = 0x04
ManagementDeviceTypeLm79       = 0x05
ManagementDeviceTypeLm80       = 0x06
ManagementDeviceTypeLm81       = 0x07
ManagementDeviceTypeAdm9240    = 0x08
ManagementDeviceTypeDs1780     = 0x09
ManagementDeviceTypeMaxim1617  = 0x0A
ManagementDeviceTypeGl518Sm    = 0x0B
ManagementDeviceTypeW83781D    = 0x0C
ManagementDeviceTypeHt82H791   = 0x0D
MISC_MANAGEMENT_DEVICE_TYPE = ENUM

ManagementDeviceAddressTypeOther   = 0x01
ManagementDeviceAddressTypeUnknown = 0x02
ManagementDeviceAddressTypeIOPort  = 0x03
ManagementDeviceAddressTypeMemory  = 0x04
ManagementDeviceAddressTypeSmbus   = 0x05
MISC_MANAGEMENT_DEVICE_ADDRESS_TYPE = ENUM

class SMBIOS_TABLE_TYPE34 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",         SMBIOS_STRUCTURE),
    ("Description", SMBIOS_TABLE_STRING),
    ("Type",        UINT8),
    ("Address",     UINT32),
    ("AddressType", UINT8)
  ]

class SMBIOS_TABLE_TYPE35 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                     SMBIOS_STRUCTURE),
    ("Description",             SMBIOS_TABLE_STRING),
    ("ManagementDeviceHandle",  UINT16),
    ("ComponentHandle",         UINT16),
    ("ThresholdHandle",         UINT16)
  ]

class SMBIOS_TABLE_TYPE36 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                           SMBIOS_STRUCTURE),
    ("LowerThresholdNonCritical",     UINT16),
    ("UpperThresholdNonCritical",     UINT16),
    ("LowerThresholdCritical",        UINT16),
    ("UpperThresholdCritical",        UINT16),
    ("LowerThresholdNonRecoverable",  UINT16),
    ("UpperTresholdNonRecoverable",   UINT16)
  ]                                    

class MEMORY_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceLoad",    UINT8),
    ("DeviceHandle",  UINT16)
  ]                                    

MemoryChannelTypeOther       = 0x01
MemoryChannelTypeUnknown     = 0x02
MemoryChannelTypeRambus      = 0x03
MemoryChannelTypeSyncLink    = 0x04
MEMORY_CHANNEL_TYPE = ENUM

class SMBIOS_TABLE_TYPE37 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 SMBIOS_STRUCTURE),
    ("ChannelType",         UINT8),
    ("MaximumChannelLoad",  UINT8),
    ("MemoryDeviceCount",   UINT8),
    ("MemoryDevice",        MEMORY_DEVICE * 1)
  ]                                    

IPMIDeviceInfoInterfaceTypeUnknown       = 0x00
IPMIDeviceInfoInterfaceTypeKCS           = 0x01
IPMIDeviceInfoInterfaceTypeSMIC          = 0x02
IPMIDeviceInfoInterfaceTypeBT            = 0x03
IPMIDeviceInfoInterfaceTypeReserved      = 0x04
BMC_INTERFACE_TYPE = ENUM

class SMBIOS_TABLE_TYPE38 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                               SMBIOS_STRUCTURE),
    ("InterfaceType",                     UINT8),
    ("IPMISpecificationRevision",         UINT8),
    ("I2CSlaveAddress",                   UINT8),
    ("NVStorageDeviceAddress",            UINT8),
    ("BaseAddress",                       UINT64),
    ("BaseAddressModifier_InterruptInfo", UINT8),
    ("InterruptNumber",                   UINT8)
  ]                                    

class SYS_POWER_SUPPLY_CHARACTERISTICS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerSupplyHotReplaceable", UINT16, 1),
    ("PowerSupplyPresent",        UINT16, 1),
    ("PowerSupplyUnplugged",      UINT16, 1),
    ("InputVoltageRangeSwitch",   UINT16, 4),
    ("PowerSupplyStatus",         UINT16, 3),
    ("PowerSupplyType",           UINT16, 4),
    ("Reserved",                  UINT16, 2)
  ]                                    

class SMBIOS_TABLE_TYPE39 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                         SMBIOS_STRUCTURE),
    ("PowerUnitGroup",              UINT8),
    ("Location",                    SMBIOS_TABLE_STRING),
    ("DeviceName",                  SMBIOS_TABLE_STRING),
    ("Manufacturer",                SMBIOS_TABLE_STRING),
    ("SerialNumber",                SMBIOS_TABLE_STRING),
    ("AssetTagNumber",              SMBIOS_TABLE_STRING),
    ("ModelPartNumber",             SMBIOS_TABLE_STRING),
    ("RevisionLevel",               SMBIOS_TABLE_STRING),
    ("MaxPowerCapacity",            UINT16),
    ("PowerSupplyCharacteristics",  SYS_POWER_SUPPLY_CHARACTERISTICS),
    ("InputVoltageProbeHandle",     UINT16),
    ("CoolingDeviceHandle",         UINT16),
    ("InputCurrentProbeHandle",     UINT16)
  ]

class ADDITIONAL_INFORMATION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryLength",       UINT8),
    ("ReferencedHandle",  UINT16),
    ("ReferencedOffset",  UINT8),
    ("EntryString",       SMBIOS_TABLE_STRING),
    ("Value",             UINT8 * 1)
  ]

class SMBIOS_TABLE_TYPE40 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                                   SMBIOS_STRUCTURE),
    ("NumberOfAdditionalInformationEntries",  UINT8),
    ("AdditionalInfoEntries",                 ADDITIONAL_INFORMATION_ENTRY * 1)
  ]

OnBoardDeviceExtendedTypeOther          = 0x01
OnBoardDeviceExtendedTypeUnknown        = 0x02
OnBoardDeviceExtendedTypeVideo          = 0x03
OnBoardDeviceExtendedTypeScsiController = 0x04
OnBoardDeviceExtendedTypeEthernet       = 0x05
OnBoardDeviceExtendedTypeTokenRing      = 0x06
OnBoardDeviceExtendedTypeSound          = 0x07
OnBoardDeviceExtendedTypePATAController = 0x08
OnBoardDeviceExtendedTypeSATAController = 0x09
OnBoardDeviceExtendedTypeSASController  = 0x0A
OnBoardDeviceExtendedTypeWirelessLAN    = 0x0B
OnBoardDeviceExtendedTypeBluetooth      = 0x0C
OnBoardDeviceExtendedTypeWWAN           = 0x0D
OnBoardDeviceExtendedTypeeMMC           = 0x0E
OnBoardDeviceExtendedTypeNvme           = 0x0F
OnBoardDeviceExtendedTypeUfc            = 0x10
ONBOARD_DEVICE_EXTENDED_INFO_TYPE = ENUM

class SMBIOS_TABLE_TYPE41 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                   SMBIOS_STRUCTURE),
    ("ReferenceDesignation",  SMBIOS_TABLE_STRING),
    ("DeviceType",            UINT8),
    ("DeviceTypeInstance",    UINT8),
    ("SegmentGroupNum",       UINT16),
    ("BusNum",                UINT8),
    ("DevFuncNum",            UINT8)
  ]

class MC_HOST_INTERFACE_PROTOCOL_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ProtocolType",        UINT8),
    ("ProtocolTypeDataLen", UINT8),
    ("ProtocolTypeData",    UINT8 * 1)
  ]

MCHostInterfaceTypeNetworkHostInterface = 0x40
MCHostInterfaceTypeOemDefined           = 0xF0
MC_HOST_INTERFACE_TYPE = ENUM

MCHostInterfaceProtocolTypeIPMI          = 0x02
MCHostInterfaceProtocolTypeMCTP          = 0x03
MCHostInterfaceProtocolTypeRedfishOverIP = 0x04
MCHostInterfaceProtocolTypeOemDefined    = 0xF0
MC_HOST_INTERFACE_PROTOCOL_TYPE          = ENUM

class SMBIOS_TABLE_TYPE42 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                             SMBIOS_STRUCTURE),
    ("InterfaceType",                   UINT8),
    ("InterfaceTypeSpecificDataLength", UINT8),
    ("InterfaceTypeSpecificData",       UINT8 * 4)
  ]

ProcessorSpecificBlockArchTypeReserved    = 0x00
ProcessorSpecificBlockArchTypeIa32        = 0x01
ProcessorSpecificBlockArchTypeX64         = 0x02
ProcessorSpecificBlockArchTypeItanium     = 0x03
ProcessorSpecificBlockArchTypeAarch32     = 0x04
ProcessorSpecificBlockArchTypeAarch64     = 0x05
ProcessorSpecificBlockArchTypeRiscVRV32   = 0x06
ProcessorSpecificBlockArchTypeRiscVRV64   = 0x07
ProcessorSpecificBlockArchTypeRiscVRV128  = 0x08
ProcessorSpecificBlockArchTypeLoongArch32 = 0x09
ProcessorSpecificBlockArchTypeLoongArch64 = 0x0A
PROCESSOR_SPECIFIC_BLOCK_ARCH_TYPE        = ENUM

class PROCESSOR_SPECIFIC_BLOCK (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",              UINT8),
    ("ProcessorArchType",   UINT8)
  ]

class SMBIOS_TABLE_TYPE44 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                     SMBIOS_STRUCTURE),
    ("RefHandle",               SMBIOS_HANDLE),
    ("ProcessorSpecificBlock",  PROCESSOR_SPECIFIC_BLOCK)
  ]

class SMBIOS_TABLE_TYPE43 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 SMBIOS_STRUCTURE),
    ("VendorID",            UINT8 * 4),
    ("MajorSpecVersion",    UINT8),
    ("MinorSpecVersion",    UINT8),
    ("FirmwareVersion1",    UINT32),
    ("FirmwareVersion2",    UINT32),
    ("Description",         SMBIOS_TABLE_STRING),
    ("Characteristics",     UINT64),
    ("OemDefined",          UINT32)
  ]

VersionFormatTypeFreeForm   = 0x00
VersionFormatTypeMajorMinor = 0x01
VersionFormatType32BitHex   = 0x02
VersionFormatType64BitHex   = 0x03
VersionFormatTypeReserved   = 0x04  # 0x04 - 0x7F are reserved
VersionFormatTypeOem        = 0x80  # 0x80 - 0xFF are BIOS Vendor/OEM-specific
FIRMWARE_INVENTORY_VERSION_FORMAT_TYPE = ENUM

FirmwareIdFormatTypeFreeForm     = 0x00
FirmwareIdFormatTypeUuid         = 0x01
FirmwareIdFormatTypeReserved     = 0x04  # 0x04 - 0x7F are reserved
InventoryFirmwareIdFormatTypeOem = 0x80  # 0x80 - 0xFF are BIOS Vendor/OEM-specific
FIRMWARE_INVENTORY_FIRMWARE_ID_FORMAT_TYPE = ENUM

class FIRMWARE_CHARACTERISTICS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Updatable",       UINT16, 1),
    ("WriteProtected",  UINT16, 1),
    ("Reserved",        UINT16, 14)
  ]

FirmwareInventoryStateOther              = 0x01
FirmwareInventoryStateUnknown            = 0x02
FirmwareInventoryStateDisabled           = 0x03
FirmwareInventoryStateEnabled            = 0x04
FirmwareInventoryStateAbsent             = 0x05
FirmwareInventoryStateStandbyOffline     = 0x06
FirmwareInventoryStateStandbySpare       = 0x07
FirmwareInventoryStateUnavailableOffline = 0x08
FIRMWARE_INVENTORY_STATE = ENUM

class SMBIOS_TABLE_TYPE45 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                         SMBIOS_STRUCTURE),
    ("FirmwareComponentName",       SMBIOS_TABLE_STRING),
    ("FirmwareVersion",             SMBIOS_TABLE_STRING),
    ("FirmwareVersionFormat",       UINT8),
    ("FirmwareId",                  SMBIOS_TABLE_STRING),
    ("FirmwareIdFormat",            UINT8),
    ("ReleaseDate",                 SMBIOS_TABLE_STRING),
    ("Manufacturer",                SMBIOS_TABLE_STRING),
    ("LowestSupportedVersion",      SMBIOS_TABLE_STRING),
    ("ImageSize",                   UINT64),
    ("Characteristics",             FIRMWARE_CHARACTERISTICS),
    ("State",                       UINT8),
    ("AssociatedComponentCount",    UINT8)
  ]

StringPropertyIdNone       = 0x0000
StringPropertyIdDevicePath = 0x0001
StringPropertyIdReserved   = 0x0002  # Reserved    0x0002 - 0x7FFF
StringPropertyIdBiosVendor = 0x8000  # BIOS vendor 0x8000 - 0xBFFF
StringPropertyIdOem        = 0xC000  # OEM range   0xC000 - 0xFFFF
STRING_PROPERTY_ID         = ENUM

class SMBIOS_TABLE_TYPE46 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 SMBIOS_STRUCTURE),
    ("StringPropertyId",    UINT16),
    ("StringPropertyValue", SMBIOS_TABLE_STRING),
    ("ParentHandle",        SMBIOS_HANDLE),
  ]

class SMBIOS_TABLE_TYPE126 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr", SMBIOS_STRUCTURE)
  ]

class SMBIOS_TABLE_TYPE127 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr", SMBIOS_STRUCTURE)
  ]

class SMBIOS_TABLE_OEM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr", SMBIOS_STRUCTURE)
  ]

class SMBIOS_STRUCTURE_POINTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Hdr",     POINTER (SMBIOS_STRUCTURE)),
    ("Type0",   POINTER (SMBIOS_TABLE_TYPE0)),
    ("Type1",   POINTER (SMBIOS_TABLE_TYPE1)),
    ("Type2",   POINTER (SMBIOS_TABLE_TYPE2)),
    ("Type3",   POINTER (SMBIOS_TABLE_TYPE3)),
    ("Type4",   POINTER (SMBIOS_TABLE_TYPE4)),
    ("Type5",   POINTER (SMBIOS_TABLE_TYPE5)),
    ("Type6",   POINTER (SMBIOS_TABLE_TYPE6)),
    ("Type7",   POINTER (SMBIOS_TABLE_TYPE7)),
    ("Type8",   POINTER (SMBIOS_TABLE_TYPE8)),
    ("Type9",   POINTER (SMBIOS_TABLE_TYPE9)),
    ("Type10",  POINTER (SMBIOS_TABLE_TYPE10)),
    ("Type11",  POINTER (SMBIOS_TABLE_TYPE11)),
    ("Type12",  POINTER (SMBIOS_TABLE_TYPE12)),
    ("Type13",  POINTER (SMBIOS_TABLE_TYPE13)),
    ("Type14",  POINTER (SMBIOS_TABLE_TYPE14)),
    ("Type15",  POINTER (SMBIOS_TABLE_TYPE15)),
    ("Type16",  POINTER (SMBIOS_TABLE_TYPE16)),
    ("Type17",  POINTER (SMBIOS_TABLE_TYPE17)),
    ("Type18",  POINTER (SMBIOS_TABLE_TYPE18)),
    ("Type19",  POINTER (SMBIOS_TABLE_TYPE19)),
    ("Type20",  POINTER (SMBIOS_TABLE_TYPE20)),
    ("Type21",  POINTER (SMBIOS_TABLE_TYPE21)),
    ("Type22",  POINTER (SMBIOS_TABLE_TYPE22)),
    ("Type23",  POINTER (SMBIOS_TABLE_TYPE23)),
    ("Type24",  POINTER (SMBIOS_TABLE_TYPE24)),
    ("Type25",  POINTER (SMBIOS_TABLE_TYPE25)),
    ("Type26",  POINTER (SMBIOS_TABLE_TYPE26)),
    ("Type27",  POINTER (SMBIOS_TABLE_TYPE27)),
    ("Type28",  POINTER (SMBIOS_TABLE_TYPE28)),
    ("Type29",  POINTER (SMBIOS_TABLE_TYPE29)),
    ("Type30",  POINTER (SMBIOS_TABLE_TYPE30)),
    ("Type31",  POINTER (SMBIOS_TABLE_TYPE31)),
    ("Type32",  POINTER (SMBIOS_TABLE_TYPE32)),
    ("Type33",  POINTER (SMBIOS_TABLE_TYPE33)),
    ("Type34",  POINTER (SMBIOS_TABLE_TYPE34)),
    ("Type35",  POINTER (SMBIOS_TABLE_TYPE35)),
    ("Type36",  POINTER (SMBIOS_TABLE_TYPE36)),
    ("Type37",  POINTER (SMBIOS_TABLE_TYPE37)),
    ("Type38",  POINTER (SMBIOS_TABLE_TYPE38)),
    ("Type39",  POINTER (SMBIOS_TABLE_TYPE39)),
    ("Type40",  POINTER (SMBIOS_TABLE_TYPE40)),
    ("Type41",  POINTER (SMBIOS_TABLE_TYPE41)),
    ("Type42",  POINTER (SMBIOS_TABLE_TYPE42)),
    ("Type43",  POINTER (SMBIOS_TABLE_TYPE43)),
    ("Type44",  POINTER (SMBIOS_TABLE_TYPE44)),
    ("Type45",  POINTER (SMBIOS_TABLE_TYPE45)),
    ("Type46",  POINTER (SMBIOS_TABLE_TYPE46)),
    ("Type126", POINTER (SMBIOS_TABLE_TYPE126)),
    ("Type127", POINTER (SMBIOS_TABLE_TYPE127)),
    ("Oem",     POINTER (SMBIOS_TABLE_OEM))
  ]

