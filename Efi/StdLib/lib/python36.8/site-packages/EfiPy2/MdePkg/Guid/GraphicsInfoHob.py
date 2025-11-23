# GraphicsInfoHob.py
#
# EfiPy2.MdePkg.Guid.GraphicsInfoHob
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol  import GraphicsOutput

gEfiGraphicsInfoHobGuid = \
  EFI_GUID (0x39f62cce, 0x6825, 0x4669, ( 0xbb, 0x56, 0x54, 0x1a, 0xba, 0x75, 0x3a, 0x07 ))

gEfiGraphicsDeviceInfoHobGuid = \
  EFI_GUID (0xe5cb2ac9, 0xd35d, 0x4430, ( 0x93, 0x6e, 0x1d, 0xe3, 0x32, 0x47, 0x8d, 0xe7 ))

class EFI_PEI_GRAPHICS_INFO_HOB (Structure):
  _fields_ = [
    ("FrameBufferBase", EFI_PHYSICAL_ADDRESS),
    ("FrameBufferSize", UINT32),
    ("GraphicsMode",    GraphicsOutput.EFI_GRAPHICS_OUTPUT_MODE_INFORMATION)
  ]

class EFI_PEI_GRAPHICS_DEVICE_INFO_HOB (Structure):
  _fields_ = [
    ("VendorId",            UINT16),
    ("DeviceId",            UINT16),
    ("SubsystemVendorId",   UINT16),
    ("SubsystemId",         UINT16),
    ("RevisionId",          UINT8),
    ("BarIndex",            UINT8)
  ]

