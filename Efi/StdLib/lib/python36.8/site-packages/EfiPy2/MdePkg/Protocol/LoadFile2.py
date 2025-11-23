# LoadFile2.py
#
# EfiPy2.MdePkg.Protocol.LoadFile2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiLoadFile2ProtocolGuid = \
  EFI_GUID (0x4006c0c1, 0xfcb3, 0x403e, (0x99, 0x6d, 0x4a, 0x6c, 0x87, 0x24, 0xe0, 0x6d ))

LOAD_FILE2_PROTOCOL = gEfiLoadFile2ProtocolGuid

class EFI_LOAD_FILE2_PROTOCOL (Structure):
  pass

EFI_LOAD_FILE2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LOAD_FILE2_PROTOCOL),   # IN      *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),  # IN      *FilePath,
  BOOLEAN,                            # IN      BootPolicy,
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID                               # IN      *Buffer OPTIONAL
  )

EFI_LOAD_FILE2_PROTOCOL._fields_ = [
    ("LoadFile",    EFI_LOAD_FILE2)
  ]

