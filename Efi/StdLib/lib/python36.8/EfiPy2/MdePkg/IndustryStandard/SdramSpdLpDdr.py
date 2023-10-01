# SdramSpdLpDdr.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpdLpDdr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BytesUsed",   UINT8, 4),
    ("BytesTotal",  UINT8, 3),
    ("CrcCoverage", UINT8, 1)
    ]

class SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_REVISION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Minor",   UINT8, 4),
    ("Major",   UINT8, 4)
    ]

class SPD_LPDDR_REVISION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_REVISION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8, 8)
    ]

class SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleType",  UINT8, 4),
    ("HybridMedia", UINT8, 3),
    ("Hybrid",      UINT8, 1)
    ]

class SPD_LPDDR_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Density",     UINT8, 4),
    ("BankAddress", UINT8, 2),
    ("BankGroup",   UINT8, 2)
    ]

class SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_SDRAM_ADDRESSING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ColumnAddress",   UINT8, 3),
    ("RowAddress",      UINT8, 3),
    ("Reserved",        UINT8, 2)
    ]

class SPD_LPDDR_SDRAM_ADDRESSING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_ADDRESSING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",       UINT8, 2),
    ("ChannelsPerDie",      UINT8, 2),
    ("DieCount",            UINT8, 3),
    ("SdramPackageType",    UINT8, 1),
    ]

class SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaximumActivateCount",    UINT8, 4),
    ("MaximumActivateWindow",   UINT8, 2),
    ("Reserved",                UINT8, 2)
    ]

class SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 8)
    ]

class SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 5),
    ("SoftPPR",             UINT8, 1),
    ("PostPackageRepair",   UINT8, 2)
    ]

class SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OperationAt1_20",     UINT8, 1),
    ("EndurantAt1_20",      UINT8, 1),
    ("OperationAt1_10",     UINT8, 1),
    ("EndurantAt1_10",      UINT8, 1),
    ("OperationAtTBD2V",    UINT8, 1),
    ("EndurantAtTBD2V",     UINT8, 1),
    ("Reserved",            UINT8, 2)
    ]

class SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_MODULE_ORGANIZATION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdramDeviceWidth",    UINT8, 3),
    ("RankCount",           UINT8, 3),
    ("Reserved",            UINT8, 2)
    ]

class SPD_LPDDR_MODULE_ORGANIZATION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_ORGANIZATION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PrimaryBusWidth",     UINT8, 3),
    ("BusWidthExtension",   UINT8, 2),
    ("NumberofChannels",    UINT8, 3)
    ]

class SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 7),
    ("ThermalSensorPresence",   UINT8, 1)
    ]

class SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedBaseModuleType",  UINT8, 4),
    ("Reserved",                UINT8, 4)
    ]

class SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_SIGNAL_LOADING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChipSelectLoading",                   UINT8, 3),
    ("CommandAddressControlClockLoading",   UINT8, 3),
    ("DataStrobeMaskLoading",               UINT8, 2)
    ]

class SPD_LPDDR_SIGNAL_LOADING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SIGNAL_LOADING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TIMEBASE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fine",        UINT8, 2),
    ("Medium",      UINT8, 2),
    ("Reserved",    UINT8, 4)
    ]

class SPD_LPDDR_TIMEBASE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TIMEBASE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TCK_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmin",  UINT8, 8)
    ]

class SPD_LPDDR_TCK_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TCK_MAX_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmax",  UINT8, 8)
    ]

class SPD_LPDDR_TCK_MAX_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MAX_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl3",         UINT32, 1),
    ("Cl6",         UINT32, 1),
    ("Cl8",         UINT32, 1),
    ("Cl9",         UINT32, 1),
    ("Cl10",        UINT32, 1),
    ("Cl11",        UINT32, 1),
    ("Cl12",        UINT32, 1),
    ("Cl14",        UINT32, 1),
    ("Cl16",        UINT32, 1),
    ("Reserved0",   UINT32, 1),
    ("Cl20",        UINT32, 1),
    ("Cl22",        UINT32, 1),
    ("Cl24",        UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("Cl28",        UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("Cl32",        UINT32, 1),
    ("Reserved3",   UINT32, 1),
    ("Cl36",        UINT32, 1),
    ("Reserved4",   UINT32, 1),
    ("Cl40",        UINT32, 1),
    ("Reserved5",   UINT32, 11)
    ]

class SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT_Bits),
    ("Data",    UINT32),
    ("Data16",  UINT16 * 2),
    ("Data8",   UINT8  * 4)
    ]

class SPD_LPDDR_TAA_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAmin",  UINT8, 8)
    ]

class SPD_LPDDR_TAA_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TAA_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_RW_LATENCY_OPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReadLatencyMode", UINT8, 2),
    ("WriteLatencySet", UINT8, 2),
    ("Reserved",        UINT8, 4)
    ]

class SPD_LPDDR_RW_LATENCY_OPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_RW_LATENCY_OPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TRCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDmin", UINT8, 8)
    ]

class SPD_LPDDR_TRCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TRP_AB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPab",   UINT8, 8)
    ]

class SPD_LPDDR_TRP_AB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_AB_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TRP_PB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPpb",   UINT8, 8)
    ]

class SPD_LPDDR_TRP_PB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_PB_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TRFC_AB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCab",  UINT16, 16)
    ]

class SPD_LPDDR_TRFC_AB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRFC_AB_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD_LPDDR_TRFC_PB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCpb",  UINT16, 16)
    ]

class SPD_LPDDR_TRFC_PB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRFC_PB_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BitOrderatSDRAM",         UINT8, 5),
    ("WiredtoUpperLowerNibble", UINT8, 1),
    ("PackageRankMap",          UINT8, 2),
    ]

class SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_TRP_PB_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPpbFine",  INT8, 8)
    ]

class SPD_LPDDR_TRP_PB_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_PB_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD_LPDDR_TRP_AB_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPabFine",  INT8, 8)
    ]

class SPD_LPDDR_TRP_AB_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_AB_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD_LPDDR_TRCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDminFine", INT8, 8)
    ]

class SPD_LPDDR_TRCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD_LPDDR_TAA_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAminFine",  INT8, 8)
    ]

class SPD_LPDDR_TAA_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TAA_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD_LPDDR_TCK_MAX_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmaxFine",  INT8, 8)
    ]

class SPD_LPDDR_TCK_MAX_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MAX_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD_LPDDR_TCK_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKminFine",  INT8, 8)
    ]

class SPD_LPDDR_TCK_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD_LPDDR_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD_LPDDR_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2),
    ]

class SPD_LPDDR_MANUFACTURING_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Location",   UINT8)
    ]

class SPD_LPDDR_MANUFACTURING_DATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Year",   UINT8),
    ("Week",   UINT8)
    ]

class SPD_LPDDR_MANUFACTURER_SERIAL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data",            UINT32),
    ("SerialNumber16",  UINT16 * 2),
    ("SerialNumber8",   UINT8  * 4)
    ]

class SPD_LPDDR_UNIQUE_MODULE_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdCode",          SPD_LPDDR_MANUFACTURER_ID_CODE),
    ("Location",        SPD_LPDDR_MANUFACTURING_LOCATION),
    ("Date",            SPD_LPDDR_MANUFACTURING_DATE),
    ("SerialNumber",    SPD_LPDDR_MANUFACTURER_SERIAL_NUMBER)
    ]

class SPD_LPDDR_MODULE_MAXIMUM_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD_LPDDR_MODULE_MAXIMUM_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_MAXIMUM_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",              UINT8, 5),
    ("RawCardExtension",    UINT8, 3)
    ]

class SPD_LPDDR_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD_LPDDR_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD_LPDDR_CYCLIC_REDUNDANCY_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Crc",     UINT16 * 1),
    ("Data8",   UINT8  * 2)
    ]

class SPD_LPDDR_BASE_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Description",                 SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT           ),
    ("Revision",                    SPD_LPDDR_REVISION_STRUCT                     ),
    ("DramDeviceType",              SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT             ),
    ("ModuleType",                  SPD_LPDDR_MODULE_TYPE_STRUCT                  ),
    ("SdramDensityAndBanks",        SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT          ),
    ("SdramAddressing",             SPD_LPDDR_SDRAM_ADDRESSING_STRUCT             ),
    ("SdramPackageType",            SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT           ),
    ("SdramOptionalFeatures",       SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT      ),
    ("ThermalAndRefreshOptions",    SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT        ),
    ("OtherOptionalFeatures",       SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT),
    ("Reserved0",                   UINT8                                         ),
    ("ModuleNominalVoltage",        SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT       ),
    ("ModuleOrganization",          SPD_LPDDR_MODULE_ORGANIZATION_STRUCT          ),
    ("ModuleMemoryBusWidth",        SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT      ),
    ("ModuleThermalSensor",         SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT        ),
    ("ExtendedModuleType",          SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT         ),
    ("SignalLoading",               SPD_LPDDR_SIGNAL_LOADING_STRUCT               ),
    ("Timebase",                    SPD_LPDDR_TIMEBASE_STRUCT                     ),
    ("tCKmin",                      SPD_LPDDR_TCK_MIN_MTB_STRUCT                  ),
    ("tCKmax",                      SPD_LPDDR_TCK_MAX_MTB_STRUCT                  ),
    ("CasLatencies",                SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT      ),
    ("tAAmin",                      SPD_LPDDR_TAA_MIN_MTB_STRUCT                  ),
    ("LatencySetOptions",           SPD_LPDDR_RW_LATENCY_OPTION_STRUCT            ),
    ("tRCDmin",                     SPD_LPDDR_TRCD_MIN_MTB_STRUCT                 ),
    ("tRPab",                       SPD_LPDDR_TRP_AB_MTB_STRUCT                   ),
    ("tRPpb",                       SPD_LPDDR_TRP_PB_MTB_STRUCT                   ),
    ("tRFCab",                      SPD_LPDDR_TRFC_AB_MTB_STRUCT                  ),
    ("tRFCpb",                      SPD_LPDDR_TRFC_PB_MTB_STRUCT                  ),
    ("Reserved1",                   UINT8 * (59 - 33 + 1)                         ),
    ("BitMapping",                  SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT * (77 - 60 + 1)),
    ("Reserved2",                   UINT8 * (119 - 78 + 1)                        ),
    ("tRPpbFine",                   SPD_LPDDR_TRP_PB_FTB_STRUCT                   ),
    ("tRPabFine",                   SPD_LPDDR_TRP_AB_FTB_STRUCT                   ),
    ("tRCDminFine",                 SPD_LPDDR_TRCD_MIN_FTB_STRUCT                 ),
    ("tAAminFine",                  SPD_LPDDR_TAA_MIN_FTB_STRUCT                  ),
    ("tCKmaxFine",                  SPD_LPDDR_TCK_MAX_FTB_STRUCT                  ),
    ("tCKminFine",                  SPD_LPDDR_TCK_MIN_FTB_STRUCT                  ),
    ("Crc",                         SPD_LPDDR_CYCLIC_REDUNDANCY_CODE              )
    ]

class SPD_LPDDR_MODULE_LPDIMM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",     SPD_LPDDR_MODULE_NOMINAL_HEIGHT   ),
    ("ModuleMaximumThickness",  SPD_LPDDR_MODULE_MAXIMUM_THICKNESS),
    ("ReferenceRawCardUsed",    SPD_LPDDR_REFERENCE_RAW_CARD      ),
    ("Reserved",                UINT8 * (253 - 131 + 1)           ),
    ("Crc",                     SPD_LPDDR_CYCLIC_REDUNDANCY_CODE  )
    ]

class SPD_LPDDR_MODULE_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LpDimm",  SPD_LPDDR_MODULE_LPDIMM)
    ]

class SPD_LPDDR_MODULE_PART_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModulePartNumber",  UINT8 * (348 - 329 + 1))
    ]

class SPD_LPDDR_MANUFACTURER_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ManufacturerSpecificData",  UINT8 * (381 - 353 + 1))
    ]

SPD_LPDDR_MODULE_REVISION_CODE  = UINT8
SPD_LPDDR_DRAM_STEPPING         = UINT8

class SPD_LPDDR_MANUFACTURING_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleId",                    SPD_LPDDR_UNIQUE_MODULE_ID     ),
    ("ModulePartNumber",            SPD_LPDDR_MODULE_PART_NUMBER   ),
    ("ModuleRevisionCode",          SPD_LPDDR_MODULE_REVISION_CODE ),
    ("DramIdCode",                  SPD_LPDDR_MANUFACTURER_ID_CODE ),
    ("DramStepping",                SPD_LPDDR_DRAM_STEPPING        ),
    ("ManufacturerSpecificData",    SPD_LPDDR_MANUFACTURER_SPECIFIC),
    ("Reserved",                    UINT8 * (383 - 382 + 1)        )
    ]

class SPD_LPDDR_END_USER_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8 * (511 - 384 + 1))
    ]

class SPD_LPDDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Base",            SPD_LPDDR_BASE_SECTION      ),
    ("Module",          SPD_LPDDR_MODULE_SPECIFIC   ),
    ("Reserved",        UINT8 * (319 - 256 + 1)     ),
    ("ManufactureInfo", SPD_LPDDR_MANUFACTURING_DATA),
    ("EndUser",         SPD_LPDDR_END_USER_SECTION  )
    ]

