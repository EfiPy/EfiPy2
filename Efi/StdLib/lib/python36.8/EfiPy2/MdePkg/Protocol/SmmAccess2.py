# SmmAccess2.py
#
# EfiPy2.MdePkg.Protocol.SmmAccess2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.MmAccess import gEfiMmAccessProtocolGuid,   \
                                            EFI_MM_ACCESS_PROTOCOL,     \
                                            EFI_MM_OPEN,                \
                                            EFI_MM_CLOSE,               \
                                            EFI_MM_LOCK,                \
                                            EFI_MM_CAPABILITIES

gEfiSmmAccess2ProtocolGuid = gEfiMmAccessProtocolGuid

EFI_SMM_ACCESS2_PROTOCOL = EFI_MM_ACCESS_PROTOCOL

EFI_SMM_OPEN2 = EFI_MM_OPEN

EFI_SMM_CLOSE2 = EFI_MM_CLOSE

EFI_SMM_LOCK2 = EFI_MM_LOCK

EFI_SMM_CAPABILITIES2 = EFI_MM_CAPABILITIES

