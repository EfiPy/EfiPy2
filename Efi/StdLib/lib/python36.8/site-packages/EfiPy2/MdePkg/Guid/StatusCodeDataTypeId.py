# StatusCodeDataTypeId.py
#
# EfiPy2.MdePkg.Guid.StatusCodeDataTypeId
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import DebugSupport

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import  \
                                    EFI_HII_HANDLE,           \
                                    EFI_STRING_ID

from EfiPy2.MdePkg.Pi.PiStatusCode  import \
            EFI_STATUS_CODE_DATA

gEfiStatusCodeDataTypeStringGuid  = \
  EFI_GUID (0x92D11080, 0x496F, 0x4D95, ( 0xBE, 0x7E, 0x03, 0x74, 0x88, 0x38, 0x2B, 0x0A ))

EfiStringAscii    = 0
EfiStringUnicode  = 1
EfiStringToken    = 2
EFI_STRING_TYPE   = ENUM

class EFI_STATUS_CODE_STRING_TOKEN (Structure):
  _fields_ = [
    ("Handle",  EFI_HII_HANDLE),
    ("Token",   EFI_STRING_ID)
  ]

class EFI_STATUS_CODE_STRING (Union):
  _fields_ = [
    ("Ascii",   PCHAR8),
    ("Unicode", PCHAR16),
    ("Hii",     EFI_STATUS_CODE_STRING_TOKEN)
  ]

class EFI_STATUS_CODE_STRING_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("StringType",  EFI_STRING_TYPE),
    ("String",      EFI_STATUS_CODE_STRING)
  ]

gEfiStatusCodeSpecificDataGuid  = \
  EFI_GUID (0x335984bd, 0xe805, 0x409a, ( 0xb8, 0xf8, 0xd2, 0x7e, 0xce, 0x5f, 0xf7, 0xa6 ))

class EFI_DEVICE_PATH_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA)
    # ("DevicePath",  EFI_DEVICE_PATH_PROTOCOL)
  ]

class EFI_DEVICE_HANDLE_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Handle",      EFI_HANDLE)
  ]

class EFI_RESOURCE_ALLOC_FAILURE_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",      EFI_STATUS_CODE_DATA),
    ("Bar",             UINT32),
    ("DevicePathSize",  UINT16),
    ("ReqResSize",      UINT16),
    ("AllocResSize",    UINT16)
    # ("DevicePath",      EFI_DEVICE_PATH_PROTOCOL),
    # ("ReqRes",          UINT8 * N),
    # ("AllocRes",        UINT8 * N)
  ]

class EFI_EXP_BASE10_DATA (Structure):
  _fields_ = [
    ("Value",     INT16),
    ("Exponent",  INT16)
  ]

class EFI_COMPUTING_UNIT_VOLTAGE_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",EFI_STATUS_CODE_DATA),
    ("Voltage",   EFI_EXP_BASE10_DATA),
    ("Threshold", EFI_EXP_BASE10_DATA)
  ]

class EFI_COMPUTING_UNIT_MICROCODE_UPDATE_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",EFI_STATUS_CODE_DATA),
    ("Version",   UINT32)
  ]

class EFI_COMPUTING_UNIT_TIMER_EXPIRED_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("TimerLimit",  EFI_EXP_BASE10_DATA)
  ]

EFI_COMPUTING_UNIT_MISMATCH_SPEED       = 0x0001
EFI_COMPUTING_UNIT_MISMATCH_FSB_SPEED   = 0x0002
EFI_COMPUTING_UNIT_MISMATCH_FAMILY      = 0x0004
EFI_COMPUTING_UNIT_MISMATCH_MODEL       = 0x0008
EFI_COMPUTING_UNIT_MISMATCH_STEPPING    = 0x0010
EFI_COMPUTING_UNIT_MISMATCH_CACHE_SIZE  = 0x0020
EFI_COMPUTING_UNIT_MISMATCH_OEM1        = 0x1000
EFI_COMPUTING_UNIT_MISMATCH_OEM2        = 0x2000
EFI_COMPUTING_UNIT_MISMATCH_OEM3        = 0x4000
EFI_COMPUTING_UNIT_MISMATCH_OEM4        = 0x8000

class EFI_HOST_PROCESSOR_MISMATCH_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Instance",    UINT32),
    ("Attributes",  UINT16)
  ]

class EFI_COMPUTING_UNIT_THERMAL_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Temperature", EFI_EXP_BASE10_DATA),
    ("Threshold",   EFI_EXP_BASE10_DATA)
  ]

EfiInitCacheDataOnly      = 0
EfiInitCacheInstrOnly     = 1
EfiInitCacheBoth          = 2
EfiInitCacheUnspecified   = 3
EFI_INIT_CACHE_TYPE       = ENUM

class EFI_CACHE_INIT_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Level",       UINT32),
    ("Type",        EFI_INIT_CACHE_TYPE)
  ]

EFI_CPU_STATE_CHANGE_CAUSE              = UINT32

EFI_CPU_CAUSE_INTERNAL_ERROR            = 0x0001
EFI_CPU_CAUSE_THERMAL_ERROR             = 0x0002
EFI_CPU_CAUSE_SELFTEST_FAILURE          = 0x0004
EFI_CPU_CAUSE_PREBOOT_TIMEOUT           = 0x0008
EFI_CPU_CAUSE_FAILED_TO_START           = 0x0010
EFI_CPU_CAUSE_CONFIG_ERROR              = 0x0020
EFI_CPU_CAUSE_USER_SELECTION            = 0x0080
EFI_CPU_CAUSE_BY_ASSOCIATION            = 0x0100
EFI_CPU_CAUSE_UNSPECIFIED               = 0x8000

class EFI_COMPUTING_UNIT_CPU_DISABLED_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",        EFI_STATUS_CODE_DATA),
    ("Cause",             UINT32),
    ("SoftwareDisabled",  BOOLEAN)
  ]

EFI_MEMORY_ERROR_GRANULARITY  = UINT8

EFI_MEMORY_ERROR_OTHER      = 0x01
EFI_MEMORY_ERROR_UNKNOWN    = 0x02
EFI_MEMORY_ERROR_DEVICE     = 0x03
EFI_MEMORY_ERROR_PARTITION  = 0x04

EFI_MEMORY_ERROR_OPERATION          = UINT8

EFI_MEMORY_OPERATION_OTHER          = 0x01
EFI_MEMORY_OPERATION_UNKNOWN        = 0x02
EFI_MEMORY_OPERATION_READ           = 0x03
EFI_MEMORY_OPERATION_WRITE          = 0x04
EFI_MEMORY_OPERATION_PARTIAL_WRITE  = 0x05

class EFI_MEMORY_EXTENDED_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Granularity", EFI_MEMORY_ERROR_GRANULARITY),
    ("Operation",   EFI_MEMORY_ERROR_OPERATION),
    ("Syndrome",    UINTN),
    ("Address",     EFI_PHYSICAL_ADDRESS),
    ("Resolution",  UINTN)
  ]

EFI_MULTIPLE_MEMORY_DEVICE_OPERATION = 0xfffe

EFI_ALL_MEMORY_DEVICE_OPERATION = 0xffff

EFI_MULTIPLE_MEMORY_ARRAY_OPERATION = 0xfffe

EFI_ALL_MEMORY_ARRAY_OPERATION = 0xffff

class EFI_STATUS_CODE_DIMM_NUMBER (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Array",       UINT16),
    ("Device",      UINT16)
  ]

class EFI_MEMORY_MODULE_MISMATCH_ERROR_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Instance",    EFI_STATUS_CODE_DIMM_NUMBER)
  ]

class EFI_MEMORY_RANGE_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Start",       EFI_PHYSICAL_ADDRESS),
    ("Length",      EFI_PHYSICAL_ADDRESS)
  ]

class EFI_DEBUG_ASSERT_DATA (Structure):
  _fields_ = [
    ("DataHeader",    EFI_STATUS_CODE_DATA),
    ("LineNumber",    UINT32),
    ("FileNameSize",  UINT32),
    ("FileName",      POINTER(EFI_STATUS_CODE_STRING_DATA))
  ]

class EFI_STATUS_CODE_EXCEP_SYSTEM_CONTEXT (Union):
  _fields_ = [
    ("SystemContextEbc",  DebugSupport.EFI_SYSTEM_CONTEXT_EBC),
    ("SystemContextIa32", DebugSupport.EFI_SYSTEM_CONTEXT_IA32),
    ("SystemContextIpf",  DebugSupport.EFI_SYSTEM_CONTEXT_IPF),
    ("SystemContextX64",  DebugSupport.EFI_SYSTEM_CONTEXT_X64),
    ("SystemContextArm",  DebugSupport.EFI_SYSTEM_CONTEXT_ARM)
  ]

class EFI_STATUS_CODE_EXCEP_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",  EFI_STATUS_CODE_DATA),
    ("Context",     EFI_STATUS_CODE_EXCEP_SYSTEM_CONTEXT)
  ]

class EFI_STATUS_CODE_START_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",          EFI_STATUS_CODE_DATA),
    ("ControllerHandle",    EFI_HANDLE),
    ("DriverBindingHandle", EFI_HANDLE),
    ("DevicePathSize",      UINT16)
    # ("RemainingDevicePath", EFI_DEVICE_PATH_PROTOCOL)
  ]

class EFI_LEGACY_OPROM_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",    EFI_STATUS_CODE_DATA),
    ("DeviceHandle",  EFI_HANDLE),
    ("RomImageBase",  EFI_PHYSICAL_ADDRESS)
  ]

class EFI_RETURN_STATUS_EXTENDED_DATA (Structure):
  _fields_ = [
    ("DataHeader",    EFI_STATUS_CODE_DATA),
    ("ReturnStatus",  EFI_STATUS)
  ]

