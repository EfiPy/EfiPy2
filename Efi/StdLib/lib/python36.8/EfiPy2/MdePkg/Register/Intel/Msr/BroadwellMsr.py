# BroadwellMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.BroadwellMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_BROADWELL_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x3D and (
           DisplayModel == 0x47 or
           DisplayModel == 0x4F or
           DisplayModel == 0x56
           )

MSR_BROADWELL_IA32_PERF_GLOBAL_STATUS  = 0x0000038E

class MSR_BROADWELL_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0",        UINT32, 1),
    ("Ovf_PMC1",        UINT32, 1),
    ("Ovf_PMC2",        UINT32, 1),
    ("Ovf_PMC3",        UINT32, 1),
    ("Reserved1",       UINT32, 28),
    ("Ovf_FixedCtr0",   UINT32, 1),
    ("Ovf_FixedCtr1",   UINT32, 1),
    ("Ovf_FixedCtr2",   UINT32, 1),
    ("Reserved2",       UINT32, 20),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved3",       UINT32, 5),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_BROADWELL_IA32_PERF_GLOBAL_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_BROADWELL_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_BROADWELL_PKG_CST_CONFIG_CONTROL  = 0x000000E2

class MSR_BROADWELL_PKG_CST_CONFIG_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Limit",               UINT32, 4),
    ("Reserved1",           UINT32, 6),
    ("IO_MWAIT",            UINT32, 1),
    ("Reserved2",           UINT32, 4),
    ("CFGLock",             UINT32, 1),
    ("Reserved3",           UINT32, 9),
    ("C3AutoDemotion",      UINT32, 1),
    ("C1AutoDemotion",      UINT32, 1),
    ("C3Undemotion",        UINT32, 1),
    ("C1Undemotion",        UINT32, 1),
    ("CStateAutoDemotion",  UINT32, 1),
    ("CStateUndemotion",    UINT32, 1),
    ("Reserved4",           UINT32, 1),
    ("Reserved5",           UINT32, 32)
  ]

class MSR_BROADWELL_PKG_CST_CONFIG_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_BROADWELL_PKG_CST_CONFIG_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_BROADWELL_TURBO_RATIO_LIMIT  = 0x000001AD

class MSR_BROADWELL_TURBO_RATIO_LIMIT_REGISTER_Bits (Structure):
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

class MSR_BROADWELL_TURBO_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_BROADWELL_TURBO_RATIO_LIMIT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

MSR_BROADWELL_MSRUNCORE_RATIO_LIMIT  = 0x00000620

class MSR_BROADWELL_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("MAX_RATIO", UINT32, 7),
    ("Reserved2", UINT32, 1),
    ("MIN_RATIO", UINT32, 7),
    ("Reserved3", UINT32, 17),
    ("Reserved4", UINT32, 32)
  ]

class MSR_BROADWELL_MSRUNCORE_RATIO_LIMIT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_BROADWELL_MSRUNCORE_RATIO_LIMIT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

MSR_BROADWELL_PP0_ENERGY_STATUS  = 0x00000639

