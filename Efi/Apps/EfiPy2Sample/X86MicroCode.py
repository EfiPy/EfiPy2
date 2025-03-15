# X86MicroCode.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.Lib import CpuIdIntel as CpuId
from EfiPy2.Lib.X86Processor import Me
from EfiPy2.Lib.Msr import MSR_GENERIC_REGISTER
from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_BIOS_SIGN_ID, MSR_IA32_BIOS_SIGN_ID_REGISTER 

MsrReg = MSR_GENERIC_REGISTER ()
Me.WrMsr (MSR_IA32_BIOS_SIGN_ID, MsrReg)

CpuIdReg = CpuId.CPUID_GENERIC_REGISTERs ()
Me.CpuId (CpuId.CPUID_VERSION_INFO, 0x00, CpuIdReg)

Signature = MSR_IA32_BIOS_SIGN_ID_REGISTER ()
Me.RdMsr (MSR_IA32_BIOS_SIGN_ID, Signature)

print (f"Micro Code Signature: 0x{Signature.Bits.MicrocodeUpdateSignature:08X}")