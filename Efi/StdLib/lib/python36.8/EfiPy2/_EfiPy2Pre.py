# _EfiPy2Pre.py
#
# _EfiPy2Pre
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Linux
# 
#  os.name                  'posix'
#  sys.platform()           'linux'
#  platform.machine()       'x86_64'
#  platform.architecture()  ('64bit', 'ELF')
#
# Windows 10
# 
#  os.name                  'nt'
#  sys.platform()           'win32'
#  platform.machine()       'AMD64'
#  platform.architecture()  ('64bit', 'WindowsPE')
#
# uefi shell
# 
#  os.name                  'edk2'
#  sys.platform()           'uefi'
#  platform.machine()       ''
#  platform.architecture()  ('64bit', '')
#

import os
if os.name == 'edk2':
  from _EfiPy2 import *
else:
  import platform
  if platform.machine() in ['x86_64', 'AMD64']:

    EFI_REMOVABLE_MEDIA_FILE_NAME_IA32          = r"\EFI\BOOT\BOOTIA32.EFI"
    EFI_REMOVABLE_MEDIA_FILE_NAME_X64           = r"\EFI\BOOT\BOOTX64.EFI"
    EFI_REMOVABLE_MEDIA_FILE_NAME_ARM           = r"\EFI\BOOT\BOOTARM.EFI"
    EFI_REMOVABLE_MEDIA_FILE_NAME_AARCH64       = r"\EFI\BOOT\BOOTAA64.EFI"
    EFI_REMOVABLE_MEDIA_FILE_NAME_RISCV64       = r"\EFI\BOOT\BOOTRISCV64.EFI"
    EFI_REMOVABLE_MEDIA_FILE_NAME_LOONGARCH64   = r"\EFI\BOOT\BOOTLOONGARCH64.EFI"

    EFIPY_MDE_CPU_IA32                          = 0
    EFIPY_MDE_CPU_X64                           = 1
    EFIPY_MDE_CPU_ARM                           = 2
    EFIPY_MDE_CPU_AARCH64                       = 3
    EFIPY_MDE_CPU_EBC                           = 4
    EFIPY_MDE_CPU_RISCV64                       = 5
    EFIPY_MDE_CPU_LOONGARCH64                   = 6

    EFIPY_MDE_CPU_TYPE            = EFIPY_MDE_CPU_X64
    EFI_REMOVABLE_MEDIA_FILE_NAME = EFI_REMOVABLE_MEDIA_FILE_NAME_X64

    _platformBits, _      = platform.architecture()

    MAX_BIT               = 0x8000000000000000
    MAX_2_BITS            = 0xC000000000000000
    MAX_ADDRESS           = 0xFFFFFFFFFFFFFFFF
    CPU_STACK_ALIGNMENT   = 16
    gImageHandle          = 0
    pImageHandle          = 0
    EfiPygStAddr          = 0
    EfiPygRtAddr          = 0
    EfiPygBsAddr          = 0
