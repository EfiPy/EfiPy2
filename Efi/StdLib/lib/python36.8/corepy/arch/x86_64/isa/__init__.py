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

from corepy.arch.x86_64.isa.x86_64_isa import *


# Nothing to see here, move along... ;)
__active_code = None

def set_active_code(code):
  global __active_code

  if __active_code is not None:
    __active_code.set_active_callback(None)

  __active_code = code

  if code is not None:
    code.set_active_callback(set_active_code)
  return

# Property version
def __get_active_code(self):
  global __active_code
  return __active_code

# Free function version
def get_active_code():
  global __active_code
  return __active_code

# _x86_active_code_prop = property(get_active_code)

# Build the instructions
#members = {}
#for inst in x86_isa.X86_ISA:
#  name = inst[0]
#  machine_inst = getattr(machine, name)
  
#  members['asm_order'] = None
#  members['machine_inst'] =  machine_inst
#  members['active_code']  = property(__get_active_code) # _x86_active_code_prop
#  globals()[name] = type(name, (spe.Instruction,), members)

for l in list (locals().values()):
  if isinstance(l, type):
    if issubclass(l, x86Instruction) or issubclass(l, x86DispatchInstruction):
      l.active_code = property(__get_active_code)

                                                       
# ------------------------------
# Mnemonics
# ------------------------------

# TODO: Find a better place for these...
def Illegal(): return 0;

