# CpuId.py
#
# EfiPy2.Lib.CpuId
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

class CpuIdClass:

  def __init__ (self):

    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.platform as env
    import corepy.arch.x86_64.lib.memory as mem

    self.code   = env.InstructionStream()
    self.proc   = env.Processor()
    self.params = env.ExecParams()

    self.code.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 16)))  # parameter 1
    self.code.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 24)))  # parameter 2
    self.code.add(x86.mov(reg.rdi, mem.MemRef(reg.rbp, 32)))  # parameter 3

    self.code.add(x86.push(reg.rax))                          # save input parameter

    self.code.add(x86.cpuid())

    self.code.add(x86.mov(mem.MemRef(reg.rdi,  0, data_size = 32), reg.eax))
    self.code.add(x86.mov(mem.MemRef(reg.rdi,  4, data_size = 32), reg.ebx))
    self.code.add(x86.mov(mem.MemRef(reg.rdi,  8, data_size = 32), reg.ecx))
    self.code.add(x86.mov(mem.MemRef(reg.rdi, 12, data_size = 32), reg.edx))

    self.code.add(x86.pop(reg.rax))                           # restore input parameter as return value

  #
  # UINT32 GetId (UINT32 eax, UINT32 ecx, CpuIdRegisters *CpuIdRegAddr);
  #
  def GetId (self, eax, ecx, CpuIdRegAddr):

    self.params.p1 = eax
    self.params.p2 = ecx
    self.params.p3 = CpuIdRegAddr
    return self.proc.execute(self.code, params = self.params, mode = 'int')

  #
  # UINT32 GetId (UINT32 eax, UINT32 ecx, struct CpuIdReg &CpuIdReg);
  #
  def GetId2 (self, eax, ecx, CpuIdReg):

    CpuIdRegAddr = EfiPy.addressof (CpuIdReg)

    self.params.p1 = eax
    self.params.p2 = ecx
    self.params.p3 = CpuIdRegAddr
    return self.proc.execute(self.code, params = self.params, mode = 'int')

class CPUID_GENERIC_REGISTERs (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

if __name__ == '__main__':

  import EfiPy2.MdePkg.Register.Intel.Cpuid as CpuidRegs

  class CpuIdRegisters (EfiPy.Structure):
    _pack_   = 1
    _fields_ = [
      ('EAX',  CpuidRegs.CPUID_VERSION_INFO_EAX),
      ('EBX',  CpuidRegs.CPUID_VERSION_INFO_EBX),
      ('ECX',  CpuidRegs.CPUID_VERSION_INFO_ECX),
      ('EDX',  CpuidRegs.CPUID_VERSION_INFO_EDX)
    ]
  CpuIdReg  = CpuIdRegisters()
  CpuIdObj  = CpuIdClass()

  rax = CpuIdObj.GetId2(CpuidRegs.CPUID_VERSION_INFO, 0, CpuIdReg)
  

  print (f'''
  CPUID From instruction cpuid
  ============================================
    EAX = 0x{CpuIdReg.EAX.Uint32:08X}
    EBX = 0x{CpuIdReg.EBX.Uint32:08X}
    ECX = 0x{CpuIdReg.ECX.Uint32:08X}
    EDX = 0x{CpuIdReg.EDX.Uint32:08X}
  ''')
