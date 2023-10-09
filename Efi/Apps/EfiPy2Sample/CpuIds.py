#
# CpuIds.py
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# CpuIds.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CpuIds.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

from CpuId import *

cpu  = CpuId()
cpuI = CpuIdUnion()

CpuInfoAddr = EfiPy.addressof (cpuI)

rax = cpu.GetId(0, 0, CpuInfoAddr)

print ("============================================")
print ("   Input      EAX      EBX      ECX      EDX")
print ("%08X %08X %08X %08X %08X" % (rax,
                                     cpuI.CpuInfo.EAX,
                                     cpuI.CpuInfo.EBX,
                                     cpuI.CpuInfo.ECX,
                                     cpuI.CpuInfo.EDX))
