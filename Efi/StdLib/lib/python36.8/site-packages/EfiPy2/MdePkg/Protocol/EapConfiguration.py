# EapConfiguration.py
#
# EfiPy2.MdePkg.Protocol.EapConfiguration
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiEapConfigurationProtocolGuid  = \
  EFI_GUID (0xe5b58dbb, 0x7688, 0x44b4, (0x97, 0xbf, 0x5f, 0x1d, 0x4b, 0x7c, 0xc8, 0xdb ))

class EFI_EAP_CONFIGURATION_PROTOCOL (Structure):
  pass

EFI_EAP_TYPE_ATTRIBUTE = 0

EfiEapConfigEapAuthMethod                       =  0
EfiEapConfigEapSupportedAuthMethod              =  1
EfiEapConfigIdentityString                      =  2
EfiEapConfigEapTlsCACert                        =  3
EfiEapConfigEapTlsClientCert                    =  4
EfiEapConfigEapTlsClientPrivateKeyFile          =  5
EfiEapConfigEapTlsClientPrivateKeyFilePassword  =  6
EfiEapConfigEapTlsCipherSuite                   =  7
EfiEapConfigEapTlsSupportedCipherSuite          =  8
EfiEapConfigEapMSChapV2Password                 =  9
EfiEapConfigEap2ndAuthMethod                    = 10
EFI_EAP_CONFIG_DATA_TYPE                        = ENUM

EFI_EAP_TYPE                = UINT8
EFI_EAP_TYPE_ATTRIBUTE      = 0
EFI_EAP_TYPE_IDENTITY       = 1
EFI_EAP_TYPE_NOTIFICATION   = 2
EFI_EAP_TYPE_NAK            = 3
EFI_EAP_TYPE_MD5CHALLENGE   = 4
EFI_EAP_TYPE_OTP            = 5
EFI_EAP_TYPE_GTC            = 6
EFI_EAP_TYPE_EAPTLS         = 13
EFI_EAP_TYPE_EAPSIM         = 18
EFI_EAP_TYPE_TTLS           = 21
EFI_EAP_TYPE_PEAP           = 25
EFI_EAP_TYPE_MSCHAPV2       = 26
EFI_EAP_TYPE_EAP_EXTENSION  = 33

EFI_EAP_CONFIGURATION_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_CONFIGURATION_PROTOCOL),  # IN *This,
  EFI_EAP_TYPE,                             # IN EapType,
  EFI_EAP_CONFIG_DATA_TYPE,                 # IN DataType,
  PVOID,                                    # IN *Data,
  UINTN                                     # IN DataSize
  )

EFI_EAP_CONFIGURATION_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_CONFIGURATION_PROTOCOL),  # IN      *This,
  EFI_EAP_TYPE,                             # IN      EapType,
  EFI_EAP_CONFIG_DATA_TYPE,                 # IN      DataType,
  PVOID,                                    # IN OUT  *Data,
  POINTER(UINTN)                            # IN OUT  DataSize
  )

EFI_EAP_CONFIGURATION_PROTOCOL._fields_ = [
    ("SetData", EFI_EAP_CONFIGURATION_SET_DATA),
    ("GetData", EFI_EAP_CONFIGURATION_GET_DATA)
  ]

