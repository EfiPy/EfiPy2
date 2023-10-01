# S3SmmSaveState.py
#
# EfiPy2.MdePkg.Protocol.S3SmmSaveState
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.S3SaveState import EFI_S3_SAVE_STATE_PROTOCOL

gEfiS3SmmSaveStateProtocolGuid   = \
  EFI_GUID (0x320afe62, 0xe593, 0x49cb, ( 0xa9, 0xf1, 0xd4, 0xc2, 0xf4, 0xaf, 0x1, 0x4c ))

EFI_S3_SMM_SAVE_STATE_PROTOCOL = EFI_S3_SAVE_STATE_PROTOCOL

