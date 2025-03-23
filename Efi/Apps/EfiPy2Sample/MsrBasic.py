# CpuId.py
#
# EfiPy2.Lib.CpuId
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.Lib.Msr import MSR_GENERIC_REGISTER
from EfiPy2.Lib.X86Processor import Me

if __name__ == '__main__':

  Reg = MSR_GENERIC_REGISTER ()
  Me.RdMsr (0x17, Reg)

  print ('MsrReg.Uint64:   0x%016X' % Reg.Uint64)
  print ('MsrReg.Bits.EAX: 0x%08X'  % Reg.Bits.EAX)
  print ('MsrReg.Bits.EDX: 0x%08X'  % Reg.Bits.EDX)

  print ()
  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_PLATFORM_ID_REGISTER, MSR_IA32_PLATFORM_ID

  Reg = MSR_IA32_PLATFORM_ID_REGISTER ()
  Me.RdMsr (MSR_IA32_PLATFORM_ID, Reg)

  print ('Reg.Uint64:           0x%016X' % Reg.Uint64)
  print ('Reg.Bits.Reserved1:   0x%X' % Reg.Bits.Reserved1)
  print ('Reg.Bits.Reserved2:   0x%X' % Reg.Bits.Reserved2)
  print ('Reg.Bits.PlatformId:  0x%X' % Reg.Bits.PlatformId)
  print ('Reg.Bits.Reserved3:   0x%X' % Reg.Bits.Reserved3)

  print ()
  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_APIC_BASE_REGISTER, MSR_IA32_APIC_BASE

  Reg = MSR_IA32_APIC_BASE_REGISTER ()
  Me.RdMsr (MSR_IA32_APIC_BASE, Reg)

  print ('Reg.Uint64:           0x%016X' % Reg.Uint64)
  print ('Reg.Bits.BSP:         0x%X' % Reg.Bits.BSP)
  print ('Reg.Bits.EXTD:        0x%X' % Reg.Bits.EXTD)
  print ('Reg.Bits.EN:          0x%X' % Reg.Bits.EN)
  print ('Reg.Bits.ApicBase:    0x%X' % Reg.Bits.ApicBase)
  print ('Reg.Bits.ApicBaseHi:  0x%X' % Reg.Bits.ApicBaseHi)
  ApicBase = (Reg.Bits.ApicBaseHi << 20) | Reg.Bits.ApicBase
  print ('ApicBase:             0x%X' % ApicBase)
