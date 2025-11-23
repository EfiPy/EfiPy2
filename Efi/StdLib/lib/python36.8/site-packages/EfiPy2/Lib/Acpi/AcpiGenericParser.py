# AcpiGenericParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiGenericParser (GenericRaw):

    import copy
    import EfiPy2 as EfiPy
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    
    #
    # Get BGRT Type, object and Raw data
    #
    GenericType    = Acpi.EFI_ACPI_DESCRIPTION_HEADER
    GenericObj     = GenericType.from_buffer (GenericRaw)

    # GenericFields  = copy.copy (GenericType._fields_)
    # PadBytes       = GenericObj.Length - EfiPy.sizeof (GenericType)
    # GenericFields.append (("Pad", EfiPy.UINT8 * PadBytes))

    # class GenericType (Acpi.EFIPY_INDUSTRY_STRUCTURE):
    #    _fields_ = GenericFields

    # GenericObj = GenericType.from_buffer (GenericRaw)

    return GenericObj, GenericType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    GenericFileName   = sys.argv[4]
    GenericFileHandle = open (GenericFileName, 'rb')
    if GenericFileHandle == None:
      print (f"Open {GenericFileName} error.")
      sys.exit (-1)
    GenericRaw     = bytearray (GenericFileHandle.read())
    
    GenericObj, GenericType = AcpiGenericParser (GenericRaw)

    DumpStruct (2, GenericObj, GenericType)
    print ('\n==== ACPI RAW data ======')
    HexDump (GenericRaw)
