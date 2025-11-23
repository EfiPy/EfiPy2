# CapsuleReport.py
#
# EfiPy2.MdePkg.Guid.CapsuleReport
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiCapsuleReportGuid = \
  EFI_GUID (0x39b68c46, 0xf7fb, 0x441b, ( 0xb6, 0xec, 0x16, 0xb0, 0xf6, 0x98, 0x21, 0xf3 ))

class EFI_CAPSULE_RESULT_VARIABLE_HEADER (Structure):
  _fields_ = [
    ("VariableTotalSize",   UINT32),
    ("Reserved",            UINT32),
    ("CapsuleGuid",         EFI_GUID),
    ("CapsuleProcessed",    EFI_TIME),
    ("CapsuleStatus",       EFI_STATUS)
  ]

class EFI_CAPSULE_RESULT_VARIABLE_FMP (Structure):
  _fields_ = [
    ("Version",             UINT16),
    ("PayloadIndex",        UINT8),
    ("UpdateImageIndex",    UINT8),
    ("UpdateImageTypeId",   EFI_GUID)
    # ("CapsuleFileName",     CHAR16 * N),
    # ("CapsuleTarget",       CHAR16 * N)
  ]

class EFI_CAPSULE_RESULT_VARIABLE_JSON (Structure):
  _fields_ = [
    ("Version",     UINT32),
    ("CapsuleId",   UINT32),
    ("RespLength",  UINT32),
    ("Resp",        UINT8 * 0)
  ]

