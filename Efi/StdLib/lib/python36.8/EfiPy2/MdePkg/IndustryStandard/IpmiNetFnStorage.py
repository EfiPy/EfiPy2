# IpmiNetFnStorage.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnStorage
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

IPMI_NETFN_STORAGE  = 0x0A

IPMI_STORAGE_GET_FRU_INVENTORY_AREAINFO  = 0x10

class IPMI_GET_FRU_INVENTORY_AREA_INFO_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceId",    UINT8)
    ]

class IPMI_GET_FRU_INVENTORY_AREA_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8 ),
    ("InventoryAreaSize",   UINT16),
    ("AccessType",          UINT8 )
    ]

IPMI_STORAGE_READ_FRU_DATA  = 0x11

class IPMI_FRU_COMMON_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FruDeviceId", UINT8 ),
    ("FruOffset",   UINT16)
    ]

class IPMI_FRU_READ_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    IPMI_FRU_COMMON_DATA),
    ("Count",   UINT8)
    ]

class IPMI_READ_FRU_DATA_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceId",        UINT8),
    ("InventoryOffset", UINT16),
    ("CountToRead",     UINT8)
    ]

class IPMI_READ_FRU_DATA_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("CountReturned",   UINT8),
    ("Data",            UINT8 * 0)
    ]

IPMI_STORAGE_WRITE_FRU_DATA  = 0x12

class IPMI_FRU_WRITE_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    IPMI_FRU_COMMON_DATA),
    ("FruData", UINT8 * 16)
    ]

class IPMI_WRITE_FRU_DATA_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceId",        UINT8),
    ("InventoryOffset", UINT16),
    ("Data",            UINT8 * 0)
    ]

class IPMI_WRITE_FRU_DATA_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("CountWritten",    UINT8)
    ]

IPMI_STORAGE_GET_SDR_REPOSITORY_INFO  = 0x20

class IPMI_SDR_OPERATION_SUPPORT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdrRepAllocInfoCmd",  UINT8,  1),
    ("SdrRepReserveCmd",    UINT8,  1),
    ("PartialAddSdrCmd",    UINT8,  1),
    ("DeleteSdrRepCmd",     UINT8,  1),
    ("Reserved",            UINT8,  1),
    ("SdrRepUpdateOp",      UINT8,  2),
    ("Overflow",            UINT8,  1)
    ]

class IPMI_SDR_OPERATION_SUPPORT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_OPERATION_SUPPORT_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_SDR_REPOSITORY_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",          UINT8                     ),
    ("Version",                 UINT8                     ),
    ("RecordCount",             UINT16                    ),
    ("FreeSpace",               UINT16                    ),
    ("RecentAdditionTimeStamp", UINT32                    ),
    ("RecentEraseTimeStamp",    UINT32                    ),
    ("OperationSupport",        IPMI_SDR_OPERATION_SUPPORT)
    ]

IPMI_STORAGE_GET_SDR_REPOSITORY_ALLOCATION_INFO  = 0x21

IPMI_STORAGE_RESERVE_SDR_REPOSITORY  = 0x22

class IPMI_RESERVE_SDR_REPOSITORY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ReservationId",   UINT8 * 2)
    ]

class IPMI_SDR_RECORD_SENSOR_INIT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EventScanningEnabled",    UINT8,  1),
    ("EventScanningDisabled",   UINT8,  1),
    ("InitSensorType",          UINT8,  1),
    ("InitHysteresis",          UINT8,  1),
    ("InitThresholds",          UINT8,  1),
    ("InitEvent",               UINT8,  1),
    ("InitScanning",            UINT8,  1),
    ("SettableSensor",          UINT8,  1)
    ]

class IPMI_SDR_RECORD_SENSOR_INIT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_SENSOR_INIT_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_SENSOR_CAP_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EventMessageControl",     UINT8,  2),
    ("ThresholdAccessSupport",  UINT8,  2),
    ("HysteresisSupport",       UINT8,  2),
    ("ReArmSupport",            UINT8,  1),
    ("IgnoreSensor",            UINT8,  1)
    ]

class IPMI_SDR_RECORD_SENSOR_CAP (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_SENSOR_CAP_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_LINEARIZATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Linearization",   UINT8,  7),
    ("Reserved",        UINT8,  1)
    ]

class IPMI_SDR_RECORD_LINEARIZATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_LINEARIZATION_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_M_TOLERANCE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Toleremce",   UINT8,  6),
    ("MHi",         UINT8,  2)
    ]

class IPMI_SDR_RECORD_M_TOLERANCE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_M_TOLERANCE_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_B_ACCURACY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AccuracyLow", UINT8,  6),
    ("BHi",         UINT8,  2)
    ]

class IPMI_SDR_RECORD_B_ACCURACY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_B_ACCURACY_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_ACCURACY_SENSOR_DIR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8,  2),
    ("AccuracyExp", UINT8,  2),
    ("AccuracyHi",  UINT8,  4)
    ]

class IPMI_SDR_RECORD_ACCURACY_SENSOR_DIR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_ACCURACY_SENSOR_DIR_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_R_EXP_B_EXP_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BExp",    UINT8,  4),
    ("RExp",    UINT8,  4)
    ]

class IPMI_SDR_RECORD_R_EXP_B_EXP (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_R_EXP_B_EXP_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_ANALOG_FLAGS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NominalReadingSpscified", UINT8,  1),
    ("NominalMaxSpscified",     UINT8,  1),
    ("NominalMinSpscified",     UINT8,  1),
    ("Reserved",                UINT8,  5),
    ]

class IPMI_SDR_RECORD_ANALOG_FLAGS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_ANALOG_FLAGS_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_STRUCT_1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",                    UINT16                             ), # 1
    ("Version",                     UINT8                              ), # 3
    ("RecordType",                  UINT8                              ), # 4
    ("RecordLength",                UINT8                              ), # 5
    ("OwnerId",                     UINT8                              ), # 6
    ("OwnerLun",                    UINT8                              ), # 7
    ("SensorNumber",                UINT8                              ), # 8
    ("EntityId",                    UINT8                              ), # 9
    ("EntityInstance",              UINT8                              ), # 10
    ("SensorInitialization",        IPMI_SDR_RECORD_SENSOR_INIT        ), # 11
    ("SensorCapabilities",          IPMI_SDR_RECORD_SENSOR_CAP         ), # 12
    ("SensorType",                  UINT8                              ), # 13
    ("EventType",                   UINT8                              ), # 14
    ("Reserved1",                   UINT8 * 7                          ), # 15
    ("UnitType",                    UINT8                              ), # 22
    ("Reserved2",                   UINT8                              ), # 23
    ("Linearization",               IPMI_SDR_RECORD_LINEARIZATION      ), # 24
    ("MLo",                         UINT8                              ), # 25
    ("MHiTolerance",                IPMI_SDR_RECORD_M_TOLERANCE        ), # 26
    ("BLo",                         UINT8                              ), # 27
    ("BHiAccuracyLo",               IPMI_SDR_RECORD_B_ACCURACY         ), # 28
    ("AccuracySensorDirection",     IPMI_SDR_RECORD_ACCURACY_SENSOR_DIR), # 29
    ("RExpBExp",                    IPMI_SDR_RECORD_R_EXP_B_EXP        ), # 30
    ("AnalogFlags",                 IPMI_SDR_RECORD_ANALOG_FLAGS       ), # 31
    ("NominalReading",              UINT8                              ), # 32
    ("Reserved3",                   UINT8 * 4                          ), # 33
    ("UpperNonRecoverThreshold",    UINT8                              ), # 37
    ("UpperCriticalThreshold",      UINT8                              ), # 38
    ("UpperNonCriticalThreshold",   UINT8                              ), # 39
    ("LowerNonRecoverThreshold",    UINT8                              ), # 40
    ("LowerCriticalThreshold",      UINT8                              ), # 41
    ("LowerNonCriticalThreshold",   UINT8                              ), # 42
    ("Reserved4",                   UINT8 * 5                          ), # 43
    ("IdStringLength",              UINT8                              ), # 48
    ("AsciiIdString",               UINT8 * 16                         ) # 49 - 64
    ]

class IPMI_SDR_RECORD_STRUCT_2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",                UINT16                     ), # 1
    ("Version",                 UINT8                      ), # 3
    ("RecordType",              UINT8                      ), # 4
    ("RecordLength",            UINT8                      ), # 5
    ("OwnerId",                 UINT8                      ), # 6
    ("OwnerLun",                UINT8                      ), # 7
    ("SensorNumber",            UINT8                      ), # 8
    ("EntityId",                UINT8                      ), # 9
    ("EntityInstance",          UINT8                      ), # 10
    ("SensorInitialization",    IPMI_SDR_RECORD_SENSOR_INIT), # 11
    ("SensorCapabilities",      IPMI_SDR_RECORD_SENSOR_CAP ), # 12
    ("SensorType",              UINT8                      ), # 13
    ("EventType",               UINT8                      ), # 14
    ("Reserved1",               UINT8 * 7                  ), # 15
    ("UnitType",                UINT8                      ), # 22
    ("Reserved2",               UINT8 * 9                  ), # 23
    ("IdStringLength",          UINT8                      ), # 32
    ("AsciiIdString",           UINT8 * 16                 ) # 33 - 48
    ]

class IPMI_FRU_DATA_INFO_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",               UINT8,  1),
    ("ControllerSlaveAddress",  UINT8,  7),
    ("FruDeviceId",             UINT8),
    ("BusId",                   UINT8,  3),
    ("Lun",                     UINT8,  2),
    ("Reserved2",               UINT8,  2),
    ("LogicalFruDevice",        UINT8,  1),
    ("Reserved3",               UINT8,  4),
    ("ChannelNumber",           UINT8,  4)
    ]

class IPMI_FRU_DATA_INFO (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_FRU_DATA_INFO_Bits),
    ("Uint32",  UINT32)
    ]

class IPMI_SDR_RECORD_DEV_ID_STR_TYPE_LENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",      UINT8,  4),
    ("Reserved",    UINT8,  1),
    ("StringType",  UINT8,  3),
    ]

class IPMI_SDR_RECORD_DEV_ID_STR_TYPE_LENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SDR_RECORD_DEV_ID_STR_TYPE_LENGTH_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SDR_RECORD_STRUCT_11 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",            UINT16                                ), # 1
    ("Version",             UINT8                                 ), # 3
    ("RecordType",          UINT8                                 ), # 4
    ("RecordLength",        UINT8                                 ), # 5
    ("FruDeviceData",       IPMI_FRU_DATA_INFO                    ), # 6
    ("Reserved",            UINT8                                 ), # 10
    ("DeviceType",          UINT8                                 ), # 11
    ("DeviceTypeModifier",  UINT8                                 ), # 12
    ("FruEntityId",         UINT8                                 ), # 13
    ("FruEntityInstance",   UINT8                                 ), # 14
    ("OemReserved",         UINT8                                 ), # 15
    ("StringTypeLength",    IPMI_SDR_RECORD_DEV_ID_STR_TYPE_LENGTH), # 16
    ("String",              UINT8 * 16                            )  # 17
    ]

class IPMI_SDR_RECORD_STRUCT_C0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",         UINT16),       # 1
    ("Version",          UINT8 ),       # 3
    ("RecordType",       UINT8 ),       # 4
    ("RecordLength",     UINT8 ),       # 5
    ("ManufacturerId",   UINT8 * 3),    # 6
    ("StringChars",      UINT8 * 20)
    ]

class IPMI_SDR_RECORD_STRUCT_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",         UINT16),       # 1
    ("Version",          UINT8 ),       # 3
    ("RecordType",       UINT8 ),       # 4
    ("RecordLength",     UINT8 )        # 5
    ]

class IPMI_SENSOR_RECORD_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("SensorType1",   IPMI_SDR_RECORD_STRUCT_1     ),
    ("SensorType2",   IPMI_SDR_RECORD_STRUCT_2     ),
    ("SensorType11",  IPMI_SDR_RECORD_STRUCT_11    ),
    ("SensorTypeC0",  IPMI_SDR_RECORD_STRUCT_C0    ),
    ("SensorHeader",  IPMI_SDR_RECORD_STRUCT_HEADER)
    ]

class IPMI_GET_SDR_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReservationId",   UINT16),
    ("RecordId",        UINT16),
    ("RecordOffset",    UINT8 ),
    ("BytesToRead",     UINT8 )
    ]

class IPMI_GET_SDR_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8                    ),
    ("NextRecordId",    UINT16                   ),
    ("RecordData",      IPMI_SENSOR_RECORD_STRUCT)
    ]

IPMI_STORAGE_ADD_SDR  = 0x24

IPMI_STORAGE_PARTIAL_ADD_SDR  = 0x25

IPMI_STORAGE_DELETE_SDR  = 0x26

IPMI_STORAGE_CLEAR_SDR  = 0x27

IPMI_STORAGE_GET_SDR_REPOSITORY_TIME  = 0x28

IPMI_STORAGE_SET_SDR_REPOSITORY_TIME  = 0x29

IPMI_STORAGE_ENTER_SDR_UPDATE_MODE  = 0x2A

IPMI_STORAGE_EXIT_SDR_UPDATE_MODE  = 0x2B

IPMI_STORAGE_RUN_INIT_AGENT  = 0x2C

IPMI_STORAGE_GET_SEL_INFO  = 0x40

IPMI_GET_SEL_INFO_OPERATION_SUPPORT_GET_SEL_ALLOCATION_INFO_CMD  = BIT0
IPMI_GET_SEL_INFO_OPERATION_SUPPORT_RESERVE_SEL_CMD              = BIT1
IPMI_GET_SEL_INFO_OPERATION_SUPPORT_PARTIAL_ADD_SEL_ENTRY_CMD    = BIT2
IPMI_GET_SEL_INFO_OPERATION_SUPPORT_DELETE_SEL_CMD               = BIT3
IPMI_GET_SEL_INFO_OPERATION_SUPPORT_OVERFLOW_FLAG                = BIT7

class IPMI_GET_SEL_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",          UINT8 ),
    ("Version",                 UINT8 ),
    ("NoOfEntries",             UINT16),
    ("FreeSpace",               UINT16),
    ("RecentAddTimeStamp",      UINT32),
    ("RecentEraseTimeStamp",    UINT32),
    ("OperationSupport",        UINT8 )
    ]

IPMI_STORAGE_GET_SEL_ALLOCATION_INFO  = 0x41

IPMI_STORAGE_RESERVE_SEL  = 0x42

class IPMI_RESERVE_SEL_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ReservationId",   UINT8 * 2)
    ]

IPMI_STORAGE_GET_SEL_ENTRY  = 0x43

class IPMI_SEL_EVENT_RECORD_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",      UINT16),
    ("RecordType",    UINT8 ),
    ("TimeStamp",     UINT32),
    ("GeneratorId",   UINT16),
    ("EvMRevision",   UINT8 ),
    ("SensorType",    UINT8 ),
    ("SensorNumber",  UINT8 ),
    ("EventDirType",  UINT8 ),
    ("OEMEvData1",    UINT8 ),
    ("OEMEvData2",    UINT8 ),
    ("OEMEvData3",    UINT8 )
    ]

class IPMI_TIMESTAMPED_OEM_SEL_RECORD_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",        UINT16),
    ("RecordType",      UINT8 ),
    ("TimeStamp",       UINT32),
    ("ManufacturerId",  UINT8 * 3),
    ("OEMDefined",      UINT8 * 6)
    ]

class IPMI_NON_TIMESTAMPED_OEM_SEL_RECORD_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordId",        UINT16),
    ("RecordType",      UINT8 ),
    ("OEMDefined",      UINT8 * 13)
    ]

class IPMI_GET_SEL_ENTRY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReserveId",   UINT8 * 2),
    ("SelRecID",    UINT8 * 2),
    ("Offset",      UINT8),
    ("BytesToRead", UINT8)
    ]

class IPMI_GET_SEL_ENTRY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("NextSelRecordId", UINT16),
    ("RecordData",      IPMI_SEL_EVENT_RECORD_DATA)
    ]

IPMI_STORAGE_ADD_SEL_ENTRY  = 0x44

class IPMI_ADD_SEL_ENTRY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordData",      IPMI_SEL_EVENT_RECORD_DATA)
    ]

class IPMI_ADD_SEL_ENTRY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("RecordId",        UINT16)
    ]

IPMI_STORAGE_PARTIAL_ADD_SEL_ENTRY  = 0x45

class IPMI_PARTIAL_ADD_SEL_ENTRY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReservationId",       UINT16),
    ("RecordId",            UINT16),
    ("OffsetIntoRecord",    UINT8 ),
    ("InProgress",          UINT8 ),
    ("RecordData",          UINT8 * 0)
    ]

class IPMI_PARTIAL_ADD_SEL_ENTRY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8),
    ("RecordId",            UINT16)
    ]

IPMI_STORAGE_DELETE_SEL_ENTRY  = 0x46

class IPMI_DELETE_SEL_ENTRY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReserveId",       UINT8 * 2),
    ("RecordToDelete",  UINT8 * 2)
    ]

IPMI_DELETE_SEL_ENTRY_RESPONSE_TYPE_UNSUPPORTED   = 0x80
IPMI_DELETE_SEL_ENTRY_RESPONSE_ERASE_IN_PROGRESS  = 0x81

class IPMI_DELETE_SEL_ENTRY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("RecordId",        UINT16)
    ]

IPMI_STORAGE_CLEAR_SEL  = 0x47

IPMI_CLEAR_SEL_REQUEST_C_CHAR_ASCII      = 0x43
IPMI_CLEAR_SEL_REQUEST_L_CHAR_ASCII      = 0x4C
IPMI_CLEAR_SEL_REQUEST_R_CHAR_ASCII      = 0x52
IPMI_CLEAR_SEL_REQUEST_INITIALIZE_ERASE  = 0xAA
IPMI_CLEAR_SEL_REQUEST_GET_ERASE_STATUS  = 0x00

class IPMI_CLEAR_SEL_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserve", UINT8 * 2),
    ("AscC",    UINT8),
    ("AscL",    UINT8),
    ("AscR",    UINT8),
    ("Erase",   UINT8)
    ]

IPMI_CLEAR_SEL_RESPONSE_ERASURE_IN_PROGRESS  = 0x00
IPMI_CLEAR_SEL_RESPONSE_ERASURE_COMPLETED    = 0x01

class IPMI_CLEAR_SEL_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ErasureProgress", UINT8)
    ]

IPMI_STORAGE_GET_SEL_TIME  = 0x48

class IPMI_GET_SEL_TIME_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Timestamp",       UINT32)
    ]

IPMI_STORAGE_SET_SEL_TIME  = 0x49

class IPMI_SET_SEL_TIME_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Timestamp",       UINT32)
    ]

IPMI_STORAGE_GET_AUXILLARY_LOG_STATUS  = 0x5A

IPMI_STORAGE_SET_AUXILLARY_LOG_STATUS  = 0x5B

IPMI_STORAGE_GET_SEL_TIME_UTC_OFFSET  = 0x5C

class IPMI_GET_SEL_TIME_UTC_OFFSET_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("UtcOffset",       INT16)
    ]

IPMI_STORAGE_SET_SEL_TIME_UTC_OFFSET  = 0x5D

IPMI_COMPLETE_SEL_RECORD  = 0xFF

IPMI_SEL_SYSTEM_RECORD                   = 0x02
IPMI_SEL_OEM_TIME_STAMP_RECORD_START     = 0xC0
IPMI_SEL_OEM_TIME_STAMP_RECORD_END       = 0xDF
IPMI_SEL_OEM_NO_TIME_STAMP_RECORD_START  = 0xE0
IPMI_SEL_OEM_NO_TIME_STAMP_RECORD_END    = 0xFF

def IPMI_SEL_EVENT_DIR (EventDirType):
  return EventDirType >> 7

IPMI_SEL_EVENT_DIR_ASSERTION_EVENT    = 0x00
IPMI_SEL_EVENT_DIR_DEASSERTION_EVENT  = 0x01

def IPMI_SEL_EVENT_TYPE (EventDirType):
  return EventDirType & 0x7F

IPMI_SEL_EVENT_TYPE_UNSPECIFIED      = 0x00
IPMI_SEL_EVENT_TYPE_THRESHOLD        = 0x01
IPMI_SEL_EVENT_TYPE_GENERIC_START    = 0x02
IPMI_SEL_EVENT_TYPE_GENERIC_END      = 0x0C
IPMI_SEL_EVENT_TYPE_SENSOR_SPECIFIC  = 0x6F
IPMI_SEL_EVENT_TYPE_OEM_START        = 0x70
IPMI_SEL_EVENT_TYPE_OEM_END          = 0x7F

IPMI_SWID_BIOS_RANGE_START            = 0x00
IPMI_SWID_BIOS_RANGE_END              = 0x0F
IPMI_SWID_SMI_HANDLER_RANGE_START     = 0x10
IPMI_SWID_SMI_HANDLER_RANGE_END       = 0x1F
IPMI_SWID_SMS_RANGE_START             = 0x20
IPMI_SWID_SMS_RANGE_END               = 0x2F
IPMI_SWID_OEM_RANGE_START             = 0x30
IPMI_SWID_OEM_RANGE_END               = 0x3F
IPMI_SWID_REMOTE_CONSOLE_RANGE_START  = 0x40
IPMI_SWID_REMOTE_CONSOLE_RANGE_END    = 0x46
IPMI_SWID_TERMINAL_REMOTE_CONSOLE_ID  = 0x47

def SLAVE_ADDRESS_FROM_GENERATOR_ID(GeneratorId):
  return ((GeneratorId & 0xFF) >> 1)

def LUN_FROM_GENERATOR_ID(GeneratorId):
  return ((GeneratorId >> 8) & 0x03)

def CHANNEL_NUMBER_FROM_GENERATOR_ID(GeneratorId):
  return ((GeneratorId >> 12) & 0x0F)

IPMI_EVM_REVISION     = 0x04
IPMI_BIOS_ID          = 0x18
IPMI_FORMAT_REV       = 0x00
IPMI_FORMAT_REV1      = 0x01
IPMI_SOFTWARE_ID      = 0x01
IPMI_PLATFORM_VAL_ID  = 0x01

def IPMI_GENERATOR_ID(i, f):
  return ((i << 1) | (f << 1) | IPMI_SOFTWARE_ID)

IPMI_SENSOR_TYPE_EVENT_CODE_DISCRETE  = 0x6F

IPMI_OEM_SPECIFIC_DATA     = 0x02
IPMI_SENSOR_SPECIFIC_DATA  = 0x03
