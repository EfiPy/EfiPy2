# AcpiHpet.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.Lib.AcpiLib import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType
from EfiPy2.Lib.StructDump import DumpStruct

DsdtAddress, SsdtAddress, AcpiEntries = BuildAcpiHub ()

#
# Get ACPI version
#
Major, Minor, Errata = GetAcpiVersion (AcpiEntries)
print (f'''
ACPI Version... {Major}, {Minor}, {Errata}''')

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'HPET', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiObj = AcpiType.from_address (AcpiAddr)
DumpStruct (2, AcpiObj, AcpiType)