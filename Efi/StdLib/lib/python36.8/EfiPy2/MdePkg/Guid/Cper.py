# Cper.py
#
# EfiPy2.MdePkg.Guid.Cper
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

EFI_ERROR_RECORD_SIGNATURE_START   = SIGNATURE_32('C', 'P', 'E', 'R')
EFI_ERROR_RECORD_SIGNATURE_END     = 0xFFFFFFFF

EFI_GENERIC_ERROR_RECOVERABLE                = 0x00000000
EFI_GENERIC_ERROR_FATAL                      = 0x00000001
EFI_GENERIC_ERROR_CORRECTED                  = 0x00000002
EFI_GENERIC_ERROR_INFO                       = 0x00000003

EFI_ERROR_RECORD_HEADER_PLATFORM_ID_VALID    = BIT0
EFI_ERROR_RECORD_HEADER_TIME_STAMP_VALID     = BIT1
EFI_ERROR_RECORD_HEADER_PARTITION_ID_VALID   = BIT2

EFI_ERROR_TIME_STAMP_PRECISE                 = BIT0

class EFI_ERROR_TIME_STAMP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Seconds", UINT8),
    ("Minutes", UINT8),
    ("Hours",   UINT8),
    ("Flag",    UINT8),
    ("Day",     UINT8),
    ("Month",   UINT8),
    ("Year",    UINT8),
    ("Century", UINT8)
  ]

gEfiEventNotificationTypeCmcGuid    = \
  EFI_GUID (0x2DCE8BB1, 0xBDD7, 0x450e, ( 0xB9, 0xAD, 0x9C, 0xF4, 0xEB, 0xD4, 0xF8, 0x90 ))

gEfiEventNotificationTypeCpeGuid    = \
  EFI_GUID (0x4E292F96, 0xD843, 0x4a55, ( 0xA8, 0xC2, 0xD4, 0x81, 0xF2, 0x7E, 0xBE, 0xEE ))

gEfiEventNotificationTypeMceGuid    = \
  EFI_GUID (0xE8F56FFE, 0x919C, 0x4cc5, ( 0xBA, 0x88, 0x65, 0xAB, 0xE1, 0x49, 0x13, 0xBB ))

gEfiEventNotificationTypePcieGuid   = \
  EFI_GUID (0xCF93C01F, 0x1A16, 0x4dfc, ( 0xB8, 0xBC, 0x9C, 0x4D, 0xAF, 0x67, 0xC1, 0x04 ))

gEfiEventNotificationTypeInitGuid   = \
  EFI_GUID (0xCC5263E8, 0x9308, 0x454a, ( 0x89, 0xD0, 0x34, 0x0B, 0xD3, 0x9B, 0xC9, 0x8E ))

gEfiEventNotificationTypeNmiGuid    = \
  EFI_GUID (0x5BAD89FF, 0xB7E6, 0x42c9, ( 0x81, 0x4A, 0xCF, 0x24, 0x85, 0xD6, 0xE9, 0x8A ))

gEfiEventNotificationTypeBootGuid   = \
  EFI_GUID (0x3D61A466, 0xAB40, 0x409a, ( 0xA6, 0x98, 0xF3, 0x62, 0xD4, 0x64, 0xB3, 0x8F ))

gEfiEventNotificationTypeDmarGuid   = \
  EFI_GUID (0x667DD791, 0xC6B3, 0x4c27, ( 0x8A, 0x6B, 0x0F, 0x8E, 0x72, 0x2D, 0xEB, 0x41 ))

gEfiEventNotificationTypeSeaGuid    = \
  EFI_GUID (0x9A78788A, 0xBBE8, 0x11E4, ( 0x80, 0x9E, 0x67, 0x61, 0x1E, 0x5D, 0x46, 0xB0 ))

gEfiEventNotificationTypeSeiGuid    = \
  EFI_GUID (0x5C284C81, 0xB0AE, 0x4E87, ( 0xA3, 0x22, 0xB0, 0x4C, 0x85, 0x62, 0x43, 0x23 ))

gEfiEventNotificationTypePeiGuid    = \
  EFI_GUID (0x09A9D5AC, 0x5204, 0x4214, ( 0x96, 0xE5, 0x94, 0x99, 0x2E, 0x75, 0x2B, 0xCD ))

EFI_HW_ERROR_FLAGS_RECOVERED                 = 0x00000001
EFI_HW_ERROR_FLAGS_PREVERR                   = 0x00000002
EFI_HW_ERROR_FLAGS_SIMULATED                 = 0x00000004

class EFI_COMMON_ERROR_RECORD_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("SignatureStart",    UINT32),
    ("Revision",          UINT16),
    ("SignatureEnd",      UINT32),
    ("SectionCount",      UINT16),
    ("ErrorSeverity",     UINT32),
    ("ValidationBits",    UINT32),
    ("RecordLength",      UINT32),
    ("TimeStamp",         EFI_ERROR_TIME_STAMP),
    ("PlatformID",        EFI_GUID),
    ("PartitionID",       EFI_GUID),
    ("CreatorID",         EFI_GUID),
    ("NotificationType",  EFI_GUID),
    ("RecordID",          UINT64),
    ("Flags",             UINT32),
    ("PersistenceInfo",   UINT64),
    ("Resv1",             UINT8 * 12)
  ]

EFI_ERROR_SECTION_REVISION  = 0x0100

EFI_ERROR_SECTION_FRU_ID_VALID               = BIT0
EFI_ERROR_SECTION_FRU_STRING_VALID           = BIT1

EFI_ERROR_SECTION_FLAGS_PRIMARY                        = BIT0
EFI_ERROR_SECTION_FLAGS_CONTAINMENT_WARNING            = BIT1
EFI_ERROR_SECTION_FLAGS_RESET                          = BIT2
EFI_ERROR_SECTION_FLAGS_ERROR_THRESHOLD_EXCEEDED       = BIT3
EFI_ERROR_SECTION_FLAGS_RESOURCE_NOT_ACCESSIBLE        = BIT4
EFI_ERROR_SECTION_FLAGS_LATENT_ERROR                   = BIT5

gEfiProcessorGenericErrorSectionGuid    = \
  EFI_GUID (0x9876ccad, 0x47b4, 0x4bdb, ( 0xb6, 0x5e, 0x16, 0xf1, 0x93, 0xc4, 0xf3, 0xdb ))

gEfiProcessorSpecificErrorSectionGuid   = \
  EFI_GUID (0xdc3ea0b0, 0xa144, 0x4797, ( 0xb9, 0x5b, 0x53, 0xfa, 0x24, 0x2b, 0x6e, 0x1d ))

gEfiIa32X64ProcessorErrorSectionGuid    = \
  EFI_GUID (0xdc3ea0b0, 0xa144, 0x4797, ( 0xb9, 0x5b, 0x53, 0xfa, 0x24, 0x2b, 0x6e, 0x1d ))

gEfiArmProcessorErrorSectionGuid        = \
  EFI_GUID (0xe19e3d16, 0xbc11, 0x11e4, ( 0x9c, 0xaa, 0xc2, 0x05, 0x1d, 0x5d, 0x46, 0xb0 ))

gEfiPlatformMemoryErrorSectionGuid      = \
  EFI_GUID (0xa5bc1114, 0x6f64, 0x4ede, ( 0xb8, 0x63, 0x3e, 0x83, 0xed, 0x7c, 0x83, 0xb1 ))

gEfiPlatformMemory2ErrorSectionGuid     = \
  EFI_GUID (0x61EC04FC, 0x48E6, 0xD813, ( 0x25, 0xC9, 0x8D, 0xAA, 0x44, 0x75, 0x0B, 0x12 ))

gEfiPcieErrorSectionGuid                = \
  EFI_GUID (0xd995e954, 0xbbc1, 0x430f, ( 0xad, 0x91, 0xb4, 0x4d, 0xcb, 0x3c, 0x6f, 0x35 ))

gEfiFirmwareErrorSectionGuid            = \
  EFI_GUID (0x81212a96, 0x09ed, 0x4996, ( 0x94, 0x71, 0x8d, 0x72, 0x9c, 0x8e, 0x69, 0xed ))

gEfiPciBusErrorSectionGuid              = \
  EFI_GUID (0xc5753963, 0x3b84, 0x4095, ( 0xbf, 0x78, 0xed, 0xda, 0xd3, 0xf9, 0xc9, 0xdd ))

gEfiPciDevErrorSectionGuid              = \
  EFI_GUID (0xeb5e4685, 0xca66, 0x4769, ( 0xb6, 0xa2, 0x26, 0x06, 0x8b, 0x00, 0x13, 0x26 ))

gEfiDMArGenericErrorSectionGuid         = \
  EFI_GUID (0x5b51fef7, 0xc79d, 0x4434, ( 0x8f, 0x1b, 0xaa, 0x62, 0xde, 0x3e, 0x2c, 0x64 ))

gEfiDirectedIoDMArErrorSectionGuid      = \
  EFI_GUID (0x71761d37, 0x32b2, 0x45cd, ( 0xa7, 0xd0, 0xb0, 0xfe, 0xdd, 0x93, 0xe8, 0xcf ))

gEfiIommuDMArErrorSectionGuid           = \
  EFI_GUID (0x036f84e1, 0x7f37, 0x428c, ( 0xa7, 0x9e, 0x57, 0x5f, 0xdf, 0xaa, 0x84, 0xec ))

class EFI_ERROR_SECTION_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("SectionOffset", UINT32),
    ("SectionLength", UINT32),
    ("Revision",      UINT16),
    ("SecValidMask",  UINT8),
    ("Resv1",         UINT8),
    ("SectionFlags",  UINT32),
    ("SectionType",   EFI_GUID),
    ("FruId",         EFI_GUID),
    ("Severity",      UINT32),
    ("FruString",     CHAR8 * 20)
  ]

EFI_GENERIC_ERROR_PROC_TYPE_VALID            = BIT0
EFI_GENERIC_ERROR_PROC_ISA_VALID             = BIT1
EFI_GENERIC_ERROR_PROC_ERROR_TYPE_VALID      = BIT2
EFI_GENERIC_ERROR_PROC_OPERATION_VALID       = BIT3
EFI_GENERIC_ERROR_PROC_FLAGS_VALID           = BIT4
EFI_GENERIC_ERROR_PROC_LEVEL_VALID           = BIT5
EFI_GENERIC_ERROR_PROC_VERSION_VALID         = BIT6
EFI_GENERIC_ERROR_PROC_BRAND_VALID           = BIT7
EFI_GENERIC_ERROR_PROC_ID_VALID              = BIT8
EFI_GENERIC_ERROR_PROC_TARGET_ADDR_VALID     = BIT9
EFI_GENERIC_ERROR_PROC_REQUESTER_ID_VALID    = BIT10
EFI_GENERIC_ERROR_PROC_RESPONDER_ID_VALID    = BIT11
EFI_GENERIC_ERROR_PROC_INST_IP_VALID         = BIT12

EFI_GENERIC_ERROR_PROC_TYPE_IA32_X64  = 0x00
EFI_GENERIC_ERROR_PROC_TYPE_IA64      = 0x01
EFI_GENERIC_ERROR_PROC_TYPE_ARM       = 0x02

EFI_GENERIC_ERROR_PROC_ISA_IA32         = 0x00
EFI_GENERIC_ERROR_PROC_ISA_IA64         = 0x01
EFI_GENERIC_ERROR_PROC_ISA_X64          = 0x02
EFI_GENERIC_ERROR_PROC_ISA_ARM_A32_T32  = 0x03
EFI_GENERIC_ERROR_PROC_ISA_ARM_A64      = 0x04

EFI_GENERIC_ERROR_PROC_ERROR_TYPE_UNKNOWN    = 0x00
EFI_GENERIC_ERROR_PROC_ERROR_TYPE_CACHE      = 0x01
EFI_GENERIC_ERROR_PROC_ERROR_TYPE_TLB        = 0x02
EFI_GENERIC_ERROR_PROC_ERROR_TYPE_BUS        = 0x04
EFI_GENERIC_ERROR_PROC_ERROR_TYPE_MICRO_ARCH = 0x08

EFI_GENERIC_ERROR_PROC_OPERATION_GENERIC               = 0x00
EFI_GENERIC_ERROR_PROC_OPERATION_DATA_READ             = 0x01
EFI_GENERIC_ERROR_PROC_OPERATION_DATA_WRITE            = 0x02
EFI_GENERIC_ERROR_PROC_OPERATION_INSTRUCTION_EXEC      = 0x03

EFI_GENERIC_ERROR_PROC_FLAGS_RESTARTABLE     = BIT0
EFI_GENERIC_ERROR_PROC_FLAGS_PRECISE_IP      = BIT1
EFI_GENERIC_ERROR_PROC_FLAGS_OVERFLOW        = BIT2
EFI_GENERIC_ERROR_PROC_FLAGS_CORRECTED       = BIT3

class EFI_PROCESSOR_GENERIC_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ValidFields",   UINT64),
    ("Type",          UINT8),
    ("Isa",           UINT8),
    ("ErrorType",     UINT8),
    ("Operation",     UINT8),
    ("Flags",         UINT8),
    ("Level",         UINT8),
    ("Resv1",         UINT16),
    ("VersionInfo",   UINT64),
    ("BrandString",   CHAR8 * 128),
    ("ApicId",        UINT64),
    ("TargetAddr",    UINT64),
    ("RequestorId",   UINT64),
    ("ResponderId",   UINT64),
    ("InstructionIP", UINT64)
  ]

if EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_IA32 or EFIPY_MDE_CPU_TYPE == EFIPY_MDE_CPU_X64:

  gEfiIa32X64ErrorTypeCacheCheckGuid  = \
    EFI_GUID (0xA55701F5, 0xE3EF, 0x43de, (0xAC, 0x72, 0x24, 0x9B, 0x57, 0x3F, 0xAD, 0x2C ))

  gEfiIa32X64ErrorTypeTlbCheckGuid    = \
    EFI_GUID (0xFC06B535, 0x5E1F, 0x4562, (0x9F, 0x25, 0x0A, 0x3B, 0x9A, 0xDB, 0x63, 0xC3 ))

  gEfiIa32X64ErrorTypeBusCheckGuid    = \
    EFI_GUID (0x1CF3F8B3, 0xC5B1, 0x49a2, (0xAA, 0x59, 0x5E, 0xEF, 0x92, 0xFF, 0xA6, 0x3C ))

  gEfiIa32X64ErrorTypeMsCheckGuid     = \
    EFI_GUID (0x48AB7F57, 0xDC34, 0x4f6c, (0xA7, 0xD3, 0xB0, 0xB5, 0xB0, 0xA7, 0x43, 0x14 ))

  EFI_IA32_X64_PROCESSOR_ERROR_APIC_ID_VALID      = BIT0
  EFI_IA32_X64_PROCESSOR_ERROR_CPU_ID_INFO_VALID  = BIT1

  class EFI_IA32_X64_PROCESSOR_ERROR_RECORD (Structure):
    _pack_   = 1
    _fields_ = [
      ("ValidFields",   UINT64),
      ("ApicId",        UINT64),
      ("CpuIdInfo",     UINT8 * 48)
    ]

  EFI_CACHE_CHECK_TRANSACTION_TYPE_VALID       = BIT0
  EFI_CACHE_CHECK_OPERATION_VALID              = BIT1
  EFI_CACHE_CHECK_LEVEL_VALID                  = BIT2
  EFI_CACHE_CHECK_CONTEXT_CORRUPT_VALID        = BIT3
  EFI_CACHE_CHECK_UNCORRECTED_VALID            = BIT4
  EFI_CACHE_CHECK_PRECISE_IP_VALID             = BIT5
  EFI_CACHE_CHECK_RESTARTABLE_VALID            = BIT6
  EFI_CACHE_CHECK_OVERFLOW_VALID               = BIT7

  EFI_CACHE_CHECK_ERROR_TYPE_INSTRUCTION       = 0
  EFI_CACHE_CHECK_ERROR_TYPE_DATA_ACCESS       = 1
  EFI_CACHE_CHECK_ERROR_TYPE_GENERIC           = 2

  EFI_CACHE_CHECK_OPERATION_TYPE_GENERIC                 = 0
  EFI_CACHE_CHECK_OPERATION_TYPE_GENERIC_READ            = 1
  EFI_CACHE_CHECK_OPERATION_TYPE_GENERIC_WRITE           = 2
  EFI_CACHE_CHECK_OPERATION_TYPE_DATA_READ               = 3
  EFI_CACHE_CHECK_OPERATION_TYPE_DATA_WRITE              = 4
  EFI_CACHE_CHECK_OPERATION_TYPE_INSTRUCTION_FETCH       = 5
  EFI_CACHE_CHECK_OPERATION_TYPE_PREFETCH                = 6
  EFI_CACHE_CHECK_OPERATION_TYPE_EVICTION                = 7
  EFI_CACHE_CHECK_OPERATION_TYPE_SNOOP                   = 8

  class EFI_IA32_X64_CACHE_CHECK_INFO (Structure):
    _pack_   = 1
    _fields_ = [
      ("ValidFields",       UINT64, 16),
      ("TransactionType",   UINT64, 2),
      ("Operation",         UINT64, 4),
      ("Level",             UINT64, 3),
      ("ContextCorrupt",    UINT64, 1),
      ("ErrorUncorrected",  UINT64, 1),
      ("PreciseIp",         UINT64, 1),
      ("RestartableIp",     UINT64, 1),
      ("Overflow",          UINT64, 1),
      ("Resv1",             UINT64, 34)
    ]

  EFI_TLB_CHECK_TRANSACTION_TYPE_VALID         = BIT0
  EFI_TLB_CHECK_OPERATION_VALID                = BIT1
  EFI_TLB_CHECK_LEVEL_VALID                    = BIT2
  EFI_TLB_CHECK_CONTEXT_CORRUPT_VALID          = BIT3
  EFI_TLB_CHECK_UNCORRECTED_VALID              = BIT4
  EFI_TLB_CHECK_PRECISE_IP_VALID               = BIT5
  EFI_TLB_CHECK_RESTARTABLE_VALID              = BIT6
  EFI_TLB_CHECK_OVERFLOW_VALID                 = BIT7

  EFI_TLB_CHECK_ERROR_TYPE_INSTRUCTION         = 0
  EFI_TLB_CHECK_ERROR_TYPE_DATA_ACCESS         = 1
  EFI_TLB_CHECK_ERROR_TYPE_GENERIC             = 2

  EFI_TLB_CHECK_OPERATION_TYPE_GENERIC         = 0
  EFI_TLB_CHECK_OPERATION_TYPE_GENERIC_READ    = 1
  EFI_TLB_CHECK_OPERATION_TYPE_GENERIC_WRITE   = 2
  EFI_TLB_CHECK_OPERATION_TYPE_DATA_READ       = 3
  EFI_TLB_CHECK_OPERATION_TYPE_DATA_WRITE      = 4
  EFI_TLB_CHECK_OPERATION_TYPE_INST_FETCH      = 5
  EFI_TLB_CHECK_OPERATION_TYPE_PREFETCH        = 6

  class EFI_IA32_X64_TLB_CHECK_INFO (Structure):
    _pack_   = 1
    _fields_ = [
      ("ValidFields",       UINT64, 16),
      ("TransactionType",   UINT64, 2),
      ("Operation",         UINT64, 4),
      ("Level",             UINT64, 3),
      ("ContextCorrupt",    UINT64, 1),
      ("ErrorUncorrected",  UINT64, 1),
      ("PreciseIp",         UINT64, 1),
      ("RestartableIp",     UINT64, 1),
      ("Overflow",          UINT64, 1),
      ("Resv1",             UINT64, 34)
    ]

  EFI_BUS_CHECK_TRANSACTION_TYPE_VALID         = BIT0
  EFI_BUS_CHECK_OPERATION_VALID                = BIT1
  EFI_BUS_CHECK_LEVEL_VALID                    = BIT2
  EFI_BUS_CHECK_CONTEXT_CORRUPT_VALID          = BIT3
  EFI_BUS_CHECK_UNCORRECTED_VALID              = BIT4
  EFI_BUS_CHECK_PRECISE_IP_VALID               = BIT5
  EFI_BUS_CHECK_RESTARTABLE_VALID              = BIT6
  EFI_BUS_CHECK_OVERFLOW_VALID                 = BIT7
  EFI_BUS_CHECK_PARTICIPATION_TYPE_VALID       = BIT8
  EFI_BUS_CHECK_TIME_OUT_VALID                 = BIT9
  EFI_BUS_CHECK_ADDRESS_SPACE_VALID            = BIT10

  EFI_BUS_CHECK_ERROR_TYPE_INSTRUCTION         = 0
  EFI_BUS_CHECK_ERROR_TYPE_DATA_ACCESS         = 1
  EFI_BUS_CHECK_ERROR_TYPE_GENERIC             = 2

  EFI_BUS_CHECK_OPERATION_TYPE_GENERIC         = 0
  EFI_BUS_CHECK_OPERATION_TYPE_GENERIC_READ    = 1
  EFI_BUS_CHECK_OPERATION_TYPE_GENERIC_WRITE   = 2
  EFI_BUS_CHECK_OPERATION_TYPE_DATA_READ       = 3
  EFI_BUS_CHECK_OPERATION_TYPE_DATA_WRITE      = 4
  EFI_BUS_CHECK_OPERATION_TYPE_INST_FETCH      = 5
  EFI_BUS_CHECK_OPERATION_TYPE_PREFETCH        = 6

  EFI_BUS_CHECK_PARTICIPATION_TYPE_REQUEST     = 0
  EFI_BUS_CHECK_PARTICIPATION_TYPE_RESPONDED   = 1
  EFI_BUS_CHECK_PARTICIPATION_TYPE_OBSERVED    = 2
  EFI_BUS_CHECK_PARTICIPATION_TYPE_GENERIC     = 3

  EFI_BUS_CHECK_ADDRESS_SPACE_TYPE_MEMORY      = 0
  EFI_BUS_CHECK_ADDRESS_SPACE_TYPE_RESERVED    = 1
  EFI_BUS_CHECK_ADDRESS_SPACE_TYPE_IO          = 2
  EFI_BUS_CHECK_ADDRESS_SPACE_TYPE_OTHER       = 3

  class EFI_IA32_X64_BUS_CHECK_INFO (Structure):
    _pack_   = 1
    _fields_ = [
      ("ValidFields",       UINT64, 16),
      ("TransactionType",   UINT64, 2),
      ("Operation",         UINT64, 4),
      ("Level",             UINT64, 3),
      ("ContextCorrupt",    UINT64, 1),
      ("ErrorUncorrected",  UINT64, 1),
      ("PreciseIp",         UINT64, 1),
      ("RestartableIp",     UINT64, 1),
      ("Overflow",          UINT64, 1),
      ("ParticipationType", UINT64, 2),
      ("TimeOut",           UINT64, 1),
      ("AddressSpace",      UINT64, 2),
      ("Resv1",             UINT64, 29)
    ]

  EFI_MS_CHECK_ERROR_TYPE_VALID                = BIT0
  EFI_MS_CHECK_CONTEXT_CORRUPT_VALID           = BIT1
  EFI_MS_CHECK_UNCORRECTED_VALID               = BIT2
  EFI_MS_CHECK_PRECISE_IP_VALID                = BIT3
  EFI_MS_CHECK_RESTARTABLE_VALID               = BIT4
  EFI_MS_CHECK_OVERFLOW_VALID                  = BIT5

  EFI_MS_CHECK_ERROR_TYPE_NO                             = 0
  EFI_MS_CHECK_ERROR_TYPE_UNCLASSIFIED                   = 1
  EFI_MS_CHECK_ERROR_TYPE_MICROCODE_PARITY               = 2
  EFI_MS_CHECK_ERROR_TYPE_EXTERNAL                       = 3
  EFI_MS_CHECK_ERROR_TYPE_FRC                            = 4
  EFI_MS_CHECK_ERROR_TYPE_INTERNAL_UNCLASSIFIED          = 5

  class EFI_IA32_X64_MS_CHECK_INFO (Structure):
    _pack_   = 1
    _fields_ = [
      ("ValidFields",       UINT64, 16),
      ("ErrorType",         UINT64, 3),
      ("ContextCorrupt",    UINT64, 1),
      ("ErrorUncorrected",  UINT64, 1),
      ("PreciseIp",         UINT64, 1),
      ("RestartableIp",     UINT64, 1),
      ("Overflow",          UINT64, 1),
      ("Resv1",             UINT64, 40)
    ]

  class EFI_IA32_X64_CHECK_INFO_ITEM (Union):
    _pack_   = 1
    _fields_ = [
      ("CacheCheck",  EFI_IA32_X64_CACHE_CHECK_INFO),
      ("TlbCheck",    EFI_IA32_X64_TLB_CHECK_INFO),
      ("BusCheck",    EFI_IA32_X64_BUS_CHECK_INFO),
      ("MsCheck",     EFI_IA32_X64_MS_CHECK_INFO),
      ("Data64",      UINT64)
    ]

  EFI_IA32_X64_ERROR_PROC_CHECK_INFO_VALID       = BIT0
  EFI_IA32_X64_ERROR_PROC_TARGET_ADDR_VALID      = BIT1
  EFI_IA32_X64_ERROR_PROC_REQUESTER_ID_VALID     = BIT2
  EFI_IA32_X64_ERROR_PROC_RESPONDER_ID_VALID     = BIT3
  EFI_IA32_X64_ERROR_PROC_INST_IP_VALID          = BIT4

  class EFI_IA32_X64_PROCESS_ERROR_INFO (Structure):
    _pack_   = 1
    _fields_ = [
      ("ErrorType",     EFI_GUID),
      ("ValidFields",   UINT64),
      ("CheckInfo",     EFI_IA32_X64_CHECK_INFO_ITEM),
      ("TargetId",      UINT64),
      ("RequestorId",   UINT64),
      ("ResponderId",   UINT64),
      ("InstructionIP", UINT64)
    ]

  class EFI_IA32_X64_PROCESSOR_CONTEXT_INFO (Structure):
    _pack_   = 1
    _fields_ = [
      ("RegisterType",      UINT16),
      ("ArraySize",         UINT16),
      ("MsrAddress",        UINT32),
      ("MmRegisterAddress", UINT64)
    ]

  EFI_REG_CONTEXT_TYPE_UNCLASSIFIED            = 0x0000
  EFI_REG_CONTEXT_TYPE_MSR                     = 0x0001
  EFI_REG_CONTEXT_TYPE_IA32                    = 0x0002
  EFI_REG_CONTEXT_TYPE_X64                     = 0x0003
  EFI_REG_CONTEXT_TYPE_FXSAVE                  = 0x0004
  EFI_REG_CONTEXT_TYPE_DR_IA32                 = 0x0005
  EFI_REG_CONTEXT_TYPE_DR_X64                  = 0x0006
  EFI_REG_CONTEXT_TYPE_MEM_MAP                 = 0x0007

  class EFI_CONTEXT_IA32_REGISTER_STATE (Structure):
    _pack_   = 1
    _fields_ = [
      ("Eax",     UINT32),
      ("Ebx",     UINT32),
      ("Ecx",     UINT32),
      ("Edx",     UINT32),
      ("Esi",     UINT32),
      ("Edi",     UINT32),
      ("Ebp",     UINT32),
      ("Esp",     UINT32),
      ("Cs",      UINT16),
      ("Ds",      UINT16),
      ("Ss",      UINT16),
      ("Es",      UINT16),
      ("Fs",      UINT16),
      ("Gs",      UINT16),
      ("Eflags",  UINT32),
      ("Eip",     UINT32),
      ("Cr0",     UINT32),
      ("Cr1",     UINT32),
      ("Cr2",     UINT32),
      ("Cr3",     UINT32),
      ("Cr4",     UINT32),
      ("Gdtr",    UINT32 * 2),
      ("Idtr",    UINT32 * 2),
      ("Ldtr",    UINT16),
      ("Tr",      UINT16)
    ]

  class EFI_CONTEXT_X64_REGISTER_STATE (Structure):
    _pack_   = 1
    _fields_ = [
      ("Rax",     UINT64),
      ("Rbx",     UINT64),
      ("Rcx",     UINT64),
      ("Rdx",     UINT64),
      ("Rsi",     UINT64),
      ("Rdi",     UINT64),
      ("Rbp",     UINT64),
      ("Rsp",     UINT64),
      ("R8",      UINT64),
      ("R9",      UINT64),
      ("R10",     UINT64),
      ("R11",     UINT64),
      ("R12",     UINT64),
      ("R13",     UINT64),
      ("R14",     UINT64),
      ("R15",     UINT64),
      ("Cs",      UINT16),
      ("Ds",      UINT16),
      ("Ss",      UINT16),
      ("Es",      UINT16),
      ("Fs",      UINT16),
      ("Gs",      UINT16),
      ("Resv1",   UINT32),
      ("Rflags",  UINT64),
      ("Rip",     UINT64),
      ("Cr0",     UINT64),
      ("Cr1",     UINT64),
      ("Cr2",     UINT64),
      ("Cr3",     UINT64),
      ("Cr4",     UINT64),
      ("Gdtr",    UINT64 * 2),
      ("Idtr",    UINT64 * 2),
      ("Ldtr",    UINT16),
      ("Tr",      UINT16)
    ]

  class EFI_IA32_X64_VALID_BITS (Structure):
    _pack_   = 1
    _fields_ = [
      ("ApicIdValid",     UINT64, 1),
      ("CpuIdInforValid", UINT64, 1),
      ("ErrorInfoNum",    UINT64, 6),
      ("ContextNum",      UINT64, 6),
      ("Resv1",           UINT64, 50)
    ]

class EFI_GENERIC_ERROR_STATUS (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resv1",               UINT64, 8),
    ("Type",                UINT64, 8),
    ("AddressSignal",       UINT64, 1),
    ("ControlSignal",       UINT64, 1),
    ("DataSignal",          UINT64, 1),
    ("DetectedByResponder", UINT64, 1),
    ("DetectedByRequester", UINT64, 1),
    ("FirstError",          UINT64, 1),
    ("OverflowNotLogged",   UINT64, 1),
    ("Resv2",               UINT64, 41)
  ]

ErrorInternal       = 1
ErrorBus            = 16
ErrorMemStorage     = 4
ErrorTlbStorage     = 5
ErrorCacheStorage   = 6
ErrorFunctionalUnit = 7
ErrorSelftest       = 8
ErrorOverflow       = 9
ErrorVirtualMap     = 17
ErrorAccessInvalid  = 18
ErrorUnimplAccess   = 19
ErrorLossOfLockstep = 20
ErrorResponseInvalid= 21
ErrorParity         = 22
ErrorProtocol       = 23
ErrorPath           = 24
ErrorTimeout        = 25
ErrorPoisoned       = 26
EFI_GENERIC_ERROR_STATUS_ERROR_TYPE = ENUM

EFI_PLATFORM_MEMORY_ERROR_STATUS_VALID                 = BIT0
EFI_PLATFORM_MEMORY_PHY_ADDRESS_VALID                  = BIT1
EFI_PLATFORM_MEMORY_PHY_ADDRESS_MASK_VALID             = BIT2
EFI_PLATFORM_MEMORY_NODE_VALID                         = BIT3
EFI_PLATFORM_MEMORY_CARD_VALID                         = BIT4
EFI_PLATFORM_MEMORY_MODULE_VALID                       = BIT5
EFI_PLATFORM_MEMORY_BANK_VALID                         = BIT6
EFI_PLATFORM_MEMORY_DEVICE_VALID                       = BIT7
EFI_PLATFORM_MEMORY_ROW_VALID                          = BIT8
EFI_PLATFORM_MEMORY_COLUMN_VALID                       = BIT9
EFI_PLATFORM_MEMORY_BIT_POS_VALID                      = BIT10
EFI_PLATFORM_MEMORY_REQUESTOR_ID_VALID                 = BIT11
EFI_PLATFORM_MEMORY_RESPONDER_ID_VALID                 = BIT12
EFI_PLATFORM_MEMORY_TARGET_ID_VALID                    = BIT13
EFI_PLATFORM_MEMORY_ERROR_TYPE_VALID                   = BIT14
EFI_PLATFORM_MEMORY_ERROR_RANK_NUM_VALID               = BIT15
EFI_PLATFORM_MEMORY_ERROR_CARD_HANDLE_VALID            = BIT16
EFI_PLATFORM_MEMORY_ERROR_MODULE_HANDLE_VALID          = BIT17
EFI_PLATFORM_MEMORY_ERROR_EXTENDED_ROW_BIT_16_17_VALID = BIT18
EFI_PLATFORM_MEMORY_ERROR_BANK_GROUP_VALID             = BIT19
EFI_PLATFORM_MEMORY_ERROR_BANK_ADDRESS_VALID           = BIT20
EFI_PLATFORM_MEMORY_ERROR_CHIP_IDENTIFICATION_VALID    = BIT21

EFI_PLATFORM_MEMORY_ERROR_UNKNOWN                      = 0x00
EFI_PLATFORM_MEMORY_ERROR_NONE                         = 0x01
EFI_PLATFORM_MEMORY_ERROR_SINGLEBIT_ECC                = 0x02
EFI_PLATFORM_MEMORY_ERROR_MLTIBIT_ECC                  = 0x03
EFI_PLATFORM_MEMORY_ERROR_SINGLESYMBOLS_CHIPKILL       = 0x04
EFI_PLATFORM_MEMORY_ERROR_MULTISYMBOL_CHIPKILL         = 0x05
EFI_PLATFORM_MEMORY_ERROR_MATER_ABORT                  = 0x06
EFI_PLATFORM_MEMORY_ERROR_TARGET_ABORT                 = 0x07
EFI_PLATFORM_MEMORY_ERROR_PARITY                       = 0x08
EFI_PLATFORM_MEMORY_ERROR_WDT                          = 0x09
EFI_PLATFORM_MEMORY_ERROR_INVALID_ADDRESS              = 0x0A
EFI_PLATFORM_MEMORY_ERROR_MIRROR_FAILED                = 0x0B
EFI_PLATFORM_MEMORY_ERROR_SPARING                      = 0x0C
EFI_PLATFORM_MEMORY_ERROR_SCRUB_CORRECTED              = 0x0D
EFI_PLATFORM_MEMORY_ERROR_SCRUB_UNCORRECTED            = 0x0E
EFI_PLATFORM_MEMORY_ERROR_MEMORY_MAP_EVENT             = 0x0F

class EFI_PLATFORM_MEMORY_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ValidFields",         UINT64),
    ("ErrorStatus",         EFI_GENERIC_ERROR_STATUS),
    ("PhysicalAddress",     UINT64),
    ("PhysicalAddressMask", UINT64),
    ("Node",                UINT16),
    ("Card",                UINT16),
    ("ModuleRank",          UINT16),
    ("Bank",                UINT16),
    ("Device",              UINT16),
    ("Row",                 UINT16),
    ("Column",              UINT16),
    ("BitPosition",         UINT16),
    ("RequestorId",         UINT64),
    ("ResponderId",         UINT64),
    ("TargetId",            UINT64),
    ("ErrorType",           UINT8),
    ("Extended",            UINT8),
    ("RankNum",             UINT16),
    ("CardHandle",          UINT16),
    ("ModuleHandle",        UINT16)
  ]

EFI_PLATFORM_MEMORY2_ERROR_STATUS_VALID                 = BIT0
EFI_PLATFORM_MEMORY2_PHY_ADDRESS_VALID                  = BIT1
EFI_PLATFORM_MEMORY2_PHY_ADDRESS_MASK_VALID             = BIT2
EFI_PLATFORM_MEMORY2_NODE_VALID                         = BIT3
EFI_PLATFORM_MEMORY2_CARD_VALID                         = BIT4
EFI_PLATFORM_MEMORY2_MODULE_VALID                       = BIT5
EFI_PLATFORM_MEMORY2_BANK_VALID                         = BIT6
EFI_PLATFORM_MEMORY2_DEVICE_VALID                       = BIT7
EFI_PLATFORM_MEMORY2_ROW_VALID                          = BIT8
EFI_PLATFORM_MEMORY2_COLUMN_VALID                       = BIT9
EFI_PLATFORM_MEMORY2_RANK_VALID                         = BIT10
EFI_PLATFORM_MEMORY2_BIT_POS_VALID                      = BIT11
EFI_PLATFORM_MEMORY2_CHIP_ID_VALID                      = BIT12
EFI_PLATFORM_MEMORY2_MEMORY_ERROR_TYPE_VALID            = BIT13
EFI_PLATFORM_MEMORY2_STATUS_VALID                       = BIT14
EFI_PLATFORM_MEMORY2_REQUESTOR_ID_VALID                 = BIT15
EFI_PLATFORM_MEMORY2_RESPONDER_ID_VALID                 = BIT16
EFI_PLATFORM_MEMORY2_TARGET_ID_VALID                    = BIT17
EFI_PLATFORM_MEMORY2_CARD_HANDLE_VALID                  = BIT18
EFI_PLATFORM_MEMORY2_MODULE_HANDLE_VALID                = BIT19
EFI_PLATFORM_MEMORY2_BANK_GROUP_VALID                   = BIT20
EFI_PLATFORM_MEMORY2_BANK_ADDRESS_VALID                 = BIT21

EFI_PLATFORM_MEMORY2_ERROR_UNKNOWN                      = 0x00
EFI_PLATFORM_MEMORY2_ERROR_NONE                         = 0x01
EFI_PLATFORM_MEMORY2_ERROR_SINGLEBIT_ECC                = 0x02
EFI_PLATFORM_MEMORY2_ERROR_MLTIBIT_ECC                  = 0x03
EFI_PLATFORM_MEMORY2_ERROR_SINGLESYMBOL_CHIPKILL        = 0x04
EFI_PLATFORM_MEMORY2_ERROR_MULTISYMBOL_CHIPKILL         = 0x05
EFI_PLATFORM_MEMORY2_ERROR_MASTER_ABORT                 = 0x06
EFI_PLATFORM_MEMORY2_ERROR_TARGET_ABORT                 = 0x07
EFI_PLATFORM_MEMORY2_ERROR_PARITY                       = 0x08
EFI_PLATFORM_MEMORY2_ERROR_WDT                          = 0x09
EFI_PLATFORM_MEMORY2_ERROR_INVALID_ADDRESS              = 0x0A
EFI_PLATFORM_MEMORY2_ERROR_MIRROR_BROKEN                = 0x0B
EFI_PLATFORM_MEMORY2_ERROR_MEMORY_SPARING               = 0x0C
EFI_PLATFORM_MEMORY2_ERROR_SCRUB_CORRECTED              = 0x0D
EFI_PLATFORM_MEMORY2_ERROR_SCRUB_UNCORRECTED            = 0x0E
EFI_PLATFORM_MEMORY2_ERROR_MEMORY_MAP_EVENT             = 0x0F

class EFI_PLATFORM_MEMORY2_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ValidFields",         UINT64),
    ("ErrorStatus",         EFI_GENERIC_ERROR_STATUS),
    ("PhysicalAddress",     UINT64),
    ("PhysicalAddressMask", UINT64),
    ("Node",                UINT16),
    ("Card",                UINT16),
    ("Module",              UINT16),
    ("Bank",                UINT16),
    ("Device",              UINT32),
    ("Row",                 UINT32),
    ("Column",              UINT32),
    ("Rank",                UINT32),
    ("BitPosition",         UINT32),
    ("ChipId",              UINT8),
    ("MemErrorType",        UINT8),
    ("Status",              UINT8),
    ("Reserved",            UINT8),
    ("RequestorId",         UINT64),
    ("ResponderId",         UINT64),
    ("TargetId",            UINT64),
    ("CardHandle",          UINT32),
    ("ModuleHandle",        UINT32)
  ]

EFI_PCIE_ERROR_PORT_TYPE_VALID               = BIT0
EFI_PCIE_ERROR_VERSION_VALID                 = BIT1
EFI_PCIE_ERROR_COMMAND_STATUS_VALID          = BIT2
EFI_PCIE_ERROR_DEVICE_ID_VALID               = BIT3
EFI_PCIE_ERROR_SERIAL_NO_VALID               = BIT4
EFI_PCIE_ERROR_BRIDGE_CRL_STS_VALID          = BIT5
EFI_PCIE_ERROR_CAPABILITY_INFO_VALID         = BIT6
EFI_PCIE_ERROR_AER_INFO_VALID                = BIT7

EFI_PCIE_ERROR_PORT_PCIE_ENDPOINT            = 0x00000000
EFI_PCIE_ERROR_PORT_PCI_ENDPOINT             = 0x00000001
EFI_PCIE_ERROR_PORT_ROOT_PORT                = 0x00000004
EFI_PCIE_ERROR_PORT_UPSWITCH_PORT            = 0x00000005
EFI_PCIE_ERROR_PORT_DOWNSWITCH_PORT          = 0x00000006
EFI_PCIE_ERROR_PORT_PCIE_TO_PCI_BRIDGE       = 0x00000007
EFI_PCIE_ERROR_PORT_PCI_TO_PCIE_BRIDGE       = 0x00000008
EFI_PCIE_ERROR_PORT_ROOT_INT_ENDPOINT        = 0x00000009
EFI_PCIE_ERROR_PORT_ROOT_EVENT_COLLECTOR     = 0x0000000A

class EFI_GENERIC_ERROR_PCI_SLOT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Resv1",   UINT16, 3),
    ("Number",  UINT16, 13)
  ]

class EFI_GENERIC_ERROR_PCIE_DEV_BRIDGE_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("VendorId",            UINT16),
    ("DeviceId",            UINT16),
    ("ClassCode",           UINT8 * 3),
    ("Function",            UINT8),
    ("Device",              UINT8),
    ("Segment",             UINT16),
    ("PrimaryOrDeviceBus",  UINT8),
    ("SecondaryBus",        UINT8),
    ("Slot",                EFI_GENERIC_ERROR_PCI_SLOT),
    ("Resv1",               UINT8)
  ]

class EFI_PCIE_ERROR_DATA_CAPABILITY (Structure):
  _pack_   = 1
  _fields_ = [
    ("PcieCap", UINT8 * 60),
  ]

class EFI_PCIE_ERROR_DATA_AER (Structure):
  _pack_   = 1
  _fields_ = [
    ("PcieAer", UINT8 * 96),
  ]

class EFI_PCIE_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ValidFields",         UINT64),
    ("PortType",            UINT32),
    ("Version",             UINT32),
    ("CommandStatus",       UINT32),
    ("Resv2",               UINT32),
    ("DevBridge",           EFI_GENERIC_ERROR_PCIE_DEV_BRIDGE_ID),
    ("SerialNo",            UINT64),
    ("BridgeControlStatus", UINT32),
    ("Capability",          EFI_PCIE_ERROR_DATA_CAPABILITY),
    ("AerInfo",             EFI_PCIE_ERROR_DATA_AER)
  ]

EFI_PCI_PCIX_BUS_ERROR_STATUS_VALID          = BIT0
EFI_PCI_PCIX_BUS_ERROR_TYPE_VALID            = BIT1
EFI_PCI_PCIX_BUS_ERROR_BUS_ID_VALID          = BIT2
EFI_PCI_PCIX_BUS_ERROR_BUS_ADDRESS_VALID     = BIT3
EFI_PCI_PCIX_BUS_ERROR_BUS_DATA_VALID        = BIT4
EFI_PCI_PCIX_BUS_ERROR_COMMAND_VALID         = BIT5
EFI_PCI_PCIX_BUS_ERROR_REQUESTOR_ID_VALID    = BIT6
EFI_PCI_PCIX_BUS_ERROR_COMPLETER_ID_VALID    = BIT7
EFI_PCI_PCIX_BUS_ERROR_TARGET_ID_VALID       = BIT8

EFI_PCI_PCIX_BUS_ERROR_UNKNOWN               = 0x0000
EFI_PCI_PCIX_BUS_ERROR_DATA_PARITY           = 0x0001
EFI_PCI_PCIX_BUS_ERROR_SYSTEM                = 0x0002
EFI_PCI_PCIX_BUS_ERROR_MASTER_ABORT          = 0x0003
EFI_PCI_PCIX_BUS_ERROR_BUS_TIMEOUT           = 0x0004
EFI_PCI_PCIX_BUS_ERROR_MASTER_DATA_PARITY    = 0x0005
EFI_PCI_PCIX_BUS_ERROR_ADDRESS_PARITY        = 0x0006
EFI_PCI_PCIX_BUS_ERROR_COMMAND_PARITY        = 0x0007

class EFI_PCI_PCIX_BUS_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ValidFields", UINT64),
    ("ErrorStatus", EFI_GENERIC_ERROR_STATUS),
    ("Type",        UINT16),
    ("BusId",       UINT16),
    ("Resv2",       UINT32),
    ("BusAddress",  UINT64),
    ("BusData",     UINT64),
    ("BusCommand",  UINT64),
    ("RequestorId", UINT64),
    ("ResponderId", UINT64),
    ("TargetId",    UINT64)
  ]

EFI_PCI_PCIX_DEVICE_ERROR_STATUS_VALID                 = BIT0
EFI_PCI_PCIX_DEVICE_ERROR_ID_INFO_VALID                = BIT1
EFI_PCI_PCIX_DEVICE_ERROR_MEM_NUM_VALID                = BIT2
EFI_PCI_PCIX_DEVICE_ERROR_IO_NUM_VALID                 = BIT3
EFI_PCI_PCIX_DEVICE_ERROR_REG_DATA_PAIR_VALID          = BIT4

class EFI_GENERIC_ERROR_PCI_DEVICE_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("VendorId",  UINT16),
    ("DeviceId",  UINT16),
    ("ClassCode", UINT8 * 3),
    ("Function",  UINT8),
    ("Device",    UINT8),
    ("Bus",       UINT8),
    ("Segment",   UINT8),
    ("Resv1",     UINT8),
    ("Resv2",     UINT32)
  ]

EFI_FIRMWARE_ERROR_TYPE_IPF_SAL    = 0x00
EFI_FIRMWARE_ERROR_TYPE_SOC_TYPE1  = 0x01
EFI_FIRMWARE_ERROR_TYPE_SOC_TYPE2  = 0x02

class EFI_FIRMWARE_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("ErrorType",       UINT8),
    ("Revision",        UINT8),
    ("Resv1",           UINT8 * 6),
    ("RecordId",        UINT64),
    ("RecordIdGuid",    EFI_GUID)
  ]

EFI_DMA_FAULT_REASON_TABLE_ENTRY_NOT_PRESENT           = 0x01
EFI_DMA_FAULT_REASON_TABLE_ENTRY_INVALID               = 0x02
EFI_DMA_FAULT_REASON_ACCESS_MAPPING_TABLE_ERROR        = 0x03
EFI_DMA_FAULT_REASON_RESV_BIT_ERROR_IN_MAPPING_TABLE   = 0x04
EFI_DMA_FAULT_REASON_ACCESS_ADDR_OUT_OF_SPACE          = 0x05
EFI_DMA_FAULT_REASON_INVALID_ACCESS                    = 0x06
EFI_DMA_FAULT_REASON_INVALID_REQUEST                   = 0x07
EFI_DMA_FAULT_REASON_ACCESS_TRANSLATE_TABLE_ERROR      = 0x08
EFI_DMA_FAULT_REASON_RESV_BIT_ERROR_IN_TRANSLATE_TABLE = 0x09
EFI_DMA_FAULT_REASON_INVALID_COMMAOND                  = 0x0A
EFI_DMA_FAULT_REASON_ACCESS_COMMAND_BUFFER_ERROR       = 0x0B

EFI_DMA_ACCESS_TYPE_READ                     = 0x00
EFI_DMA_ACCESS_TYPE_WRITE                    = 0x01

EFI_DMA_ADDRESS_UNTRANSLATED                 = 0x00
EFI_DMA_ADDRESS_TRANSLATION                  = 0x01

EFI_DMA_ARCH_TYPE_VT                         = 0x01
EFI_DMA_ARCH_TYPE_IOMMU                      = 0x02

class EFI_DMAR_GENERIC_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("RequesterId",   UINT16),
    ("SegmentNumber", UINT16),
    ("FaultReason",   UINT8),
    ("AccessType",    UINT8),
    ("AddressType",   UINT8),
    ("ArchType",      UINT8),
    ("DeviceAddr",    UINT64),
    ("Resv1",         UINT8 * 16)
  ]

class EFI_DIRECTED_IO_DMAR_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",       UINT8),
    ("Revision",      UINT8),
    ("OemId",         UINT8 * 6),
    ("Capability",    UINT64),
    ("CapabilityEx",  UINT64),
    ("GlobalCommand", UINT32),
    ("GlobalStatus",  UINT32),
    ("FaultStatus",   UINT32),
    ("Resv1",         UINT8 * 12),
    ("FaultRecord",   UINT64 * 2),
    ("RootEntry",     UINT64 * 2),
    ("ContextEntry",  UINT64 * 2),
    ("PteL6",         UINT64),
    ("PteL5",         UINT64),
    ("PteL4",         UINT64),
    ("PteL3",         UINT64),
    ("PteL2",         UINT64),
    ("PteL1",         UINT64)
  ]

class EFI_IOMMU_DMAR_ERROR_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Revision",          UINT8),
    ("Resv1",             UINT8 * 7),
    ("Control",           UINT64),
    ("Status",            UINT64),
    ("Resv2",             UINT8 * 8),
    ("EventLogEntry",     UINT64 * 2),
    ("Resv3",             UINT8 * 16),
    ("DeviceTableEntry",  UINT64 * 4),
    ("PteL6",             UINT64),
    ("PteL5",             UINT64),
    ("PteL4",             UINT64),
    ("PteL3",             UINT64),
    ("PteL2",             UINT64),
    ("PteL1",             UINT64)
  ]

