# Sd.py
#
# EfiPy2.MdePkg.IndustryStandard.Sd
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

SD_GO_IDLE_STATE         = 0
SD_ALL_SEND_CID          = 2
SD_SET_RELATIVE_ADDR     = 3
SD_SET_DSR               = 4
SDIO_SEND_OP_COND        = 5
SD_SWITCH_FUNC           = 6
SD_SELECT_DESELECT_CARD  = 7
SD_SEND_IF_COND          = 8
SD_SEND_CSD              = 9
SD_SEND_CID              = 10
SD_VOLTAGE_SWITCH        = 11
SD_STOP_TRANSMISSION     = 12
SD_SEND_STATUS           = 13
SD_GO_INACTIVE_STATE     = 15
SD_SET_BLOCKLEN          = 16
SD_READ_SINGLE_BLOCK     = 17
SD_READ_MULTIPLE_BLOCK   = 18
SD_SEND_TUNING_BLOCK     = 19
SD_SPEED_CLASS_CONTROL   = 20
SD_SET_BLOCK_COUNT       = 23
SD_WRITE_SINGLE_BLOCK    = 24
SD_WRITE_MULTIPLE_BLOCK  = 25
SD_PROGRAM_CSD           = 27
SD_SET_WRITE_PROT        = 28
SD_CLR_WRITE_PROT        = 29
SD_SEND_WRITE_PROT       = 30
SD_ERASE_WR_BLK_START    = 32
SD_ERASE_WR_BLK_END      = 33
SD_ERASE                 = 38
SD_LOCK_UNLOCK           = 42
SD_READ_EXTR_SINGLE      = 48
SD_WRITE_EXTR_SINGLE     = 49
SDIO_RW_DIRECT           = 52
SDIO_RW_EXTENDED         = 53
SD_APP_CMD               = 55
SD_GEN_CMD               = 56
SD_READ_EXTR_MULTI       = 58
SD_WRITE_EXTR_MULTI      = 59

SD_SET_BUS_WIDTH           = 6           # ACMD6
SD_STATUS                  = 13          # ACMD13
SD_SEND_NUM_WR_BLOCKS      = 22          # ACMD22
SD_SET_WR_BLK_ERASE_COUNT  = 23          # ACMD23
SD_SEND_OP_COND            = 41          # ACMD41
SD_SET_CLR_CARD_DETECT     = 42          # ACMD42
SD_SEND_SCR                = 51          # ACMD51

class SD_CID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",             UINT8,  1),
    ("Crc",                 UINT8,  7),
    ("ManufacturingDate",   UINT16, 12),
    ("Reserved",            UINT16, 4),
    ("ProductSerialNumber", UINT8 * 4),
    ("ProductRevision",     UINT8),
    ("ProductName",         UINT8 * 5),
    ("OemId",               UINT8 * 2),
    ("ManufacturerId",      UINT8)
    ]

class SD_CSD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",         UINT32, 1),
    ("Crc",             UINT32, 7),
    ("Reserved",        UINT32, 2),
    ("FileFormat",      UINT32, 2),
    ("TmpWriteProtect", UINT32, 1),
    ("PermWriteProtect",UINT32, 1),
    ("Copy",            UINT32, 1),
    ("FileFormatGrp",   UINT32, 1),
    ("Reserved1",       UINT32, 5),
    ("WriteBlPartial",  UINT32, 1),
    ("WriteBlLen",      UINT32, 4),
    ("R2WFactor",       UINT32, 3),
    ("Reserved2",       UINT32, 2),
    ("WpGrpEnable",     UINT32, 1),

    ("WpGrpSize",       UINT32, 7),
    ("SectorSize",      UINT32, 7),
    ("EraseBlkEn",      UINT32, 1),
    ("CSizeMul",        UINT32, 3),
    ("VddWCurrMax",     UINT32, 3),
    ("VddWCurrMin",     UINT32, 3),
    ("VddRCurrMax",     UINT32, 3),
    ("VddRCurrMin",     UINT32, 3),
    ("CSizeLow",        UINT32, 2),

    ("CSizeHigh",       UINT32, 10),
    ("Reserved4",       UINT32, 2),
    ("DsrImp",          UINT32, 1),
    ("ReadBlkMisalign", UINT32, 1),
    ("WriteBlkMisalign",UINT32, 1),
    ("ReadBlPartial",   UINT32, 1),
    ("ReadBlLen",       UINT32, 4),
    ("Ccc",             UINT32, 12),

    ("TranSpeed",       UINT32, 8),
    ("Nsac",            UINT32, 8),
    ("Taac",            UINT32, 8),
    ("Reserved5",       UINT32, 6),
    ("CsdStructure",    UINT32, 2)
    ]

class SD_CSD2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",             UINT32, 1),
    ("Crc",                 UINT32, 7),
    ("Reserved",            UINT32, 2),
    ("FileFormat",          UINT32, 2),
    ("TmpWriteProtect",     UINT32, 1),
    ("PermWriteProtect",    UINT32, 1),
    ("Copy",                UINT32, 1),
    ("FileFormatGrp",       UINT32, 1),
    ("Reserved1",           UINT32, 5),
    ("WriteBlPartial",      UINT32, 1),
    ("WriteBlLen",          UINT32, 4),
    ("R2WFactor",           UINT32, 3),
    ("Reserved2",           UINT32, 2),
    ("WpGrpEnable",         UINT32, 1),

    ("WpGrpSize",           UINT32, 7),
    ("SectorSize",          UINT32, 7),
    ("EraseBlkEn",          UINT32, 1),
    ("Reserved3",           UINT32, 1),
    ("CSizeLow",            UINT32, 16),

    ("CSizeHigh",           UINT32, 6),
    ("Reserved4",           UINT32, 6),
    ("DsrImp",              UINT32, 1),
    ("ReadBlkMisalign",     UINT32, 1),
    ("WriteBlkMisalign",    UINT32, 1),
    ("ReadBlPartial",       UINT32, 1),
    ("ReadBlLen",           UINT32, 4),
    ("Ccc",                 UINT32, 12),

    ("TranSpeed",           UINT32, 8),
    ("Nsac",                UINT32, 8),
    ("Taac",                UINT32, 8),
    ("Reserved5",           UINT32, 6),
    ("CsdStructure",        UINT32, 2)
    ]

class SD_SCR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT32),

    ("CmdSupport",          UINT32, 4),
    ("Reserved1",           UINT32, 6),
    ("SdSpec4",             UINT32, 1),
    ("ExSecurity",          UINT32, 4),
    ("SdSpec3",             UINT32, 1),
    ("SdBusWidths",         UINT32, 4),
    ("SdSecurity",          UINT32, 3),
    ("DataStatAfterErase",  UINT32, 1),
    ("SdSpec",              UINT32, 4),
    ("ScrStructure",        UINT32, 4)
    ]

