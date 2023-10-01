# UefiGpt.py
#
# EfiPy2.MdePkg.Uefi.UefiGpt
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

PRIMARY_PART_HEADER_LBA = 1

EFI_PTAB_HEADER_ID      = SIGNATURE_64 ('E','F','I',' ','P','A','R','T')

EFI_GPT_PART_ENTRY_MIN_SIZE  = 16384

class EFI_PARTITION_TABLE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                    EFI_TABLE_HEADER),
    ("MyLBA",                     EFI_LBA),
    ("AlternateLBA",              EFI_LBA),
    ("FirstUsableLBA",            EFI_LBA),
    ("LastUsableLBA",             EFI_LBA),
    ("DiskGUID",                  EFI_GUID),
    ("PartitionEntryLBA",         EFI_LBA),
    ("NumberOfPartitionEntries",  UINT32),
    ("SizeOfPartitionEntry",      UINT32),
    ("PartitionEntryArrayCRC32",  UINT32)
  ]

class EFI_PARTITION_ENTRY (Structure):
  _pack_   = 1
  _fields_ = [
    ("PartitionTypeGUID",   EFI_GUID),
    ("UniquePartitionGUID", EFI_GUID),
    ("StartingLBA",         EFI_LBA),
    ("EndingLBA",           EFI_LBA),
    ("Attributes",          UINT64),
    ("PartitionName",       CHAR16 * 36)
  ]

