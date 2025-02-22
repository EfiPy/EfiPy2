# CpuId2.py
#
# EfiPy2.Lib.CpuId
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.Register.Intel.Cpuid as CpuidRegs

from EfiPy2.Lib import CpuId
from EfiPy2.Lib.StructDump import DumpStruct

CpuIdObj  = CpuId.CpuIdClass()

#
# Get CPUID EAX = 0
#
CpuIdReg  = CpuId.CPUID_GENERIC_REGISTERs()
rax = CpuIdObj.GetId2 (0, 0, CpuIdReg)

print (f'''
CPU signature From cpuid instruction
====================================''')
DumpStruct (2, CpuIdReg, CpuId.CPUID_GENERIC_REGISTERs)

#
# Get CPUID EAX = 1
#
class CpuIdRegisters (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  CpuidRegs.CPUID_VERSION_INFO_EAX),
    ('EBX',  CpuidRegs.CPUID_VERSION_INFO_EBX),
    ('ECX',  CpuidRegs.CPUID_VERSION_INFO_ECX),
    ('EDX',  CpuidRegs.CPUID_VERSION_INFO_EDX)
  ]

CpuIdReg  = CpuIdRegisters()
rax = CpuIdObj.GetId2 (CpuidRegs.CPUID_VERSION_INFO, 0, CpuIdReg)

print (f'''
CPU version information
=======================''')
DumpStruct (2, CpuIdReg, CpuIdRegisters)