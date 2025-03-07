# Ufs.py
#
# EfiPy2.MdePkg.IndustryStandard.Ufs
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION

UFS_LUN_0             = 0x00
UFS_LUN_1             = 0x01
UFS_LUN_2             = 0x02
UFS_LUN_3             = 0x03
UFS_LUN_4             = 0x04
UFS_LUN_5             = 0x05
UFS_LUN_6             = 0x06
UFS_LUN_7             = 0x07
UFS_WLUN_REPORT_LUNS  = 0x81
UFS_WLUN_UFS_DEV      = 0xD0
UFS_WLUN_BOOT         = 0xB0
UFS_WLUN_RPMB         = 0xC4

class UTP_COMMAND_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",       UINT8, 6),
  ("Dd",              UINT8, 1),
  ("Hd",              UINT8, 1),
  ("Flags",           UINT8),
  ("Lun",             UINT8),
  ("TaskTag",         UINT8),
  ("CmdSet",          UINT8, 4),
  ("Iid",             UINT8, 4),
  ("Rsvd1",           UINT8),
  ("Rsvd2",           UINT8),
  ("Rsvd3",           UINT8, 4),
  ("Ext_Iid",         UINT8, 4),
  ("EhsLen",          UINT8),
  ("Rsvd4",           UINT8),
  ("DataSegLen",      UINT16),
  ("ExpDataTranLen",  UINT32),
  ("Cdb",             UINT8 * 16)
  ]

class UTP_RESPONSE_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",         UINT8, 6),
  ("Dd",                UINT8, 1),
  ("Hd",                UINT8, 1),
  ("Flags",             UINT8),
  ("Lun",               UINT8),
  ("TaskTag",           UINT8),
  ("CmdSet",            UINT8, 4),
  ("Iid",               UINT8, 4),
  ("Rsvd1",             UINT8, 4),
  ("Ext_Iid",           UINT8, 4),
  ("Response",          UINT8),
  ("Status",            UINT8),
  ("EhsLen",            UINT8),
  ("DevInfo",           UINT8),
  ("DataSegLen",        UINT16),
  ("ResTranCount",      UINT32),
  ("Rsvd2[16]",         UINT8 * 16),
  ("SenseDataLen",      UINT16),
  ("SenseData[18]",     UINT8 * 18)
  ]

class UTP_DATA_OUT_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",           UINT8, 6),
  ("Dd",                  UINT8, 1),
  ("Hd",                  UINT8, 1),
  ("Flags",               UINT8),
  ("Lun",                 UINT8),
  ("TaskTag",             UINT8),
  ("Rsvd1",               UINT8, 4),
  ("Iid",                 UINT8, 4),
  ("Rsvd2",               UINT8 * 2),
  ("Rsvd3",               UINT8, 4),
  ("Ext_Iid",             UINT8, 4),
  ("EhsLen",              UINT8),
  ("Rsvd4",               UINT8),
  ("DataSegLen",          UINT16),
  ("DataBufOffset",       UINT32),
  ("DataTranCount",       UINT32),
  ("Rsvd5",               UINT8 * 12)
  # ("Data",                UINT8 * N)
  ]

class UTP_DATA_IN_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",             UINT8, 6),
  ("Dd",                    UINT8, 1),
  ("Hd",                    UINT8, 1),
  ("Flags",                 UINT8),
  ("Lun",                   UINT8),
  ("TaskTag",               UINT8),
  ("Rsvd1",                 UINT8, 4),
  ("Iid",                   UINT8, 4),
  ("Rsvd2",                 UINT8, 4),
  ("Ext_Iid",               UINT8, 4),
  ("Rsvd3",                 UINT8 * 2),
  ("EhsLen",                UINT8),
  ("Rsvd4",                 UINT8),
  ("DataSegLen",            UINT16),
  ("DataBufOffset",         UINT32),
  ("DataTranCount",         UINT32),
  ("HintControl",           UINT8, 4),
  ("Rsvd5",                 UINT8, 4),
  ("HintIid",               UINT8, 4),
  ("HintExt_Iid",           UINT8, 4),
  ("HintLun",               UINT8),
  ("HintTaskTag",           UINT8),
  ("HintDataBufOffset",     UINT32),
  ("HintDataCount",         UINT32)
  # ("Data",                  UINT8 * N)
  ]

class UTP_RDY_TO_TRAN_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",             UINT8, 6),
  ("Dd",                    UINT8, 1),
  ("Hd",                    UINT8, 1),
  ("Flags",                 UINT8),
  ("Lun",                   UINT8),
  ("TaskTag",               UINT8),
  ("Rsvd1",                 UINT8, 4),
  ("Iid",                   UINT8, 4),
  ("Rsvd2",                 UINT8, 4),
  ("Ext_Iid",               UINT8, 4),
  ("Rsvd3",                 UINT8 * 2),
  ("EhsLen",                UINT8),
  ("Rsvd4",                 UINT8),
  ("DataSegLen",            UINT16),
  ("DataBufOffset",         UINT32),
  ("DataTranCount",         UINT32),
  ("HintControl",           UINT8, 4),
  ("Rsvd5",                 UINT8, 4),
  ("HintIid",               UINT8, 4),
  ("HintExt_Iid",           UINT8, 4),
  ("HintLun",               UINT8), 
  ("HintTaskTag",           UINT8), 
  ("HintDataBufOffset",     UINT32),
  ("HintDataCount",         UINT32)
  # ("Data",                UINT8 * N) 
  ]

class UTP_TM_REQ_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",       UINT8, 6),
  ("Dd",              UINT8, 1),
  ("Hd",              UINT8, 1),
  ("Flags",           UINT8),
  ("Lun",             UINT8),
  ("TaskTag",         UINT8),
  ("Rsvd1",           UINT8, 4),
  ("Iid",             UINT8, 4),
  ("TskManFunc",      UINT8),
  ("Rsvd2",           UINT8),
  ("Rsvd3",           UINT8, 4),
  ("Ext_Iid",         UINT8, 4),
  ("EhsLen",          UINT8),
  ("Rsvd4",           UINT8),
  ("DataSegLen",      UINT16),
  ("InputParam1",     UINT32),
  ("InputParam2",     UINT32),
  ("InputParam3",     UINT32),
  ("Rsvd5",           UINT8 * 8)
  ]

class UTP_TM_RESP_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",         UINT8, 6),
  ("Dd",                UINT8, 1),
  ("Hd",                UINT8, 1),
  ("Flags",             UINT8),
  ("Lun",               UINT8),
  ("TaskTag",           UINT8),
  ("Rsvd1",             UINT8, 4),
  ("Iid",               UINT8, 4),
  ("Rsvd2",             UINT8, 4),
  ("Ext_Iid",           UINT8, 4),
  ("Resp",              UINT8),
  ("Rsvd3",             UINT8),
  ("EhsLen",            UINT8),
  ("Rsvd4",             UINT8),
  ("DataSegLen",        UINT16),
  ("OutputParam1",      UINT32),
  ("OutputParam2",      UINT32),
  ("Rsvd5",             UINT8 * 12)
  ]

class UTP_UPIU_TSF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Opcode",      UINT8),
  ("DescId",      UINT8),
  ("Index",       UINT8),
  ("Selector",    UINT8),
  ("Rsvd1",       UINT16),
  ("Length",      UINT16),
  ("Value",       UINT32),
  ("Rsvd2",       UINT32)
  ]

class UTP_QUERY_REQ_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",   UINT8, 6),
  ("Dd",          UINT8, 1),
  ("Hd",          UINT8, 1),
  ("Flags",       UINT8),
  ("Rsvd1",       UINT8),
  ("TaskTag",     UINT8),
  ("Rsvd2",       UINT8),
  ("QueryFunc",   UINT8),
  ("Rsvd3",       UINT8 * 2),
  ("EhsLen",      UINT8),
  ("Rsvd4",       UINT8),
  ("DataSegLen",  UINT16),
  ("Tsf",         UTP_UPIU_TSF),
  ("Rsvd5",       UINT8 * 4)
  # ("Data",      UINT8 * N)
  ]

QUERY_FUNC_STD_READ_REQ   = 0x01
QUERY_FUNC_STD_WRITE_REQ  = 0x81

UtpQueryFuncOpcodeNop     = 0x00
UtpQueryFuncOpcodeRdDesc  = 0x01
UtpQueryFuncOpcodeWrDesc  = 0x02
UtpQueryFuncOpcodeRdAttr  = 0x03
UtpQueryFuncOpcodeWrAttr  = 0x04
UtpQueryFuncOpcodeRdFlag  = 0x05
UtpQueryFuncOpcodeSetFlag = 0x06
UtpQueryFuncOpcodeClrFlag = 0x07
UtpQueryFuncOpcodeTogFlag = 0x08
UTP_QUERY_FUNC_OPCODE     = ENUM

class UTP_QUERY_RESP_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",     UINT8, 6),
  ("Dd",            UINT8, 1),
  ("Hd",            UINT8, 1),
  ("Flags",         UINT8),
  ("Rsvd1",         UINT8),
  ("TaskTag",       UINT8),
  ("Rsvd2",         UINT8),
  ("QueryFunc",     UINT8),
  ("QueryResp",     UINT8),
  ("Rsvd3",         UINT8),
  ("EhsLen",        UINT8),
  ("DevInfo",       UINT8),
  ("DataSegLen",    UINT16),
  ("Tsf",           UTP_UPIU_TSF),
  ("Rsvd4",         UINT8 * 4)
  # ("Data",          UINT8 * N)
  ]

UfsUtpQueryResponseSuccess             = 0x00
UfsUtpQueryResponseParamNotReadable    = 0xF6
UfsUtpQueryResponseParamNotWriteable   = 0xF7
UfsUtpQueryResponseParamAlreadyWritten = 0xF8
UfsUtpQueryResponseInvalidLen          = 0xF9
UfsUtpQueryResponseInvalidVal          = 0xFA
UfsUtpQueryResponseInvalidSelector     = 0xFB
UfsUtpQueryResponseInvalidIndex        = 0xFC
UfsUtpQueryResponseInvalidIdn          = 0xFD
UfsUtpQueryResponseInvalidOpc          = 0xFE
UfsUtpQueryResponseGeneralFailure      = 0xFF
UTP_QUERY_RESP_CODE                    = ENUM

class UTP_REJ_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",     UINT8, 6),
  ("Dd",            UINT8, 1),
  ("Hd",            UINT8, 1),
  ("Flags",         UINT8),
  ("Lun",           UINT8),
  ("TaskTag",       UINT8),
  ("Rsvd1",         UINT8, 4),
  ("Iid",           UINT8, 4),
  ("Rsvd2",         UINT8, 4),
  ("Ext_Iid",       UINT8, 4),
  ("Response",      UINT8),
  ("Rsvd3",         UINT8),
  ("EhsLen",        UINT8),
  ("DevInfo",       UINT8),
  ("DataSegLen",    UINT16),
  ("HdrSts",        UINT8),
  ("Rsvd4",         UINT8),
  ("E2ESts",        UINT8),
  ("Rsvd5",         UINT8),
  ("Rsvd6",         UINT8 * 16)
  ]

class UTP_NOP_OUT_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",       UINT8, 6),
  ("Dd",              UINT8, 1),
  ("Hd",              UINT8, 1),
  ("Flags",           UINT8),
  ("Rsvd1",           UINT8),
  ("TaskTag",         UINT8),
  ("Rsvd2",           UINT8 * 4),
  ("EhsLen",          UINT8),
  ("Rsvd3",           UINT8),
  ("DataSegLen",      UINT16),
  ("Rsvd4",           UINT8 * 20)
  ]

class UTP_NOP_OUT_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TransCode",           UINT8, 6),
  ("Dd",                  UINT8, 1),
  ("Hd",                  UINT8, 1),
  ("Flags",               UINT8),
  ("Rsvd1",               UINT8),
  ("TaskTag",             UINT8),
  ("Rsvd2",               UINT8 * 2),
  ("Resp",                UINT8),
  ("Rsvd3",               UINT8),
  ("EhsLen",              UINT8), 
  ("DevInfo",             UINT8), 
  ("DataSegLen",          UINT16),
  ("Rsvd4",               UINT8 * 20)
  ]

UfsDeviceDesc    = 0x00
UfsConfigDesc    = 0x01
UfsUnitDesc      = 0x02
UfsInterConnDesc = 0x04
UfsStringDesc    = 0x05
UfsGeometryDesc  = 0x07
UfsPowerDesc     = 0x08
UfsDevHealthDesc = 0x09
UFS_DESC_IDN     = ENUM

class UTP_NOP_OUT_UPIU (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                                    UINT8),
  ("DescType",                                  UINT8),
  ("Device",                                    UINT8),
  ("DevClass",                                  UINT8),
  ("DevSubClass",                               UINT8),
  ("Protocol",                                  UINT8),
  ("NumLun",                                    UINT8),
  ("NumWLun",                                   UINT8),
  ("BootEn",                                    UINT8),
  ("DescAccessEn",                              UINT8),
  ("InitPowerMode",                             UINT8),
  ("HighPriorityLun",                           UINT8),
  ("SecureRemovalType",                         UINT8),
  ("SecurityLun",                               UINT8),
  ("BgOpsTermLat",                              UINT8),
  ("InitActiveIccLevel",                        UINT8),
  ("SpecVersion",                               UINT16),
  ("ManufactureDate",                           UINT16),
  ("ManufacturerName",                          UINT8),
  ("ProductName",                               UINT8),
  ("SerialName",                                UINT8),
  ("OemId",                                     UINT8),
  ("ManufacturerId",                            UINT16),
  ("Ud0BaseOffset",                             UINT8),
  ("Ud0ConfParamLen",                           UINT8),
  ("DevRttCap",                                 UINT8),
  ("PeriodicRtcUpdate",                         UINT16),
  ("UFSFeaturesSupport",                        UINT8),
  ("FFUTimeout",                                UINT8),
  ("QueueDepth",                                UINT8),
  ("DeviceVersion",                             UINT16),
  ("NumSecureWPArea",                           UINT8),
  ("PSAMaxDataSize",                            UINT32),
  ("PSAStateTimeout",                           UINT8),
  ("ProductRevisionLevel",                      UINT8),
  ("Rsvd1",                                     UINT8 * 5),
  ("Rsvd2",                                     UINT8 * 16),
  ("Rsvd3",                                     UINT8 * 3),
  ("Rsvd4",                                     UINT8 * 12),
  ("ExtendedUFSFeaturesSupport",                UINT32),
  ("WriteBoosterBufPreserveUserSpaceEn",        UINT8),
  ("WriteBoosterBufType",                       UINT8),
  ("NumSharedWriteBoosterAllocUnits",           UINT32)
  ]

class UFS_SPEC_VERSION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Suffix",    UINT8, 4),
  ("Minor",     UINT8, 4),
  ("Major",     UINT8)
  ]
class UFS_SPEC_VERSION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      UFS_SPEC_VERSION_Bits),
    ("Data",      UINT16)
  ]

class EXTENDED_UFS_FEATURES_SUPPORT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("FFU",                     UINT32, 1),
  ("PSA",                     UINT32, 1),
  ("DeviceLifeSpan",          UINT32, 1),
  ("RefreshOperation",        UINT32, 1),
  ("TooHighTemp",             UINT32, 1),
  ("TooLowTemp",              UINT32, 1),
  ("ExtendedTemp",            UINT32, 1),
  ("Rsvd1",                   UINT32, 1),
  ("WriteBooster",            UINT32, 1),
  ("PerformanceThrottling",   UINT32, 1),
  ("AdvancedRPMB",            UINT32, 1),
  ("Rsvd2",                   UINT32, 3),
  ("Barrier",                 UINT32, 1),
  ("ClearErrorHistory",       UINT32, 1),
  ("Ext_Iid",                 UINT32, 1),
  ("Rsvd3",                   UINT32, 1),
  ("Rsvd4",                   UINT32, 14)
  ]
class EXTENDED_UFS_FEATURES_SUPPORT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      EXTENDED_UFS_FEATURES_SUPPORT_Bits),
    ("Data",      UINT32)
  ]

class UFS_CONFIG_DESC_GEN_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                                UINT8),
  ("DescType",                              UINT8),
  ("ConfDescContinue",                      UINT8),
  ("BootEn",                                UINT8),
  ("DescAccessEn",                          UINT8),
  ("InitPowerMode",                         UINT8),
  ("HighPriorityLun",                       UINT8),
  ("SecureRemovalType",                     UINT8),
  ("InitActiveIccLevel",                    UINT8),
  ("PeriodicRtcUpdate",                     UINT16),
  ("Rsvd1",                                 UINT8),
  ("RpmbRegionEnable",                      UINT8),
  ("RpmbRegion1Size",                       UINT8),
  ("RpmbRegion2Size",                       UINT8),
  ("RpmbRegion3Size",                       UINT8),
  ("WriteBoosterBufPreserveUserSpaceEn",    UINT8),
  ("WriteBoosterBufType",                   UINT8),
  ("NumSharedWriteBoosterAllocUnits",       UINT32)
  ]

class UFS_CONFIG_DESC_EXT_HEADER0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",              UINT8),
    ("DescType",            UINT8),
    ("ConfDescContinue",    UINT8),
    ("Rsvd1",               UINT8 * 19)
  ]

class UFS_UNIT_DESC_CONFIG_PARAMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("LunEn",                             UINT8),
  ("BootLunId",                         UINT8),
  ("LunWriteProt",                      UINT8),
  ("MemType",                           UINT8),
  ("NumAllocUnits",                     UINT32),
  ("DataReliability",                   UINT8),
  ("LogicBlkSize",                      UINT8),
  ("ProvisionType",                     UINT8),
  ("CtxCap",                            UINT16),
  ("Rsvd1",                             UINT8 *3),
  ("Rsvd2",                             UINT8 * 6),
  ("LuNumWriteBoosterBufAllocUnits",    UINT32)
  ]

class UFS_CONFIG_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Header",              UFS_CONFIG_DESC_GEN_HEADER),
  ("UnitDescConfParams",  UFS_UNIT_DESC_CONFIG_PARAMS * 8),
  ]

class UFS_GEOMETRY_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                                        UINT8),
  ("DescType",                                      UINT8),
  ("MediaTech",                                     UINT8),
  ("Rsvd1",                                         UINT8),
  ("TotalRawDevCapacity",                           UINT64),
  ("MaxNumberLu",                                   UINT8),
  ("SegSize",                                       UINT32),
  ("AllocUnitSize",                                 UINT8),
  ("MinAddrBlkSize",                                UINT8),
  ("OptReadBlkSize",                                UINT8),
  ("OptWriteBlkSize",                               UINT8),
  ("MaxInBufSize",                                  UINT8),
  ("MaxOutBufSize",                                 UINT8),
  ("RpmbRwSize",                                    UINT8),
  ("DynamicCapacityResourcePolicy",                 UINT8),
  ("DataOrder",                                     UINT8),
  ("MaxCtxIdNum",                                   UINT8),
  ("SysDataTagUnitSize",                            UINT8),
  ("SysDataResUnitSize",                            UINT8),
  ("SupSecRemovalTypes",                            UINT8),
  ("SupMemTypes",                                   UINT16),
  ("SysCodeMaxNumAllocUnits",                       UINT32),
  ("SupCodeCapAdjFac",                              UINT16),
  ("NonPersMaxNumAllocUnits",                       UINT32),
  ("NonPersCapAdjFac",                              UINT16),
  ("Enhance1MaxNumAllocUnits",                      UINT32),
  ("Enhance1CapAdjFac",                             UINT16),
  ("Enhance2MaxNumAllocUnits",                      UINT32),
  ("Enhance2CapAdjFac",                             UINT16),
  ("Enhance3MaxNumAllocUnits",                      UINT32),
  ("Enhance3CapAdjFac",                             UINT16),
  ("Enhance4MaxNumAllocUnits",                      UINT32),
  ("Enhance4CapAdjFac",                             UINT16),
  ("OptLogicBlkSize",                               UINT32),
  ("Rsvd2",                                         UINT8 * 5),
  ("Rsvd3",                                         UINT8 * 2),
  ("WriteBoosterBufMaxNumAllocUnits",               UINT32),
  ("DeviceMaxWriteBoosterLus",                      UINT8),
  ("WriteBoosterBufCapAdjFac",                      UINT8),
  ("SupWriteBoosterBufUserSpaceReductionTypes",     UINT8),
  ("SupWriteBoosterBufTypes",                       UINT8)
  ]

class UFS_UNIT_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                            UINT8),
  ("DescType",                          UINT8),
  ("UnitIdx",                           UINT8),
  ("LunEn",                             UINT8),
  ("BootLunId",                         UINT8),
  ("LunWriteProt",                      UINT8),
  ("LunQueueDep",                       UINT8),
  ("PsaSensitive",                      UINT8),
  ("MemType",                           UINT8),
  ("DataReliability",                   UINT8),
  ("LogicBlkSize",                      UINT8),
  ("LogicBlkCount",                     UINT64),
  ("EraseBlkSize",                      UINT32),
  ("ProvisionType",                     UINT8),
  ("PhyMemResCount",                    UINT64),
  ("CtxCap",                            UINT16),
  ("LargeUnitGranularity",              UINT8),
  ("Rsvd1",                             UINT8 * 6),
  ("LuNumWriteBoosterBufAllocUnits",    UINT32)
  ]

class UFS_RPMB_UNIT_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",              UINT8),
  ("DescType",            UINT8),
  ("UnitIdx",             UINT8),
  ("LunEn",               UINT8),
  ("BootLunId",           UINT8),
  ("LunWriteProt",        UINT8),
  ("LunQueueDep",         UINT8),
  ("PsaSensitive",        UINT8),
  ("MemType",             UINT8),
  ("RpmbRegionEnable",    UINT8),
  ("LogicBlkSize",        UINT8),
  ("LogicBlkCount",       UINT64),
  ("RpmbRegion0Size",     UINT8),
  ("RpmbRegion1Size",     UINT8),
  ("RpmbRegion2Size",     UINT8),
  ("RpmbRegion3Size",     UINT8),
  ("ProvisionType",       UINT8),
  ("PhyMemResCount",      UINT64),
  ("Rsvd3",               UINT8 * 3)
  ]

class UFS_POWER_PARAM_ELEMENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Value",     UINT16, 12),
  ("Rsvd1",     UINT16, 2),
  ("Unit",      UINT16, 2)
  ]

class UFS_POWER_DESC0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                      UINT8),
  ("DescType",                    UINT8),
  ("ActiveIccLevelVcc",           UFS_POWER_PARAM_ELEMENT * 16),
  ("ActiveIccLevelVccQ",          UFS_POWER_PARAM_ELEMENT * 16),
  ("ActiveIccLevelVccQ2",         UFS_POWER_PARAM_ELEMENT * 16)
  ]

class UFS_INTER_CONNECT_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                      UINT8),
  ("DescType",                    UINT8),
  ("UniProVer",                   UINT16),
  ("MphyVer",                     UINT16)
  ]

class UFS_STRING_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Length",                      UINT8),
  ("DescType",                    UINT8),
  ("Unicode",                     UINT16 * 126)
  ]

UfsFlagDevInit             = 0x01
UfsFlagPermWpEn            = 0x02
UfsFlagPowerOnWpEn         = 0x03
UfsFlagBgOpsEn             = 0x04
UfsFlagDevLifeSpanModeEn   = 0x05
UfsFlagPurgeEn             = 0x06
UfsFlagRefreshEn           = 0x07
UfsFlagPhyResRemoval       = 0x08
UfsFlagBusyRtc             = 0x09
UfsFlagPermDisFwUpdate     = 0x0B
UfsFlagWriteBoosterEn      = 0x0E
UfsFlagWbBufFlushEn        = 0x0F
UfsFlagWbBufFlushHibernate = 0x10
UFS_FLAGS_IDN              = ENUM

UfsAttrBootLunEn                    = 0x00
UfsAttrCurPowerMode                 = 0x02
UfsAttrActiveIccLevel               = 0x03
UfsAttrOutOfOrderDataEn             = 0x04
UfsAttrBgOpStatus                   = 0x05
UfsAttrPurgeStatus                  = 0x06
UfsAttrMaxDataInSize                = 0x07
UfsAttrMaxDataOutSize               = 0x08
UfsAttrDynCapNeeded                 = 0x09
UfsAttrRefClkFreq                   = 0x0a
UfsAttrConfigDescLock               = 0x0b
UfsAttrMaxNumOfRtt                  = 0x0c
UfsAttrExceptionEvtCtrl             = 0x0d
UfsAttrExceptionEvtSts              = 0x0e
UfsAttrSecondsPassed                = 0x0f
UfsAttrContextConf                  = 0x10
UfsAttrDeviceFfuStatus              = 0x14
UfsAttrPsaState                     = 0x15
UfsAttrPsaDataSize                  = 0x16
UfsAttrRefClkGatingWaitTime         = 0x17
UfsAttrDeviceCaseRoughTemp          = 0x18
UfsAttrDeviceTooHighTempBound       = 0x19
UfsAttrDeviceTooLowTempBound        = 0x1a
UfsAttrThrottlingStatus             = 0x1b
UfsAttrWriteBoosterBufFlushStatus   = 0x1c
UfsAttrAvailableWriteBoosterBufSize = 0x1d
UfsAttrWriteBoosterBufLifeTimeEst   = 0x1e
UfsAttrCurrentWriteBoosterBufSize   = 0x1f
UfsAttrExtIidEn                     = 0x2a
UfsAttrHostHintCacheSize            = 0x2b
UfsAttrRefreshStatus                = 0x2c
UfsAttrRefreshFreq                  = 0x2d
UfsAttrRefreshUnit                  = 0x2e
UfsAttrRefreshMethod                = 0x2f
UfsAttrTimestamp                    = 0x30
UFS_ATTR_IDN                        = ENUM

