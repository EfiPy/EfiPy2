# ConformanceProfiles.py
#
# EfiPy2.MdePkg.IndustryStandard.ConformanceProfiles
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiConfProfilesTableGuid = EFI_GUID (0x36122546, 0xf7e7, 0x4c8f, ( 0xbd, 0x9b, 0xeb, 0x85, 0x25, 0xb5, 0x0c, 0x0b ))

class EFI_CONFORMANCE_PROFILES_TABLE (Structure):
  _fields_ = [
  ("Version",             UINT16),
  ("NumberOfProfiles",    UINT16)
  # ("ConformanceProfiles", EFI_GUID)
  ]

EFI_CONFORMANCE_PROFILES_TABLE_VERSION  = 0x1

gEfiConfProfilesUefiSpecGuid = EFI_GUID ( 0x523c91af, 0xa195, 0x4382, ( 0x81, 0x8d, 0x29, 0x5f, 0xe4, 0x00, 0x64, 0x65 ))

EFI_CONFORMANCE_PROFILE_EBBR_2_1_GUID = EFI_GUID ( 0xcce33c35, 0x74ac, 0x4087, ( 0xbc, 0xe7, 0x8b, 0x29, 0xb0, 0x2e, 0xeb, 0x27 ))
EFI_CONFORMANCE_PROFILE_EBBR_2_2_GUID = EFI_GUID ( 0x9073eed4, 0xe50d, 0x11ee, ( 0xb8, 0xb0, 0x8b, 0x68, 0xda, 0x62, 0xfc, 0x80 ))

