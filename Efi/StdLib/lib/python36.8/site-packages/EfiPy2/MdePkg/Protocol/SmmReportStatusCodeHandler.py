# SmmReportStatusCodeHandler.py
#
# EfiPy2.MdePkg.Protocol.SmmReportStatusCodeHandler
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmReportStatusCodeHandler

gEfiSmmRscHandlerProtocolGuid = MmReportStatusCodeHandler.gEfiMmRscHandlerProtocolGuid

EFI_SMM_RSC_HANDLER_CALLBACK = MmReportStatusCodeHandler.EFI_MM_RSC_HANDLER_CALLBACK

EFI_SMM_RSC_HANDLER_REGISTER = MmReportStatusCodeHandler.EFI_MM_RSC_HANDLER_REGISTER

EFI_SMM_RSC_HANDLER_UNREGISTER = MmReportStatusCodeHandler.EFI_MM_RSC_HANDLER_UNREGISTER

EFI_SMM_RSC_HANDLER_PROTOCOL = MmReportStatusCodeHandler.EFI_MM_RSC_HANDLER_PROTOCOL

