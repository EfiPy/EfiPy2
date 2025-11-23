# AcpiBgrtParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiBgrtParser (BgrtRaw):

    import EfiPy2 as EfiPy
    
    from EfiPy2.Lib.AcpiLib import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    
    #
    # Get BGRT Type, object and Raw data
    #
    BgrtType    = Acpi.EFI_ACPI_6_5_BOOT_GRAPHICS_RESOURCE_TABLE
    BgrtObj     = BgrtType.from_buffer (BgrtRaw)

    return BgrtObj, BgrtType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    BgrtFileName   = sys.argv[4]
    BgrtFileHandle = open (BgrtFileName, 'rb')
    if BgrtFileHandle == None:
      print (f"Open {BgrtFileName} error.")
      sys.exit (-1)
    BgrtRaw     = bytearray (BgrtFileHandle.read())
    
    BgrtObj, BgrtType = AcpiBgrtParser (BgrtRaw)

    DumpStruct (2, BgrtObj, BgrtType)
    print ('\n==== ACPI BGRT RAW data ======')
    HexDump (BgrtRaw)
