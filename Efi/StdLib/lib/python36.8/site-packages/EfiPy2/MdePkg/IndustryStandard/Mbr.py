# Mbr.py
#
# EfiPy2.MdePkg.IndustryStandard.Mbr
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

MBR_SIGNATURE               = 0xaa55

EXTENDED_DOS_PARTITION      = 0x05
EXTENDED_WINDOWS_PARTITION  = 0x0F

MAX_MBR_PARTITIONS          = 4

PMBR_GPT_PARTITION          = 0xEE
EFI_PARTITION               = 0xEF

MBR_SIZE                    = 512

class MBR_PARTITION_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BootIndicator", UINT8),
    ("StartHead",     UINT8),
    ("StartSector",   UINT8),
    ("StartTrack",    UINT8),
    ("OSIndicator",   UINT8),
    ("EndHead",       UINT8),
    ("EndSector",     UINT8),
    ("EndTrack",      UINT8),
    ("StartingLBA",   UINT8 * 4),
    ("SizeInLBA",     UINT8 * 4)
  ]

class MASTER_BOOT_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BootStrapCode",       UINT8 * 440),
    ("UniqueMbrSignature",  UINT8 * 4),
    ("Unknown",             UINT8 * 2),
    ("Partition",           MBR_PARTITION_RECORD * MAX_MBR_PARTITIONS),
    ("Signature",           UINT16)
  ]
