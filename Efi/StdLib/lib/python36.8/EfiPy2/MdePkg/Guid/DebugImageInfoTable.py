# DebugImageInfoTable.py
#
# EfiPy2.MdePkg.Guid.DebugImageInfoTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol  import LoadedImage

gEfiDebugImageInfoTableGuid = \
  EFI_GUID (0x49152e77, 0x1ada, 0x4764, (0xb7, 0xa2, 0x7a, 0xfe, 0xfe, 0xd9, 0x5e, 0x8b ))

EFI_DEBUG_IMAGE_INFO_UPDATE_IN_PROGRESS = 0x01
EFI_DEBUG_IMAGE_INFO_TABLE_MODIFIED     = 0x02

EFI_DEBUG_IMAGE_INFO_TYPE_NORMAL        = 0x01

class EFI_SYSTEM_TABLE_POINTER (Structure):
  _fields_ = [
    ("Signature",           UINT64),
    ("EfiSystemTableBase",  EFI_PHYSICAL_ADDRESS),
    ("Crc32",               UINT32)
  ]

class EFI_DEBUG_IMAGE_INFO_NORMAL (Structure):
  _fields_ = [
    ("ImageInfoType",               UINT32),
    ("LoadedImageProtocolInstance", POINTER(LoadedImage.EFI_LOADED_IMAGE_PROTOCOL)),
    ("ImageHandle",                 EFI_HANDLE)
  ]

class EFI_DEBUG_IMAGE_INFO (Union):
  _fields_ = [
    ("ImageInfoType", POINTER(UINT32)),
    ("NormalImage",   POINTER(EFI_DEBUG_IMAGE_INFO_NORMAL))
  ]

class EFI_DEBUG_IMAGE_INFO_TABLE_HEADER (Structure):
  _fields_ = [
    ("UpdateStatus",            UINT32),
    ("TableSize",               UINT32),
    ("EfiDebugImageInfoTable",  POINTER(EFI_DEBUG_IMAGE_INFO))
  ]

