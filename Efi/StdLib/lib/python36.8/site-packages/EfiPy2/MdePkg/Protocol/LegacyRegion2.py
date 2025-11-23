# LegacyRegion2.py
#
# EfiPy2.MdePkg.Protocol.LegacyRegion2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiLegacyRegion2ProtocolGuid = \
  EFI_GUID (0x70101eaf, 0x85, 0x440c, (0xb3, 0x56, 0x8e, 0xe3, 0x6f, 0xef, 0x24, 0xf0 ))

class EFI_LEGACY_REGION2_PROTOCOL (Structure):
  pass

EFI_LEGACY_REGION2_DECODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32),                        # OUT *Granularity,
  POINTER(BOOLEAN)                        # IN  *On
  )

EFI_LEGACY_REGION2_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32)                         # OUT *Granularity
  )

EFI_LEGACY_REGION2_BOOT_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32)                         # OUT *Granularity OPTIONAL
  )

EFI_LEGACY_REGION2_UNLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),   # IN *This
  UINT32,                                 # IN  Start,
  UINT32,                                 # IN  Length,
  POINTER(UINT32)                         # OUT *Granularity
  )

LegacyRegionDecoded         = 0
LegacyRegionNotDecoded      = 1
LegacyRegionWriteEnabled    = 2
LegacyRegionWriteDisabled   = 3
LegacyRegionBootLocked      = 4
LegacyRegionNotLocked       = 5 
EFI_LEGACY_REGION_ATTRIBUTE = ENUM

class EFI_LEGACY_REGION_DESCRIPTOR (Structure):
  _fields_ = [
    ("Start",       UINT32),
    ("Length",      UINT32),
    ("Attribute",   EFI_LEGACY_REGION_ATTRIBUTE),
    ("Granularity", UINT32)
  ]

EFI_LEGACY_REGION_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_LEGACY_REGION2_PROTOCOL),           # IN *This
  POINTER(UINT32),                                # OUT *DescriptorCount
  POINTER(POINTER(EFI_LEGACY_REGION_DESCRIPTOR))  # OUT **Descriptor
  )

EFI_LEGACY_REGION2_PROTOCOL._fields_ = [
    ("Decode",    EFI_LEGACY_REGION2_DECODE),
    ("Lock",      EFI_LEGACY_REGION2_LOCK),
    ("BootLock",  EFI_LEGACY_REGION2_BOOT_LOCK),
    ("UnLock",    EFI_LEGACY_REGION2_UNLOCK),
    ("GetInfo",   EFI_LEGACY_REGION_GET_INFO)
  ]

