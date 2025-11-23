# PciCfg2.py
#
# EfiPy2.MdePkg.Ppi.PciCfg2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPciCfg2PpiGuid            = \
  EFI_GUID (0x57a449a, 0x1fdc, 0x4c06, ( 0xbf, 0xc9, 0xf5, 0x3f, 0x6a, 0x99, 0xbb, 0x92 ))

class EFI_PEI_PCI_CFG2_PPI (Structure):
  pass

from EfiPy2.MdePkg.Pi.PiPeiCis import EFI_PEI_SERVICES

def EFI_PEI_PCI_CFG_ADDRESS(bus, dev, func, reg):
  if reg < 256:
   return (bus  << 24) | \
          (dev  << 16) | \
          (func << 8 ) | \
           reg

  return (bus  << 24) | \
         (dev  << 16) | \
         (func << 8 ) | \
          reg  << 32

EfiPeiPciCfgWidthUint8    = 0
EfiPeiPciCfgWidthUint16   = 1
EfiPeiPciCfgWidthUint32   = 2
EfiPeiPciCfgWidthUint64   = 3
EfiPeiPciCfgWidthMaximum  = 4
EFI_PEI_PCI_CFG_PPI_WIDTH = ENUM

class EFI_PEI_PCI_CFG_PPI_PCI_ADDRESS (Structure):
  _fields_ = [
    ("Register",            UINT8),
    ("Function",            UINT8),
    ("Device",              UINT8),
    ("Bus",                 UINT8),
    ("ExtendedRegister",    UINT32)
  ]

EFI_PEI_PCI_CFG2_PPI_IO = CFUNCTYPE (
  UINT8,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_PCI_CFG2_PPI),        # IN     CONST *This,
  EFI_PEI_PCI_CFG_PPI_WIDTH,            # IN           Width
  UINT64,                               # IN           Address
  PVOID                                 # IN OUT       *Buffer
  )

EFI_PEI_PCI_CFG2_PPI_RW = CFUNCTYPE (
  UINT8,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_PCI_CFG2_PPI),        # IN     CONST *This,
  EFI_PEI_PCI_CFG_PPI_WIDTH,            # IN           Width
  UINT64,                               # IN           Address
  PVOID,                                # IN           *SetBits
  PVOID                                 # IN           *ClearBits
  )

EFI_PEI_PCI_CFG2_PPI._fields_ = [
    ("Read",    EFI_PEI_PCI_CFG2_PPI_IO),
    ("Write",   EFI_PEI_PCI_CFG2_PPI_IO),
    ("Modify",  EFI_PEI_PCI_CFG2_PPI_RW),
    ("Segment", UINT16)
  ]

