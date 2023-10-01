# SmmCommunication.py
#
# EfiPy2.MdePkg.Protocol.SmmCommunication
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.MmCommunication import EFI_MM_COMMUNICATE_HEADER,       \
                                                   EFI_MM_COMMUNICATION_PROTOCOL,   \
                                                   gEfiMmCommunicationProtocolGuid

EFI_SMM_COMMUNICATE_HEADER = EFI_MM_COMMUNICATE_HEADER

gEfiSmmCommunicationProtocolGuid = gEfiMmCommunicationProtocolGuid

EFI_SMM_COMMUNICATION_PROTOCOL = EFI_MM_COMMUNICATION_PROTOCOL
