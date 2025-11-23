# SmmUsbDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmUsbDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmUsbDispatch

gEfiSmmUsbDispatch2ProtocolGuid = MmUsbDispatch.gEfiMmUsbDispatchProtocolGuid

EFI_USB_SMI_TYPE = MmUsbDispatch.EFI_USB_MMI_TYPE

EFI_SMM_USB_REGISTER_CONTEXT = MmUsbDispatch.EFI_MM_USB_REGISTER_CONTEXT

EFI_SMM_USB_DISPATCH2_PROTOCOL = MmUsbDispatch.EFI_MM_USB_DISPATCH_PROTOCOL

EFI_SMM_USB_REGISTER2 = MmUsbDispatch.EFI_MM_USB_REGISTER

EFI_SMM_USB_UNREGISTER2 = MmUsbDispatch.EFI_MM_USB_UNREGISTER

