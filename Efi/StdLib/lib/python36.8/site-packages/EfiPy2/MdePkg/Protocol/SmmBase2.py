# SmmBase2.py
#
# EfiPy2.MdePkg.Protocol.SmmBase2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiSmmCis import EFI_SMM_SYSTEM_TABLE2

from EfiPy2.MdePkg.Protocol.MmBase import gEfiMmBaseProtocolGuid

gEfiSmmBase2ProtocolGuid = gEfiMmBaseProtocolGuid

class EFI_SMM_BASE2_PROTOCOL (Structure):
  pass

EFI_SMM_INSIDE_OUT2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_BASE2_PROTOCOL),  # IN  *This
  POINTER(BOOLEAN)                  # OUT *InSmram
  )

EFI_SMM_GET_SMST_LOCATION2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMM_BASE2_PROTOCOL),          # IN  *This
  POINTER(POINTER(EFI_SMM_SYSTEM_TABLE2))   # OUT **Smst
  )

EFI_SMM_BASE2_PROTOCOL._fields_ = [
    ("InSmm",           EFI_SMM_INSIDE_OUT2),
    ("GetSmstLocation", EFI_SMM_GET_SMST_LOCATION2)
  ]

