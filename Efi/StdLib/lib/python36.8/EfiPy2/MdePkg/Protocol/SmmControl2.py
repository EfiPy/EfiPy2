# SmmControl2.py
#
# EfiPy2.MdePkg.Protocol.SmmControl2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.MmControl import gEfiMmControlProtocolGuid, \
                                             EFI_MM_CONTROL_PROTOCOL,   \
                                             EFI_MM_PERIOD,             \
                                             EFI_MM_ACTIVATE,           \
                                             EFI_MM_DEACTIVATE

gEfiSmmControl2ProtocolGuid = gEfiMmControlProtocolGuid

EFI_SMM_CONTROL2_PROTOCOL = EFI_MM_CONTROL_PROTOCOL

EFI_SMM_PERIOD = EFI_MM_PERIOD

EFI_SMM_ACTIVATE2 = EFI_MM_ACTIVATE

EFI_SMM_DEACTIVATE2 = EFI_MM_DEACTIVATE

