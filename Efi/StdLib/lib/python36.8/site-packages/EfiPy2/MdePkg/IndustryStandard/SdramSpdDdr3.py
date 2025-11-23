# SdramSpdDdr3.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpdDdr3
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class SPD3_DEVICE_DESCRIPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BytesUsed",   UINT8, 4),
    ("BytesTotal",  UINT8, 3),
    ("CrcCoverage", UINT8, 1)
    ]

class SPD3_DEVICE_DESCRIPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_DEVICE_DESCRIPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_REVISION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Minor",   UINT8, 4),
    ("Major",   UINT8, 4)
    ]

class SPD3_REVISION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_REVISION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_DRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8, 8)
    ]

class SPD3_DRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_DRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleType",  UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class SPD3_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_SDRAM_DENSITY_BANKS_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Density",     UINT8, 4),
    ("BankAddress", UINT8, 3),
    ("Reserved",    UINT8, 1)
    ]

class SPD3_SDRAM_DENSITY_BANKS_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_DENSITY_BANKS_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_SDRAM_ADDRESSING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ColumnAddress",   UINT8, 3),
    ("RowAddress",      UINT8, 3),
    ("Reserved",        UINT8, 2)
    ]

class SPD3_SDRAM_ADDRESSING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_ADDRESSING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OperationAt1_50",     UINT8, 1),
    ("OperationAt1_35",     UINT8, 1),
    ("OperationAt1_25",     UINT8, 1),
    ("Reserved",            UINT8, 5)
    ]

class SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MODULE_ORGANIZATION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdramDeviceWidth",    UINT8, 3),
    ("RankCount",           UINT8, 3),
    ("Reserved",            UINT8, 2)
    ]

class SPD3_MODULE_ORGANIZATION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_ORGANIZATION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PrimaryBusWidth",     UINT8, 3),
    ("BusWidthExtension",   UINT8, 2),
    ("Reserved",            UINT8, 3)
    ]

class SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_FINE_TIMEBASE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Divisor",     UINT8, 4),
    ("Dividend",    UINT8, 4)
    ]

class SPD3_FINE_TIMEBASE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_FINE_TIMEBASE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Dividend",    UINT8, 8)
    ]

class SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Divisor",     UINT8, 8)
    ]

class SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MEDIUM_TIMEBASE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Dividend",    SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT),
    ("Divisor",     SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT)
    ]

class SPD3_TCK_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmin",  UINT8, 8)
    ]

class SPD3_TCK_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TCK_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_CAS_LATENCIES_SUPPORTED_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl4",         UINT16, 1),
    ("Cl5",         UINT16, 1),
    ("Cl6",         UINT16, 1),
    ("Cl7",         UINT16, 1),
    ("Cl8",         UINT16, 1),
    ("Cl9",         UINT16, 1),
    ("Cl10",        UINT16, 1),
    ("Cl11",        UINT16, 1),
    ("Cl12",        UINT16, 1),
    ("Cl13",        UINT16, 1),
    ("Cl14",        UINT16, 1),
    ("Cl15",        UINT16, 1),
    ("Cl16",        UINT16, 1),
    ("Cl17",        UINT16, 1),
    ("Cl18",        UINT16, 1),
    ("Reserved",    UINT16, 1)
    ]

class SPD3_CAS_LATENCIES_SUPPORTED_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            SPD3_CAS_LATENCIES_SUPPORTED_STRUCT_Bits),
    ("Data",            UINT16),
    ("Data8",           UINT8 * 2)
    ]

class SPD3_TAA_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAmin",  UINT8, 8)
    ]

class SPD3_TAA_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TAA_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TWR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWRmin",  UINT8, 8)
    ]

class SPD3_TWR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TWR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDmin", UINT8, 8)
    ]

class SPD3_TRCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRRD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRRDmin", UINT8, 8)
    ]

class SPD3_TRRD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRRD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRP_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPmin",  UINT8, 8)
    ]

class SPD3_TRP_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRP_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRAS_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASminUpper",    UINT8, 4),
    ("tRCminUpper",     UINT8, 4)
    ]

class SPD3_TRAS_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRAS_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRAS_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASmin", UINT8, 8)
    ]

class SPD3_TRAS_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRAS_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCmin",  UINT8, 8)
    ]

class SPD3_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRFC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCmin", UINT16, 16)
    ]

class SPD3_TRFC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRFC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD3_TWTR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWTRmin", UINT8, 8)
    ]

class SPD3_TWTR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TWTR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TRTP_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRTPmin", UINT8, 8)
    ]

class SPD3_TRTP_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRTP_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TFAW_MIN_MTB_UPPER_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWminUpper",    UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class SPD3_TFAW_MIN_MTB_UPPER_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TFAW_MIN_MTB_UPPER_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TFAW_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWmin", UINT8, 8)
    ]

class SPD3_TFAW_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TFAW_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rzq6",        UINT8, 1),
    ("Rzq7",        UINT8, 1),
    ("Reserved",    UINT8, 5),
    ("DllOff",      UINT8, 1)
    ]

class SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_SDRAM_THERMAL_REFRESH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedTemperatureRange",        UINT8, 1),
    ("ExtendedTemperatureRefreshRate",  UINT8, 1),
    ("AutoSelfRefresh",                 UINT8, 1),
    ("OnDieThermalSensor",              UINT8, 1),
    ("Reserved",                        UINT8, 3),
    ("PartialArraySelfRefresh",         UINT8, 1)
    ]

class SPD3_SDRAM_THERMAL_REFRESH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_THERMAL_REFRESH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MODULE_THERMAL_SENSOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ThermalSensorAccuracy",   UINT8, 7),
    ("ThermalSensorPresence",   UINT8, 1)
    ]

class SPD3_MODULE_THERMAL_SENSOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_THERMAL_SENSOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_SDRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",   UINT8, 2),
    ("Reserved",        UINT8, 2),
    ("DieCount",        UINT8, 3),
    ("SdramDeviceType", UINT8, 1)
    ]

class SPD3_SDRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_TCK_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKminFine",  INT8, 8)
    ]

class SPD3_TCK_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TCK_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD3_TAA_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAminFine",  INT8, 8)
    ]

class SPD3_TAA_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TAA_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD3_TRCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDminFine", INT8, 8)
    ]

class SPD3_TRCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD3_TRP_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPminFine",  INT8, 8)
    ]

class SPD3_TRP_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRP_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD3_TRC_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCminFine",  INT8, 8)
    ]

class SPD3_TRC_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRC_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

class SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaximumActivateCount",    UINT8, 4),
    ("MaximumActivateWindow",   UINT8, 2),
    ("VendorSpecific",          UINT8, 2)
    ]

class SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_UNBUF_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",              UINT8, 5),
    ("RawCardExtension",    UINT8, 3)
    ]

class SPD3_UNBUF_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_UNBUF_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD3_UNBUF_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD3_UNBUF_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD3_UNBUF_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD3_UNBUF_ADDRESS_MAPPING_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MappingRank1",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD3_UNBUF_ADDRESS_MAPPING (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_ADDRESS_MAPPING_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD3_RDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD3_RDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD3_RDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD3_RDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeatSpreaderThermalCharacteristics",  UINT8, 7),
    ("HeatSpreaderSolution",                UINT8, 1)
    ]

class SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD3_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

class SPD3_RDIMM_REGISTER_REVISION_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterRevisionNumber",  UINT8, 8)
    ]

class SPD3_RDIMM_REGISTER_REVISION_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_REVISION_NUMBER_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_REGISTER_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bit0",        UINT8, 1),
    ("Bit1",        UINT8, 1),
    ("Bit2",        UINT8, 1),
    ("Reserved",    UINT8, 5)
    ]

class SPD3_RDIMM_REGISTER_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_TYPE_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 4),
    ("CommandAddressAOutputs",  UINT8, 2),
    ("CommandAddressBOutputs",  UINT8, 2)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ControlSignalsAOutputs",  UINT8, 2),
    ("ControlSignalsBOutputs",  UINT8, 2),
    ("Y1Y3ClockOutputs",        UINT8, 2),
    ("Y0Y2ClockOutputs",        UINT8, 2)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK_Bits),
    ("Data",    UINT8)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_RESERVED_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved0",   UINT8, 4),
    ("Reserved1",   UINT8, 4)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_RESERVED (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_CONTROL_RESERVED_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD3_LRDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD3_LRDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressCommandPrelaunch", UINT8, 1),
    ("Rank1Rank5Swap",          UINT8, 1),
    ("Reserved0",               UINT8, 1),
    ("Reserved1",               UINT8, 1),
    ("AddressCommandOutputs",   UINT8, 2),
    ("QxCS_nOutputs",           UINT8, 2)
    ]

class SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_TIMING_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("QxOdtOutputs",        UINT8, 2),
    ("QxCkeOutputs",        UINT8, 2),
    ("Y1Y3ClockOutputs",    UINT8, 2),
    ("Y0Y2ClockOutputs",    UINT8, 2)
    ]

class SPD3_LRDIMM_TIMING_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_TIMING_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_EXTENDED_DELAY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("YExtendedDelay",  UINT8, 2),
    ("QxCS_n",          UINT8, 2),
    ("QxOdt",           UINT8, 2),
    ("QxCke",           UINT8, 2)
    ]

class SPD3_LRDIMM_EXTENDED_DELAY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_EXTENDED_DELAY_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DelayY",      UINT8, 3),
    ("Reserved",    UINT8, 1),
    ("QxCS_n",      UINT8, 4)
    ]

class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("QxCS_n",  UINT8, 4),
    ("QxOdt",   UINT8, 4)
    ]

class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RC8MdqOdtStrength",   UINT8, 3),
    ("RC8Reserved",         UINT8, 1),
    ("RC9MdqOdtStrength",   UINT8, 3),
    ("RC9Reserved",         UINT8, 1)
    ]

class SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RC10DA3ValueR0",   UINT8, 1),
    ("RC10DA4ValueR0",   UINT8, 1),
    ("RC10DA3ValueR1",   UINT8, 1),
    ("RC10DA4ValueR1",   UINT8, 1),
    ("RC11DA3ValueR0",   UINT8, 1),
    ("RC11DA4ValueR0",   UINT8, 1),
    ("RC11DA3ValueR1",   UINT8, 1),
    ("RC11DA4ValueR1",   UINT8, 1)
    ]

class SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_MR_1_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Driver_Impedance",    UINT8, 2),
    ("Rtt_Nom",             UINT8, 3),
    ("Reserved",            UINT8, 1),
    ("Rtt_WR",              UINT8, 2)
    ]

class SPD3_LRDIMM_MR_1_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MR_1_2_Bits),
    ("Data",    UINT8)
    ]

class SPD3_LRDIMM_MODULE_DELAY_TIME_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MinimumDelayTime",    UINT8, 7),
    ("Reserved",            UINT8, 1)
    ]

class SPD3_LRDIMM_MODULE_DELAY_TIME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_DELAY_TIME_Bits),
    ("Data",    UINT8)
    ]

class SPD3_MANUFACTURING_DATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Year",    UINT8),
    ("Week",    UINT8)
    ]

class SPD3_MANUFACTURER_SERIAL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data",            UINT32),
    ("SerialNumber16",  UINT16 * 2),
    ("SerialNumber8",   UINT8  * 4)
    ]

class SPD3_MANUFACTURING_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Location",    UINT8)
    ]
class SPD3_UNIQUE_MODULE_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdCode",          SPD3_MANUFACTURER_ID_CODE      ),
    ("Location",        SPD3_MANUFACTURING_LOCATION    ),
    ("Date",            SPD3_MANUFACTURING_DATE        ),
    ("SerialNumber",    SPD3_MANUFACTURER_SERIAL_NUMBER)
    ]

class SPD3_CYCLIC_REDUNDANCY_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Crc",    UINT16 * 1),
    ("Data8",  UINT8  * 2)
    ]

class SPD3_BASE_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Description",              SPD3_DEVICE_DESCRIPTION_STRUCT     ),
    ("Revision",                 SPD3_REVISION_STRUCT               ),
    ("DramDeviceType",           SPD3_DRAM_DEVICE_TYPE_STRUCT       ),
    ("ModuleType",               SPD3_MODULE_TYPE_STRUCT            ),
    ("SdramDensityAndBanks",     SPD3_SDRAM_DENSITY_BANKS_STRUCT    ),
    ("SdramAddressing",          SPD3_SDRAM_ADDRESSING_STRUCT       ),
    ("ModuleNominalVoltage",     SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT ),
    ("ModuleOrganization",       SPD3_MODULE_ORGANIZATION_STRUCT    ),
    ("ModuleMemoryBusWidth",     SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT),
    ("FineTimebase",             SPD3_FINE_TIMEBASE_STRUCT          ),
    ("MediumTimebase",           SPD3_MEDIUM_TIMEBASE               ),
    ("tCKmin",                   SPD3_TCK_MIN_MTB_STRUCT            ),
    ("Reserved0",                UINT8                              ),
    ("CasLatencies",             SPD3_CAS_LATENCIES_SUPPORTED_STRUCT),
    ("tAAmin",                   SPD3_TAA_MIN_MTB_STRUCT            ),
    ("tWRmin",                   SPD3_TWR_MIN_MTB_STRUCT            ),
    ("tRCDmin",                  SPD3_TRCD_MIN_MTB_STRUCT           ),
    ("tRRDmin",                  SPD3_TRRD_MIN_MTB_STRUCT           ),
    ("tRPmin",                   SPD3_TRP_MIN_MTB_STRUCT            ),
    ("tRASMintRCMinUpper",       SPD3_TRAS_TRC_MIN_MTB_STRUCT       ),
    ("tRASmin",                  SPD3_TRAS_MIN_MTB_STRUCT           ),
    ("tRCmin",                   SPD3_TRC_MIN_MTB_STRUCT            ),
    ("tRFCmin",                  SPD3_TRFC_MIN_MTB_STRUCT           ),
    ("tWTRmin",                  SPD3_TWTR_MIN_MTB_STRUCT           ),
    ("tRTPmin",                  SPD3_TRTP_MIN_MTB_STRUCT           ),
    ("tFAWMinUpper",             SPD3_TFAW_MIN_MTB_UPPER_STRUCT     ),
    ("tFAWmin",                  SPD3_TFAW_MIN_MTB_STRUCT           ),
    ("SdramOptionalFeatures",    SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT),
    ("ThermalAndRefreshOptions", SPD3_SDRAM_THERMAL_REFRESH_STRUCT  ),
    ("ModuleThermalSensor",      SPD3_MODULE_THERMAL_SENSOR_STRUCT  ),
    ("SdramDeviceType",          SPD3_SDRAM_DEVICE_TYPE_STRUCT      ),
    ("tCKminFine",               SPD3_TCK_MIN_FTB_STRUCT            ),
    ("tAAminFine",               SPD3_TAA_MIN_FTB_STRUCT            ),
    ("tRCDminFine",              SPD3_TRCD_MIN_FTB_STRUCT           ),
    ("tRPminFine",               SPD3_TRP_MIN_FTB_STRUCT            ),
    ("tRCminFine",               SPD3_TRC_MIN_FTB_STRUCT            ),
    ("Reserved1",                UINT8 * (40 - 39 + 1)              ),
    ("MacValue",                 SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT   ),
    ("Reserved2",                UINT8 * (59 - 42 + 1)              )
    ]

class SPD3_MODULE_UNBUFFERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",     SPD3_UNBUF_MODULE_NOMINAL_HEIGHT),
    ("ModuleMaximumThickness",  SPD3_UNBUF_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",    SPD3_UNBUF_REFERENCE_RAW_CARD),
    ("AddressMappingEdgeConn",  SPD3_UNBUF_ADDRESS_MAPPING),
    ("Reserved",                UINT8 * (116 - 64 + 1))
    ]

class SPD3_MODULE_REGISTERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",             SPD3_RDIMM_MODULE_NOMINAL_HEIGHT),
    ("ModuleMaximumThickness",          SPD3_RDIMM_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",            SPD3_RDIMM_REFERENCE_RAW_CARD),
    ("DimmModuleAttributes",            SPD3_RDIMM_MODULE_ATTRIBUTES),
    ("ThermalHeatSpreaderSolution",     SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION),
    ("RegisterManufacturerIdCode",      SPD3_MANUFACTURER_ID_CODE),
    ("RegisterRevisionNumber",          SPD3_RDIMM_REGISTER_REVISION_NUMBER),
    ("RegisterType",                    SPD3_RDIMM_REGISTER_TYPE),
    ("Rc1Rc0",                          SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc3Rc2",                          SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS),
    ("Rc5Rc4",                          SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK),
    ("Rc7Rc6",                          SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc9Rc8",                          SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc11Rc10",                        SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc13Rc12",                        SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc15Rc14",                        SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Reserved",                        UINT8 * (116 - 77 + 1))
    ]

class SPD3_MODULE_CLOCKED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",             SPD3_UNBUF_MODULE_NOMINAL_HEIGHT),
    ("ModuleMaximumThickness",          SPD3_UNBUF_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",            SPD3_UNBUF_REFERENCE_RAW_CARD),
    ("Reserved",                        UINT8 * (116 - 63 + 1))
    ]

class SPD3_MODULE_LOADREDUCED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",                     SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT         ),
    ("ModuleMaximumThickness",                  SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS      ),
    ("ReferenceRawCardUsed",                    SPD3_LRDIMM_REFERENCE_RAW_CARD            ),
    ("DimmModuleAttributes",                    SPD3_LRDIMM_MODULE_ATTRIBUTES             ),
    ("MemoryBufferRevisionNumber",              UINT8                                     ),
    ("ManufacturerIdCode",                      SPD3_MANUFACTURER_ID_CODE                 ),
    ("TimingControlDriveStrengthCaCs",          SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH ),
    ("DriveStrength",                           SPD3_LRDIMM_TIMING_DRIVE_STRENGTH         ),
    ("ExtendedDelay",                           SPD3_LRDIMM_EXTENDED_DELAY                ),
    ("AdditiveDelayForCsCa",                    SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA),
    ("AdditiveDelayForOdtCke",                  SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE),
    ("MdqTerminationDriveStrengthFor800_1066",  SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH),
    ("Rank_0_1QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_2_3QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_4_5QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_6_7QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("MR_1_2RegistersFor800_1066",              SPD3_LRDIMM_MR_1_2                        ),
    ("MdqTerminationDriveStrengthFor1333_1600", SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH),
    ("Rank_0_1QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_2_3QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_4_5QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_6_7QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("MR_1_2RegistersFor1333_1600",             SPD3_LRDIMM_MR_1_2                        ),
    ("MdqTerminationDriveStrengthFor1866_2133", SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH),
    ("Rank_0_1QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_2_3QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_4_5QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_6_7QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("MR_1_2RegistersFor1866_2133",             SPD3_LRDIMM_MR_1_2                        ),
    ("MinimumModuleDelayTimeFor1_5V",           SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MaximumModuleDelayTimeFor1_5V",           SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MinimumModuleDelayTimeFor1_35V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MaximumModuleDelayTimeFor1_35V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MinimumModuleDelayTimeFor1_25V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MaximumModuleDelayTimeFor1_25V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("Reserved",                                UINT8 * (101 - 96 + 1)                    ),
    ("PersonalityByte",                         UINT8 * (116 - 102 + 1)                   )
    ]

class SPD3_MODULE_SPECIFIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unbuffered",  SPD3_MODULE_UNBUFFERED ),
    ("Registered",  SPD3_MODULE_REGISTERED ),
    ("Clocked",     SPD3_MODULE_CLOCKED    ),
    ("LoadReduced", SPD3_MODULE_LOADREDUCED)
    ]

class SPD3_MODULE_PART_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModulePartNumber",            UINT8 * (145 - 128 + 1))
    ]

class SPD3_MODULE_REVISION_CODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleRevisionCode",          UINT8 * (147 - 146 + 1))
    ]

class SPD3_MANUFACTURER_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ManufacturerSpecificData",    UINT8 * (175 - 150 + 1))
    ]

class SPD_DDR3 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("General",                     SPD3_BASE_SECTION          ),
    ("Module",                      SPD3_MODULE_SPECIFIC       ),
    ("ModuleId",                    SPD3_UNIQUE_MODULE_ID      ),
    ("Crc",                         SPD3_CYCLIC_REDUNDANCY_CODE),
    ("ModulePartNumber",            SPD3_MODULE_PART_NUMBER    ),
    ("ModuleRevisionCode",          SPD3_MODULE_REVISION_CODE  ),
    ("DramIdCode",                  SPD3_MANUFACTURER_ID_CODE  ),
    ("ManufacturerSpecificData",    SPD3_MANUFACTURER_SPECIFIC ),
    ("Reserved",                    UINT8 * (255 - 176 + 1))
    ]

