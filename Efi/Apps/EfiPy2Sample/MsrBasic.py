# MsrBasic.py
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

from EfiPy2.Lib.Msr import MsrClass, MSR_GENERIC_REGISTER

def PrintCode (code):
  import corepy.lib.printer as printer

  printer.PrintInstructionStream(code, printer.x86_64_Nasm(show_epilogue = False, show_prologue = False))
  printer.PrintInstructionStream(code, printer.x86_64_Asm(show_epilogue = False, show_prologue = False))

if __name__ == '__main__':

  Msr = MsrClass()

  import os

  if os.name != 'edk2':
    PrintCode (Msr.wrmsr)
    exit (0)

  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_PLATFORM_ID_REGISTER, MSR_IA32_PLATFORM_ID

  Reg = MSR_IA32_PLATFORM_ID_REGISTER ()
  Msr.Read (MSR_IA32_PLATFORM_ID, Reg)

  print ('MSR_IA32_PLATFORM_ID 0x%08X' % MSR_IA32_PLATFORM_ID)
  print ('===========================================')
  print ('Reg.Uint64:           0x%016X' % Reg.Uint64)
  print ('Reg.Bits.Reserved1:   0x%X' % Reg.Bits.Reserved1)
  print ('Reg.Bits.Reserved2:   0x%X' % Reg.Bits.Reserved2)
  print ('Reg.Bits.PlatformId:  0x%X' % Reg.Bits.PlatformId)
  print ('Reg.Bits.Reserved3:   0x%X' % Reg.Bits.Reserved3)


  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_APIC_BASE_REGISTER, MSR_IA32_APIC_BASE

  Reg = MSR_IA32_APIC_BASE_REGISTER ()
  Msr.Read (MSR_IA32_APIC_BASE, Reg)

  print ()
  print ('MSR_IA32_APIC_BASE 0x%08X' % MSR_IA32_APIC_BASE)
  print ('===========================================')
  print ('Reg.Uint64:           0x%016X' % Reg.Uint64)
  print ('Reg.Bits.BSP:         0x%X' % Reg.Bits.BSP)
  print ('Reg.Bits.EXTD:        0x%X' % Reg.Bits.EXTD)
  print ('Reg.Bits.EN:          0x%X' % Reg.Bits.EN)
  print ('Reg.Bits.ApicBase:    0x%X' % Reg.Bits.ApicBase)
  print ('Reg.Bits.ApicBaseHi:  0x%X' % Reg.Bits.ApicBaseHi)
  ApicBase = (Reg.Bits.ApicBaseHi << 20) | Reg.Bits.ApicBase
  print ('ApicBase:             0x%X' % ApicBase)

  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_SYSENTER_CS, MSR_IA32_SYSENTER_CS_REGISTER

  Reg = MSR_IA32_SYSENTER_CS_REGISTER ()
  Reg.Bits.CS = 0x4000
  Msr.Write (MSR_IA32_SYSENTER_CS, Reg)

  Reg.Uint64 = 0x0
  Msr.Read (MSR_IA32_SYSENTER_CS, Reg)

  print ()
  print ('MSR_IA32_SYSENTER_CS 0x%08X' % MSR_IA32_SYSENTER_CS)
  print ('===========================================')
  print ('Reg.Uint64:           0x%016X' % Reg.Uint64)
  print ('Reg.Bits.CS:          0x%X' % Reg.Bits.CS)
  print ('Reg.Bits.Reserved1:   0x%X' % Reg.Bits.Reserved1)
  print ('Reg.Bits.Reserved2:   0x%X' % Reg.Bits.Reserved2)

  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_SYSENTER_ESP

  Reg = MSR_GENERIC_REGISTER ()
  Reg.Bits.EAX = 0x4000
  Msr.Write (MSR_IA32_SYSENTER_ESP, Reg)

  Reg.Uint64 = 0x0
  Msr.Read (MSR_IA32_SYSENTER_ESP, Reg)

  print ()
  print ('MSR_IA32_SYSENTER_ESP 0x%08X' % MSR_IA32_SYSENTER_ESP)
  print ('===========================================')
  print ('Reg.Uint64:           0x%016X' % Reg.Uint64)
  print ('Reg.Bits.EAX:         0x%08X' % Reg.Bits.EAX)
