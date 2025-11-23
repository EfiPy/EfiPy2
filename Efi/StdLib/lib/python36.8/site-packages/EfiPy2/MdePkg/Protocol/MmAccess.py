# MmAccess.py
#
# EfiPy2.MdePkg.Protocol.MmAccess
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Pi.PiMultiPhase import EFI_MMRAM_DESCRIPTOR

gEfiMmAccessProtocolGuid = \
  EFI_GUID (0xc2702b74, 0x800c, 0x4131, (0x87, 0x46, 0x8f, 0xb5, 0xb8, 0x9c, 0xe4, 0xac ))

class EFI_MM_ACCESS_PROTOCOL (Structure):
  pass

EFI_MM_OPEN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_ACCESS_PROTOCOL)   # IN *This
  )

EFI_MM_CLOSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_ACCESS_PROTOCOL)   # IN *This
  )

EFI_MM_LOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_ACCESS_PROTOCOL)   # IN *This
  )

EFI_MM_CAPABILITIES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_ACCESS_PROTOCOL),  # IN        *This,
  POINTER(UINTN),                   # IN OUT    *MmramMapSize,
  POINTER(EFI_MMRAM_DESCRIPTOR),    # IN OUT    *MmramMap
  )

EFI_MM_ACCESS_PROTOCOL._fields_ = [
    ("Open",            EFI_MM_OPEN),
    ("Close",           EFI_MM_CLOSE),
    ("Lock",            EFI_MM_LOCK),
    ("GetCapabilities", EFI_MM_CAPABILITIES),
    ("LockState",       BOOLEAN),
    ("OpenState",       BOOLEAN)
  ]

