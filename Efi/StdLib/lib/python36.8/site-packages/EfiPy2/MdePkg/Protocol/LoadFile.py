# LoadFile.py
#
# EfiPy2.MdePkg.Protocol.LoadFile
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiLoadFileProtocolGuid  = \
  EFI_GUID (0x56EC3091, 0x954C, 0x11d2, (0x8E, 0x3F, 0x00, 0xA0, 0xC9, 0x69, 0x72, 0x3B ))

LOAD_FILE_PROTOCOL = gEfiLoadFileProtocolGuid

class EFI_LOAD_FILE_PROTOCOL (Structure):
  pass

EFI_LOAD_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LOAD_FILE_PROTOCOL),    # IN      *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),  # IN      *FilePath,
  BOOLEAN,                            # IN      BootPolicy,
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID                               # IN      *Buffer OPTIONAL
  )

EFI_LOAD_FILE_PROTOCOL._fields_ = [
    ("LoadFile",    EFI_LOAD_FILE)
  ]

