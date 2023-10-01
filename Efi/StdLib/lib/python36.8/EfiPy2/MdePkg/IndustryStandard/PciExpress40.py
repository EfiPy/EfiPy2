# PciExpress40.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress40
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.PciExpress31 import *

PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_16_0_ID    = 0x0026
PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_16_0_VER1  = 0x1

PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_OFFSET                       = 0x04
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_OFFSET                            = 0x08
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_OFFSET                             = 0x0C
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LOCAL_DATA_PARITY_STATUS_OFFSET           = 0x10
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_FIRST_RETIMER_DATA_PARITY_STATUS_OFFSET   = 0x14
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_SECOND_RETIMER_DATA_PARITY_STATUS_OFFSET  = 0x18
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_OFFSET          = 0x20

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT32, 32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT32, 32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EqualizationComplete",        UINT32, 1),
    ("EqualizationPhase1Success",   UINT32, 1),
    ("EqualizationPhase2Success",   UINT32, 1),
    ("EqualizationPhase3Success",   UINT32, 1),
    ("LinkEqualizationRequest",     UINT32, 1),
    ("Reserved",                    UINT32, 27)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DownstreamPortTransmitterPreset", UINT8, 4),
    ("UpstreamPortTransmitterPreset",   UINT8, 4)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_Bits),
    ("Uint8",           UINT8)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_PHYSICAL_LAYER_16_0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                         ),
    ("Capablities",                             PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES                 ),
    ("Control",                                 PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL                      ),
    ("Status",                                  PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS                       ),
    ("LocalDataParityMismatchStatus",           UINT32                                                           ),
    ("FirstRetimerDataParityMismatchStatus",    UINT32                                                           ),
    ("SecondRetimerDataParityMismatchStatus",   UINT32                                                           ),
    ("Reserved",                                UINT32                                                           ),
    ("LaneEqualizationControl",                 PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL * 1)
  ]

class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DvsecVendorId",   UINT32, 16),
    ("DvsecRevision",   UINT32, 4),
    ("DvsecLength",     UINT32, 12)
  ]

class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DvsecId",         UINT16, 16)
  ]

class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_DESIGNATED_VENDOR_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DesignatedVendorSpecificHeader1", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DesignatedVendorSpecificHeader2", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("DesignatedVendorSpecific",        UINT8 * 1)
  ]

