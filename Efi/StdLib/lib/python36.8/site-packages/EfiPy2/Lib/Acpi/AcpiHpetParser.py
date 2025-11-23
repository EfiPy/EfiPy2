# AcpiHpetParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 -2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiHpetParser (HpetRaw):

  import EfiPy2 as EfiPy
  
  from EfiPy2.MdePkg.IndustryStandard import Acpi
  from EfiPy2.Lib.AcpiTableDb import AcpiHpet
  
  #
  # Get HPET Type, object and Raw data
  #
  
  HpetHead    = Acpi.EFI_ACPI_DESCRIPTION_HEADER.from_buffer_copy (HpetRaw)
  HpetType    = AcpiHpet [HpetHead.Revision]
  
  HpetObj     = HpetType.from_buffer_copy (HpetRaw)

  return HpetObj, HpetType
  
if __name__ == '__main__':

  import sys
  
  from EfiPy2.Lib.StructDump import DumpStruct
  from EfiPy2.Lib.HexDump import HexDump
  
  HpetFileName   = sys.argv[4]
  HpetFileHandle = open (HpetFileName, 'rb')
  if HpetFileHandle == None:
    print (f"Open {HpetFileName} error.")
    sys.exit (-1)
  
  HpetRaw     = HpetFileHandle.read()

  HpetObj, HpetType = AcpiHpetParser (HpetRaw)

  DumpStruct (2, HpetObj, HpetType)
  print ('\n==== ACPI HPET RAW data ======')
  HexDump (HpetRaw)
