# HiiPopup.py
#
# EfiPy2.MdePkg.Protocol.HiiPopup
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import \
    EFI_HII_HANDLE, \
    EFI_STRING_ID

gEfiHiiPopupProtocolGuid = \
  EFI_GUID (0x4311edc0, 0x6054, 0x46d4, (0x9e, 0x40, 0x89, 0x3e, 0xa9, 0x52, 0xfc, 0xcc ))

EFI_HII_POPUP_PROTOCOL_REVISION  = 1

class EFI_HII_POPUP_PROTOCOL (Structure):
  pass

EfiHiiPopupStyleInfo    = 1
EfiHiiPopupStyleWarning = 2
EfiHiiPopupStyleError   = 3
EFI_HII_POPUP_STYLE     = ENUM

EfiHiiPopupTypeOk           = 1
EfiHiiPopupTypeOkCancel     = 2
EfiHiiPopupTypeYesNo        = 3
EfiHiiPopupTypeYesNoCancel  = 4
EFI_HII_POPUP_TYPE          = ENUM

EfiHiiPopupSelectionOk      = 1
EfiHiiPopupSelectionCancel  = 2
EfiHiiPopupSelectionYes     = 3
EfiHiiPopupSelectionNo      = 4
EFI_HII_POPUP_SELECTION     = ENUM

EFI_HII_CREATE_POPUP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_POPUP_PROTOCOL),  #   IN  *This,
  EFI_HII_POPUP_STYLE,              #   IN  PopupStyle,
  EFI_HII_POPUP_TYPE,               #   IN  PopupType,
  EFI_HII_HANDLE,                   #   IN  HiiHandle,
  EFI_STRING_ID,                    #   IN  Message,
  POINTER(EFI_HII_POPUP_SELECTION)  #   OUT *UserSelection OPTIONAL
  )

EFI_HII_POPUP_PROTOCOL._fields_ = [
    ("Revision",        UINT64)
  ]

