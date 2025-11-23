# EraseBlock.py
#
# EfiPy2.MdePkg.Protocol.EraseBlock
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiEraseBlockProtocolGuid  = \
  EFI_GUID (0x95a9a93e, 0xa86e, 0x4926, ( 0xaa, 0xef, 0x99, 0x18, 0xe7, 0x72, 0xd9, 0x87 ))

class EFI_ERASE_BLOCK_PROTOCOL (Structure):
  pass

EFI_ERASE_BLOCK_PROTOCOL_REVISION  = ((2<<16) | (60))

class EFI_ERASE_BLOCK_TOKEN (Structure):
  _fields_ = [
    ("Event",               EFI_EVENT),
    ("TransactionStatus",   EFI_STATUS)
  ]

EFI_BLOCK_ERASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ERASE_BLOCK_PROTOCOL),    # IN     *This
  UINT32,                               # IN     MediaId,
  EFI_LBA,                              # IN     LBA,
  POINTER(EFI_ERASE_BLOCK_TOKEN),       # IN OUT *Token,
  UINTN                                 # IN     Size
  )

EFI_ERASE_BLOCK_PROTOCOL._fields_ = [
    ("Revision",                UINT64),
    ("EraseLengthGranularity",  UINT32)
  ]

