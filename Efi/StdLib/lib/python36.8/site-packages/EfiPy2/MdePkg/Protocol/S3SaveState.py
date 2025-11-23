# S3SaveState.py
#
# EfiPy2.MdePkg.Protocol.S3SaveState
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiS3SaveStateProtocolGuid   = \
  EFI_GUID (0xe857caf6, 0xc046, 0x45dc, ( 0xbe, 0x3f, 0xee, 0x7, 0x65, 0xfb, 0xa8, 0x87 ))

EFI_S3_BOOT_SCRIPT_POSITION = PVOID

class EFI_S3_SAVE_STATE_PROTOCOL (Structure):
  pass

EFI_S3_SAVE_STATE_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN  *This
  UINTN                                 # IN  OpCode
  )

EFI_S3_SAVE_STATE_INSERT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN      *This
  BOOLEAN,                              # IN      BeforeOrAfter,
  POINTER(EFI_S3_BOOT_SCRIPT_POSITION), # IN OUT  *Position       OPTIONAL,
  UINTN                                 # IN      OpCode
  )

EFI_S3_SAVE_STATE_LABEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN        *This
  BOOLEAN,                              # IN        BeforeOrAfter,
  BOOLEAN,                              # IN        CreateIfNotFound,
  POINTER(EFI_S3_BOOT_SCRIPT_POSITION), # IN OUT    *Position       OPTIONAL,
  POINTER(CHAR8)                        # IN CONST  *Label  
  )

EFI_S3_SAVE_STATE_COMPARE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_S3_SAVE_STATE_PROTOCOL),  # IN      *This
  EFI_S3_BOOT_SCRIPT_POSITION,          # IN      Position1,
  EFI_S3_BOOT_SCRIPT_POSITION,          # IN      Position2,
  POINTER(UINTN)                        #     OUT *RelativePosition  
  )

EFI_S3_SAVE_STATE_PROTOCOL._fields_ = [
    ("Write",   EFI_S3_SAVE_STATE_WRITE),
    ("Insert",  EFI_S3_SAVE_STATE_INSERT),
    ("Label",   EFI_S3_SAVE_STATE_LABEL),
    ("Compare", EFI_S3_SAVE_STATE_COMPARE)
  ]

