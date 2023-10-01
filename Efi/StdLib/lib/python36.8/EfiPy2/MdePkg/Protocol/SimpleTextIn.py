# SimpleTextIn.py
#
# EfiPy2.MdePkg.Protocol.SimpleTextIn
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiSimpleTextInProtocolGuid = EFI_GUID( 0x387477c1, 0x69c7, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b))

class EFI_SIMPLE_TEXT_INPUT_PROTOCOL (Structure):
  pass

class EFI_INPUT_KEY (Structure):
  _fields_ = [
    ("ScanCode",    UINT16),
    ("UnicodeChar", CHAR16)
    ]

CHAR_NULL             = 0x0000
CHAR_BACKSPACE        = 0x0008
CHAR_TAB              = 0x0009
CHAR_LINEFEED         = 0x000A
CHAR_CARRIAGE_RETURN  = 0x000D

SCAN_NULL       = 0x0000
SCAN_UP         = 0x0001
SCAN_DOWN       = 0x0002
SCAN_RIGHT      = 0x0003
SCAN_LEFT       = 0x0004
SCAN_HOME       = 0x0005
SCAN_END        = 0x0006
SCAN_INSERT     = 0x0007
SCAN_DELETE     = 0x0008
SCAN_PAGE_UP    = 0x0009
SCAN_PAGE_DOWN  = 0x000A
SCAN_F1         = 0x000B
SCAN_F2         = 0x000C
SCAN_F3         = 0x000D
SCAN_F4         = 0x000E
SCAN_F5         = 0x000F
SCAN_F6         = 0x0010
SCAN_F7         = 0x0011
SCAN_F8         = 0x0012
SCAN_F9         = 0x0013
SCAN_F10        = 0x0014
SCAN_ESC        = 0x0017

EFI_INPUT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_PROTOCOL),  # IN *This
  BOOLEAN                                   # IN ExtendedVerification
  )

EFI_INPUT_READ_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_PROTOCOL),  # IN  *This
  POINTER(EFI_INPUT_KEY)                    # OUT *Key
  )

EFI_SIMPLE_TEXT_INPUT_PROTOCOL._fields_ = [
  ("Reset",         EFI_INPUT_RESET),
  ("ReadKeyStroke", EFI_INPUT_READ_KEY),
  ("WaitForKey",    EFI_EVENT)
  ]

