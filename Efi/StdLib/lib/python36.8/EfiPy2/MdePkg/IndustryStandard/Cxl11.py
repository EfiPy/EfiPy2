# Cxl11.py
#
# EfiPy2.MdePkg.IndustryStandard.Cxl11
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION
from EfiPy2.MdePkg.IndustryStandard.Pci import PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER,        \
                                               PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1, \
                                               PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2

INTEL_CXL_DVSEC_VENDOR_ID  = 0x8086

CXL_DEV_DEV   = 0
CXL_DEV_FUNC  = 0

class CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheCapable",    UINT16, 1),
    ("IoCapable",       UINT16, 1),
    ("MemCapable",      UINT16, 1),
    ("MemHwInitMode",   UINT16, 1),
    ("HdmCount",        UINT16, 2),
    ("Reserved1",       UINT16, 8),
    ("ViralCapable",    UINT16, 1),
    ("Reserved2",       UINT16, 1)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
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

class CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 14),
    ("ViralStatus", UINT16, 1),
    ("Reserved2",   UINT16, 1)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_STATUS_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 1),
    ("Reserved2",   UINT16, 1),
    ("Reserved3",   UINT16, 1),
    ("Reserved4",   UINT16, 13)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 1),
    ("Reserved2",   UINT16, 1),
    ("Reserved3",   UINT16, 14)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_LOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ConfigLock",  UINT16, 1),
    ("Reserved1",   UINT16, 15)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_LOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_LOCK_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemorySizeHigh",  UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryInfoValid",     UINT32, 1),
    ("MemoryActive",        UINT32, 1),
    ("MediaType",           UINT32, 3),
    ("MemoryClass",         UINT32, 3),
    ("DesiredInterleave",   UINT32, 3),
    ("Reserved",            UINT32, 17),
    ("MemorySizeLow",       UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryBaseHigh",      UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT32, 28),
    ("MemoryBaseLow",   UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemorySizeHigh",  UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryInfoValid",     UINT32, 1),
    ("MemoryActive",        UINT32, 1),
    ("MediaType",           UINT32, 3),
    ("MemoryClass",         UINT32, 3),
    ("DesiredInterleave",   UINT32, 3),
    ("Reserved",            UINT32, 17),
    ("MemorySizeLow",       UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryBaseHigh",      UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT32, 28),
    ("MemoryBaseLow",   UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

FLEX_BUS_DEVICE_DVSEC_ID  = 0

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER       ),
    ("DesignatedVendorSpecificHeader1", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DesignatedVendorSpecificHeader2", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("DeviceCapability",                CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY           ),
    ("DeviceControl",                   CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL              ),
    ("DeviceStatus",                    CXL_DVSEC_FLEX_BUS_DEVICE_STATUS               ),
    ("DeviceControl2",                  CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2         ),
    ("DeviceStatus2",                   CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2          ),
    ("DeviceLock",                      CXL_DVSEC_FLEX_BUS_DEVICE_LOCK                 ),
    ("Reserved",                        UINT16                                         ),
    ("DeviceRange1SizeHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH     ),
    ("DeviceRange1SizeLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW      ),
    ("DeviceRange1BaseHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH     ),
    ("DeviceRange1BaseLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW      ),
    ("DeviceRange2SizeHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH     ),
    ("DeviceRange2SizeLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW      ),
    ("DeviceRange2BaseHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH     ),
    ("DeviceRange2BaseLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW      )
  ]
class CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheCapable",    UINT16, 1),
    ("IoCapable",       UINT16, 1),
    ("MemCapable",      UINT16, 1),
    ("Reserved",        UINT16, 13)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheEnable",         UINT16, 1),
    ("IoEnable",            UINT16, 1),
    ("MemEnable",           UINT16, 1),
    ("CxlSyncBypassEnable", UINT16, 1),
    ("DriftBufferEnable",   UINT16, 1),
    ("Reserved",            UINT16, 3),
    ("Retimer1Present",     UINT16, 1),
    ("Retimer2Present",     UINT16, 1),
    ("Reserved2",           UINT16, 6)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL_Bits),
    ("Uint16",          UINT16)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheEnable",                             UINT16, 1),
    ("IoEnable",                                UINT16, 1),
    ("MemEnable",                               UINT16, 1),
    ("CxlSyncBypassEnable",                     UINT16, 1),
    ("DriftBufferEnable",                       UINT16, 1),
    ("Reserved",                                UINT16, 3),
    ("CxlCorrectableProtocolIdFramingError",    UINT16, 1),
    ("CxlUncorrectableProtocolIdFramingError",  UINT16, 1),
    ("CxlUnexpectedProtocolIdDropped",          UINT16, 1),
    ("Reserved2",                               UINT16, 5)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS_Bits),
    ("Uint16",          UINT16)
  ]

FLEX_BUS_PORT_DVSEC_ID  = 7

class CXL_1_1_DVSEC_FLEX_BUS_PORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER       ),
    ("DesignatedVendorSpecificHeader1", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DesignatedVendorSpecificHeader2", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("PortCapability",                  CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY         ),
    ("PortControl",                     CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL            ),
    ("PortStatus",                      CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS             )
  ]

CXL_CAPABILITY_HEADER_OFFSET  = 0
class CXL_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",         UINT32, 16),
    ("CxlCapabilityVersion",    UINT32,  4),
    ("CxlCacheMemVersion",      UINT32,  4),
    ("ArraySize",               UINT32,  8)
  ]

class CXL_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

CXL_RAS_CAPABILITY_HEADER_OFFSET  = 4
class CXL_RAS_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",         UINT32, 16),
    ("CxlCapabilityVersion",    UINT32,  4),
    ("CxlRasCapabilityPointer", UINT32, 12)
  ]

class CXL_RAS_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_RAS_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

CXL_SECURITY_CAPABILITY_HEADER_OFFSET  = 8
class CXL_SECURITY_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",                 UINT32, 16),
    ("CxlCapabilityVersion",            UINT32,  4),
    ("CxlSecurityCapabilityPointer",    UINT32, 12)
  ]

class CXL_SECURITY_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_SECURITY_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

CXL_LINK_CAPABILITY_HEADER_OFFSET  = 0xC
class CXL_LINK_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",             UINT32, 16),
    ("CxlCapabilityVersion",        UINT32,  4),
    ("CxlLinkCapabilityPointer",    UINT32, 12)
  ]

class CXL_LINK_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataParity",         UINT32,  1),
    ("CacheAddressParity",      UINT32,  1),
    ("CacheByteEnableParity",   UINT32,  1),
    ("CacheDataEcc",            UINT32,  1),
    ("MemDataParity",           UINT32,  1),
    ("MemAddressParity",        UINT32,  1),
    ("MemByteEnableParity",     UINT32,  1),
    ("MemDataEcc",              UINT32,  1),
    ("ReInitThreshold",         UINT32,  1),
    ("RsvdEncodingViolation",   UINT32,  1),
    ("PoisonReceived",          UINT32,  1),
    ("ReceiverOverflow",        UINT32,  1),
    ("Reserved",                UINT32, 20)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_UNCORRECTABLE_ERROR_STATUS_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_MASK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataParityMask",         UINT32,   1),
    ("CacheAddressParityMask",      UINT32,   1),
    ("CacheByteEnableParityMask",   UINT32,   1),
    ("CacheDataEccMask",            UINT32,   1),
    ("MemDataParityMask",           UINT32,   1),
    ("MemAddressParityMask",        UINT32,   1),
    ("MemByteEnableParityMask",     UINT32,   1),
    ("MemDataEccMask",              UINT32,   1),
    ("ReInitThresholdMask",         UINT32,   1),
    ("RsvdEncodingViolationMask",   UINT32,   1),
    ("PoisonReceivedMask",          UINT32,   1),
    ("ReceiverOverflowMask",        UINT32,   1),
    ("Reserved",                    UINT32,  20)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_MASK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_UNCORRECTABLE_ERROR_MASK_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataParitySeverity",         UINT32,   1),
    ("CacheAddressParitySeverity",      UINT32,   1),
    ("CacheByteEnableParitySeverity",   UINT32,   1),
    ("CacheDataEccSeverity",            UINT32,   1),
    ("MemDataParitySeverity",           UINT32,   1),
    ("MemAddressParitySeverity",        UINT32,   1),
    ("MemByteEnableParitySeverity",     UINT32,   1),
    ("MemDataEccSeverity",              UINT32,   1),
    ("ReInitThresholdSeverity",         UINT32,   1),
    ("RsvdEncodingViolationSeverity",   UINT32,   1),
    ("PoisonReceivedSeverity",          UINT32,   1),
    ("ReceiverOverflowSeverity",        UINT32,   1),
    ("Reserved",                        UINT32,  20)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_CORRECTABLE_ERROR_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataEcc",        UINT32,  1),
    ("MemoryDataEcc",       UINT32,  1),
    ("CrcThreshold",        UINT32,  1),
    ("RetryThreshold",      UINT32,  1),
    ("CachePoisonReceived", UINT32,  1),
    ("MemoryPoisonReceived",UINT32,  1),
    ("PhysicalLayerError",  UINT32,  1),
    ("Reserved",            UINT32, 25)
  ]

class CXL_CORRECTABLE_ERROR_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CORRECTABLE_ERROR_STATUS_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_CORRECTABLE_ERROR_MASK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataEccMask",        UINT32,  1),
    ("MemoryDataEccMask",       UINT32,  1),
    ("CrcThresholdMask",        UINT32,  1),
    ("RetryThresholdMask",      UINT32,  1),
    ("CachePoisonReceivedMask", UINT32,  1),
    ("MemoryPoisonReceivedMask",UINT32,  1),
    ("PhysicalLayerErrorMask",  UINT32,  1),
    ("Reserved",                UINT32, 25)
  ]

class CXL_CORRECTABLE_ERROR_MASK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CORRECTABLE_ERROR_MASK_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_ERROR_CAPABILITIES_AND_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FirstErrorPointer",                   UINT32,  4),
    ("Reserved1",                           UINT32,  5),
    ("MultipleHeaderRecordingCapability",   UINT32,  1),
    ("Reserved2",                           UINT32,  3),
    ("PoisonEnabled",                       UINT32,  1),
    ("Reserved3",                           UINT32, 18)
  ]

class CXL_ERROR_CAPABILITIES_AND_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_ERROR_CAPABILITIES_AND_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_1_1_RAS_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UncorrectableErrorStatus",    CXL_1_1_UNCORRECTABLE_ERROR_STATUS  ),
    ("UncorrectableErrorMask",      CXL_1_1_UNCORRECTABLE_ERROR_MASK    ),
    ("UncorrectableErrorSeverity",  CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY),
    ("CorrectableErrorStatus",      CXL_CORRECTABLE_ERROR_STATUS        ),
    ("CorrectableErrorMask",        CXL_CORRECTABLE_ERROR_MASK          ),
    ("ErrorCapabilitiesAndControl", CXL_ERROR_CAPABILITIES_AND_CONTROL  ),
    ("HeaderLog",                   UINT32 * 16                         )
  ]

class CXL_1_1_SECURITY_POLICY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceTrustLevel",    UINT32, 2),
    ("Reserved",            UINT32, 30)
  ]

class CXL_1_1_SECURITY_POLICY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_SECURITY_POLICY_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_1_1_SECURITY_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SecurityPolicy",  CXL_1_1_SECURITY_POLICY)
  ]

class CXL_LINK_LAYER_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlLinkVersionSupported", UINT64, 4),
    ("CxlLinkVersionReceived",  UINT64, 4),
    ("LlrWrapValueSupported",   UINT64, 8),
    ("LlrWrapValueReceived",    UINT64, 8),
    ("NumRetryReceived",        UINT64, 5),
    ("NumPhyReinitReceived",    UINT64, 5),
    ("WrPtrReceived",           UINT64, 8),
    ("EchoEseqReceived",        UINT64, 8),
    ("NumFreeBufReceived",      UINT64, 8),
    ("Reserved",                UINT64, 6)
  ]

class CXL_LINK_LAYER_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_CAPABILITY_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_LINK_LAYER_CONTROL_AND_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LlReset",                 UINT64, 1),
    ("LlInitStall",             UINT64, 1),
    ("LlCrdStall",              UINT64, 1),
    ("InitState",               UINT64, 2),
    ("LlRetryBufferConsumed",   UINT64, 8),
    ("Reserved",                UINT64, 3)
  ]

class CXL_LINK_LAYER_CONTROL_AND_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_CONTROL_AND_STATUS_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_LINK_LAYER_RX_CREDIT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReqCredits",  UINT64, 10),
    ("CacheRspCredits",  UINT64, 10),
    ("CacheDataCredits", UINT64, 10),
    ("MemReqRspCredits", UINT64, 10),
    ("MemDataCredits",   UINT64, 10)
  ]

class CXL_LINK_LAYER_RX_CREDIT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_RX_CREDIT_CONTROL_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReqCredits",  UINT64, 10),
    ("CacheRspCredits",  UINT64, 10),
    ("CacheDataCredits", UINT64, 10),
    ("MemReqRspCredits", UINT64, 10),
    ("MemDataCredits",   UINT64, 10)
  ]

class CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_LINK_LAYER_TX_CREDIT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReqCredits",  UINT64, 10),
    ("CacheRspCredits",  UINT64, 10),
    ("CacheDataCredits", UINT64, 10),
    ("MemReqRspCredits", UINT64, 10),
    ("MemDataCredits",   UINT64, 10)
  ]

class CXL_LINK_LAYER_TX_CREDIT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_TX_CREDIT_STATUS_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_LINK_LAYER_ACK_TIMER_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AckForceThreshold",  UINT64, 8),
    ("AckFLushRetimer",    UINT64, 10)
  ]

class CXL_LINK_LAYER_ACK_TIMER_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_ACK_TIMER_CONTROL_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_LINK_LAYER_DEFEATURE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MdhDisable",  UINT32, 1),
    ("Reserved",    UINT32, 31)
  ]

class CXL_LINK_LAYER_DEFEATURE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_DEFEATURE_Bits),
    ("Uint64",          UINT64)
  ]

class CXL_1_1_LINK_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LinkLayerCapability",             CXL_LINK_LAYER_CAPABILITY             ),
    ("LinkLayerControlStatus",          CXL_LINK_LAYER_CONTROL_AND_STATUS     ),
    ("LinkLayerRxCreditControl",        CXL_LINK_LAYER_RX_CREDIT_CONTROL      ),
    ("LinkLayerRxCreditReturnStatus",   CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS),
    ("LinkLayerTxCreditStatus",         CXL_LINK_LAYER_TX_CREDIT_STATUS       ),
    ("LinkLayerAckTimerControl",        CXL_LINK_LAYER_ACK_TIMER_CONTROL      ),
    ("LinkLayerDefeature",              CXL_LINK_LAYER_DEFEATURE              )
  ]

class CXL_IO_ARBITRATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",                           UINT32,  4),
    ("WeightedRoundRobinArbitrationWeight", UINT32,  4),
    ("Reserved2",                           UINT32, 24)
  ]

class CXL_IO_ARBITRATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_IO_ARBITRATION_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_CACHE_MEMORY_ARBITRATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",                           UINT32,  4),
    ("WeightedRoundRobinArbitrationWeight", UINT32,  4),
    ("Reserved2",                           UINT32, 24)
  ]

class CXL_CACHE_MEMORY_ARBITRATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CACHE_MEMORY_ARBITRATION_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

class CXL_RCRB_BASE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RcrbEnable",      UINT64,  1),
    ("Reserved",        UINT64, 12),
    ("RcrbBaseAddress", UINT64, 51)
  ]

class CXL_RCRB_BASE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_RCRB_BASE_Bits),
    ("Uint64",          UINT64)
  ]

CXL_PORT_RCRB_MEMBAR0_LOW_OFFSET               = 0x010
CXL_PORT_RCRB_MEMBAR0_HIGH_OFFSET              = 0x014
CXL_PORT_RCRB_EXTENDED_CAPABILITY_BASE_OFFSET  = 0x100
