# SmmPowerButtonDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmPowerButtonDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmPowerButtonDispatch
gEfiSmmPowerButtonDispatch2ProtocolGuid = MmPowerButtonDispatch.gEfiMmPowerButtonDispatchProtocolGuid

EFI_SMM_POWER_BUTTON_REGISTER_CONTEXT = MmPowerButtonDispatch.EFI_MM_POWER_BUTTON_REGISTER_CONTEXT

EFI_SMM_POWER_BUTTON_DISPATCH2_PROTOCOL = MmPowerButtonDispatch.EFI_MM_POWER_BUTTON_DISPATCH_PROTOCOL

EFI_SMM_POWER_BUTTON_REGISTER2 = MmPowerButtonDispatch.EFI_MM_POWER_BUTTON_REGISTER

EFI_SMM_POWER_BUTTON_UNREGISTER2 = MmPowerButtonDispatch.EFI_MM_POWER_BUTTON_UNREGISTER

