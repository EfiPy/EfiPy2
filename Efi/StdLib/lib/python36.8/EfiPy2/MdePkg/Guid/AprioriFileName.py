# AprioriFileName.py
#
# EfiPy2.MdePkg.Guid.AprioriFileName
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gPeiAprioriFileNameGuid = \
  EFI_GUID (0x1b45cc0a, 0x156a, 0x428a, ( 0x62, 0XAF, 0x49, 0x86, 0x4d, 0xa0, 0xe6, 0xe6 ))

class PEI_APRIORI_FILE_CONTENTS (Structure):
  _fields_ = [
    ("FileNamesWithinVolume",  EFI_GUID * 1)
  ]

