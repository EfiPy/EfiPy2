# DeferredImageLoad.py
#
# EfiPy2.MdePkg.Protocol.DeferredImageLoad
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDeferredImageLoadProtocolGuid   = \
  EFI_GUID (0x15853d7c, 0x3ddf, 0x43e0, ( 0xa1, 0xcb, 0xeb, 0xf8, 0x5b, 0x8f, 0x87, 0x2c ))

class EFI_DEFERRED_IMAGE_LOAD_PROTOCOL (Structure):
  pass

EFI_DEFERRED_IMAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEFERRED_IMAGE_LOAD_PROTOCOL),    # IN      *This
  UINTN,                                        # IN      ImageIndex
  POINTER (POINTER (EFI_DEVICE_PATH_PROTOCOL)), #    OUT  **ImageDevicePath,
  POINTER(PVOID),                               #    OUT  **Image,
  POINTER(UINTN),                               #    OUT  *ImageSize
  POINTER(BOOLEAN)                              #    OUT  *BootOption
  )

EFI_DEFERRED_IMAGE_LOAD_PROTOCOL._fields_ = [
    ("GetImageInfo",  EFI_DEFERRED_IMAGE_INFO)
  ]

