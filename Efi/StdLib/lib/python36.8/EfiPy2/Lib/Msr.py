# Msr.py
#
# EfiPy2.Lib.Msr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

class MsrClass:
  def __init__ (self):

    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.platform as env
    import corepy.arch.x86_64.lib.memory as mem

    self.proc   = env.Processor()
    self.params = env.ExecParams()

    #
    # Read MSR procedure
    #
    self.rdmsr  = env.InstructionStream()
    self.rdmsr.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 16)))  # parameter 1
    self.rdmsr.add(x86.mov(reg.rdi, mem.MemRef(reg.rbp, 24)))  # parameter 2

    self.rdmsr.add(x86.rdmsr())

    self.rdmsr.add(x86.mov(mem.MemRef(reg.rdi,  0, data_size = 32), reg.eax))
    self.rdmsr.add(x86.mov(mem.MemRef(reg.rdi,  4, data_size = 32), reg.edx))

    #
    # Write MSR procedure
    #
    self.wrmsr  = env.InstructionStream()
    self.wrmsr.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 16)))  # parameter 1
    self.wrmsr.add(x86.mov(reg.rsi, mem.MemRef(reg.rbp, 24)))  # parameter 2

    self.wrmsr.add(x86.mov(reg.eax, mem.MemRef(reg.rsi, 0, data_size = 32)))
    self.wrmsr.add(x86.mov(reg.edx, mem.MemRef(reg.rsi, 4, data_size = 32)))

    self.wrmsr.add(x86.wrmsr())

  def Read (self, ecx, RetReg):

    RetAddr = EfiPy.addressof (RetReg)
    self.params.p1 = ecx
    self.params.p2 = RetAddr
    self.proc.execute(self.rdmsr, params = self.params, mode = 'int')

  def Write (self, ecx, RetReg):

    RetAddr = EfiPy.addressof (RetReg)
    self.params.p1 = ecx
    self.params.p2 = RetAddr
    self.proc.execute(self.wrmsr, params = self.params, mode = 'int')

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
