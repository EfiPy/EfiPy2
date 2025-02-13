# AcpiFpdtParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiFpdtParser (FpdtRaw):

    import copy
    import EfiPy2 as EfiPy
    
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    
    #
    # Get FPDT Type, object and Raw data
    #
    FpdtRecord  = 0
    FpdtType    = Acpi.EFI_ACPI_6_5_FIRMWARE_PERFORMANCE_RECORD_TABLE
    FpdtField   = copy.copy(FpdtType._fields_)
    FpdtObj     = FpdtType.from_buffer (FpdtRaw)

    while True:

        FpdtRecordName = f"FpdtRecord_{FpdtRecord}"
        FpdtField.append ((FpdtRecordName, Acpi.EFI_ACPI_6_5_FPDT_PERFORMANCE_RECORD_HEADER))
        FpdtObj        = FpdtType.from_buffer (FpdtRaw)
        class FpdtType (Acpi.EFIPY_INDUSTRY_STRUCTURE):
            _fields_ = FpdtField
        FpdtObj     = FpdtType.from_buffer (FpdtRaw)

        FpdtRecordObj  = getattr (FpdtObj, FpdtRecordName)
        if   FpdtRecordObj.Type == 0:
          FpdtField [-1] = ((FpdtRecordName, Acpi.EFI_ACPI_6_5_FPDT_BOOT_PERFORMANCE_TABLE_POINTER_RECORD))
        elif FpdtRecordObj.Type == 1:
          FpdtField [-1] = ((FpdtRecordName, Acpi.EFI_ACPI_6_5_FPDT_S3_PERFORMANCE_TABLE_POINTER_RECORD))

        class FpdtType (Acpi.EFIPY_INDUSTRY_STRUCTURE):
            _fields_ = FpdtField
        FpdtObj     = FpdtType.from_buffer (FpdtRaw)

        if FpdtObj.Header.Length <= EfiPy.sizeof (FpdtObj):
            break

        FpdtRecord += 1

        # if FpdtRecord >= 1:
        #     break

    return FpdtObj, FpdtType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    FpdtFileName   = sys.argv[4]
    FpdtFileHandle = open (FpdtFileName, 'rb')
    if FpdtFileHandle == None:
      print (f"Open {FpdtFileName} error.")
      sys.exit (-1)
    FpdtRaw     = bytearray (FpdtFileHandle.read())
    
    FpdtObj, FpdtType = AcpiFpdtParser (FpdtRaw)

    DumpStruct (2, FpdtObj, FpdtType)
    print ('\n==== ACPI BGRT RAW data ======')
    HexDump (FpdtRaw)
