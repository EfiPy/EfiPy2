# Svsm.py
#
# EfiPy2.MdePkg.Register.Amd.Svsm
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
# 
from EfiPy2  import *

class SVSM_INFORMATION (Structure):
  _pack_   = 1
  _fields_ = [
  ("Reserved1",         UINT8 * 320),
  ("SvsmBase",          UINT64),
  ("SvsmSize",          UINT64),
  ("SvsmCaa",           UINT64),
  ("SvsmMaxVersion",    UINT32),
  ("SvsmGuestVmpl",     UINT8),
  ("Reserved2",         UINT8 * 3)
  ]

class SVSM_CAA (Structure):
  _pack_   = 1
  _fields_ = [
  ("SvsmCallPending",   UINT8),
  ("SvsmMemAvailable",  UINT8),
  ("Reserved1",         UINT8 * 6),
  ("SvsmBuffer",        UINT8 * (SIZE_4KB - 8))
  ]

SVSM_SUCCESS                   = 0x00000000
SVSM_ERR_INCOMPLETE            = 0x80000000
SVSM_ERR_UNSUPPORTED_PROTOCOL  = 0x80000001
SVSM_ERR_UNSUPPORTED_CALL      = 0x80000002
SVSM_ERR_INVALID_ADDRESS       = 0x80000003
SVSM_ERR_INVALID_FORMAT        = 0x80000004
SVSM_ERR_INVALID_PARAMETER     = 0x80000005
SVSM_ERR_INVALID_REQUEST       = 0x80000006
SVSM_ERR_BUSY                  = 0x80000007

SVSM_ERR_PVALIDATE_FAIL_INPUT          = 0x80001001
SVSM_ERR_PVALIDATE_FAIL_SIZE_MISMATCH  = 0x80001006
SVSM_ERR_PVALIDATE_FAIL_NO_CHANGE      = 0x80001010

class SVSM_PVALIDATE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
  ("Entries",   UINT16),
  ("Next",      UINT16),
  ("Reserved",  UINT8 * 4)
  ]

class SVSM_PVALIDATE_ENTRY_Bits (Structure):
  _pack_   = 1
  _fields_ = [
  ("PageSize",    UINT64, 2),
  ("Action",      UINT64, 1),
  ("IgnoreCf",    UINT64, 1),
  ("Reserved_2",  UINT64, 8),
  ("Address",     UINT64, 52)
  ]
class SVSM_PVALIDATE_ENTRY (Union):
  _fields_ = [
  ("Bits",      SVSM_PVALIDATE_ENTRY_Bits ),
  ("Uint64",    UINT64)
  ]

class SVSM_PVALIDATE_REQUEST (Structure):
  _pack_   = 1
  _fields_ = [
  ("Header",    SVSM_PVALIDATE_HEADER)
  # ("Entry",     SVSM_PVALIDATE_ENTRY * N)
  ]

class SVSM_REQUEST (Union):
  _pack_   = 1
  _fields_ = [
  ("PvalidateRequest",    SVSM_PVALIDATE_REQUEST)
  ]

class SVSM_FUNCTION_Bits (Structure):
  _pack_   = 1
  _fields_ = [
  ("CallId",    UINT32),
  ("Protocol",  UINT32)
  ]
class SVSM_FUNCTION (Union):
  _pack_   = 1
  _fields_ = [
  ("Id",        SVSM_FUNCTION_Bits),
  ("Uint64",    UINT64)
  ]

