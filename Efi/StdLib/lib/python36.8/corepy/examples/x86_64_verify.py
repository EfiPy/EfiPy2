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

import array

import corepy.arch.x86_64.isa as x86
from corepy.arch.x86_64.types.registers import *

import corepy.arch.x86_64.platform as env
from corepy.arch.x86_64.lib.memory import MemRef

def verify(inst, b):
  a = inst.render()

  print inst
  for n in a:
    print "%02X" % n,
  print

  if len(a) != len(b):
    for n in b:
      print "%02X" % n,
    print "  ERROR"
    return

  for (x, y) in zip(a, b):
    if x != y:
      for n in b:
        print "%02X" % n,
      print "  ERROR"
      return
  return


def Test():
  verify(x86.xor(ebx, eax),                 [0x31, 0xC3])
  verify(x86.add(ebx, ebx),                 [0x01, 0xdb])
  verify(x86.add(ebx, r13d),                [0x44, 0x01, 0xeb])
  verify(x86.add(r13d, ebx),                [0x41, 0x01, 0xdd])
  verify(x86.xor(rax, r15),                 [0x4c, 0x31, 0xf8])
  verify(x86.xor(r15, rax),                 [0x49, 0x31, 0xc7])
  verify(x86.xor(r13, r13),                 [0x4d, 0x31, 0xed])
  verify(x86.mov(rax, 0xDEADDEADBEEFl),     [0x48, 0xb8, 0xef, 0xbe, 0xad, 0xde, 0xad, 0xde, 0x00, 0x00])
  verify(x86.mov(r11, 0xDEADDEADBEEFl),     [0x49, 0xbb, 0xef, 0xbe, 0xad, 0xde, 0xad, 0xde, 0x00, 0x00])
  verify(x86.mov(r12, 0xDEADDEADBEEFl),     [0x49, 0xbc, 0xef, 0xbe, 0xad, 0xde, 0xad, 0xde, 0x00, 0x00])
  verify(x86.mov(r13, 0xDEADDEADBEEFl),     [0x49, 0xbd, 0xef, 0xbe, 0xad, 0xde, 0xad, 0xde, 0x00, 0x00])
  verify(x86.mov(r14, 0xDEADDEADBEEFl),     [0x49, 0xbe, 0xef, 0xbe, 0xad, 0xde, 0xad, 0xde, 0x00, 0x00])
  verify(x86.mov(r15, 0xDEADDEADBEEFl),     [0x49, 0xbf, 0xef, 0xbe, 0xad, 0xde, 0xad, 0xde, 0x00, 0x00])
  verify(x86.add(r15, 0xBEEF),              [0x49, 0x81, 0xc7, 0xef, 0xbe, 0x00, 0x00])
  verify(x86.add(r8, 0xA),                  [0x49, 0x83, 0xc0, 0x0a])
  verify(x86.mov(r8, MemRef(rbx, 3)),       [0x4c, 0x8b, 0x43, 0x03])
  verify(x86.mov(rax, MemRef(r9, 3)),       [0x49, 0x8b, 0x41, 0x03])
  verify(x86.mov(rcx, MemRef(rsp)),         [0x48, 0x8b, 0x0c, 0x24])
  verify(x86.mov(rbx, MemRef(rsp)),         [0x48, 0x8b, 0x1c, 0x24])
  verify(x86.mov(rdx, MemRef(rbp, 64)),     [0x48, 0x8b, 0x55, 0x40])
  verify(x86.mov(rdi, MemRef(rbp)),         [0x48, 0x8b, 0x7d, 0x00])
  verify(x86.mov(rdx, MemRef(rax, 64, r10, 4)), [0x4a, 0x8b, 0x54, 0x90, 0x40])
  verify(x86.mov(rdx, MemRef(r14, 24, rbx, 2)), [0x49, 0x8b, 0x54, 0x5e, 0x18])
  verify(x86.add(MemRef(rsp), 16),          [0x48, 0x83, 0x04, 0x24, 0x10])
  verify(x86.add(MemRef(rsp), r15),         [0x4c, 0x01, 0x3c, 0x24])
  verify(x86.call(MemRef(r12)),             [0x41, 0xff, 0x14, 0x24])
  verify(x86.cmpxchg8b(MemRef(rax)),        [0x0f, 0xc7, 0x08])
  verify(x86.cmpxchg8b(MemRef(r8)),         [0x41, 0x0f, 0xc7, 0x08])
  verify(x86.cmpxchg16b(MemRef(rax, data_size = 128)), [0x48, 0x0f, 0xc7, 0x08])
  verify(x86.cmpxchg16b(MemRef(r8, data_size = 128)), [0x49, 0x0f, 0xc7, 0x08])
  verify(x86.add(MemRef(rbp), 5),           [0x48, 0x83, 0x45, 0x00, 0x05])
  verify(x86.add(MemRef(rbp), 0x1EADBEEF),  [0x48, 0x81, 0x45, 0x00, 0xef, 0xbe, 0xad, 0x1e])
  verify(x86.call(MemRef(rdx)),             [0xff, 0x12])
  verify(x86.dec(rax),                      [0x48, 0xff, 0xc8])
  verify(x86.dec(MemRef(rax)),              [0x48, 0xff, 0x08])
  verify(x86.dec(MemRef(r15)),              [0x49, 0xff, 0x0f])
  verify(x86.div(rax),                      [0x48, 0xf7, 0xf0])
  verify(x86.div(r13),                      [0x49, 0xf7, 0xf5])
  verify(x86.div(MemRef(rax)),              [0x48, 0xf7, 0x30])
  verify(x86.div(MemRef(r13)),              [0x49, 0xf7, 0x75, 0x00])
  verify(x86.jmp(rax),                      [0x48, 0xff, 0xe0])
  verify(x86.jmp(MemRef(r13)),              [0x41, 0xff, 0x65, 0x00])
  verify(x86.jmp(MemRef(rax)),              [0xff, 0x20])
  verify(x86.lea(rdx, MemRef(r14, 24, rbx, 2, data_size = None)), [0x49, 0x8d, 0x54, 0x5e, 0x18])
  verify(x86.loop(-4),                      [0xe2, 0xfc])
  verify(x86.mov(r13, -0x1EADBEEFDEADBEEF), [0x49, 0xbd, 0x11, 0x41, 0x52, 0x21, 0x10, 0x41, 0x52, 0xe1])
  verify(x86.shld(rax, r15, cl),            [0x4c, 0x0f, 0xa5, 0xf8])
  # verify(x86.movd(xmm8, r15),               [0x66, 0x4d, 0x0f, 0x6e, 0xc7])
  verify(x86.addpd(xmm11, xmm10),           [0x66, 0x45, 0x0f, 0x58, 0xda])
  verify(x86.addpd(xmm11, MemRef(rdx, data_size = 128)), [0x66, 0x44, 0x0f, 0x58, 0x1a])
  verify(x86.cmpxchg8b(MemRef(eax)),        [0x67, 0x0f, 0xc7, 0x08])
  verify(x86.mov(r8, MemRef(ebx, 3)),       [0x67, 0x4c, 0x8b, 0x43, 0x03])
  verify(x86.mov(rax, MemRef(r9d, 3)),      [0x67, 0x49, 0x8b, 0x41, 0x03])
  verify(x86.mov(rdx, MemRef(ebp, 64)),     [0x67, 0x48, 0x8b, 0x55, 0x40])
  verify(x86.mov(rdx, MemRef(eax, 64, r10d, 4)), [0x67, 0x4a, 0x8b, 0x54, 0x90, 0x40])
  verify(x86.mov(rdx, MemRef(r14d, 24, ebx, 2)), [0x67, 0x49, 0x8b, 0x54, 0x5e, 0x18])
  verify(x86.add(MemRef(rbp, data_size = 32), 5), [0x83, 0x45, 0x00, 0x05])
  verify(x86.add(MemRef(rbp, data_size = 32), 0x1EADBEEF), [0x81, 0x45, 0x00, 0xef, 0xbe, 0xad, 0x1e])
  verify(x86.add(ebp, 8),                   [0x83, 0xc5, 0x08])
  verify(x86.add(r15d, 8),                  [0x41, 0x83, 0xc7, 0x08])
  verify(x86.add(r15d, 0x1EADBEEF),         [0x41, 0x81, 0xc7, 0xef, 0xbe, 0xad, 0x1e])
  verify(x86.mov(r8d, 0x1EADBEEF),          [0x41, 0xb8, 0xef, 0xbe, 0xad, 0x1e])
  verify(x86.add(ax, r9w),                  [0x66, 0x44, 0x01, 0xc8])
  verify(x86.add(eax, r9d),                 [0x44, 0x01, 0xc8])
  verify(x86.add(rax, MemRef(rbp, -8)),     [0x48, 0x03, 0x45, 0xf8])
  verify(x86.cmplepd(xmm11, xmm10),         [0x66, 0x45, 0x0f, 0xc2, 0xda, 0x02])
  verify(x86.pextrw(eax, xmm7, 2),          [0x66, 0x0f, 0xc5, 0xc7, 0x02])
  verify(x86.mov(rax, MemRef(rip, 128)),    [0x48, 0x8b, 0x05, 0x80, 0x00, 0x00, 0x00])
  verify(x86.mov(MemRef(rip, 128), rax),    [0x48, 0x89, 0x05, 0x80, 0x00, 0x00, 0x00])
  verify(x86.mov(eax, MemRef(rip, 128, data_size = 32)), [0x8b, 0x05, 0x80, 0x00, 0x00, 0x00])
  verify(x86.mov(rax,MemRef(128)),          [0x48, 0x8b, 0x04, 0x25, 0x80, 0x00, 0x00, 0x00])
  verify(x86.mov(rax,MemRef(rbp)),          [0x48, 0x8b, 0x45, 0x00])
  verify(x86.mov(rbx,MemRef(rbp, index = rdx, scale=2)), [0x48, 0x8b, 0x5c, 0x55, 0x00])
  verify(x86.mov(rbx,MemRef(rdi, index = rdx, scale=2)), [0x48, 0x8b, 0x1c, 0x57])
  verify(x86.mov(rbx,MemRef(rsp, index = rdx, scale=2)), [0x48, 0x8b, 0x1c, 0x54])
  verify(x86.mov(rax,MemRef(rbp, 0, index = rdx, scale=2)), [0x48, 0x8b, 0x44, 0x55, 0x00])
  verify(x86.mov(eax,MemRef(ebp, data_size = 32)), [0x67, 0x8b, 0x45, 0x00])
  verify(x86.and_(al,bl),                   [0x20, 0xd8])
  verify(x86.and_(al,ch),                   [0x20, 0xe8])
  verify(x86.and_(al,sil),                  [0x40, 0x20, 0xf0])
  verify(x86.and_(al,spl),                  [0x40, 0x20, 0xe0])
  verify(x86.and_(bpl,MemRef(rax, data_size = 8)), [0x40, 0x22, 0x28])
  verify(x86.invlpg(MemRef(rax, data_size = 8)), [0x0F, 0x01, 0x38])
  verify(x86.rdtscp(), [0x0F, 0x01, 0xF9])
  verify(x86.cmove(rcx, rdx), [0x48, 0x0F, 0x44, 0xCA])
  verify(x86.cmove(ecx, edx), [0x0F, 0x44, 0xCA])
  verify(x86.cmove(cx, dx), [0x66, 0x0F, 0x44, 0xCA])
  verify(x86.shld(rax, rbx, cl), [0x48, 0x0F, 0xA5, 0xD8])
  verify(x86.shld(eax, ebx, cl), [0x0F, 0xA5, 0xD8])
  verify(x86.shld(ax, bx, cl), [0x66, 0x0F, 0xA5, 0xD8])
  verify(x86.shld(rax, rbx, 4), [0x48, 0x0F, 0xA4, 0xD8, 0x04])
  verify(x86.shld(eax, ebx, 4), [0x0F, 0xA4, 0xD8, 0x04])
  verify(x86.shld(ax, bx, 4), [0x66, 0x0F, 0xA4, 0xD8, 0x04])
  verify(x86.imul(rax, rdx, 0x100000), [0x48, 0x69, 0xC2, 0x00, 0x00, 0x10, 0x00])
  verify(x86.imul(rax, rdx, 0x10), [0x48, 0x6B, 0xC2, 0x10])
  verify(x86.imul(eax, edx, 0x100000), [0x69, 0xC2, 0x00, 0x00, 0x10, 0x00])
  verify(x86.imul(ax, dx, 0x1000), [0x66, 0x69, 0xC2, 0x00, 0x10])
  verify(x86.shl(rax, 1), [0x48, 0xD1, 0xE0])
  verify(x86.add(eax, 1), [0x83, 0xC0, 0x01])
  verify(x86.mov(r15, 4), [0x49, 0xC7, 0xC7, 0x04, 0x00, 0x00, 0x00])

  print

  verify(x86.cvtss2si(r9d, xmm0),           [0xf3, 0x44, 0x0f, 0x2d, 0xc8])
  verify(x86.cvttsd2si(r9d, xmm0),          [0xf2, 0x44, 0x0f, 0x2c, 0xc8])
  verify(x86.cvttss2si(r9d, xmm0),          [0xf3, 0x44, 0x0f, 0x2c, 0xc8])
  verify(x86.movmskpd(eax,xmm9), [0x66, 0x41, 0x0F, 0x50, 0xC1])
  verify(x86.pmovmskb(eax,xmm9), [0x66, 0x41, 0x0F, 0xD7, 0xC1])
  verify(x86.pextrw(ebx, xmm12, 4), [0x66, 0x41, 0x0F, 0xC5, 0xDC, 0x04])
  verify(x86.pinsrw(xmm12, ebx, 4), [0x66, 0x44, 0x0F, 0xC4, 0xE3, 0x04])
  verify(x86.movd(ecx,xmm5), [0x66, 0x0F, 0x7E, 0xE9])
  verify(x86.movd(xmm5,edx), [0x66, 0x0F, 0x6E, 0xEA])
  # verify(x86.movd(xmm5,rdx), [0x66, 0x48, 0x0F, 0x6E, 0xEA])

  print

  # verify(x86.cvtsi2sd(xmm0, r9),           [0xF3, 0x49, 0x0F, 0x2A, 0xC1])
  # verify(x86.cvtss2si(r9, xmm0),           [0xF3, 0x4C, 0x0F, 0x2D, 0xC8])
  # verify(x86.cvttsd2si(r9, xmm0),          [0xF2, 0x4C, 0x0F, 0x2C, 0xC8])
  # verify(x86.cvttss2si(r9, xmm0),          [0xF3, 0x4C, 0x0F, 0x2C, 0xC8])
  # verify(x86.movd(rcx,xmm5), [0x66, 0x48, 0x0F, 0x7E, 0xE9])
  # verify(x86.movd(xmm5,rdx), [0x66, 0x48, 0x0F, 0x6E, 0xEA])

  print

  verify(x86.pmovmskb(eax,mm1), [0x0F, 0xD7, 0xC1])
  # verify(x86.pmovmskb(rax,mm1), [0x48, 0x0F, 0xD7, 0xC1])
  # verify(x86.movd(rcx,mm5), [0x48, 0x0F, 0x7E, 0xE9])
  # verify(x86.movd(mm5,rdx), [0x48, 0x0F, 0x6E, 0xEA])

  return

Test()

