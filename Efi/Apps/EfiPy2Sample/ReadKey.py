#
# ReadKey.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# ReadKey.py is free software: you can redistribute it and/or modify
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

from EfiPy2.MdePkg.Protocol import SimpleTextIn as Si

EventIndex  = EfiPy.UINTN()
InputKey    = Si.EFI_INPUT_KEY ()

while True:

  Status      = EfiPy.EFI_NOT_READY

  EfiPy.gST.ConOut[0].OutputString (
                        EfiPy.gST.ConOut,
                        "Please enter any keys for test or press Q(q) to exit...\r\n"
                        )

  while EfiPy.RETURN_ERROR (Status):

    Status = EfiPy.gBS.WaitForEvent (
                         1,
                         EfiPy.byref(EfiPy.EFI_EVENT(EfiPy.gST.ConIn[0].WaitForKey)),
                         EfiPy.byref(EventIndex)
                         )

  Status = EfiPy.gST.ConIn[0].ReadKeyStroke (
                                EfiPy.gST.ConIn,
                                EfiPy.byref (InputKey)
                                )

  #
  # ScanCode is inpute
  #
  if InputKey.ScanCode != Si.SCAN_NULL:

    EfiPy.gST.ConOut[0].OutputString (
                          EfiPy.gST.ConOut,
                          "Scan code 0x%04X is input\r\n" % InputKey.ScanCode
                          )

  else:

    EfiPy.gST.ConOut[0].OutputString (
                          EfiPy.gST.ConOut,
                          'Input key "%c"\r\n' % InputKey.UnicodeChar
                          )

    if InputKey.UnicodeChar == "q" or InputKey.UnicodeChar == "Q":

      EfiPy.gST.ConOut[0].OutputString (
                            EfiPy.gST.ConOut,
                            "Exit\r\n"
                            )

      break
