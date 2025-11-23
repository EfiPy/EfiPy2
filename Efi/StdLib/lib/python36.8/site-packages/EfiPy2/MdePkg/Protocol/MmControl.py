# MmControl.py
#
# EfiPy2.MdePkg.Protocol.MmControl
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiMmControlProtocolGuid = \
  EFI_GUID (0x843dc720, 0xab1e, 0x42cb, (0x93, 0x57, 0x8a, 0x0, 0x78, 0xf3, 0x56, 0x1b ))

class EFI_MM_CONTROL_PROTOCOL (Structure):
  pass

# typedef UINTN                            EFI_MM_PERIOD;
EFI_MM_PERIOD = UINTN

EFI_MM_ACTIVATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CONTROL_PROTOCOL), #   IN CONST    *This,
  POINTER(UINT8),                   #   IN OUT      *CommandPort       OPTIONAL,
  POINTER(UINT8),                   #   IN OUT      *DataPort          OPTIONAL,
  BOOLEAN,                          #   IN          Periodic           OPTIONAL,
  UINTN                             #   IN          ActivationInterval OPTIONAL
  )

EFI_MM_DEACTIVATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CONTROL_PROTOCOL), #   IN CONST    *This,
  BOOLEAN                           #   IN          Periodic           OPTIONAL,
  )

EFI_MM_CONTROL_PROTOCOL._fields_ = [
    ("Trigger",                 EFI_MM_ACTIVATE),
    ("Clear",                   EFI_MM_DEACTIVATE),
    ("MinimumTriggerPeriod",    EFI_MM_PERIOD)
  ]

