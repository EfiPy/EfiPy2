# Bmp.py
#
# EfiPy2.MdePkg.IndustryStandard.Bmp
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class BMP_COLOR_MAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Blue",      UINT8),
    ("Green",     UINT8),
    ("Red",       UINT8),
    ("Reserved",  UINT8)
  ]

class BMP_IMAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CharB",           CHAR8),
    ("CharM",           CHAR8),
    ("Size",            UINT32),
    ("Reserved",        UINT16 * 2),
    ("ImageOffset",     UINT32),
    ("HeaderSize",      UINT32),
    ("PixelWidth",      UINT32),
    ("PixelHeight",     UINT32),
    ("Planes",          UINT16),
    ("BitPerPixel",     UINT16),
    ("CompressionType", UINT32),
    ("ImageSize",       UINT32),
    ("XPixelsPerMeter", UINT32),
    ("YPixelsPerMeter", UINT32),
    ("NumberOfColors",  UINT32),
    ("ImportantColors", UINT32)
  ]
