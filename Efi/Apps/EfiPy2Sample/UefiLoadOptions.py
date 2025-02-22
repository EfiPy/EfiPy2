# UefiLoadOptions.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import copy
import EfiPy2
from EfiPy2.Lib.EfiPyVariable import Variable
from EfiPy2.Lib.EfiPyVariables import Variables
from EfiPy2.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid
from EfiPy2.MdePkg.Uefi.UefiSpec import EFI_LOAD_OPTION

with Variables('Boot0', CaseSensitive = True) as Vars:

  for n, g in Vars:

    if g != gEfiGlobalVariableGuid:
      print (f'GUID {g} and {gEfiGlobalVariableGuid} is not equal')
      continue
    if 'Boot0' not in n:
      continue

    LoadOptionVariable = Variable (n, g)
    LoadOptionVariable.GetVariable ()

    EfiLoadOptionObject = EFI_LOAD_OPTION.from_buffer_copy (LoadOptionVariable.Value)
    EfiLoadOptionField  = copy.copy (EFI_LOAD_OPTION._fields_)

    #
    # Add Description in Load Option
    #
    EfiLoadOptionDescriptionByte = LoadOptionVariable.Value [EfiPy2.sizeof (EFI_LOAD_OPTION):]
    EfiLoadOptionDescriptionStr  = EfiLoadOptionDescriptionByte.decode ('utf16').split('\x00')[0]

    EfiLoadOptionField.append (('Description', EfiPy2.UINT16 * (len (EfiLoadOptionDescriptionStr) + 1)))
    class EfiLoadOptionType (EfiPy2.Structure):
      _fields_ = EfiLoadOptionField
    EfiLoadOptionObject  = EfiLoadOptionType.from_buffer_copy (LoadOptionVariable.Value)

    #
    # FilePathList and OptionalData in bytes
    #
    FilePathListByte = LoadOptionVariable.Value [EfiPy2.sizeof (EfiLoadOptionType):]

    print (f'''
{n}, GUID: {g}
====================================================''')
    print (f'Variable size:      0x{len(LoadOptionVariable.Value):08X}')
    print (f'Attributes:         0x{EfiLoadOptionObject.Attributes:08X}')
    print (f'FilePathListLength: 0x{EfiLoadOptionObject.FilePathListLength:04X} ({EfiLoadOptionObject.FilePathListLength})')
    print (f'Description:        {EfiLoadOptionDescriptionStr}')
    print (FilePathListByte)
    print ('\nRaw data')
    from EfiPy2.Lib.HexDump import HexDump
    HexDump (LoadOptionVariable.VarValue[:])
