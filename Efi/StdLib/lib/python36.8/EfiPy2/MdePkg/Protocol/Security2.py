# Security2.py
#
# EfiPy2.MdePkg.Protocol.Security2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSecurity2ArchProtocolGuid = \
  EFI_GUID (0x94ab2f58, 0x1438, 0x4ef1, (0x91, 0x52, 0x18, 0x94, 0x1a, 0x3a, 0x0e, 0x68 ))

class EFI_SECURITY2_ARCH_PROTOCOL (Structure):
  pass

EFI_SECURITY2_FILE_AUTHENTICATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SECURITY2_ARCH_PROTOCOL), # IN        *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN  CONST *DevicePath,
  PVOID,                                # IN        *FileBuffer,
  UINTN,                                # IN        FileSize,
  BOOLEAN                               # IN        BootPolicy
  )

EFI_SECURITY2_ARCH_PROTOCOL._fields_ = [
    ("FileAuthentication", EFI_SECURITY2_FILE_AUTHENTICATION),
  ]

