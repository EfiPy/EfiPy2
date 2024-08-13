# AcpiSample.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.Lib.AcpiLib import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType

from EfiPy2.MdePkg.IndustryStandard.Acpi20  import EFI_ACPI_DESCRIPTION_HEADER

Rsdp, Rsdt, Xsdt, TableAddresses = ScanAcpiRsdp()

print (f'''
*****************************************************************************
RSDP
  Signature        : {Rsdp.Signature.to_bytes (8, 'little')}
  OemId            : {bytes (Rsdp.OemId[:])}
  Revision         : 0x{Rsdp.Revision:02X}
  RsdtAddress      : 0x{Rsdp.RsdtAddress:08X}
  Length           : 0x{Rsdp.Length:08X}'
  XsdtAddress      : 0x{Rsdp.XsdtAddress:08X}
  ExtendedChecksum : 0x{Rsdp.ExtendedChecksum}
RSDT
  Signature        : {Rsdt.Signature.to_bytes (4, 'little')}
  OemId            : {bytes (Rsdt.OemId[:])}
  Revision         : 0x{Rsdp.Revision:02X}
XSDT
  Signature        : {Xsdt.Signature.to_bytes (4, 'little')}
  OemId            : {bytes (Xsdt.OemId[:])}
  Revision         : 0x{Rsdp.Revision:02X}
*****************************************************************************''')

DsdtAddress, SsdtAddress, AcpiEntries = BuildAcpiHub ()

#
# Get DSDT table
#
Dsdt = EFI_ACPI_DESCRIPTION_HEADER.from_address (DsdtAddress)
print (f'''
*****************************************************************************
DSDT
  Signature: {Dsdt.Signature.to_bytes (4, 'little')}, OemId: {bytes (Dsdt.OemId[:])}
*****************************************************************************''')

#
# Get SSDT table
#
print (f'\n*****************************************************************************')
for i, SsdtAddr in enumerate (SsdtAddress):
  Ssdt = EFI_ACPI_DESCRIPTION_HEADER.from_address (SsdtAddr)
  print (f"  Signature: {Ssdt.Signature.to_bytes (4, 'little')}, OemId: {bytes (Ssdt.OemId[:])}")
print (f'*****************************************************************************')

#
# Dump every ACPI Signature by AcpiEntries
#
print (f'\n*****************************************************************************')
for AcpiId, AcpiAddr in AcpiEntries.items ():
  Acpi = EFI_ACPI_DESCRIPTION_HEADER.from_address (AcpiAddr)
  print (f"{AcpiId},  Signature: {Acpi.Signature.to_bytes (4, 'little')}, OemId: {bytes (Acpi.OemId[:])}, Revision: 0x{Acpi.Revision:02X}")
print (f'*****************************************************************************')

#
# Get ACPI version
#
Major, Minor, Errata = GetAcpiVersion (AcpiEntries)
print (f'''
ACPI Version... {Major}, {Minor}, {Errata}''')

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'MCFG', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'TPM2', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'APIC', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'BGRT', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'FACP', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');
AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'FACP')
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'bbbb', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType}, AcpiAddr: {AcpiAddr}');