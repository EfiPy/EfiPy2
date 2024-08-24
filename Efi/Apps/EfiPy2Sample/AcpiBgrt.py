# AcpiBgrt.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.Lib.AcpiLib import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType

DsdtAddress, SsdtAddress, AcpiEntries = BuildAcpiHub ()

#
# Get ACPI version
#
Major, Minor, Errata = GetAcpiVersion (AcpiEntries)
print (f'''
ACPI Version... {Major}, {Minor}, {Errata}''')

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'BGRT', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

Bgrt = AcpiType.from_address (AcpiAddr)

print (f'  Version      : 0x{Bgrt.Version:04X}');
print (f'  Status       : 0x{Bgrt.Status:02X}');
print (f'  ImageType    : 0x{Bgrt.ImageType:02X}');
print (f'  ImageAddress : 0x{Bgrt.ImageAddress:016X}');
print (f'  ImageOffsetX : {Bgrt.ImageOffsetX} 0x{Bgrt.ImageOffsetX:08X}');
print (f'  ImageOffsetY : {Bgrt.ImageOffsetY} 0x{Bgrt.ImageOffsetY:08X}');

BgrtImage = (EfiPy.UINT8 * 0x20).from_address (Bgrt.ImageAddress)
print (f'  Image Head   : {bytes(BgrtImage[:])}');
