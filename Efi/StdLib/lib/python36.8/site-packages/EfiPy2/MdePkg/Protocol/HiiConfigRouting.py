# HiiConfigRouting.py
#
# EfiPy2.MdePkg.Protocol.HiiConfigRouting
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import EFI_STRING

gEfiHiiConfigRoutingProtocolGuid  = \
  EFI_GUID (0x587e72d7, 0xcc50, 0x4f79, ( 0x82, 0x09, 0xca, 0x29, 0x1f, 0xc1, 0xa1, 0x0f ))

class EFI_HII_CONFIG_ROUTING_PROTOCOL (Structure):
  pass

EFI_HII_EXTRACT_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  EFI_STRING,                               # IN CONST Request,
  POINTER(EFI_STRING),                      # OUT      *Progress,
  POINTER(EFI_STRING)                       # OUT      *Results
  )

EFI_HII_EXPORT_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  POINTER(EFI_STRING)                       # OUT      *Results
  )

EFI_HII_ROUTE_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  EFI_STRING,                               # IN CONST Configuration,
  POINTER(EFI_STRING)                       # OUT      *Progress
  )

EFI_HII_BLOCK_TO_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN       *This
  EFI_STRING,                               # IN CONST ConfigRequest,
  POINTER(UINT8),                           # IN CONST *Block,
  UINTN,                                    # IN CONST BlockSize,
  POINTER(EFI_STRING),                      # OUT      *Config,
  POINTER(EFI_STRING)                       # OUT      *Progress
  )

EFI_HII_CONFIG_TO_BLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN        *This
  EFI_STRING,                               # IN CONST  ConfigResp,
  POINTER(UINT8),                           # IN OUT    *Block,
  POINTER(UINTN),                           # IN OUT    *BlockSize,
  POINTER(EFI_STRING)                       # OUT       *Progress
  )

EFI_HII_GET_ALT_CFG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_CONFIG_ROUTING_PROTOCOL), # IN        *This
  EFI_STRING,                               # IN  CONST ConfigResp, 
  POINTER(EFI_GUID),                        # IN  CONST *Guid, 
  EFI_STRING,                               # IN  CONST Name, 
  POINTER(EFI_DEVICE_PATH_PROTOCOL),        # IN  CONST *DevicePath,  
  POINTER(UINT16),                          # IN  CONST *AltCfgId,
  POINTER(EFI_STRING)                       # OUT       *AltCfgResp 
  )

EFI_HII_CONFIG_ROUTING_PROTOCOL._fields_ = [
    ("ExtractConfig", EFI_HII_EXTRACT_CONFIG),
    ("ExportConfig",  EFI_HII_EXPORT_CONFIG),
    ("RouteConfig",   EFI_HII_ROUTE_CONFIG),
    ("BlockToConfig", EFI_HII_BLOCK_TO_CONFIG),
    ("ConfigToBlock", EFI_HII_CONFIG_TO_BLOCK),
    ("GetAltConfig",  EFI_HII_GET_ALT_CFG)
  ]

