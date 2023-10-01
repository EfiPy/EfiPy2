# WindowsUxCapsule.py
#
# EfiPy2.MdePkg.IndustryStandard.WindowsUxCapsule
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard  import *
from EfiPy2.MdePkg.Uefi.UefiSpec     import EFI_CAPSULE_HEADER

class DISPLAY_DISPLAY_PAYLOAD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",   UINT8),
    ("Checksum",  UINT8),
    ("ImageType", UINT8),
    ("Reserved",  UINT8),
    ("Mode",      UINT32),
    ("OffsetX",   UINT32),
    ("OffsetY",   UINT32)
    # ("Image",     UINT8 * N)
  ]

class EFI_DISPLAY_CAPSULE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CapsuleHeader", EFI_CAPSULE_HEADER),
    ("ImagePayload",  DISPLAY_DISPLAY_PAYLOAD)
  ]

gWindowsUxCapsuleGuid = EFI_GUID (0x3b8c8162, 0x188c, 0x46a4, ( 0xae, 0xc9, 0xbe, 0x43, 0xf1, 0xd6, 0x56, 0x97))
