# DevicePathFromText.py
#
# EfiPy2.MdePkg.Protocol.DevicePathFromText
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDevicePathFromTextProtocolGuid      = \
  EFI_GUID (0x5c99a21, 0xc70f, 0x4ad2, (0x8a, 0x5f, 0x35, 0xdf, 0x33, 0x43, 0xf5, 0x1e  ))

EFI_DEVICE_PATH_FROM_TEXT_NODE = CFUNCTYPE (
  POINTER (EFI_DEVICE_PATH_PROTOCOL),
  PCHAR16                             # IN *TextDeviceNode
  )

EFI_DEVICE_PATH_FROM_TEXT_PATH = CFUNCTYPE (
  POINTER (EFI_DEVICE_PATH_PROTOCOL),
  PCHAR16                             # IN *TextDeviceNode
  )

class EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL (Structure):
  _fields_ = [
    ("ConvertTextToDeviceNode",  EFI_DEVICE_PATH_FROM_TEXT_NODE),
    ("ConvertTextToDevicePath",  EFI_DEVICE_PATH_FROM_TEXT_PATH)
  ]

