# Acpi_Bgrt.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Reference from https://uefi.org/acpi
#
import EfiPy2
from EfiPy2.Lib.StructDump import DumpStruct
from EfiPy2.Lib.HexDump import HexDump

def GetBufFromPa (Pa: int):
  import os
  if os.name == 'nt':
    return -1
  elif os.name == 'edk2':
    return bytes ((EfiPy2.UINT8 * 4096).from_address (Pa)), 0

  import mmap

  MmapFile = open ('/dev/mem', 'rb')
  Offset  = Pa % mmap.PAGESIZE
  MapSize = mmap.PAGESIZE - Offset

  MmapHandle = mmap.mmap (
                      MmapFile.fileno(),
                      length = mmap.PAGESIZE + Offset,
                      flags  = mmap.MAP_SHARED,
                      access = mmap.ACCESS_READ,
                      offset = Pa - Offset
                      )
  MmapFile.close ()

  return MmapHandle, Offset

def ParsingBgrtImage (BgrtObj):

  from EfiPy2.MdePkg.IndustryStandard import Acpi
  from EfiPy2.MdePkg.IndustryStandard import Bmp

  Entry = BgrtObj.ImageAddress
  BgrtMem, Offset = GetBufFromPa (Entry)
  DumpSize = 0x30
  if BgrtObj.ImageType == Acpi.EFI_ACPI_5_0_BGRT_IMAGE_TYPE_BMP:
    print (f"""
BMP Image Header:
=======================================================================================================================""")
    VaBuff, Offset = GetBufFromPa (Entry)
    BmpType   = Bmp.BMP_IMAGE_HEADER
    BmpHeader = Bmp.BMP_IMAGE_HEADER.from_buffer_copy (BgrtMem[Offset : Offset + EfiPy2.sizeof (BmpType)])
    from EfiPy2.Lib.StructDump import DumpStruct
    DumpStruct (2, BmpHeader, BmpType)
    DumpSize = EfiPy2.sizeof (BmpHeader)

  print (f"""
BGRT Image Address: 0x{Entry:08X}
=======================================================================================================================""")
  VaBuff, Offset = GetBufFromPa (Entry)

  HexDump (VaBuff[Offset: Offset + DumpSize])

if __name__ == '__main__':
    from EfiPy2.Lib.Acpi.AcpiBgrtParser import AcpiBgrtParser
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    BgrtSignature = b'BGRT'

    import os
    if os.name == 'nt':
      from EfiPy2.Lib.Acpi.AcpiRetrieveWin  import ExtractTable
    elif os.name == 'posix':
      from EfiPy2.Lib.Acpi.AcpiRetrieveLinux  import ExtractTable
    elif os.name == 'edk2':
      from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable

    BgrtRaw = ExtractTable (BgrtSignature, 0)
    BgrtObj, BgrtType = AcpiBgrtParser (BgrtRaw)

    print (f"""
Firmware Performance Descript Table (FPDT)
=======================================================================================================================""")
    DumpStruct (2, BgrtObj, BgrtType)

    ParsingBgrtImage (BgrtObj)