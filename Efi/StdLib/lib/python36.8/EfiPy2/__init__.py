# __init__.py
#
# EfiPy2.__init__
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
import _EfiPy2Pre
from ctypes   import *
from ctypes   import _SimpleCData

from EfiPy2.MdePkg.Uefi.UefiBaseType import *
from EfiPy2.MdePkg.Uefi.UefiSpec     import *

from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME_IA32
from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME_X64
from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME_ARM
from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME_AARCH64
from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME_RISCV64
from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME_LOONGARCH64

from _EfiPy2Pre import EFI_REMOVABLE_MEDIA_FILE_NAME

#
# UEFI basic tables gST, gRT, gBS
#

gRT = EFI_RUNTIME_SERVICES.from_address (_EfiPy2Pre.EfiPygRtAddr)
gST = EFI_SYSTEM_TABLE.from_address     (_EfiPy2Pre.EfiPygStAddr)
gBS = EFI_BOOT_SERVICES.from_address    (_EfiPy2Pre.EfiPygBsAddr)

#
# EDK basic image handle
#

gImageHandle = EFI_HANDLE.from_address( _EfiPy2Pre.gImageHandle)
# pImageHandle = EFI_HANDLE.from_address( _EfiPy2Pre.pImageHandle)

