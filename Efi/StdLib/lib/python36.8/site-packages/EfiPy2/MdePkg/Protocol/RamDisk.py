# RamDisk.py
#
# EfiPy2.MdePkg.Protocol.RamDisk
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.DevicePath import EFI_DEVICE_PATH, EFI_DEVICE_PATH_PROTOCOL

gEfiRamDiskProtocolGuid     = \
  EFI_GUID (0xab38a0df, 0x6873, 0x44a9, ( 0x87, 0xe6, 0xd4, 0xeb, 0x56, 0x14, 0x84, 0x49 ))

class EFI_RAM_DISK_PROTOCOL (Structure):
  pass

EFI_RAM_DISK_REGISTER_RAMDISK = CFUNCTYPE (
  EFI_STATUS,
  UINT64,                                       #   IN  RamDiskBase,
  UINT64,                                       #   IN  RamDiskSize,
  POINTER(EFI_GUID),                            #   IN  *RamDiskType,
  POINTER(EFI_DEVICE_PATH),                     #   IN  *ParentDevicePath     OPTIONAL,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))    #   OUT **DevicePath
  )

EFI_RAM_DISK_UNREGISTER_RAMDISK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     #   OUT *DevicePath
  )

EFI_RAM_DISK_PROTOCOL._fields_ = [
    ("Register",    EFI_RAM_DISK_REGISTER_RAMDISK),
    ("Unregister",  EFI_RAM_DISK_UNREGISTER_RAMDISK)
  ]

