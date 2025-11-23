# CpuIo.py
#
# EfiPy2.MdePkg.Ppi.CpuIo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPeiCpuIoPpiInstalledGuid            = \
  EFI_GUID (0xe6af1f7b, 0xfc3f, 0x46da, (0xa8, 0x28, 0xa3, 0xb4, 0x57, 0xa4, 0x42, 0x82 ))

class EFI_PEI_CPU_IO_PPI (Structure):
  pass

from EfiPy2.MdePkg.Pi.PiPeiCis import EFI_PEI_SERVICES

EfiPeiCpuIoWidthUint8       = 0 
EfiPeiCpuIoWidthUint16      = 1 
EfiPeiCpuIoWidthUint32      = 2 
EfiPeiCpuIoWidthUint64      = 3 
EfiPeiCpuIoWidthFifoUint8   = 4 
EfiPeiCpuIoWidthFifoUint16  = 5 
EfiPeiCpuIoWidthFifoUint32  = 6 
EfiPeiCpuIoWidthFifoUint64  = 7 
EfiPeiCpuIoWidthFillUint8   = 8 
EfiPeiCpuIoWidthFillUint16  = 9 
EfiPeiCpuIoWidthFillUint32  = 10
EfiPeiCpuIoWidthFillUint64  = 11
EfiPeiCpuIoWidthMaximum     = 12
EFI_PEI_CPU_IO_PPI_WIDTH    = ENUM

EFI_PEI_CPU_IO_PPI_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  EFI_PEI_CPU_IO_PPI_WIDTH,             # IN           Width,
  UINT64,                               # IN           Address,
  UINTN,                                # IN           Count,
  PVOID                                 # IN OUT       *Buffer
  )

class EFI_PEI_CPU_IO_PPI_ACCESS (Structure):
  _fields_ = [
    ("Read",    EFI_PEI_CPU_IO_PPI_IO_MEM),
    ("Write",   EFI_PEI_CPU_IO_PPI_IO_MEM)
  ]

EFI_PEI_CPU_IO_PPI_IO_READ8 = CFUNCTYPE (
  UINT8,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_IO_READ16 = CFUNCTYPE (
  UINT16,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_IO_READ32 = CFUNCTYPE (
  UINT32,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_IO_READ64 = CFUNCTYPE (
  UINT64,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_IO_WRITE8 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT8                                 # IN           Data
  )

EFI_PEI_CPU_IO_PPI_IO_WRITE16 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT16                                # IN           Data
  )

EFI_PEI_CPU_IO_PPI_IO_WRITE32 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT32                                # IN           Data
  )

EFI_PEI_CPU_IO_PPI_IO_WRITE64 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT64                                # IN           Data
  )

EFI_PEI_CPU_IO_PPI_MEM_READ8 = CFUNCTYPE (
  UINT8,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_MEM_READ16 = CFUNCTYPE (
  UINT16,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_MEM_READ32 = CFUNCTYPE (
  UINT32,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_MEM_READ64 = CFUNCTYPE (
  UINT64,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64                                # IN           Address
  )

EFI_PEI_CPU_IO_PPI_MEM_WRITE8 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT8                                 # IN           Data
  )

EFI_PEI_CPU_IO_PPI_MEM_WRITE16 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT16                                # IN           Data
  )

EFI_PEI_CPU_IO_PPI_MEM_WRITE32 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT32                                # IN           Data
  )

EFI_PEI_CPU_IO_PPI_MEM_WRITE64 = CFUNCTYPE (
  None,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_CPU_IO_PPI),          # IN     CONST *This,
  UINT64,                               # IN           Address
  UINT64                                # IN           Data
  )

EFI_PEI_CPU_IO_PPI_fields_ = [
    ("Mem",         EFI_PEI_CPU_IO_PPI_ACCESS),
    ("Io",          EFI_PEI_CPU_IO_PPI_ACCESS),
    ("IoRead8",     EFI_PEI_CPU_IO_PPI_IO_READ8),
    ("IoRead16",    EFI_PEI_CPU_IO_PPI_IO_READ16),
    ("IoRead32",    EFI_PEI_CPU_IO_PPI_IO_READ32),
    ("IoRead64",    EFI_PEI_CPU_IO_PPI_IO_READ64),
    ("IoWrite8",    EFI_PEI_CPU_IO_PPI_IO_WRITE8),
    ("IoWrite16",   EFI_PEI_CPU_IO_PPI_IO_WRITE16),
    ("IoWrite32",   EFI_PEI_CPU_IO_PPI_IO_WRITE32),
    ("IoWrite64",   EFI_PEI_CPU_IO_PPI_IO_WRITE64),
    ("MemRead8",    EFI_PEI_CPU_IO_PPI_MEM_READ8),
    ("MemRead16",   EFI_PEI_CPU_IO_PPI_MEM_READ16),
    ("MemRead32",   EFI_PEI_CPU_IO_PPI_MEM_READ32),
    ("MemRead64",   EFI_PEI_CPU_IO_PPI_MEM_READ64),
    ("MemWrite8",   EFI_PEI_CPU_IO_PPI_MEM_WRITE8),
    ("MemWrite16",  EFI_PEI_CPU_IO_PPI_MEM_WRITE16),
    ("MemWrite32",  EFI_PEI_CPU_IO_PPI_MEM_WRITE32),
    ("MemWrite64",  EFI_PEI_CPU_IO_PPI_MEM_WRITE64)
  ]

