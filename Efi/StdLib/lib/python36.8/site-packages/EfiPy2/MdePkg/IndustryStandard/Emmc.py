# Emmc.py
#
# EfiPy2.MdePkg.IndustryStandard.Emmc
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

EMMC_GO_IDLE_STATE         = 0
EMMC_SEND_OP_COND          = 1
EMMC_ALL_SEND_CID          = 2
EMMC_SET_RELATIVE_ADDR     = 3
EMMC_SET_DSR               = 4
EMMC_SLEEP_AWAKE           = 5
EMMC_SWITCH                = 6
EMMC_SELECT_DESELECT_CARD  = 7
EMMC_SEND_EXT_CSD          = 8
EMMC_SEND_CSD              = 9
EMMC_SEND_CID              = 10
EMMC_STOP_TRANSMISSION     = 12
EMMC_SEND_STATUS           = 13
EMMC_BUSTEST_R             = 14
EMMC_GO_INACTIVE_STATE     = 15
EMMC_SET_BLOCKLEN          = 16
EMMC_READ_SINGLE_BLOCK     = 17
EMMC_READ_MULTIPLE_BLOCK   = 18
EMMC_BUSTEST_W             = 19
EMMC_SEND_TUNING_BLOCK     = 21
EMMC_SET_BLOCK_COUNT       = 23
EMMC_WRITE_BLOCK           = 24
EMMC_WRITE_MULTIPLE_BLOCK  = 25
EMMC_PROGRAM_CID           = 26
EMMC_PROGRAM_CSD           = 27
EMMC_SET_WRITE_PROT        = 28
EMMC_CLR_WRITE_PROT        = 29
EMMC_SEND_WRITE_PROT       = 30
EMMC_SEND_WRITE_PROT_TYPE  = 31
EMMC_ERASE_GROUP_START     = 35
EMMC_ERASE_GROUP_END       = 36
EMMC_ERASE                 = 38
EMMC_FAST_IO               = 39
EMMC_GO_IRQ_STATE          = 40
EMMC_LOCK_UNLOCK           = 42
EMMC_SET_TIME              = 49
EMMC_PROTOCOL_RD           = 53
EMMC_PROTOCOL_WR           = 54
EMMC_APP_CMD               = 55
EMMC_GEN_CMD               = 56

EmmcPartitionUserData = 0
EmmcPartitionBoot1    = 1
EmmcPartitionBoot2    = 2
EmmcPartitionRPMB     = 3
EmmcPartitionGP1      = 4
EmmcPartitionGP2      = 5
EmmcPartitionGP3      = 6
EmmcPartitionGP4      = 7
EmmcPartitionUnknown  = 8
EMMC_PARTITION_TYPE = ENUM

class EMMC_CID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",             UINT8, 1),              # Not used [0:0]
    ("Crc",                 UINT8, 7),              # CRC [7:1]
    ("ManufacturingDate",   UINT8),                 # Manufacturing date [15:8]
    ("ProductSerialNumber", UINT8 * 4),             # Product serial number [47:16]
    ("ProductRevision",     UINT8),                 # Product revision [55:48]
    ("ProductName",         UINT8 * 6),             # Product name [103:56]
    ("OemId",               UINT8),                 # OEM/Application ID [111:104]
    ("DeviceType",          UINT8, 2),              # Device/BGA [113:112]
    ("Reserved",            UINT8, 6),              # Reserved [119:114]
    ("ManufacturerId",      UINT8)                  # Manufacturer ID [127:120]
  ]

class EMMC_CSD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",             UINT32, 1),
    ("Crc",                 UINT32, 7),
    ("Ecc",                 UINT32, 2),
    ("FileFormat",          UINT32, 2),
    ("TmpWriteProtect",     UINT32, 1),
    ("PermWriteProtect",    UINT32, 1),
    ("Copy",                UINT32, 1),
    ("FileFormatGrp",       UINT32, 1),
    ("ContentProtApp",      UINT32, 1),
    ("Reserved",            UINT32, 4),
    ("WriteBlPartial",      UINT32, 1),
    ("WriteBlLen",          UINT32, 4),
    ("R2WFactor",           UINT32, 3),
    ("DefaultEcc",          UINT32, 2),
    ("WpGrpEnable",         UINT32, 1),
    ("WpGrpSize",           UINT32, 5),
    ("EraseGrpMult",        UINT32, 5),
    ("EraseGrpSize",        UINT32, 5),
    ("CSizeMult",           UINT32, 3),
    ("VddWCurrMax",         UINT32, 3),
    ("VddWCurrMin",         UINT32, 3),
    ("VddRCurrMax",         UINT32, 3),
    ("VddRCurrMin",         UINT32, 3),
    ("CSizeLow",            UINT32, 2),
    ("CSizeHigh",           UINT32, 10),
    ("Reserved1",           UINT32, 2),
    ("DsrImp",              UINT32, 1),
    ("ReadBlkMisalign",     UINT32, 1),
    ("WriteBlkMisalign",    UINT32, 1),
    ("ReadBlPartial",       UINT32, 1),
    ("ReadBlLen",           UINT32, 4),
    ("Ccc",                 UINT32, 12),
    ("TranSpeed",           UINT32, 8),
    ("Nsac",                UINT32, 8),
    ("Taac",                UINT32, 8),
    ("Reserved2",           UINT32, 2),
    ("SpecVers",            UINT32, 4),
    ("CsdStructure",        UINT32, 2)
  ]

class EMMC_CSD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                        UINT8 * 16),
    ("SecureRemovalType",               UINT8),
    ("ProductStateAwarenessEnablement", UINT8),
    ("MaxPreLoadingDataSize",           UINT8 * 4),
    ("PreLoadingDataSize",              UINT8 * 4),
    ("FfuStatus",                       UINT8),
    ("Reserved1",                       UINT8 * 2),
    ("ModeOperationCodes",              UINT8),
    ("ModeConfig",                      UINT8),
    ("Reserved2",                       UINT8),
    ("FlushCache",                      UINT8),
    ("CacheCtrl",                       UINT8),
    ("PowerOffNotification",            UINT8),
    ("PackedFailureIndex",              UINT8),
    ("PackedCommandStatus",             UINT8),
    ("ContextConf",                     UINT8 * 15),
    ("ExtPartitionsAttribute",          UINT8 * 2),
    ("ExceptionEventsStatus",           UINT8 * 2),
    ("ExceptionEventsCtrl",             UINT8 * 2),
    ("DyncapNeeded",                    UINT8),
    ("Class6Ctrl",                      UINT8),
    ("IniTimeoutEmu",                   UINT8),
    ("DataSectorSize",                  UINT8),
    ("UseNativeSector",                 UINT8),
    ("NativeSectorSize",                UINT8),
    ("VendorSpecificField",             UINT8 * 64),
    ("Reserved3",                       UINT8 * 2),
    ("ProgramCidCsdDdrSupport",         UINT8),
    ("PeriodicWakeup",                  UINT8),
    ("TcaseSupport",                    UINT8),
    ("ProductionStateAwareness",        UINT8),
    ("SecBadBlkMgmnt",                  UINT8),
    ("Reserved4",                       UINT8),
    ("EnhStartAddr",                    UINT8 * 4),
    ("EnhSizeMult",                     UINT8 * 3),
    ("GpSizeMult",                      UINT8 * 12),
    ("PartitionSettingCompleted",       UINT8),
    ("PartitionsAttribute",             UINT8),
    ("MaxEnhSizeMult",                  UINT8 * 3),
    ("PartitioningSupport",             UINT8),
    ("HpiMgmt",                         UINT8),
    ("RstFunction",                     UINT8),
    ("BkopsEn",                         UINT8),
    ("BkopsStart",                      UINT8),
    ("SanitizeStart",                   UINT8),
    ("WrRelParam",                      UINT8),
    ("WrRelSet",                        UINT8),
    ("RpmbSizeMult",                    UINT8),
    ("FwConfig",                        UINT8),
    ("Reserved5",                       UINT8),
    ("UserWp",                          UINT8),
    ("Reserved6",                       UINT8),
    ("BootWp",                          UINT8),
    ("BootWpStatus",                    UINT8),
    ("EraseGroupDef",                   UINT8),
    ("Reserved7",                       UINT8),
    ("BootBusConditions",               UINT8),
    ("BootConfigProt",                  UINT8),
    ("PartitionConfig",                 UINT8),
    ("Reserved8",                       UINT8),
    ("ErasedMemCont",                   UINT8),
    ("Reserved9",                       UINT8),
    ("BusWidth",                        UINT8),
    ("Reserved10",                      UINT8),
    ("HsTiming",                        UINT8),
    ("Reserved11",                      UINT8),
    ("PowerClass",                      UINT8),
    ("Reserved12",                      UINT8),
    ("CmdSetRev",                       UINT8),
    ("Reserved13",                      UINT8),
    ("CmdSet",                          UINT8),
    ("ExtCsdRev",                       UINT8),
    ("Reserved14",                      UINT8),
    ("CsdStructure",                    UINT8),
    ("Reserved15",                      UINT8),
    ("DeviceType",                      UINT8),
    ("DriverStrength",                  UINT8),
    ("OutOfInterruptTime",              UINT8),
    ("PartitionSwitchTime",             UINT8),
    ("PwrCl52M195V",                    UINT8),
    ("PwrCl26M195V",                    UINT8),
    ("PwrCl52M360V",                    UINT8),
    ("PwrCl26M360V",                    UINT8),
    ("Reserved16",                      UINT8),
    ("MinPerfR4B26M",                   UINT8),
    ("MinPerfW4B26M",                   UINT8),
    ("MinPerfR8B26M4B52M",              UINT8),
    ("MinPerfW8B26M4B52M",              UINT8),
    ("MinPerfR8B52M",                   UINT8),
    ("MinPerfW8B52M",                   UINT8),
    ("Reserved17",                      UINT8),
    ("SecCount",                        UINT8 * 4),
    ("SleepNotificationTime",           UINT8),
    ("SATimeout",                       UINT8),
    ("ProductionStateAwarenessTimeout", UINT8),
    ("SCVccq",                          UINT8),
    ("SCVcc",                           UINT8),
    ("HcWpGrpSize",                     UINT8),
    ("RelWrSecC",                       UINT8),
    ("EraseTimeoutMult",                UINT8),
    ("HcEraseGrpSize",                  UINT8),
    ("AccSize",                         UINT8),
    ("BootSizeMult",                    UINT8),
    ("Reserved18",                      UINT8),
    ("BootInfo",                        UINT8),
    ("SecTrimMult",                     UINT8),
    ("SecEraseMult",                    UINT8),
    ("SecFeatureSupport",               UINT8),
    ("TrimMult",                        UINT8),
    ("Reserved19",                      UINT8),
    ("MinPerfDdrR8b52M",                UINT8),
    ("MinPerfDdrW8b52M",                UINT8),
    ("PwrCl200M130V",                   UINT8),
    ("PwrCl200M195V",                   UINT8),
    ("PwrClDdr52M195V",                 UINT8),
    ("PwrClDdr52M360V",                 UINT8),
    ("Reserved20",                      UINT8),
    ("IniTimeoutAp",                    UINT8),
    ("CorrectlyPrgSectorsNum",          UINT8 * 4),
    ("BkopsStatus",                     UINT8),
    ("PowerOffLongTime",                UINT8),
    ("GenericCmd6Time",                 UINT8),
    ("CacheSize",                       UINT8 * 4),
    ("PwrClDdr200M360V",                UINT8),
    ("FirmwareVersion",                 UINT8 * 8),
    ("DeviceVersion",                   UINT8 * 2),
    ("OptimalTrimUnitSize",             UINT8),
    ("OptimalWriteSize",                UINT8),
    ("OptimalReadSize",                 UINT8),
    ("PreEolInfo",                      UINT8),
    ("DeviceLifeTimeEstTypA",           UINT8),
    ("DeviceLifeTimeEstTypB",           UINT8),
    ("VendorProprietaryHealthReport",   UINT8 * 32),
    ("NumOfFwSectorsProgrammed",        UINT8 * 4),
    ("Reserved21",                      UINT8 * 181),
    ("FfuArg",                          UINT8 * 4),
    ("OperationCodeTimeout",            UINT8),
    ("FfuFeatures",                     UINT8),
    ("SupportedModes",                  UINT8),
    ("ExtSupport",                      UINT8),
    ("LargeUnitSizeM1",                 UINT8),
    ("ContextCapabilities",             UINT8),
    ("TagResSize",                      UINT8),
    ("TagUnitSize",                     UINT8),
    ("DataTagSupport",                  UINT8),
    ("MaxPackedWrites",                 UINT8),
    ("MaxPackedReads",                  UINT8),
    ("BkOpsSupport",                    UINT8),
    ("HpiFeatures",                     UINT8),
    ("SupportedCmdSet",                 UINT8),
    ("ExtSecurityErr",                  UINT8),
    ("Reserved22",                      UINT8 * 6)
  ]
