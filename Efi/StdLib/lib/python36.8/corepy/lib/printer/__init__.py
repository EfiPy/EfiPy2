# Copyright (c) 2006-2008 The Trustees of Indiana University.                   
# All rights reserved.                                                          
#                                                                               
# Redistribution and use in source and binary forms, with or without            
# modification, are permitted provided that the following conditions are met:   
#                                                                               
# - Redistributions of source code must retain the above copyright notice, this 
#   list of conditions and the following disclaimer.                            
#                                                                               
# - Redistributions in binary form must reproduce the above copyright notice,   
#   this list of conditions and the following disclaimer in the documentation   
#   and/or other materials provided with the distribution.                      
#                                                                               
# - Neither the Indiana University nor the names of its contributors may be used
#   to endorse or promote products derived from this software without specific  
#   prior written permission.                                                   
#                                                                               
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"   
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE     
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE   
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL    
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER    
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.          

import sys
import corepy.spre.spe as spe

from corepy.lib.printer.default import Default
from corepy.lib.printer.spu_asm import SPU_Asm
from corepy.lib.printer.x86_64_asm import x86_64_Asm
from corepy.lib.printer.x86_64_nasm import x86_64_Nasm
from corepy.lib.printer.x86_nasm import x86_Nasm


def PrintInstructionStream(code, module, fd = sys.stdout):
  code.cache_code()

  module.header(fd)
  if code._prologue != None and module.prologue(fd):
    for obj in code._prologue:
      if isinstance(obj, spe.Instruction):
        module.instruction(fd, obj)
      elif isinstance(obj, spe.Label):
        module.label(fd, obj)
      else:
        raise Exception("Unknown object in instruction stream: %s" % str(obj))
 
  module.body(fd) 
  for obj in code:
    if isinstance(obj, spe.Instruction):
      module.instruction(fd, obj)
    elif isinstance(obj, spe.Label):
      module.label(fd, obj)
    else:
      raise Exception("Unknown object in instruction stream: %s" % str(obj))

  if code._epilogue != None and module.epilogue(fd):
    for obj in code._epilogue:
      if isinstance(obj, spe.Instruction):
        module.instruction(fd, obj)
      elif isinstance(obj, spe.Label):
        module.label(fd, obj)
      else:
        raise Exception("Unknown object in instruction stream: %s" % str(obj))

  return

if __name__ == '__main__':
  #import corepy.arch.spu.platform as env
  #import corepy.arch.spu.isa as spu
  #import corepy.arch.spu.lib.dma as dma

  #code = env.InstructionStream()
  #reg = code.acquire_register()
  #code.add(spu.ilhu(reg, 0xDEAD))
  #code.add(spu.iohl(reg, 0xBEEF))
  #code.add(spu.stqd(reg, code.r_zero, 1, foo = 12))

  #dma.mem_get(code, 0x1000, 0xDEADBEEF, 16, 12)
  #code.add(spu.nop(0))
  #dma.mem_complete(code, 12)

  #code.add(spu.lnop())

  # should this be done in printis?
  #code.cache_code()
  #code.print_code(pro = True, epi = True)

  #PrintInstructionStream(code, Default(show_prologue = True, show_epilogue = True, line_numbers = True, show_hex = True))
  #PrintInstructionStream(code, Default())
  #PrintInstructionStream(code, SPU_Asm(comment_chan = True))

  import corepy.arch.x86_64.platform as env
  import corepy.arch.x86_64.isa as x86
  import corepy.arch.x86_64.types.registers as regs
  import corepy.arch.x86_64.lib.memory as mem

  code = env.InstructionStream()
  code.add(x86.mov(regs.rax, 0xDEADBEEF))
  code.add(x86.add(regs.rax, 0xDEADBEEF))
  code.add(x86.call(-6))
  code.add(x86.div(mem.MemRef(regs.r8, 1048576, regs.r13, 4, data_size = 16, addr_size = 32)))
  code.add(x86.sub(regs.rax, 0xBEEF))
  code.add(x86.mov(regs.rax, mem.MemRef(regs.rbp, 8)))

  code.cache_code()
  PrintInstructionStream(code, Default(show_hex = True))
  PrintInstructionStream(code, x86_64_Nasm(function_name="foobar"))

