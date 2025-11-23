# Xeon5600Msr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.Xeon5600Msr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_XEON_5600_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x06 and (
           DisplayModel == 0x25 or
           DisplayModel == 0x2C
           )

MSR_XEON_5600_FEATURE_CONFIG  = 0x0000013C

class MSR_XEON_5600_FEATURE_CONFIG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("AESConfiguration",    UINT32, 2),
    ("Reserved1",           UINT32, 30),
    ("Reserved2",           UINT32, 32)
  ]

class MSR_XEON_5600_FEATURE_CONFIG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_5600_FEATURE_CONFIG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_XEON_5600_OFFCORE_RSP_1     = 0x000001A7
MSR_XEON_5600_TURBO_RATIO_LIMIT = 0x000001AD

class MSR_XEON_5600_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Maximum1C",   UINT32, 8),
    ("Maximum2C",   UINT32, 8),
    ("Maximum3C",   UINT32, 8),
    ("Maximum4C",   UINT32, 8),
    ("Maximum5C",   UINT32, 8),
    ("Maximum6C",   UINT32, 8),
    ("Reserved",    UINT32, 16)
  ]

class MSR_XEON_5600_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_XEON_5600_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_XEON_5600_IA32_ENERGY_PERF_BIAS  = 0x000001B0
