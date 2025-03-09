# CpuId.py
#
# EfiPy2.Lib.CpuId
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.Register.Intel.Cpuid as CpuidRegs

CPUID_SIGNATURE = CpuidRegs.CPUID_SIGNATURE
class CPUID_GENERIC_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

CPUID_VERSION_INFO  = CpuidRegs.CPUID_VERSION_INFO
class CPUID_VERSION_INFO_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_VERSION_INFO_EAX),
    ('EBX',  CpuidRegs.CPUID_VERSION_INFO_EBX),
    ('ECX',  CpuidRegs.CPUID_VERSION_INFO_ECX),
    ('EDX',  CpuidRegs.CPUID_VERSION_INFO_EDX)
  ]
