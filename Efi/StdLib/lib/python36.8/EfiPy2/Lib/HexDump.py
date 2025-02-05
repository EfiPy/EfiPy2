# HexDump.py
#
# EfiPy2.Lib.HexDump
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
import sys

def HexDump (InputData, HexOffset = 0, DumpLead = 0, OutFile = sys.stdout):

  DumpEmpty  = HexOffset % 0x10
  DumpData   = b' ' * DumpEmpty + InputData
  DumpOffset = (HexOffset // 0x10) * 0x10
  InputArray = [DumpData[i: i + 16] for i in range(0, len(DumpData), 16)]

  print (' ' * DumpLead + f'            0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F  01234567 89ABCDEF', file = OutFile)
  print (' ' * DumpLead + f'------------------------------------------------------------------------------', file = OutFile)
  
  for BinaryData in InputArray:

    b = ''.join(f'{b:02X} ' for b in BinaryData)
    b = b + '   ' * (16 - len(BinaryData))
    b = b[:24] + ' ' + b[24:]
    if DumpEmpty != 0:
      e = '   ' * DumpEmpty
      e += ' ' if DumpEmpty > 8 else ''
      b = e + b[len(e):]
    DumpEmpty = 0
    s = ''.join(f'{b:c}' if b >= 0x20 and b <= 0x7E else '.' for b in BinaryData)
    s = s + ' ' * (16 - len(BinaryData))
    s = s[:8] + ' ' + s[8:]

    print(' ' * DumpLead + f'{DumpOffset:08X}   {b} {s}', file = OutFile)
    DumpOffset += 16

def HexDumpDemo ():

  print("\n1. =============================================================================")
  InputData = b'\x01\x02ab'
  print (f'Try to dump binary data via HexDump {InputData}\n')
  HexDump (InputData, DumpLead = 1)

  print("\n2. =============================================================================")
  InputData = b'\x01\x02abcded\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x00\x0D\x0E\x0F\x10\x11\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04abcded\xaa'
  print (f'Try to dump binary data via HexDump {InputData}\n')
  HexDump (InputData, HexOffset = 0x1000, DumpLead = 1)

  print ("\n3. ============================================================================")
  HexDump (InputData, HexOffset = 0x1002, DumpLead = 1)

  print ("\n4. ============================================================================")
  HexDump (InputData, HexOffset = 0x100A, DumpLead = 1)

if __name__ == '__main__':

  if len (sys.argv) == 1:
    HexDumpDemo ()
    sys.exit(0)

  try:
    with open (sys.argv[1], 'br') as f:
      b = f.read()
      HexDump (b)
  except FileNotFoundError as e:
    print (e)
    print ("Turn to internal default demo program...")
    HexDumpDemo ()
