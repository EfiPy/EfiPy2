# UgaDraw.py
#
# EfiPy2.MdePkg.Protocol.UgaDraw
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiUgaDrawProtocolGuid  = \
  EFI_GUID (0x982c298b, 0xf4fa, 0x41cb, (0xb8, 0x38, 0x77, 0xaa, 0x68, 0x8f, 0xb8, 0x39 ))

class EFI_UGA_DRAW_PROTOCOL (Structure):
  pass

EFI_UGA_DRAW_PROTOCOL_GET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_DRAW_PROTOCOL), # IN      *This
  POINTER(UINT32),                #     OUT *HorizontalResolution,
  POINTER(UINT32),                #     OUT *VerticalResolution,
  POINTER(UINT32),                #     OUT *ColorDepth,
  POINTER(UINT32)                 #     OUT *RefreshRate
  )

EFI_UGA_DRAW_PROTOCOL_SET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_DRAW_PROTOCOL), # IN  *This
  UINT32,                         # IN  HorizontalResolution,
  UINT32,                         # IN  VerticalResolution,
  UINT32,                         # IN  ColorDepth,
  UINT32                          # IN  RefreshRate
  )

class EFI_UGA_PIXEL (Structure):
  _fields_ = [
    ("Blue",      UINT8),
    ("Green",     UINT8),
    ("Red",       UINT8),
    ("Reserved",  UINT8)
  ]

class EFI_UGA_PIXEL_UNION (Union):
  _fields_ = [
    ("Pixel", EFI_UGA_PIXEL),
    ("Raw",   UINT32)
  ]

EfiUgaVideoFill         = 0
EfiUgaVideoToBltBuffer  = 1
EfiUgaBltBufferToVideo  = 2
EfiUgaVideoToVideo      = 3
EfiUgaBltMax            = 4
EFI_UGA_BLT_OPERATION   = ENUM

EFI_UGA_DRAW_PROTOCOL_BLT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_DRAW_PROTOCOL), # IN  *This
  POINTER(EFI_UGA_PIXEL),         # IN  * BltBuffer, OPTIONAL
  EFI_UGA_BLT_OPERATION,          # IN  BltOperation,
  UINTN,                          # IN  SourceX,
  UINTN,                          # IN  SourceY,
  UINTN,                          # IN  DestinationX,
  UINTN,                          # IN  DestinationY,
  UINTN,                          # IN  Width,
  UINTN,                          # IN  Height,
  UINTN                           # IN  Delta         OPTIONAL
  )

EFI_UGA_DRAW_PROTOCOL._fields_ = [
    ("GetMode", EFI_UGA_DRAW_PROTOCOL_GET_MODE),
    ("SetMode", EFI_UGA_DRAW_PROTOCOL_SET_MODE),
    ("Blt",     EFI_UGA_DRAW_PROTOCOL_BLT)
  ]

