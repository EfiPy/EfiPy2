#
# EfiPy2Guid.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# EfiPy2Guid.py is free software: you can redistribute it and/or modify
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

from EfiPy2 import EFI_GUID
TestGuid1 = EFI_GUID (
              0x8D59D32B,
              0xC655,
              0x4AE9,
              (0x9B, 0x15, 0xF2, 0x59, 0x04, 0x99, 0x2A, 0x43)
              )
TestGuid2 = EFI_GUID (
              0x8D59D32B,
              0xC655,
              0x4AE9,
              (0x9B, 0x15, 0xF2, 0x59, 0x04, 0x99, 0x2A, 0x44)
              )
TestGuid3 = EFI_GUID (
              0x8D59D32B,
              0xC655,
              0x4AE9,
             (0x9B, 0x15, 0xF2, 0x59, 0x04, 0x99, 0x2A, 0x43)
             )

print ("TestGuid1: %s" % TestGuid1)
print ("TestGuid2: %s" % TestGuid2)
print ("TestGuid3: %s" % TestGuid3)
print ("TestGuid1 == TestGuid2 :", TestGuid1 == TestGuid2)
print ("TestGuid1 == TestGuid3 :", TestGuid1 == TestGuid3)
