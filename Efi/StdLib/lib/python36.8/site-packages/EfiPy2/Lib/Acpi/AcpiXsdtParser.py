# AcpiXsdtParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiXsdtParser (XsdtRaw):

    import copy
    import EfiPy2 as EfiPy
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    
    #
    # Get BGRT Type, object and Raw data
    #
    XsdtType    = Acpi.EFI_ACPI_DESCRIPTION_HEADER
    XsdtFields  = copy.copy (XsdtType._fields_)
    XsdtObj     = XsdtType.from_buffer (XsdtRaw)

    EntryNum    = (XsdtObj.Length - EfiPy.sizeof (XsdtType)) // 8
    XsdtFields.append (("Entry", EfiPy.UINT64 * EntryNum))

    class XsdtType (Acpi.EFIPY_INDUSTRY_STRUCTURE):
       _fields_ = XsdtFields

    XsdtObj = XsdtType.from_buffer (XsdtRaw)

    return XsdtObj, XsdtType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    XsdtFileName   = sys.argv[4]
    XsdtFileHandle = open (XsdtFileName, 'rb')
    if XsdtFileHandle == None:
      print (f"Open {XsdtFileName} error.")
      sys.exit (-1)
    XsdtRaw     = bytearray (XsdtFileHandle.read())
    
    XsdtObj, XsdtType = AcpiXsdtParser (XsdtRaw)

    DumpStruct (2, XsdtObj, XsdtType)
    print ('\n==== ACPI XSDT RAW data ======')
    HexDump (XsdtRaw)
