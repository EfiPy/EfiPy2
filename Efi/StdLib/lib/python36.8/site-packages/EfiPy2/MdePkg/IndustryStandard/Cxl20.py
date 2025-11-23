# Cxl20.py
#
# EfiPy2.MdePkg.IndustryStandard.Cxl20
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import Cxl11, Acpi, PciExpress50, EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION

CXL_DVSEC_ID_PCIE_DVSEC_FOR_CXL_DEVICE         = 0x0
CXL_DVSEC_ID_NON_CXL_FUNCTION_MAP              = 0x2
CXL_DVSEC_ID_CXL20_EXTENSIONS_DVSEC_FOR_PORTS  = 0x3
CXL_DVSEC_ID_GPF_DVSEC_FOR_CXL_PORTS           = 0x4
CXL_DVSEC_ID_GPF_DVSEC_FOR_CXL_DEVICES         = 0x5
CXL_DVSEC_ID_PCIE_DVSEC_FOR_FLEX_BUS_PORT      = 0x7
CXL_DVSEC_ID_REGISTER_LOCATOR                  = 0x8
CXL_DVSEC_ID_MLD                               = 0x9
CXL_DVSEC_ID_PCIE_DVSEC_FOR_TEST_CAPABILITY    = 0xA

CXL_REGISTER_BLOCK_ID_EMPTY                   = 0x0
CXL_REGISTER_BLOCK_ID_COMPONENT               = 0x1
CXL_REGISTER_BLOCK_ID_BAR_VIRTUALIZATION_ACL  = 0x2
CXL_REGISTER_BLOCK_ID_DEVICE                  = 0x3

CXL_COMPONENT_REGISTER_RANGE_OFFSET_IO         = 0x0
CXL_COMPONENT_REGISTER_RANGE_OFFSET_CACHE_MEM  = 0x1000
CXL_COMPONENT_REGISTER_RANGE_OFFSET_ARB_MUX    = 0xE000

CXL_CACHE_MEM_CAPABILITY_ID_CXL                = 0x1
CXL_CACHE_MEM_CAPABILITY_ID_RAS                = 0x2
CXL_CACHE_MEM_CAPABILITY_ID_SECURITY           = 0x3
CXL_CACHE_MEM_CAPABILITY_ID_LINK               = 0x4
CXL_CACHE_MEM_CAPABILITY_ID_HDM_DECODER        = 0x5
CXL_CACHE_MEM_CAPABILITY_ID_EXTENDED_SECURITY  = 0x6
CXL_CACHE_MEM_CAPABILITY_ID_IDE                = 0x7
CXL_CACHE_MEM_CAPABILITY_ID_SNOOP_FILTER       = 0x8
CXL_CACHE_MEM_CAPABILITY_ID_MASK               = 0xFFFF

CXL_DEVICE_CAPABILITY_ID_CAPABILITIES_ARRAY_REGISTER  = 0x0000
CXL_DEVICE_CAPABILITY_ID_DEVICE_STATUS                = 0x0001
CXL_DEVICE_CAPABILITY_ID_PRIMARY_MAILBOX              = 0x0002
CXL_DEVICE_CAPABILITY_ID_SECONDARY_MAILBOX            = 0x0003

CXL_DEVICE_CAPABILITY_ID_MEMORY_DEVICE_STATUS  = 0x4000
CXL_DEVICE_CAPABILITY_ID_MASK                  = 0xFFFF

CXL_MEM_DEVICE_MEDIA_STATUS_NOT_READY  = 0x0
CXL_MEM_DEVICE_MEDIA_STATUS_READY      = 0x1
CXL_MEM_DEVICE_MEDIA_STATUS_ERROR      = 0x2
CXL_MEM_DEVICE_MEDIA_STATUS_DISABLED   = 0x3

CXL_EARLY_DISCOVERY_TABLE_SIGNATURE  = SIGNATURE_32 ('C', 'E', 'D', 'T')

CEDT_TYPE_CHBS  = 0x0

class CXL_DVSEC_CXL_DEVICE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheCapable",                        UINT16, 1),
    ("IoCapable",                           UINT16, 1),
    ("MemCapable",                          UINT16, 1),
    ("MemHwInitMode",                       UINT16, 1),
    ("HdmCount",                            UINT16, 2),
    ("CacheWriteBackAndInvalidateCapable",  UINT16, 1),
    ("CxlResetCapable",                     UINT16, 1),
    ("CxlResetTimeout",                     UINT16, 3),
    ("CxlResetMemClrCapable",               UINT16, 1),
    ("Reserved",                            UINT16, 1),
    ("MultipleLogicalDevice",               UINT16, 1),
    ("ViralCapable",                        UINT16, 1),
    ("PmInitCompletionReportingCapable",    UINT16, 1)
  ]
class CXL_DVSEC_CXL_DEVICE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_CAPABILITY_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheEnable",         UINT16, 1),
    ("IoEnable",            UINT16, 1),
    ("MemEnable",           UINT16, 1),
    ("CacheSfCoverage",     UINT16, 5),
    ("CacheSfGranularity",  UINT16, 3),
    ("CacheCleanEviction",  UINT16, 1),
    ("Reserved1",           UINT16, 2),
    ("ViralEnable",         UINT16, 1),
    ("Reserved2",           UINT16, 1)
  ]
class CXL_DVSEC_CXL_DEVICE_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_CONTROL_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 14),
    ("ViralStatus", UINT16, 1),
    ("Reserved2",   UINT16, 1)
  ]
class CXL_DVSEC_CXL_DEVICE_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_STATUS_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DisableCaching",                      UINT16, 1),
    ("InitiateCacheWriteBackAndInvalidate", UINT16, 1),
    ("InitiateCxlReset",                    UINT16, 1),
    ("CxlResetMemClrEnable",                UINT16, 1),
    ("Reserved",                            UINT16, 12)
  ]
class CXL_DVSEC_CXL_DEVICE_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_CONTROL2_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_STATUS2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheInvalid",                          UINT16, 1),
    ("CxlResetComplete",                      UINT16, 1),
    ("Reserved",                              UINT16, 13),
    ("PowerManagementInitialzationComplete",  UINT16, 1)
  ]
class CXL_DVSEC_CXL_DEVICE_STATUS2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_STATUS2_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_LOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ConfigLock",  UINT16, 1),
    ("Reserved",    UINT16, 15)
  ]
class CXL_DVSEC_CXL_DEVICE_LOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_LOCK_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_CAPABILITY2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheSizeUnit", UINT16, 4),
    ("Reserved",      UINT16, 4),
    ("CacheSize",     UINT16, 8)
  ]
class CXL_DVSEC_CXL_DEVICE_CAPABILITY2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_CAPABILITY2_Bits),
    ("Uint16",    UINT16)
  ]

class CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemorySizeHigh ",   UINT32, 32)
  ]
class CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_HIGH_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryInfoValid",       UINT32, 1),
    ("MemoryActive",          UINT32, 1),
    ("MediaType",             UINT32, 3),
    ("MemoryClass",           UINT32, 3),
    ("DesiredInterleave",     UINT32, 5),
    ("MemoryActiveTimeout",   UINT32, 3),
    ("Reserved",              UINT32, 12),
    ("MemorySizeLow",         UINT32, 4)
  ]
class CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_LOW_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_DVSEC_CXL_DEVICE_RANGE_BASE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryBaseHigh",       UINT32, 32)
  ]
class CXL_DVSEC_CXL_DEVICE_RANGE_BASE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_RANGE_BASE_HIGH_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_DVSEC_CXL_DEVICE_RANGE_BASE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT32, 28),
    ("MemoryBaseLow",   UINT32, 4)
  ]
class CXL_DVSEC_CXL_DEVICE_RANGE_BASE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_CXL_DEVICE_RANGE_BASE_LOW_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_DVSEC_CXL_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                PciExpress50.PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER       ),
    ("DvsecHeader1",          PciExpress50.PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DvsecHeader2",          PciExpress50.PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("DeviceCapability",      CXL_DVSEC_CXL_DEVICE_CAPABILITY                ),
    ("DeviceControl",         CXL_DVSEC_CXL_DEVICE_CONTROL                   ),
    ("DeviceStatus",          CXL_DVSEC_CXL_DEVICE_STATUS                    ),
    ("DeviceControl2",        CXL_DVSEC_CXL_DEVICE_CONTROL2                  ),
    ("DeviceStatus2",         CXL_DVSEC_CXL_DEVICE_STATUS2                   ),
    ("DeviceLock",            CXL_DVSEC_CXL_DEVICE_LOCK                      ),
    ("DeviceCapability2",     CXL_DVSEC_CXL_DEVICE_CAPABILITY2               ),
    ("DeviceRange1SizeHigh",  CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_HIGH           ),
    ("DeviceRange1SizeLow",   CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_LOW            ),
    ("DeviceRange1BaseHigh",  CXL_DVSEC_CXL_DEVICE_RANGE_BASE_HIGH           ),
    ("DeviceRange1BaseLow",   CXL_DVSEC_CXL_DEVICE_RANGE_BASE_LOW            ),
    ("DeviceRange2SizeHigh",  CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_HIGH           ),
    ("DeviceRange2SizeLow",   CXL_DVSEC_CXL_DEVICE_RANGE_SIZE_LOW            ),
    ("DeviceRange2BaseHigh",  CXL_DVSEC_CXL_DEVICE_RANGE_BASE_HIGH           ),
    ("DeviceRange2BaseLow",   CXL_DVSEC_CXL_DEVICE_RANGE_BASE_LOW            )
  ]

CXL_DVSEC_CXL_DEVICE_REVISION_1  = 0x1

class CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterBir",             UINT32, 3),
    ("Reserved",                UINT32, 5),
    ("RegisterBlockIdentifier", UINT32, 8),
    ("RegisterBlockOffsetLow",  UINT32, 16)
  ]
class CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_LOW_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterBlockOffsetHigh",  UINT32, 32)
  ]
class CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_HIGH_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_DVSEC_REGISTER_LOCATOR_REGISTER_BLOCK (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OffsetLow",  CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_LOW),
    ("OffsetHigh", CXL_DVSEC_REGISTER_LOCATOR_REGISTER_OFFSET_HIGH)
  ]

class CXL_DVSEC_REGISTER_LOCATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",        PciExpress50.PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DvsecHeader1",  PciExpress50.PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DvsecHeader2",  PciExpress50.PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("Reserved",      UINT16),
    ("RegisterBlock", CXL_DVSEC_REGISTER_LOCATOR_REGISTER_BLOCK)
  ]

CXL_DVSEC_REGISTER_LOCATOR_REVISION_0  = 0x0

class CXL_HDM_DECODER_CAPABILITY_HEADER_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",                 UINT32, 16),
    ("CxlCapabilityVersion",            UINT32,  4),
    ("CxlHdmDecoderCapabilityPointer",  UINT32, 12)
  ]
class CXL_HDM_DECODER_CAPABILITY_HEADER_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_CAPABILITY_HEADER_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_CAPABILITY_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DecoderCount",                  UINT32, 4),
    ("TargetCount",                   UINT32, 4),
    ("InterleaveCapableA11to8",       UINT32, 1),
    ("InterleaveCapableA14to12",      UINT32, 1),
    ("PoisonOnDecodeErrorCapability", UINT32, 1),
    ("Reserved", UINT32, 21)
  ]
class CXL_HDM_DECODER_CAPABILITY_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_CAPABILITY_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_GLOBAL_CONTROL_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PoisonOnDecodeErrorEnable", UINT32, 1),
    ("HdmDecoderEnable",          UINT32, 1),
    ("Reserved",                  UINT32, 30)
  ]
class CXL_HDM_DECODER_GLOBAL_CONTROL_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_GLOBAL_CONTROL_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_BASE_LOW_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",      UINT32, 28),
    ("MemoryBaseLow", UINT32, 4)
  ]
class CXL_HDM_DECODER_BASE_LOW_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_BASE_LOW_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_BASE_HIGH_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryBaseHigh",    UINT32, 32)
  ]
class CXL_HDM_DECODER_BASE_HIGH_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_BASE_HIGH_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_SIZE_LOW_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT32, 28),
    ("MemorySizeLow",   UINT32, 4)
  ]
class CXL_HDM_DECODER_SIZE_LOW_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_SIZE_LOW_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_SIZE_HIGH_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemorySizeHigh",    UINT32, 32)
  ]
class CXL_HDM_DECODER_SIZE_HIGH_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_SIZE_HIGH_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_CONTROL_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InterleaveGranularity", UINT32, 4),
    ("InterleaveWays",        UINT32, 4),
    ("LockOnCommit",          UINT32, 1),
    ("Commit",                UINT32, 1),
    ("Committed",             UINT32, 1),
    ("ErrorNotCommitted",     UINT32, 1),
    ("TargetDeviceType",      UINT32, 1),
    ("Reserved",              UINT32, 19)
  ]
class CXL_HDM_DECODER_CONTROL_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_CONTROL_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_TARGET_LIST_LOW_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TargetPortIdentiferWay0", UINT32, 8),
    ("TargetPortIdentiferWay1", UINT32, 8),
    ("TargetPortIdentiferWay2", UINT32, 8),
    ("TargetPortIdentiferWay3", UINT32, 8)
  ]
class CXL_HDM_DECODER_TARGET_LIST_LOW_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_TARGET_LIST_LOW_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_DPA_SKIP_LOW_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT32, 28),
    ("DpaSkipLow",  UINT32, 4)
  ]
class CXL_HDM_DECODER_DPA_SKIP_LOW_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_DPA_SKIP_LOW_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_TARGET_LIST_HIGH_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TargetPortIdentiferWay4", UINT32, 8),
    ("TargetPortIdentiferWay5", UINT32, 8),
    ("TargetPortIdentiferWay6", UINT32, 8),
    ("TargetPortIdentiferWay7", UINT32, 8)
  ]
class CXL_HDM_DECODER_TARGET_LIST_HIGH_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_TARGET_LIST_HIGH_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_DPA_SKIP_HIGH_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DpaSkipHigh ",    UINT32, 32)
  ]
class CXL_HDM_DECODER_DPA_SKIP_HIGH_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_HDM_DECODER_DPA_SKIP_HIGH_REGISTER_Bits),
    ("Uint32",    UINT32)
  ]

class CXL_HDM_DECODER_TARGET_LIST_OR_DPA_SKIP_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("TargetListLow", CXL_HDM_DECODER_TARGET_LIST_LOW_REGISTER),
    ("DpaSkipLow",    CXL_HDM_DECODER_DPA_SKIP_LOW_REGISTER)
  ]

class CXL_HDM_DECODER_TARGET_LIST_OR_DPA_SKIP_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("TargetListHigh",  CXL_HDM_DECODER_TARGET_LIST_HIGH_REGISTER),
    ("DpaSkipHigh",     CXL_HDM_DECODER_DPA_SKIP_HIGH_REGISTER)
  ]

class CXL_HDM_DECODER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DecoderBaseLow",                CXL_HDM_DECODER_BASE_LOW_REGISTER           ),
    ("DecoderBaseHigh",               CXL_HDM_DECODER_BASE_HIGH_REGISTER          ),
    ("DecoderSizeLow",                CXL_HDM_DECODER_SIZE_LOW_REGISTER           ),
    ("DecoderSizeHigh",               CXL_HDM_DECODER_SIZE_HIGH_REGISTER          ),
    ("DecoderControl",                CXL_HDM_DECODER_CONTROL_REGISTER            ),
    ("DecoderTargetListDpaSkipLow",   CXL_HDM_DECODER_TARGET_LIST_OR_DPA_SKIP_LOW ),
    ("DecoderTargetListDpaSkipHigh",  CXL_HDM_DECODER_TARGET_LIST_OR_DPA_SKIP_HIGH),
    ("Reserved", UINT32                                      )
  ]

class CXL_DEVICE_CAPABILITIES_ARRAY_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlDeviceCapabilityId",       UINT64, 16),
    ("CxlDeviceCapabilityVersion",  UINT64, 8),
    ("Reserved1",                   UINT64, 8),
    ("CxlDeviceCapabilitiesCount",  UINT64, 16),
    ("Reserved2",                   UINT64, 16)
  ]
class CXL_DEVICE_CAPABILITIES_ARRAY_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_DEVICE_CAPABILITIES_ARRAY_REGISTER_Bits),
    ("Uint64",    UINT64)
  ]

class CXL_MEMORY_DEVICE_STATUS_REGISTER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceFatal",             UINT64, 1),
    ("FwHalt",                  UINT64, 1),
    ("MediaStatus",             UINT64, 2),
    ("MailboxInterfacesReady",  UINT64, 1),
    ("ResetNeeded",             UINT64, 3),
    ("Reserved",                UINT64, 56)
  ]
class CXL_MEMORY_DEVICE_STATUS_REGISTER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",      CXL_MEMORY_DEVICE_STATUS_REGISTER_Bits),
    ("Uint64",    UINT64)
  ]

class CXL_EARLY_DISCOVERY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                Acpi.EFI_ACPI_DESCRIPTION_HEADER)
  ]

class CEDT_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",      UINT8 ),
    ("Reserved",  UINT8 ),
    ("Length",    UINT16)
  ]

class CXL_HOST_BRIDGE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      CEDT_STRUCTURE),
    ("Uid",         UINT32        ),
    ("CxlVersion",  UINT32        ),
    ("Reserved",    UINT32        ),
    ("Base",        UINT64        ),
    ("Length",      UINT64        )
  ]
