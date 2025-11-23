# MmCpuIo.py
#
# EfiPy2.MdePkg.Protocol.MmCpuIo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiMmCpuIoProtocolGuid      = EFI_GUID( 0x3242A9D8, 0xCE70, 0x4AA0, ( 0x95, 0x5D, 0x5E, 0x7B, 0x14, 0x0D, 0xE4, 0xD2 ))

class EFI_MM_CPU_IO_PROTOCOL (Structure):
  pass

MM_IO_UINT8  = 0
MM_IO_UINT16 = 1
MM_IO_UINT32 = 2
MM_IO_UINT64 = 3
EFI_MM_IO_WIDTH = ENUM

EFI_MM_CPU_IO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CPU_IO_PROTOCOL),  # IN     CONST *This,
  EFI_MM_IO_WIDTH,                  # IN           Width,
  UINT64,                           # IN           Address,
  UINTN,                            # IN           Count,
  PVOID                             # IN OUT       *Buffer
  )

class EFI_MM_IO_ACCESS (Structure):
  _fields_ = [
    ("Read",    EFI_MM_CPU_IO),
    ("Write",   EFI_MM_CPU_IO)
  ]

EFI_MM_CPU_IO_PROTOCOL._fields_ = [
    ("Mem", EFI_MM_IO_ACCESS),
    ("Io",  EFI_MM_IO_ACCESS)
  ]

