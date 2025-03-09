# Msr.py
#
# EfiPy2.Lib.Msr
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

class MSR_GENERIC_REGISTER_Bits (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32, 32), # Low bytes
    ('EDX',  EfiPy.UINT32, 32)  # High bytes
  ]

class MSR_GENERIC_REGISTER (EfiPy.Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_GENERIC_REGISTER_Bits),
    ("Uint32",  EfiPy.UINT32 * 2),
    ("Uint64",  EfiPy.UINT64)
  ]
