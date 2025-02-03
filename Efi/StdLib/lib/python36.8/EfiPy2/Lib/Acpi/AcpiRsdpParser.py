# AcpiRsdpParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiRsdpParser (RsdpRaw):

    import copy
    import EfiPy2 as EfiPy
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    
    #
    # Get BGRT Type, object and Raw data
    #
    RsdpType    = Acpi.EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER
    RsdpObj     = RsdpType.from_buffer (RsdpRaw)

    return RsdpObj, RsdpType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    RsdpFileName   = sys.argv[4]
    RsdpFileHandle = open (RsdpFileName, 'rb')
    if RsdpFileHandle == None:
      print (f"Open {RsdpFileName} error.")
      sys.exit (-1)
    RsdpRaw     = bytearray (RsdpFileHandle.read())
    
    RsdpObj, RsdpType = AcpiRsdpParser (RsdpRaw)

    DumpStruct (2, RsdpObj, RsdpType)
    print ('\n==== ACPI RSDP RAW data ======')
    HexDump (RsdpRaw)
