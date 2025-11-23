# AcpiMcfgParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiMcfgParser (McfgRaw):

  import EfiPy2 as EfiPy
  from EfiPy2.Lib.AcpiTableDb import EFIPY_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_DESCRIPTION_TABLE

  #
  # Get MCFG Type, object and Raw data
  #
  McfgType    = EFIPY_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_DESCRIPTION_TABLE
  McfgObj = McfgType.from_buffer_copy (McfgRaw)

  return McfgObj, McfgType

if __name__ == '__main__':

  import sys
  from EfiPy2.Lib.StructDump import DumpStruct
  from EfiPy2.Lib.HexDump import HexDump

  McfgFileName   = sys.argv[4]
  McfgFileHandle = open (McfgFileName, 'rb')
  if McfgFileHandle == None:
    print (f"Open {McfgFileName} error.")
    sys.exit (-1)

  McfgRaw = McfgFileHandle.read()
  McfgObj, McfgType = AcpiMcfgParser (McfgRaw)

  DumpStruct (2, McfgObj, McfgType)
  print ('\n==== ACPI MCFG RAW data ======')
  HexDump (McfgRaw)
