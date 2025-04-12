# PciTree.py
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com All rights reserved.
#
# GPL-v2
#

import EfiPy2 as EfiPy
from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION
import EfiPy2.MdePkg.IndustryStandard.Pci as pci

from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable
from EfiPy2.Lib.Acpi.AcpiMcfgParser import AcpiMcfgParser

def BuildPciHeader (EcamBase: int, EcamOffset: int) -> None:

  PciCfgAddress = EcamBase + EcamOffset

  PciCfg = pci.PCI_TYPE00.from_address (PciCfgAddress)

  PciTypeFields = [
      ('Hdr',     pci.PCI_DEVICE_INDEPENDENT_REGION),
    ]

  #
  # Build TYPE 00/01 header
  #
  if pci.IS_PCI_BRIDGE (PciCfg) or pci.IS_CARDBUS_BRIDGE (PciCfg):
    # Type 1
    PciTypeFields.append (('Cfg', pci.PCI_BRIDGE_CONTROL_REGISTER))

  else:
    # Type 0
    PciTypeFields.append (('Cfg', pci.PCI_DEVICE_HEADER_TYPE_REGION))

  class PciStruct (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = PciTypeFields

  PciCfg = PciStruct.from_address (PciCfgAddress)

  return PciCfg, PciStruct

def IS_PCI_HC(_p):
  return pci.IS_CLASS3 (_p, pci.PCI_CLASS_BRIDGE, pci.PCI_CLASS_BRIDGE_HOST, pci.PCI_IF_BRIDGE_P2P)

PciCfgBase = 0x00
ScanB = False

def ScanBus (Bus, Depth):

  global ScanB

  for Dev in range (pci.PCI_MAX_DEVICE + 1):
    for Func in range (pci.PCI_MAX_FUNC + 1):

        PciCfgOffset  = pci.PCI_ECAM_ADDRESS (Bus, Dev, Func, 0)
        PciObj, PciType = BuildPciHeader (PciCfgBase, PciCfgOffset)

        if PciObj.Hdr.VendorId == 0xFFFF and Func == 0:
          break

        if PciObj.Hdr.VendorId == 0xFFFF:
          continue

        if pci.IS_PCI_P2P (PciObj):
            if Depth == 0:
              print ()
            print (f'{"------+"*Depth} B {Bus:02X}:{Dev:02X}.{Func:X} ({PciObj.Hdr.VendorId:04X} {PciObj.Hdr.DeviceId:04X}) => ({PciObj.Cfg.SecondaryBus:02X}, {PciObj.Cfg.SubordinateBus:02X})')
            if Depth == 0:
              print (' =================================')
              ScanB = True
            ScanBus (PciObj.Cfg.SecondaryBus, Depth + 1)
        else:
            if ScanB == True and Depth == 0:
              print ()
            print (f'{"------+"*Depth} D {Bus:02X}:{Dev:02X}.{Func:X} ({PciObj.Hdr.VendorId:04X} {PciObj.Hdr.DeviceId:04X})')
            ScanB = False

if __name__ == '__main__':

  AcpiRaw = ExtractTable (b'MCFG', 0)
  AcpiObj, AcpiType = AcpiMcfgParser (AcpiRaw)
  PciCfgBase = AcpiObj.McfgDesc.BaseAddress

  ScanBus (0, 0)