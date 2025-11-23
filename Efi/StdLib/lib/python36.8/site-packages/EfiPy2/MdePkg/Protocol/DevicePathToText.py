# DevicePathToText.py
#
# EfiPy2.MdePkg.Protocol.DevicePathToText
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiDevicePathToTextProtocolGuid        = \
  EFI_GUID (0x8b843e20, 0x8132, 0x4852, (0x90, 0xcc, 0x55, 0x1a, 0x4e, 0x4a, 0x7f, 0x1c ))

EFI_DEVICE_PATH_TO_TEXT_NODE = CFUNCTYPE (
  PCHAR16,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *DeviceNode
  BOOLEAN,                              # IN DisplayOnly,
  BOOLEAN                               # IN AllowShortcuts
  )

EFI_DEVICE_PATH_TO_TEXT_PATH = CFUNCTYPE (
  PCHAR16,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    # IN *DeviceNode
  BOOLEAN,                              # IN DisplayOnly,
  BOOLEAN                               # IN AllowShortcuts
  )

class EFI_DEVICE_PATH_TO_TEXT_PROTOCOL (Structure):
  _fields_ = [
    ("ConvertDeviceNodeToText",  EFI_DEVICE_PATH_TO_TEXT_NODE),
    ("ConvertDevicePathToText",  EFI_DEVICE_PATH_TO_TEXT_PATH)
  ]

