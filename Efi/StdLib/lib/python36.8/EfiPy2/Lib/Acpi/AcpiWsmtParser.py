# AcpiWsmtParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiWsmtParser (WsmtRaw):

    from EfiPy2.MdePkg.IndustryStandard import WindowsSmmSecurityMitigationTable
    
    #
    # Get BGRT Type, object and Raw data
    #
    WsmtType    = WindowsSmmSecurityMitigationTable.EFI_ACPI_WSMT_TABLE
    WsmtObj     = WsmtType.from_buffer (WsmtRaw)

    return WsmtObj, WsmtType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    WsmtFileName   = sys.argv[4]
    WsmtFileHandle = open (WsmtFileName, 'rb')
    if WsmtFileHandle == None:
      print (f"Open {WsmtFileName} error.")
      sys.exit (-1)
    WsmtRaw     = bytearray (WsmtFileHandle.read())
    
    WsmtObj, WsmtType = AcpiWsmtParser (WsmtRaw)

    DumpStruct (2, WsmtObj, WsmtType)
    print ('\n==== ACPI WSMT RAW data ======')
    HexDump (WsmtRaw)
