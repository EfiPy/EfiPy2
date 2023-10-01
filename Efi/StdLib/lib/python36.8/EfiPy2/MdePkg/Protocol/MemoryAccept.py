# MemoryAccept.py
#
# EfiPy2.MdePkg.Protocol.MemoryAccept
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEdkiiMemoryAcceptProtocolGuid  = \
  EFI_GUID (0x38c74800, 0x5590, 0x4db4, ( 0xa0, 0xf3, 0x67, 0x5d, 0x9b, 0x8e, 0x80, 0x26 ))

class EDKII_MEMORY_ACCEPT_PROTOCOL (Structure):
  pass

EDKII_ACCEPT_MEMORY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_MEMORY_ACCEPT_PROTOCOL),    #   IN  *This
  EFI_PHYSICAL_ADDRESS,                     #   IN  StartAddress,
  UINTN                                     #   IN  Size
  )

EDKII_MEMORY_ACCEPT_PROTOCOL._fields_ = [
    ("AcceptMemory",  EDKII_ACCEPT_MEMORY)
  ]

