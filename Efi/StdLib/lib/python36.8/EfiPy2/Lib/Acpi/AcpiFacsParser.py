# AcpiFacsParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiFacsParser (FacsRaw):

    from EfiPy2.Lib.AcpiTableDb import AcpiFacs
    
    #
    # Get FACS Type, object and Raw data
    #
    FacsType    = AcpiFacs [1]
    FacsObj     = FacsType.from_buffer (FacsRaw)
    FacsType    = AcpiFacs [FacsObj.Version]
    FacsObj     = FacsType.from_buffer (FacsRaw)

    return FacsObj, FacsType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    FacsFileName   = sys.argv[4]
    FacsFileHandle = open (FacsFileName, 'rb')
    if FacsFileHandle == None:
      print (f"Open {FacsFileName} error.")
      sys.exit (-1)
    FacsRaw     = bytearray (FacsFileHandle.read())
    
    FacsObj, FacsType = AcpiFacsParser (FacsRaw)

    DumpStruct (2, FacsObj, FacsType)
    print ('\n==== ACPI FACS RAW data ======')
    HexDump (FacsRaw)
