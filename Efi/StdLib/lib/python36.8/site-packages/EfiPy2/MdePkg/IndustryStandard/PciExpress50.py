# PciExpress50.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress50
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.PciExpress40 import *

PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_32_0_ID    = 0x002A
PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_32_0_VER1  = 0x1

PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CAPABILITIES_OFFSET               = 0x04
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CONTROL_OFFSET                    = 0x08
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_STATUS_OFFSET                     = 0x0C
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA1_OFFSET     = 0x10
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA2_OFFSET     = 0x14
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA1_OFFSET    = 0x18
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA2_OFFSET    = 0x1C
PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_LANE_EQUALIZATION_CONTROL_OFFSET  = 0x20

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EqualizationByPassToHighestRateSuppor",   UINT32, 1),
    ("NoEqualizationNeededSupport",             UINT32, 1),
    ("Reserved1",                               UINT32, 6),
    ("ModifiedTSUsageMode0Support",             UINT32, 1),
    ("ModifiedTSUsageMode1Support",             UINT32, 1),
    ("ModifiedTSUsageMode2Support",             UINT32, 1),
    ("ModifiedTSReservedUsageModes",            UINT32, 5),
    ("Reserved2",                               UINT32, 16)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CAPABILITIES_Bits),
    ("Uint32",          UINT32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EqualizationByPassToHighestRateDisable",  UINT32, 1),
    ("NoEqualizationNeededDisable",             UINT32, 1),
    ("Reserved1",                               UINT32, 6),
    ("ModifiedTSUsageModeSelected",             UINT32, 3),
    ("Reserved2",                               UINT32, 21)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EqualizationComplete",        UINT32, 1),
    ("EqualizationPhase1Success",   UINT32, 1),
    ("EqualizationPhase2Success",   UINT32, 1),
    ("EqualizationPhase3Success",   UINT32, 1),
    ("LinkEqualizationRequest",     UINT32, 1),
    ("ModifiedTSRcvd",              UINT32, 1),
    ("RcvdEnhancedLinkControl",     UINT32, 2),
    ("TransmitterPrecodingOn",      UINT32, 1),
    ("TransmitterPrecodeRequest",   UINT32, 1),
    ("NoEqualizationNeededRcvd",    UINT32, 1),
    ("Reserved",                    UINT32, 21)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_STATUS_Bits),
    ("Uint32",          UINT32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RcvdModifiedTSUsageMode",     UINT32, 3),
    ("RcvdModifiedTSUsageInfo1",    UINT32, 13),
    ("RcvdModifiedTSVendorId",      UINT32, 16)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA1_Bits),
    ("Uint32",          UINT32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RcvdModifiedTSUsageInfo2",        UINT32, 24),
    ("AltProtocolNegotiationStatus",    UINT32, 2),
    ("Reserved",                        UINT32, 6)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA2_Bits),
    ("Uint32",          UINT32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TransModifiedTSUsageMode",    UINT32, 3),
    ("TransModifiedTSUsageInfo1",   UINT32, 13),
    ("TransModifiedTSVendorId",     UINT32, 16)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA1_Bits),
    ("Uint32",          UINT32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TransModifiedTSUsageInfo2",       UINT32, 24),
    ("AltProtocolNegotiationStatus",    UINT32, 2),
    ("Reserved",                        UINT32, 6)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA2_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_LANE_EQUALIZATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DownstreamPortTransmitterPreset", UINT8, 4),
    ("UpstreamPortTransmitterPreset",   UINT8, 4)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_LANE_EQUALIZATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_LANE_EQUALIZATION_CONTROL_Bits),
    ("Uint8",           UINT8)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_PHYSICAL_LAYER_32_0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                     ),
    ("Capablities",             PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CAPABILITIES             ),
    ("Control",                 PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_CONTROL                  ),
    ("Status",                  PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_STATUS                   ),
    ("RcvdModifiedTs1Data",     PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA1   ),
    ("RcvdModifiedTs2Data",     PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_RCVD_MODIFIED_TS_DATA2   ),
    ("TransModifiedTs1Data",    PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA1  ),
    ("TransModifiedTs2Data",    PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_TRANS_MODIFIED_TS_DATA2  ),
    ("LaneEqualizationControl", PCI_EXPRESS_REG_PHYSICAL_LAYER_32_0_LANE_EQUALIZATION_CONTROL)
  ]
