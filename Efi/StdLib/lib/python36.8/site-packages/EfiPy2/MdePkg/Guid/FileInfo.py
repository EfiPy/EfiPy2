# FileInfo.py
#
# EfiPy2.MdePkg.Guid.FileInfo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiFileInfoGuid = EFI_GUID( 0x9576e92, 0x6d3f, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_FILE_INFO (Structure):
  _fields_ = [
      ("Size",              UINT64),
      ("FileSize",          UINT64),
      ("PhysicalSize",      UINT64),
      ("CreateTime",        EFI_TIME),
      ("LastAccessTime",    EFI_TIME),
      ("ModificationTime",  EFI_TIME),
      ("Attribute",         UINT64),
      ("FileName",          CHAR16 * 1)
    ]

SIZE_OF_EFI_FILE_INFO = EFI_FILE_INFO.FileName.offset

