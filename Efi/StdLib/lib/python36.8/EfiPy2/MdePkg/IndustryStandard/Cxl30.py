# Cxl30.py
#
# EfiPy2.MdePkg.IndustryStandard.Cxl30
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import Cxl20, Acpi, EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION

CXL_CACHE_MEM_CAPABILITY_ID_TIMEOUT_AND_ISOLATION  = 0x0009
CXL_CACHE_MEM_CAPABILITY_ID_EXTENDED               = 0x000A
CXL_CACHE_MEM_CAPABILITY_ID_BI_ROUTE_TABLE         = 0x000B
CXL_CACHE_MEM_CAPABILITY_ID_BI_DECODER             = 0x000C
CXL_CACHE_MEM_CAPABILITY_ID_CACHE_ID_ROUTE_TABLE   = 0x000D
CXL_CACHE_MEM_CAPABILITY_ID_CACHE_ID_DECODER       = 0x000E
CXL_CACHE_MEM_CAPABILITY_ID_EXTENDED_HDM_DECODER   = 0x000F

CXL_HDM_DECODER_VERSION_30  = 0x3

CXL_HDM_16_WAY_INTERLEAVING  = 0x4
CXL_HDM_3_WAY_INTERLEAVING   = 0x8
CXL_HDM_6_WAY_INTERLEAVING   = 0x9
CXL_HDM_12_WAY_INTERLEAVING  = 0xA

CEDT_TYPE_CFMWS  = 0x1
CEDT_TYPE_CXIMS  = 0x2
CEDT_TYPE_RDPAS  = 0x3

class CXL_CM_EXTENTED_REGISTER_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedRangesBitmap",  UINT32, 16),
    ("Reserved",              UINT32, 16)
  ]
class CXL_CM_EXTENTED_REGISTER_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CM_EXTENTED_REGISTER_CAPABILITY_Bits),
    ("Uint32",    UINT32)
  ]

CXL_CM_EXTENTED_RANGES_BITMAP  = (BIT2 | BIT3 | BIT4 | BIT5 | BIT6 | BIT7 | BIT8 | BIT9 | BIT10 | BIT11 | BIT12 | BIT13 | BIT15)

class CXL_BI_RT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExplicitBiRtCommitRequired",  UINT32, 1),
    ("Reserved",                    UINT32, 31)
  ]
class CXL_BI_RT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_BI_RT_CAPABILITY_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_BI_RT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BiRtCommit",    UINT32, 1),
    ("Reserved",      UINT32, 31)
  ]
class CXL_BI_RT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_BI_RT_CONTROL_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_BI_RT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("BiRtCommitted",           UINT32, 1),
  ("BiRtErrorNotCommitted",   UINT32, 1),
  ("Reserved1",               UINT32, 6),
  ("BiRtCommitTimeoutScale",  UINT32, 4),
  ("BiRtCommitTimeoutBase",   UINT32, 4),
  ("Reserved2",               UINT32, 16)
  ]
class CXL_BI_RT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_BI_RT_STATUS_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_BI_ROUTE_TABLE_CAPABILITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("BiRtCap",         CXL_BI_RT_CAPABILITY),
  ("BiRtControl",     CXL_BI_RT_CONTROL   ),
  ("BiRtStatus",      CXL_BI_RT_STATUS    )
  ]

class CXL_BI_DECODER_CAP_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("HdmDCapable",                     UINT32, 1),
  ("ExplicitBiDecoderCommitRequired", UINT32, 1),
  ("Reserved",                        UINT32, 30)
  ]
class CXL_BI_DECODER_CAP (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_BI_DECODER_CAP_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_BI_DECODER_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("BiForward",             UINT32, 1),
  ("BiEnable",              UINT32, 1),
  ("BiDecoderCommit",       UINT32, 1),
  ("Reserved",              UINT32, 29),
  ]
class CXL_BI_DECODER_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_BI_DECODER_CONTROL_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_BI_DECODER_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("BiDecoderCommitted",          UINT32, 1),
  ("BiDecoderErrorNotCommitted",  UINT32, 1),
  ("Reserved1",                   UINT32, 6),
  ("BiDecoderCommitTimeoutScale", UINT32, 4),
  ("BiDecoderCommitTimeoutBase",  UINT32, 4),
  ("Reserved2",                   UINT32, 16)
  ]
class CXL_BI_DECODER_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_BI_DECODER_STATUS_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_BI_DECODER_CAPABILITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("BiDecoderCap",        CXL_BI_DECODER_CAP),
  ("BiDecoderControl",    CXL_BI_DECODER_CONTROL),
  ("BiDecoderStatus",     CXL_BI_DECODER_STATUS)
  ]

class CXL_CACHE_ID_RT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CacheIdTargetCount",                UINT32, 5),
  ("Reserved1",                         UINT32, 3),
  ("HdmDType2DeviceMaxCount",           UINT32, 4),
  ("Reserved2",                         UINT32, 4),
  ("ExplicitCacheIdRtCommitRequired",   UINT32, 1),
  ("Reserved3",                         UINT32, 15)
  ]
class CXL_CACHE_ID_RT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_RT_CAPABILITY_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_RT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CacheIdRtCommit",     UINT32, 1),
  ("Reserved",            UINT32, 31)
  ]
class CXL_CACHE_ID_RT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_RT_CONTROL_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_RT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CacheIdRtCommitted",            UINT32, 1),
  ("CacheIdRtErrNotCommitted",      UINT32, 1),
  ("Reserved1",                     UINT32, 6),
  ("CacheIdRtCommitTimeoutScale",   UINT32, 4),
  ("CacheIdRtCommitTimeoutBase",    UINT32, 4),
  ("Reserved2",                     UINT32, 16)
  ]
class CXL_CACHE_ID_RT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_RT_STATUS_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_RT_TARGET_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Valid",             UINT16, 1),
  ("Reserved",          UINT16, 7),
  ("PortNumber",        UINT16, 8)
  ]
class CXL_CACHE_ID_RT_TARGET (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_RT_TARGET_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_ROUTE_TABLE_CAPABILITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CacheIdRtCap",        CXL_CACHE_ID_RT_CAPABILITY),
  ("CacheIdRtControl",    CXL_CACHE_ID_RT_CONTROL   ),
  ("CacheIdRtStatus",     CXL_CACHE_ID_RT_STATUS    ),
  ("Reserved",            UINT32                    ),
  # ("CacheIdRtTarget",     CXL_CACHE_ID_RT_TARGET * N)
  ]

class CXL_CACHE_ID_DECODER_CAP_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("ExplicitCacheIdDecoderCommitRequired ",   UINT32, 1),
  ("Reserved",                                UINT32, 31)
  ]
class CXL_CACHE_ID_DECODER_CAP (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_DECODER_CAP_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_DECODER_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("ForwardCacheId",          UINT32, 1),
  ("AssignCacheId",           UINT32, 1),
  ("HdmDType2DevicePresent",  UINT32, 1),
  ("CacheIdDecoderCommit",    UINT32, 1),
  ("Reserved1",               UINT32, 4),
  ("HdmDType2DeviceCacheId",  UINT32, 4),
  ("Reserved2",               UINT32, 4),
  ("LocalCacheId",            UINT32, 4),
  ("Reserved3",               UINT32, 4),
  ("TrustLevel",              UINT32, 2),
  ("Reserved4",               UINT32, 6)
  ]
class CXL_CACHE_ID_DECODER_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_DECODER_CONTROL_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_DECODER_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CacheIdDecoderCommitted",           UINT32, 1),
  ("CacheIdDecoderErrorNotCommitted",   UINT32, 1),
  ("Reserved1",                         UINT32, 6),
  ("CacheIdDecoderCommitTimeoutScale",  UINT32, 4),
  ("CacheIdDecoderCommitTimeoutBase",   UINT32, 4),
  ("Reserved2",                         UINT32, 16)
  ]
class CXL_CACHE_ID_DECODER_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_CACHE_ID_DECODER_STATUS_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_CACHE_ID_DECODER_CAPABILITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CacheIdDecoderCap",       CXL_CACHE_ID_DECODER_CAP),
  ("CacheIdDecoderControl",   CXL_CACHE_ID_DECODER_CONTROL),
  ("CacheIdDecoderStatus",    CXL_CACHE_ID_DECODER_STATUS)
  ]

class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CxlmemTransactionTimeoutRangesSupported",     UINT32, 4),
  ("CxlmemTransactionTimeoutSupported",           UINT32, 1),
  ("Reserved1",                                   UINT32, 3),
  ("CxlcacheTransactionTimeoutRangesSupported",   UINT32, 4),
  ("CxlcacheTransactionTimeoutSupported",         UINT32, 1),
  ("Reserved2",                                   UINT32, 3),
  ("CxlmemIsolationSupported",                    UINT32, 1),
  ("CxlmemIsolationLinkdownSupported",            UINT32, 1),
  ("CxlcacheIsolationSupported",                  UINT32, 1),
  ("CxlcacheIsolationLinkdownSupported",          UINT32, 1),
  ("Reserved3",                                   UINT32, 5),
  ("IsolationErrCorSignalingSupported",           UINT32, 1),
  ("IsolationInterruptSupported",                 UINT32, 1),
  ("IsolationInterruptMessageNumber",             UINT32, 5)
  ]
class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CAPABILITY_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CxlmemTransactionTimeoutValue",       UINT32, 4),
  ("CxlmemTransactionTimeoutEnable",      UINT32, 1),
  ("Reserved1",                           UINT32, 3),
  ("CxlcacheTransactionTimeoutValue",     UINT32, 4),
  ("CxlcacheTransactionTimeoutEnable",    UINT32, 1),
  ("Reserved2",                           UINT32, 3),
  ("CxlmemIsolationEnable",               UINT32, 1),
  ("CxlmemIsolationLinkdownEnable",       UINT32, 1),
  ("CxlcacheIsolationEnable",             UINT32, 1),
  ("CxlcacheIsolationLinkdownEnable",     UINT32, 1),
  ("Reserved3",                           UINT32, 5),
  ("IsolationErrCorSignalingEnable",      UINT32, 1),
  ("IsolationInterruptEnable",            UINT32, 1),
  ("Reserved4",                           UINT32, 5)
  ]
class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CONTROL_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CxlmemTransactionTimeout",        UINT32, 1),
  ("Reserved1",                       UINT32, 3),
  ("CxlcacheTransactionTimeout",      UINT32, 1),
  ("Reserved2",                       UINT32, 3),
  ("CxlmemIsolationStatus",           UINT32, 1),
  ("CxlmemIsolationLinkdownStatus",   UINT32, 1),
  ("Reserved3",                       UINT32, 2),
  ("CxlcacheIsolationStatus",         UINT32, 1),
  ("CxlcacheIsolationLinkdownStatus", UINT32, 1),
  ("CxlRpBusy",                       UINT32, 1),
  ("Reserved4",                       UINT32, 17)
  ]
class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_STATUS_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("TimeoutAndIsolationCap",      CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CAPABILITY ),
  ("Reserved",                    UINT32                                       ),
  ("TimeoutAndIsolationControl",  CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_CONTROL    ),
  ("TimeoutAndIsolationStatus",   CXL_3_0_CXL_TIMEOUT_AND_ISOLATION_STATUS     )
  ]

class CXL_FIXED_MEMORY_WINDOW_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Header",                    Cxl20.CEDT_STRUCTURE),
  ("Reserved",                  UINT32),
  ("BaseHpa",                   UINT64),
  ("WindowSize",                UINT64),
  ("EncodedInterleaveWays",     UINT8),
  ("InterleaveArithmetic",      UINT8),
  ("Reserved1",                 UINT16),
  ("Granularity",               UINT32),
  ("Restrictions",              UINT16),
  ("QtgId",                     UINT16),
  ("TargetList",                UINT32 * 16)
  ]

class CXL_XOR_INTERLEAVE_MATH_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Header",            Cxl20.CEDT_STRUCTURE),
  ("Reserved",          UINT16),
  ("HBIG",              UINT8),
  ("NIB",               UINT8),
  ("XORMAPList",        UINT64 * 4)
  ]

class RCEC_DOWNSTREAM_PORT_ASSOCIATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Header",                Cxl20.CEDT_STRUCTURE),
  ("SegmentNumber",         UINT16),
  ("Bdf",                   UINT16),
  ("BaseAddress",           UINT64),
  ("ProtocolType",          UINT8)
  ]

