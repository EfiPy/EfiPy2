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

import corepy.spre.spe as spe
import corepy.arch.x86.isa as x86
import corepy.arch.x86.isa.x86_fields as x86_fields
from corepy.arch.x86.lib.memory import MemoryReference


class x86_Nasm(object):
  """
  x86 NASM-compatible assembly syntax printer.

  Output syntax from this printer is designed to look like NASM (Intel) syntax
  assembly code.

    mov eax, 0xDEADBEEF
    sub eax, 0xBEEF
    mov 8(ebp), eax

  Several options are available for modifying the output (with defaults):
    show_prologue = True    Whether the prologue code should be printed
    show_epilogue = True    Whether the epilogue code should be printed
    function_name = ""      Optionally define the function name of the code
    verbose = False         Print extra comment information
  """

  def __init__(self, show_prologue = True, show_epilogue = True,
                     function_name = "", verbose = False):
    self.show_prologue = show_prologue
    self.show_epilogue = show_epilogue
    self.function_name = function_name
    self.verbose = verbose

    return

  def __del__(self):
    return

  def header(self, fd):
    if self.function_name != "":
      #print (".global %s\n%s:" % (self.function_name, self.function_name), file = fd)
      print ("BITS 32\nSECTION .text\nglobal %s\n%s:" % (self.function_name, self.function_name), file = fd)
    return

  def footer(self, fd):
    print ("resw 16384", file = fd)
    return

  def prologue(self, fd):
    """ Allow the module to print a prologue header if desired.
        The return value should be a boolean indicating whether prologue
        instructions should be printed. """
    #if self.show_prologue:
    #  print ("\nprologue:", file = fd)

    return self.show_prologue

  def epilogue(self, fd):
    """ Allow the module to print a prologue header if desired.
        The return value should be a boolean indicating whether epilogue
        instructions should be printed. """
    #if self.show_epilogue:
    #  print ("\nepilogue:", file = fd)

    return self.show_epilogue

  def body(self, fd):
    #print ("\nbody:", file = fd)
    return

  def str_op(self, op, op_sig, no_size_word = False):
    if isinstance(op, spe.Register):
      return op.name
    elif isinstance(op, spe.Variable):
      return op.reg.name
    elif isinstance(op, spe.Label):
      return op.name
    elif isinstance(op, MemoryReference):
      ref = ""
      if no_size_word == False:
        if op.data_size == 64:
          ref = "qword "
        elif op.data_size == 32:
          ref = "dword "
        elif op.data_size == 16:
          ref = "word "
        elif op.data_size == 8:
          ref = "byte "
        elif op.data_size == 80:
          ref = "tword "

      # [base + index * scale + disp]
    
      if op.base != None:
        if op.disp != None:
          if op.index != None:
            return ref + "[%s + %s * %d + %d]" % (op.base.name, op.index.name, op.scale, op.disp)
          return ref + "[%s + %d]" % (op.base.name, op.disp)
        elif op.index != None:
          return ref + "[%s + %s * %d]" % (op.base.name, op.index.name, op.scale)
        return ref + "[%s]" % (op.base.name)
      elif self.addr != None:
        return "[0x%x]" % (op.addr)
    elif isinstance(op, (long, int)):
      return str(op)
    return

  def instruction(self, fd, inst):
    no_size_word = hasattr(inst, "arch_ext")
    ops = zip(list(inst._supplied_operands), inst.machine_inst.signature, [no_size_word] * len(inst._supplied_operands))
    op_str = ', '.join([self.str_op(*op) for op in ops])
    # TODO - what to do about keywords?
    #for k, v in inst._supplied_koperands.items():
    #  op_str += ", %s = %s" % (str(k), str(v))

    name = inst.__class__.__name__.strip("_")
    print ("\t%s %s" % (name, op_str), file = fd)
    return

  def label(self, fd, lbl):
    print ("\n%s:" % lbl.name, file = fd)
    return


