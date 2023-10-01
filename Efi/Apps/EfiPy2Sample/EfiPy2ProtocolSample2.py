#
# EfiPy2ProtocolSample2.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# EfiPy2ProtocolSample2.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy

gEfiPy2SampleProtocolGuid = EfiPy.EFI_GUID(
                                    0x8BE4DF61,
                                    0x93CA,
                                    0x11d2,
                                    (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x81)
                                    )

#
# Protocol memeber functions
#

def EfiPy2SampleProtocolFunc1 (Val1, Val2):

  print ("   EfiPy2SampleProtocolFunc1 Val1:", Val1)

  if not Val2:
    print ("   Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 3

  return EfiPy.EFI_SUCCESS

def EfiPy2SampleProtocolFunc2 (Val1, Val2):

  print ("   EfiPy2SampleProtocolFunc2 Val1:", Val1)

  if not Val2:
    print ("   Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 5

  return EfiPy.EFI_SUCCESS

#
# Protocl function type
#
EFIPY2_SAMPLEPROTOCOL_FUNC1 = EfiPy.CFUNCTYPE (
                                      EfiPy.EFI_STATUS,
                                      EfiPy.UINTN,
                                      EfiPy.POINTER(EfiPy.UINT32)
                                      )

EFIPY2_SAMPLEPROTOCOL_FUNC2 = EfiPy.CFUNCTYPE (
                                      EfiPy.EFI_STATUS,
                                      EfiPy.UINTN,
                                      EfiPy.POINTER(EfiPy.UINT32)
                                      )

#
# Protocol Structure
#

class EFIPY2_SAMPLEPROTOCOL_CLASS (EfiPy.Structure):
  _fields_ = [("P1Func1", EFIPY2_SAMPLEPROTOCOL_FUNC1),
              ("P1Val",   EfiPy.UINT32),
              ("P1Func2", EFIPY2_SAMPLEPROTOCOL_FUNC2)
             ]

#
# Building protocol object
#

P1 = EFIPY2_SAMPLEPROTOCOL_FUNC1 (EfiPy2SampleProtocolFunc1)
P2 = EFIPY2_SAMPLEPROTOCOL_FUNC2 (EfiPy2SampleProtocolFunc2)
EfiPy2SampleProtocol = EFIPY2_SAMPLEPROTOCOL_CLASS (P1, 3, P2)

#
# Protocl event variable
#

def ProtocolRegisterFunc (Event, Context):
  print ("    Protocl Register notification call back.")

Event = EfiPy.EFI_EVENT ()
tFunc = EfiPy.EFI_EVENT_NOTIFY(ProtocolRegisterFunc)
gContext = EfiPy.UINTN (1024)

Status = EfiPy.gBS.CreateEvent (
                     EfiPy.EVT_NOTIFY_SIGNAL,
                     EfiPy.TPL_NOTIFY,
                     tFunc,
                     EfiPy.PVOID.from_address (EfiPy.addressof(gContext)),
                     EfiPy.byref (Event)
                     )

print ("gBS.CreateEvent(Status:0x%016X)" % Status)

#
# RegisterProtocolNotify
#

Registration = EfiPy.PVOID()

Status = EfiPy.gBS.RegisterProtocolNotify (
                     EfiPy.byref (gEfiPy2SampleProtocolGuid),
                     Event,
                     EfiPy.byref(Registration)
                     )

print ("gBS.RegisterProtocolNotify(Status:0x%016X)" % Status)

#
# InstallProtocolInterface
#
Handle1 = EfiPy.EFI_HANDLE()

Status = EfiPy.gBS.InstallProtocolInterface (
                     EfiPy.byref (Handle1),
                     EfiPy.byref (gEfiPy2SampleProtocolGuid),
                     EfiPy.EFI_NATIVE_INTERFACE,
                     EfiPy.byref (EfiPy2SampleProtocol)
                     )

print
print ("gBS.InstallProtocolInterface(Status:0x%016X)" % Status)

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
                     EfiPy.byref (gEfiPy2SampleProtocolGuid),
                     None,
                     EfiPy.byref (Interface)
                     )

print ("gBS.LocateProtocol(Status:0x%016X)" % Status)

IntProt = EfiPy.cast (Interface, EfiPy.POINTER(EFIPY2_SAMPLEPROTOCOL_CLASS))
Status = IntProt[0].P1Func1 (20, None)
print ("IntProt[0].P1Func1 (Status:0x%016X)" % Status)

Ret = EfiPy.UINT32 (8)

Status = IntProt[0].P1Func2 (30, EfiPy.byref(Ret))
print ("IntProt[0].P1Func2 (Status:0x%016X), Val:%d" % (Status, Ret.value))

Status = EfiPy.gBS.UninstallProtocolInterface (
                     Handle1,
                     EfiPy.byref (gEfiPy2SampleProtocolGuid),
                     Interface
                     )

print ("gBS.UninstallProtocolInterface(Status:0x%016X)" % Status)

Status = EfiPy.gBS.CloseEvent (Event)
print ("gBS.CloseEvent(Status:0x%016X)" % Status)

