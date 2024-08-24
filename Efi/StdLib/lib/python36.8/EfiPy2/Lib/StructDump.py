# StructDump.py
#
# EfiPy2.Lib.StructDump
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

def DumpArray (Lead, FieldType, FieldArray, ArrayValue):
  for i, j in enumerate (ArrayValue):
    FieldName = f'{FieldArray}[{i}]'
    if   ArrayValue._type_ is EfiPy.UINT8_BE:
      if j >= 0x20 and j <= 0x7E:
        FieldString = f"0x{j:02X} '{chr (j)}'"
      else:
        FieldString = f"0x{j:02X} '.'"
      # print (f'{" " * Lead}{FieldString:>20s} {FieldName}')
      print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')
    elif   ArrayValue._type_ is EfiPy.UINT8:
      if j >= 0x20 and j <= 0x7E:
        FieldString = f"0x{j:02X} '{chr (j)}'"
      else:
        FieldString = f"0x{j:02X} '.'"
      # print (f'{" " * Lead}{FieldString:>20s} {FieldName}')
      print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

    elif   ArrayValue._type_ is EfiPy.UINT16_BE:
      FieldString = f"0x{j:04X}"
      print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')
    elif   ArrayValue._type_ is EfiPy.UINT16:
      FieldString = f"0x{j:04X}"
      print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

    elif   ArrayValue._type_ is EfiPy.UINT32_BE:
      FieldString = f"0x{j:08X}"
      print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')
    elif   ArrayValue._type_ is EfiPy.UINT32:
      FieldString = f"0x{j:08X}"
      print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

    elif   ArrayValue._type_ is EfiPy.UINT64_BE:
      FieldString = f"0x{j:016X}"
      print (f'{" " * Lead}{FieldName:59s}{FieldString:<}')
    elif   ArrayValue._type_ is EfiPy.UINT64:
      FieldString = f"0x{j:016X}"
      print (f'{" " * Lead}{FieldName:59s}{FieldString:<}')

    elif isinstance (ArrayValue[0], EfiPy.Structure):
      FieldString = f'{type(j).__name__}'
      # print (f'{" " * Lead}{" ":>20s} {FieldName}')
      print (f'{" " * Lead}{FieldName} Struct {FieldString:<}')
      DumpStruct (Lead + 2, j, type(j))

    else:
      FieldString = f'Array'
      print (f'{" " * Lead}{FieldName} {FieldString:<}')

def DumpStruct (Lead, DumpData, DumpType):
  if isinstance (DumpData, EfiPy.Structure):
    DumpObject = DumpData
  else:
    DumpObject = DumpType.from_buffer_copy  (DumpData.Value)

  # for FieldName, FieldType in DumpType._fields_:
  for FielTuple in DumpType._fields_:

    if len (FielTuple) == 2:
      FieldName, FieldType = FielTuple
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
      else:
        FieldString = f'{getattr (DumpObject, FieldName)}'
        print (f'{" " * Lead}{FieldName:63s}{FieldString:<}')

    elif len (FielTuple) == 3:
      FieldName, FieldType, FieldWidth = FielTuple
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
