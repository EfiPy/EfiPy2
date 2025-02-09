# AcpiRetrieveWin.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import ctypes
from ctypes import wintypes

import EfiPy2 as EfiPy
from EfiPy2.Lib.StructDump import DumpStruct
from EfiPy2.MdePkg.IndustryStandard.Acpi import EFI_ACPI_DESCRIPTION_HEADER
from EfiPy2 import SIGNATURE_32, SIGNATURE2_32, SIGNATURE2_32_BE

import winreg
RegLocal = winreg.HKEY_LOCAL_MACHINE

def AcpiReadSsdtFromRegistry (Index):

  SsdtNameList = [
      'SSDT', 'SSD1', 'SSD2', 'SSD3', 'SSD4', 'SSD5', 'SSD6', 'SSD7', 'SSD8',
      'SSD9', 'SSDA', 'SSDB', 'SSDC', 'SSDD', 'SSDE', 'SSDF', 'SSDG', 'SSDH',
      'SSDI', 'SSDJ', 'SSDK', 'SSDL', 'SSDM', 'SSDN', 'SSDO', 'SSDP', 'SSDQ',
      'SSDR', 'SSDS', 'SSDT', 'SSDU', 'SSDV', 'SSDW', 'SSDX', 'SSDY', 'SSDZ',
      ]

  AcpiRegPath = fr"HARDWARE\ACPI\{SsdtNameList[Index]}"

  AcpiRegKey  = winreg.OpenKey(RegLocal, AcpiRegPath, 0, winreg.KEY_READ)

  OemIdName     = winreg.EnumKey (AcpiRegKey, 0)
  OemIdPath     = fr"{AcpiRegPath}\{OemIdName}"
  OemIdKey      = winreg.OpenKey(RegLocal, OemIdPath, 0, winreg.KEY_READ)

  OemTableIdName    = winreg.EnumKey (OemIdKey, 0)
  OemTableIdPath    = fr"{OemIdPath}\{OemTableIdName}"
  OemTableIdKey     = winreg.OpenKey(RegLocal, OemTableIdPath, 0, winreg.KEY_READ)

  OemRivisionName    = winreg.EnumKey (OemTableIdKey, 0)
  OemRivisionPath    = fr"{OemTableIdPath}\{OemRivisionName}"
  OemRivisionKey     = winreg.OpenKey(RegLocal, OemRivisionPath, 0, winreg.KEY_READ)

  v, t = winreg.QueryValueEx (OemRivisionKey, '00000000')

  winreg.CloseKey(OemRivisionKey)
  winreg.CloseKey(OemTableIdKey)
  winreg.CloseKey(OemIdKey)
  winreg.CloseKey(AcpiRegKey)
  return v

def AcpiReadFacsFromRegistry ():

  AcpiRegPath = fr"HARDWARE\ACPI\FACS"
  AcpiRegKey  = winreg.OpenKey(RegLocal, AcpiRegPath, 0, winreg.KEY_READ)

  v, t = winreg.QueryValueEx (AcpiRegKey, '00000000')

  winreg.CloseKey(AcpiRegKey)
  return v

def WriteAcpiRawToFile (AcpiFileName, AcpiTableRaw):
  AcpiFileHandle = open (AcpiFileName, 'wb')
  AcpiFileHandle.write (AcpiTableRaw)
  AcpiFileHandle.close ()

  Acpi = EFI_ACPI_DESCRIPTION_HEADER.from_buffer_copy (AcpiTableRaw)
  print (f'\n= {AcpiFileName} =================================================')
  print (f'Signature: {Acpi.Signature.to_bytes(4, byteorder = "little")}, Length: {Acpi.Length}, OemId: {bytes (Acpi.OemId[:])}')

def ExtractTable (AcpiTableName: bytes, AcpiIndex: int):

  print (f'ExtractType: {AcpiTableName}, {AcpiIndex}')

  if b'FACS' == AcpiTableName:
    return bytearray (AcpiReadFacsFromRegistry ())

  if b'SSDT' == AcpiTableName:
    return bytearray (AcpiReadSsdtFromRegistry (AcpiIndex))

  kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

  kernel32.GetSystemFirmwareTable.restype  = wintypes.UINT
  kernel32.GetSystemFirmwareTable.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD]

  AcpiSignature  = SIGNATURE2_32_BE (b'ACPI')
  AcpiTableId    = int.from_bytes (AcpiTableName, 'little')

  AcpiTableSize  = kernel32.GetSystemFirmwareTable (AcpiSignature, AcpiTableId, None, 0)
  AcpiTableRaw   = (EfiPy.UINT8 * AcpiTableSize)()
  AcpiTableSize  = kernel32.GetSystemFirmwareTable (AcpiSignature, AcpiTableId, AcpiTableRaw, AcpiTableSize)

  return bytearray (AcpiTableRaw)

def AcpiTableList (AcpiTableName: bytes, Verbose: bool):

  kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

  kernel32.EnumSystemFirmwareTables.restype  = wintypes.UINT
  kernel32.EnumSystemFirmwareTables.argtypes = [wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD]

  kernel32.GetSystemFirmwareTable.restype  = wintypes.UINT
  kernel32.GetSystemFirmwareTable.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD]

  AcpiSignature  = SIGNATURE2_32_BE (b'ACPI')
  AcpiTableSize  = kernel32.EnumSystemFirmwareTables (AcpiSignature, None, 0);
  AcpiTableNum   = AcpiTableSize // 4
  AcpiTableIndex = (EfiPy.UINT32 * AcpiTableNum)()

  AcpiTableSize  = kernel32.EnumSystemFirmwareTables (AcpiSignature, AcpiTableIndex, AcpiTableSize);
  AcpiTableDict  = dict (zip (AcpiTableIndex, [[] for _ in range (AcpiTableNum)]))

  if AcpiTableName == b'FACS' and AcpiReadFacsFromRegistry () != None:
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName == b'FACS':
    print (f'{AcpiTableName.decode("utf-8")} does not exist.')
    return False

  if AcpiTableName == b'DSDT' and kernel32.GetSystemFirmwareTable (AcpiSignature, SIGNATURE2_32 (b'DSDT'), None, 0) != 0:
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName == b'DSDT':
    print (f'{AcpiTableName.decode("utf-8")} does not exist.')
    return False

  if AcpiTableName == b'XSDT' and kernel32.GetSystemFirmwareTable (AcpiSignature, SIGNATURE2_32 (b'XSDT'), None, 0) != 0:
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName == b'XSDT':
    print (f'{AcpiTableName.decode("utf-8")} does not exist.')
    return False

  if AcpiTableName == b'RSDT' and kernel32.GetSystemFirmwareTable (AcpiSignature, SIGNATURE2_32 (b'RSDT'), None, 0) != 0:
    print (f'{AcpiTableName.decode("utf-8")} exist.')
    return True
  elif AcpiTableName == b'RSDT':
    print (f'{AcpiTableName.decode("utf-8")} does not exist.')
    return False

  if AcpiTableName is None:

    if AcpiReadFacsFromRegistry () != None:
      print ('FACS  ', end=' ')

    if kernel32.GetSystemFirmwareTable (AcpiSignature, SIGNATURE2_32 (b'DSDT'), None, 0) != 0:
      print ('DSDT  ', end=' ')
  
    if kernel32.GetSystemFirmwareTable (AcpiSignature, SIGNATURE2_32 (b'XSDT'), None, 0) != 0:
      print ('XSDT  ', end=' ')

    if kernel32.GetSystemFirmwareTable (AcpiSignature, SIGNATURE2_32 (b'RSDT'), None, 0) != 0:
      print ('RSDT  ', end=' ')

  if AcpiTableName is not None:
    print (f'{SIGNATURE2_32 (AcpiTableName)}')
    if SIGNATURE2_32 (AcpiTableName) in AcpiTableDict:
      print (f'{AcpiTableName.decode("utf-8")} exist.')
      return True
    else:
      print (f'{AcpiTableName.decode("utf-8")} does not exist.')
      return False
  else:
    for AcpiTableId in AcpiTableDict:
      print (f"{AcpiTableId.to_bytes (length = 4, byteorder = 'little').decode('utf-8')}", end = '  ')

  return True

def ExtractMain ():
  kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

  kernel32.EnumSystemFirmwareTables.restype  = wintypes.UINT
  kernel32.EnumSystemFirmwareTables.argtypes = [wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD]

  kernel32.GetSystemFirmwareTable.restype  = wintypes.UINT
  kernel32.GetSystemFirmwareTable.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD]

  AcpiSignature  = SIGNATURE2_32_BE (b'ACPI')
  AcpiTableSize  = kernel32.EnumSystemFirmwareTables (AcpiSignature, None, 0);
  AcpiTableNum   = AcpiTableSize // 4
  AcpiTableIndex = (EfiPy.UINT32 * AcpiTableNum)()

  AcpiTableSize  = kernel32.EnumSystemFirmwareTables (AcpiSignature, AcpiTableIndex, AcpiTableSize);
  AcpiTableDict  = dict (zip (AcpiTableIndex, [[] for _ in range (AcpiTableNum)]))
  AcpiTableDict[SIGNATURE2_32 (b'DSDT')] = []
  AcpiTableDict[SIGNATURE2_32 (b'XSDT')] = []
  # AcpiTableDict[SIGNATURE2_32 (b'FACS')] = []

  SsdtNumber = AcpiTableIndex[:].count(SIGNATURE2_32 (b'SSDT'))

  AcpiFileName = f'Acpi_FACS.dat'
  AcpiTableRaw = AcpiReadFacsFromRegistry ()
  WriteAcpiRawToFile (AcpiFileName, AcpiTableRaw)

  for AcpiTableId, AcpiTableList in AcpiTableDict.items():

    if AcpiTableId.to_bytes(4, byteorder = "little") == b'SSDT':

      for SsdtIndex in range (SsdtNumber):

        if SsdtIndex == 0:
          AcpiFileName = f'Acpi_SSDT.dat'
        else:
          AcpiFileName = f'Acpi_SSDT{SsdtIndex}.dat'
        AcpiTableRaw = AcpiReadSsdtFromRegistry (SsdtIndex)

        WriteAcpiRawToFile (AcpiFileName, AcpiTableRaw)

    else:
      AcpiTableSize  = kernel32.GetSystemFirmwareTable (AcpiSignature, AcpiTableId, None, 0)
      AcpiTableRaw   = (EfiPy.UINT8 * AcpiTableSize)()
      AcpiTableSize  = kernel32.GetSystemFirmwareTable (AcpiSignature, AcpiTableId, AcpiTableRaw, AcpiTableSize)

      AcpiFileName   = f'Acpi_{AcpiTableId.to_bytes(4, byteorder = "little").decode("utf-8")}.dat'

      WriteAcpiRawToFile (AcpiFileName, AcpiTableRaw)

if __name__ == '__main__':
  print ('''ACPI Extract utility (Windows)....
==================================''')

  ExtractMain ()