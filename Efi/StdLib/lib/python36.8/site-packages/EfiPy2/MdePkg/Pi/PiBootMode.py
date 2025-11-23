# PiBootMode.py
#
# EfiPy2.MdePkg.Pi.PiBootMode
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

EFI_BOOT_MODE = UINT32

BOOT_WITH_FULL_CONFIGURATION                   = 0x00
BOOT_WITH_MINIMAL_CONFIGURATION                = 0x01
BOOT_ASSUMING_NO_CONFIGURATION_CHANGES         = 0x02
BOOT_WITH_FULL_CONFIGURATION_PLUS_DIAGNOSTICS  = 0x03
BOOT_WITH_DEFAULT_SETTINGS                     = 0x04
BOOT_ON_S4_RESUME                              = 0x05
BOOT_ON_S5_RESUME                              = 0x06
BOOT_WITH_MFG_MODE_SETTINGS                    = 0x07
BOOT_ON_S2_RESUME                              = 0x10
BOOT_ON_S3_RESUME                              = 0x11
BOOT_ON_FLASH_UPDATE                           = 0x12
BOOT_IN_RECOVERY_MODE                          = 0x20

