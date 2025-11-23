# HiiImage.py
#
# EfiPy2.MdePkg.Protocol.HiiImage
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2         import *
from EfiPy2.MdePkg.Protocol.GraphicsOutput import \
            EFI_GRAPHICS_OUTPUT_BLT_PIXEL,  \
            EFI_GRAPHICS_OUTPUT_PROTOCOL

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import \
        EFI_HII_HANDLE, \
        EFI_IMAGE_ID

gEfiHiiImageProtocolGuid  = \
  EFI_GUID (0x31a6406a, 0x6bdf, 0x4e46, ( 0xb2, 0xa2, 0xeb, 0xaa, 0x89, 0xc4, 0x9, 0x20 ))

class EFI_HII_IMAGE_PROTOCOL (Structure):
  pass

EFI_IMAGE_TRANSPARENT = 0x00000001

class EFI_IMAGE_INPUT (Structure):
  _fields_ = [
    ("Flags;  ", UINT32),
    ("Width;  ", UINT16),
    ("Height; ", UINT16),
    ("Bitmap; ", POINTER(EFI_GRAPHICS_OUTPUT_BLT_PIXEL))
  ]

EFI_HII_NEW_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_PROTOCOL),  # IN       *This
  EFI_HII_HANDLE,                   # IN       PackageList,
  POINTER(EFI_IMAGE_ID),            # OUT      *ImageId,
  POINTER(EFI_IMAGE_INPUT)          # IN CONST *Image
  )

EFI_HII_GET_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_PROTOCOL),  # IN  *This
  EFI_HII_HANDLE,                   # IN  PackageList,
  EFI_IMAGE_ID,                     # IN  ImageId,
  POINTER(EFI_IMAGE_INPUT)          # OUT *Image
  )

EFI_HII_SET_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_PROTOCOL),  # IN        *This
  EFI_HII_HANDLE,                   # IN        PackageList,
  EFI_IMAGE_ID,                     # IN        ImageId,
  POINTER(EFI_IMAGE_INPUT)          # IN CONST  *Image
  )

EFI_HII_DRAW_FLAGS  = UINT32

EFI_HII_DRAW_FLAG_CLIP          = 0x00000001
EFI_HII_DRAW_FLAG_TRANSPARENT   = 0x00000030
EFI_HII_DRAW_FLAG_DEFAULT       = 0x00000000
EFI_HII_DRAW_FLAG_FORCE_TRANS   = 0x00000010
EFI_HII_DRAW_FLAG_FORCE_OPAQUE  = 0x00000020
EFI_HII_DIRECT_TO_SCREEN        = 0x00000080

class EFI_IMAGE_OUTPUT_Image (Union):
  _fields_ = [
    ("Bitmap", POINTER(EFI_GRAPHICS_OUTPUT_BLT_PIXEL)),
    ("Screen", POINTER(EFI_GRAPHICS_OUTPUT_PROTOCOL))
  ]

class EFI_IMAGE_OUTPUT (Structure):
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Image",   EFI_IMAGE_OUTPUT_Image)
  ]

EFI_HII_DRAW_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_PROTOCOL),    # IN        *This
  EFI_HII_DRAW_FLAGS,                 # IN        Flags,
  POINTER(EFI_IMAGE_INPUT),           # IN CONST  *Image,
  POINTER(POINTER(EFI_IMAGE_OUTPUT)), # IN OUT    **Blt,
  UINTN,                              # IN        BltX,
  UINTN                               # IN        BltY
  )

EFI_HII_DRAW_IMAGE_ID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_PROTOCOL),    # IN        *This
  EFI_HII_DRAW_FLAGS,                 # IN        Flags,
  EFI_HII_HANDLE,                     # IN        PackageList,
  EFI_IMAGE_ID,                       # IN        ImageId,
  POINTER(POINTER(EFI_IMAGE_OUTPUT)), # IN OUT    **Blt,
  UINTN,                              # IN        BltX,
  UINTN                               # IN        BltY
  )

EFI_HII_IMAGE_PROTOCOL._fields_ = [
    ("NewImage",    EFI_HII_NEW_IMAGE),
    ("GetImage",    EFI_HII_GET_IMAGE),
    ("SetImage",    EFI_HII_SET_IMAGE),
    ("DrawImage",   EFI_HII_DRAW_IMAGE),
    ("DrawImageId", EFI_HII_DRAW_IMAGE_ID)
  ]

