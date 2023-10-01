# SmmStandbyButtonDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmStandbyButtonDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmStandbyButtonDispatch

gEfiSmmStandbyButtonDispatch2ProtocolGuid = MmStandbyButtonDispatch.gEfiMmStandbyButtonDispatchProtocolGuid

EFI_SMM_STANDBY_BUTTON_REGISTER_CONTEXT = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_REGISTER_CONTEXT

EFI_SMM_STANDBY_BUTTON_DISPATCH2_PROTOCOL = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL

EFI_SMM_STANDBY_BUTTON_REGISTER2 = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_REGISTER
EFI_SMM_STANDBY_BUTTON_UNREGISTER2 = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_UNREGISTER

