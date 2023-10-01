# RtPropertiesTable.py
#
# EfiPy2.MdePkg.Guid.RtPropertiesTable
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiRtPropertiesTableGuid  = \
  EFI_GUID (0xeb66918a, 0x7eef, 0x402a, (0x84, 0x2e, 0x93, 0x1d, 0x21, 0xc3, 0x8a, 0xe9))

class EFI_RT_PROPERTIES_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",                     UINT16),
    ("Length",                      UINT16),
    ("RuntimeServicesSupported",    UINT32)
  ]

EFI_RT_PROPERTIES_TABLE_VERSION  = 0x1

EFI_RT_SUPPORTED_GET_TIME                       = 0x0001
EFI_RT_SUPPORTED_SET_TIME                       = 0x0002
EFI_RT_SUPPORTED_GET_WAKEUP_TIME                = 0x0004
EFI_RT_SUPPORTED_SET_WAKEUP_TIME                = 0x0008
EFI_RT_SUPPORTED_GET_VARIABLE                   = 0x0010
EFI_RT_SUPPORTED_GET_NEXT_VARIABLE_NAME         = 0x0020
EFI_RT_SUPPORTED_SET_VARIABLE                   = 0x0040
EFI_RT_SUPPORTED_SET_VIRTUAL_ADDRESS_MAP        = 0x0080
EFI_RT_SUPPORTED_CONVERT_POINTER                = 0x0100
EFI_RT_SUPPORTED_GET_NEXT_HIGH_MONOTONIC_COUNT  = 0x0200
EFI_RT_SUPPORTED_RESET_SYSTEM                   = 0x0400
EFI_RT_SUPPORTED_UPDATE_CAPSULE                 = 0x0800
EFI_RT_SUPPORTED_QUERY_CAPSULE_CAPABILITIES     = 0x1000
EFI_RT_SUPPORTED_QUERY_VARIABLE_INFO            = 0x2000

