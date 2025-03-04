# MpServiceSample3.py
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

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.Protocol.MpService as MpService
from EfiPy2.MdePkg.Pi.PiMultiPhase  import EFI_AP_PROCEDURE

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
           EfiPy.byref (MpService.gEfiMpServiceProtocolGuid),
           None,
           EfiPy.byref (Interface)
           )

if Status != EfiPy.EFI_SUCCESS:
  print ("Locate protocol.(Status:0x%016X)" % Status)
  import sys
  sys.exit (Status)

pMpServiceProtocol = EfiPy.cast (
                       Interface,
                       EfiPy.POINTER(MpService.EFI_MP_SERVICES_PROTOCOL)
                       )

MpServiceProtocol = pMpServiceProtocol[0]

NumberOfProcessors          = EfiPy.UINTN ()
NumberOfEnabledProcessors   = EfiPy.UINTN ()

Status = MpServiceProtocol.GetNumberOfProcessors (
           pMpServiceProtocol,
           EfiPy.byref (NumberOfProcessors),
           EfiPy.byref (NumberOfEnabledProcessors)
           )

if Status != EfiPy.EFI_SUCCESS:
  print ('GetNumberOfProcessors status: 0x%016X' % Status)
  import sys
  sys.exit (Status)
#
# Checking current thread id
#
ProcessorBsp = EfiPy.UINTN (-1)
Status = MpServiceProtocol.WhoAmI (
        pMpServiceProtocol,
        EfiPy.byref (ProcessorBsp)
        )

###############################################################################
#                                                                             #
# launch LocalApicIdGet function in different core                            #
#                                                                             #
###############################################################################
#
# Mp service function call
#
import corepy.arch.x86_64.isa as x86
import corepy.arch.x86_64.types.registers as reg
import corepy.arch.x86_64.lib.memory as mem
import corepy.arch.x86_64.platform as env

code                = env.InstructionStream()
MachineCodeStream   = None

def LocalApicIdGetMachineCode ():
    # $ cat stub.c
    # void  __attribute__((__ms_abi__)) EfiPyLocalApicGet (unsigned int *a) {
    # 
    #     unsigned int *apicid;
    #     *a = *(unsigned int *)0xFEE00020;
    #     *a = *a >> 24;
    # }
    # $ objdump -S stub.o
    # 
    # stub.o:     file format elf64-x86-64
    # 
    # 
    # Disassembly of section .text:
    # 
    # 0000000000000000 <EfiPyLocalApicGet>:
    # void  __attribute__((__ms_abi__)) EfiPyLocalApicGet (unsigned int *a) {
    #    0:   f3 0f 1e fa             endbr64
    #    4:   55                      push   %rbp
    #    5:   48 89 e5                mov    %rsp,%rbp
    #    8:   48 89 4d 10             mov    %rcx,0x10(%rbp)
    # 
    #     unsigned int *apicid;
    #     *a = *(unsigned int *)0xFEE00020;
    #    c:   b8 20 00 e0 fe          mov    $0xfee00020,%eax
    #   11:   8b 10                   mov    (%rax),%edx
    #   13:   48 8b 45 10             mov    0x10(%rbp),%rax
    #   17:   89 10                   mov    %edx,(%rax)
    #     *a = *a >> 24;
    #   19:   48 8b 45 10             mov    0x10(%rbp),%rax
    #   1d:   8b 00                   mov    (%rax),%eax
    #   1f:   c1 e8 18                shr    $0x18,%eax
    #   22:   89 c2                   mov    %eax,%edx
    #   24:   48 8b 45 10             mov    0x10(%rbp),%rax
    #   28:   89 10                   mov    %edx,(%rax)
    # }
    #   2a:   90                      nop
    #   2b:   5d                      pop    %rbp
    #   2c:   c3                      ret
    # $

    global MachineCodeStream

    MachineCodeByte = b'\x55\x48\x89\xe5\x48\x89\x4d\x10\xb8\x20\x00\xe0\xfe\x8b\x10\x48\x8b\x45\x10\x89\x10\x48\x8b\x45\x10\x8b\x00\xc1\xe8\x18\x89\xc2\x48\x8b\x45\x10\x89\x10\x90\x5d\xc3'
    MachineCodeStream   = EfiPy.create_string_buffer (MachineCodeByte)
    MachineCodeAddress  = EfiPy.addressof (MachineCodeStream)
    return MachineCodeAddress

def LocalApicIdGetCorePy ():

    global code, MachineCodeStream

    code.add(x86.mov(reg.eax, 0xFEE00020))                                  #               rdx =  0xFEE00000
    code.add(x86.mov(reg.edx, mem.MemRef(reg.eax, 0x00, data_size = 32)))   #               eax = *(UINT32)(rdx + 0x20)
    code.add(x86.shr(reg.edx, 24))

    code.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 0x10)))   #               eax = *(UINT32)(rdx + 0x20)
    code.add(x86.mov(mem.MemRef(reg.rax, 0, data_size = 32), reg.edx))                     #               rdx = *(UINT32 *)(rbp)

    code.add(x86.nop())

    # code.print_code(pro = True, epi = True, hex = True)
    MachineCodeAddress, MachineCodeStream = code.get_code_bytes ()
    return MachineCodeAddress 

def LocalApicIdGetWraper (Buffer):
    LocalApicIdPointer = EfiPy.UINT32_BE.from_address (0xFEE00000 + 0x20)
    LocalApicId = LocalApicIdPointer.value & 0x000000FF

    LocalApicIdBuffer  = EfiPy.UINT32.from_address (Buffer)
    LocalApicIdBuffer.value = LocalApicId


# EfiPyLocalApicGet = MpService.EFI_AP_PROCEDURE (LocalApicIdGetWraper)
# MachineCodeAddress  = LocalApicIdGetMachineCode ()
MachineCodeAddress  = LocalApicIdGetCorePy ()

print (f'MachindeCodeAddress: 0x{MachineCodeAddress:08X}')
EfiPyLocalApicGet = MpService.EFI_AP_PROCEDURE (MachineCodeAddress)

#
# Get ApicId from 0xFEE00000 on curretn id 1
#
print ('\n==================================================================')
LocalApicId = EfiPy.UINT32(-1)    # Assign invalid number, first
ProcessorIds = []

for ProcessorGo in range (NumberOfProcessors.value):
  if ProcessorGo == ProcessorBsp.value:
    Status = EfiPyLocalApicGet (EfiPy.byref (LocalApicId))
  else:
    Status = MpServiceProtocol.StartupThisAP (
               pMpServiceProtocol,          # POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
               EfiPyLocalApicGet,           # EFI_AP_PROCEDURE,                   # IN  Procedure,
               ProcessorGo,                 # UINTN,                              # IN  ProcessorNumber,
               None,                        # EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
               0,                           # UINTN,                              # IN  TimeoutInMicroseconds,
               EfiPy.byref (LocalApicId),   # PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
               None,                        # POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
               )
  ProcessorIds.append (LocalApicId.value)
  
  print (f'Launch thread run in #{ProcessorGo}')
  print (f'  Local Apic ID is 0x{LocalApicId.value:08X}')

print ()
print ('Processor IDs...', ProcessorIds)