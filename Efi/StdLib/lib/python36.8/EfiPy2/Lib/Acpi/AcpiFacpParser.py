# AcpiFacpParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.MdePkg.IndustryStandard import Acpi
from EfiPy2.Lib.AcpiTableDb import AcpiFacp

def AcpiFacpParser (FacpRaw):
  #
  # Get FACP Type, object and Raw data
  #
  FacpHead    = Acpi.EFI_ACPI_DESCRIPTION_HEADER.from_buffer_copy (FacpRaw)
  FacpType    = AcpiFacp [FacpHead.Revision]
  FacpObj     = FacpType.from_buffer_copy (FacpRaw)

  return FacpObj, FacpType

if __name__ == '__main__':

  import sys
  from EfiPy2.Lib.StructDump import DumpStruct
  from EfiPy2.Lib.HexDump import HexDump

  FacpFileName   = sys.argv[4]
  FacpFileHandle = open (FacpFileName, 'rb')
  if FacpFileHandle == None:
    print (f"Open {FacpFileName} error.")
    sys.exit (-1)

  FacpRaw     = FacpFileHandle.read()
  FacpObj, FacpType = AcpiFacpParser (FacpRaw)

  DumpStruct (2, FacpObj, FacpType)
  print ('\n==== ACPI FACP RAW data ======')
  HexDump (FacpRaw)
