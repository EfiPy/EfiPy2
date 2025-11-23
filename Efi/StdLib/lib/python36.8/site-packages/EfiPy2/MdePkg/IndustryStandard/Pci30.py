# Pci30.py
#
# EfiPy2.MdePkg.IndustryStandard.Pci30
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.Pci23 import *

PCI_CLASS_MASS_STORAGE_SATADPA   = 0x06
PCI_IF_MASS_STORAGE_SATA         = 0x00
PCI_IF_MASS_STORAGE_AHCI         = 0x01

PCI_SUBCLASS_ETHERNET_80211A    = 0x20
PCI_SUBCLASS_ETHERNET_80211B    = 0x21

def IS_PCI_SATADPA(_p):
  return IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_SATADPA)

EFI_PCI_CAPABILITY_ID_PCIEXP  = 0x10

class PCI_3_0_DATA_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",                     UINT32),
    ("VendorId",                      UINT16),
    ("DeviceId",                      UINT16),
    ("DeviceListOffset",              UINT16),
    ("Length",                        UINT16),
    ("Revision",                      UINT8),
    ("ClassCode",                     UINT8 * 3),
    ("ImageLength",                   UINT16),
    ("CodeRevision",                  UINT16),
    ("CodeType",                      UINT8),
    ("Indicator",                     UINT8),
    ("MaxRuntimeImageLength",         UINT16),
    ("ConfigUtilityCodeHeaderOffset", UINT16),
    ("DMTFCLPEntryPointOffset",       UINT16)
    ]

