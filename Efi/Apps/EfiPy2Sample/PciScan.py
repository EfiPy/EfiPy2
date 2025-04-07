# PciScan3.py
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com All rights reserved.
#
#   GPL-2.0
# 

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.IndustryStandard.Pci as pci
from EfiPy2.Lib.X86Processor import Me

def PciRegRead32 (Bus: int = 0, Dev: int = 0, Func: int = 0, Reg: int = 0) -> int:

  reg = pci.PCI_CONFIG_ACCESS_CF8((Reg & 0xFC, Func, Dev, Bus, 0, 1))

  ret = Me.IndexDatar32  (0xCF8, 0xCFC, reg.Uint32)

  return ret

class PCI_DEVICE_INDEPENDENT_REGION_UNION (pci.EFIPY_INDUSTRY_UNION):

  _fields_ = [
    ('Hdr',     pci.PCI_DEVICE_INDEPENDENT_REGION),
    ('Raw',     EfiPy.UINT32 * (EfiPy.sizeof (pci.PCI_DEVICE_INDEPENDENT_REGION) // (EfiPy.sizeof (EfiPy.UINT32)))),
    ('Raw16',   EfiPy.UINT16 * (EfiPy.sizeof (pci.PCI_DEVICE_INDEPENDENT_REGION) // (EfiPy.sizeof (EfiPy.UINT16)))),
  ]

if __name__ == '__main__':

  import pciids

  PciCfg = PCI_DEVICE_INDEPENDENT_REGION_UNION ()

  for Bus in range (pci.PCI_MAX_BUS + 1):
    for Dev in range (pci.PCI_MAX_DEVICE + 1):
      for Func in range (pci.PCI_MAX_FUNC + 1):

        PciCfg.Raw[0] = PciRegRead32(Bus, Dev, Func, 0)

        VendorId, DeviceId = PciCfg.Raw16 [:2]

        if VendorId == 0xFFFF and Func == 0:
          break

        if VendorId == 0xFFFF:
          continue

        for idx in range (4, EfiPy.sizeof (PCI_DEVICE_INDEPENDENT_REGION_UNION), 4):
          ret = PciRegRead32(Bus, Dev, Func, idx)
          PciCfg.Raw[idx // 4] = ret

        RevisionID                      = PciCfg.Hdr.RevisionID
        Interface, SubClass, BaseClass  = PciCfg.Hdr.ClassCode [:]

        DeviceClass, SubClassDict       = pciids.PciClass.get (BaseClass, (f"Class {BaseClass:02X}", {}))
        SubName, ProgIfDict             =    SubClassDict.get (SubClass,(f"SubClass {BaseClass:02X}", {}))
        ProgIfName                      =    ProgIfDict.get (Interface, f"ProgIf {Interface:02X}")
        VendorName, DeviceDict          = pciids.PciIds.get (VendorId, (f"Vendor {VendorId:04X}", {}))
        DeviceName, _                   =    DeviceDict.get (DeviceId, (f"Device {DeviceId:04X}", {}))

        print (f"{Bus:02X}:{Dev:02X}.{Func:X} {SubName}: {ProgIfName} ({BaseClass:X},{SubClass:X},{Interface:X}): {VendorName}: {DeviceName} ({VendorId:04X} {DeviceId:04X} rev: {RevisionID:02X})")

        if Func == 0 and not pci.IS_PCI_MULTI_FUNC (PciCfg):
          break
