# SdramSpdDdr4.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpdDdr4
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class SPD4_DEVICE_DESCRIPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BytesUsed",   UINT8, 4),
    ("BytesTotal",  UINT8, 3),
    ("CrcCoverage", UINT8, 1)
    ]

class SPD4_DEVICE_DESCRIPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_DEVICE_DESCRIPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_REVISION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Minor",   UINT8, 4),
    ("Major",   UINT8, 4)
    ]

class SPD4_REVISION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_REVISION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_DRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8, 8)
    ]

class SPD4_DRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_DRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleType",  UINT8, 4),
    ("HybridMedia", UINT8, 3),
    ("Hybrid",      UINT8, 1)
    ]

class SPD4_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_SDRAM_DENSITY_BANKS_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Density",     UINT8, 4),
    ("BankAddress", UINT8, 2),
    ("BankGroup",   UINT8, 2)
    ]

class SPD4_SDRAM_DENSITY_BANKS_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_DENSITY_BANKS_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_SDRAM_ADDRESSING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ColumnAddress",   UINT8, 3),
    ("RowAddress",      UINT8, 3),
    ("Reserved",        UINT8, 2)
    ]

class SPD4_SDRAM_ADDRESSING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_ADDRESSING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",       UINT8, 2),
    ("Reserved",            UINT8, 2),
    ("DieCount",            UINT8, 3),
    ("SdramPackageType",    UINT8, 1),
    ]

class SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaximumActivateCount",    UINT8, 4),
    ("MaximumActivateWindow",   UINT8, 2),
    ("Reserved",                UINT8, 2)
    ]

class SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_SDRAM_THERMAL_REFRESH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 8)
    ]

class SPD4_SDRAM_THERMAL_REFRESH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_THERMAL_REFRESH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 5),
    ("SoftPPR",             UINT8, 1),
    ("PostPackageRepair",   UINT8, 2)
    ]

class SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",       UINT8, 2),
    ("DRAMDensityRatio",    UINT8, 2),
    ("DieCount",            UINT8, 3),
    ("SdramPackageType",    UINT8, 1)
    ]

class SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OperationAt1_20",     UINT8, 1),
    ("EndurantAt1_20",      UINT8, 1),
    ("Reserved",            UINT8, 6)
    ]

class SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_MODULE_ORGANIZATION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdramDeviceWidth",    UINT8, 3),
    ("RankCount",           UINT8, 3),
    ("RankMix",             UINT8, 1),
    ("Reserved",            UINT8, 1)
    ]

class SPD4_MODULE_ORGANIZATION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_ORGANIZATION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PrimaryBusWidth",     UINT8, 3),
    ("BusWidthExtension",   UINT8, 2),
    ("Reserved",            UINT8, 3)
    ]

class SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_MODULE_THERMAL_SENSOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 7),
    ("ThermalSensorPresence",   UINT8, 1)
    ]

class SPD4_MODULE_THERMAL_SENSOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_THERMAL_SENSOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_EXTENDED_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedBaseModuleType",  UINT8, 4),
    ("Reserved",                UINT8, 4)
    ]

class SPD4_EXTENDED_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_EXTENDED_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TIMEBASE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fine",        UINT8, 2),
    ("Medium",      UINT8, 2),
    ("Reserved",    UINT8, 4)
    ]

class SPD4_TIMEBASE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TIMEBASE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TCK_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmin",  UINT8, 8)
    ]

class SPD4_TCK_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TCK_MAX_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmax",  UINT8, 8)
    ]

class SPD4_TCK_MAX_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MAX_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl7",         UINT32, 1),
    ("Cl8",         UINT32, 1),
    ("Cl9",         UINT32, 1),
    ("Cl10",        UINT32, 1),
    ("Cl11",        UINT32, 1),
    ("Cl12",        UINT32, 1),
    ("Cl13",        UINT32, 1),
    ("Cl14",        UINT32, 1),
    ("Cl15",        UINT32, 1),
    ("Cl16",        UINT32, 1),
    ("Cl17",        UINT32, 1),
    ("Cl18",        UINT32, 1),
    ("Cl19",        UINT32, 1),
    ("Cl20",        UINT32, 1),
    ("Cl21",        UINT32, 1),
    ("Cl22",        UINT32, 1),
    ("Cl23",        UINT32, 1),
    ("Cl24",        UINT32, 1),
    ("Cl25",        UINT32, 1),
    ("Cl26",        UINT32, 1),
    ("Cl27",        UINT32, 1),
    ("Cl28",        UINT32, 1),
    ("Cl29",        UINT32, 1),
    ("Cl30",        UINT32, 1),
    ("Cl31",        UINT32, 1),
    ("Cl32",        UINT32, 1),
    ("Cl33",        UINT32, 1),
    ("Cl34",        UINT32, 1),
    ("Cl35",        UINT32, 1),
    ("Cl36",        UINT32, 1),
    ("Reserved",    UINT32, 1),
    ("ClRange",     UINT32, 1)
    ]

class SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_HighRangeBits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl23",        UINT32, 1),
    ("Cl24",        UINT32, 1),
    ("Cl25",        UINT32, 1),
    ("Cl26",        UINT32, 1),
    ("Cl27",        UINT32, 1),
    ("Cl28",        UINT32, 1),
    ("Cl29",        UINT32, 1),
    ("Cl30",        UINT32, 1),
    ("Cl31",        UINT32, 1),
    ("Cl32",        UINT32, 1),
    ("Cl33",        UINT32, 1),
    ("Cl34",        UINT32, 1),
    ("Cl35",        UINT32, 1),
    ("Cl36",        UINT32, 1),
    ("Cl37",        UINT32, 1),
    ("Cl38",        UINT32, 1),
    ("Cl39",        UINT32, 1),
    ("Cl40",        UINT32, 1),
    ("Cl41",        UINT32, 1),
    ("Cl42",        UINT32, 1),
    ("Cl43",        UINT32, 1),
    ("Cl44",        UINT32, 1),
    ("Cl45",        UINT32, 1),
    ("Cl46",        UINT32, 1),
    ("Cl47",        UINT32, 1),
    ("Cl48",        UINT32, 1),
    ("Cl49",        UINT32, 1),
    ("Cl50",        UINT32, 1),
    ("Cl51",        UINT32, 1),
    ("Cl52",        UINT32, 1),
    ("Reserved",    UINT32, 1),
    ("ClRange",     UINT32, 1)
    ]

class SPD4_CAS_LATENCIES_SUPPORTED_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_Bits),
    ("HighRangeBits",   SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_HighRangeBits),
    ("Data",            UINT32),
    ("Data16",          UINT16 * 2),
    ("Data8",           UINT8  * 4)
    ]

class SPD4_TAA_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAmin",  UINT8, 8)
    ]

class SPD4_TAA_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TAA_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDmin", UINT8, 8)
    ]

class SPD4_TRCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRP_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPmin",  UINT8, 8)
    ]

class SPD4_TRP_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRP_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRAS_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASminUpper",    UINT8, 4),
    ("tRCminUpper",     UINT8, 4)
    ]

class SPD4_TRAS_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRAS_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRAS_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASmin", UINT8, 8)
    ]

class SPD4_TRAS_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRAS_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCmin",  UINT8, 8)
    ]

class SPD4_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRFC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCmin", UINT16, 16)
    ]

class SPD4_TRFC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRFC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD4_TFAW_MIN_MTB_UPPER_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWminUpper",    UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class SPD4_TFAW_MIN_MTB_UPPER_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TFAW_MIN_MTB_UPPER_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TFAW_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWmin", UINT8, 8)
    ]

class SPD4_TFAW_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TFAW_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TRRD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRRDmin", UINT8, 8)
    ]

class SPD4_TRRD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRRD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TCCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCCDmin", UINT8, 8)
    ]

class SPD4_TCCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TWR_UPPER_NIBBLE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWRminMostSignificantNibble", UINT8, 4),
    ("Reserved",                    UINT8, 4)
    ]

class SPD4_TWR_UPPER_NIBBLE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWR_UPPER_NIBBLE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TWR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWRmin",  UINT8, 8)
    ]

class SPD4_TWR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TWTR_UPPER_NIBBLE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWTR_SminMostSignificantNibble", UINT8, 4),
    ("tWTR_LminMostSignificantNibble", UINT8, 4)
    ]

class SPD4_TWTR_UPPER_NIBBLE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWTR_UPPER_NIBBLE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TWTR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWTRmin", UINT8, 8)
    ]

class SPD4_TWTR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWTR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BitOrderatSDRAM",         UINT8, 5),
    ("WiredtoUpperLowerNibble", UINT8, 1),
    ("PackageRankMap",          UINT8, 2),
    ]

class SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_TCCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCCDminFine", INT8, 8)
    ]

class SPD4_TCCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TRRD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRRDminFine", INT8, 8)
    ]

class SPD4_TRRD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRRD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TRC_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCminFine",  INT8, 8)
    ]

class SPD4_TRC_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRC_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TRP_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPminFine",  INT8, 8)
    ]

class SPD4_TRP_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRP_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TRCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDminFine", INT8, 8)
    ]

class SPD4_TRCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TAA_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAminFine",  INT8, 8)
    ]

class SPD4_TAA_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TAA_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TCK_MAX_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmaxFine",  INT8, 8)
    ]

class SPD4_TCK_MAX_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MAX_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_TCK_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKminFine",  INT8, 8)
    ]

class SPD4_TCK_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD4_UNBUF_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",              UINT8, 5),
    ("RawCardExtension",    UINT8, 3)
    ]

class SPD4_UNBUF_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_UNBUF_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD4_UNBUF_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD4_UNBUF_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1),
    ]

class SPD4_UNBUF_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD4_UNBUF_ADDRESS_MAPPING_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MappingRank1",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD4_UNBUF_ADDRESS_MAPPING (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_ADDRESS_MAPPING_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD4_RDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD4_RDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD4_RDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD4_RDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeatSpreaderThermalCharacteristics",  UINT8, 7),
    ("HeatSpreaderSolution",                UINT8, 1)
    ]

class SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits),
    ("Data",    UINT8)
    ]

class SPD4_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD4_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD4_RDIMM_REGISTER_REVISION_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterRevisionNumber",  UINT8, 8)
    ]

class SPD4_RDIMM_REGISTER_REVISION_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REGISTER_REVISION_NUMBER_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rank1Mapping",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cke",             UINT8, 2),
    ("Odt",             UINT8, 2),
    ("CommandAddress",  UINT8, 2),
    ("ChipSelect",      UINT8, 2)
    ]

class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits),
    ("Data",    UINT8)
    ]

class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Y0Y2",                        UINT8, 2),
    ("Y1Y3",                        UINT8, 2),
    ("Reserved0",                   UINT8, 2),
    ("RcdOutputSlewRateControl",    UINT8, 1),
    ("Reserved1",                   UINT8, 1)
    ]

class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD4_LRDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD4_LRDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeatSpreaderThermalCharacteristics",  UINT8, 7),
    ("HeatSpreaderSolution",                UINT8, 1)
    ]

class SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_REGISTER_REVISION_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterRevisionNumber",  UINT8, 8)
    ]

class SPD4_LRDIMM_REGISTER_REVISION_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REGISTER_REVISION_NUMBER_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rank1Mapping",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cke",             UINT8, 2),
    ("Odt",             UINT8, 2),
    ("CommandAddress",  UINT8, 2),
    ("ChipSelect",      UINT8, 2)
    ]

class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Y0Y2",                        UINT8, 2),
    ("Y1Y3",                        UINT8, 2),
    ("Reserved0",                   UINT8, 2),
    ("RcdOutputSlewRateControl",    UINT8, 1),
    ("Reserved1",                   UINT8, 1)
    ]

class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DATA_BUFFER_REVISION_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBufferRevisionNumber",    UINT8)
    ]

class SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DramVrefDQForPackageRank0",   UINT8, 6),
    ("Reserved",                    UINT8, 2)
    ]

class SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBufferVrefDQforDramInterface",    UINT8)
    ]

class SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DramInterfaceMdqDriveStrength",           UINT8, 4),
    ("DramInterfaceMdqReadTerminationStrength", UINT8, 4)
    ]

class SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DRAM_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataRateLe1866",  UINT8, 2),
    ("DataRateLe2400",  UINT8, 2),
    ("DataRateLe3200",  UINT8, 2),
    ("Reserved",        UINT8, 2)
    ]

class SPD4_LRDIMM_DRAM_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rtt_Nom",     UINT8, 3),
    ("Rtt_WR",      UINT8, 3),
    ("Reserved",    UINT8, 2)
    ]

class SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PackageRanks0_1", UINT8, 3),
    ("PackageRanks2_3", UINT8, 3),
    ("Reserved",        UINT8, 2),
    ]

class SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rank0",       UINT8, 1),
    ("Rank1",       UINT8, 1),
    ("Rank2",       UINT8, 1),
    ("Rank3",       UINT8, 1),
    ("DataBuffer",  UINT8, 1),
    ("Reserved",    UINT8, 3)
    ]

class SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE_Bits),
    ("Data",    UINT8)
    ]

class SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBufferGainAdjustment",    UINT8, 1),
    ("DataBufferDfe",               UINT8, 1),
    ("Reserved",                    UINT8, 6)
    ]

class SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION_Bits),
    ("Data",    UINT8)
    ]

SPD4_NVDIMM_MODULE_PRODUCT_IDENTIFIER = UINT16

class SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_IDENTIFIER     = UINT16
SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_REVISION_CODE  = UINT8

class SPD4_NVDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD4_NVDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD4_NVDIMM_MODULE_CHARACTERISTICS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 4),
    ("Extension",   UINT8, 4)
    ]

class SPD4_NVDIMM_MODULE_CHARACTERISTICS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_MODULE_CHARACTERISTICS_Bits),
    ("Data",    UINT8)
    ]

class SPD4_NVDIMM_HYBRID_MODULE_MEDIA_TYPES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8),
    ("MediaType",   UINT8)
    ]

SPD4_NVDIMM_MAXIMUM_NONVOLATILE_MEMORY_INITIALIZATION_TIME = UINT8

class SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FunctionInterface",   UINT16, 5),
    ("FunctionClass",       UINT16, 5),
    ("BlockOffset",         UINT16, 4),
    ("Reserved",            UINT16, 1),
    ("Implemented",         UINT16, 1)
    ]

class SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD4_MANUFACTURING_DATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Year",    UINT8),
    ("Week",    UINT8)
    ]

class SPD4_MANUFACTURER_SERIAL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data",            UINT32),
    ("SerialNumber16",  UINT16 * 2),
    ("SerialNumber8",   UINT8  * 4)
    ]

class SPD4_MANUFACTURING_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Location",    UINT8)
    ]

class SPD4_UNIQUE_MODULE_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdCode",          SPD4_MANUFACTURER_ID_CODE      ),
    ("Location",        SPD4_MANUFACTURING_LOCATION    ),
    ("Date",            SPD4_MANUFACTURING_DATE        ),
    ("SerialNumber",    SPD4_MANUFACTURER_SERIAL_NUMBER)
    ]

class SPD4_CYCLIC_REDUNDANCY_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Crc",    UINT16 * 1),
    ("Data8",  UINT8  * 2)
    ]

class SPD4_BASE_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Description",                 SPD4_DEVICE_DESCRIPTION_STRUCT           ),
    ("Revision",                    SPD4_REVISION_STRUCT                     ),
    ("DramDeviceType",              SPD4_DRAM_DEVICE_TYPE_STRUCT             ),
    ("ModuleType",                  SPD4_MODULE_TYPE_STRUCT                  ),
    ("SdramDensityAndBanks",        SPD4_SDRAM_DENSITY_BANKS_STRUCT          ),
    ("SdramAddressing",             SPD4_SDRAM_ADDRESSING_STRUCT             ),
    ("PrimarySdramPackageType",     SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT   ),
    ("SdramOptionalFeatures",       SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT      ),
    ("ThermalAndRefreshOptions",    SPD4_SDRAM_THERMAL_REFRESH_STRUCT        ),
    ("OtherOptionalFeatures",       SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT),
    ("SecondarySdramPackageType",   SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT ),
    ("ModuleNominalVoltage",        SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT       ),
    ("ModuleOrganization",          SPD4_MODULE_ORGANIZATION_STRUCT          ),
    ("ModuleMemoryBusWidth",        SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT      ),
    ("ModuleThermalSensor",         SPD4_MODULE_THERMAL_SENSOR_STRUCT        ),
    ("ExtendedModuleType",          SPD4_EXTENDED_MODULE_TYPE_STRUCT         ),
    ("Reserved0",                   UINT8                                    ),
    ("Timebase",                    SPD4_TIMEBASE_STRUCT                     ),
    ("tCKmin",                      SPD4_TCK_MIN_MTB_STRUCT                  ),
    ("tCKmax",                      SPD4_TCK_MAX_MTB_STRUCT                  ),
    ("CasLatencies",                SPD4_CAS_LATENCIES_SUPPORTED_STRUCT      ),
    ("tAAmin",                      SPD4_TAA_MIN_MTB_STRUCT                  ),
    ("tRCDmin",                     SPD4_TRCD_MIN_MTB_STRUCT                 ),
    ("tRPmin",                      SPD4_TRP_MIN_MTB_STRUCT                  ),
    ("tRASMintRCMinUpper",          SPD4_TRAS_TRC_MIN_MTB_STRUCT             ),
    ("tRASmin",                     SPD4_TRAS_MIN_MTB_STRUCT                 ),
    ("tRCmin",                      SPD4_TRC_MIN_MTB_STRUCT                  ),
    ("tRFC1min",                    SPD4_TRFC_MIN_MTB_STRUCT                 ),
    ("tRFC2min",                    SPD4_TRFC_MIN_MTB_STRUCT                 ),
    ("tRFC4min",                    SPD4_TRFC_MIN_MTB_STRUCT                 ),
    ("tFAWMinUpper",                SPD4_TFAW_MIN_MTB_UPPER_STRUCT           ),
    ("tFAWmin",                     SPD4_TFAW_MIN_MTB_STRUCT                 ),
    ("tRRD_Smin",                   SPD4_TRRD_MIN_MTB_STRUCT                 ),
    ("tRRD_Lmin",                   SPD4_TRRD_MIN_MTB_STRUCT                 ),
    ("tCCD_Lmin",                   SPD4_TCCD_MIN_MTB_STRUCT                 ),
    ("tWRUpperNibble",              SPD4_TWR_UPPER_NIBBLE_STRUCT             ),
    ("tWRmin",                      SPD4_TWR_MIN_MTB_STRUCT                  ),
    ("tWTRUpperNibble",             SPD4_TWTR_UPPER_NIBBLE_STRUCT            ),
    ("tWTR_Smin",                   SPD4_TWTR_MIN_MTB_STRUCT                 ),
    ("tWTR_Lmin",                   SPD4_TWTR_MIN_MTB_STRUCT                 ),
    ("Reserved1",                   UINT8 * (59 - 46 + 1)                    ),
    ("BitMapping",                  SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT * (77 - 60 + 1)),
    ("Reserved2",                   UINT8 * (116 - 78 + 1)                   ),
    ("tCCD_LminFine",               SPD4_TCCD_MIN_FTB_STRUCT                 ),
    ("tRRD_LminFine",               SPD4_TRRD_MIN_FTB_STRUCT                 ),
    ("tRRD_SminFine",               SPD4_TRRD_MIN_FTB_STRUCT                 ),
    ("tRCminFine",                  SPD4_TRC_MIN_FTB_STRUCT                  ),
    ("tRPminFine",                  SPD4_TRP_MIN_FTB_STRUCT                  ),
    ("tRCDminFine",                 SPD4_TRCD_MIN_FTB_STRUCT                 ),
    ("tAAminFine",                  SPD4_TAA_MIN_FTB_STRUCT                  ),
    ("tCKmaxFine",                  SPD4_TCK_MAX_FTB_STRUCT                  ),
    ("tCKminFine",                  SPD4_TCK_MIN_FTB_STRUCT                  ),
    ("Crc",                         SPD4_CYCLIC_REDUNDANCY_CODE              )
    ]

class SPD4_MODULE_UNBUFFERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",     SPD4_UNBUF_MODULE_NOMINAL_HEIGHT   ),
    ("ModuleMaximumThickness",  SPD4_UNBUF_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",    SPD4_UNBUF_REFERENCE_RAW_CARD      ),
    ("AddressMappingEdgeConn",  SPD4_UNBUF_ADDRESS_MAPPING         ),
    ("Reserved",                UINT8 * (253 - 132 + 1)            ),
    ("Crc",                     SPD4_CYCLIC_REDUNDANCY_CODE        )
    ]

class SPD4_MODULE_REGISTERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",                                 SPD4_RDIMM_MODULE_NOMINAL_HEIGHT                                     ),
    ("ModuleMaximumThickness",                              SPD4_RDIMM_MODULE_NOMINAL_THICKNESS                                  ),
    ("ReferenceRawCardUsed",                                SPD4_RDIMM_REFERENCE_RAW_CARD                                        ),
    ("DimmModuleAttributes",                                SPD4_RDIMM_MODULE_ATTRIBUTES                                         ),
    ("DimmThermalHeatSpreaderSolution",                     SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION                            ),
    ("RegisterManufacturerIdCode",                          SPD4_MANUFACTURER_ID_CODE                                            ),
    ("RegisterRevisionNumber",                              SPD4_RDIMM_REGISTER_REVISION_NUMBER                                  ),
    ("AddressMappingFromRegisterToDRAM",                    SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM                     ),
    ("RegisterOutputDriveStrengthForControlCommandAddress", SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS),
    ("RegisterOutputDriveStrengthForClock",                 SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK                  ),
    ("Reserved",                                            UINT8 * (253 - 139 + 1)                                              ),
    ("Crc",                                                 SPD4_CYCLIC_REDUNDANCY_CODE                                          )
    ]

class SPD4_MODULE_LOADREDUCED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",                                 SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT                                     ),
    ("ModuleMaximumThickness",                              SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS                                  ),
    ("ReferenceRawCardUsed",                                SPD4_LRDIMM_REFERENCE_RAW_CARD                                        ),
    ("DimmModuleAttributes",                                SPD4_LRDIMM_MODULE_ATTRIBUTES                                         ),
    ("ThermalHeatSpreaderSolution",                         SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION                            ),
    ("RegisterManufacturerIdCode",                          SPD4_MANUFACTURER_ID_CODE                                             ),
    ("RegisterRevisionNumber",                              SPD4_LRDIMM_REGISTER_REVISION_NUMBER                                  ),
    ("AddressMappingFromRegisterToDram",                    SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM                     ),
    ("RegisterOutputDriveStrengthForControlCommandAddress", SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS),
    ("RegisterOutputDriveStrengthForClock",                 SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK                  ),
    ("DataBufferRevisionNumber",                            SPD4_LRDIMM_DATA_BUFFER_REVISION_NUMBER                               ),
    ("DramVrefDQForPackageRank0",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DramVrefDQForPackageRank1",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DramVrefDQForPackageRank2",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DramVrefDQForPackageRank3",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DataBufferVrefDQForDramInterface",                    SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE                     ),
    ("DataBufferMdqDriveStrengthRttForDataRateLe1866",      SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE          ),
    ("DataBufferMdqDriveStrengthRttForDataRateLe2400",      SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE          ),
    ("DataBufferMdqDriveStrengthRttForDataRateLe3200",      SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE          ),
    ("DramDriveStrength",                                   SPD4_LRDIMM_DRAM_DRIVE_STRENGTH                                       ),
    ("DramOdtRttWrRttNomForDataRateLe1866",                 SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                     ),
    ("DramOdtRttWrRttNomForDataRateLe2400",                 SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                     ),
    ("DramOdtRttWrRttNomForDataRateLe3200",                 SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                     ),
    ("DramOdtRttParkForDataRateLe1866",                     SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                           ),
    ("DramOdtRttParkForDataRateLe2400",                     SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                           ),
    ("DramOdtRttParkForDataRateLe3200",                     SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                           ),
    ("DataBufferVrefDQForDramInterfaceRange",               SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE               ),
    ("DataBufferDqDecisionFeedbackEqualization",            SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION             ),
    ("Reserved",                                            UINT8 * (253 - 157 + 1)                                               ),
    ("Crc",                                                 SPD4_CYCLIC_REDUNDANCY_CODE                                           )
    ]

class SPD4_MODULE_NVDIMM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved0",                                   UINT8 * (191 - 128 + 1)                                   ),
    ("ModuleProductIdentifier",                     SPD4_NVDIMM_MODULE_PRODUCT_IDENTIFIER                     ),
    ("SubsystemControllerManufacturerIdCode",       SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE     ),
    ("SubsystemControllerIdentifier",               SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_IDENTIFIER               ),
    ("SubsystemControllerRevisionCode",             SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_REVISION_CODE            ),
    ("ReferenceRawCardUsed",                        SPD4_NVDIMM_REFERENCE_RAW_CARD                            ),
    ("ModuleCharacteristics",                       SPD4_NVDIMM_MODULE_CHARACTERISTICS                        ),
    ("HybridModuleMediaTypes",                      SPD4_NVDIMM_HYBRID_MODULE_MEDIA_TYPES                     ),
    ("MaximumNonVolatileMemoryInitializationTime",  SPD4_NVDIMM_MAXIMUM_NONVOLATILE_MEMORY_INITIALIZATION_TIME),
    ("FunctionInterfaceDescriptors",                SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR * 8             ),
    ("Reserved",                                    UINT8 * (253 - 220 + 1)                                   ),
    ("Crc",                                         SPD4_CYCLIC_REDUNDANCY_CODE                               )
    ]

class SPD4_MODULE_SPECIFIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unbuffered",  SPD4_MODULE_UNBUFFERED),
    ("Registered",  SPD4_MODULE_REGISTERED),
    ("LoadReduced", SPD4_MODULE_LOADREDUCED),
    ("NonVolatile", SPD4_MODULE_NVDIMM)
    ]

class SPD4_MODULE_PART_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModulePartNumber",   UINT8 * (348 - 329 + 1))
    ]

class SPD4_MANUFACTURER_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ManufacturerSpecificData",   UINT8 * (381 - 353 + 1))
    ]

SPD4_MODULE_REVISION_CODE   = UINT8
SPD4_DRAM_STEPPING          = UINT8

class SPD4_MANUFACTURING_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleId",                    SPD4_UNIQUE_MODULE_ID     ),
    ("ModulePartNumber",            SPD4_MODULE_PART_NUMBER   ),
    ("ModuleRevisionCode",          SPD4_MODULE_REVISION_CODE ),
    ("DramIdCode",                  SPD4_MANUFACTURER_ID_CODE ),
    ("DramStepping",                SPD4_DRAM_STEPPING        ),
    ("ManufacturerSpecificData",    SPD4_MANUFACTURER_SPECIFIC),
    ("Reserved",                    UINT8 * 2                 )
    ]

class SPD4_END_USER_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",   UINT8 * (511 - 384 + 1))
    ]

class SPD_DDR4 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Base",            SPD4_BASE_SECTION),
    ("Module",          SPD4_MODULE_SPECIFIC),
    ("Reserved",        UINT8 * (319 - 256 + 1)),
    ("ManufactureInfo", SPD4_MANUFACTURING_DATA),
    ("EndUser",         SPD4_END_USER_SECTION)
    ]

