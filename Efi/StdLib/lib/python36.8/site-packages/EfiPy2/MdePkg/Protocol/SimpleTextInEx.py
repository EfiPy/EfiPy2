# SimpleTextInEx.py
#
# EfiPy2.MdePkg.Protocol.SimpleTextInEx
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY

gEfiSimpleTextInputExProtocolGuid = \
  EFI_GUID (0xdd9e7534, 0x7762, 0x4698, ( 0x8c, 0x14, 0xf5, 0x85, 0x17, 0xa6, 0x25, 0xaa ))

class EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL (Structure):
  pass

EFI_INPUT_RESET_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL), # IN *This
  BOOLEAN                                     # IN ExtendedVerification
  )

EFI_KEY_TOGGLE_STATE  = UINT8

class EFI_KEY_STATE (Structure):
  _fields_ = [
    ("KeyShiftState",   UINT32),
    ("KeyToggleState",  EFI_KEY_TOGGLE_STATE)
  ]

class EFI_KEY_DATA (Structure):
  _fields_ = [
    ("Key",       EFI_INPUT_KEY),
    ("KeyState",  EFI_KEY_STATE)
  ]

EFI_SHIFT_STATE_VALID     = 0x80000000
EFI_RIGHT_SHIFT_PRESSED   = 0x00000001
EFI_LEFT_SHIFT_PRESSED    = 0x00000002
EFI_RIGHT_CONTROL_PRESSED = 0x00000004
EFI_LEFT_CONTROL_PRESSED  = 0x00000008
EFI_RIGHT_ALT_PRESSED     = 0x00000010
EFI_LEFT_ALT_PRESSED      = 0x00000020
EFI_RIGHT_LOGO_PRESSED    = 0x00000040
EFI_LEFT_LOGO_PRESSED     = 0x00000080
EFI_MENU_KEY_PRESSED      = 0x00000100
EFI_SYS_REQ_PRESSED       = 0x00000200

EFI_TOGGLE_STATE_VALID    = 0x80
EFI_KEY_STATE_EXPOSED     = 0x40
EFI_SCROLL_LOCK_ACTIVE    = 0x01
EFI_NUM_LOCK_ACTIVE       = 0x02
EFI_CAPS_LOCK_ACTIVE      = 0x04

SCAN_F11                  = 0x0015
SCAN_F12                  = 0x0016
SCAN_PAUSE                = 0x0048
SCAN_F13                  = 0x0068
SCAN_F14                  = 0x0069
SCAN_F15                  = 0x006A
SCAN_F16                  = 0x006B
SCAN_F17                  = 0x006C
SCAN_F18                  = 0x006D
SCAN_F19                  = 0x006E
SCAN_F20                  = 0x006F
SCAN_F21                  = 0x0070
SCAN_F22                  = 0x0071
SCAN_F23                  = 0x0072
SCAN_F24                  = 0x0073
SCAN_MUTE                 = 0x007F
SCAN_VOLUME_UP            = 0x0080
SCAN_VOLUME_DOWN          = 0x0081
SCAN_BRIGHTNESS_UP        = 0x0100
SCAN_BRIGHTNESS_DOWN      = 0x0101
SCAN_SUSPEND              = 0x0102
SCAN_HIBERNATE            = 0x0103
SCAN_TOGGLE_DISPLAY       = 0x0104
SCAN_RECOVERY             = 0x0105
SCAN_EJECT                = 0x0106

EFI_INPUT_READ_KEY_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL), # IN  *This
  POINTER(EFI_KEY_DATA)                       # OUT *KeyData
  )

EFI_SET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL), # IN  *This
  POINTER(EFI_KEY_TOGGLE_STATE)               # IN  *KeyToggleState
  )

EFI_KEY_NOTIFY_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_KEY_DATA)                 # IN  *EFI_KEY_DATA
  )

EFI_REGISTER_KEYSTROKE_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL), # IN  *This
  POINTER(EFI_KEY_DATA),                      # OUT *KeyData
  EFI_KEY_NOTIFY_FUNCTION,                    # IN  KeyNotificationFunction
  POINTER(PVOID)                              # OUT **NotifyHandle
  )

EFI_UNREGISTER_KEYSTROKE_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL), # IN  *This
  PVOID                                       # IN  *NotificationHandle
  )

EFI_SIMPLE_TEXT_INPUT_EX_PROTOCOL._fields_ = [
    ("Reset",               EFI_INPUT_RESET_EX),
    ("ReadKeyStrokeEx",     EFI_INPUT_READ_KEY_EX),
    ("WaitForKeyEx",        EFI_EVENT),
    ("SetState",            EFI_SET_STATE),
    ("RegisterKeyNotify",   EFI_REGISTER_KEYSTROKE_NOTIFY),
    ("UnregisterKeyNotify", EFI_UNREGISTER_KEYSTROKE_NOTIFY)
  ]

