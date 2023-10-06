#
# Variable.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# Variable.py is free software: you can redistribute it and/or modify
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

OutStrF = EfiPy.gST.ConOut[0].OutputString
ConOutP = EfiPy.gST.ConOut

VariableName  = "EfiPy2Demo"
VariableGuid  = EfiPy.EFI_GUID (
                        0x8BE4DF61,
                        0x93CA,
                        0x11d2,
                        (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8D)
                        )

DataSize      = EfiPy.UINTN (0x00)

Status = EfiPy.gRT.GetVariable(
                     VariableName,
                     EfiPy.byref (VariableGuid),
                     None,
                     EfiPy.byref (DataSize),
                     None
                     )

OutStrF (
  ConOutP,
  'gRT.GetVariable(Name: "%s" (Status:0x%016X)\r\n' % (VariableName, Status)
  )

if Status == EfiPy.EFI_BUFFER_TOO_SMALL:

  DataBuffer    = (EfiPy.CHAR8 * DataSize.value) ()
  Attributes    = EfiPy.UINT32 ()
  Status = EfiPy.gRT.GetVariable(
                       VariableName,
                       EfiPy.byref (VariableGuid),
                       EfiPy.byref (Attributes),
                       EfiPy.byref (DataSize),
                       EfiPy.byref (DataBuffer)
                       )

  if Status != EfiPy.EFI_SUCCESS:

    OutStrF (
      ConOutP,
      'gRT.GetVariable(Name: "%s" (Status:0x%016X)\r\n' % (VariableName, Status)
      )
    

  OutStrF (
    ConOutP,
    'gRT.GetVariable(Name: "%s" (Size:%d)\r\n' % (VariableName, DataSize.value)
    )

  OutStrF (
    ConOutP,
    "Variable contents:\"%s\"\r\n" % DataBuffer.value
    )

elif Status == EfiPy.EFI_NOT_FOUND:

  DataSize      = EfiPy.UINTN (0x05)
  DataBuffer    = EfiPy.create_string_buffer (b"AbCdE", 5)
  Attributes    = EfiPy.UINT32(
                          EfiPy.EFI_VARIABLE_BOOTSERVICE_ACCESS |
                          EfiPy.EFI_VARIABLE_NON_VOLATILE       |
                          EfiPy.EFI_VARIABLE_RUNTIME_ACCESS
                          )

  Status = EfiPy.gRT.SetVariable(
                       VariableName,
                       EfiPy.byref (VariableGuid),
                       Attributes,
                       DataSize,
                       EfiPy.byref (DataBuffer)
                       )

  OutStrF (
    ConOutP,
    'gRT.SetVariable(Name: "%s" (Status:0x%016X)\r\n' % (VariableName, Status)
    )

OutStrF (ConOutP, "Done\r\n")
