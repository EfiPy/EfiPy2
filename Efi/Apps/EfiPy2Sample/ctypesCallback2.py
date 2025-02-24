# ctypesCallback2.py
#
# Copyright (C) 2025 efipy.core@gmail.com All rights reserved.
#
# asm.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PaTest.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import ctypes, EfiPy2

import os
if os.name == 'posix':
  # $ cat stub.c
  # 
  # int  func (int a, int b) {
  #   return a + b;
  # }
  # 
  # $ gcc -c -g stub.c -o stub.o
  # $
  # $ objdump -S stub.o 
  #
  # 0000000000000000 <func>:
  # int  func (int a, int b) {
  #    0:   f3 0f 1e fa             endbr64
  #    4:   55                      push   %rbp
  #    5:   48 89 e5                mov    %rsp,%rbp
  #    8:   89 7d fc                mov    %edi,-0x4(%rbp)
  #    b:   89 75 f8                mov    %esi,-0x8(%rbp)
  #   return a + b;
  #    e:   8b 55 fc                mov    -0x4(%rbp),%edx
  #   11:   8b 45 f8                mov    -0x8(%rbp),%eax
  #   14:   01 d0                   add    %edx,%eax
  # }
  #   16:   5d                      pop    %rbp
  #   17:   c3                      ret
  MachineCodeByte     = b"\x55\x48\x89\xe5\x89\x7d\xfc\x89\x75\xf8\x8b\x55\xfc\x8b\x45\xf8\x01\xd0\x5d\xc3"


elif os.name == 'edk2':
  # 
  # $ cat stub.c
  # int __attribute__((__ms_abi__)) func (int a, int b) {
  #   return a + b;
  # }
  # $
  # $ gcc -g -c stub.c -o stub.o 
  # $
  # $ objdump -S stub.o
  # 
  # stub.o:     file format elf64-x86-64
  # 
  # 
  # Disassembly of section .text:
  # 
  # 0000000000000000 <func>:
  # int __attribute__((__ms_abi__)) func (int a, int b) {
  #    0:   f3 0f 1e fa             endbr64
  #    4:   55                      push   %rbp
  #    5:   48 89 e5                mov    %rsp,%rbp
  #    8:   89 4d 10                mov    %ecx,0x10(%rbp)
  #    b:   89 55 18                mov    %edx,0x18(%rbp)
  #   return a + b;
  #    e:   8b 55 10                mov    0x10(%rbp),%edx
  #   11:   8b 45 18                mov    0x18(%rbp),%eax
  #   14:   01 d0                   add    %edx,%eax
  # }
  #   16:   5d                      pop    %rbp
  #   17:   c3                      ret
  #
  MachineCodeByte     = b"\x55\x48\x89\xe5\x89\x4d\x10\x89\x55\x18\x8b\x55\x10\x8b\x45\x18\x01\xd0\x5d\xc3"

# MachineCodeByte     = b"\x55\x89\xe5\x5d\xc3"
MachineCodeStream   = EfiPy2.create_string_buffer (MachineCodeByte)
MachineCodeAddress  = EfiPy2.addressof (MachineCodeStream)

if os.name == 'posix':

  # Initialise ctypes prototype for mprotect().
  # According to the manpage:
  #     int mprotect(const void *addr, size_t len, int prot);
  libc = ctypes.CDLL("libc.so.6")
  mprotect = libc.mprotect
  mprotect.restype = ctypes.c_int
  mprotect.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]
  
  PROT_NONE = 0x0
  PROT_READ = 0x1
  PROT_WRITE = 0x2
  PROT_EXEC = 0x4
  
  pagesize = 0x1000
  pagestart = MachineCodeAddress & ~(pagesize - 1)

  if mprotect(pagestart, pagesize, PROT_READ|PROT_WRITE|PROT_EXEC):
      raise RuntimeError("Failed to set permissions using mprotect()")

EFIPY2_CFUNCTYPE1 = EfiPy2.CFUNCTYPE (
                             EfiPy2.PVOID,
                             EfiPy2.INTN,
                             EfiPy2.INTN
                             )

print ("Assign Machine code buffer to function address...")
P1 = EFIPY2_CFUNCTYPE1(MachineCodeAddress)

input1 = 100
input2 = 200
print ("Berfor calling P1...")
ret = P1 (input1, input2)
print ("After calling P1... %d" % ret)
