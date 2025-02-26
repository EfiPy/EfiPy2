# MpServiceSample.py
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
from EfiPy2.Lib.StructDump import DumpStruct

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
           EfiPy.byref (MpService.gEfiMpServiceProtocolGuid),
           None,
           EfiPy.byref (Interface)
           )


if Status != EfiPy.EFI_SUCCESS:
  print ("Locate protocol.(Status:0x%016X)" % Status)
  import sys
  sys.exit (0)

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
  sys.exit (0)

print ('We have %d processors in this system' % NumberOfProcessors.value)
print ('%d processors are enabled' % NumberOfEnabledProcessors.value)

ProcessorInfo = MpService.EFI_PROCESSOR_INFORMATION()

ProcessorIds = []
for Index in range (NumberOfProcessors.value):
  Status = MpServiceProtocol.GetProcessorInfo (
             pMpServiceProtocol,
             Index,
             EfiPy.byref (ProcessorInfo)
             )

  print ('==========================================================================')
  if Status != EfiPy.EFI_SUCCESS:
    print ('GetProcessorInfo status: 0x%016X' % Status)
    continue
  
  DumpStruct (2, ProcessorInfo, MpService.EFI_PROCESSOR_INFORMATION)
  print ()
  ProcessorIds.append (ProcessorInfo.ProcessorId)

ProcessorNumber = EfiPy.UINTN ()
Status = MpServiceProtocol.WhoAmI (
        pMpServiceProtocol,
        EfiPy.byref (ProcessorNumber)
        )
print ('This application run in #%d, Status: 0x%016X' % (ProcessorNumber.value, Status))

print ('Processor IDs...', ProcessorIds)