#
# asm.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
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

import corepy.lib.printer as printer
import corepy.arch.x86_64.isa as x86
from corepy.arch.x86_64.types.registers import *
import corepy.arch.x86_64.platform as env

code = env.InstructionStream()
proc = env.Processor()


code.add(x86.mov(dx, 0x80))
code.add(x86.mov(ax, 0xaa))
code.add(x86.out(dx, ax))

code.print_code()

proc.execute(code)
