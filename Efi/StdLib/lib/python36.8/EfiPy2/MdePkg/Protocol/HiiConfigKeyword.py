# HiiConfigKeyword.py
#
# EfiPy2.MdePkg.Protocol.HiiConfigKeyword
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import EFI_STRING

gEfiConfigKeywordHandlerProtocolGuid = \
  EFI_GUID (0x0a8badd5, 0x03b8, 0x4d19, (0xb1, 0x28, 0x7b, 0x8f, 0x0e, 0xda, 0xa5, 0x96 ))

KEYWORD_HANDLER_NO_ERROR                     = 0x00000000
KEYWORD_HANDLER_NAMESPACE_ID_NOT_FOUND       = 0x00000001
KEYWORD_HANDLER_MALFORMED_STRING             = 0x00000002
KEYWORD_HANDLER_KEYWORD_NOT_FOUND            = 0x00000004
KEYWORD_HANDLER_INCOMPATIBLE_VALUE_DETECTED  = 0x00000008
KEYWORD_HANDLER_ACCESS_NOT_PERMITTED         = 0x00000010
KEYWORD_HANDLER_UNDEFINED_PROCESSING_ERROR   = 0x80000000

class EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL (Structure):
  pass

EFI_CONFIG_KEYWORD_HANDLER_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL), # IN       *This
  EFI_STRING,                                   # IN CONST KeywordString,
  POINTER(EFI_STRING),                          # OUT      *Progress,
  POINTER(UINT32)                               # OUT      *ProgressErr
  )

EFI_CONFIG_KEYWORD_HANDLER_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL), # IN       *This
  EFI_STRING,                                   # IN CONST NameSpaceId, OPTIONAL
  EFI_STRING,                                   # IN CONST KeywordString, OPTIONAL
  POINTER(EFI_STRING),                          # OUT      *Progress, 
  POINTER(UINT32),                              # OUT      *ProgressErr,
  POINTER(EFI_STRING)                           # OUT      *Results
  )

EFI_CONFIG_KEYWORD_HANDLER_PROTOCOL._fields_ = [
  ("SetData", EFI_CONFIG_KEYWORD_HANDLER_SET_DATA),
  ("GetData", EFI_CONFIG_KEYWORD_HANDLER_GET_DATA)
  ]

