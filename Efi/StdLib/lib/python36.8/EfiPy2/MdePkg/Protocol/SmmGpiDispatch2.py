# SmmGpiDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmGpiDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmGpiDispatch

gEfiSmmGpiDispatch2ProtocolGuid = MmGpiDispatch.gEfiMmGpiDispatchProtocolGuid

EFI_SMM_GPI_REGISTER_CONTEXT = MmGpiDispatch.EFI_MM_GPI_REGISTER_CONTEXT

EFI_SMM_GPI_REGISTER2 = MmGpiDispatch.EFI_MM_GPI_REGISTER

EFI_SMM_GPI_UNREGISTER2 = MmGpiDispatch.EFI_MM_GPI_UNREGISTER

EFI_SMM_GPI_DISPATCH2_PROTOCOL = MmGpiDispatch.EFI_MM_GPI_DISPATCH_PROTOCOL

