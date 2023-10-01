# PartitionInfo.py
#
# EfiPy2.MdePkg.Protocol.PartitionInfo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard.Mbr import MBR_PARTITION_RECORD

from EfiPy2.MdePkg.Uefi.UefiGpt         import EFI_PARTITION_ENTRY

gEfiPartitionInfoProtocolGuid           = \
  EFI_GUID (0x8cf2f62c, 0xbc9b, 0x4821, ( 0x80, 0x8d, 0xec, 0x9e, 0xc4, 0x21, 0xa1, 0xa0 ))

EFI_PARTITION_INFO_PROTOCOL_REVISION  = 0x0001000
PARTITION_TYPE_OTHER                  = 0x00
PARTITION_TYPE_MBR                    = 0x01
PARTITION_TYPE_GPT                    = 0x02

class EFI_PARTITION_INFO_PROTOCOL_Info (Union):
  _pack_   = 1
  _fields_  = [
    ("Mbr", MBR_PARTITION_RECORD),
    ("Gpt", EFI_PARTITION_ENTRY),
  ]

class EFI_PARTITION_INFO_PROTOCOL (Structure):
  _pack_   = 1
  _fields_  = [
    ("Revision",    UINT32),
    ("Type",        UINT32),
    ("System",      UINT8),
    ("Reserved",    UINT8 * 7),
    ("Info",        EFI_PARTITION_INFO_PROTOCOL_Info)
  ]

