#
# VariableBootOrder.py
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com All rights reserved.
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
from EfiPy2.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid

VariableName  = "BootOrder"
VariableGuid  = gEfiGlobalVariableGuid

VariableSize  = EfiPy.UINTN (0x00)

Status = EfiPy.gRT.GetVariable(
                     VariableName,
                     EfiPy.byref (VariableGuid),
                     None,
                     EfiPy.byref (VariableSize),
                     None
                     )

if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
    print (f'Expect gRT.GetVariable return 0x{EfiPy.EFI_BUFFER_TOO_SMALL:016X} (EfiPy.EFI_BUFFER_TOO_SMALL), but 0x{Status:016X} return.')
    import sys
    sys.exit(1)

VariableBuff    = (EfiPy.CHAR8 * VariableSize.value) ()
VariableAttr    = EfiPy.UINT32 ()
Status = EfiPy.gRT.GetVariable(
                     VariableName,
                     EfiPy.byref (VariableGuid),
                     EfiPy.byref (VariableAttr),
                     EfiPy.byref (VariableSize),
                     EfiPy.byref (VariableBuff)
                     )

if Status != EfiPy.EFI_SUCCESS:
    print (f'Expect gRT.GetVariable return 0x{EfiPy.EFI_SUCCESS:016X} (EfiPy.EFI_SUCCESS), but 0x{Status:016X} return.')
    import sys
    sys.exit(1)


print (f'''Expect gRT.GetVariable return 0x{EfiPy.EFI_SUCCESS:016X}
    Variable Name:      {VariableName}
    Variable GUID:      {VariableGuid}
    Variable Attribute: {VariableAttr.value}
    Variable size:      {VariableSize.value}
    Variable buff:      {VariableBuff[:]}
''')

from EfiPy2.Lib.HexDump import HexDump
HexDump (VariableBuff[:])
