# TcgStorageOpal.py
#
# EfiPy2.MdePkg.IndustryStandard.TcgStorageOpal
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import TcgStorageCore

OPAL_UID_ADMIN_SP             = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x01)
OPAL_UID_ADMIN_SP_C_PIN_MSID  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x84, 0x02)
OPAL_UID_ADMIN_SP_C_PIN_SID   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x01)
OPAL_UID_LOCKING_SP           = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x02)

OPAL_ADMIN_SP_ANYBODY_AUTHORITY  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x01)
OPAL_ADMIN_SP_ADMINS_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x02)
OPAL_ADMIN_SP_MAKERS_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x03)
OPAL_ADMIN_SP_SID_AUTHORITY      = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x06)
OPAL_ADMIN_SP_ADMIN1_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x02, 0x01)
OPAL_ADMIN_SP_PSID_AUTHORITY     = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x01, 0xFF, 0x01)

OPAL_ADMIN_SP_ACTIVATE_METHOD  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x03)
OPAL_ADMIN_SP_REVERT_METHOD    = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x02)

OPAL_UID_ADMIN_SP_DATA_REMOVAL_MECHANISM  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x11, 0x01, 0x00, 0x00, 0x00, 0x01)

OPAL_LOCKING_SP_ANYBODY_AUTHORITY  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x01)
OPAL_LOCKING_SP_ADMINS_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x02)
OPAL_LOCKING_SP_ADMIN1_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x01, 0x00, 0x01)
OPAL_LOCKING_SP_USERS_AUTHORITY    = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x00)
OPAL_LOCKING_SP_USER1_AUTHORITY    = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x01)

OPAL_LOCKING_SP_REVERTSP_METHOD  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x11)

OPAL_LOCKING_SP_C_PIN_ADMIN1  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x01 )
OPAL_LOCKING_SP_C_PIN_USER1   = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x0B, 0x00, 0x03, 0x00, 0x01 )

OPAL_LOCKING_SP_LOCKING_GLOBALRANGE  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x02, 0x00, 0x00, 0x00, 0x01 )
OPAL_LOCKING_SP_LOCKING_RANGE1       = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x02, 0x00, 0x03, 0x00, 0x01 )

OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_GET_ALL       = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xD0, 0x00 )
OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_SET_RDLOCKED  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xE0, 0x00 )
OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_SET_WRLOCKED  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xE8, 0x00 )

OPAL_LOCKING_SP_ACE_K_AES_256_GLOBALRANGE_GENKEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xB8, 0x00 )
OPAL_LOCKING_SP_ACE_K_AES_128_GLOBALRANGE_GENKEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xB0, 0x00 )

OPAL_LOCKING_SP_LOCKING_INFO  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0x01 )

OPAL_LOCKING_SP_LOCKINGINFO_ALIGNMENTREQUIRED_COL     = 0x7
OPAL_LOCKING_SP_LOCKINGINFO_LOGICALBLOCKSIZE_COL      = 0x8
OPAL_LOCKING_SP_LOCKINGINFO_ALIGNMENTGRANULARITY_COL  = 0x9
OPAL_LOCKING_SP_LOCKINGINFO_LOWESTALIGNEDLBA_COL      = 0xA

OPAL_LOCKING_SP_K_AES_256_GLOBALRANGE_KEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x06, 0x00, 0x00, 0x00, 0x01 )

OPAL_LOCKING_SP_K_AES_128_GLOBALRANGE_KEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x05, 0x00, 0x00, 0x00, 0x01 )

OPAL_MIN_MAX_COM_PACKET_SIZE          = 2048
OPAL_MIN_MAX_REPONSE_COM_PACKET_SIZE  = 2048
OPAL_MIN_MAX_PACKET_SIZE              = 2028
OPAL_MIN_MAX_IND_TOKEN_SIZE           = 1992
OPAL_MIN_MAX_PACKETS                  = 1
OPAL_MIN_MAX_SUBPACKETS               = 1
OPAL_MIN_MAX_METHODS                  = 1
OPAL_MIN_MAX_SESSIONS                 = 1
OPAL_MIN_MAX_AUTHENTICATIONS          = 2
OPAL_MIN_MAX_TRANSACTION_LIMIT        = 1

OPAL_ADMIN_SP_PIN_COL               = 3
OPAL_LOCKING_SP_C_PIN_TRYLIMIT_COL  = 5
OPAL_RANDOM_METHOD_MAX_COUNT_SIZE   = 32

OPAL_ADMIN_SP_ACTIVE_DATA_REMOVAL_MECHANISM_COL  = 1

OverwriteDataErase  = 0
BlockErase          = 1
CryptoErase         = 2
Unmap               = 3
ResetWritePointers  = 4
VendorSpecificErase = 5
ResearvedMechanism  = 6
SUPPORTED_DATA_REMOVAL_MECHANISM = ENUM

class OPAL_GEOMETRY_REPORTING_FEATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Reserved",                UINT8 * 8),
    ("LogicalBlockSizeBE",      UINT32),
    ("AlignmentGranularityBE",  UINT64),
    ("LowestAlignedLBABE",      UINT64)
  ]

class OPAL_SINGLE_USER_MODE_FEATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("NumLockingObjectsSupportedBE",  UINT32),
    ("Any",         UINT8, 1),
    ("All",         UINT8, 1),
    ("Policy",      UINT8, 1),
    ("Reserved",    UINT8, 5),
    ("Reserved2",   UINT8 * 7)
  ]

class OPAL_DATASTORE_TABLE_FEATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Reserved",        UINT16),
    ("MaxNumTablesBE",  UINT16),
    ("MaxTotalSizeBE",  UINT32),
    ("SizeAlignmentBE", UINT32)
  ]

class OPAL_SSCV1_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",    UINT16),
    ("NumComIdsBE",     UINT16),
    ("RangeCrossing",   UINT8, 1),
    ("Reserved",        UINT8, 7),
    ("Future",          UINT8 * 11),
  ]

class OPAL_SSCV2_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8),
    ("NumLockingSpAdminAuthoritiesSupportedBE", UINT16),
    ("NumLockingSpUserAuthoritiesSupportedBE",  UINT16),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

class OPAL_SSCLITE_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8 * 5),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

class PYRITE_SSC_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8 * 5),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

class PYRITE_SSCV2_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8 * 5),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

class DATA_REMOVAL_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Reserved",            UINT8),
    ("OperationProcessing", UINT8, 1),
    ("Reserved2",           UINT8, 7),
    ("RemovalMechanism",    UINT8),
    ("FormatBit0",          UINT8, 1),
    ("FormatBit1",          UINT8, 1),
    ("FormatBit2",          UINT8, 1),
    ("FormatBit3",          UINT8, 1),
    ("FormatBit4",          UINT8, 1),
    ("FormatBit5",          UINT8, 1),
    ("Reserved3",           UINT8, 2),
    ("TimeBit0",            UINT16),
    ("TimeBit1",            UINT16),
    ("TimeBit2",            UINT16),
    ("TimeBit3",            UINT16),
    ("TimeBit4",            UINT16),
    ("TimeBit5",            UINT16),
    ("Future",              UINT8 * 16)
  ]

class OPAL_LEVEL0_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("CommonHeader",    TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Tper",            TcgStorageCore.TCG_TPER_FEATURE_DESCRIPTOR),
    ("Locking",         TcgStorageCore.TCG_LOCKING_FEATURE_DESCRIPTOR),
    ("Geometry",        OPAL_GEOMETRY_REPORTING_FEATURE),
    ("SingleUser",      OPAL_SINGLE_USER_MODE_FEATURE),
    ("DataStore",       OPAL_DATASTORE_TABLE_FEATURE),
    ("OpalSscV1",       OPAL_SSCV1_FEATURE_DESCRIPTOR),
    ("OpalSscV2",       OPAL_SSCV2_FEATURE_DESCRIPTOR),
    ("OpalSscLite",     OPAL_SSCLITE_FEATURE_DESCRIPTOR),
    ("PyriteSsc",       PYRITE_SSC_FEATURE_DESCRIPTOR),
    ("PyriteSscV2",     PYRITE_SSCV2_FEATURE_DESCRIPTOR),
    ("BlockSid",        TcgStorageCore.TCG_BLOCK_SID_FEATURE_DESCRIPTOR),
    ("DataRemoval",     DATA_REMOVAL_FEATURE_DESCRIPTOR)
  ]

