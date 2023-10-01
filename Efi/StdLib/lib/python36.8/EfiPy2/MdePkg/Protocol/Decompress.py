# Decompress.py
#
# EfiPy2.MdePkg.Protocol.Decompress
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDecompressProtocolGuid    = \
  EFI_GUID (0xd8117cfe, 0x94a6, 0x11d4, (0x9a, 0x3a, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_DECOMPRESS_PROTOCOL (Structure):
  pass

EFI_DECOMPRESS_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DECOMPRESS_PROTOCOL),   # IN      *This
  PVOID,                              # IN      *Source,
  UINT32,                             # IN      SourceSize
  POINTER(UINT32),                    #    OUT  *DestinationSize,
  POINTER(UINT32)                     #    OUT  *ScratchSize
  )

EFI_DECOMPRESS_DECOMPRESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DECOMPRESS_PROTOCOL),   # IN      *This
  PVOID,                              # IN      *Source,
  UINT32,                             # IN      SourceSize
  PVOID,                              # IN OUT  *Destination,
  UINT32,                             # IN      DestinationSize
  PVOID,                              # IN OUT  *Scratch,
  UINT32                              # IN      ScratchSize
  )

EFI_DECOMPRESS_PROTOCOL._fields_ = [
    ("GetInfo",     EFI_DECOMPRESS_GET_INFO),
    ("Decompress",  EFI_DECOMPRESS_DECOMPRESS)
  ]

