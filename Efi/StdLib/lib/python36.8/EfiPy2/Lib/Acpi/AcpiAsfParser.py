# AcpiAsfParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#


def AcpiAsfParser (AsfRaw):

  import copy
  import EfiPy2 as EfiPy

  from EfiPy2.MdePkg.IndustryStandard import AlertStandardFormatTable as Asf
  from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE
  from EfiPy2.MdePkg.IndustryStandard.AlertStandardFormatTable     import EFI_ACPI_ASF_DESCRIPTION_HEADER

  AsfType    = EFI_ACPI_ASF_DESCRIPTION_HEADER
  AsfObj     = AsfType.from_buffer_copy (AsfRaw)
  
  def AsfRecordInfo (AsfRaw, AsfFieldPing):
    return Asf.EFI_ACPI_ASF_INFO

  def AsfRecordAlrt (AsfRaw, AsfFieldPing):

    class AsfType (EFIPY_INDUSTRY_STRUCTURE):
      pass
    TempField = copy.copy (AsfFieldPing)
    TempField.append ((f'AlrtHead', Asf.EFI_ACPI_ASF_ALRT))
    AsfType._fields_ = TempField
    AsfObj = AsfType.from_buffer_copy (AsfRaw)
  
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
  
  def AsfRecordRctl (AsfRaw, AsfFieldPing):
  
    class AsfType (EFIPY_INDUSTRY_STRUCTURE):
      pass
    TempField = copy.copy (AsfFieldPing)
    TempField.append ((f'RctlHead', Asf.EFI_ACPI_ASF_RCTL))
    AsfType._fields_ = TempField
    AsfObj = AsfType.from_buffer_copy (AsfRaw)
  
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
  
  def AsfRecordRmcp (AsfRaw, AsfFieldPing):
    return Asf.EFI_ACPI_ASF_RMCP
  
  def AsfRecordAddr (AsfRaw, AsfFieldPing):
  
    class AsfType (EFIPY_INDUSTRY_STRUCTURE):
      pass
    TempField = copy.copy (AsfFieldPing)
    TempField.append ((f'RctlHead', Asf.EFI_ACPI_ASF_ADDR))
    AsfType._fields_ = TempField
    AsfObj = AsfType.from_buffer_copy (AsfRaw)
  
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
  
  AsfFieldPing = copy.copy (AsfType._fields_)
  AsfFieldPong = copy.copy (AsfFieldPing)
  AsfFieldPong.append (('RecordHeader', Asf.EFI_ACPI_ASF_RECORD_HEADER))
  
  AsfRecordType = 0
  
  while (AsfRecordType & 0x80) != 0x80 and EfiPy.sizeof (AsfType) < AsfObj.Length:
    class AsfType (EFIPY_INDUSTRY_STRUCTURE):
      _fields_ = AsfFieldPong
  
    AsfObj = AsfType.from_buffer_copy (AsfRaw)
    AsfRecordType   = AsfObj.RecordHeader.Type
    AsfRecordLength = AsfObj.RecordHeader.RecordLength
    # print (f'AsfRecordType: 0x{AsfRecordType:02X}, AsfRecordLength:{AsfRecordLength}')
  
    # print ("==============================================================================")
    # print (f" {EfiPy.sizeof (AsfType)} {AsfObj.Length}")
    # print ("==============================================================================")
  
    RecordStruct = AsfRecordDict [AsfRecordType & 0x7F] (AsfRaw, AsfFieldPing)
    AsfFieldPing.append ((f'Record{AsfRecordIndex}', RecordStruct))

    AsfRecordIndex += 1
    AsfFieldPong = copy.copy (AsfFieldPing)
    AsfFieldPong.append (('RecordHeader', Asf.EFI_ACPI_ASF_RECORD_HEADER))
    
    if EfiPy.sizeof (AsfType) >= AsfObj.Length : break
  
  class AsfType (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = AsfFieldPing
  AsfObj = AsfType.from_buffer_copy (AsfRaw)

  return AsfObj, AsfType

if __name__ == '__main__':

  import sys
  from EfiPy2.Lib.StructDump import DumpStruct
  from EfiPy2.Lib.HexDump import HexDump

  AsfFileName   = sys.argv[4]
  AsfFileHandle = open (AsfFileName, 'rb')
  if AsfFileHandle == None:
    print (f"Open {AsfFileName} error.")
    sys.exit (-1)

  #
  # Get ASF! Type, object and Raw data
  #
  AsfRaw     = AsfFileHandle.read()
  AsfObj, AsfType = AcpiAsfParser (AsfRaw)

  DumpStruct (2, AsfObj, AsfType)

  print ('\n==== ACPI ASF RAW data ======')
  HexDump (AsfRaw)
