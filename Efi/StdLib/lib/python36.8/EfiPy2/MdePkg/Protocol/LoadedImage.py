# LoadedImage.py
#
# EfiPy2.MdePkg.Protocol.LoadedImage
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiLoadedImageProtocolGuid           = \
  EFI_GUID (0x5B1B31A1, 0x9562, 0x11d2, (0x8E, 0x3F, 0x00, 0xA0, 0xC9, 0x69, 0x72, 0x3B ))

gEfiLoadedImageDevicePathProtocolGuid = \
  EFI_GUID (0xbc62157e, 0x3e33, 0x4fec, (0x99, 0x20, 0x2d, 0x3b, 0x36, 0xd7, 0x50, 0xdf ))

EFI_LOADED_IMAGE_PROTOCOL_REVISION  = 0x1000

EFI_LOADED_IMAGE_INFORMATION_REVISION  = EFI_LOADED_IMAGE_PROTOCOL_REVISION

class EFI_LOADED_IMAGE_PROTOCOL (Structure):
  _fields_ = [
    ("Revision",        UINT32),
    ("ParentHandle",    EFI_HANDLE),
    ("SystemTable",     POINTER (EFI_SYSTEM_TABLE)),
    ("DeviceHandle",    EFI_HANDLE),
    ("FilePath",        POINTER (EFI_DEVICE_PATH_PROTOCOL)),
    ("Reserved",        PVOID),
    ("LoadOptionsSize", UINT32),
    ("LoadOptions",     PVOID),
    ("ImageBase",       PVOID),
    ("ImageSize",       UINT64),
    ("ImageCodeType",   EFI_MEMORY_TYPE),
    ("ImageDataType",   EFI_MEMORY_TYPE),
    ("Unload",          EFI_IMAGE_UNLOAD)
  ]

