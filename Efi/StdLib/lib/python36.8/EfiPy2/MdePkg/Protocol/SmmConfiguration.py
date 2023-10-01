# SmmConfiguration.py
#
# EfiPy2.MdePkg.Protocol.SmmConfiguration
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.MmConfiguration import gEfiMmConfigurationProtocolGuid

from EfiPy2.MdePkg.Pi.PiSmmCis              import EFI_SMM_ENTRY_POINT

gEfiSmmConfigurationProtocolGuid = gEfiMmConfigurationProtocolGuid

class EFI_SMM_RESERVED_SMRAM_REGION (Structure):
  _fields_ = [
    ("SmramReservedStart",  EFI_PHYSICAL_ADDRESS),
    ("SmramReservedSize",   UINT64)
  ]


class EFI_SMM_CONFIGURATION_PROTOCOL (Structure):
  pass

EFI_SMM_REGISTER_SMM_ENTRY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_CONFIGURATION_PROTOCOL),  # IN *This,
  EFI_SMM_ENTRY_POINT                       # IN SmmEntryPoint
  )

EFI_SMM_CONFIGURATION_PROTOCOL._fields_ = [
    ("SmramReservedRegions",    POINTER(EFI_SMM_RESERVED_SMRAM_REGION)),
    ("RegisterSmmEntry",        EFI_SMM_REGISTER_SMM_ENTRY)
  ]

