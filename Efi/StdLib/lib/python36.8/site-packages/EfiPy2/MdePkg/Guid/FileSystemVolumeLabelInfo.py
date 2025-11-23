# FileSystemVolumeLabelInfo.py
#
# EfiPy2.MdePkg.Guid.FileSystemVolumeLabelInfo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiFileSystemVolumeLabelInfoIdGuid = \
  EFI_GUID (0xDB47D7D3, 0xFE81, 0x11d3, (0x9A, 0x35, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

class EFI_FILE_SYSTEM_VOLUME_LABEL (Structure):
  _fields_ = [
    ("VolumeLabel", CHAR16 * 1)
  ]

SIZE_OF_EFI_FILE_SYSTEM_VOLUME_LABEL = EFI_FILE_SYSTEM_VOLUME_LABEL.VolumeLabel.offset

