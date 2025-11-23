# TlsConfig.py
#
# EfiPy2.MdePkg.Protocol.TlsConfig
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiTlsConfigurationProtocolGuid = \
  EFI_GUID (0x1682fe44, 0xbd7a, 0x4407, ( 0xb7, 0xc7, 0xdc, 0xa3, 0x7c, 0xa3, 0x92, 0x2d ))

class EFI_TLS_CONFIGURATION_PROTOCOL (Structure):
  pass

EfiTlsConfigDataTypeHostPublicCert      = 1
EfiTlsConfigDataTypeHostPrivateKey      = 2
EfiTlsConfigDataTypeCACertificate       = 3
EfiTlsConfigDataTypeCertRevocationList  = 4
EfiTlsConfigDataTypeMaximum             = 5
EFI_TLS_CONFIG_DATA_TYPE                = ENUM

EFI_TLS_CONFIGURATION_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TLS_CONFIGURATION_PROTOCOL),  #   IN *This,
  EFI_TLS_CONFIG_DATA_TYPE,                 #   IN DataType,
  PVOID,                                    #   IN *Data,
  UINTN                                     #   IN DataSize
  )

EFI_TLS_CONFIGURATION_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TLS_CONFIGURATION_PROTOCOL),  #   IN     *This,
  EFI_TLS_CONFIG_DATA_TYPE,                 #   IN     DataType,
  PVOID,                                    #   IN OUT *Data,
  POINTER(UINTN)                            #   IN OUT *DataSize
  )

EFI_TLS_CONFIGURATION_PROTOCOL._fields_ = [
    ("SetData",      EFI_TLS_CONFIGURATION_SET_DATA),
    ("GetData",      EFI_TLS_CONFIGURATION_GET_DATA)
  ]

