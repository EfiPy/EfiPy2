# VariablesSamples.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.Lib.EfiPyVariables import Variables
from EfiPy2.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid

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
  print ("with Variables('BOOT', gEfiGlobalVariableGuid) as Vars:")
  with Variables('BOOT', gEfiGlobalVariableGuid) as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', gEfiGlobalVariableGuid, CaseSensitive = True)) as Vars:")
  with Variables('BOOT', gEfiGlobalVariableGuid, CaseSensitive = True) as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', gEfiGlobalVariableGuid, CaseSensitive = False)) as Vars:")
  with Variables('BOOT', gEfiGlobalVariableGuid, CaseSensitive = False) as Vars:
    for n, g in Vars:
      print (n, g)
