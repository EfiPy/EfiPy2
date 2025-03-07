# SvsmMsr.py
#
# EfiPy2.MdePkg.Register.Amd.SvsmMsr
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
# 
from EfiPy2  import *

MSR_SVSM_CAA  = 0xc001f000

class MSR_SVSM_CAA_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
  ("Lower32Bits",   UINT32),
  ("Upper32Bits",   UINT32)
  ]
class MSR_SVSM_CAA_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
  ("Bits",      MSR_SVSM_CAA_REGISTER_Bits),
  ("Uint64",    UINT64)
  ]

