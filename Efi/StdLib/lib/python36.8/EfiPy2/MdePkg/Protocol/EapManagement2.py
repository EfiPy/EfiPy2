# EapManagement2.py
#
# EfiPy2.MdePkg.Protocol.EapManagement2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import EapManagement

gEfiEapManagement2ProtocolGuid    = \
  EFI_GUID (0x5e93c847, 0x456d, 0x40b3, (0xa6, 0xb4, 0x78, 0xb0, 0xc9, 0xcf, 0x7f, 0x20 ))

class EFI_EAP_MANAGEMENT2_PROTOCOL (Structure):
  pass

EFI_EAP_GET_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT2_PROTOCOL),  # IN     *This
  POINTER(UINT8),                         # IN OUT *Msk,
  POINTER(UINTN),                         # IN OUT *MskSize,
  POINTER(UINT8),                         # IN OUT *Emsk,
  POINTER(UINT8)                          # IN OUT *EmskSize
  )

EFI_EAP_MANAGEMENT2_PROTOCOL._fields_ = [
    ("GetSystemConfiguration",      EapManagement.EFI_EAP_GET_SYSTEM_CONFIGURATION),
    ("SetSystemConfiguration",      EapManagement.EFI_EAP_SET_SYSTEM_CONFIGURATION),
    ("InitializePort",              EapManagement.EFI_EAP_INITIALIZE_PORT),
    ("UserLogon",                   EapManagement.EFI_EAP_USER_LOGON),
    ("UserLogoff",                  EapManagement.EFI_EAP_USER_LOGOFF),
    ("GetSupplicantStatus",         EapManagement.EFI_EAP_GET_SUPPLICANT_STATUS),
    ("SetSupplicantConfiguration",  EapManagement.EFI_EAP_SET_SUPPLICANT_CONFIGURATION),
    ("GetSupplicantStatistics",     EapManagement.EFI_EAP_GET_SUPPLICANT_STATISTICS),
    ("GetKey",                      EFI_EAP_GET_KEY)
  ]

