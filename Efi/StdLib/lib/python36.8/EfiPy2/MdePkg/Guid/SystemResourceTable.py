# SystemResourceTable.py
#
# EfiPy2.MdePkg.Guid.SystemResourceTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSystemResourceTableGuid = \
  EFI_GUID (0xb122a263, 0x3661, 0x4f68, (0x99, 0x29, 0x78, 0xf8, 0xb0, 0xd6, 0x21, 0x80 ))

EFI_SYSTEM_RESOURCE_TABLE_FIRMWARE_RESOURCE_VERSION  = 1

ESRT_FW_TYPE_UNKNOWN         = 0x00000000
ESRT_FW_TYPE_SYSTEMFIRMWARE  = 0x00000001
ESRT_FW_TYPE_DEVICEFIRMWARE  = 0x00000002
ESRT_FW_TYPE_UEFIDRIVER      = 0x00000003

LAST_ATTEMPT_STATUS_SUCCESS                         = 0x00000000
LAST_ATTEMPT_STATUS_ERROR_UNSUCCESSFUL              = 0x00000001
LAST_ATTEMPT_STATUS_ERROR_INSUFFICIENT_RESOURCES    = 0x00000002
LAST_ATTEMPT_STATUS_ERROR_INCORRECT_VERSION         = 0x00000003
LAST_ATTEMPT_STATUS_ERROR_INVALID_FORMAT            = 0x00000004
LAST_ATTEMPT_STATUS_ERROR_AUTH_ERROR                = 0x00000005
LAST_ATTEMPT_STATUS_ERROR_PWR_EVT_AC                = 0x00000006
LAST_ATTEMPT_STATUS_ERROR_PWR_EVT_BATT              = 0x00000007
LAST_ATTEMPT_STATUS_ERROR_UNSATISFIED_DEPENDENCIES  = 0x00000008

class EFI_SYSTEM_RESOURCE_ENTRY (Structure):
  _fields_ = [
    ("FwClass",                   EFI_GUID),
    ("FwType",                    UINT32),
    ("FwVersion",                 UINT32),
    ("LowestSupportedFwVersion",  UINT32),
    ("CapsuleFlags",              UINT32),
    ("LastAttemptVersion",        UINT32),
    ("LastAttemptStatus",         UINT32)
  ]

class EFI_SYSTEM_RESOURCE_TABLE (Structure):
  _fields_ = [
    ("FwResourceCount",     UINT32),
    ("FwResourceCountMax",  UINT32),
    ("FwResourceVersion",   UINT64)
    # ("Entries",             EFI_SYSTEM_RESOURCE_ENTRY * N)
  ]

