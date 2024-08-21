from EfiPy2.Lib.HexDump import HexDump

def HexDumpDemo ():

  InputData = b'\x01\x02ab'
  print (f'Try to dump binary data via HexDump {InputData}\n')
  HexDump (InputData)
  print()
  InputData = b'\x01\x02abcded\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x00\x0D\x0E\x0F\x10\x11\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04abcded\xaa'
  print (f'Try to dump binary data via HexDump {InputData}\n')
  HexDump (InputData, HexOffset = 0x1000, DumpLead = 4)
  print ()
  HexDump (InputData, HexOffset = 0x1002, DumpLead = 4)
  print ()
  HexDump (InputData, HexOffset = 0x100A, DumpLead = 4)
  print ()

if __name__ == '__main__':

  import sys
  if len (sys.argv) == 1:
    HexDumpDemo ()
    sys.exit(0)

  with open (sys.argv[1], 'br') as f:
    b = f.read()
    HexDump (b)
