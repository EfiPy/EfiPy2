# AcpiUefi.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.Lib.AcpiLib     import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType
from EfiPy2.Lib.AcpiTableDb import EFI_ACPI_DATA_TABLE, EFIPY_UEFI_ACPI_DATA_TABLE
from EfiPy2.Lib.StructDump import DumpStruct
from EfiPy2.Lib.HexDump import HexDump

DsdtAddress, SsdtAddress, AcpiEntries = BuildAcpiHub ()

#
# Get ACPI version
#
Major, Minor, Errata = GetAcpiVersion (AcpiEntries)
print (f'''
ACPI Version... {Major}, {Minor}, {Errata}''')

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'UEFI', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiObj = AcpiType.from_address (AcpiAddr)

from EfiPy2.MdePkg.Protocol.MmCommunication import gEfiMmCommunicationProtocolGuid

if AcpiObj.Identifier == gEfiMmCommunicationProtocolGuid:
  AcpiObj = EFIPY_UEFI_ACPI_DATA_TABLE.from_address (AcpiAddr)
  DumpStruct (2, AcpiObj, EFIPY_UEFI_ACPI_DATA_TABLE)
else:
  print ('Note... Unknown Identifier.')
  DumpStruct (2, AcpiObj, AcpiType)
  AcpiRaw = (EfiPy.UINT8 * (AcpiObj.Header.Length - EfiPy.sizeof (AcpiType))).from_address (AcpiAddr + EfiPy.sizeof (AcpiType))
  HexDump (bytes(AcpiRaw), HexOffset = EfiPy.sizeof (AcpiType))

print ('''
==================
ACPI UEFI raw data
==================''')
AcpiRaw = (EfiPy.UINT8 * AcpiObj.Header.Length).from_address (AcpiAddr)
HexDump (bytes (AcpiRaw))
