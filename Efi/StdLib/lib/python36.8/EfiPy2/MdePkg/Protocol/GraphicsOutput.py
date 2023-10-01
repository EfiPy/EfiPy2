# GraphicsOutput.py
#
# EfiPy2.MdePkg.Protocol.GraphicsOutput
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.Uefi.UefiBaseType   import *
from EfiPy2.MdePkg.Uefi.UefiSpec       import *

gEfiGraphicsOutputProtocolGuid  = \
  EFI_GUID (0x9042a9de, 0x23dc, 0x4a38, (0x96, 0xfb, 0x7a, 0xde, 0xd0, 0x80, 0x51, 0x6a ))

class EFI_GRAPHICS_OUTPUT_PROTOCOL (Structure):
  pass

class EFI_PIXEL_BITMASK (Structure):
  _fields_ = [
    ("RedMask",       UINT32),
    ("GreenMask",     UINT32),
    ("BlueMask",      UINT32),
    ("ReservedMask",  UINT32)
  ]

PixelRedGreenBlueReserved8BitPerColor   = 0
PixelBlueGreenRedReserved8BitPerColor   = 1
PixelBitMask                            = 2
PixelBltOnly                            = 3
PixelFormatMax                          = 4
EFI_GRAPHICS_PIXEL_FORMAT               = ENUM

class EFI_GRAPHICS_OUTPUT_MODE_INFORMATION (Structure):
  _fields_ = [
    ("Version",               UINT32),
    ("HorizontalResolution",  UINT32),
    ("VerticalResolution",    UINT32),
    ("PixelFormat",           EFI_GRAPHICS_PIXEL_FORMAT),
    ("PixelInformation",      EFI_PIXEL_BITMASK),
    ("PixelsPerScanLine",     UINT32)
  ]

EFI_GRAPHICS_OUTPUT_PROTOCOL_QUERY_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GRAPHICS_OUTPUT_PROTOCOL),                  # IN  *This
  UINT32,                                                 # IN  ModeNumber
  POINTER(UINTN),                                         # OUT *SizeOfInfo
  POINTER(POINTER(EFI_GRAPHICS_OUTPUT_MODE_INFORMATION))  # OUT **Info
  )

EFI_GRAPHICS_OUTPUT_PROTOCOL_SET_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GRAPHICS_OUTPUT_PROTOCOL),  # IN  *This
  UINT32                                  # IN  ModeNumber
  )

class EFI_GRAPHICS_OUTPUT_BLT_PIXEL (Structure):
  _fields_ = [
    ("Blue",      UINT8),
    ("Green",     UINT8),
    ("Red",       UINT8),
    ("Reserved",  UINT8)
  ]

class EFI_GRAPHICS_OUTPUT_BLT_PIXEL_UNION (Union):
  _fields_ = [
    ("Pixel", EFI_GRAPHICS_OUTPUT_BLT_PIXEL),
    ("Raw",   UINT32)
  ]

EfiBltVideoFill                   = 0
EfiBltVideoToBltBuffer            = 1
EfiBltBufferToVideo               = 2
EfiBltVideoToVideo                = 3
EfiGraphicsOutputBltOperationMax  = 4
EFI_GRAPHICS_OUTPUT_BLT_OPERATION = ENUM

EFI_GRAPHICS_OUTPUT_PROTOCOL_BLT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GRAPHICS_OUTPUT_PROTOCOL),  # IN *This
  POINTER(EFI_GRAPHICS_OUTPUT_BLT_PIXEL), # IN *BltBuffer,   OPTIONAL
  EFI_GRAPHICS_OUTPUT_BLT_OPERATION,      # IN BltOperation,
  UINTN,                                  # IN SourceX,
  UINTN,                                  # IN SourceY,
  UINTN,                                  # IN DestinationX,
  UINTN,                                  # IN DestinationY,
  UINTN,                                  # IN Width,
  UINTN,                                  # IN Height,
  UINTN                                   # IN Delta         OPTIONAL
  )

class EFI_GRAPHICS_OUTPUT_PROTOCOL_MODE (Structure):
  _fields_ = [
    ("MaxMode",         UINT32),
    ("Mode",            UINT32),
    ("Info",            POINTER(EFI_GRAPHICS_OUTPUT_MODE_INFORMATION)),
    ("SizeOfInfo",      UINTN),
    ("FrameBufferBase", EFI_PHYSICAL_ADDRESS),
    ("FrameBufferSize", UINTN)
  ]

EFI_GRAPHICS_OUTPUT_PROTOCOL._fields_ = [
    ("QueryMode", EFI_GRAPHICS_OUTPUT_PROTOCOL_QUERY_MODE),
    ("SetMode",   EFI_GRAPHICS_OUTPUT_PROTOCOL_SET_MODE),
    ("Blt",       EFI_GRAPHICS_OUTPUT_PROTOCOL_BLT),
    ("Mode",      POINTER(EFI_GRAPHICS_OUTPUT_PROTOCOL_MODE))
  ]

