# MmConfiguration.py
#
# EfiPy2.MdePkg.Protocol.MmConfiguration
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_ENTRY_POINT
from EfiPy2.MdePkg.Pi.PiMultiPhase  import EFI_MM_RESERVED_MMRAM_REGION

gEfiMmConfigurationProtocolGuid = \
  EFI_GUID (0x26eeb3de, 0xb689, 0x492e, (0x80, 0xf0, 0xbe, 0x8b, 0xd7, 0xda, 0x4b, 0xa7 ))

class EFI_MM_CONFIGURATION_PROTOCOL (Structure):
  pass

EFI_MM_REGISTER_MM_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CONFIGURATION_PROTOCOL),   #   IN CONST  *This,
  EFI_MM_ENTRY_POINT                        #   IN        MmEntryPoint
  )

EFI_MM_CONFIGURATION_PROTOCOL._fields_ = [
    ("MmramReservedRegions",    POINTER(EFI_MM_RESERVED_MMRAM_REGION)),
    ("RegisterMmEntry",         EFI_MM_REGISTER_MM_ENTRY)
  ]

