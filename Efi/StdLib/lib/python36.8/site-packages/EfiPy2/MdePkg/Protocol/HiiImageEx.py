# HiiImageEx.py
#
# EfiPy2.MdePkg.Protocol.HiiImageEx
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import EFI_HII_HANDLE, EFI_IMAGE_ID
from EfiPy2.MdePkg.Protocol.HiiImage import EFI_IMAGE_INPUT,    \
                                            EFI_IMAGE_OUTPUT,   \
                                            EFI_HII_DRAW_FLAGS

gEfiHiiImageExProtocolGuid = \
  EFI_GUID (0x1a1241e6, 0x8f19, 0x41a9,  ( 0xbc, 0xe, 0xe8, 0xef, 0x39, 0xe0, 0x65, 0x46 ))

class EFI_HII_IMAGE_EX_PROTOCOL (Structure):
  pass

EFI_HII_NEW_IMAGE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_EX_PROTOCOL),   # IN CONST  *This,
  EFI_HII_HANDLE,                       # IN         PackageList,
  POINTER(EFI_IMAGE_ID),                # OUT        *ImageId,
  POINTER(EFI_IMAGE_INPUT)              # IN CONST   *Image
  )

EFI_HII_GET_IMAGE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_EX_PROTOCOL),   #   IN CONST  *This,
  EFI_HII_HANDLE,                       #   IN        PackageList,
  EFI_IMAGE_ID,                         #   IN        ImageId,
  POINTER(EFI_IMAGE_INPUT)              #   OUT       *Image
  )

EFI_HII_SET_IMAGE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_EX_PROTOCOL),   #   IN CONST  *This,
  EFI_HII_HANDLE,                       #   IN        PackageList,
  EFI_IMAGE_ID,                         #   IN        ImageId,
  POINTER(EFI_IMAGE_INPUT)              #   IN CONST  *Image
  )

EFI_HII_DRAW_IMAGE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_EX_PROTOCOL),   #   IN CONST  *This,
  EFI_HII_DRAW_FLAGS,                   #   IN        Flags,
  POINTER(EFI_IMAGE_INPUT),             #   IN CONST  *Image,
  POINTER(POINTER(EFI_IMAGE_OUTPUT)),   #   IN OUT    **Blt,
  UINTN,                                #   IN        BltX,
  UINTN                                 #   IN        BltY
  )

EFI_HII_DRAW_IMAGE_ID_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_EX_PROTOCOL),   #   IN CONST  *This,
  EFI_HII_DRAW_FLAGS,                   #   IN        Flags,
  EFI_HII_HANDLE,                       #   IN        PackageList,
  EFI_IMAGE_ID,                         #   IN        ImageId,
  POINTER(POINTER(EFI_IMAGE_OUTPUT)),   #   IN OUT    **Blt,
  UINTN,                                #   IN        BltX,
  UINTN                                 #   IN        BltY
  )

EFI_HII_GET_IMAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_EX_PROTOCOL),   #   IN CONST  *This,
  EFI_HII_HANDLE,                       #   IN        PackageList,
  EFI_IMAGE_ID,                         #   IN        ImageId,
  POINTER(EFI_IMAGE_OUTPUT)             #   OUT       *Image,
  )

EFI_HII_IMAGE_EX_PROTOCOL._fields_ = [
    ("NewImageEx",      EFI_HII_NEW_IMAGE_EX),
    ("GetImageEx",      EFI_HII_GET_IMAGE_EX),
    ("SetImageEx",      EFI_HII_SET_IMAGE_EX),
    ("DrawImageEx",     EFI_HII_DRAW_IMAGE_EX),
    ("DrawImageIdEx",   EFI_HII_DRAW_IMAGE_ID_EX),
    ("GetImageInfo",    EFI_HII_GET_IMAGE_INFO)
  ]

