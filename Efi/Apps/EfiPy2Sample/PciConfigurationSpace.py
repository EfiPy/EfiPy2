# PciConfigurationSpace.py
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com All rights reserved.
#   GPL-2.0
#
# Reference from
#   1. https://github.com/torvalds/linux/blob/master/include/uapi/linux/pci_regs.h
#   2. https://github.com/reactos/reactos/blob/master/sdk/include/xdk/iotypes.h
#   3. https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/pcie/cap.h
#

import copy
import EfiPy2 as EfiPy
from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION
import EfiPy2.MdePkg.IndustryStandard.Pci as pci

from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable
from EfiPy2.Lib.Acpi.AcpiMcfgParser import AcpiMcfgParser

EFIPY_PCI_CAPABILITY_HT         = 0x08    # HyperTransport
EFIPY_PCI_CAPABILITY_DEBUG      = 0x0A    # Debug port
EFIPY_PCI_CAPABILITY_CCRC       = 0x0B    # CompactPCI Central Resource Control
EFIPY_PCI_CAPABILITY_ID_SSVID   = 0x0D

class EFIPY_PCI_CAPABILITY_SSVID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 pci.EFI_PCI_CAPABILITY_HDR),
    ("Reserved",            EfiPy.UINT16),
    ("VendorId",            EfiPy.UINT16),
    ("DeviceID",            EfiPy.UINT16),
    ]

EFIPY_PCI_CAPABILITY_AGP        = 0x0E    # AGP 8X
EFIPY_PCI_CAPABILITY_SECURE     = 0x0F    # Secure Device

EFIPY_PCI_CAPABILITY_ID_MSI_X   = 0x11

class EFIPY_PCI_CAPABILITY_MSI_X (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 pci.EFI_PCI_CAPABILITY_HDR),
    ("MessageControl",      EfiPy.UINT16),
    ("TableOffset",         EfiPy.UINT32),
    ("PbaOffset",           EfiPy.UINT32),
    ]

EFIPY_PCI_CAPABILITY_ID_SATA    = 0x12

class EFIPY_PCI_CAPABILITY_SATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 pci.EFI_PCI_CAPABILITY_HDR),

    ("MinorVersion",        EfiPy.UINT8, 4),
    ("MajorVersion",        EfiPy.UINT8, 4),
    ("Reserved1",           EfiPy.UINT8),

    ("BarLoc",              EfiPy.UINT32, 4),
    ("BarOfst",             EfiPy.UINT32, 20),
    ("Reserved2",           EfiPy.UINT32, 8),
    ]

EFIPY_PCI_CAPABILITY_ID_AF      = 0x13    # Advanced Features (AF)
EFIPY_PCI_CAPABILITY_ID_EA      = 0x14    # Enhanced Allocation
EFIPY_PCI_CAPABILITY_ID_FPB     = 0x15    # Flattening Portal Bridge

class PCI_DEVICE_INDEPENDENT_REGION_UNION (pci.EFIPY_INDUSTRY_UNION):

  _fields_ = [
    ('Hdr',     pci.PCI_DEVICE_INDEPENDENT_REGION),
    ('Raw',     EfiPy.UINT32 * (EfiPy.sizeof (pci.PCI_DEVICE_INDEPENDENT_REGION) // (EfiPy.sizeof (EfiPy.UINT32))))
  ]

def PciCapGetMsiStruct (CapId, PciRaw, CapPtr):
  TpmObj = pci.EFI_PCI_CAPABILITY_MSI32.from_buffer (PciRaw)
  if TpmObj.MsgCtrlReg & 0x08:
    return pci.EFI_PCI_CAPABILITY_MSI64
  return pci.EFI_PCI_CAPABILITY_MSI32

def PciCapGetVendorStruct (CapId, PciRaw, CapPtr):
  StructLength = PciRaw [CapPtr + 2]
  class EFIPY_PCI_CAPABILITY_VENDOR (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
    ("CapabilityID",  EfiPy.UINT8),
    ("NextItemPtr",   EfiPy.UINT8),
    ("Length",        EfiPy.UINT8),
    ("VendorRaw",     EfiPy.UINT8 * (StructLength - 3)),
    ]
  return EFIPY_PCI_CAPABILITY_VENDOR

def PciCapGetDefault (CapId, PciRaw, CapPtr):
  return pci.EFI_PCI_CAPABILITY_HDR

PciCapDict2 = {
  pci.EFI_PCI_CAPABILITY_ID_PMI:     lambda CapId, PciRaw, CapPtr: pci.EFI_PCI_CAPABILITY_PMI,        # 0x01
  pci.EFI_PCI_CAPABILITY_ID_AGP:     lambda CapId, PciRaw, CapPtr: pci.EFI_PCI_CAPABILITY_AGP,        # 0x02
  pci.EFI_PCI_CAPABILITY_ID_VPD:     lambda CapId, PciRaw, CapPtr: pci.EFI_PCI_CAPABILITY_VPD,        # 0x03
  pci.EFI_PCI_CAPABILITY_ID_SLOTID:  lambda CapId, PciRaw, CapPtr: pci.EFI_PCI_CAPABILITY_SLOTID,     # 0x04
  pci.EFI_PCI_CAPABILITY_ID_MSI:     PciCapGetMsiStruct,                                              # 0x05
  # pci.EFI_PCI_CAPABILITY_ID_HOTPLUG: None,                              # 0x06
  # pci.EFI_PCI_CAPABILITY_ID_PCIX:    None,                              # 0x07
  # EFIPY_PCI_CAPABILITY_HT: None,                                        # 0x08
  pci.EFI_PCI_CAPABILITY_ID_VENDOR:  PciCapGetVendorStruct,                                           # 0x09
  # EFIPY_PCI_CAPABILITY_DEBUG: None,                                     # 0x0A
  # EFIPY_PCI_CAPABILITY_CCRC: None,                                      # 0x0B
  # pci.EFI_PCI_CAPABILITY_ID_SHPC:    None,                              # 0x0C
  EFIPY_PCI_CAPABILITY_ID_SSVID:      lambda CapId, PciRaw, CapPtr: EFIPY_PCI_CAPABILITY_SSVID,       # 0x0D
  # EFIPY_PCI_CAPABILITY_AGP: None,                                       # 0x0E
  # EFIPY_PCI_CAPABILITY_SECURE: None,                                    # 0x0F
  pci.EFI_PCI_CAPABILITY_ID_PCIEXP:   lambda CapId, PciRaw, CapPtr: pci.PCI_CAPABILITY_PCIEXP,        # 0x10
  EFIPY_PCI_CAPABILITY_ID_MSI_X:      lambda CapId, PciRaw, CapPtr: EFIPY_PCI_CAPABILITY_MSI_X,       # 0x11
  EFIPY_PCI_CAPABILITY_ID_SATA:       lambda CapId, PciRaw, CapPtr: EFIPY_PCI_CAPABILITY_SATA,        # 0x12
  # EFIPY_PCI_CAPABILITY_ID_AF: None,                                     # 0x13
  # EFIPY_PCI_CAPABILITY_ID_EA: None,                                     # 0x14
  # EFIPY_PCI_CAPABILITY_ID_FPB: None,                                    # 0x15
}

def BuildPciCapabilitiesList (PciRaw, CapPtr: int) -> list:
    CapList = []
    while True:
      if CapPtr == 0:
        break

      CapId, CapNPtr = PciRaw[CapPtr: CapPtr + 2]
      CapList.append ((CapPtr, CapId, CapNPtr))
      CapPtr = CapNPtr
    return CapList

def BuildPciCapabilitiesFull (PciRaw, PciReserved, CapPtr: int) -> bool:

  IsPcieDevice = False

  if CapPtr == 0:
    return IsPcieDevice

  CapId, CapNPtr = PciRaw[CapPtr: CapPtr + 2]
  print (f'Cap ID: 0x{CapId:02X} (offset: 0x{CapPtr:02X}, next offset: 0x{CapNPtr:02X}), in EfiPy2 database: {CapId in PciCapDict2}')
  if pci.EFI_PCI_CAPABILITY_ID_PCIEXP == CapId:
    IsPcieDevice = True

  CapStruct = PciCapDict2.get (CapId, PciCapGetDefault) (CapId, PciRaw, CapPtr)
  for idx, (r, s) in enumerate (PciReserved):
    if CapPtr in r:
      NewCapSize  = EfiPy.sizeof (CapStruct)
      NewCapStop  = CapPtr + NewCapSize
      NewCapRange = range (CapPtr, NewCapStop)
      if NewCapRange == r:
        PciReserved[idx] = (r, CapStruct)
      elif NewCapRange.start == r.start:
        PciReserved[idx:idx+1] = [(NewCapRange, CapStruct),
                                  (range (NewCapStop, r.stop), EfiPy.UINT8 * (r.stop - NewCapStop))]
      elif NewCapRange.stop == r.stop:
        PciReserved[idx:idx+1] = [(range (r.start, CapPtr), EfiPy.UINT8 * (CapPtr - r.start)),
                                  (NewCapRange, CapStruct)]
      else:
        PciReserved[idx:idx+1] = [(range(r.start, CapPtr), EfiPy.UINT8 * (CapPtr - r.start)),
                                  (NewCapRange, CapStruct),
                                  (range (NewCapStop, r.stop), EfiPy.UINT8 * (r.stop - NewCapStop))]
      break
  IsPcieDevice |= BuildPciCapabilitiesFull (PciRaw, PciReserved, CapNPtr)
  return IsPcieDevice

def BuildPciHeader (EcamBase: int, EcamOffset: int):

  CapNameDict = {}

  def BuildCapName (CapName, CapNameDict):
    ShowIndex = CapNameDict.get (CapName, -1)
    CapNameDict [CapName] = ShowIndex + 1
    if ShowIndex == -1:
      return CapName
    return f'{CapName}{ShowIndex + 1}'


  PciCfgAddress = EcamBase + EcamOffset

  PciCfg = PCI_DEVICE_INDEPENDENT_REGION_UNION.from_address (PciCfgAddress)

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

  class PciUnion (EFIPY_INDUSTRY_UNION):
    _fields_ = [
        ('Fields',  PciStruct),
        ('Raw',     EfiPy.UINT8 * 0x100),
    ]

  PciCfg = PciUnion.from_address (PciCfgAddress)

  IsPcieDevice = False
  if PciCfg.Fields.Hdr.Status & pci.EFI_PCI_STATUS_CAPABILITY == pci.EFI_PCI_STATUS_CAPABILITY:

    PciRaw = (EfiPy.UINT8 * 0x100).from_address (PciCfgAddress)
    PciReserved = [(range(0x40, 0x100), EfiPy.UINT8 * 0xC0)]

    IsPcieDevice = BuildPciCapabilitiesFull (PciRaw, PciReserved, PciCfg.Fields.Cfg.CapabilityPtr)

    for idx, (r, s) in enumerate (PciReserved):

      if type(s).__name__ == 'PyCStructType':
        ShowName = BuildCapName (s.__name__, CapNameDict)
        PciTypeFields.append ((ShowName, s))
      else:
        ShowName = BuildCapName ('Reserved', CapNameDict)
        PciTypeFields.append ((ShowName, EfiPy.UINT8 * len(r)))

    class PciStruct (EFIPY_INDUSTRY_STRUCTURE):
      _fields_ = PciTypeFields

  else:
    PciTypeFields.append (('Reserved', EfiPy.UINT8 * (0x100 - EfiPy.sizeof (PciStruct))))

    class PciStruct (EFIPY_INDUSTRY_STRUCTURE):
      _fields_ = PciTypeFields

  class PciUnion (EFIPY_INDUSTRY_UNION):
    _fields_ = [
        ('Fields',  PciStruct),
        ('Raw',     EfiPy.UINT8 * 0x100),
    ]

  PciCfg = PciUnion.from_address (PciCfgAddress)

  return PciCfg, PciUnion, IsPcieDevice

if __name__ == '__main__':

  import argparse

  parser = argparse.ArgumentParser (prog = 'PciConfigurationSpace.py')
  ArgCommand = parser.add_subparsers (help = 'Dump PCI configuration space registers via MMIO.')
  parser.add_argument ('-v', '--verbose', action = 'store_true', help = 'Verbose output by Read/Dump MSR')
  args = parser.parse_args ()

  # if args.verbose == True:
  if True:
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump

  AcpiRaw = ExtractTable (b'MCFG', 0)
  AcpiObj, AcpiType = AcpiMcfgParser (AcpiRaw)

  Bus   = 0x0
  Dev   = 0x1F
  Func  = 0x02

  PciCfgOffset  = pci.PCI_ECAM_ADDRESS (Bus, Dev, Func, 0)
  PciCfgAddress = AcpiObj.McfgDesc.BaseAddress + PciCfgOffset

  PciObj, PciType, IsPcieDevice = BuildPciHeader (AcpiObj.McfgDesc.BaseAddress, PciCfgOffset)
  print (f"PCI{'e' if IsPcieDevice else ''} Base: 0x{AcpiObj.McfgDesc.BaseAddress:08X}, Device {Bus:02X}:{Dev:02X}.{Func:X} ECAM: 0x{PciCfgOffset:08X}")
  DumpStruct (0, PciObj, PciType)

  PciRaw = (EfiPy.UINT8 * 0x100).from_address (PciCfgAddress)
  if PciRaw [pci.PCI_PRIMARY_STATUS_OFFSET] & pci.EFI_PCI_STATUS_CAPABILITY == pci.EFI_PCI_STATUS_CAPABILITY:
    CapList = BuildPciCapabilitiesList (PciRaw, PciRaw [pci.PCI_CAPBILITY_POINTER_OFFSET])
    print ('\nPCI capabilities list...')
    for CapPtr, CapId, CapNPtr in CapList:
      print (f'0x{CapPtr:X} 0x{CapId:X} 0x{CapNPtr:X}')