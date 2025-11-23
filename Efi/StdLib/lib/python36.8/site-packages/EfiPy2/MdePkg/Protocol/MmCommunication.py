# MmCommunication.py
#
# EfiPy2.MdePkg.Protocol.MmCommunication
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

class EFI_MM_COMMUNICATE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HeaderGuid",      EFI_GUID),
    ("MessageLength",   UINTN),
    ("Data",            UINT8 * 1)
  ]

gEfiMmCommunicationProtocolGuid = \
  EFI_GUID (0xc68ed8e2, 0x9dc6, 0x4cbd, ( 0x9d, 0x94, 0xdb, 0x65, 0xac, 0xc5, 0xc3, 0x32 ))

class EFI_MM_COMMUNICATION_PROTOCOL (Structure):
  pass

EFI_MM_COMMUNICATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_COMMUNICATION_PROTOCOL),   #   IN CONST  *This,
  PVOID,                                    #   IN        *CommBuffer,
  POINTER(UINTN)                            #   IN OUT    *CommSize OPTIONAL
  )

EFI_MM_COMMUNICATION_PROTOCOL._fields_ = [
    ("Communicate", EFI_MM_COMMUNICATE)
  ]

