# SmramMemoryReserve.py
#
# EfiPy2.MdePkg.Guid.SmramMemoryReserve
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *
from EfiPy2.MdePkg.Pi.PiMultiPhase  import EFI_SMRAM_DESCRIPTOR

gEfiSmmSmramMemoryGuid      = EFI_GUID( 0x6dadf1d1, 0xd4cc, 0x4910, (0xbb, 0x6e, 0x82, 0xb1, 0xfd, 0x80, 0xff, 0x3d ))

class EFI_SMRAM_HOB_DESCRIPTOR_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("NumberOfSmmReservedRegions",  UINT32),
    ("Descriptor",                  EFI_SMRAM_DESCRIPTOR * 1)
  ]

