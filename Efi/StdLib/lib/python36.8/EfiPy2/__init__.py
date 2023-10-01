# __init__.py
#
# EfiPy2.__init__
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
import _EfiPy2
from ctypes   import *
from ctypes   import _SimpleCData

from EfiPy2.MdePkg.Uefi.UefiBaseType import *
from EfiPy2.MdePkg.Uefi.UefiSpec     import *

from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_IA32
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_X64
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_ARM
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_AARCH64
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_RISCV64
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_LOONGARCH64

from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME

#
# UEFI basic tables gST, gRT, gBS
#

gRT = EFI_RUNTIME_SERVICES.from_address (_EfiPy2.EfiPygRtAddr)
gST = EFI_SYSTEM_TABLE.from_address     (_EfiPy2.EfiPygStAddr)
gBS = EFI_BOOT_SERVICES.from_address    (_EfiPy2.EfiPygBsAddr)

#
# EDK basic image handle
#

gImageHandle = EFI_HANDLE.from_address( _EfiPy2.gImageHandle)
# pImageHandle = EFI_HANDLE.from_address( _EfiPy2.pImageHandle)

