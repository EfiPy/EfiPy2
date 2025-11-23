# HiiImageDecoder.py
#
# EfiPy2.MdePkg.Protocol.HiiImageDecoder
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.HiiImage import EFI_IMAGE_OUTPUT

gEfiHiiImageDecoderProtocolGuid = \
  EFI_GUID (0x9e66f251, 0x727c, 0x418c, ( 0xbf, 0xd6, 0xc2, 0xb4, 0x25, 0x28, 0x18, 0xea ))

gEfiHiiImageDecoderNameJpegGuid = \
  EFI_GUID (0xefefd093, 0xd9b, 0x46eb,  ( 0xa8, 0x56, 0x48, 0x35, 0x7, 0x0, 0xc9, 0x8 ))

gEfiHiiImageDecoderNamePngGuid = \
  EFI_GUID (0xaf060190, 0x5e3a, 0x4025, ( 0xaf, 0xbd, 0xe1, 0xf9, 0x5, 0xbf, 0xaa, 0x4c ))

class EFI_HII_IMAGE_DECODER_PROTOCOL (Structure):
  pass

EFI_HII_IMAGE_DECODER_COLOR_TYPE_RGB     = 0x0
EFI_HII_IMAGE_DECODER_COLOR_TYPE_RGBA    = 0x1
EFI_HII_IMAGE_DECODER_COLOR_TYPE_CMYK    = 0x2
EFI_HII_IMAGE_DECODER_COLOR_TYPE_UNKNOWN = 0xFF
EFI_HII_IMAGE_DECODER_COLOR_TYPE         = ENUM

class EFI_HII_IMAGE_DECODER_IMAGE_INFO_HEADER (Structure):
  _fields_ = [
    ("DecoderName",         EFI_GUID),
    ("ImageInfoSize",       UINT16),
    ("ImageWidth",          UINT16),
    ("ImageHeight",         UINT16),
    ("ColorType",           EFI_HII_IMAGE_DECODER_COLOR_TYPE),
    ("ColorDepthInBits",    UINT8)
  ]

EFI_IMAGE_JPEG_SCANTYPE_PROGREESSIVE  = 0x01
EFI_IMAGE_JPEG_SCANTYPE_INTERLACED    = 0x02

class EFI_HII_IMAGE_DECODER_JPEG_INFO (Structure):
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_DECODER_IMAGE_INFO_HEADER),
    ("ScanType",    UINT16),
    ("Reserved",    UINT64)
  ]

class EFI_HII_IMAGE_DECODER_PNG_INFO (Structure):
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_DECODER_IMAGE_INFO_HEADER),
    ("Channels",    UINT16),
    ("Reserved",    UINT64)
  ]

class EFI_HII_IMAGE_DECODER_OTHER_INFO (Structure):
  _fields_ = [
    ("Header",          EFI_HII_IMAGE_DECODER_IMAGE_INFO_HEADER),
    ("ImageExtenion",   CHAR16 * 1)
  ]

EFI_HII_IMAGE_DECODER_GET_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_DECODER_PROTOCOL),  # IN      *This
  POINTER(POINTER(EFI_GUID)),               # IN OUT  **DecoderName,
  POINTER(UINT16)                           # IN OUT  *NumberOfDecoderName
  )

EFI_HII_IMAGE_DECODER_GET_IMAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_DECODER_PROTOCOL),                  # IN      *This
  PVOID,                                                    # IN      *Image,
  UINTN,                                                    # IN      SizeOfImage,
  POINTER(POINTER(EFI_HII_IMAGE_DECODER_IMAGE_INFO_HEADER)) # IN OUT  **ImageInfo
  )

EFI_HII_IMAGE_DECODER_DECODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_IMAGE_DECODER_PROTOCOL),  # IN      *This
  PVOID,                                    # IN      *Image,
  UINTN,                                    # IN      ImageRawDataSize,
  POINTER(POINTER(EFI_IMAGE_OUTPUT)),       # IN OUT  **Bitmap,
  BOOLEAN                                   # IN      Transparent
  )

EFI_HII_IMAGE_DECODER_PROTOCOL._fields_ = [
    ("GetImageDecoderName", EFI_HII_IMAGE_DECODER_GET_NAME),
    ("GetImageInfo",        EFI_HII_IMAGE_DECODER_GET_IMAGE_INFO),
    ("DecodeImage",         EFI_HII_IMAGE_DECODER_DECODE)
  ]

