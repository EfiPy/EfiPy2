# MemoryAttributesTable.py
#
# EfiPy2.MdePkg.Guid.MemoryAttributesTable
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiMemoryAttributesTableGuid  = \
  EFI_GUID(0xdcfa911d, 0x26eb, 0x469f, (0xa2, 0x20, 0x38, 0xb7, 0xdc, 0x46, 0x12, 0x20 ))

class EFI_JSON_CAPSULE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",         UINT32),
    ("NumberOfEntries", UINT32),
    ("DescriptorSize",  UINT32),
    ("Flags",           UINT32)
    # ("Entry",           EFI_MEMORY_DESCRIPTOR)
  ]

EFI_MEMORY_ATTRIBUTES_TABLE_VERSION  = 0x00000002

