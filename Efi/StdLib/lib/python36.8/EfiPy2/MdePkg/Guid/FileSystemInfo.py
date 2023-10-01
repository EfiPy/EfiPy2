# FileSystemInfo.py
#
# EfiPy2.MdePkg.Guid.FileSystemInfo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiFileSystemInfoGuid = EFI_GUID( 0x9576e93, 0x6d3f, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_FILE_SYSTEM_INFO (Structure):
  _fields_ = [
    ("Size",        UINT64),
    ("ReadOnly",    BOOLEAN),
    ("VolumeSize",  UINT64),
    ("FreeSpace",   UINT64),
    ("BlockSize",   UINT32),
    ("VolumeLabel", CHAR16 * 1)
    ]

SIZE_OF_EFI_FILE_SYSTEM_INFO = EFI_FILE_SYSTEM_INFO.VolumeLabel.offset

