#
# VariableBootOrder2.py
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

from EfiPy2.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid
from EfiPy2.Lib.EfiPyVariable import Variable

var = Variable ('BootOrder', gEfiGlobalVariableGuid)
var.GetVariable ()

print (f'Attribute: {var.Attribute}')
print (f'{var.VarValue[:]}, size: {len(var)}')

from EfiPy2.Lib.HexDump import HexDump
HexDump (var.VarValue[:])
