# Scsi.py
#
# EfiPy2.MdePkg.IndustryStandard.Scsi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

EFI_SCSI_OP_CHANGE_DEFINITION = 0x40
EFI_SCSI_OP_COMPARE           = 0x39
EFI_SCSI_OP_COPY              = 0x18
EFI_SCSI_OP_COPY_VERIFY       = 0x3a
EFI_SCSI_OP_INQUIRY           = 0x12
EFI_SCSI_OP_LOG_SELECT        = 0x4c
EFI_SCSI_OP_LOG_SENSE         = 0x4d
EFI_SCSI_OP_MODE_SEL6         = 0x15
EFI_SCSI_OP_MODE_SEL10        = 0x55
EFI_SCSI_OP_MODE_SEN6         = 0x1a
EFI_SCSI_OP_MODE_SEN10        = 0x5a
EFI_SCSI_OP_READ_BUFFER       = 0x3c
EFI_SCSI_OP_RECEIVE_DIAG      = 0x1c
EFI_SCSI_OP_REQUEST_SENSE     = 0x03
EFI_SCSI_OP_SEND_DIAG         = 0x1d
EFI_SCSI_OP_TEST_UNIT_READY   = 0x00
EFI_SCSI_OP_WRITE_BUFF        = 0x3b

EFI_SCSI_OP_FORMAT          = 0x04
EFI_SCSI_OP_LOCK_UN_CACHE   = 0x36
EFI_SCSI_OP_PREFETCH        = 0x34
EFI_SCSI_OP_MEDIA_REMOVAL   = 0x1e
EFI_SCSI_OP_READ6           = 0x08
EFI_SCSI_OP_READ10          = 0x28
EFI_SCSI_OP_READ16          = 0x88
EFI_SCSI_OP_READ_CAPACITY   = 0x25
EFI_SCSI_OP_READ_CAPACITY16 = 0x9e
EFI_SCSI_OP_READ_DEFECT     = 0x37
EFI_SCSI_OP_READ_LONG       = 0x3e
EFI_SCSI_OP_REASSIGN_BLK    = 0x07
EFI_SCSI_OP_RELEASE         = 0x17
EFI_SCSI_OP_REZERO          = 0x01
EFI_SCSI_OP_SEARCH_DATA_E   = 0x31
EFI_SCSI_OP_SEARCH_DATA_H   = 0x30
EFI_SCSI_OP_SEARCH_DATA_L   = 0x32
EFI_SCSI_OP_SEEK6           = 0x0b
EFI_SCSI_OP_SEEK10          = 0x2b
EFI_SCSI_OP_SEND_DIAG       = 0x1d
EFI_SCSI_OP_SET_LIMIT       = 0x33
EFI_SCSI_OP_START_STOP_UNIT = 0x1b
EFI_SCSI_OP_SYNC_CACHE      = 0x35
EFI_SCSI_OP_VERIFY          = 0x2f
EFI_SCSI_OP_WRITE6          = 0x0a
EFI_SCSI_OP_WRITE10         = 0x2a
EFI_SCSI_OP_WRITE16         = 0x8a
EFI_SCSI_OP_WRITE_VERIFY    = 0x2e
EFI_SCSI_OP_WRITE_LONG      = 0x3f
EFI_SCSI_OP_WRITE_SAME      = 0x41
EFI_SCSI_OP_UNMAP           = 0x42

EFI_SCSI_OP_ERASE             = 0x19
EFI_SCSI_OP_LOAD_UNLOAD       = 0x1b
EFI_SCSI_OP_LOCATE            = 0x2b
EFI_SCSI_OP_READ_BLOCK_LIMIT  = 0x05
EFI_SCSI_OP_READ_POS          = 0x34
EFI_SCSI_OP_READ_REVERSE      = 0x0f
EFI_SCSI_OP_RECOVER_BUF_DATA  = 0x14
EFI_SCSI_OP_RESERVE_UNIT      = 0x16
EFI_SCSI_OP_REWIND            = 0x01
EFI_SCSI_OP_SPACE             = 0x11
EFI_SCSI_OP_VERIFY_TAPE       = 0x13
EFI_SCSI_OP_WRITE_FILEMARK    = 0x10

EFI_SCSI_OP_PRINT       = 0x0a
EFI_SCSI_OP_SLEW_PRINT  = 0x0b
EFI_SCSI_OP_STOP_PRINT  = 0x1b
EFI_SCSI_OP_SYNC_BUFF   = 0x10

EFI_SCSI_OP_RECEIVE = 0x08
EFI_SCSI_OP_SEND    = 0x0a

EFI_SCSI_OP_MEDIUM_SCAN     = 0x38
EFI_SCSI_OP_SEARCH_DAT_E10  = 0x31
EFI_SCSI_OP_SEARCH_DAT_E12  = 0xb1
EFI_SCSI_OP_SEARCH_DAT_H10  = 0x30
EFI_SCSI_OP_SEARCH_DAT_H12  = 0xb0
EFI_SCSI_OP_SEARCH_DAT_L10  = 0x32
EFI_SCSI_OP_SEARCH_DAT_L12  = 0xb2
EFI_SCSI_OP_SET_LIMIT10     = 0x33
EFI_SCSI_OP_SET_LIMIT12     = 0xb3
EFI_SCSI_OP_VERIFY10        = 0x2f
EFI_SCSI_OP_VERIFY12        = 0xaf
EFI_SCSI_OP_WRITE12         = 0xaa
EFI_SCSI_OP_WRITE_VERIFY10  = 0x2e
EFI_SCSI_OP_WRITE_VERIFY12  = 0xae

EFI_SCSI_OP_PLAY_AUD_10       = 0x45
EFI_SCSI_OP_PLAY_AUD_12       = 0xa5
EFI_SCSI_OP_PLAY_AUD_MSF      = 0x47
EFI_SCSI_OP_PLAY_AUD_TKIN     = 0x48
EFI_SCSI_OP_PLAY_TK_REL10     = 0x49
EFI_SCSI_OP_PLAY_TK_REL12     = 0xa9
EFI_SCSI_OP_READ_CD_CAPACITY  = 0x25
EFI_SCSI_OP_READ_HEADER       = 0x44
EFI_SCSI_OP_READ_SUB_CHANNEL  = 0x42
EFI_SCSI_OP_READ_TOC          = 0x43

EFI_SCSI_OP_GET_DATABUFF_STAT = 0x34
EFI_SCSI_OP_GET_WINDOW        = 0x25
EFI_SCSI_OP_OBJECT_POS        = 0x31
EFI_SCSI_OP_SCAN              = 0x1b
EFI_SCSI_OP_SET_WINDOW        = 0x24

EFI_SCSI_OP_UPDATE_BLOCK  = 0x3d

EFI_SCSI_OP_EXCHANGE_MEDIUM   = 0xa6
EFI_SCSI_OP_INIT_ELEMENT_STAT = 0x07
EFI_SCSI_OP_POS_TO_ELEMENT    = 0x2b
EFI_SCSI_OP_REQUEST_VE_ADDR   = 0xb5
EFI_SCSI_OP_SEND_VOL_TAG      = 0xb6

EFI_SCSI_OP_GET_MESSAGE6    = 0x08
EFI_SCSI_OP_GET_MESSAGE10   = 0x28
EFI_SCSI_OP_GET_MESSAGE12   = 0xa8
EFI_SCSI_OP_SEND_MESSAGE6   = 0x0a
EFI_SCSI_OP_SEND_MESSAGE10  = 0x2a
EFI_SCSI_OP_SEND_MESSAGE12  = 0xaa

EFI_SCSI_OP_SECURITY_PROTOCOL_IN   = 0xa2
EFI_SCSI_OP_SECURITY_PROTOCOL_OUT  = 0xb5

EFI_SCSI_DATA_IN  = 0
EFI_SCSI_DATA_OUT = 1

EFI_SCSI_BLOCK_FUA  = BIT3
EFI_SCSI_BLOCK_DPO  = BIT4

EFI_SCSI_TYPE_DISK             = 0x00
EFI_SCSI_TYPE_TAPE             = 0x01
EFI_SCSI_TYPE_PRINTER          = 0x02
EFI_SCSI_TYPE_PROCESSOR        = 0x03
EFI_SCSI_TYPE_WORM             = 0x04
EFI_SCSI_TYPE_CDROM            = 0x05
EFI_SCSI_TYPE_SCANNER          = 0x06
EFI_SCSI_TYPE_OPTICAL          = 0x07
EFI_SCSI_TYPE_MEDIUMCHANGER    = 0x08
EFI_SCSI_TYPE_COMMUNICATION    = 0x09
EFI_SCSI_TYPE_ASCIT8_1         = 0x0A
EFI_SCSI_TYPE_ASCIT8_2         = 0x0B
EFI_SCSI_TYPE_RAID             = 0x0C
EFI_SCSI_TYPE_SES              = 0x0D
EFI_SCSI_TYPE_RBC              = 0x0E
EFI_SCSI_TYPE_OCRW             = 0x0F
EFI_SCSI_TYPE_BRIDGE           = 0x10
EFI_SCSI_TYPE_OSD              = 0x11
EFI_SCSI_TYPE_AUTOMATION       = 0x12
EFI_SCSI_TYPE_SECURITYMANAGER  = 0x13
EFI_SCSI_TYPE_RESERVED_LOW     = 0x14
EFI_SCSI_TYPE_RESERVED_HIGH    = 0x1D
EFI_SCSI_TYPE_WLUN             = 0x1E
EFI_SCSI_TYPE_UNKNOWN          = 0x1F

EFI_SCSI_PAGE_CODE_SUPPORTED_VPD    = 0x00
EFI_SCSI_PAGE_CODE_BLOCK_LIMITS_VPD = 0xB0

class EFI_SCSI_INQUIRY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Peripheral_Type",       UINT8, 5),
    ("Peripheral_Qualifier",  UINT8, 3),
    ("DeviceType_Modifier",   UINT8, 7),
    ("Rmb",                   UINT8, 1),
    ("Version",               UINT8),
    ("Response_Data_Format",  UINT8),
    ("Addnl_Length",          UINT8),
    ("Reserved_5_95",         UINT8 * (95 - 5 + 1) )
  ]

class EFI_SCSI_SUPPORTED_VPD_PAGES_VPD_PAGE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Peripheral_Type",       UINT8, 5),
    ("Peripheral_Qualifier",  UINT8, 3),
    ("PageCode",              UINT8),
    ("PageLength2",           UINT8),
    ("PageLength1",           UINT8),
    ("SupportedVpdPageList",  UINT8 * 0X100 )
  ]

class EFI_SCSI_BLOCK_LIMITS_VPD_PAGE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Peripheral_Type",                                UINT8, 5),
    ("Peripheral_Qualifier",                           UINT8, 3),
    ("PageCode",                                       UINT8),
    ("PageLength2",                                    UINT8),
    ("PageLength1",                                    UINT8),
    ("WriteSameNonZero",                               UINT8, 1),
    ("Reserved_4",                                     UINT8, 7),
    ("MaximumCompareAndWriteLength",                   UINT8),
    ("OptimalTransferLengthGranularity2",              UINT8),
    ("OptimalTransferLengthGranularity1",              UINT8),
    ("MaximumTransferLength4",                         UINT8),
    ("MaximumTransferLength3",                         UINT8),
    ("MaximumTransferLength2",                         UINT8),
    ("MaximumTransferLength1",                         UINT8),
    ("OptimalTransferLength4",                         UINT8),
    ("OptimalTransferLength3",                         UINT8),
    ("OptimalTransferLength2",                         UINT8),
    ("OptimalTransferLength1",                         UINT8),
    ("MaximumPrefetchXdreadXdwriteTransferLength4",    UINT8),
    ("MaximumPrefetchXdreadXdwriteTransferLength3",    UINT8),
    ("MaximumPrefetchXdreadXdwriteTransferLength2",    UINT8),
    ("MaximumPrefetchXdreadXdwriteTransferLength1",    UINT8),
    ("MaximumUnmapLbaCount4",                          UINT8),
    ("MaximumUnmapLbaCount3",                          UINT8),
    ("MaximumUnmapLbaCount2",                          UINT8),
    ("MaximumUnmapLbaCount1",                          UINT8),
    ("MaximumUnmapBlockDescriptorCount4",              UINT8),
    ("MaximumUnmapBlockDescriptorCount3",              UINT8),
    ("MaximumUnmapBlockDescriptorCount2",              UINT8),
    ("MaximumUnmapBlockDescriptorCount1",              UINT8),
    ("OptimalUnmapGranularity4",                       UINT8),
    ("OptimalUnmapGranularity3",                       UINT8),
    ("OptimalUnmapGranularity2",                       UINT8),
    ("OptimalUnmapGranularity1",                       UINT8),
    ("UnmapGranularityAlignment4",                     UINT8, 7),
    ("UnmapGranularityAlignmentValid",                 UINT8, 1),
    ("UnmapGranularityAlignment3",                     UINT8),
    ("UnmapGranularityAlignment2",                     UINT8),
    ("UnmapGranularityAlignment1",                     UINT8),
    ("MaximumWriteSameLength4",                        UINT8),
    ("MaximumWriteSameLength3",                        UINT8),
    ("MaximumWriteSameLength2",                        UINT8),
    ("MaximumWriteSameLength1",                        UINT8),
    ("MaximumAtomicTransferLength4",                   UINT8),
    ("MaximumAtomicTransferLength3",                   UINT8),
    ("MaximumAtomicTransferLength2",                   UINT8),
    ("MaximumAtomicTransferLength1",                   UINT8),
    ("AtomicAlignment4",                               UINT8),
    ("AtomicAlignment3",                               UINT8),
    ("AtomicAlignment2",                               UINT8),
    ("AtomicAlignment1",                               UINT8),
    ("AtomicTransferLengthGranularity4",               UINT8),
    ("AtomicTransferLengthGranularity3",               UINT8),
    ("AtomicTransferLengthGranularity2",               UINT8),
    ("AtomicTransferLengthGranularity1",               UINT8),
    ("MaximumAtomicTransferLengthWithAtomicBoundary4", UINT8),
    ("MaximumAtomicTransferLengthWithAtomicBoundary3", UINT8),
    ("MaximumAtomicTransferLengthWithAtomicBoundary2", UINT8),
    ("MaximumAtomicTransferLengthWithAtomicBoundary1", UINT8),
    ("MaximumAtomicBoundarySize4",                     UINT8),
    ("MaximumAtomicBoundarySize3",                     UINT8),
    ("MaximumAtomicBoundarySize2",                     UINT8),
    ("MaximumAtomicBoundarySize1",                     UINT8)
  ]

class EFI_SCSI_SENSE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Error_Code",                  UINT8, 7),
    ("Valid : 1",                   UINT8, 1),
    ("Segment_Number",              UINT8),
    ("Sense_Key",                   UINT8, 4),
    ("Reserved_21",                 UINT8, 1),
    ("Ili",                         UINT8, 1),
    ("Reserved_22",                 UINT8, 2),
    ("Information_3_6",             UINT8 * 4),
    ("Addnl_Sense_Length",          UINT8),
    ("Vendor_Specific_8_11",        UINT8 * 4),
    ("Addnl_Sense_Code",            UINT8),
    ("Addnl_Sense_Code_Qualifier",  UINT8),
    ("Field_Replaceable_Unit_Code", UINT8),
    ("Reserved_15_17",              UINT8 * 3)
  ]

class EFI_SCSI_DISK_CAPACITY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LastLba3",    UINT8),
    ("LastLba2",    UINT8),
    ("LastLba1",    UINT8),
    ("LastLba0",    UINT8),
    ("BlockSize3",  UINT8),
    ("BlockSize2",  UINT8),
    ("BlockSize1",  UINT8),
    ("BlockSize0",  UINT8)
  ]

class EFI_SCSI_DISK_CAPACITY_DATA16 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LastLba7",          UINT8),
    ("LastLba6",          UINT8),
    ("LastLba5",          UINT8),
    ("LastLba4",          UINT8),
    ("LastLba3",          UINT8),
    ("LastLba2",          UINT8),
    ("LastLba1",          UINT8),
    ("LastLba0",          UINT8),
    ("BlockSize3",        UINT8),
    ("BlockSize2",        UINT8),
    ("BlockSize1",        UINT8),
    ("BlockSize0",        UINT8),
    ("Protection",        UINT8),
    ("LogicPerPhysical",  UINT8),
    ("LowestAlignLogic2", UINT8),
    ("LowestAlignLogic1", UINT8),  
    ("Reserved",          UINT8 * 16)
  ]

class EFI_SCSI_DISK_UNMAP_PARAM_LIST_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataLen",         UINT16),
    ("BlkDespDataLen",  UINT16),
    ("Reserved",        UINT8 * 4)
  ]

class EFI_SCSI_DISK_UNMAP_BLOCK_DESP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Lba",         UINT64),
    ("BlockNum",    UINT32),
    ("Reserved",    UINT8 * 4)
  ]

EFI_SCSI_SK_NO_SENSE          = 0x0
EFI_SCSI_SK_RECOVERY_ERROR    = 0x1
EFI_SCSI_SK_NOT_READY         = 0x2
EFI_SCSI_SK_MEDIUM_ERROR      = 0x3
EFI_SCSI_SK_HARDWARE_ERROR    = 0x4
EFI_SCSI_SK_ILLEGAL_REQUEST   = 0x5
EFI_SCSI_SK_UNIT_ATTENTION    = 0x6
EFI_SCSI_SK_DATA_PROTECT      = 0x7
EFI_SCSI_SK_BLANK_CHECK       = 0x8
EFI_SCSI_SK_VENDOR_SPECIFIC   = 0x9
EFI_SCSI_SK_RESERVED_A        = 0xA
EFI_SCSI_SK_ABORT             = 0xB
EFI_SCSI_SK_RESERVED_C        = 0xC
EFI_SCSI_SK_OVERFLOW          = 0xD
EFI_SCSI_SK_MISCOMPARE        = 0xE
EFI_SCSI_SK_RESERVED_F        = 0xF

EFI_SCSI_ASC_NOT_READY                    = 0x04
EFI_SCSI_ASCQ_IN_PROGRESS                 = 0x01

EFI_SCSI_ASC_MEDIA_ERR1                   = 0x10
EFI_SCSI_ASC_MEDIA_ERR2                   = 0x11
EFI_SCSI_ASC_MEDIA_ERR3                   = 0x14
EFI_SCSI_ASC_MEDIA_ERR4                   = 0x30
EFI_SCSI_ASC_MEDIA_UPSIDE_DOWN            = 0x06
EFI_SCSI_ASC_INVALID_CMD                  = 0x20
EFI_SCSI_ASC_LBA_OUT_OF_RANGE             = 0x21
EFI_SCSI_ASC_INVALID_FIELD                = 0x24
EFI_SCSI_ASC_WRITE_PROTECTED              = 0x27
EFI_SCSI_ASC_MEDIA_CHANGE                 = 0x28
EFI_SCSI_ASC_RESET                        = 0x29
EFI_SCSI_ASC_ILLEGAL_FIELD                = 0x26
EFI_SCSI_ASC_NO_MEDIA                     = 0x3A
EFI_SCSI_ASC_ILLEGAL_MODE_FOR_THIS_TRACK  = 0x64

