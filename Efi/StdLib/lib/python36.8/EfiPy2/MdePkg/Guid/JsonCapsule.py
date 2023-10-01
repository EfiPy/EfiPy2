# JsonCapsule.py
#
# EfiPy2.MdePkg.Guid.JsonCapsule
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiJsonConfigDataTableGuid  = \
  EFI_GUID(0x87367f87, 0x1119, 0x41ce, (0xaa, 0xec, 0x8b, 0xe0, 0x11, 0x1f, 0x55, 0x8a ))

gEfiJsonCapsuleDataTableGuid  = \
  EFI_GUID(0x35e7a725, 0x8dd2, 0x4cac, (0x80, 0x11, 0x33, 0xcd, 0xa8, 0x10, 0x90, 0x56 ))

gEfiJsonCapsuleResultTableGuid  = \
  EFI_GUID(0xdbc461c3, 0xb3de, 0x422a, (0xb9, 0xb4, 0x98, 0x86, 0xfd, 0x49, 0xa1, 0xe5 ))

gEfiJsonCapsuleIdGuid  = \
  EFI_GUID(0x67d6f4cd, 0xd6b8,  0x4573, (0xbf, 0x4a, 0xde, 0x5e, 0x25, 0x2d, 0x61, 0xae ))

class EFI_JSON_CAPSULE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",         UINT32),
    ("CapsuleId",       UINT32),
    ("PayloadLength",   UINT32),
    ("Payload",         UINT8 * 0)
  ]

class EFI_JSON_CONFIG_DATA_ITEM (Structure):
  _pack_   = 1
  _fields_ = [
    ("ConfigDataLength",    UINT32),
    ("ConfigData",          UINT8 * 0)
  ]

class EFI_JSON_CAPSULE_CONFIG_DATA (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",         UINT32),
    ("TotalLength",     UINT32),
    ("ConfigDataList",  EFI_JSON_CONFIG_DATA_ITEM * 0),
  ]

