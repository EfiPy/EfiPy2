# Hsti.py
#
# EfiPy2.MdePkg.IndustryStandard.Hsti
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import *

gAdapterInfoPlatformSecurityGuid = EFI_GUID( 0x6be272c7, 0x1320, 0x4ccd, (0x90, 0x17, 0xd4, 0x61, 0x2c, 0x01, 0x2b, 0x25))

PLATFORM_SECURITY_VERSION_VNEXTCS  = 0x00000003

PLATFORM_SECURITY_ROLE_PLATFORM_REFERENCE  = 0x00000001 # IHV
PLATFORM_SECURITY_ROLE_PLATFORM_IBV        = 0x00000002
PLATFORM_SECURITY_ROLE_IMPLEMENTOR_OEM     = 0x00000003
PLATFORM_SECURITY_ROLE_IMPLEMENTOR_ODM     = 0x00000004

class ADAPTER_INFO_PLATFORM_SECURITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",              UINT32     ),
    ("Role",                 UINT32     ),
    ("ImplementationID",     CHAR16 *256),
    ("SecurityFeaturesSize", UINT32     )
    # ("SecurityFeaturesRequired",      UINT8  * N),
    # ("SecurityFeaturesImplemented",   UINT8  * N),
    # ("SecurityFeaturesVerified",      UINT8  * N),
    # ("ErrorString",                   CHAR16 * N)
  ]

