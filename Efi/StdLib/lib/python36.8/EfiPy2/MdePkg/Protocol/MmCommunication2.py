# MmCommunication2.py
#
# EfiPy2.MdePkg.Protocol.MmCommunication2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmCommunication

gEfiMmCommunication2ProtocolGuid = \
  EFI_GUID (0x378daedc, 0xf06b, 0x4446, ( 0x83, 0x14, 0x40, 0xab, 0x93, 0x3c, 0x87, 0xa3 ))

class EFI_MM_COMMUNICATION2_PROTOCOL (Structure):
  pass

EFI_MM_COMMUNICATE2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_COMMUNICATION2_PROTOCOL),  #   IN CONST  *This,
  PVOID,                                    #   IN OUT    *CommBufferPhysical,
  PVOID,                                    #   IN OUT    *CommBufferVirtual,
  POINTER(UINTN),                           #   IN OUT    *CommSize OPTIONAL
  )

EFI_MM_COMMUNICATION2_PROTOCOL._fields_ = [
    ("Communicate", EFI_MM_COMMUNICATE2)
  ]

