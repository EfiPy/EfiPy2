# StructDump.py
#
# EfiPy2.Lib.StructDump
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.Lib.HexDump import HexDump

FieldNameDict = {
  EfiPy.UINT8:      ('UINT8',     2,  63),
  EfiPy.UINT8_BE:   ('UINT8',     2,  63),
  EfiPy.UINT16:     ('UINT16',    4,  63),
  EfiPy.UINT16_BE:  ('UINT16',    4,  63),
  EfiPy.UINT32:     ('UINT32',    8,  63),
  EfiPy.UINT32_BE:  ('UINT32',    8,  63),
  EfiPy.UINT64:     ('UINT64',    16, 59),
  EfiPy.UINT64_BE:  ('UINT64',    16, 59),
  EfiPy.Structure:  ('Structure', 16, 59),
  EfiPy.Union:      ('Union',     16, 59),
}

def DumpArray (Lead, FieldType, FieldArray, ArrayValue):

  ValueType, ValueDigit, FieldWitdth = FieldNameDict.get (ArrayValue._type_, ("Array", 16, 59))

  FieldName = f'{FieldArray} << {ValueType} * {len (ArrayValue)} (0x{len (ArrayValue):04X}) >>'

  if ArrayValue._type_ in (EfiPy.UINT8_BE, EfiPy.UINT8):
    print (' ' * Lead + FieldName)
    HexDump (ArrayValue, DumpLead = Lead, OffsetDigit=2)
    print ()

  elif ArrayValue._type_ in (EfiPy.UINT16_BE, EfiPy.UINT16, EfiPy.UINT32, EfiPy.UINT32_BE, EfiPy.UINT64, EfiPy.UINT64_BE):
    for i, j in enumerate (ArrayValue):
      FieldName = f'{FieldArray}[{i}]'
      FieldString = f"0x{j:{0}{ValueDigit}X}"
      print (f'{" " * Lead}{FieldName:{FieldWitdth}s}{FieldString:<}')

  elif isinstance (ArrayValue[0], EfiPy.Structure):
    for i, j in enumerate (ArrayValue):
      FieldName = f'{FieldArray}[{i}]'
      FieldString = f'{type(j).__name__}'
      print (f'{" " * Lead}{FieldName:63s}Struct {FieldString:<}')
      DumpStruct (Lead + 2, j, type(j))

  elif isinstance (ArrayValue[0], EfiPy.Union):
    for i, j in enumerate (ArrayValue):
      FieldName = f'{FieldArray}[{i}]'
      FieldString = f'{type(j).__name__}'
      print (f'{" " * Lead}{FieldName:63s}Union {FieldString:<}')
      DumpStruct (Lead + 2, j, type(j))

  else:
    FieldString = f'Array'
    print (f'{" " * Lead}{FieldName} {FieldString:<}')

def DumpStruct (Lead, DumpData, DumpType):
  if isinstance (DumpData, (EfiPy.Structure, EfiPy.Union)):
    DumpObject = DumpData
  else:
    DumpObject = DumpType.from_buffer_copy  (DumpData.Value)

  # for FieldName, FieldType in DumpType._fields_:
  for FieldTuple in DumpType._fields_:

    if len (FieldTuple) == 2:
      FieldName, FieldType = FieldTuple
      FieldValue = getattr (DumpObject, FieldName)

      if isinstance (FieldValue, EfiPy.GUID):
        FieldString = f'{getattr (DumpObject, FieldName)}'
        print (f'{" " * Lead}{FieldName:39s}{FieldString:<}')

      elif FieldType is EfiPy.UINT8_BE:
        FieldString = f'0x{getattr (DumpObject, FieldName):02X}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

      elif FieldType is EfiPy.UINT8:
        FieldString = f'0x{getattr (DumpObject, FieldName):02X}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

      elif FieldType is EfiPy.UINT16_BE:
        FieldString = f'0x{getattr (DumpObject, FieldName):04X}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

      elif FieldType is EfiPy.UINT16:
        FieldString = f'0x{getattr (DumpObject, FieldName):04X}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

      elif FieldType is EfiPy.UINT32_BE:
        FieldString = f'0x{getattr (DumpObject, FieldName):08X}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

      elif FieldType is EfiPy.UINT32:
        FieldString = f'0x{getattr (DumpObject, FieldName):08X}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

      elif FieldType is EfiPy.UINT64_BE:
        FieldString = f'0x{getattr (DumpObject, FieldName):016X}'
        print (f'{" " * Lead}{FieldName:55s}{FieldString:<}')

      elif FieldType is EfiPy.UINT64:
        FieldString = f'0x{getattr (DumpObject, FieldName):016X}'
        print (f'{" " * Lead}{FieldName:55s}{FieldString:<}')

      elif isinstance (FieldValue, EfiPy.Array):
        DumpArray (Lead, FieldType, FieldName, FieldValue)

      elif isinstance (FieldValue, EfiPy.Structure):
        FieldString = f'0x{getattr (DumpObject, FieldName)}'
        print (f'{" " * Lead}{FieldName:63s}Struct {type (FieldValue).__name__:<}')
        DumpStruct (Lead + 2, FieldValue, type(FieldValue))

      elif isinstance (FieldValue, EfiPy.Union):
        FieldString = f'0x{getattr (DumpObject, FieldName)}'
        print (f'{" " * Lead}{FieldName:63s}Union {type (FieldValue).__name__:<}')
        DumpStruct (Lead + 2, FieldValue, type(FieldValue))

      elif type(type(FieldValue)).__name__ == 'PyCPointerType':
        FieldString = f'{getattr (DumpObject, FieldName)}'
        # TODO - Dump Poiter address and pointer type
        print (f'{"-" * Lead}{FieldName:63s}{FieldString:<}')

      else:
        FieldString = f'{getattr (DumpObject, FieldName)}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

    elif len (FieldTuple) == 3:
      FieldName, FieldType, FieldWidth = FieldTuple
      FieldValue = getattr (DumpObject, FieldName)
      if FieldType is EfiPy.UINT8:
        FieldString = f'0x{getattr (DumpObject, FieldName):02X} ({FieldWidth})'
      elif FieldType is EfiPy.UINT16:
        FieldString = f'0x{getattr (DumpObject, FieldName):04X} ({FieldWidth})'
      elif FieldType is EfiPy.UINT32:
        FieldString = f'0x{getattr (DumpObject, FieldName):08X} ({FieldWidth})'
      elif FieldType is EfiPy.UINT64:
        FieldString = f'0x{getattr (DumpObject, FieldName):016X} ({FieldWidth})'

      print (f'{" " * Lead}{FieldName:55s}{FieldString:<}')
