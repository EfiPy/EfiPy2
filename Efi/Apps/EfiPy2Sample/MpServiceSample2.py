# MpServiceSample2.py
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
def LocalApicIdGet (Buffer):
    LocalApicIdPointer = EfiPy.UINT32_BE.from_address (0xFEE00000 + 0x20)
    LocalApicId = LocalApicIdPointer.value & 0x000000FF

    LocalApicIdBuffer  = EfiPy.UINT32.from_address (Buffer)
    LocalApicIdBuffer.value = LocalApicId

EfiPyLocalApicGet = MpService.EFI_AP_PROCEDURE (LocalApicIdGet)

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
  print (f'  Local Apic ID is {LocalApicId.value}')

print ()
print ('Processor IDs...', ProcessorIds)