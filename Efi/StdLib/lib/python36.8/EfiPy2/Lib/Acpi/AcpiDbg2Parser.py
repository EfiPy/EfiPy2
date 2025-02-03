# AcpiDbg2Parser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Reference from
#
#   https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/acpi-debug-port-table
#   https://github.com/MicrosoftDocs/windows-driver-docs/blob/staging/windows-driver-docs-pr/bringup/acpi-debug-port-table.md
#

def AcpiDbg2Parser (Dbg2Raw):

    import EfiPy2 as EfiPy
    
    import copy
    from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE
    from EfiPy2.MdePkg.IndustryStandard import DebugPort2Table
    
    #
    # Get BGRT Type, object and Raw data
    #
    Dbg2Type    = DebugPort2Table.EFI_ACPI_DEBUG_PORT_2_DESCRIPTION_TABLE
    Dbg2Obj     = Dbg2Type.from_buffer (Dbg2Raw)

    Dbg2Field   = copy.copy (Dbg2Type._fields_)

    s = EfiPy.sizeof (DebugPort2Table.EFI_ACPI_DEBUG_PORT_2_DESCRIPTION_TABLE)
    t = Dbg2Obj.OffsetDbgDeviceInfo
    if s < t:
       Dbg2Field.append (("Reserved", EfiPy.UINT8 * (t - s)))

    n = range (Dbg2Obj.NumberDbgDeviceInfo)
    for idx in n:
        DevName = f"Dev{idx}"
        #
        # Create basic DBG2 device information strcture
        #
        DevField = copy.copy (DebugPort2Table.EFI_ACPI_DBG2_DEBUG_DEVICE_INFORMATION_STRUCT._fields_)
        class DevType (EFIPY_INDUSTRY_STRUCTURE):
           _fields_ = DevField
        Dbg2Field.append ((DevName, DevType))
    
        del (Dbg2Type)
        del (Dbg2Obj)
        class Dbg2Type (EFIPY_INDUSTRY_STRUCTURE):
           _fields_ = Dbg2Field

        Dbg2Obj = Dbg2Type.from_buffer (Dbg2Raw)

        #
        # Create complete DBG2 device information structure
        #
        DevObj = getattr (Dbg2Obj, DevName)

        # Base Address Register
        if DevObj.BaseAddressRegisterOffset > EfiPy.sizeof (DevType):
            DevField.append (("Reserved1", EfiPy.UINT8 * (DevObj.baseAddressRegisterOffset - EfiPy.sizeof (DevType))))
        DevField.append (("BaseAddressRegister", EfiPy.UINT32 * (3 * DevObj.NumberofGenericAddressRegisters)))

        class DevType (EFIPY_INDUSTRY_STRUCTURE):
           _fields_ = DevField

        Dbg2Field[-1] = (DevName, DevType)
        del (Dbg2Type)
        class Dbg2Type (EFIPY_INDUSTRY_STRUCTURE):
           _fields_ = Dbg2Field

        # Adress Size
        if DevObj.AddressSizeOffset > EfiPy.sizeof (DevType):
            DevField.append (("Reserved2", EfiPy.UINT8 * (DevObj.AddressSizeOffset - EfiPy.sizeof (DevType))))
        DevField.append (("AddressSize", EfiPy.UINT32 * DevObj.NumberofGenericAddressRegisters))

        class DevType (EFIPY_INDUSTRY_STRUCTURE):
           _fields_ = DevField

        Dbg2Field[-1] = (DevName, DevType)
        del (Dbg2Type)
        class Dbg2Type (EFIPY_INDUSTRY_STRUCTURE):
           _fields_ = Dbg2Field

        # NamespaceString
        if DevObj.NameSpaceStringOffset != 0:
            if DevObj.NameSpaceStringOffset > EfiPy.sizeof (DevType):
                DevField.append (("Reserved3", EfiPy.UINT8 * (DevObj.AddressSizeOffset - EfiPy.sizeof (DevType))))
            DevField.append (("NamespaceString", EfiPy.UINT8 * DevObj.NameSpaceStringLength))

            class DevType (EFIPY_INDUSTRY_STRUCTURE):
               _fields_ = DevField

            Dbg2Field[-1] = (DevName, DevType)
            del (Dbg2Type)
            class Dbg2Type (EFIPY_INDUSTRY_STRUCTURE):
               _fields_ = Dbg2Field

        # OemData
        if DevObj.OemDataOffset != 0:
            if DevObj.OemDataOffset > EfiPy.sizeof (DevType):
                DevField.append (("Reserved4", EfiPy.UINT8 * (DevObj.OemDataOffset - EfiPy.sizeof (DevType))))
            DevField.append (("OemData", EfiPy.UINT8 * DevObj.OemDataLength))

            class DevType (EFIPY_INDUSTRY_STRUCTURE):
               _fields_ = DevField

            Dbg2Field[-1] = (DevName, DevType)
            del (Dbg2Type)
            class Dbg2Type (EFIPY_INDUSTRY_STRUCTURE):
               _fields_ = Dbg2Field

        # Final
        del (Dbg2Obj)
        Dbg2Obj = Dbg2Type.from_buffer (Dbg2Raw)

    return Dbg2Obj, Dbg2Type

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    Dbg2FileName   = sys.argv[4]
    Dbg2FileHandle = open (Dbg2FileName, 'rb')
    if Dbg2FileHandle == None:
      print (f"Open {Dbg2FileName} error.")
      sys.exit (-1)
    Dbg2Raw     = bytearray (Dbg2FileHandle.read())
    
    Dbg2Obj, Dbg2Type = AcpiDbg2Parser (Dbg2Raw)

    DumpStruct (2, Dbg2Obj, Dbg2Type)
    print ('\n==== ACPI DBG2 RAW data ======')
    HexDump (Dbg2Raw)
