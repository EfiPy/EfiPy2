# PciScan2.py
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

  Me.Iow32 (0xCF8, reg.Uint32)
  ret = Me.Ior32 (0xCFC)

  return ret

class PciDevUnion (pci.EFIPY_INDUSTRY_UNION):

  _fields_ = [
    ('PciReg',  pci.PCI_TYPE_GENERIC),
    ('PciRaw',  EfiPy.UINT32 * (EfiPy.sizeof (pci.PCI_TYPE_GENERIC) // (EfiPy.sizeof (EfiPy.UINT32))))
  ]

if __name__ == '__main__':

  PciData = PciDevUnion()
  _p = PciData.PciReg.Device

  for Bus in range (pci.PCI_MAX_BUS):
    for Dev in range (pci.PCI_MAX_DEVICE):
      for Func in range (pci.PCI_MAX_FUNC):

        PciData.PciRaw[0] = PciRegRead32(Bus, Dev, Func, 0)

        if _p.Hdr.VendorId == 0xFFFF and Func == 0:
          break

        if _p.Hdr.VendorId == 0xFFFF:
          continue

        for idx in range (4, EfiPy.sizeof (pci.PCI_TYPE_GENERIC), 4):
          ret = PciRegRead32(Bus, Dev, Func, idx)
          PciData.PciRaw[idx // 4] = ret

        print ("Bus: %d, Dev: %d, Func: %d" % (Bus, Dev, Func))
        print ("  VendorID: 0x%04X, DeviceID: 0x%04X" % (_p.Hdr.VendorId, _p.Hdr.DeviceId))

        if Func == 0 and not pci.IS_PCI_MULTI_FUNC (_p):
          break