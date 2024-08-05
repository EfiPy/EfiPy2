import sys

def HexDump (InputData, DumpHead = 0, OutFile = sys.stdout):

  InputArray = [InputData[i: i + 16] for i in range(0, len(InputData), 16)]

  print (f'            0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F  01234567 89ABCDEF', file = OutFile)
  print (f'------------------------------------------------------------------------------', file = OutFile)
  
  for BinaryData in InputArray:

    b = ''.join(f'{b:02X} ' for b in BinaryData)
    b = b + '   ' * (16 - len(BinaryData))
    b = b[:24] + ' ' + b[24:]

    s = ''.join(f'{b:c}' if b >= 0x20 and b <= 0x7E else '.' for b in BinaryData)
    s = s + ' ' * (16 - len(BinaryData))
    s = s[:8] + ' ' + s[8:]

    print(f'{DumpHead:08X}   {b} {s}', file = OutFile)
    DumpHead += 16

def HexDumpDemo ():

  InputData = b'\x01\x02ab'
  print (f'Try to dump binary data via HexDump {InputData}\n')
  HexDump (InputData)
  print()
  InputData = b'\x01\x02abcded\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x00\x0D\x0E\x0F\x10\x11\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04abcded\xaa'
  print (f'Try to dump binary data via HexDump {InputData}\n')
  HexDump (InputData)

if __name__ == '__main__':

  if len (sys.argv) == 1:
    HexDumpDemo ()
    sys.exit(0)

  with open (sys.argv[1], 'br') as f:
    b = f.read()
    HexDump (b)
