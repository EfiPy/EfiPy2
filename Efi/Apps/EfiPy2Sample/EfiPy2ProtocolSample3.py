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
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy

TestGuid1 = EfiPy.EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x81))
TestGuid2 = EfiPy.EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2C, 0x81))
TestGuid3 = EfiPy.EFI_GUID( 0x8BE4DF61, 0x93CA, 0x11d2, (0xAA, 0x0D, 0x00, 0xE0, 0x99, 0x03, 0x2C, 0x81))

#
# Protocol memeber function set 1
#

def ProtocolFunc1 (Val1, Val2):

  print ("   ProtocolFunc1 Val1:", Val1)

  if not Val2:
    print ("   ProtocolFunc1: Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 3

  return EfiPy.EFI_SUCCESS

def ProtocolFunc2 (Val1, Val2):

  print ("   ProtocolFunc2 Val1:", Val1)

  if not Val2:
    print ("   ProtocolFunc2: Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 5

  return EfiPy.EFI_SUCCESS

#
# Protocol memeber function set 2
#

def ProtocolFunc3 (Val1, Val2):

  print ("   ProtocolFunc1 Val3:", Val1)

  if not Val2:
    print ("   ProtocolFunc3: Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 3

  return EfiPy.EFI_SUCCESS

def ProtocolFunc4 (Val1, Val2):

  print ("   ProtocolFunc4 Val1:", Val1)

  if not Val2:
    print ("   ProtocolFunc4: Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 5

  return EfiPy.EFI_SUCCESS

#
# Protocol memeber function set 3
#

def ProtocolFunc5 (Val1, Val2):

  print ("   ProtocolFunc1 Val5:", Val1)

  if not Val2:
    print ("   ProtocolFunc5: Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 3

  return EfiPy.EFI_SUCCESS

def ProtocolFunc6 (Val1, Val2):

  print ("   ProtocolFunc6 Val1:", Val1)

  if not Val2:
    print ("   ProtocolFunc6: Get NULL pointer of Val2")
    return EfiPy.EFI_INVALID_PARAMETER

  Val2[0] = 5

  return EfiPy.EFI_SUCCESS

#
# Protocl function type
#
PROTOCOL_FUNC1 = EfiPy.CFUNCTYPE (
                   EfiPy.EFI_STATUS,
                   EfiPy.UINTN,
                   EfiPy.POINTER(EfiPy.UINT32)
                   )

PROTOCOL_FUNC2 = EfiPy.CFUNCTYPE (
                   EfiPy.EFI_STATUS,
                   EfiPy.UINTN,
                   EfiPy.POINTER(EfiPy.UINT32)
                   )

#
# Protocol Structure
#

class TEST_PROTOCOL (EfiPy.Structure):
  _fields_ = [("P1Func1", PROTOCOL_FUNC1),
              ("P1Val",   EfiPy.UINT32),
              ("P1Func2", PROTOCOL_FUNC2)
             ]

#
# Protocl variable
#

P1 = PROTOCOL_FUNC1 (ProtocolFunc1)
P2 = PROTOCOL_FUNC2 (ProtocolFunc2)
P3 = PROTOCOL_FUNC1 (ProtocolFunc3)
P4 = PROTOCOL_FUNC2 (ProtocolFunc4)
P5 = PROTOCOL_FUNC1 (ProtocolFunc5)
P6 = PROTOCOL_FUNC2 (ProtocolFunc6)

TestProtocol1 = TEST_PROTOCOL (P1, 3, P2)
TestProtocol2 = TEST_PROTOCOL (P3, 4, P4)
TestProtocol3 = TEST_PROTOCOL (P5, 4, P6)

print ('''
MultipleProtocol testing...
''')

Handle1 = EfiPy.EFI_HANDLE ()
EfiPy.gBS.InstallMultipleProtocolInterfaces.argtypes = [
      EfiPy.POINTER(EfiPy.EFI_HANDLE),
      EfiPy.POINTER(EfiPy.EFI_GUID),
      EfiPy.POINTER(EfiPy.PVOID),
      EfiPy.POINTER(EfiPy.PVOID)
      ]

Status = EfiPy.gBS.InstallMultipleProtocolInterfaces (
               EfiPy.byref (Handle1),
               EfiPy.byref (TestGuid1),
               EfiPy.byref (TestProtocol1),
               None
               )

print ("gBS.InstallMultipleProtocolInterfaces - 1 (Status:0x%016X)" % Status)

Handle2 = EfiPy.EFI_HANDLE ()
EfiPy.gBS.InstallMultipleProtocolInterfaces.argtypes = [
      EfiPy.POINTER(EfiPy.EFI_HANDLE),
      EfiPy.POINTER(EfiPy.EFI_GUID),
      EfiPy.POINTER(EfiPy.PVOID),
      EfiPy.POINTER(EfiPy.EFI_GUID),
      EfiPy.POINTER(EfiPy.PVOID),
      EfiPy.POINTER(EfiPy.PVOID)
      ]

Status = EfiPy.gBS.InstallMultipleProtocolInterfaces (
               EfiPy.byref (Handle2),
               EfiPy.byref (TestGuid2),
               EfiPy.byref (TestProtocol2),
               EfiPy.byref (TestGuid3),
               EfiPy.byref (TestProtocol3),
               None
               )

print ("gBS.InstallMultipleProtocolInterfaces - 2 (Status:0x%016X)" % Status)

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
                     EfiPy.byref (TestGuid1),
                     None,
                     EfiPy.byref (Interface)
                     )

IntProt = EfiPy.cast (Interface, EfiPy.POINTER(TEST_PROTOCOL))
Status = IntProt[0].P1Func1 (20, None)
print ("IntProt[0].P1Func1 (Status:0x%016X)" % Status)

EfiPy.gBS.UninstallMultipleProtocolInterfaces.argtypes = [
      EfiPy.EFI_HANDLE,
      EfiPy.POINTER(EfiPy.EFI_GUID),
      EfiPy.POINTER(EfiPy.PVOID),
      EfiPy.POINTER(EfiPy.EFI_GUID),
      EfiPy.POINTER(EfiPy.PVOID),
      EfiPy.POINTER(EfiPy.PVOID)
      ]

Status = EfiPy.gBS.UninstallMultipleProtocolInterfaces (
               Handle2,
               EfiPy.byref (TestGuid2),
               EfiPy.byref (TestProtocol2),
               EfiPy.byref (TestGuid3),
               EfiPy.byref (TestProtocol3),
               None
               )

print ("gBS.UninstallMultipleProtocolInterfaces - 1 (Status:0x%016X)" % Status)

EfiPy.gBS.UninstallMultipleProtocolInterfaces.argtypes = [
      EfiPy.EFI_HANDLE,
      EfiPy.POINTER(EfiPy.EFI_GUID),
      EfiPy.POINTER(EfiPy.PVOID),
      EfiPy.POINTER(EfiPy.PVOID)
      ]

Status = EfiPy.gBS.UninstallMultipleProtocolInterfaces (
               Handle1,
               EfiPy.byref (TestGuid1),
               EfiPy.byref (TestProtocol1),
               None
               )

print ("gBS.UninstallMultipleProtocolInterfaces - 2 (Status:0x%016X)" % Status)
