# AcpiUefiParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiUefiParser (UefiRaw):

  import EfiPy2 as EfiPy

  from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE
  from EfiPy2.Lib.AcpiTableDb import AcpiUefi, EFIPY_UEFI_ACPI_DATA_TABLE
  #
  # Get Uefi Type, object and Raw data
  #
  UefiHead    = Acpi.EFI_ACPI_DESCRIPTION_HEADER.from_buffer_copy (UefiRaw)
  UefiType    = AcpiUefi [UefiHead.Revision]
  UefiObj     = UefiType.from_buffer_copy (UefiRaw)

  from EfiPy2.MdePkg.Protocol.MmCommunication import gEfiMmCommunicationProtocolGuid
  
  if UefiObj.Identifier == gEfiMmCommunicationProtocolGuid:
    if UefiObj.Header.Length < EfiPy.sizeof (EFIPY_UEFI_ACPI_DATA_TABLE):
      class EFIPY_UEFI_ACPI_DATA_TABLE (EFIPY_INDUSTRY_STRUCTURE):
        _fields_ = [
          ("Header",              Acpi.EFI_ACPI_DESCRIPTION_HEADER),
          ("Identifier",          EfiPy.GUID),
          ("DataOffset",          EfiPy.UINT16),
          ("SwSmiNumber",         EfiPy.UINT32),
          ("BufferPtrAddress",    EfiPy.UINT64),
        ]
      print ('Note... ACPI UEFI table lost InvocationRegister.\n')

    UefiType = EFIPY_UEFI_ACPI_DATA_TABLE
    UefiObj  = EFIPY_UEFI_ACPI_DATA_TABLE.from_buffer_copy (UefiRaw)

  return UefiObj, UefiType

if __name__ == '__main__':

  import sys
  from EfiPy2.Lib.StructDump import DumpStruct
  from EfiPy2.Lib.HexDump import HexDump

  UefiFileName   = sys.argv[4]
  UefiFileHandle = open (UefiFileName, 'rb')
  if UefiFileHandle == None:
    print (f"Open {UefiFileName} error.")
    sys.exit (-1)

  UefiRaw     = UefiFileHandle.read()

  UefiObj, UefiType = AcpiUefiParser (UefiRaw)

  DumpStruct (2, UefiObj, UefiType)

  print ('''
  ==================
  ACPI UEFI raw data
  ==================''')
  HexDump (UefiRaw)
