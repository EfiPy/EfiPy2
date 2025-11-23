# HiiString.py
#
# EfiPy2.MdePkg.Protocol.HiiString
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.Uefi.UefiBaseType   import *
from EfiPy2.MdePkg.Uefi.UefiSpec       import *

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import \
    EFI_HII_HANDLE, \
    EFI_STRING_ID,  \
    EFI_STRING

from EfiPy2.MdePkg.Protocol import HiiFont

gEfiHiiStringProtocolGuid = \
  EFI_GUID (0xfd96974, 0x23aa, 0x4cdc, ( 0xb9, 0xcb, 0x98, 0xd1, 0x77, 0x50, 0x32, 0x2a ))

class EFI_HII_STRING_PROTOCOL (Structure):
  pass

EFI_HII_NEW_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL),   # IN CONST  *This,
  EFI_HII_HANDLE,                     # IN        PackageList,
  POINTER(EFI_STRING_ID),             # OUT       *StringId,
  PCHAR8,                             # IN CONST  *Language,
  PCHAR16,                            # IN  CONST *LanguageName, OPTIONAL  
  EFI_STRING,                         # IN CONST  String,
  POINTER(HiiFont.EFI_FONT_INFO)      # IN CONST  *StringFontInfo OPTIONAL
  )

EFI_HII_GET_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL),       # IN CONST  *This,
  PCHAR8,                                 # IN CONST  *Language,
  EFI_HII_HANDLE,                         # IN        PackageList,
  EFI_STRING_ID,                          # IN        StringId,
  EFI_STRING,                             # OUT       String,
  POINTER(UINTN),                         # IN OUT    *StringSize,
  POINTER(POINTER(HiiFont.EFI_FONT_INFO)) # OUT       **StringFontInfo OPTIONAL
  )

EFI_HII_SET_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                   # IN        PackageList,
  EFI_STRING_ID,                    # IN        StringId,
  PCHAR8,                           # IN CONST  *Language,
  EFI_STRING,                       # IN        String,
  POINTER(HiiFont.EFI_FONT_INFO)    # IN CONST  *StringFontInfo OPTIONAL
  )

EFI_HII_GET_LANGUAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                   # IN        PackageList,
  PCHAR8,                           # IN OUT    *Languages,
  POINTER(UINTN)                    # IN OUT    *LanguagesSize
  )

EFI_HII_GET_2ND_LANGUAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_STRING_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                   # IN        PackageList,
  PCHAR8,                           # IN CONST  *PrimaryLanguage,
  PCHAR8,                           # IN OUT    *SecondaryLanguages,
  POINTER(UINTN)                    # IN OUT    *SecondaryLanguagesSize
  )

EFI_HII_STRING_PROTOCOL._fields_ = [
    ("NewString",             EFI_HII_NEW_STRING),
    ("GetString",             EFI_HII_GET_STRING),
    ("SetString",             EFI_HII_SET_STRING),
    ("GetLanguages",          EFI_HII_GET_LANGUAGES),
    ("GetSecondaryLanguages", EFI_HII_GET_2ND_LANGUAGES)
  ]

