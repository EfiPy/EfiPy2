# IScsiInitiatorName.py
#
# EfiPy2.MdePkg.Protocol.IScsiInitiatorName
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiIScsiInitiatorNameProtocolGuid  = \
  EFI_GUID (0x59324945, 0xec44, 0x4c0d, (0xb1, 0xcd, 0x9d, 0xb1, 0x39, 0xdf, 0x7, 0xc ))

class EFI_ISCSI_INITIATOR_NAME_PROTOCOL (Structure):
  pass

EFI_ISCSI_INITIATOR_NAME_GET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISCSI_INITIATOR_NAME_PROTOCOL), # IN      *This,
  POINTER(UINTN),                             # IN OUT  *BufferSize,
  PVOID                                       # OUT     *Buffer
  )

EFI_ISCSI_INITIATOR_NAME_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISCSI_INITIATOR_NAME_PROTOCOL), # IN      *This,
  POINTER(UINTN),                             # IN OUT  *BufferSize,
  PVOID                                       # IN      *Buffer
  )

EFI_ISCSI_INITIATOR_NAME_PROTOCOL._fields_ = [
    ("Get", EFI_ISCSI_INITIATOR_NAME_GET),
    ("Set", EFI_ISCSI_INITIATOR_NAME_SET)
  ]

