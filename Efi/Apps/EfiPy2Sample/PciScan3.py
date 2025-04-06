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
    ('Raw',     EfiPy.UINT32 * (EfiPy.sizeof (pci.PCI_DEVICE_INDEPENDENT_REGION) // (EfiPy.sizeof (EfiPy.UINT32))))
  ]

if __name__ == '__main__':

  import argparse

  parser = argparse.ArgumentParser (prog = 'PciScan.py')
  ArgCommand = parser.add_subparsers (help = 'Scanning PCI device via IO space 0xCF8/0xCFC.')
  parser.add_argument ('-v', '--verbose', action = 'store_true', help = 'Verbose output PCI_DEVICE_INDEPENDENT_REGION')
  args = parser.parse_args ()

  if args.verbose == True:
    from EfiPy2.Lib.StructDump import DumpStruct

  PciCfg = PCI_DEVICE_INDEPENDENT_REGION_UNION ()

  for Bus in range (pci.PCI_MAX_BUS):
    for Dev in range (pci.PCI_MAX_DEVICE):
      for Func in range (pci.PCI_MAX_FUNC):

        PciCfg.Raw[0] = PciRegRead32(Bus, Dev, Func, 0)

        if PciCfg.Hdr.VendorId == 0xFFFF and Func == 0:
          break

        if PciCfg.Hdr.VendorId == 0xFFFF:
          continue

        print ("Bus: %d, Dev: %d, Func: %d" % (Bus, Dev, Func))
        for idx in range (4, EfiPy.sizeof (PCI_DEVICE_INDEPENDENT_REGION_UNION), 4):
          ret = PciRegRead32(Bus, Dev, Func, idx)
          PciCfg.Raw[idx // 4] = ret
        if args.verbose == True:
          DumpStruct (2, PciCfg.Hdr, pci.PCI_DEVICE_INDEPENDENT_REGION)
        else:
          print ("  VendorID: 0x%04X, DeviceID: 0x%04X" % (PciCfg.Hdr.VendorId, PciCfg.Hdr.DeviceId))

        if Func == 0 and not pci.IS_PCI_MULTI_FUNC (PciCfg):
          break
