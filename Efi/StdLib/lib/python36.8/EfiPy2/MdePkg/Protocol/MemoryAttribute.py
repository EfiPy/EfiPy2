# MemoryAttribute.py
#
# EfiPy2.MdePkg.Protocol.MemoryAttribute
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMemoryAttributeProtocolGuid  = \
  EFI_GUID (0xf4560cf6, 0x40ec, 0x4b4a, ( 0xa1, 0x92, 0xbf, 0x1d, 0x57, 0xd0, 0xb1, 0x89 ))

class EFI_MEMORY_ATTRIBUTE_PROTOCOL (Structure):
  pass

EFI_SET_MEMORY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MEMORY_ATTRIBUTE_PROTOCOL),   #   IN  *This
  EFI_PHYSICAL_ADDRESS,                     #   IN  BaseAddress,
  UINT64,                                   #   IN  Length
  UINT64                                    #   IN  Attributes
  )

EFI_CLEAR_MEMORY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MEMORY_ATTRIBUTE_PROTOCOL),   #   IN  *This
  EFI_PHYSICAL_ADDRESS,                     #   IN  BaseAddress,
  UINT64,                                   #   IN  Length
  UINT64                                    #   IN  Attributes
  )

EFI_GET_MEMORY_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MEMORY_ATTRIBUTE_PROTOCOL),   #   IN  *This
  EFI_PHYSICAL_ADDRESS,                     #   IN  BaseAddress,
  UINT64,                                   #   IN  Length
  POINTER(UINT64)                           #   OUT *Attributes
  )

EFI_MEMORY_ATTRIBUTE_PROTOCOL._fields_ = [
    ("GetMemoryAttributes",     EFI_GET_MEMORY_ATTRIBUTES),
    ("SetMemoryAttributes",     EFI_SET_MEMORY_ATTRIBUTES),
    ("ClearMemoryAttributes",   EFI_CLEAR_MEMORY_ATTRIBUTES)
  ]

