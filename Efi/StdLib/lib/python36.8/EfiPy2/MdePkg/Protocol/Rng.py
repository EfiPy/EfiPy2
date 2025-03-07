# Rng.py
#
# EfiPy2.MdePkg.Protocol.Rng
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Guid import Rng

gEfiRngProtocolGuid                 = \
  EFI_GUID (0x3152bca5, 0xeade, 0x433d, (0x86, 0x2e, 0xc0, 0x1c, 0xdc, 0x29, 0x1f, 0x44 ))

EFI_RNG_PROTOCOL = Rng.EFI_RNG_INTERFACE

