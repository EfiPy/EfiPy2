# AcpiRetrieveLinux.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.MdePkg.IndustryStandard.Acpi import EFI_ACPI_DESCRIPTION_HEADER as AcpiHeader
from EfiPy2.MdePkg.IndustryStandard.Acpi import EFI_ACPI_2_0_FIXED_ACPI_DESCRIPTION_TABLE as FacpType
from EfiPy2.MdePkg.IndustryStandard.Acpi import EFI_ACPI_2_0_FIRMWARE_ACPI_CONTROL_STRUCTURE as FacsType
from EfiPy2.MdePkg.IndustryStandard.Acpi import EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER as RsdpType

def FindRsdpBaseLinux ():

  try:
    SysTableHandle = open ("/sys/firmware/efi/systab", 'rb')
    SysTableBuffer = SysTableHandle.read ()
    SysTableHandle.close ()
    SystTables = SysTableBuffer.split(b'\x0a')

    Acpi20Offset = -1

    for Table in SystTables:
      Flag, Value = Table.split(b'=')
      if Flag == b'ACPI20':
        Acpi20Offset = int(Value, 16)
        break

    return Acpi20Offset, 0x00020000   # Base, Size
    
  except IOError as e:
    return 0x000E0000, 0x00020000   # Base, Size

def LoadAcpiTableLinux (MmapFile, TableBase, TableSize, Signature = None):

  import mmap
  Offset = TableBase % mmap.PAGESIZE

  MmapHandle = mmap.mmap (
                      MmapFile.fileno(),
                      length = TableSize + Offset,
                      flags  = mmap.MAP_SHARED,
                      access = mmap.ACCESS_READ,
                      offset = TableBase - Offset
                      )

  if Signature != None:
    TableOffset = MmapHandle.find (Signature)
  else:
    TableOffset = Offset
  return MmapHandle, TableOffset

def WriteAcpiRawToFile (AcpiFileName, Acpi, Raw, SigSize = 4):
  AcpiFileHandle = open (AcpiFileName, 'wb')
  AcpiFileHandle.write (bytes (Raw))
  AcpiFileHandle.close ()

  print (f'\n= {AcpiFileName} =================================================')
  try:
    print (f'Signature: {Acpi.Signature.to_bytes(SigSize, byteorder = "little")}, Length: {Acpi.Length}, OemId: {bytes (Acpi.OemId[:])}')
  except AttributeError as e:
    print (f'Signature: {Acpi.Signature.to_bytes(SigSize, byteorder = "little")}, Length: {Acpi.Length}')

def ExtractTable (AcpiTableName: bytes, AcpiIndex: int):

  RsdpBase, RsdpSize = FindRsdpBaseLinux ()

  MmapFile   = open ('/dev/mem', 'rb')

  MmapHandle, TableOffset = LoadAcpiTableLinux (MmapFile, RsdpBase, RsdpSize, b"RSD PTR ")

  if AcpiTableName == b'RSDP':
    return bytearray (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (RsdpType)])

  Rsdp = RsdpType.from_buffer_copy (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (RsdpType)])
  if Rsdp.XsdtAddress != 0:

    MmapHandle, XsdtOffset = LoadAcpiTableLinux (MmapFile, Rsdp.XsdtAddress, 0x1000, b"XSDT")

    Xsdt = AcpiHeader.from_buffer_copy (MmapHandle[XsdtOffset: XsdtOffset + EfiPy.sizeof (AcpiHeader)])

    if AcpiTableName == b'XSDT':
      return bytearray (MmapHandle[XsdtOffset: XsdtOffset + Xsdt.Length])

    TableOffset = XsdtOffset + EfiPy.sizeof (AcpiHeader)
    EntryCount = (Xsdt.Length - EfiPy.sizeof (AcpiHeader)) // 8
    TableAddresses  = (EfiPy.UINT64 * EntryCount).from_buffer_copy (MmapHandle [TableOffset: ])

  elif Rsdp.RsdtAddress != 0 and Rsdp.XsdtAddress == 0:

    MmapHandle, RsdtOffset = LoadAcpiTableLinux (MmapFile, Rsdp.RsdtAddress, 0x1000, b"RSDT")

    Rsdt = AcpiHeader.from_buffer_copy (MmapHandle[RsdtOffset: RsdtOffset + EfiPy.sizeof (AcpiHeader)])

    if AcpiTableName == b'RSDT':
      return bytearray (MmapHandle[RsdtOffset: RsdtOffset + Rsdt.Length])

    TableOffset = RsdtOffset + EfiPy.sizeof (AcpiHeader)
    EntryCount = (Rsdt.Length - EfiPy.sizeof (AcpiHeader)) // 4
    TableAddresses  = (EfiPy.UINT32 * EntryCount).from_buffer_copy (MmapHandle [TableOffset: ])

  #
  # Looking common ACPI table
  #
  FacpAddress = None
  TargetIndex = 0
  for TableAddress in TableAddresses:

    MmapHandle, TableOffset = LoadAcpiTableLinux (MmapFile, TableAddress, 0x1000)
    Table       = AcpiHeader.from_buffer_copy (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (AcpiHeader)])
    Signature   = Table.Signature.to_bytes (4, "little")

    if Signature == b'FACP':
      FacpAddress = TableAddress

    if Signature == AcpiTableName:
      if TargetIndex != AcpiIndex:
        TargetIndex += 1
        continue

      return bytearray (MmapHandle[TableOffset : TableOffset  + Table.Length])

  if AcpiTableName in (b'DSDT', b'FACS'):

    # FadtHandle, FadtOffset = LoadAcpiTableLinux (MmapFile, AcpiEntries[b'FACP'], 0x1000)
    FadtHandle, FadtOffset = LoadAcpiTableLinux (MmapFile, FacpAddress, 0x1000)
    Fadt        = FacpType.from_buffer_copy (FadtHandle[FadtOffset: FadtOffset + EfiPy.sizeof (FacpType)])

    if AcpiTableName == b'DSDT':

      if Fadt.XDsdt == 0:
        DsdtAddress = Fadt.Dsdt
      else:
        DsdtAddress = Fadt.XDsdt

      MmapHandle, DsdtOffset = LoadAcpiTableLinux (MmapFile, DsdtAddress, 0x30000)
      Dsdt       = AcpiHeader.from_buffer_copy (MmapHandle[DsdtOffset: DsdtOffset + EfiPy.sizeof (AcpiHeader)])
      return bytearray (MmapHandle[DsdtOffset: DsdtOffset + Dsdt.Length])

    if AcpiTableName == b'FACS':
      FacsAddress = Fadt.FirmwareCtrl
      FacsHandle, FacsOffset = LoadAcpiTableLinux (MmapFile, FacsAddress, EfiPy.sizeof (FacsType))
      Facs       = FacsType.from_buffer_copy (FacsHandle[FacsOffset: FacsOffset + EfiPy.sizeof (FacsType)])
      return bytearray (FacsHandle[FacsOffset: FacsOffset + Facs.Length])

def AcpiTableList (AcpiTableName: bytes, Verbose: bool):

  RsdpBase, RsdpSize = FindRsdpBaseLinux ()

  if AcpiTableName == b'RSDP':
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName is None:
    print ('RSDP  ', end=' ')

  MmapFile   = open ('/dev/mem', 'rb')

  MmapHandle, TableOffset = LoadAcpiTableLinux (MmapFile, RsdpBase, RsdpSize, b"RSD PTR ")

  Rsdp = RsdpType.from_buffer_copy (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (RsdpType)])

  if Rsdp.XsdtAddress != 0:

    if AcpiTableName == b'XSDT':
      print (f'{AcpiTableName.decode("utf-8")} exist.')
      return True
    if AcpiTableName == b'RSDT':
      print (f'{AcpiTableName.decode("utf-8")} does not exist.')
      return False
    elif AcpiTableName is None:
      print ('XSDT  ', end=' ')

    MmapHandle, XsdtOffset = LoadAcpiTableLinux (MmapFile, Rsdp.XsdtAddress, 0x1000, b"XSDT")

    Xsdt = AcpiHeader.from_buffer_copy (MmapHandle[XsdtOffset: XsdtOffset + EfiPy.sizeof (AcpiHeader)])

    TableOffset = XsdtOffset + EfiPy.sizeof (AcpiHeader)
    EntryCount = (Xsdt.Length - EfiPy.sizeof (AcpiHeader)) // 8
    TableAddresses  = (EfiPy.UINT64 * EntryCount).from_buffer_copy (MmapHandle [TableOffset: ])

  elif Rsdp.RsdtAddress != 0 and Rsdp.XsdtAddress == 0:

    if AcpiTableName == b'RSDT':
      print (f'{AcpiTableName.decode("utf-8")} exist.')
      return True
    if AcpiTableName == b'XSDT':
      print (f'{AcpiTableName.decode("utf-8")} does not exist.')
      return False
    elif AcpiTableName is None:
      print ('RSDT  ', end=' ')

    MmapHandle, RsdtOffset = LoadAcpiTableLinux (MmapFile, Rsdp.RsdtAddress, 0x1000, b"RSDT")

    Rsdt = AcpiHeader.from_buffer_copy (MmapHandle[RsdtOffset: RsdtOffset + EfiPy.sizeof (AcpiHeader)])

    TableOffset = RsdtOffset + EfiPy.sizeof (AcpiHeader)
    EntryCount = (Rsdt.Length - EfiPy.sizeof (AcpiHeader)) // 4
    TableAddresses  = (EfiPy.UINT32 * EntryCount).from_buffer_copy (MmapHandle [TableOffset: ])

  for TableAddress in TableAddresses:

    MmapHandle, TableOffset = LoadAcpiTableLinux (MmapFile, TableAddress, 0x1000)
    Table       = AcpiHeader.from_buffer_copy (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (AcpiHeader)])
    Signature   = Table.Signature.to_bytes (4, "little")

    if AcpiTableName == Signature:
      print (f'{AcpiTableName.decode("utf-8")} exist.')
      return True
    elif AcpiTableName is None:
      print (f'{Signature.decode("utf-8")}  ', end=' ')

    if Signature == b'FACP':
      FacpEntry = TableAddress

  FadtHandle, FadtOffset = LoadAcpiTableLinux (MmapFile, FacpEntry, 0x1000)
  Fadt        = FacpType.from_buffer_copy (FadtHandle[FadtOffset: FadtOffset + EfiPy.sizeof (FacpType)])

  if Fadt.XDsdt == 0:
    DsdtAddress = Fadt.Dsdt
  else:
    DsdtAddress = Fadt.XDsdt

  MmapHandle, DsdtOffset = LoadAcpiTableLinux (MmapFile, DsdtAddress, 0x30000)
  if AcpiTableName == b'DSDT':
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName is None:
    print (f'DSDT  ', end=' ')

  FacsAddress = Fadt.FirmwareCtrl
  FacsHandle, FacsOffset = LoadAcpiTableLinux (MmapFile, FacsAddress, EfiPy.sizeof (FacsType))
  if AcpiTableName == b'FACS':
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName is None:
    print (f'FACS  ', end=' ')

  MmapFile.close ()

  if AcpiTableName is not None:
    print (f'{AcpiTableName.decode('utf-8')} does not exist.')
    return False

  return True

def ExtractMain ():
  RsdpBase, RsdpSize = FindRsdpBaseLinux ()

  MmapFile   = open ('/dev/mem', 'rb')

  MmapHandle, TableOffset = LoadAcpiTableLinux (MmapFile, RsdpBase, RsdpSize, b"RSD PTR ")

  Rsdp = RsdpType.from_buffer_copy (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (RsdpType)])

  WriteAcpiRawToFile ('Acpi_RSDP.dat', Rsdp, MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (RsdpType)], SigSize = 8)

  if Rsdp.XsdtAddress != 0:

    MmapHandle, XsdtOffset = LoadAcpiTableLinux (MmapFile, Rsdp.XsdtAddress, 0x1000, b"XSDT")

    Xsdt = AcpiHeader.from_buffer_copy (MmapHandle[XsdtOffset: XsdtOffset + EfiPy.sizeof (AcpiHeader)])

    TableOffset = XsdtOffset + EfiPy.sizeof (AcpiHeader)
    EntryCount = (Xsdt.Length - EfiPy.sizeof (AcpiHeader)) // 8
    TableAddresses  = (EfiPy.UINT64 * EntryCount).from_buffer_copy (MmapHandle [TableOffset: ])

    WriteAcpiRawToFile ('Acpi_XSDT.dat', Xsdt, MmapHandle[XsdtOffset: XsdtOffset + Xsdt.Length])

  elif Rsdp.RsdtAddress != 0 and Rsdp.XsdtAddress == 0:

    MmapHandle, RsdtOffset = LoadAcpiTableLinux (MmapFile, Rsdp.RsdtAddress, 0x1000, b"RSDT")

    Rsdt = AcpiHeader.from_buffer_copy (MmapHandle[RsdtOffset: RsdtOffset + EfiPy.sizeof (AcpiHeader)])

    TableOffset = RsdtOffset + EfiPy.sizeof (AcpiHeader)
    EntryCount = (Rsdt.Length - EfiPy.sizeof (AcpiHeader)) // 4
    TableAddresses  = (EfiPy.UINT32 * EntryCount).from_buffer_copy (MmapHandle [TableOffset: ])

    WriteAcpiRawToFile ('Acpi_RSDT.dat', Rsdt, MmapHandle[RsdtOffset: RsdtOffset + Rsdt.Length])

  SsdtIndex   = 0
  SsdtAddress = []
  AcpiEntries = {}
  for TableAddress in TableAddresses:

    MmapHandle, TableOffset = LoadAcpiTableLinux (MmapFile, TableAddress, 0x1000)
    Table       = AcpiHeader.from_buffer_copy (MmapHandle[TableOffset: TableOffset + EfiPy.sizeof (AcpiHeader)])
    Signature   = Table.Signature.to_bytes (4, "little")

    if Signature == b'SSDT':
      SsdtAddress.append (TableAddress)
      if SsdtIndex == 0:
        AcpiFileName = f'Acpi_SSDT.dat'
      else:
        AcpiFileName = f'Acpi_SSDT{SsdtIndex}.dat'
      SsdtIndex += 1
    else:
      AcpiEntries[Signature] = TableAddress
      AcpiFileName = f'Acpi_{Signature.decode("utf-8")}.dat'

    WriteAcpiRawToFile (AcpiFileName, Table, MmapHandle[TableOffset: TableOffset + Table.Length])

  FadtHandle, FadtOffset = LoadAcpiTableLinux (MmapFile, AcpiEntries[b'FACP'], 0x1000)
  Fadt        = FacpType.from_buffer_copy (FadtHandle[FadtOffset: FadtOffset + EfiPy.sizeof (FacpType)])

  if Fadt.XDsdt == 0:
    DsdtAddress = Fadt.Dsdt
  else:
    DsdtAddress = Fadt.XDsdt

  MmapHandle, DsdtOffset = LoadAcpiTableLinux (MmapFile, DsdtAddress, 0x30000)
  Dsdt       = AcpiHeader.from_buffer_copy (MmapHandle[DsdtOffset: DsdtOffset + EfiPy.sizeof (AcpiHeader)])
  WriteAcpiRawToFile ('Acpi_DSDT.dat', Dsdt, MmapHandle[DsdtOffset: DsdtOffset + Dsdt.Length])

  FacsAddress = Fadt.FirmwareCtrl
  FacsHandle, FacsOffset = LoadAcpiTableLinux (MmapFile, FacsAddress, EfiPy.sizeof (FacsType))
  Facs       = FacsType.from_buffer_copy (FacsHandle[FacsOffset: FacsOffset + EfiPy.sizeof (FacsType)])
  WriteAcpiRawToFile ('Acpi_FACS.dat', Facs, FacsHandle[FacsOffset: FacsOffset + Facs.Length])

  MmapFile.close ()

if __name__ == '__main__':

  print ('''ACPI Extract utility (Linux)....
================================''')

  ExtractMain ()
