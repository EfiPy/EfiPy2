# PciExpress30.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress30
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.PciExpress21 import *

PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_ID    = 0x0019
PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_VER1  = 0x1   

class PCI_EXPRESS_REG_LINK_CONTROL3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PerformEqualization",                     UINT32, 1),
    ("LinkEqualizationRequestInterruptEnable",  UINT32, 1),
    ("Reserved",                                UINT32, 30)
  ]

class PCI_EXPRESS_REG_LINK_CONTROL3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_LINK_CONTROL3_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DownstreamPortTransmitterPreset",     UINT16, 4),
    ("DownstreamPortReceiverPresetHint",    UINT16, 3),
    ("Reserved",                            UINT16, 1),
    ("UpstreamPortTransmitterPreset",       UINT16, 4),
    ("UpstreamPortReceiverPresetHint",      UINT16, 3),
    ("Reserved2",                           UINT16, 1)
  ]

class PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_SECONDARY_PCIE (Structure):
  _fields_ = [
    ("Header",              PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("LinkControl3",        PCI_EXPRESS_REG_LINK_CONTROL3),
    ("LaneErrorStatus",     UINT32),
    ("EqualizationControl", PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL * 2)
    ]
