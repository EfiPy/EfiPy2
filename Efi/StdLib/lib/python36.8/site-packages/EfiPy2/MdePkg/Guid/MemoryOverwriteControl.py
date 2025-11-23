# MemoryOverwriteControl.py
#
# EfiPy2.MdePkg.Guid.MemoryOverwriteControl
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMemoryOverwriteControlDataGuid  = \
  EFI_GUID (0xe20939be, 0x32d4, 0x41be, (0xa1, 0x50, 0x89, 0x7f, 0x85, 0xd4, 0x98, 0x29))

MEMORY_OVERWRITE_REQUEST_VARIABLE_NAME = "MemoryOverwriteRequestControl"

MOR_CLEAR_MEMORY_BIT_MASK        = 0x01

MOR_DISABLEAUTODETECT_BIT_MASK   = 0x10

MOR_CLEAR_MEMORY_BIT_OFFSET      = 0
MOR_DISABLEAUTODETECT_BIT_OFFSET = 4

def MOR_CLEAR_MEMORY_VALUE(mor):
  return (mor & MOR_CLEAR_MEMORY_BIT_MASK) >> MOR_CLEAR_MEMORY_BIT_OFFSET

def MOR_DISABLE_AUTO_DETECT_VALUE(mor):
  return (mor & MOR_DISABLEAUTODETECT_BIT_MASK) >> MOR_DISABLEAUTODETECT_BIT_OFFSET

