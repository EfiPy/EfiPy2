# HexDumpSample.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.Lib.HexDump import HexDump

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

  import sys
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
