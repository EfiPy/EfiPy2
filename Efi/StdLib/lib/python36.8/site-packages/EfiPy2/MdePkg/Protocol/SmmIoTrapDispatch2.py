# SmmIoTrapDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmIoTrapDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmIoTrapDispatch

gEfiSmmIoTrapDispatch2ProtocolGuid = MmIoTrapDispatch.gEfiMmIoTrapDispatchProtocolGuid

EFI_SMM_IO_TRAP_DISPATCH_TYPE = MmIoTrapDispatch.EFI_MM_IO_TRAP_DISPATCH_TYPE
EFI_SMM_IO_TRAP_REGISTER_CONTEXT = MmIoTrapDispatch.EFI_MM_IO_TRAP_REGISTER_CONTEXT
EFI_SMM_IO_TRAP_CONTEXT = MmIoTrapDispatch.EFI_MM_IO_TRAP_CONTEXT
EFI_SMM_IO_TRAP_DISPATCH2_PROTOCOL = MmIoTrapDispatch.EFI_MM_IO_TRAP_DISPATCH_PROTOCOL

EFI_SMM_IO_TRAP_DISPATCH2_REGISTER = MmIoTrapDispatch.EFI_MM_IO_TRAP_DISPATCH_REGISTER

EFI_SMM_IO_TRAP_DISPATCH2_UNREGISTER = MmIoTrapDispatch.EFI_MM_IO_TRAP_DISPATCH_UNREGISTER

