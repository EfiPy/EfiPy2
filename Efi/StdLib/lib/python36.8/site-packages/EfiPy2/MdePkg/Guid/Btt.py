# Btt.py
#
# EfiPy2.MdePkg.Guid.Btt
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiBttAbstractionGuid = \
  EFI_GUID (0x18633bfc, 0x1735, 0x4217, ( 0x8a, 0xc9, 0x17, 0x23, 0x92, 0x82, 0xd3, 0xf8 ))

EFI_BTT_ALIGNMENT  = 4096

EFI_BTT_INFO_UNUSED_LEN  = 3968

EFI_BTT_INFO_BLOCK_SIG_LEN  = 16

EFI_BTT_INFO_BLOCK_FLAGS_ERROR  = 0x00000001

EFI_BTT_INFO_BLOCK_MAJOR_VERSION  = 2
EFI_BTT_INFO_BLOCK_MINOR_VERSION  = 0

class EFI_BTT_INFO_BLOCK (Structure):
  _fields_ = [
    ("Sig",             CHAR8 * EFI_BTT_INFO_BLOCK_SIG_LEN),
    ("Uuid",            GUID),
    ("ParentUuid",      GUID),
    ("Flags",           UINT32),
    ("Major",           UINT16),
    ("Minor",           UINT16),
    ("ExternalLbaSize", UINT32),
    ("ExternalNLba",    UINT32),
    ("InternalLbaSize", UINT32),
    ("InternalNLba",    UINT32),
    ("NFree",           UINT32),
    ("InfoSize",        UINT32),
    ("NextOff",         UINT64),
    ("DataOff",         UINT64),
    ("MapOff",          UINT64),
    ("FlogOff",         UINT64),
    ("InfoOff",         UINT64),
    ("Unused",          CHAR8 * EFI_BTT_INFO_UNUSED_LEN),
    ("Checksum",        UINT64)
  ]

class EFI_BTT_MAP_ENTRY (Structure):
  _fields_ = [
    ("PostMapLba",  UINT32, 30),
    ("Error",       UINT32, 1),
    ("Zero",        UINT32, 1)
  ]

EFI_BTT_FLOG_ENTRY_ALIGNMENT  = 64

class EFI_BTT_FLOG (Structure):
  _fields_ = [
    ("Lba0",    UINT32),
    ("OldMap0", UINT32),
    ("NewMap0", UINT32),
    ("Seq0",    UINT32),
    ("Lba1",    UINT32),
    ("OldMap1", UINT32),
    ("NewMap1", UINT32),
    ("Seq1",    UINT32)
  ]

