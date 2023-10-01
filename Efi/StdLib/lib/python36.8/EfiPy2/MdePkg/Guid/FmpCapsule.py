# FmpCapsule.py
#
# EfiPy2.MdePkg.Guid.FmpCapsule
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiFmpCapsuleGuid  = \
  EFI_GUID (0x6dcbd5ed, 0xe82d, 0x4c44, (0xbd, 0xa1, 0x71, 0x94, 0x19, 0x9a, 0xd9, 0x2a ))

class EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",             UINT32),
    ("EmbeddedDriverCount", UINT16),
    ("PayloadItemCount",    UINT16),
    # ("ItemOffsetList",      UINT64 * N)
  ]

class EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",                 UINT32),
    ("UpdateImageTypeId",       EFI_GUID),
    ("UpdateImageIndex",        UINT8),
    ("reserved_bytes",          UINT8 * 3),
    ("UpdateImageSize",         UINT32),
    ("UpdateVendorCodeSize",    UINT32),
    ("UpdateHardwareInstance",  UINT64),
    ("ImageCapsuleSupport",     UINT64)
  ]

EFI_FIRMWARE_MANAGEMENT_CAPSULE_HEADER_INIT_VERSION        = 0x00000001
EFI_FIRMWARE_MANAGEMENT_CAPSULE_IMAGE_HEADER_INIT_VERSION  = 0x00000003
CAPSULE_SUPPORT_AUTHENTICATION                             = 0x0000000000000001
CAPSULE_SUPPORT_DEPENDENCY                                 = 0x0000000000000002

