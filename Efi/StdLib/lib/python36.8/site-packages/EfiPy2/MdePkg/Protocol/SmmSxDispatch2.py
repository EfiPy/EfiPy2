# SmmSxDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmSxDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmSxDispatch
from EfiPy2.MdePkg.Protocol import MmSwDispatch

gEfiSmmSxDispatch2ProtocolGuid = MmSwDispatch.gEfiMmSwDispatchProtocolGuid

EFI_SMM_SX_REGISTER_CONTEXT = MmSxDispatch.EFI_MM_SX_REGISTER_CONTEXT

EFI_SMM_SX_DISPATCH2_PROTOCOL = MmSxDispatch.EFI_MM_SX_DISPATCH_PROTOCOL

EFI_SMM_SX_REGISTER2 = MmSxDispatch.EFI_MM_SX_REGISTER

EFI_SMM_SX_UNREGISTER2 = MmSxDispatch.EFI_MM_SX_UNREGISTER

