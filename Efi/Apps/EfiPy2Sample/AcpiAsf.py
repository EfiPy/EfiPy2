# AcpiAsf.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
import copy

from EfiPy2.MdePkg.IndustryStandard import AlertStandardFormatTable as Asf
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE
from EfiPy2.Lib.AcpiLib import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType
from EfiPy2.Lib.StructDump import DumpStruct
from EfiPy2.Lib.HexDump import HexDump

DsdtAddress, SsdtAddress, AcpiEntries = BuildAcpiHub ()

#
# Get ACPI version
#
Major, Minor, Errata = GetAcpiVersion (AcpiEntries)
print (f'''
ACPI Version... {Major}, {Minor}, {Errata}''')

AcpiType, AcpiAddr = RetrieveAcpiType (SignatureByte = b'ASF!', AcpiEntries = AcpiEntries)
print (f'AcpiType: {AcpiType.__name__}, AcpiAddr: {AcpiAddr}');

AsfObj = AcpiType.from_address (AcpiAddr)

def AsfRecordInfo (AcpiAddr, AsfFieldPing):
  return Asf.EFI_ACPI_ASF_INFO

def AsfRecordAlrt (AcpiAddr, AsfFieldPing):

  class AsfType (EFIPY_INDUSTRY_STRUCTURE):
    pass
  TempField = copy.copy (AsfFieldPing)
  TempField.append ((f'AlrtHead', Asf.EFI_ACPI_ASF_ALRT))
  AsfType._fields_ = TempField
  AsfObj = AsfType.from_address (AcpiAddr)

  class EFI_ACPI_ASF_ALERTDATA (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("DeviceAddress",     EfiPy.UINT8),
      ("Command",           EfiPy.UINT8),
      ("DataMask",          EfiPy.UINT8),
      ("CompareValue",      EfiPy.UINT8),
      ("EventSenseType",    EfiPy.UINT8),
      ("EventType",         EfiPy.UINT8),
      ("EventOffset",       EfiPy.UINT8),
      ("EventSourceType",   EfiPy.UINT8),
      ("EventSeverity",     EfiPy.UINT8),
      ("SensorNumber",      EfiPy.UINT8),
      ("Entity",            EfiPy.UINT8),
      ("EntityInstance",    EfiPy.UINT8),
      ("Padding",           EfiPy.UINT8 * (AsfObj.AlrtHead.ArrayElementLength - EfiPy.sizeof (Asf.EFI_ACPI_ASF_ALERTDATA))),
    ]

  class EFI_ACPI_ASF_ALRT (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("RecordHeader",            Asf.EFI_ACPI_ASF_RECORD_HEADER),
      ("AssertionEventBitMask",   EfiPy.UINT8),
      ("DeassertionEventBitMask", EfiPy.UINT8),
      ("NumberOfAlerts",          EfiPy.UINT8),
      ("ArrayElementLength",      EfiPy.UINT8),
      ("DeviceArray",             EFI_ACPI_ASF_ALERTDATA * AsfObj.AlrtHead.NumberOfAlerts)
    ]

  del (AsfObj)
  del (AsfType)

  return EFI_ACPI_ASF_ALRT
  # return Asf.EFI_ACPI_ASF_ALRT

def AsfRecordRctl (AcpiAddr, AsfFieldPing):

  class AsfType (EFIPY_INDUSTRY_STRUCTURE):
    pass
  TempField = copy.copy (AsfFieldPing)
  TempField.append ((f'RctlHead', Asf.EFI_ACPI_ASF_RCTL))
  AsfType._fields_ = TempField
  AsfObj = AsfType.from_address (AcpiAddr)

  class EFI_ACPI_ASF_RCTL (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("RecordHeader",        Asf.EFI_ACPI_ASF_RECORD_HEADER),
      ("NumberOfControls",    EfiPy.UINT8),
      ("ArrayElementLength",  EfiPy.UINT8),
      ("RctlReserved",        EfiPy.UINT16),
      ("DeviceArray",         Asf.EFI_ACPI_ASF_CONTROLDATA * AsfObj.RctlHead.NumberOfControls)
    ]

  del (AsfObj)
  del (AsfType)

  return EFI_ACPI_ASF_RCTL

def AsfRecordRmcp (AcpiAddr, AsfFieldPing):
  return Asf.EFI_ACPI_ASF_RMCP

def AsfRecordAddr (AcpiAddr, AsfFieldPing):

  class AsfType (EFIPY_INDUSTRY_STRUCTURE):
    pass
  TempField = copy.copy (AsfFieldPing)
  TempField.append ((f'RctlHead', Asf.EFI_ACPI_ASF_ADDR))
  AsfType._fields_ = TempField
  AsfObj = AsfType.from_address (AcpiAddr)

  class EFI_ACPI_ASF_ADDR (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
    ("RecordHeader",        Asf.EFI_ACPI_ASF_RECORD_HEADER),
    ("SEEPROMAddress",      EfiPy.UINT8),
    ("NumberOfDevices",     EfiPy.UINT8),
    ("FixedSmbusAddresses", EfiPy.UINT8 * AsfObj.RctlHead.NumberOfDevices)
    ]

  del (AsfObj)
  del (AsfType)

  return EFI_ACPI_ASF_ADDR

AsfRecordDict = {
  0x00: AsfRecordInfo,
  0x01: AsfRecordAlrt,
  0x02: AsfRecordRctl,
  0x03: AsfRecordRmcp,
  0x04: AsfRecordAddr,
  }
AsfRecordIndex = 0

AsfType      = AcpiType
AsfFieldPing = copy.copy (AcpiType._fields_)
AsfFieldPong = copy.copy (AsfFieldPing)
AsfFieldPong.append (('RecordHeader', Asf.EFI_ACPI_ASF_RECORD_HEADER))

AsfRecordType = 0

ParseDonw = True

while (AsfRecordType & 0x80) != 0x80 and EfiPy.sizeof (AsfType) < AsfObj.Length:
  class AsfType (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = AsfFieldPong

  AsfObj = AsfType.from_address (AcpiAddr)
  AsfRecordType   = AsfObj.RecordHeader.Type
  AsfRecordLength = AsfObj.RecordHeader.RecordLength
  # print (f'AsfRecordType: 0x{AsfRecordType:02X}, AsfRecordLength:{AsfRecordLength}')

  # print ("==============================================================================")
  # print (f" {EfiPy.sizeof (AsfType)} {AsfObj.Length}")
  # print ("==============================================================================")

  try:
    RecordStruct = AsfRecordDict [AsfRecordType & 0x7F] (AcpiAddr, AsfFieldPing)
    AsfFieldPing.append ((f'Record{AsfRecordIndex}', RecordStruct))

    AsfRecordIndex += 1
    AsfFieldPong = copy.copy (AsfFieldPing)
    AsfFieldPong.append (('RecordHeader', Asf.EFI_ACPI_ASF_RECORD_HEADER))
  except KeyError as e:
    ParseDonw = False
    # print (e)
    break

  if EfiPy.sizeof (AsfType) >= AsfObj.Length : break

class AsfType (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = AsfFieldPing
AsfObj = AsfType.from_address (AcpiAddr)
DumpStruct (2, AsfObj, AsfType)

if ParseDonw == False:
  print ('\nParsing ASF! is not finished, Dump ASF! raw data')
  AsfRaw = (EfiPy.UINT8 * AsfObj.Length).from_address (AcpiAddr)
  HexDump (bytes (AsfRaw))
