# UfsDeviceConfig.py
#
# EfiPy2.MdePkg.Protocol.UfsDeviceConfig
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiUfsDeviceConfigProtocolGuid  = \
  EFI_GUID (0xb81bfab0, 0xeb3, 0x4cf9, ( 0x84, 0x65, 0x7f, 0xa9, 0x86, 0x36, 0x16, 0x64 ))

class EFI_UFS_DEVICE_CONFIG_PROTOCOL (Structure):
  pass

EFI_UFS_DEVICE_CONFIG_RW_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UFS_DEVICE_CONFIG_PROTOCOL),  #   IN     *This,
  BOOLEAN,                                  #   IN     Read,
  UINT8,                                    #   IN     DescId,
  UINT8,                                    #   IN     Index,
  UINT8,                                    #   IN     Selector,
  POINTER(UINT8),                           #   IN OUT *Descriptor,
  POINTER(UINT32)                           #   IN OUT *DescSize
  )

EFI_UFS_DEVICE_CONFIG_RW_FLAG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UFS_DEVICE_CONFIG_PROTOCOL),  #   IN     *This,
  BOOLEAN,                                  #   IN     Read,
  UINT8,                                    #   IN     FlagId,
  POINTER(UINT8),                           #   IN OUT *Flag
  )

EFI_UFS_DEVICE_CONFIG_RW_ATTRIBUTE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UFS_DEVICE_CONFIG_PROTOCOL),  #   IN     *This,
  BOOLEAN,                                  #   IN     Read,
  UINT8,                                    #   IN     AttrId,
  UINT8,                                    #   IN     Index,
  UINT8,                                    #   IN     Selector,
  POINTER(UINT8),                           #   IN OUT *Attribute,
  POINTER(UINT32),                          #   IN OUT *AttrSize
  )

EFI_UFS_DEVICE_CONFIG_PROTOCOL._fields_ = [
    ("RwUfsDescriptor", EFI_UFS_DEVICE_CONFIG_RW_DESCRIPTOR),
    ("RwUfsFlag",       EFI_UFS_DEVICE_CONFIG_RW_FLAG),
    ("RwUfsAttribute",  EFI_UFS_DEVICE_CONFIG_RW_ATTRIBUTE)
  ]

