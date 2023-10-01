#
# EfiPy2ProtocolSample1.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# EfiPy2ProtocolSample1.py is free software: you can redistribute it and/or modify
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

from EfiPy2.MdePkg.Protocol.SimpleTextOut import     \
                     gEfiSimpleTextOutProtocolGuid,  \
                     EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL

Interface = EfiPy.PVOID ()
Status = EfiPy.gBS.LocateProtocol (
           EfiPy.byref (gEfiSimpleTextOutProtocolGuid),
           None,
           EfiPy.byref (Interface)
           )

print ("Locate protocol.(Status:0x%016X)" % Status)

TestConOut = EfiPy.cast (
               Interface,
               EfiPy.POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)
               )

print ("MaxMode:", TestConOut[0].Mode[0].MaxMode)

TestConOut[0].OutputString (
  TestConOut,
  EfiPy.PCHAR16 ("Locate protocol testing.\n\r")
  )
