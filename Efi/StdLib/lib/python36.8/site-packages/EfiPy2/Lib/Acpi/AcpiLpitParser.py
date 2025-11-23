# AcpiLpitParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Reference
#
#   https://docs.kernel.org/firmware-guide/acpi/lpit.html
#   https://uefi.org/sites/default/files/resources/Intel_ACPI_Low_Power_S0_Idle.pdf
#

def AcpiLpitParser (LpitRaw):

    import EfiPy2 as EfiPy
    import copy
    from EfiPy2.MdePkg.IndustryStandard import LowPowerIdleTable
    from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    
    #
    # Get FACS Type, object and Raw data
    #
    LpitFields  = copy.copy (Acpi.EFI_ACPI_DESCRIPTION_HEADER._fields_)
    LpitObj     = Acpi.EFI_ACPI_DESCRIPTION_HEADER.from_buffer (LpitRaw)
    LpitNum     = (LpitObj.Length - EfiPy.sizeof (Acpi.EFI_ACPI_DESCRIPTION_HEADER)) // EfiPy.sizeof (LowPowerIdleTable.ACPI_LPI_NATIVE_CSTATE_DESCRIPTOR)
    LpitFields.append (('C_state', LowPowerIdleTable.ACPI_LPI_NATIVE_CSTATE_DESCRIPTOR * LpitNum))

    class LpitType (EFIPY_INDUSTRY_STRUCTURE):
       _fields_ = LpitFields

    LpitObj     = LpitType.from_buffer (LpitRaw)

    return LpitObj, LpitType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    LpitFileName   = sys.argv[4]
    LpitFileHandle = open (LpitFileName, 'rb')
    if LpitFileHandle == None:
      print (f"Open {LpitFileName} error.")
      sys.exit (-1)
    LpitRaw     = bytearray (LpitFileHandle.read())
    
    LpitObj, LpitType = AcpiLpitParser (LpitRaw)

    DumpStruct (2, LpitObj, LpitType)
    print ('\n==== ACPI LPIT RAW data ======')
    HexDump (LpitRaw)
