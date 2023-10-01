#
# ErrorTest.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# ErrorTest.py is free software: you can redistribute it and/or modify
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

import traceback
import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Protocol.SimpleTextOut import     \
                     gEfiSimpleTextOutProtocolGuid,  \
                     EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL

try:
  Status = EfiPy.gBS.LocateProtocol (
             EfiPy.byref (gEfiSimpleTextOutProtocolGuid),
             None,
             EfiPy.byref (Interface)
             )
  print ("Locate SimpleTextOut Protocol, result: ", status)

except:
  print ("""## Exception Test:
## Due to Interface is not define...
## NameError exception should be occure...

   name 'Interface' is not defined

## traceback result...
==============================================================================""")
  print (traceback.format_exc())
