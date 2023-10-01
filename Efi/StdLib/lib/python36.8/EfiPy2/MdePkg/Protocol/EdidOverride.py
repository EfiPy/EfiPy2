# EdidOverride.py
#
# EfiPy2.MdePkg.Protocol.EdidOverride
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiEdidOverrideProtocolGuid  = \
  EFI_GUID (0x48ecb431, 0xfb72, 0x45c0, (0xa9, 0x22, 0xf4, 0x58, 0xfe, 0x4, 0xb, 0xd5 ))

class EFI_EDID_OVERRIDE_PROTOCOL (Structure):
  pass

EFI_EDID_OVERRIDE_DONT_OVERRIDE   = 0x01
EFI_EDID_OVERRIDE_ENABLE_HOT_PLUG = 0x02

EFI_EDID_OVERRIDE_PROTOCOL_GET_EDID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EDID_OVERRIDE_PROTOCOL),  # IN     *This
  POINTER(EFI_HANDLE),                  # IN     *ChildHandle,
  POINTER(UINT32),                      # OUT    *Attributes,
  POINTER(UINTN),                       # IN OUT *EdidSize,
  POINTER(POINTER(UINT8))               # IN OUT **Edid
  )

EFI_EDID_OVERRIDE_PROTOCOL._fields_ = [
    ("GetEdid", EFI_EDID_OVERRIDE_PROTOCOL_GET_EDID)
  ]

