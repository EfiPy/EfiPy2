# PciOverride.py
#
# EfiPy2.MdePkg.Protocol.PciOverride
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.PciPlatform import EFI_PCI_PLATFORM_PROTOCOL

gEfiPciOverrideProtocolGuid = \
  EFI_GUID (0xb5b35764, 0x460c, 0x4a06, (0x99, 0xfc, 0x77, 0xa1, 0x7c, 0x1b, 0x5c, 0xeb))

EFI_PCI_OVERRIDE_PROTOCOL = EFI_PCI_PLATFORM_PROTOCOL
