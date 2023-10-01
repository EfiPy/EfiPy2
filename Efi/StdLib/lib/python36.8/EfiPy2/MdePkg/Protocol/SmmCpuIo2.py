# SmmCpuIo2.py
#
# EfiPy2.MdePkg.Protocol.SmmCpuIo2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import MmCpuIo

gEfiSmmCpuIo2ProtocolGuid = MmCpuIo.gEfiMmCpuIoProtocolGuid

EFI_SMM_CPU_IO2_PROTOCOL  = MmCpuIo.EFI_MM_CPU_IO_PROTOCOL

SMM_IO_UINT8   = MmCpuIo.MM_IO_UINT8
SMM_IO_UINT16  = MmCpuIo.MM_IO_UINT16
SMM_IO_UINT32  = MmCpuIo.MM_IO_UINT32
SMM_IO_UINT64  = MmCpuIo.MM_IO_UINT64

EFI_SMM_IO_WIDTH    = MmCpuIo.EFI_MM_IO_WIDTH
EFI_SMM_CPU_IO2     = MmCpuIo.EFI_MM_CPU_IO

EFI_SMM_IO_ACCESS2  = MmCpuIo.EFI_MM_IO_ACCESS
