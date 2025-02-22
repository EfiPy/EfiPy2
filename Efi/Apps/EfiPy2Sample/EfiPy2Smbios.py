#!/usr/bin/python

#
# EfiPy2Smbios.py
#
# Copyright (C) 2016 - 2025 MaxWu efipy.core@gmail.com All rights reserved.
#
# EfiPy2Smbios.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Protocol import Smbios as sb
import EfiPy2.MdePkg.IndustryStandard.SmBios as Isb
from EfiPy2.Lib.HexDump import HexDump
from EfiPy2.Lib.StructDump import DumpStruct

SmbiosDumpDict  = {}

def SmbiosDumpArray (DumpLevel, ArrayValue):

  if   id (ArrayValue._type_) == id(EfiPy.UINT8):
    print ("    " * DumpLevel, end = '')
    for Valu in ArrayValue:
      print ('0x%02X ' % Valu, end = '')
    print ('')

  elif id (ArrayValue._type_) == id(EfiPy.UINT16):
    print ("    " * DumpLevel, end = '')
    for Valu in ArrayValue:
      print ('0x%04X ' % Valu, end = '')
    print ('')

  elif id (ArrayValue._type_) == id(EfiPy.UINT32):
    print ("    " * DumpLevel, end = '')
    for Valu in ArrayValue:
      print ('0x%08X ' % Valu, end = '')
    print ('')

  elif id (ArrayValue._type_) == id(EfiPy.UINT64):
    print ("    " * DumpLevel, end = '')
    for Valu in ArrayValue:
      print ('0x%016X ' % Valu, end = '')
    print ('')

  elif id (ArrayValue._type_) == id(EfiPy.GUID):
    for Index, Valu in enumerate (ArrayValue):
      print ("    " * DumpLevel + '%d: %s' % (Index, Valu))

def SmbiosDumpStruct3 (DumpLevel, SmbiosStruct):
  for RecordKey, RecordClass, RecordField in SmbiosStruct._fields_:
    print ("    " * DumpLevel + "%s (%d): 0x%X" % (RecordKey, RecordField, getattr (SmbiosStruct, RecordKey)))

def SmbiosDumpStruct2 (DumpLevel, SmbiosStruct):

  for RecordKey, RecordClass in SmbiosStruct._fields_:

    KeyValue = getattr (SmbiosStruct, RecordKey)

    try:

      SmbiosDumpFunc = SmbiosDumpDict[id(RecordClass)]
      SmbiosDumpFunc (DumpLevel, SmbiosStruct, RecordKey, KeyValue)

    except KeyError:

      if isinstance (KeyValue, EfiPy.Array):
        print ("    " * DumpLevel + "%s: (ARRAY, length: %d)" % (RecordKey, len (KeyValue)))
        SmbiosDumpArray (DumpLevel + 1, KeyValue)

      elif isinstance (KeyValue, EfiPy.Structure)or isinstance (KeyValue, EfiPy.Union):

        print ("    " * DumpLevel + "%s: (%s)" % (RecordKey, RecordClass))

        if   len (RecordClass._fields_[0]) == 2:
          SmbiosDumpStruct2 (DumpLevel + 1, KeyValue)

        elif len (RecordClass._fields_[0]) == 3:
          SmbiosDumpStruct3 (DumpLevel + 1, KeyValue)

      else:
        print ("    " * DumpLevel + "%s %s" % (RecordKey, RecordClass))

def SmbiosBuildStrings (SmbiosRecord):

  SmbiosRecord.Strings = []

  SmbiosStrAddr = EfiPy.addressof (SmbiosRecord) + SmbiosRecord.Hdr.Length

  SmbiosStrObj = EfiPy.PCHAR8(SmbiosStrAddr)
  while len (SmbiosStrObj.value) != 0:
    SmbiosRecord.Strings.append (SmbiosStrObj)
    SmbiosStrAddr += len (SmbiosStrObj.value) + 1
    SmbiosStrObj   = EfiPy.PCHAR8(SmbiosStrAddr)

def SmbiosDumpString (DumpLevel, SmbiosRecord, RecordKey, KeyValue):

  print ("    " * DumpLevel +  "%s (SMBIOS_TABLE_STRING, %d): " % (RecordKey, KeyValue.value), end = '')

  try:
    SmbiosString = SmbiosRecord.Strings [KeyValue.value - 1]
    print (SmbiosString.value)
  except AttributeError:
    print ('[%s]' % SmbiosString)
  except IndexError:
    print ('[Index Error]')

def SmbiosDumpUint8 (DumpLevel, SmbiosRecord, RecordKey, KeyValue):
  print ("    " * DumpLevel +  "%s (UINT8): 0x%02X" % (RecordKey, KeyValue))

def SmbiosDumpUint16 (DumpLevel, SmbiosRecord, RecordKey, KeyValue):
  print ("    " * DumpLevel +  "%s (UINT16): 0x%04X" % (RecordKey, KeyValue))

def SmbiosDumpUint32 (DumpLevel, SmbiosRecord, RecordKey, KeyValue):
  print ("    " * DumpLevel +  "    " * DumpLevel +  "%s (UINT32): 0x%08X" % (RecordKey, KeyValue))

def SmbiosDumpUint64 (DumpLevel, SmbiosRecord, RecordKey, KeyValue):
  print ("    " * DumpLevel +  "%s (UINT64): 0x%08X" % (RecordKey, KeyValue))

def SmbiosDumpGuid (DumpLevel, SmbiosRecord, RecordKey, KeyValue):
  print ("    " * DumpLevel +  "%s (GUID): %s" % (RecordKey, KeyValue))

SmbiosDumpDict [id(Isb.SMBIOS_TABLE_STRING) ] = SmbiosDumpString
SmbiosDumpDict [id(EfiPy.UINT8)             ] = SmbiosDumpUint8
SmbiosDumpDict [id(EfiPy.UINT16)            ] = SmbiosDumpUint16
SmbiosDumpDict [id(EfiPy.UINT32)            ] = SmbiosDumpUint32
SmbiosDumpDict [id(EfiPy.UINT64)            ] = SmbiosDumpUint64
SmbiosDumpDict [id(EfiPy.GUID)              ] = SmbiosDumpGuid

def SmbiosDumpMain (SmbiosRecord, DumpContent = False, DumpRaw = False, DumpString = False):

  #
  #  SMBIOS_STRUCTURE           *SmbiosRecord;
  #  SMBIOS_STRUCTURE_POINTER   SmbiosPointer;
  #
  #  &SmbiosPointer = SmbiosRecord;
  #

  SmbiosPointer = EfiPy.POINTER(Isb.SMBIOS_STRUCTURE_POINTER)(SmbiosRecord)[0]
  SmbiosHdr     = SmbiosPointer.Hdr[0]
  print (f'''
=======================================
Handle 0x{SmbiosHdr.Handle:04X}, DMI type {SmbiosHdr.Type}, {SmbiosHdr.Length} bytes
=======================================''')
  SmbiosType = 'Type%d' % SmbiosHdr.Type
  SmbiosTypeX = getattr (SmbiosPointer, SmbiosType, SmbiosPointer.Oem)[0]
  SmbiosBuildStrings (SmbiosTypeX)

  if DumpContent == True:
    SmbiosDumpStruct2 (0, SmbiosTypeX)
    # DumpStruct (2, SmbiosTypeX, type (SmbiosTypeX))

  if DumpRaw == True:
    Raw = (EfiPy.CHAR8 * SmbiosHdr.Length).from_address (EfiPy.addressof (SmbiosHdr))
    print (f'''
RAW:''')
    HexDump (bytes(Raw))

  if DumpString == True:
    print ("\nStrings:\n--------")
    for i, s in enumerate (SmbiosTypeX.Strings, 1):
      print (" %d): %s" % (i, s.value))

if __name__ == "__main__":

  Interface = EfiPy.PVOID ()

  Status = EfiPy.gBS.LocateProtocol (
                  EfiPy.byref (sb.gEfiSmbiosProtocolGuid),
                  None,
                  EfiPy.byref (Interface)
                  )
  if EfiPy.EFI_ERROR(Status):
    print ("Error: %x" % Status)
    exit (0)

  SmbiosProtocol = EfiPy.cast (Interface, EfiPy.POINTER(sb.EFI_SMBIOS_PROTOCOL))

  print ('''SMBIOS
    MajorVersion: %d
    MinorVersion: %d'''% (SmbiosProtocol[0].MajorVersion, SmbiosProtocol[0].MinorVersion))

  SmbiosHandle = sb.EFI_SMBIOS_HANDLE (Isb.SMBIOS_HANDLE_PI_RESERVED)

  SmbiosRecord = EfiPy.POINTER(sb.EFI_SMBIOS_TABLE_HEADER)()

  while (1):
    Status = SmbiosProtocol[0].GetNext (
               SmbiosProtocol,
               EfiPy.byref (SmbiosHandle),
               None,
               EfiPy.byref (SmbiosRecord),
               None)
    if EfiPy.EFI_ERROR (Status):
      break

    SmbiosDumpMain (SmbiosRecord, True, True, True)