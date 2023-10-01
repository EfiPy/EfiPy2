# PciExpress31.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress31
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.PciExpress30 import *

PCI_EXPRESS_EXTENDED_CAPABILITY_L1_PM_SUBSTATES_ID    = 0x001E
PCI_EXPRESS_EXTENDED_CAPABILITY_L1_PM_SUBSTATES_VER1  = 0x1

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PciPmL12",                UINT32, 1),
    ("PciPmL11",                UINT32, 1),
    ("AspmL12",                 UINT32, 1),
    ("AspmL11",                 UINT32, 1),
    ("L1PmSubstates",           UINT32, 1),
    ("Reserved",                UINT32, 3),
    ("CommonModeRestoreTime",   UINT32, 8),
    ("TPowerOnScale",           UINT32, 2),
    ("Reserved2",               UINT32, 1),
    ("TPowerOnValue",           UINT32, 5),
    ("Reserved3",               UINT32, 8)
  ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PciPmL12",                UINT32, 1),
    ("PciPmL11",                UINT32, 1),
    ("AspmL12",                 UINT32, 1),
    ("AspmL11",                 UINT32, 1),
    ("Reserved",                UINT32, 4),
    ("CommonModeRestoreTime",   UINT32, 8),
    ("LtrL12ThresholdValue",    UINT32, 10),
    ("Reserved2",               UINT32, 3),
    ("LtrL12ThresholdScale",    UINT32, 3)
  ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TPowerOnScale",   UINT32, 2),
    ("Reserved",        UINT32, 1),
    ("TPowerOnValue",   UINT32, 5),
    ("Reserved2",       UINT32, 24)
  ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_L1_PM_SUBSTATES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("Capability",  PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY),
    ("Control1",    PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1),
    ("Control2",    PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2)
  ]

