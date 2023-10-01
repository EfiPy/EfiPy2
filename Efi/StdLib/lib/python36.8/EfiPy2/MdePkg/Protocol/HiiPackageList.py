# HiiPackageList.py
#
# EfiPy2.MdePkg.Protocol.HiiPackageList
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import EFI_HII_PACKAGE_LIST_HEADER

gEfiHiiPackageListProtocolGuid = \
  EFI_GUID (0x6a1ee763, 0xd47a, 0x43b4, (0xaa, 0xbe, 0xef, 0x1d, 0xe2, 0xab, 0x56, 0xfc ))

EFI_HII_PACKAGE_LIST_PROTOCOL = POINTER(EFI_HII_PACKAGE_LIST_HEADER)

