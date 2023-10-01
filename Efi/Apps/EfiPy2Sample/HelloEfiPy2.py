#
# HelloEfiPy2.py
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# HelloEfiPy2.py is free software: you can redistribute it and/or modify
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

print ("FirmwareVendor: ", EfiPy.gST.FirmwareVendor)
print ("FirmwareRevision: ", EfiPy.gST.FirmwareRevision)
EfiPy.gST.ConOut[0].OutputString(EfiPy.gST.ConOut, "Hello EfiPy2\r\n")
