# AcpiLib.py
#
# EfiPy2.Lib.AcpiLib
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Guid.Acpi                import gEfiAcpiTableGuid
from EfiPy2.MdePkg.IndustryStandard.Acpi20  import EFI_ACPI_DESCRIPTION_HEADER,                 \
                                                   EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE,   \
                                                   EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER
from EfiPy2.Lib.gStConfiguration            import RetrieveConfiguration, FindConfiguration
from EfiPy2.Lib.AcpiTableDb                 import AcpiDb

def ScanAcpiRsdp ():

  Rsdp = FindConfiguration (gEfiAcpiTableGuid, EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER)

  Rsdt = None if Rsdp.RsdtAddress == 0 else EFI_ACPI_DESCRIPTION_HEADER.from_address (Rsdp.RsdtAddress)
  Xsdt = None if Rsdp.RsdtAddress == 0 else EFI_ACPI_DESCRIPTION_HEADER.from_address (Rsdp.XsdtAddress)

  TableAddresses = None

  if Xsdt is None and Rsdt is not None:
    TableEntryPtr = Rsdp.RsdtAddress + EfiPy.sizeof (EFI_ACPI_DESCRIPTION_HEADER)
    EntryCount = (Rsdt.Length - EfiPy.sizeof (EFI_ACPI_DESCRIPTION_HEADER)) // 4
    TableAddresses  = (EfiPy.UINT32 * EntryCount).from_address(TableEntryPtr)

  if Xsdt is not None:
    TableEntryPtr = Rsdp.XsdtAddress + EfiPy.sizeof (EFI_ACPI_DESCRIPTION_HEADER)
    EntryCount = (Xsdt.Length - EfiPy.sizeof (EFI_ACPI_DESCRIPTION_HEADER)) // 8
    TableAddresses  = (EfiPy.UINT64 * EntryCount).from_address(TableEntryPtr)

  return Rsdp, Rsdt, Xsdt, TableAddresses

def BuildAcpiHub ():

  Rsdp, Rsdt, Xsdt, TableAddresses = ScanAcpiRsdp()

  DsdtAddress = None
  SsdtAddress = []
  AcpiEntries = {}

  for TableAddress in TableAddresses:

    Table       = EFI_ACPI_DESCRIPTION_HEADER.from_address (TableAddress)
    Signature   = Table.Signature.to_bytes (4, "little")

    if Signature == b'SSDT':
      SsdtAddress.append (TableAddress)
    else:
      AcpiEntries[Signature] = TableAddress

  Fadt = EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE.from_address (AcpiEntries[b'FACP'])
  if Fadt.XDsdt == 0:
    DsdtAddress = Fadt.Dsdt
  else:
    DsdtAddress = Fadt.XDsdt

  return DsdtAddress, SsdtAddress, AcpiEntries

def GetAcpiVersion (AcpiEntries):

  Fadt = EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE.from_address (AcpiEntries[b'FACP'])

  Major  =  Fadt.Header.Revision
  Minor  = (Fadt.Reserved2[2] & 0x0F) >> 0
  Errata = (Fadt.Reserved2[2] & 0xF0) >> 4

  return Major, Minor, Errata

def RetrieveAcpiType (SignatureByte = None, SignatureInt = None, AcpiEntries = {}):

  if SignatureInt is not None and (type (SignatureInt) in [int]):
    if SignatureByte is not None:
      raise TypeError (f'Only one of Signature parameter can be passed, SignatureByte: {SignatureByte}, SignatureInt: {SignatureInt}.')
    SignatureByte = SignatureInt.to_bytes (4, 'little')
  elif SignatureByte is not None and (type (SignatureByte) in [bytes, bytearray]):
    SignatureInt = int.from_bytes (SignatureByte, byteorder='little', signed = False)
  else:
    raise TypeError (f'Invalid parameter SignatureByte: {SignatureByte}, SignatureInt: {SignatureInt}.')

  AcpiAddr  = AcpiEntries.get (SignatureByte)
  if AcpiEntries is None or AcpiAddr is None:
    Revision = 1
  else:
    AcpiTable = EFI_ACPI_DESCRIPTION_HEADER.from_address (AcpiAddr)
    Revision = AcpiTable.Revision

  AcpiTypeDict = AcpiDb.get (SignatureByte)
  if AcpiTypeDict is None:
    return None, None
  else:
    AcpiType = None
    for v, t in AcpiTypeDict.items ():
      # print ('v Revision (Debug)', v, Revision, v <= Revision, t.__name__)
      if v <= Revision:
        AcpiType = t
      else:
        break

  return AcpiType, AcpiAddr
