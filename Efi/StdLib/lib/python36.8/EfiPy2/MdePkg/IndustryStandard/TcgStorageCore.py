# TcgStorageCore.py
#
# EfiPy2.MdePkg.IndustryStandard.TcgStorageCore
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

TCG_UID = UINT64

def TCG_TO_UID(b0, b1, b2, b3, b4, b5, b6, b7):
  return (b0)       | \
         (b1) << 8  | \
         (b2) << 16 | \
         (b3) << 24 | \
         (b4) << 32 | \
         (b5) << 40 | \
         (b6) << 48 | \
         (b7) << 56

class TCG_COM_PACKET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReservedBE",        UINT32),
    ("ComIDBE",           UINT16),
    ("ComIDExtensionBE",  UINT16),
    ("OutstandingDataBE", UINT32),
    ("MinTransferBE",     UINT32),
    ("LengthBE",          UINT32),
    ("Payload",           UINT8 * 0)
  ]

class TCG_PACKET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TperSessionNumberBE",  UINT32),
    ("HostSessionNumberBE",  UINT32),
    ("SequenceNumberBE",     UINT32),
    ("ReservedBE",           UINT16),
    ("AckTypeBE",            UINT16),
    ("AcknowledgementBE",    UINT32),
    ("LengthBE",             UINT32),
    ("Payload",              UINT8 * 0)
  ]

class TCG_SUB_PACKET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReservedBE",     UINT8 * 6),
    ("KindBE",         UINT16),
    ("LengthBE",       UINT32),
    ("Payload",        UINT8 * 0)
  ]

SUBPACKET_KIND_DATA            = 0x0000
SUBPACKET_KIND_CREDIT_CONTROL  = 0x8001

TCG_ATOM_TYPE_INTEGER  = 0x0
TCG_ATOM_TYPE_BYTE     = 0x1

class TCG_TINY_ATOM_BITS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    UINT8, 6),
    ("Sign",    UINT8, 1),
    ("IsZero",  UINT8, 1)
  ]

class TCG_SIMPLE_TOKEN_TINY_ATOM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Raw",             UINT8),
    ("TinyAtomBits",    TCG_TINY_ATOM_BITS)
  ]

class TCG_SHORT_ATOM_BITS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",      UINT8, 4),
    ("SignOrCont",  UINT8, 1),
    ("ByteOrInt",   UINT8, 1),
    ("IsZero",      UINT8, 1),
    ("IsOne",       UINT8, 1)
  ]

class TCG_SIMPLE_TOKEN_SHORT_ATOM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("RawHeader",       UINT8),
    ("ShortAtomBits",   TCG_SHORT_ATOM_BITS)
  ]

TCG_MEDIUM_ATOM_LENGTH_HIGH_SHIFT  = 0x8
TCG_MEDIUM_ATOM_LENGTH_HIGH_MASK   = 0x7

class TCG_MEDIUM_ATOM_BITS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LengthHigh",  UINT8, 3),
    ("SignOrCont",  UINT8, 1),
    ("ByteOrInt",   UINT8, 1),
    ("IsZero",      UINT8, 1),
    ("IsOne1",      UINT8, 1),
    ("IsOne2",      UINT8, 1),
    ("LengthLow",   UINT8)
  ]

class TCG_SIMPLE_TOKEN_MEDIUM_ATOM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("RawHeader",       UINT16),
    ("MediumAtomBits",  TCG_MEDIUM_ATOM_BITS)
  ]

TCG_LONG_ATOM_LENGTH_HIGH_SHIFT  = 16
TCG_LONG_ATOM_LENGTH_MID_SHIFT   = 8

class TCG_LONG_ATOM_BITS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignOrCont",  UINT8, 1),
    ("ByteOrInt",   UINT8, 1),
    ("Reserved",    UINT8, 2),
    ("IsZero",      UINT8, 1),
    ("IsOne1",      UINT8, 1),
    ("IsOne2",      UINT8, 1),
    ("IsOne3",      UINT8, 1),
    ("LengthHigh",  UINT8),
    ("LengthMid",   UINT8),
    ("LengthLow",   UINT8)
  ]

class TCG_SIMPLE_TOKEN_LONG_ATOM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("RawHeader",       UINT32),
    ("LongAtomBits",    TCG_LONG_ATOM_BITS)
  ]

TcgTokenTypeReserved            = 0
TcgTokenTypeTinyAtom            = 1
TcgTokenTypeShortAtom           = 2
TcgTokenTypeMediumAtom          = 3
TcgTokenTypeLongAtom            = 4
TcgTokenTypeStartList           = 5
TcgTokenTypeEndList             = 6
TcgTokenTypeStartName           = 7
TcgTokenTypeEndName             = 8
TcgTokenTypeCall                = 9
TcgTokenTypeEndOfData           = 10
TcgTokenTypeEndOfSession        = 11
TcgTokenTypeStartTransaction    = 12
TcgTokenTypeEndTransaction      = 13
TcgTokenTypeEmptyAtom           = 14
TCG_TOKEN_TYPE  = ENUM

TCG_TOKEN_SHORTATOM_MAX_BYTE_SIZE   = 0x0F
TCG_TOKEN_MEDIUMATOM_MAX_BYTE_SIZE  = 0x7FF
TCG_TOKEN_LONGATOM_MAX_BYTE_SIZE    = 0xFFFFFF

TCG_TOKEN_TINYATOM_UNSIGNED_MAX_VALUE  = 0x3F
TCG_TOKEN_TINYATOM_SIGNED_MAX_VALUE    = 0x1F
TCG_TOKEN_TINYATOM_SIGNED_MIN_VALUE    = -32

TCG_TOKEN_TINYATOM          = 0x00
TCG_TOKEN_TINYSIGNEDATOM    = 0x40
TCG_TOKEN_SHORTATOM         = 0x80
TCG_TOKEN_SHORTSIGNEDATOM   = 0x90
TCG_TOKEN_SHORTBYTESATOM    = 0xA0
TCG_TOKEN_MEDIUMATOM        = 0xC0
TCG_TOKEN_MEDIUMSIGNEDATOM  = 0xC8
TCG_TOKEN_MEDIUMBYTESATOM   = 0xD0
TCG_TOKEN_LONGATOM          = 0xE0
TCG_TOKEN_LONGSIGNEDATOM    = 0xE1
TCG_TOKEN_LONGBYTESATOM     = 0xE2
TCG_TOKEN_STARTLIST         = 0xF0
TCG_TOKEN_ENDLIST           = 0xF1
TCG_TOKEN_STARTNAME         = 0xF2
TCG_TOKEN_ENDNAME           = 0xF3
# 0xF4 - 0xF7 TCG Reserved
TCG_TOKEN_CALL              = 0xF8
TCG_TOKEN_ENDDATA           = 0xF9
TCG_TOKEN_ENDSESSION        = 0xFA
TCG_TOKEN_STARTTRANSACTION  = 0xFB
TCG_TOKEN_ENDTRANSACTION    = 0xFC
# 0xFD - 0xFE TCG Reserved
TCG_TOKEN_EMPTY  = 0xFF

TCG_CELL_BLOCK_TABLE_NAME         = 0x00
TCG_CELL_BLOCK_START_ROW_NAME     = 0x01
TCG_CELL_BLOCK_END_ROW_NAME       = 0x02
TCG_CELL_BLOCK_START_COLUMN_NAME  = 0x03
TCG_CELL_BLOCK_END_COLUMN_NAME    = 0x04

TCG_METHOD_STATUS_CODE_SUCCESS                = 0x00
TCG_METHOD_STATUS_CODE_NOT_AUTHORIZED         = 0x01
TCG_METHOD_STATUS_CODE_OBSOLETE               = 0x02
TCG_METHOD_STATUS_CODE_SP_BUSY                = 0x03
TCG_METHOD_STATUS_CODE_SP_FAILED              = 0x04
TCG_METHOD_STATUS_CODE_SP_DISABLED            = 0x05
TCG_METHOD_STATUS_CODE_SP_FROZEN              = 0x06
TCG_METHOD_STATUS_CODE_NO_SESSIONS_AVAILABLE  = 0x07
TCG_METHOD_STATUS_CODE_UNIQUENESS_CONFLICT    = 0x08
TCG_METHOD_STATUS_CODE_INSUFFICIENT_SPACE     = 0x09
TCG_METHOD_STATUS_CODE_INSUFFICIENT_ROWS      = 0x0A
TCG_METHOD_STATUS_CODE_INVALID_PARAMETER      = 0x0C
TCG_METHOD_STATUS_CODE_OBSOLETE2              = 0x0D
TCG_METHOD_STATUS_CODE_OBSOLETE3              = 0x0E
TCG_METHOD_STATUS_CODE_TPER_MALFUNCTION       = 0x0F
TCG_METHOD_STATUS_CODE_TRANSACTION_FAILURE    = 0x10
TCG_METHOD_STATUS_CODE_RESPONSE_OVERFLOW      = 0x11
TCG_METHOD_STATUS_CODE_AUTHORITY_LOCKED_OUT   = 0x12
TCG_METHOD_STATUS_CODE_FAIL                   = 0x3F

TCG_FEATURE_INVALID             = 0x0000
TCG_FEATURE_TPER                = 0x0001
TCG_FEATURE_LOCKING             = 0x0002
TCG_FEATURE_GEOMETRY_REPORTING  = 0x0003
TCG_FEATURE_SINGLE_USER_MODE    = 0x0201
TCG_FEATURE_DATASTORE_TABLE     = 0x0202
TCG_FEATURE_OPAL_SSC_V1_0_0     = 0x0200
TCG_FEATURE_OPAL_SSC_V2_0_0     = 0x0203
TCG_FEATURE_OPAL_SSC_LITE       = 0x0301
TCG_FEATURE_PYRITE_SSC          = 0x0302
TCG_FEATURE_PYRITE_SSC_V2_0_0   = 0x0303
TCG_FEATURE_BLOCK_SID           = 0x0402
TCG_FEATURE_DATA_REMOVAL        = 0x0404

TCG_ACE_EXPRESSION_AND  = 0x0
TCG_ACE_EXPRESSION_OR   = 0x1

TCG_SECURITY_PROTOCOL_INFO                    = 0x00
TCG_OPAL_SECURITY_PROTOCOL_1                  = 0x01
TCG_OPAL_SECURITY_PROTOCOL_2                  = 0x02
TCG_SECURITY_PROTOCOL_TCG3                    = 0x03
TCG_SECURITY_PROTOCOL_TCG4                    = 0x04
TCG_SECURITY_PROTOCOL_TCG5                    = 0x05
TCG_SECURITY_PROTOCOL_TCG6                    = 0x06
TCG_SECURITY_PROTOCOL_CBCS                    = 0x07
TCG_SECURITY_PROTOCOL_TAPE_DATA               = 0x20
TCG_SECURITY_PROTOCOL_DATA_ENCRYPT_CONFIG     = 0x21
TCG_SECURITY_PROTOCOL_SA_CREATION_CAPS        = 0x40
TCG_SECURITY_PROTOCOL_IKEV2_SCSI              = 0x41
TCG_SECURITY_PROTOCOL_JEDEC_UFS               = 0xEC
TCG_SECURITY_PROTOCOL_SDCARD_SECURITY         = 0xED
TCG_SECURITY_PROTOCOL_IEEE_1667               = 0xEE
TCG_SECURITY_PROTOCOL_ATA_DEVICE_SERVER_PASS  = 0xEF

TCG_SP_SPECIFIC_PROTOCOL_LIST              = 0x0000
TCG_SP_SPECIFIC_PROTOCOL_LEVEL0_DISCOVERY  = 0x0001

TCG_RESERVED_COMID  = 0x0000

TCG_BLOCKSID_COMID  = 0x0005

class TCG_SUPPORTED_SECURITY_PROTOCOLS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT8 * 6),
    ("ListLength_BE",   UINT16),
    ("List",            UINT8 * 504)
  ]

class TCG_LEVEL0_DISCOVERY_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LengthBE",        UINT32),
    ("VerMajorBE",      UINT16),
    ("VerMinorBE",      UINT16),
    ("Reserved",        UINT8 * 8),
    ("VendorUnique",    UINT8 * 32)
  ]

class TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FeatureCode_BE",  UINT16),
    ("Reserved",        UINT8, 4),
    ("Version",         UINT8, 4),
    ("Length",          UINT8)
  ]

class TCG_LOCKING_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",           TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("LockingSupported", UINT8, 1),
    ("LockingEnabled",   UINT8, 1),
    ("Locked",           UINT8, 1),
    ("MediaEncryption",  UINT8, 1),
    ("MbrEnabled",       UINT8, 1),
    ("MbrDone",          UINT8, 1),
    ("Reserved",         UINT8, 2),
    ("Reserved515",      UINT8 * 11)
  ]

class TCG_BLOCK_SID_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("SIDValueState",   UINT8, 1),
    ("SIDBlockedState", UINT8, 1),
    ("Reserved4",       UINT8, 6),
    ("HardwareReset",   UINT8, 1),
    ("Reserved5",       UINT8, 7),
    ("Reserved615",     UINT8 * 10),
  ]

class TCG_TPER_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("SyncSupported",       UINT8, 1),
    ("AsyncSupported",      UINT8, 1),
    ("AckNakSupported",     UINT8, 1),
    ("BufferMgmtSupported", UINT8, 1),
    ("StreamingSupported",  UINT8, 1),
    ("Reserved4b5",         UINT8, 1),
    ("ComIdMgmtSupported",  UINT8, 1),
    ("Reserved4b7",         UINT8, 1),
    ("Reserved515",         UINT8 * 11),
  ]

TCG_UID_NULL     = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
TCG_UID_THIS_SP  = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01)
TCG_UID_SMUID    = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF)

TCG_UID_SM_PROPERTIES             = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x01)
TCG_UID_SM_START_SESSION          = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x02)
TCG_UID_SM_SYNC_SESSION           = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x03)
TCG_UID_SM_START_TRUSTED_SESSION  = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x04)
TCG_UID_SM_SYNC_TRUSTED_SESSION   = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x05)
TCG_UID_SM_CLOSE_SESSION          = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x06)

TCG_UID_METHOD_DELETE_SP          = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x01)
TCG_UID_METHOD_CREATE_TABLE       = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x02)
TCG_UID_METHOD_DELETE             = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x03)
TCG_UID_METHOD_CREATE_ROW         = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x04)
TCG_UID_METHOD_DELETE_ROW         = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x05)
TCG_UID_METHOD_NEXT               = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x08)
TCG_UID_METHOD_GET_FREE_SPACE     = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x09)
TCG_UID_METHOD_GET_FREE_ROWS      = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x0A)
TCG_UID_METHOD_DELETE_METHOD      = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x0B)
TCG_UID_METHOD_GET_ACL            = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x0D)
TCG_UID_METHOD_ADD_ACE            = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x0E)
TCG_UID_METHOD_REMOVE_ACE         = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x0F)
TCG_UID_METHOD_GEN_KEY            = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x10)
TCG_UID_METHOD_GET_PACKAGE        = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x12)
TCG_UID_METHOD_SET_PACKAGE        = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x13)
TCG_UID_METHOD_GET                = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x16)
TCG_UID_METHOD_SET                = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x17)
TCG_UID_METHOD_AUTHENTICATE       = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x1C)
TCG_UID_METHOD_ISSUE_SP           = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x01)
TCG_UID_METHOD_GET_CLOCK          = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x04, 0x01)
TCG_UID_METHOD_RESET_CLOCK        = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x04, 0x02)
TCG_UID_METHOD_SET_CLOCK_HIGH     = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x04, 0x03)
TCG_UID_METHOD_SET_LAG_HIGH       = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x04, 0x04)
TCG_UID_METHOD_SET_CLOCK_LOW      = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x04, 0x05)
TCG_UID_METHOD_SET_LAG_LOW        = TCG_TO_UID(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x06)
TCG_UID_METHOD_INCREMENT_COUNTER  = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x04, 0x07)
TCG_UID_METHOD_RANDOM             = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x01)
TCG_UID_METHOD_SALT               = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x02)
TCG_UID_METHOD_DECRYPT_INIT       = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x03)
TCG_UID_METHOD_DECRYPT            = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x04)
TCG_UID_METHOD_DECRYPT_FINALIZE   = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x05)
TCG_UID_METHOD_ENCRYPT_INIT       = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x06)
TCG_UID_METHOD_ENCRYPT            = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x07)
TCG_UID_METHOD_ENCRYPT_FINALIZE   = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x08)
TCG_UID_METHOD_HMAC_INIT          = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x09)
TCG_UID_METHOD_HMAC               = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x0A)
TCG_UID_METHOD_HMAC_FINALIZE      = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x0B)
TCG_UID_METHOD_HASH_INIT          = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x0C)
TCG_UID_METHOD_HASH               = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x0D)
TCG_UID_METHOD_HASH_FINALIZE      = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x0E)
TCG_UID_METHOD_SIGN               = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x0F)
TCG_UID_METHOD_VERIFY             = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x10)
TCG_UID_METHOD_XOR                = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x06, 0x11)
TCG_UID_METHOD_ADD_LOG            = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x0A, 0x01)
TCG_UID_METHOD_CREATE_LOG         = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x0A, 0x02)
TCG_UID_METHOD_CLEAR_LOG          = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x0A, 0x03)
TCG_UID_METHOD_FLUSH_LOG          = TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x0A, 0x04)

