# RegularExpressionProtocol.py
#
# EfiPy2.MdePkg.Protocol.RegularExpressionProtocol
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiRegularExpressionProtocolGuid       = \
  EFI_GUID(0xB3F79D9A, 0x436C, 0xDC11, (0xB0, 0x52, 0xCD, 0x85, 0xDF, 0x52, 0x4C, 0xE6 ))

gEfiRegexSyntaxTypePosixExtendedGuid    = \
  EFI_GUID(0x5F05B20F, 0x4A56, 0xC231, (0xFA, 0x0B, 0xA7, 0xB1, 0xF1, 0x10, 0x04, 0x1D ))

gEfiRegexSyntaxTypePerlGuid             = \
  EFI_GUID(0x63E60A51, 0x497D, 0xD427, (0xC4, 0xA5, 0xB8, 0xAB, 0xDC, 0x3A, 0xAE, 0xB6 ))

gEfiRegexSyntaxTypeEcma262Guid          = \
  EFI_GUID(0x9A473A4A, 0x4CEB, 0xB95A, (0x41, 0x5E, 0x5B, 0xA0, 0xBC, 0x63, 0x9B, 0x2E ))

class EFI_REGULAR_EXPRESSION_PROTOCOL (Structure):
  pass

class EFI_REGEX_CAPTURE (Structure):
  _fields_ = [
    ("CapturePtr",  POINTER(CHAR16)),
    ("Length",      UINTN)
  ]

EFI_REGEX_SYNTAX_TYPE = EFI_GUID

EFI_REGULAR_EXPRESSION_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REGULAR_EXPRESSION_PROTOCOL), # IN      *This
  POINTER(UINTN),                           # IN OUT  *RegExSyntaxTypeListSize,
  POINTER(EFI_REGEX_SYNTAX_TYPE)            # OUT     *RegExSyntaxTypeList
  )

EFI_REGULAR_EXPRESSION_MATCH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REGULAR_EXPRESSION_PROTOCOL), # IN  *This
  PCHAR16,                                  # IN  *String,
  PCHAR16,                                  # IN  *Pattern,
  POINTER(EFI_REGEX_SYNTAX_TYPE),           # IN  *SyntaxType, OPTIONAL
  POINTER(BOOLEAN),                         # OUT *Result,
  POINTER(POINTER(EFI_REGEX_CAPTURE)),      # OUT **Captures, OPTIONAL
  POINTER(UINTN)                            # OUT *CapturesCount
  )

EFI_REGULAR_EXPRESSION_PROTOCOL._fields_ = [
    ("MatchString", EFI_REGULAR_EXPRESSION_MATCH),
    ("GetInfo",     EFI_REGULAR_EXPRESSION_GET_INFO)
  ]

