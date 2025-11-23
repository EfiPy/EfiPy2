# GuidedSectionExtraction.py
#
# EfiPy2.MdePkg.Protocol.GuidedSectionExtraction
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

class EFI_GUIDED_SECTION_EXTRACTION_PROTOCOL (Structure):
  pass

EFI_EXTRACT_GUIDED_SECTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUIDED_SECTION_EXTRACTION_PROTOCOL),  # IN        *This
  PVOID,                                            # IN CONST  *InputSection,
  POINTER(PVOID),                                   # OUT       **OutputBuffer,
  POINTER(UINTN),                                   # OUT       *OutputSize,
  POINTER(UINT32)                                   # OUT       *AuthenticationStatus
  )

EFI_GUIDED_SECTION_EXTRACTION_PROTOCOL._fields_ = [
  ("ExtractSection",    EFI_EXTRACT_GUIDED_SECTION),
  ]

