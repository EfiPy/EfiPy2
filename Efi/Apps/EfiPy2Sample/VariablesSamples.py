import EfiPy2 as EfiPy
from EfiPy2.Lib.EfiPyVariables import Variables

if __name__ == '__main__':

  print ("with Variables() as Vars:")
  with Variables() as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT') as Vars:")
  with Variables('BOOT') as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C))) as Vars:")
  with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C))) as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C), CaseSensitive = True)) as Vars:")
  with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C)), CaseSensitive = True) as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C), CaseSensitive = False)) as Vars:")
  with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C)), CaseSensitive = False) as Vars:
    for n, g in Vars:
      print (n, g)
