# CorePyBasic1.py
#
# Copyright (C) 2025 efipy.core@gmail.com All rights reserved.
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

def CopyPyAdd (a: int, b: int, DumpCode: bool = False) -> int:
    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.lib.memory as mem
    import corepy.arch.x86_64.platform as env

    code    = env.InstructionStream()
    proc    = env.Processor()
    params  = env.ExecParams()

    params.p1 = a
    params.p2 = b

    code.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 16)))  # ret = a
    code.add(x86.add(reg.rax, mem.MemRef(reg.rbp, 24)))  # ret = ret + b

    if DumpCode:
        code.print_code(pro = True, epi = True, hex = True)

    return proc.execute(code, params = params, mode = 'int')

if __name__ == '__main__':

    input1 = 100
    input2 = 200

    ret1 = CopyPyAdd (input1, input2)   # ret1 = input1 + input2
    ret2 = input1 + input2              # ret2 = input1 + input2

    print (f'{input1} + {input2} = {ret1}, result: {ret1 == ret2}')