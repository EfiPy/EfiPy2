# CpuId2.py
#
# EfiPy2.Lib.CpuId
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.Lib import CpuId
from EfiPy2.Lib.X86Processor import Me
from EfiPy2.Lib.StructDump import DumpStruct

#
# Get CPUID EAX = 0, CpuId.CPUID_SIGNATURE
#
CpuIdReg  = CpuId.CPUID_GENERIC_REGISTERs()
Me.CpuId (CpuId.CPUID_SIGNATURE, 0x00, CpuIdReg)

print (f'''
CPU signature From cpuid instruction
====================================''')
DumpStruct (2, CpuIdReg, CpuId.CPUID_GENERIC_REGISTERs)

#
# Get CPUID EAX = 1 # CpuId.CPUID_VERSION_INFO
#
CpuIdReg  = CpuId.CPUID_VERSION_INFO_REGISTERs()
Me.CpuId (CpuId.CPUID_VERSION_INFO, 0x00, CpuIdReg)

print (f'''
CPU version information
=======================''')
DumpStruct (2, CpuIdReg, CpuId.CPUID_VERSION_INFO_REGISTERs)